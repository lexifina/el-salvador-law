"""Add the Índice Legislativo decrees (corpus.d/30-acts-*.json with a .PUBLISH) to repo/README.md and repo/LICENSE,
between markers. Deterministic; reads only the parts.

    python -X utf8 w3_docs.py
"""
import json
import re
from pathlib import Path

H = Path(__file__).resolve().parent
parts = sorted(p for p in (H / 'corpus.d').glob('30-acts-*.json') if p.with_suffix('.PUBLISH').exists())
acts = [a for p in parts for a in json.loads(p.read_text('utf-8'))['acts']]
acts.sort(key=lambda a: (a['slug']))
n = len(acts)
units = sum(len(a['versions'][0]['units']) for a in acts)
reformed = sum(1 for a in acts if not a['versions'][0]['note'].startswith('The decree as published'))
A0, A1 = '<!-- acts:start -->', '<!-- acts:end -->'
rows = '\n'.join(f"| `{a['slug']}/` | [{a['title'].replace('|', '/')}]({a['url']}) | {a['versions'][0]['from']} |"
                 for a in acts)
SECTION = f"""{A0}
## Decrees from the Índice Legislativo

{n} decrees (laws, codes and other legislative decrees), {units:,} files, one folder per decree named by its year and number (`decreto-1940-0017/` is Decreto N° 17 de 1940, the Ley de Asuetos, Vacaciones y Licencias de los Empleados Públicos). Each is one version: the text the Asamblea Legislativa's Índice Legislativo prints today, with its reforms worked in ({reformed} of them have reforms).

**Dates.** A decree with no reform listed is dated by its own entry into force: its vigencia article when it says "desde ... su publicación" or "n días después de su publicación", otherwise eight days after its Diario Oficial publication (Constitución art. 140). A reformed decree's text is dated eight days after the Diario Oficial publication of the latest reform in the Índice's list, and credited to that reform; earlier wordings are not shown, so the history of a reformed decree starts with today's text on that day. Where the reform list could not be read, the decree is dated by the day it was retrieved (3 November 2026).

**How it was checked.** Read from the text layer of the Índice's born-digital PDFs; no OCR. Every word before the Diario Oficial block is in a file, in order, except page headers, the reform markers "(n)" at the end of reformed paragraphs and editors' notes; `preambulo.md` holds the text before Art. 1, `art-NNN.md` each article (`art-010-bis.md` is Art. 10 bis), and `firma.md` the "DADO EN ..." closing with the signatures. A decree whose articles are not numbered 1, 2, 3 and so on, each once, is left out, and so are temporary decrees, which may have lapsed.

| Folder | Decree | In force from |
| --- | --- | --- |
{rows}
{A1}"""


def put(path: Path, text: str, anchor: str | None) -> None:
    s = path.read_text('utf-8') if path.exists() else ''
    if A0 in s:
        s = re.sub(re.escape(A0) + '.*?' + re.escape(A1), lambda m: text, s, flags=re.S)
    elif anchor and anchor in s:
        s = s.replace(anchor, text + '\n\n' + anchor, 1)
    else:
        s = s.rstrip('\n') + '\n\n' + text + '\n'
    path.write_text(s, 'utf-8', newline='\n')


put(H / 'repo' / 'README.md', SECTION, '## Source')
LIC = f"""{A0}
Decrees in the folders decreto-YYYY-NNNN/: the texts of the Asamblea Legislativa's Índice Legislativo
(https://www.asamblea.gob.sv/leyes-y-decretos/decretos-por-anios), retrieved November 2026, under the same article 50
of the Ley de Propiedad Intelectual.
{A1}"""
put(H / 'repo' / 'LICENSE', LIC, 'The arrangement of this repository')
print(n, 'acts', units, 'units')
