"""
Download the complete ISTAT CP2021 professional classification.

Scrapes the ISTAT classification tree at professioni.istat.it recursively,
extracting all 5 hierarchy levels down to Unità Professionali.

Output: professioni.json — master list of all professional units with hierarchy.

Usage:
    uv run python download_classification.py
    uv run python download_classification.py --force  # re-scrape ignoring cache
"""

import argparse
import json
import os
import re
import time
import httpx
from bs4 import BeautifulSoup

BASE_URL = "https://professioni.istat.it/sistemainformativoprofessioni/cp"
OUTPUT_FILE = "professioni.json"
HIERARCHY_FILE = "classificazione_cp2021.json"

# Delay between requests (be polite)
REQUEST_DELAY = 0.5


def fetch_page(client, params=None):
    """Fetch a classification page and return parsed BeautifulSoup."""
    url = f"{BASE_URL}/index.php"
    resp = client.get(url, params=params, timeout=30)
    resp.raise_for_status()
    return BeautifulSoup(resp.text, "html.parser")


def fetch_scheda(client, code):
    """Fetch an individual profession page (Unità Professionale)."""
    url = f"{BASE_URL}/scheda.php"
    resp = client.get(url, params={"id": code}, timeout=30)
    resp.raise_for_status()
    return BeautifulSoup(resp.text, "html.parser")


def extract_links(soup, level):
    """Extract classification items from page links.

    Returns list of (code, name) tuples for the given level.
    """
    items = []
    # Look for links that contain codice_{level} parameters
    for a in soup.find_all("a", href=True):
        href = a["href"]
        text = re.sub(r'\s+', ' ', a.get_text()).strip()
        if not text:
            continue

        # Match links like index.php?codice_X=...
        # Level 1: codice_1=1
        # Level 2: codice_2=1.1
        # Level 3: codice_3=1.1.1
        # Level 4: codice_4=1.1.1.1
        param_key = f"codice_{level}"
        if param_key in href:
            # Extract the code value
            m = re.search(rf'{param_key}=([\d.]+)', href)
            if m:
                code = m.group(1)
                # Clean up name: remove code prefix if present
                name = re.sub(r'^\d[\d.]*\s*[-–]\s*', '', text).strip()
                if name and code not in [item[0] for item in items]:
                    items.append((code, name))

        # Level 5: links to scheda.php?id=X.X.X.X.X
        if level == 5 and "scheda.php" in href:
            m = re.search(r'id=([\d.]+)', href)
            if m:
                code = m.group(1)
                name = re.sub(r'^\d[\d.]*\s*[-–]\s*', '', text).strip()
                if name and code not in [item[0] for item in items]:
                    items.append((code, name))

    return items


def build_params(codes_by_level):
    """Build URL parameters from a dict of {level: code}."""
    params = {}
    for lvl, code in sorted(codes_by_level.items()):
        params[f"codice_{lvl}"] = code
    return params


def slugify(code, title):
    """Create URL-safe slug from code and title."""
    slug = f"{code.replace('.', '-')}-{title.lower()}"
    slug = re.sub(r'[^a-z0-9-]', '-', slug)
    slug = re.sub(r'-+', '-', slug).strip('-')
    return slug[:80]  # limit length


def scrape_classification(client):
    """Recursively scrape the entire CP2021 classification tree."""

    hierarchy = {
        "grandi_gruppi": [],
        "gruppi": [],
        "classi": [],
        "categorie": [],
        "unita_professionali": []
    }

    # Level 1: Grandi Gruppi
    print("Scaricando Grandi Gruppi (livello 1)...")
    soup = fetch_page(client)
    grandi_gruppi = extract_links(soup, 1)

    if not grandi_gruppi:
        # Fallback: manually define the 9 Grandi Gruppi
        grandi_gruppi = [
            ("1", "Legislatori, imprenditori e alta dirigenza"),
            ("2", "Professioni intellettuali, scientifiche e di elevata specializzazione"),
            ("3", "Professioni tecniche"),
            ("4", "Professioni esecutive nel lavoro d'ufficio"),
            ("5", "Professioni qualificate nelle attività commerciali e nei servizi"),
            ("6", "Artigiani, operai specializzati e agricoltori"),
            ("7", "Conduttori di impianti, operai di macchinari fissi e mobili e conducenti di veicoli"),
            ("8", "Professioni non qualificate"),
            ("9", "Forze armate"),
        ]
        print(f"  Usando lista predefinita: {len(grandi_gruppi)} Grandi Gruppi")
    else:
        print(f"  Trovati {len(grandi_gruppi)} Grandi Gruppi")

    for gg_code, gg_name in grandi_gruppi:
        hierarchy["grandi_gruppi"].append({"code": gg_code, "name": gg_name})

    # Level 2: Gruppi
    print("\nScaricando Gruppi (livello 2)...")
    for gg_code, gg_name in grandi_gruppi:
        time.sleep(REQUEST_DELAY)
        params = build_params({1: gg_code})
        soup = fetch_page(client, params)
        gruppi = extract_links(soup, 2)
        print(f"  GG {gg_code}: {len(gruppi)} Gruppi")

        for g_code, g_name in gruppi:
            hierarchy["gruppi"].append({
                "code": g_code,
                "name": g_name,
                "grande_gruppo": gg_code,
            })

            # Level 3: Classi
            time.sleep(REQUEST_DELAY)
            params3 = build_params({1: gg_code, 2: g_code})
            soup3 = fetch_page(client, params3)
            classi = extract_links(soup3, 3)

            for c_code, c_name in classi:
                hierarchy["classi"].append({
                    "code": c_code,
                    "name": c_name,
                    "gruppo": g_code,
                    "grande_gruppo": gg_code,
                })

                # Level 4: Categorie
                time.sleep(REQUEST_DELAY)
                params4 = build_params({1: gg_code, 2: g_code, 3: c_code})
                soup4 = fetch_page(client, params4)
                categorie = extract_links(soup4, 4)

                for cat_code, cat_name in categorie:
                    hierarchy["categorie"].append({
                        "code": cat_code,
                        "name": cat_name,
                        "classe": c_code,
                        "gruppo": g_code,
                        "grande_gruppo": gg_code,
                    })

                    # Level 5: Unità Professionali
                    time.sleep(REQUEST_DELAY)
                    params5 = build_params({
                        1: gg_code, 2: g_code,
                        3: c_code, 4: cat_code
                    })
                    soup5 = fetch_page(client, params5)
                    ups = extract_links(soup5, 5)

                    for up_code, up_name in ups:
                        hierarchy["unita_professionali"].append({
                            "code": up_code,
                            "name": up_name,
                            "categoria": cat_code,
                            "classe": c_code,
                            "gruppo": g_code,
                            "grande_gruppo": gg_code,
                        })

                print(f"    Classe {c_code}: {len(categorie)} cat, "
                      f"{sum(1 for u in hierarchy['unita_professionali'] if u['classe'] == c_code)} UP")

    return hierarchy


def build_professioni_json(hierarchy):
    """Build the master professioni.json from the hierarchy."""
    # Create lookup maps
    gg_names = {g["code"]: g["name"] for g in hierarchy["grandi_gruppi"]}

    professioni = []
    for up in hierarchy["unita_professionali"]:
        gg_code = up["grande_gruppo"]
        professioni.append({
            "code": up["code"],
            "title_it": up["name"],
            "slug": slugify(up["code"], up["name"]),
            "grande_gruppo": int(gg_code),
            "grande_gruppo_name_it": gg_names.get(gg_code, ""),
            "gruppo": up["gruppo"],
            "classe": up["classe"],
            "categoria": up["categoria"],
            "istat_url": f"{BASE_URL}/scheda.php?id={up['code']}",
            "inapp_url": f"https://www.inapp.gov.it/professioni/scopri-professioni/scheda/?keyword={up['code']}",
        })

    # Sort by code
    professioni.sort(key=lambda x: [int(c) for c in x["code"].split(".")])
    return professioni


def main():
    parser = argparse.ArgumentParser(description="Download ISTAT CP2021 classification")
    parser.add_argument("--force", action="store_true", help="Re-download ignoring cache")
    args = parser.parse_args()

    # Check cache
    if not args.force and os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE) as f:
            data = json.load(f)
        print(f"Cached: {len(data)} professioni in {OUTPUT_FILE}")
        print("Use --force to re-download")
        return

    print("=== Download Classificazione ISTAT CP2021 ===\n")

    client = httpx.Client(
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept-Language": "it-IT,it;q=0.9",
        },
        follow_redirects=True,
    )

    try:
        hierarchy = scrape_classification(client)
    finally:
        client.close()

    # Save full hierarchy
    with open(HIERARCHY_FILE, "w", encoding="utf-8") as f:
        json.dump(hierarchy, f, indent=2, ensure_ascii=False)
    print(f"\nGerarchia completa salvata in {HIERARCHY_FILE}")

    # Build and save professioni.json
    professioni = build_professioni_json(hierarchy)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(professioni, f, indent=2, ensure_ascii=False)

    # Summary
    print(f"\n=== Riepilogo ===")
    print(f"Grandi Gruppi:       {len(hierarchy['grandi_gruppi'])}")
    print(f"Gruppi:              {len(hierarchy['gruppi'])}")
    print(f"Classi:              {len(hierarchy['classi'])}")
    print(f"Categorie:           {len(hierarchy['categorie'])}")
    print(f"Unità Professionali: {len(hierarchy['unita_professionali'])}")
    print(f"\nSalvate {len(professioni)} professioni in {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
