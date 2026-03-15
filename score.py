"""
Score each Italian profession's AI exposure using Claude via Anthropic SDK.

Reads Markdown descriptions from pages/, sends each to Claude Haiku with a
scoring rubric integrating Anthropic's observed exposure framework.
Results are cached incrementally to scores.json.

Usage:
    uv run python score.py
    uv run python score.py --model claude-haiku-4-5-20251001
    uv run python score.py --start 0 --end 10   # test on first 10
"""

import argparse
import json
import os
import time
import anthropic
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env", override=True)

DEFAULT_MODEL = "claude-haiku-4-5-20251001"
OUTPUT_FILE = "scores.json"

SYSTEM_PROMPT = """\
You are an expert analyst evaluating how exposed different occupations are to \
AI. You will be given a description of an Italian occupation from the ISTAT \
CP2021 professional classification system.

Rate the occupation's overall **AI Exposure** on a scale from 0 to 10.

AI Exposure measures: how much will AI reshape this occupation? Consider both \
direct effects (AI automating tasks currently done by humans) and indirect \
effects (AI making each worker so productive that fewer are needed).

Apply Anthropic's "observed exposure" framework:
- For each core task, estimate whether AI could **AUTOMATE** it (replace the \
human entirely) or **AUGMENT** it (double worker productivity).
- Automated tasks contribute full weight to exposure; augmented tasks \
contribute half weight.
- A key signal is whether the job's work product is fundamentally digital.

If the job can be done entirely from a home office on a computer — writing, \
coding, analyzing, communicating — then AI exposure is inherently high (7+), \
because AI capabilities in digital domains are advancing rapidly. Conversely, \
jobs requiring physical presence, manual skill, or real-time human interaction \
in the physical world have a natural barrier to AI exposure.

Italian labor market context to consider:
- Italy has a larger share of small/medium enterprises (PMI) and artisanal work
- Public administration and bureaucratic roles are proportionally larger
- Manufacturing and "Made in Italy" craftsmanship sectors are significant
- Tourism and hospitality sector is proportionally larger

Use these anchors to calibrate your score:

- **0–1: Minimal exposure.** Almost entirely physical, hands-on work in \
unpredictable environments. AI has essentially no impact. \
Examples: muratore (bricklayer), giardiniere (gardener), sommozzatore (diver).

- **2–3: Low exposure.** Mostly physical or interpersonal work. AI helps with \
minor peripheral tasks but doesn't touch the core job. \
Examples: elettricista (electrician), idraulico (plumber), vigile del fuoco \
(firefighter), infermiere generico (nursing aide).

- **4–5: Moderate exposure.** Mix of physical/interpersonal and knowledge work. \
AI meaningfully assists with information tasks but substantial human presence \
needed. \
Examples: infermiere professionale (registered nurse), poliziotto (police \
officer), veterinario (veterinarian), cuoco (chef).

- **6–7: High exposure.** Predominantly knowledge work with some human judgment \
or presence needed. AI tools already useful, workers using AI substantially \
more productive. \
Examples: insegnante (teacher), dirigente (manager), commercialista \
(accountant), giornalista (journalist), impiegato amministrativo (admin clerk).

- **8–9: Very high exposure.** Almost entirely digital work. All core tasks in \
domains where AI is rapidly improving. Major restructuring ahead. \
Examples: sviluppatore software (developer), grafico (graphic designer), \
traduttore (translator), analista dati (data analyst), paralegale (paralegal).

- **10: Maximum exposure.** Routine digital information processing, fully \
digital, no physical component. AI can already do most of it. \
Examples: addetto inserimento dati (data entry), operatore telemarketing.

Respond with ONLY a JSON object in this exact format, no other text:
{
  "exposure": <0-10>,
  "rationale_en": "<2-3 sentences in English explaining key factors>",
  "rationale_it": "<2-3 sentences in Italian explaining key factors>",
  "title_en": "<English translation of the profession title>"
}\
"""


def score_occupation(client, text, model):
    """Send one occupation to Claude and parse the structured response."""
    message = client.messages.create(
        model=model,
        max_tokens=500,
        temperature=0.2,
        system=SYSTEM_PROMPT,
        messages=[
            {"role": "user", "content": text},
        ],
    )
    content = message.content[0].text

    # Strip markdown code fences if present
    content = content.strip()
    if content.startswith("```"):
        content = content.split("\n", 1)[1]
        if content.endswith("```"):
            content = content[:-3]
        content = content.strip()

    return json.loads(content)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--end", type=int, default=None)
    parser.add_argument("--delay", type=float, default=0.3)
    parser.add_argument("--force", action="store_true",
                        help="Re-score even if already cached")
    args = parser.parse_args()

    with open("professioni.json", encoding="utf-8") as f:
        professioni = json.load(f)

    subset = professioni[args.start:args.end]

    # Load existing scores
    scores = {}
    if os.path.exists(OUTPUT_FILE) and not args.force:
        with open(OUTPUT_FILE, encoding="utf-8") as f:
            for entry in json.load(f):
                scores[entry["slug"]] = entry

    print(f"Scoring {len(subset)} professions with {args.model}")
    print(f"Already cached: {len(scores)}")

    errors = []
    client = anthropic.Anthropic()

    for i, prof in enumerate(subset):
        slug = prof["slug"]

        if slug in scores:
            continue

        md_path = f"pages/{slug}.md"
        if not os.path.exists(md_path):
            print(f"  [{i+1}] SKIP {slug} (no markdown)")
            continue

        with open(md_path, encoding="utf-8") as f:
            text = f.read()

        print(f"  [{i+1}/{len(subset)}] {prof['title_it'][:50]}...", end=" ", flush=True)

        try:
            result = score_occupation(client, text, args.model)
            scores[slug] = {
                "slug": slug,
                "code": prof["code"],
                "title_it": prof["title_it"],
                "title_en": result.get("title_en", ""),
                **result,
            }
            print(f"exposure={result['exposure']}")
        except Exception as e:
            print(f"ERROR: {e}")
            errors.append(slug)

        # Save after each one (incremental checkpoint)
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(list(scores.values()), f, indent=2, ensure_ascii=False)

        if i < len(subset) - 1:
            time.sleep(args.delay)

    print(f"\nDone. Scored {len(scores)} professions, {len(errors)} errors.")
    if errors:
        print(f"Errors: {errors}")

    # Summary stats
    vals = [s for s in scores.values() if "exposure" in s]
    if vals:
        avg = sum(s["exposure"] for s in vals) / len(vals)
        by_score = {}
        for s in vals:
            bucket = s["exposure"]
            by_score[bucket] = by_score.get(bucket, 0) + 1
        print(f"\nAverage exposure across {len(vals)} professions: {avg:.1f}")
        print("Distribution:")
        for k in sorted(by_score):
            print(f"  {k}: {'#' * by_score[k]} ({by_score[k]})")


if __name__ == "__main__":
    main()
