# AI Exposure of the Italian Job Market

Analysis of AI exposure for **813 occupations** in the Italian labor market, based on the ISTAT CP2021 classification.

Interactive site: [morkmindy74.github.io/AHI-Artificial-Human-Intelligence-for-Italian-jobs](https://morkmindy74.github.io/AHI-Artificial-Human-Intelligence-for-Italian-jobs/)

## What's here

The ISTAT CP2021 classification covers **813 Professional Units** organized into 9 Major Groups, with detailed job descriptions, occupation examples, and a 5-level hierarchy. We downloaded all the occupation sheets, scored each one for AI exposure using an LLM, and built an interactive visualization.

The scoring methodology integrates Anthropic Research's ["observed exposure"](https://www.anthropic.com/research/labor-market-impacts) framework, distinguishing between automation (full weight) and augmentation (half weight).

## Data pipeline

1. **Classification** (`download_classification.py`) — Downloads the full CP2021 hierarchy from professioni.istat.it: 9 Major Groups > 40 Groups > 130 Classes > 510 Categories > 813 PUs. Output: `professioni.json`.
2. 2. **Scraping** (`scrape.py`) — Downloads the detailed occupation sheets from the ISTAT website into `html/`.
   3. 3. **Parsing** (`parse_detail.py`, `process.py`) — BeautifulSoup converts the HTML into clean Markdown in `pages/`.
      4. 4. **Table** (`make_csv.py`) — Extracts structured fields (description, education, examples) into `professioni.csv`.
         5. 5. **Scoring** (`score.py`) — Sends each occupation to Claude (Haiku 4.5 via Anthropic SDK) with a scoring rubric. Output: `scores.json` with a 0–10 score and bilingual IT/EN rationale.
            6. 6. **Site data** (`build_site_data.py`) — Merges CSV and scores into `site/data.json`.
               7. 7. **Website** (`site/index.html`) — Bilingual interactive visualization with three views: treemap, sunburst, and bar chart.
                 
                  8. ## Exposure scale
                 
                  9. | Score | Level | Examples |
                  10. |-------|-------|---------|
                  11. | 0–1 | Minimal | Bricklayer, gardener, diver |
                  12. | 2–3 | Low | Electrician, plumber, firefighter |
                  13. | 4–5 | Moderate | Nurse, police officer, veterinarian |
                  14. | 6–7 | High | Teacher, manager, accountant |
                  15. | 8–9 | Very high | Software developer, translator, data analyst |
                  16. | 10 | Maximum | Data entry clerk, telemarketing operator |
                 
                  17. ## Data sources
                 
                  18. - **Occupations:** [ISTAT CP2021](https://professioni.istat.it/sistemainformativoprofessioni/cp/) — Italian Classification of Occupations 2021
                      - - **AI Scoring:** [Claude Haiku 4.5](https://www.anthropic.com/) via Anthropic SDK
                        - - **Framework:** [Anthropic Research — Labor Market Impacts](https://www.anthropic.com/research/labor-market-impacts)
                         
                          - ## Setup
                         
                          - ```bash
                            uv sync
                            echo "ANTHROPIC_API_KEY=sk-ant-..." > .env
                            ```

                            ## Full run

                            ```bash
                            uv run python download_classification.py  # 1. Download CP2021 classification
                            uv run python scrape.py                   # 2. Download ISTAT sheets (~7 min)
                            uv run python process.py                  # 3. HTML -> Markdown
                            uv run python make_csv.py                 # 4. Generate CSV
                            uv run python score.py                    # 5. AI scoring (~$0.50, ~15 min)
                            uv run python build_site_data.py          # 6. Generate site data
                            uv run python make_prompt.py              # 7. Generate analysis report
                            cd site && python -m http.server 8000     # 8. Preview locally
                            ```

                            ## Visualization

                            The site offers three views:

                            - **Treemap** — Rectangles grouped by Major Group, color = AI exposure
                            - - **Sunburst** — Concentric rings with all 5 levels of the CP2021 hierarchy
                              - - **Bar chart** — Distribution by exposure score
                               
                                - Bilingual IT/EN interface with a toggle in the sidebar.
                               
                                - ## Credits
                               
                                - Based on [AI Exposure of the US Job Market](https://github.com/karpathy/jobs) by Andrej Karpathy, adapted for the Italian labor market.
