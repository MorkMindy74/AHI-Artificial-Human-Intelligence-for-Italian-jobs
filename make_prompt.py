"""
Generate a comprehensive analysis document from all Italian profession data.

Aggregates classification, scoring, and statistics into prompt.md.

Usage:
    uv run python make_prompt.py
"""

import csv
import json


def main():
    with open("professioni.json", encoding="utf-8") as f:
        professioni = json.load(f)

    scores = {}
    try:
        with open("scores.json", encoding="utf-8") as f:
            for entry in json.load(f):
                scores[entry["slug"]] = entry
    except FileNotFoundError:
        pass

    csv_data = {}
    try:
        with open("professioni.csv", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                csv_data[row["slug"]] = row
    except FileNotFoundError:
        pass

    md = []

    md.append("# Esposizione all'IA del Mercato del Lavoro Italiano")
    md.append("")
    md.append("Analisi dell'esposizione all'intelligenza artificiale di 813 professioni")
    md.append("italiane classificate secondo ISTAT CP2021.")
    md.append("")

    md.append("## Metodologia")
    md.append("")
    md.append("Ogni professione e' stata valutata su una scala 0-10 utilizzando Claude (Anthropic),")
    md.append("integrando il framework 'observed exposure' di Anthropic Research.")
    md.append("")
    md.append("| Punteggio | Significato | Esempi |")
    md.append("|-----------|-------------|--------|")
    md.append("| 0-1 | Minima | Muratore, giardiniere, sommozzatore |")
    md.append("| 2-3 | Bassa | Elettricista, idraulico, vigile del fuoco |")
    md.append("| 4-5 | Moderata | Infermiere, poliziotto, veterinario |")
    md.append("| 6-7 | Alta | Insegnante, dirigente, commercialista |")
    md.append("| 8-9 | Molto alta | Sviluppatore software, traduttore, analista dati |")
    md.append("| 10 | Massima | Addetto inserimento dati, operatore telemarketing |")
    md.append("")

    scored = [s for s in scores.values() if "exposure" in s]
    if scored:
        avg = sum(s["exposure"] for s in scored) / len(scored)
        md.append("## Statistiche aggregate")
        md.append("")
        md.append(f"- **Professioni totali:** {len(professioni)}")
        md.append(f"- **Professioni con score:** {len(scored)}")
        md.append(f"- **Media esposizione:** {avg:.1f}/10")
        md.append("")

        by_score = {}
        for s in scored:
            bucket = s["exposure"]
            by_score[bucket] = by_score.get(bucket, 0) + 1
        md.append("### Distribuzione per punteggio")
        md.append("")
        for k in sorted(by_score):
            md.append(f"- **{k}/10:** {by_score[k]} professioni")
        md.append("")

        gg_map = {}
        for p in professioni:
            gg = p["grande_gruppo"]
            if p["slug"] in scores and "exposure" in scores[p["slug"]]:
                if gg not in gg_map:
                    gg_map[gg] = {"name": p["grande_gruppo_name_it"], "sum": 0, "count": 0}
                gg_map[gg]["sum"] += scores[p["slug"]]["exposure"]
                gg_map[gg]["count"] += 1

        md.append("### Media esposizione per Grande Gruppo")
        md.append("")
        md.append("| GG | Nome | Prof. | Media |")
        md.append("|----|------|-------|-------|")
        for gg in sorted(gg_map):
            g = gg_map[gg]
            avg_gg = g["sum"] / g["count"] if g["count"] > 0 else 0
            md.append(f"| {gg} | {g['name'][:50]} | {g['count']} | {avg_gg:.1f} |")
        md.append("")

        tiers = [
            ("Minima (0-1)", 0, 1),
            ("Bassa (2-3)", 2, 3),
            ("Moderata (4-5)", 4, 5),
            ("Alta (6-7)", 6, 7),
            ("Molto alta (8-10)", 8, 10),
        ]
        md.append("### Ripartizione per fascia")
        md.append("")
        md.append("| Fascia | Professioni | % |")
        md.append("|--------|-------------|---|")
        for name, lo, hi in tiers:
            count = sum(1 for s in scored if lo <= s["exposure"] <= hi)
            pct = count / len(scored) * 100
            md.append(f"| {name} | {count} | {pct:.1f}% |")
        md.append("")

    md.append("## Tabella completa")
    md.append("")
    md.append("| Codice | Professione | GG | Esposizione | Rationale |")
    md.append("|--------|-------------|-----|-------------|-----------|")

    sorted_prof = sorted(professioni,
                         key=lambda p: -scores.get(p["slug"], {}).get("exposure", -1))
    for p in sorted_prof:
        s = scores.get(p["slug"], {})
        exp = s.get("exposure", "—")
        rat = s.get("rationale_it", "")[:80]
        md.append(f"| {p['code']} | {p['title_it'][:40]} | {p['grande_gruppo']} | {exp} | {rat} |")

    md.append("")

    with open("prompt.md", "w", encoding="utf-8") as f:
        f.write("\n".join(md))

    print(f"Written prompt.md ({len(md)} lines)")


if __name__ == "__main__":
    main()
