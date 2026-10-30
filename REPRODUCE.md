# How this repository was made (El Salvador)

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Asamblea Legislativa de El Salvador, Índice Legislativo | <https://www.asamblea.gob.sv/leyes-y-decretos> | 2026-10-29 | Official legislative text; Ley de Propiedad Intelectual (D.L. 66/2024) art. 50 allows publication of laws faithful to the official text |
| Asamblea Legislativa de El Salvador, Índice Legislativo: Código Penal | <https://www.asamblea.gob.sv/sites/default/files/documents/decretos/631050CB-7A8D-4CBE-A750-2B33EBE41B8A.pdf> | 2026-10-30 | Official legislative text; Ley de Propiedad Intelectual (D.L. 66/2024) art. 50 allows publication of laws faithful to the official text |
| Asamblea Legislativa de El Salvador, Índice Legislativo: Código Civil | <https://www.asamblea.gob.sv/sites/default/files/documents/decretos/D491C5C6-3C26-4D3D-B9A7-CC394CEE2D69.pdf> | 2026-10-30 | Official legislative text; Ley de Propiedad Intelectual (D.L. 66/2024) art. 50 allows publication of laws faithful to the official text |
| Asamblea Legislativa de El Salvador, Índice Legislativo: Código de Comercio | <https://www.asamblea.gob.sv/sites/default/files/documents/decretos/945102FD-7B05-485E-B98B-6C5D3C0509E3.pdf> | 2026-10-30 | Official legislative text; Ley de Propiedad Intelectual (D.L. 66/2024) art. 50 allows publication of laws faithful to the official text |
| Asamblea Legislativa de El Salvador, Índice Legislativo: Código de Trabajo | <https://www.asamblea.gob.sv/sites/default/files/documents/decretos/78CDEA76-6047-427C-8CFE-00F1650C6066.pdf> | 2026-10-30 | Official legislative text; Ley de Propiedad Intelectual (D.L. 66/2024) art. 50 allows publication of laws faithful to the official text |
| Asamblea Legislativa de El Salvador, Índice Legislativo: Código Procesal Penal | <https://www.asamblea.gob.sv/sites/default/files/documents/decretos/6BCD7BC0-F6BF-4696-9354-4C8EDA34E677.pdf> | 2026-10-30 | Official legislative text; Ley de Propiedad Intelectual (D.L. 66/2024) art. 50 allows publication of laws faithful to the official text |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitucion` | Constitución de la República de El Salvador (Decreto Constituyente n.º 38, 1983) | 1 | 2026-05-07 to 2026-05-07 |
| `codigo-penal` | Código Penal (Decreto Legislativo n.º 1030, 1997) | 1 | 2026-03-27 to 2026-03-27 |
| `codigo-civil` | Código Civil (decreto del Poder Ejecutivo de 23 de agosto de 1859) | 1 | 2022-04-26 to 2022-04-26 |
| `codigo-de-comercio` | Código de Comercio (Decreto Legislativo n.º 671, 1970) | 1 | 2024-04-11 to 2024-04-11 |
| `codigo-de-trabajo` | Código de Trabajo (Decreto Legislativo n.º 15, 1972) | 1 | 2026-09-24 to 2026-09-24 |
| `codigo-procesal-penal` | Código Procesal Penal (Decreto Legislativo n.º 733, 2008) | 1 | 2026-04-26 to 2026-04-26 |

The build made 6 commits:

| Commits | Kind |
| ---: | --- |
| 6 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `futuro`: laws not yet in force on 2026-10-30.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 1 laws in the record.
- 6 tags.

## Dates

Each commit is dated at noon (America/El_Salvador) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Constitución art. 140: la ley entra en vigencia ocho días después de su publicación en el Diario Oficial, salvo que el propio decreto disponga otra cosa https://www.asamblea.gob.sv

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `89688fe86335187504b4a36b0329920462de092ded82d68e9cb128d588a82d53` (3153796 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3d00541d258745461ab52b1b0cb4e1716a27a95d`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

6 versions of 6 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

A second build from the same corpus into an empty folder gave identical hashes for all 6 history commits and 6 tags (history tip `e5d06e5d05b507adc8192cb2ff70a3dd57462e9f`).

## Decisions made by hand

- Only the current consolidated text was available from the Asamblea, so the repository holds one version, dated 2026-05-07, the Diario Oficial date of the last reform listed in the source (D.L. 569 and 570, D.O. 83); the in-force day of the most recent reforms was not checked separately.
- Footnote markers (n) for reform references, page headers and the list of signatories were removed; title, chapter and section headings between articles were not kept as units.
- Reform references were not credited to individual provisions (the source lists them only as numbers), so the single version is credited to the publisher as oldest version available.
- Código Penal: one version, dated 2026-03-27, the Diario Oficial date of the last reform in the source list (reform 81, D.L. 537 of 26 March 2026, D.O. 61); later editor marks up to 21 April 2026 were not treated as reforms, and the in-force day was not checked separately. Headings and marginal article titles are taken out as whole blocks, so reformed article text printed in capitals is kept in full.
- Código Civil: one version, dated 2022-04-26, the Diario Oficial date of the last reform in the source list (reform 19, D.L. 294 of 22 February 2022, D.O. 78); the in-force day was not checked separately. The source prints the superscript ordinal marks in lists as "1" (for example "11)" for "1º)") and they are kept as printed. The preamble holds the 1859 promulgating decree, and the "Edición" notes after the final article are not kept.
- Código de Comercio: one version, dated 2024-04-11, the Diario Oficial date of the last reform in the source list (reform 24, D.L. 972 of 19 March 2024, D.O. 67); the in-force day was not checked separately. Articles 15 and 456 do not appear in the source text, so they have no file; the two authentic interpretations printed in the middle of the text (D.L. 237/1985 and 389/2001) are not part of the code and are left out.
- Codes: page headers and footers, reform footnote markers "(n)", and the Libro, Título, Capítulo, Sección and marginal headings between articles were not kept as units; a repeated article with the same text in the source (Código Civil arts. 109, 349, 435, 438) is kept once.
- Código de Trabajo: one version, dated 2026-09-24, the day the last reform in the source list took effect (reform 28, D.L. 669 of 23 September 2026, D.O. 177 of 24 September 2026; its final article puts it in force on the day of its publication in the Diario Oficial, read in the decree itself). The notes on unconstitutionality rulings after the reform list are not part of the code and are left out.
- Código de Trabajo: page headers and footers, reform footnote markers "(n)", and the Libro, Título, Capítulo, Sección and marginal headings between articles were not kept as units; ordinal marks, quotation marks and the inverted question mark printed in a symbol font were mapped to the characters the page shows.
- Código Procesal Penal: one version, dated 2026-04-26, the day the last reform in the source list took effect (reform 23, D.L. 534 of 26 March 2026, D.O. 61 of 27 March 2026; its art. 8 puts it in force thirty days after publication, read in the decree itself). Mixed-case marginal article titles are left out like the capitalised ones; the extradition articles 502-A onwards keep their source numbering.
- Código Procesal Penal: page headers and footers, reform footnote markers "(n)", and the Libro, Título, Capítulo, Sección and marginal headings between articles were not kept as units; ordinal marks, quotation marks and the inverted question mark printed in a symbol font were mapped to the characters the page shows.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none
- none
- none
