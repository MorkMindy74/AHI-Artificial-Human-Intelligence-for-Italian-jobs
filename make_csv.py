"""
Build a CSV summary of all Italian professions from scraped HTML and classification data.

Reads from professioni.json and html/<slug>.html, writes to professioni.csv.

Usage:
    uv run python make_csv.py
"""

import csv
import json
import os
import re
from bs4 import BeautifulSoup


def clean(text):
    return re.sub(r'\s+', ' ', text).strip()


# Education level inferred from Grande Gruppo
EDUCATION_BY_GG = {
    1: "Laurea magistrale o superiore",
    2: "Laurea magistrale o superiore",
    3: "Laurea triennale / Diploma tecnico superiore",
    4: "Diploma di scuola superiore",
    5: "Diploma di scuola superiore / Qualifica professionale",
    6: "Qualifica professionale / Apprendistato",
    7: "Qualifica professionale / Licenza media",
    8: "Nessun titolo specifico",
    9: "Variabile per grado",
}

EDUCATION_EN_BY_GG = {
    1: "Master's degree or higher",
    2: "Master's degree or higher",
    3: "Bachelor's degree / Higher technical diploma",
    4: "High school diploma",
    5: "High school diploma / Vocational qualification",
    6: "Vocational qualification / Apprenticeship",
    7: "Vocational qualification / Middle school",
    8: "No specific qualification",
    9: "Varies by rank",
}


def extract_description(html_path):
    """Extract the description from an ISTAT scheda page."""
    with open(html_path, encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    desc_p = soup.find("p", class_="black")
    if desc_p:
        return clean(desc_p.get_text())
    return ""


def extract_examples(html_path):
    """Extract example profession titles from an ISTAT scheda page."""
    with open(html_path, encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    examples_h3 = soup.find("h3", string=re.compile(r"ESEMPI DI PROFESSIONI", re.I))
    if examples_h3:
        container = examples_h3.find_parent("tr")
        if container:
            next_tr = container.find_next_sibling("tr")
            if next_tr:
                return [clean(li.get_text()) for li in next_tr.find_all("li")
                        if clean(li.get_text())]
    return []


def main():
    with open("professioni.json", encoding="utf-8") as f:
        professioni = json.load(f)

    fieldnames = [
        "code", "title_it", "slug", "grande_gruppo",
        "grande_gruppo_name_it", "gruppo", "classe", "categoria",
        "education_it", "education_en",
        "description", "examples",
        "istat_url", "inapp_url",
    ]

    rows = []
    missing = 0
    for prof in professioni:
        html_path = f"html/{prof['slug']}.html"

        description = ""
        examples = []
        if os.path.exists(html_path):
            description = extract_description(html_path)
            examples = extract_examples(html_path)
        else:
            missing += 1

        gg = prof["grande_gruppo"]
        rows.append({
            "code": prof["code"],
            "title_it": prof["title_it"],
            "slug": prof["slug"],
            "grande_gruppo": gg,
            "grande_gruppo_name_it": prof["grande_gruppo_name_it"],
            "gruppo": prof["gruppo"],
            "classe": prof["classe"],
            "categoria": prof["categoria"],
            "education_it": EDUCATION_BY_GG.get(gg, ""),
            "education_en": EDUCATION_EN_BY_GG.get(gg, ""),
            "description": description,
            "examples": "; ".join(examples),
            "istat_url": prof.get("istat_url", ""),
            "inapp_url": prof.get("inapp_url", ""),
        })

    with open("professioni.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows to professioni.csv (missing HTML: {missing})")

    # Quick sanity check
    with_desc = sum(1 for r in rows if r["description"])
    with_examples = sum(1 for r in rows if r["examples"])
    print(f"With description: {with_desc}/{len(rows)}")
    print(f"With examples: {with_examples}/{len(rows)}")

    print(f"\nSample rows:")
    for r in rows[:3]:
        print(f"  {r['code']} {r['title_it'][:40]}: GG{r['grande_gruppo']}, {r['education_it']}")


if __name__ == "__main__":
    main()
