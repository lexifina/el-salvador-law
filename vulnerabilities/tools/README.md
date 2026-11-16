# Tools

The scripts behind this El Salvador-only run of global-law's vulnerability detectors. They run inside a copy of
[global-law/vulnerabilities/scripts](https://github.com/lexifina/global-law/tree/main/vulnerabilities/scripts) (Python 3.11+,
`pip install duckdb pyarrow`), with a bare clone of this repository at `sources/corpus/el-salvador-law.git`, a blobless bare
clone of global-law at `sources/global-law.git`, and a `pins.json` that names only el-salvador-law and its commit (language
`es`, code `SV`). `build_vulns.py`, `flags_chart.py`, `late_ext_select.py`, `late_ext_rebut.py` and `patch_sv.py` sit two
folders above the scripts, next to `config.json`.

| Script | What it does |
| --- | --- |
| `run.sh` | Indexes the history and texts, maps paths to the folders since the move (`map_moved.py`), adds this repository's history rows, and runs the detectors (`bash run.sh <shards>`) |
| `add_root.py` | Builds the history rows from this repository's own commits (global-law replays it only up to an earlier commit), so the history detectors read every change |
| `map_moved.py` | Rewrites the paths in the history table to each act's folder since the move of 10 November 2026 (`data/paths.json`), so that an act's history is not split in two at the move; `run.sh` runs it after the history is indexed |
| `patch_sv.py` | The two Salvadoran fixes below, in the copy of global-law's scripts (`python -X utf8 patch_sv.py <scripts dir>`; a fix already in place is skipped) |
| `run_triage.sh` | The model review: the 40 strongest flags per category, the 40 strongest lapsed time limits in law texts, and the empty periods |
| `late_ext_select.py` | Chooses the empty periods for global-law's review of that category (there were none here) |
| `late_ext_rebut.py` | Adds the second, arguing-against pass to the empty-period review, as `triage.py` does for the other categories |
| `build_vulns.py` | Builds `data/flags.csv`, `data/reviewed.csv` and `data/by_category.csv` from the findings and the model review |
| `flags_chart.py` | Draws the chart at the top of the READMEs, in Spanish and English, light and dark |
| `config.json` | The repository, the Spanish category names, the files that are not law, and the chart's labels |
| `patch_detectors.py` | Fixes blind spots found in runs on several country repositories in the copy of global-law's scripts (`python -X utf8 patch_detectors.py <scripts dir>`; a fix already in place is skipped) |
| `patch_detectors_vi.py`, `patch_es.py`, `patch_ca.py`, `patch_en.py`, `patch_de.py`, `patch_en_et.py` | The same for the Vietnamese, Spanish, Catalan, English (two rounds) and German blind spots found by other runs; `patch_es.py`'s Spanish date forms ("hasta el día 31 de diciembre de 2020", "31 de diciembre del año 2020") also apply here, the others change nothing, but `redo.py` runs them on every repository |
| `redo.py` | Runs those patches, then again only the scans and detectors the fixes change, the model review of lapsed time limits, references to deleted provisions and empty periods, and the build (`python -X utf8 redo.py <run folder> [--keep-reviews] [--full]`; `--full` runs every step again through `run.sh`; `EMBED_FONTS` names the script that embeds the chart's fonts). It does not run `patch_sv.py`; run that first |

The model review needs `LLM_BASE_URL`, `LLM_API_KEY`, `LLM_MODEL` and `LLM_AUTH` set for an OpenAI-compatible Responses API.
It was run as `bash run_triage.sh '^(data/|tools/|README|REPRODUCE|LICENSE|jurisdiction\.json)'`; every act is under
`constitution/`, `code/` or `decreto/`, so the review of lapsed time limits in law texts drew the same 40 flags as the review
of all of them, and `build_vulns.py` keeps the later review of each flag.

The detectors in this copy already carry every fix of `patch_detectors.py` and the other patches above. Changes made for
this repository:

- `pins.json`: the corpus's `language` was null; it is now `es`, which several detectors read (month names, words that are
  not currencies in a language).
- `patch_sv.py`, dates in words: the time-limit search now reads a date written wholly in words, as Salvadoran decrees
  write it ("hasta el treinta y uno de diciembre de dos mil catorce", "HASTA EL TREINTA DE SEPTIEMBRE DE MIL NOVECIENTOS
  NOVENTA Y NUEVE"); the day (primero, uno ... treinta y uno) and the year (mil novecientos ..., dos mil ...) are turned into
  figures. Lapsed time limits went from 32 to 46: the 14 new flags are every phrase of that kind with "hasta" in the
  repository. Still not read: "a más tardar" (no later than; 11 past dates, in figures or words) and "antes del" (before)
  followed by a date, which the Spanish time-limit search does not read in any form.
- `patch_sv.py`, the colón: the dead-currency search now reads "colones" and "¢" next to an amount ("¢2,000.00",
  "50 colones"), for the jurisdiction coded `SV` in `pins.json` only (`EXTRA_CURRENCY_CODE`), since Costa Rica's colón is
  still in use; not the singular "colón", which is also a place name ("Canal Río Colón 6.5"). The colón was replaced in
  circulation by the US dollar under the Monetary Integration Act (in force from 1 January 2001, at a fixed 8.75 colones to
  the dollar) but is still legal tender; the amounts are flagged as dead currency, as pesetas are in Spain, and the
  category's Spanish name is "Monedas fuera de circulación" (out of circulation), not "sin curso legal". Dead currencies
  went from 5 (German marks) to 357.
- `config.json` counts each act's `README.md` (its title and list of provisions), `REPRODUCE.md` and the top-level files as
  not law; each act's `preambulo.md` and `firma.md` are part of the decree's text and count as law.
- `add_root.py` needed no change: law commits here carry `Kind: law`, and the two `Kind: documentation` commits are left out.
