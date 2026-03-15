# Esposizione all'IA del Mercato del Lavoro Italiano

Analisi dell'esposizione all'intelligenza artificiale di **813 professioni** del mercato del lavoro italiano, basata sulla classificazione ISTAT CP2021.

*English: AI Exposure of the Italian Job Market — analyzing how susceptible every occupation in the Italian economy is to AI and automation.*

## Cosa c'e' qui

La classificazione ISTAT CP2021 copre **813 Unita' Professionali** organizzate in 9 Grandi Gruppi, con descrizioni dettagliate delle mansioni, esempi di professioni e gerarchia a 5 livelli. Abbiamo scaricato tutte le schede, valutato l'esposizione all'IA di ogni professione usando un LLM, e costruito una visualizzazione interattiva.

La metodologia di scoring integra il framework ["observed exposure"](https://www.anthropic.com/research/labor-market-impacts) di Anthropic Research, distinguendo tra automazione (peso pieno) e augmentazione (peso dimezzato).

## Pipeline dati

1. **Classificazione** (`download_classification.py`) — Scarica la gerarchia completa CP2021 da professioni.istat.it: 9 Grandi Gruppi > 40 Gruppi > 130 Classi > 510 Categorie > 813 UP. Output: `professioni.json`.
2. **Scraping** (`scrape.py`) — Scarica le schede dettagliate di ogni professione dal sito ISTAT in `html/`.
3. **Parsing** (`parse_detail.py`, `process.py`) — BeautifulSoup converte l'HTML in Markdown pulito in `pages/`.
4. **Tabella** (`make_csv.py`) — Estrae campi strutturati (descrizione, istruzione, esempi) in `professioni.csv`.
5. **Scoring** (`score.py`) — Invia ogni professione a Claude (Haiku 4.5 via Anthropic SDK) con un rubric di scoring. Output: `scores.json` con punteggio 0-10 e rationale bilingue IT/EN.
6. **Dati sito** (`build_site_data.py`) — Fonde CSV e score in `site/data.json`.
7. **Sito web** (`site/index.html`) — Visualizzazione interattiva bilingue con tre viste: treemap, sunburst e colonne.

## Scala di esposizione

| Punteggio | Significato | Esempi |
|-----------|-------------|--------|
| 0-1 | Minima | Muratore, giardiniere, sommozzatore |
| 2-3 | Bassa | Elettricista, idraulico, vigile del fuoco |
| 4-5 | Moderata | Infermiere, poliziotto, veterinario |
| 6-7 | Alta | Insegnante, dirigente, commercialista |
| 8-9 | Molto alta | Sviluppatore software, traduttore, analista dati |
| 10 | Massima | Addetto inserimento dati, operatore telemarketing |

## Fonti dati

- **Professioni:** [ISTAT CP2021](https://professioni.istat.it/sistemainformativoprofessioni/cp/) — Classificazione delle Professioni 2021
- **Scoring IA:** [Claude Haiku 4.5](https://www.anthropic.com/) via Anthropic SDK
- **Framework:** [Anthropic Research — Labor Market Impacts](https://www.anthropic.com/research/labor-market-impacts)

## Setup

```bash
uv sync
echo "ANTHROPIC_API_KEY=sk-ant-..." > .env
```

## Esecuzione completa

```bash
uv run python download_classification.py   # 1. Scarica classificazione CP2021
uv run python scrape.py                     # 2. Scarica schede ISTAT (~7 min)
uv run python process.py                    # 3. HTML -> Markdown
uv run python make_csv.py                   # 4. Genera CSV
uv run python score.py                      # 5. Scoring AI (~$0.50, ~15 min)
uv run python build_site_data.py            # 6. Genera dati sito
uv run python make_prompt.py                # 7. Genera report analisi
cd site && python -m http.server 8000       # 8. Visualizza
```

## Visualizzazione

Il sito offre tre viste:

- **Treemap** — Rettangoli raggruppati per Grande Gruppo, colore = esposizione IA
- **Sunburst** — Cerchi concentrici con tutti i 5 livelli della gerarchia CP2021
- **Colonne** — Distribuzione per punteggio di esposizione

Interfaccia bilingue IT/EN con toggle nel sidebar.

## Crediti

Basato su [AI Exposure of the US Job Market](https://github.com/karpathy/jobs) di Andrej Karpathy, adattato per il mercato del lavoro italiano.
