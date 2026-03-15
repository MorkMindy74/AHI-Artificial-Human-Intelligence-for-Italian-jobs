"""Parse an ISTAT CP2021 profession detail page into a clean Markdown document."""

import sys
import re
from bs4 import BeautifulSoup


def clean(text):
    """Clean up whitespace from extracted text."""
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def parse_profession_page(html_path):
    """Parse an ISTAT scheda.php page into structured Markdown."""
    with open(html_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    md = []

    # --- Code and Title from header ---
    header = soup.find("div", class_="headred")
    if header:
        header_text = clean(header.get_text())
        # Format: "1.1.1.1.1 - Membri di organismi..."
        m = re.match(r'([\d.]+)\s*-\s*(.*)', header_text)
        if m:
            code = m.group(1)
            title = m.group(2)
            md.append(f"# {code} - {title}")
        else:
            md.append(f"# {header_text}")
    else:
        md.append("# Professione sconosciuta")
    md.append("")

    # --- Classification hierarchy ---
    content_div = soup.find("div", id="content_scheda")
    if content_div:
        hierarchy_items = []
        # Find the left column with the hierarchy
        left_div = content_div.find("div", style=re.compile(r"float:\s*left"))
        if left_div:
            h3_pos = left_div.find("h3", string=re.compile(r"POSIZIONE", re.I))
            if h3_pos:
                pos_text = clean(h3_pos.find_next("td").get_text()) if h3_pos.find_next("td") else ""
                if pos_text and pos_text != clean(h3_pos.get_text()):
                    md.append(f"**Posizione:** {pos_text}")
                    md.append("")

            # Extract hierarchy path from nested tables
            for table in left_div.find_all("table", style=re.compile(r"margin-left")):
                for a in table.find_all("a"):
                    text = clean(a.get_text())
                    if text and not text.startswith("img"):
                        hierarchy_items.append(text)
                # Also check for non-linked text (the final level is not a link)
                for td in table.find_all("td", style=re.compile(r"text-align:\s*justify")):
                    text = clean(td.get_text())
                    if text and text not in hierarchy_items and re.match(r'[\d.]', text):
                        hierarchy_items.append(text)

        if hierarchy_items:
            md.append("## Classificazione")
            md.append("")
            for item in hierarchy_items:
                # Determine indent level by counting dots in code prefix
                code_match = re.match(r'([\d.]+)', item)
                if code_match:
                    level = code_match.group(1).count('.')
                    md.append(f"{'  ' * level}- {item}")
            md.append("")

    # --- Description ---
    desc_p = soup.find("p", class_="black")
    if desc_p:
        description = clean(desc_p.get_text())
        if description:
            md.append("## Descrizione")
            md.append("")
            md.append(description)
            md.append("")

    # --- Examples of professions ---
    examples_h3 = soup.find("h3", string=re.compile(r"ESEMPI DI PROFESSIONI", re.I))
    if examples_h3:
        # Find the UL items after this heading
        examples_container = examples_h3.find_parent("tr")
        if examples_container:
            next_tr = examples_container.find_next_sibling("tr")
            if next_tr:
                examples = []
                for li in next_tr.find_all("li"):
                    text = clean(li.get_text())
                    if text:
                        examples.append(text)
                if examples:
                    md.append("## Esempi di professioni")
                    md.append("")
                    for ex in examples:
                        md.append(f"- {ex}")
                    md.append("")

    # --- Related professions ---
    related_h3 = soup.find("h3", string=re.compile(r"AFFINI.*ALTROVE", re.I))
    if related_h3:
        related_container = related_h3.find_parent("tr")
        if related_container:
            next_tr = related_container.find_next_sibling("tr")
            if next_tr:
                related = []
                for li in next_tr.find_all("li"):
                    text = clean(li.get_text())
                    if text:
                        related.append(text)
                if related:
                    md.append("## Professioni affini classificate altrove")
                    md.append("")
                    for rel in related:
                        md.append(f"- {rel}")
                    md.append("")

    return "\n".join(md)


if __name__ == "__main__":
    html_path = sys.argv[1] if len(sys.argv) > 1 else "html/test.html"
    result = parse_profession_page(html_path)

    out_path = html_path.replace(".html", ".md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(result)
    print(f"Written to {out_path}")
    print()
    print(result)
