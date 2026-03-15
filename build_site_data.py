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
    data = []
    for row in rows:
        slug = row["slug"]
        score = scores.get(slug, {})
        gg = int(row["grande_gruppo"])
        data.append({
            "code": row["code"],
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
        })

    os.makedirs("site", exist_ok=True)
    with open("site/data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)

    print(f"Wrote {len(data)} professions to site/data.json")

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
