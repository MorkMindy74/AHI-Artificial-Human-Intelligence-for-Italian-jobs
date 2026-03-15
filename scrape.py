"""
Scrape ISTAT CP2021 profession detail pages.

Downloads detail pages from professioni.istat.it for each Unità Professionale.
Falls back to INAPP (via Playwright) if available.

Saves raw HTML to html/<slug>.html as the source of truth.
Run process.py afterwards to derive pages/<slug>.md.

Usage:
    uv run python scrape.py                      # scrape all
    uv run python scrape.py --start 0 --end 5    # scrape first 5
    uv run python scrape.py --force               # re-scrape ignoring cache
"""

import argparse
import json
import os
import time
import httpx

ISTAT_BASE = "https://professioni.istat.it/sistemainformativoprofessioni/cp"


def main():
    parser = argparse.ArgumentParser(description="Scrape ISTAT profession pages")
    parser.add_argument("--start", type=int, default=0, help="Start index (inclusive)")
    parser.add_argument("--end", type=int, default=None, help="End index (exclusive)")
    parser.add_argument("--force", action="store_true", help="Re-scrape even if cached")
    parser.add_argument("--delay", type=float, default=0.5, help="Seconds between requests")
    args = parser.parse_args()

    with open("professioni.json", encoding="utf-8") as f:
        professioni = json.load(f)

    end = args.end if args.end is not None else len(professioni)
    subset = professioni[args.start:end]

    os.makedirs("html", exist_ok=True)
    os.makedirs("pages", exist_ok=True)

    # Figure out what needs scraping
    to_scrape = []
    for i, prof in enumerate(subset, start=args.start):
        html_path = f"html/{prof['slug']}.html"
        if not args.force and os.path.exists(html_path):
            print(f"  [{i}] CACHED {prof['title_it'][:50]}")
            continue
        to_scrape.append((i, prof))

    if not to_scrape:
        print("Nothing to scrape — all cached.")
        return

    print(f"\nScraping {len(to_scrape)} profession pages from ISTAT...\n")

    client = httpx.Client(
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept-Language": "it-IT,it;q=0.9",
        },
        follow_redirects=True,
        timeout=30,
    )

    errors = []
    for idx, (i, prof) in enumerate(to_scrape):
        slug = prof["slug"]
        code = prof["code"]
        html_path = f"html/{slug}.html"
        url = f"{ISTAT_BASE}/scheda.php?id={code}"

        print(f"  [{i}/{len(professioni)}] {prof['title_it'][:50]}...", end=" ", flush=True)

        try:
            resp = client.get(url)
            if resp.status_code != 200:
                print(f"HTTP {resp.status_code} — SKIPPED")
                errors.append(slug)
                continue

            html = resp.text
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(html)

            print(f"OK ({len(html):,} bytes)")

        except Exception as e:
            print(f"ERROR: {e}")
            errors.append(slug)

        if idx < len(to_scrape) - 1:
            time.sleep(args.delay)

    client.close()

    cached = len([f for f in os.listdir("html") if f.endswith(".html")])
    print(f"\nDone. {cached}/{len(professioni)} HTML files cached in html/")
    if errors:
        print(f"Errors ({len(errors)}): {errors[:10]}...")


if __name__ == "__main__":
    main()
