# El Salvador: law history in git


The national law of El Salvador as a git history: one file per article, one commit per version on the day it took effect, and the law behind each version as the commit's author. `git blame` names the law behind every article; `git log` lists every change to an article; picking a date gives the text in force that day, as far as the record reaches.

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is El Salvador's national law, which global-law reads at `el-salvador/national/acts/`.

**What is in it now:** the Constitution of 1983, five codes (the Código Civil, the Código de Comercio, the Código de Trabajo, the Código Penal and the Código Procesal Penal) and 945 decrees of the Asamblea Legislativa (laws, ratified treaties and other legislative decrees), each as one version: today's text with its reforms worked in. [`data/versions.json`](data/versions.json) lists every act with its version; each act's folder has a `README.md` listing its provisions.

Each act is a folder: `constitution/constitucion/`, `code/<code>/` (`code/codigo-de-trabajo/` is the Código de Trabajo, Decreto Legislativo n.º 15 of 1972) and `decreto/<year>/<number>/` (`decreto/1940/0017/` is Decreto N° 17 de 1940, the Ley de Asuetos, Vacaciones y Licencias de los Empleados Públicos; a second decree with the same year and number takes the Índice's view id, `decreto/2015/0961-v3138/`). In it, `art-177.md` is Art. 177 and `art-010-bis.md` Art. 10 bis; a decree's `preambulo.md` holds the text before Art. 1 and `firma.md` the closing and signatures. [`data/paths.json`](data/paths.json) maps each act id to its folder.

The text is in Spanish, as the Asamblea Legislativa prints it. An English translation is not part of this record.

## Questions as git commands

| Question | Command |
| --- | --- |
| Every change to Art. 177 (annual leave) of the Código de Trabajo | `git log -p --follow --word-diff -- code/codigo-de-trabajo/art-177.md` |
| Which act wrote each line of Art. 177? | `git blame code/codigo-de-trabajo/art-177.md` |
| Every version of the Código de Trabajo, with the day each took effect | `git log --format="%h %(trailers:key=In-force,valueonly,separator=) %an" --grep="^Act: CT$"` |
| Art. 177 as in force on 1 November 2026 | `python tools/on.py 2026-11-01 codigo-de-trabajo 177` |

**Outside git**, we also host this record publicly, for free:

- **[Ask Claude about Salvadoran law](https://global-law.lexifina.com/v1/try_claude?country=el-salvador)**: opens Claude with a first question ready.
- **[Ask ChatGPT](https://global-law.lexifina.com/v1/try_chatgpt?country=el-salvador)**: the same question in ChatGPT.
- **[Call the API in your browser](https://global-law.lexifina.com/v1/search_law?query=vacaciones&jurisdictions=el-salvador)**: a search of Salvadoran law for "vacaciones", returned as JSON. See the [documentation here](https://lexifina.com/api/global-law).

Both assistants read the record through the free Global law connector (MCP, `https://global-law.lexifina.com/mcp`); the first time, the chat gives you the link that adds it. Ask in Spanish or in English.

**Host it yourself easily.** All it takes is git and Python, and the tools run on your machine:

```sh
git clone --depth 1 https://github.com/lexifina/global-law && cd global-law
python3 tools/countries.py add el-salvador/national/acts
python3 tools/law.py show 2026-11-01 el-salvador/national/acts/code/codigo-de-trabajo/art-177.md
```

Opened in Claude Code, Cursor, VS Code or Codex, the clone also starts a local MCP server with the same tools ([MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md)).

## Dates

Each commit is dated at noon, America/El_Salvador, on the day the version took effect, and carries it in its `In-force:` trailer:

- for the Constitution and the codes, the Diario Oficial day of the last reform the source lists (the Constitution 7 May 2026, the Código Penal 27 March 2026, the Código Civil 26 April 2022, the Código de Comercio 11 April 2024), or the day that reform took effect, read in the reform itself (the Código de Trabajo 24 September 2026, the Código Procesal Penal 26 April 2026);
- for a decree with no reform listed, the day its own vigencia article gives, otherwise eight days after its Diario Oficial publication (Constitución art. 140); for a reformed decree, eight days after the Diario Oficial publication of the latest reform listed; where the list could not be read (17 decrees), the day it was retrieved, 3 November 2026;
- git cannot store dates before 1970, so the 7 decrees in force earlier (1934 to 1951) are dated from 1970-01-01, one second apart, with the real day in `In-force:`. Ask for a date with `tools/on.py`, not `git log --before`.

A decree with no reform is credited to itself (`D. L. N° 149 de 1934`) and a reformed one to its latest reform (`D. L. N° 674 de 2026`), for its whole text. The Constitution, the codes and the 17 decrees whose reform list could not be read are the "oldest version available", credited to the publisher, the Asamblea Legislativa's Índice Legislativo.

## How it is checked

- Every text is read from the text layer of the Asamblea's born-digital PDFs, without OCR. In a decree, every word before the Diario Oficial block is in a file, in order, except page headers, the reform markers "(n)" and editors' notes.
- A decree whose articles are not numbered 1, 2, 3 and so on, each once, is left out, and so are temporary decrees, which may have lapsed.
- `tools/build.py` writes the history from one corpus file, and the same corpus always gives the same commit hashes; `tools/check_repo.py` reads every version back from git and compares it with the corpus, and checks that `main` has no merge commits and nothing dated in the future. [`REPRODUCE.md`](REPRODUCE.md) does not yet record a run of it or a second build.

## What it does not show

- **Earlier wordings.** Each act is one text, as the Asamblea prints it today: how the Código de Trabajo read before its 2026 reform, or the Constitution as adopted in 1983, is not here. Passages a reform changed are printed in capitals in the source and kept so.
- **Which reform changed which article.** A reformed decree's whole text is credited to its latest reform, and the codes and the Constitution to the publisher.
- **Headings and notes.** The Libro, Título and Capítulo headings between articles, reform footnotes and page headers are not in the files; Arts. 15 and 456 of the Código de Comercio are not in the source text.
- **Most decrees of the Índice Legislativo**, among them those left out above, and executive decrees and regulations, municipal ordinances and case law.

## Sources

| Source | Kind | Past versions | Notes |
| --- | --- | --- | --- |
| [Asamblea Legislativa, Índice Legislativo](https://www.asamblea.gob.sv/leyes-y-decretos/decretos-por-anios) | Official index of legislative decrees | no: the current text, with its list of reforms | The Constitution, the five codes and the 945 decrees, from its PDFs; the Diario Oficial publication of each decree and of its reforms |

## Licence

See [`LICENSE`](LICENSE). Article 50 of the Ley de Propiedad Intelectual (Decreto Legislativo n.º 66 of 2024) allows laws to be published, singly or in collections, faithful to the official text and without the Government's authorisation. The arrangement, tables, commit messages and tools are by Lexifina, under the Creative Commons Attribution 4.0 International licence.

No AI model wrote, translated or corrected legal text, and none runs at build time; the scripts were written by Claude Code running Claude Opus 5.5 (see [`REPRODUCE.md`](REPRODUCE.md)).

## More

From [lexifina/global-law](https://github.com/lexifina/global-law):

- [FEATURES.md](https://github.com/lexifina/global-law/blob/main/FEATURES.md): every feature, and what every corpus must support (`git blame`, `law.py`, the MCP tools)
- [FAQ.md](https://github.com/lexifina/global-law/blob/main/FAQ.md): questions and answers · [CONTRIBUTING.md](https://github.com/lexifina/global-law/blob/main/CONTRIBUTING.md): proposing changes · [MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md): the MCP server · [REPRODUCE.md](https://github.com/lexifina/global-law/blob/main/REPRODUCE.md): how it was built · [CHANGELOG.md](https://github.com/lexifina/global-law/blob/main/CHANGELOG.md)
- [FRESHNESS.md](https://github.com/lexifina/global-law/blob/main/FRESHNESS.md): how current each corpus is · [Monitoring](https://github.com/lexifina/global-law/tree/main/monitoring): whether updates are running · [WATCHING.md](https://github.com/lexifina/global-law/blob/main/WATCHING.md): how each official source is watched for changes
- [performance/](https://github.com/lexifina/global-law/tree/main/performance): how fast the tools are, measured
- [visualisations/](https://github.com/lexifina/global-law/tree/main/visualisations): charts and bridges across the world's law
- [Vulnerabilities](https://github.com/lexifina/global-law/tree/main/vulnerabilities): mistakes in legislation as published
