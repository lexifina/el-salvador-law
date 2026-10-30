# El Salvador: law history in git

The Constitution of El Salvador and its core codes as a git repository: one file per article, so `git blame` and `git log` work on the text. It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `sv/`.

**What is in it now**

| Folder | Law | Versions | History |
| --- | --- | ---: | --- |
| `constitucion/` | Constitución de la República de El Salvador (Decreto Constituyente n.º 38, in force 20 December 1983) | 1 | The current consolidated text, including every reform up to Decreto Legislativo n.º 570 of 7 May 2026 |
| `codigo-penal/` | Código Penal (Decreto Legislativo n.º 1030 of 26 April 1997, in force 20 April 1998): preamble and Arts. 1 to 409, with the lettered articles | 1 | The current consolidated text, including every reform up to Decreto Legislativo n.º 537 of 26 March 2026, dated from its Diario Oficial of 27 March 2026 |
| `codigo-civil/` | Código Civil (declared law by the Poder Ejecutivo on 23 August 1859, published 10 April 1860): promulgating decree, Arts. 1 to 2263 and the final article | 1 | The current consolidated text, including every reform up to Decreto Legislativo n.º 294 of 22 February 2022, dated from its Diario Oficial of 26 April 2022 |
| `codigo-de-comercio/` | Código de Comercio (Decreto Legislativo n.º 671 of 8 May 1970): preamble and Arts. 1 to 1566 (Arts. 15 and 456 are not in the source text) | 1 | The current consolidated text, including every reform up to Decreto Legislativo n.º 972 of 19 March 2024, dated from its Diario Oficial of 11 April 2024 |
| `codigo-de-trabajo/` | Código de Trabajo (Decreto Legislativo n.º 15 of 23 June 1972): Arts. 1 to 637, with the lettered articles | 1 | The current consolidated text, including every reform up to Decreto Legislativo n.º 669 of 23 September 2026, dated 24 September 2026, the day that reform took effect (on its publication) |
| `codigo-procesal-penal/` | Código Procesal Penal (Decreto Legislativo n.º 733 of 22 October 2008): preamble and Arts. 1 to 506, with the lettered articles (502-A onwards on extradition and assistance) | 1 | The current consolidated text, including every reform up to Decreto Legislativo n.º 534 of 26 March 2026, dated 26 April 2026, the day that reform took effect (thirty days after its publication) |

**Language.** The text is in Spanish, the official language. There is no official English text.

## Dates and limits

- The record has **one version**: the "oldest version available", the consolidated text the Asamblea Legislativa publishes in its Índice Legislativo. It is dated 7 May 2026, the Diario Oficial date (D.O. n.º 83, Tomo 451) of the last reforms the text lists (D.L. 569 and 570). The in-force day of those last reforms was not checked separately.
- **Earlier versions are not in the record.** The 1983 text and the reforms of 1991 to 2025 are not published as separate consolidations on the site, so the commit is credited to the publisher, not to the decree behind each change. Passages the reforms changed are printed in capitals in the source and kept that way.
- Reform footnote numbers, page headers and the list of signatories are not in the files. Title, chapter and section headings between articles are not kept. `preambulo.md` holds the preamble and `art-274.md` the final article with the transitional provision added by the reforms.
- File names: `art-005.md` is Article 5. In the codes, each file is one article with the same limits: one version each, dated from the last reform in the source's list (its Diario Oficial date, or its in-force day where the README says so), and the Libro, Título and Capítulo headings are not files.

## Source

Asamblea Legislativa de la República de El Salvador, Índice Legislativo (https://www.asamblea.gob.sv/leyes-y-decretos), retrieved 29 October 2026. Article 50 of the Ley de Propiedad Intelectual (D.L. 66/2024) allows laws to be published faithful to the official text without authorisation.

No AI model wrote or changed legal text. This is not legal advice and not an official publication; for anything that matters, read the original.
