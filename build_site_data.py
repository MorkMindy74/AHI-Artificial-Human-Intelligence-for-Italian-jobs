"""
Build a compact JSON for the website by merging CSV stats with AI exposure scores.

Reads professioni.csv (for stats) and scores.json (for AI exposure).
Writes site/data.json.

Usage:
    uv run python build_site_data.py
"""

import csv
import json
import os
import glob
from html.parser import HTMLParser


class SimpleHTMLExtractor(HTMLParser):
    """Extract description and examples from ISTAT profession pages."""
    def __init__(self):
        super().__init__()
        self._in_black_p = False
        self._in_h3 = False
        self._in_li = False
        self._after_esempi = False
        self.description = ""
        self.examples = []
        self._current_text = ""

    def handle_starttag(self, tag, attrs):
        attrs_d = dict(attrs)
        if tag == "p" and "black" in attrs_d.get("class", ""):
            self._in_black_p = True
            self._current_text = ""
        elif tag == "h3":
            self._in_h3 = True
            self._current_text = ""
        elif tag == "li" and self._after_esempi:
            self._in_li = True
            self._current_text = ""

    def handle_endtag(self, tag):
        if tag == "p" and self._in_black_p:
            self._in_black_p = False
            if not self.description:
                self.description = self._current_text.strip()
        elif tag == "h3" and self._in_h3:
            self._in_h3 = False
            if "ESEMPI" in self._current_text.upper():
                self._after_esempi = True
        elif tag == "li" and self._in_li:
            self._in_li = False
            ex = self._current_text.strip()
            if ex:
                self.examples.append(ex)
        elif tag == "ul" and self._after_esempi:
            self._after_esempi = False

    def handle_data(self, data):
        if self._in_black_p or self._in_h3 or self._in_li:
            self._current_text += data


def extract_from_html(html_dir, slug):
    """Try to find and extract description + examples for a profession."""
    # Find HTML file matching slug
    pattern = os.path.join(html_dir, slug.replace(".", "-") + "*.html")
    matches = glob.glob(pattern)
    # Also try with the code pattern
    if not matches:
        pattern2 = os.path.join(html_dir, slug[:5].replace(".", "-") + "*.html")
        matches = glob.glob(pattern2)
    if not matches:
        return "", []

    try:
        with open(matches[0], encoding="utf-8") as f:
            html = f.read()
        parser = SimpleHTMLExtractor()
        parser.feed(html)
        return parser.description[:300], parser.examples[:10]
    except Exception:
        return "", []


# Grande Gruppo English names
GG_NAMES_EN = {
    1: "Legislators, entrepreneurs & senior management",
    2: "Intellectual, scientific & highly specialized professions",
    3: "Technical professions",
    4: "Executive office work professions",
    5: "Qualified commercial & service professions",
    6: "Craftspeople, specialized workers & farmers",
    7: "Plant operators, machinery workers & vehicle drivers",
    8: "Unskilled professions",
    9: "Armed forces",
}


def main():
    # Load AI exposure scores
    with open("scores.json", encoding="utf-8") as f:
        scores_list = json.load(f)
    scores = {s["slug"]: s for s in scores_list}

    # Load CSV stats
    with open("professioni.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # Merge
    html_dir = os.path.join(os.path.dirname(__file__), "html")
    data = []
    desc_count = 0
    for row in rows:
        slug = row["slug"]
        code = row["code"]
        score = scores.get(slug, {})
        gg = int(row["grande_gruppo"])

        # Extract description and examples from HTML
        description, examples = extract_from_html(html_dir, slug)
        if description:
            desc_count += 1

        entry = {
            "code": code,
            "title_it": row["title_it"],
            "title_en": score.get("title_en", ""),
            "slug": slug,
            "grande_gruppo": gg,
            "grande_gruppo_name_it": row["grande_gruppo_name_it"],
            "grande_gruppo_name_en": GG_NAMES_EN.get(gg, ""),
            "gruppo": row["gruppo"],
            "classe": row["classe"],
            "categoria": row["categoria"],
            "education_it": row.get("education_it", ""),
            "education_en": row.get("education_en", ""),
            "exposure": score.get("exposure"),
            "exposure_rationale_it": score.get("rationale_it", ""),
            "exposure_rationale_en": score.get("rationale_en", ""),
            "url": row.get("istat_url", ""),
        }
        # Only add description/examples if present (to keep JSON lean)
        if description:
            entry["description"] = description
        if examples:
            entry["examples"] = ", ".join(examples)

        data.append(entry)

    os.makedirs("site", exist_ok=True)
    with open("site/data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)

    print(f"Wrote {len(data)} professions to site/data.json")
    print(f"With description: {desc_count}/{len(data)}")

    scored = sum(1 for d in data if d["exposure"] is not None)
    print(f"With exposure scores: {scored}/{len(data)}")

    # Distribution by GG
    print("\nBy Grande Gruppo:")
    from collections import Counter
    gg_counts = Counter(d["grande_gruppo"] for d in data)
    for gg in sorted(gg_counts):
        gg_scored = [d for d in data if d["grande_gruppo"] == gg and d["exposure"] is not None]
        avg = sum(d["exposure"] for d in gg_scored) / len(gg_scored) if gg_scored else 0
        print(f"  GG{gg} ({GG_NAMES_EN.get(gg, ''):50s}): {gg_counts[gg]:3d} prof, avg={avg:.1f}")


if __name__ == "__main__":
    main()
