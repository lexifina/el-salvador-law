"""Rewrites repo/README.md and repo/LICENSE for the codes listed on the command line (idempotent from the base copies)."""
import pathlib, sys
H = pathlib.Path(__file__).parent
R = H / 'repo'
want = sys.argv[1:]
ROWS = {
 'penal': "| `codigo-penal/` | Código Penal (Decreto Legislativo n.º 1030 of 26 April 1997, in force 20 April 1998): preamble and Arts. 1 to 409, with the lettered articles | 1 | The current consolidated text, including every reform up to Decreto Legislativo n.º 537 of 26 March 2026, dated from its Diario Oficial of 27 March 2026 |\n",
 'civil': "| `codigo-civil/` | Código Civil (declared law by the Poder Ejecutivo on 23 August 1859, published 10 April 1860): promulgating decree, Arts. 1 to 2263 and the final article | 1 | The current consolidated text, including every reform up to Decreto Legislativo n.º 294 of 22 February 2022, dated from its Diario Oficial of 26 April 2022 |\n",
 'comercio': "| `codigo-de-comercio/` | Código de Comercio (Decreto Legislativo n.º 671 of 8 May 1970): preamble and Arts. 1 to 1566 (Arts. 15 and 456 are not in the source text) | 1 | The current consolidated text, including every reform up to Decreto Legislativo n.º 972 of 19 March 2024, dated from its Diario Oficial of 11 April 2024 |\n",
 'trabajo': "| `codigo-de-trabajo/` | Código de Trabajo (Decreto Legislativo n.º 15 of 23 June 1972): Arts. 1 to 637, with the lettered articles | 1 | The current consolidated text, including every reform up to Decreto Legislativo n.º 669 of 23 September 2026, dated 24 September 2026, the day that reform took effect (on its publication) |\n",
 'procesal': "| `codigo-procesal-penal/` | Código Procesal Penal (Decreto Legislativo n.º 733 of 22 October 2008): preamble and Arts. 1 to 506, with the lettered articles (502-A onwards on extradition and assistance) | 1 | The current consolidated text, including every reform up to Decreto Legislativo n.º 534 of 26 March 2026, dated 26 April 2026, the day that reform took effect (thirty days after its publication) |\n",
}
base = H / 'README.base.txt'
if not base.exists():
    base.write_text((R / 'README.md').read_text(encoding='utf-8'), encoding='utf-8', newline='')
    (H / 'LICENSE.base.txt').write_text((R / 'LICENSE').read_text(encoding='utf-8'), encoding='utf-8', newline='')
s = base.read_text(encoding='utf-8')
s = s.replace("The Constitution of El Salvador as a git repository: one file per article,", "The Constitution of El Salvador and its core codes as a git repository: one file per article,", 1)
i = s.index("| `constitucion/`")
j = s.index("\n", i) + 1
s = s[:j] + ''.join(ROWS[w] for w in want) + s[j:]
s = s.replace("- File names: `art-005.md` is Article 5.", "- File names: `art-005.md` is Article 5. In the codes, each file is one article with the same limits: one version each, dated from the last reform in the source's list (its Diario Oficial date, or its in-force day where the README says so), and the Libro, Título and Capítulo headings are not files.")
(R / 'README.md').write_text(s, encoding='utf-8', newline='')
lic = (H / 'LICENSE.base.txt').read_text(encoding='utf-8')
lic = lic.replace("The legal text is the Constitution of El Salvador as published", "The legal text is the Constitution of El Salvador" + (", and the codes listed in the README," if want else "") + " as published", 1)
(R / 'LICENSE').write_text(lic, encoding='utf-8', newline='')
