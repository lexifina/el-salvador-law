import re, json, hashlib, pymupdf, sys
raw = open('src2/cn.pdf','rb').read()
sha = hashlib.sha256(raw).hexdigest()
d = pymupdf.open('src2/cn.pdf')
lines = []
for p in d:
    ls = p.get_text().split('\n')
    # drop header: through the "ÍNDICE LEGISLATIVO" line and the page number after it
    for i, l in enumerate(ls[:10]):
        if 'ÍNDICE LEGISLATIVO' in l:
            ls = ls[i+2:]; break
    lines += ls + ['']
text = '\n'.join(lines)
end = text.index('DADO EN EL SALON')
text = text[:end]
def clean(s):
    s = s.replace('\xa0', ' ')
    s = re.sub(r'\s*\((\d{1,2})\)', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s
STRUCT = re.compile(r'^(TITULO|CAPITULO|SECCION|DISPOSICIONES|C O N S T I T U C I O N|[IVXL]+$)')
# split into chunks by Art.
parts = re.split(r'(?m)^(?=Art\. ?\d+\.-)', text)
units = {}
pre = parts[0]
def paras(block):
    out, cur = [], []
    for l in block.split('\n'):
        if l.strip() == '':
            if cur: out.append(' '.join(cur)); cur = []
        else: cur.append(l.strip())
    if cur: out.append(' '.join(cur))
    return out
def drop_struct(ps):
    # structural headings (Titulo/Capitulo/Seccion plus their title lines) trail the previous article; cut at first one
    res = []
    for p in ps:
        if STRUCT.match(p.strip()): break
        res.append(p)
    return res
pp = paras(pre)
pp = [p for p in pp if not re.match(r'^(_+|C O N S T I T U C I O N)', p)]
# preamble: Decreto No. 38 .. DECRETAMOS...
i = [k for k,p in enumerate(pp) if p.startswith('DECRETAMOS')][0]
pp = [clean(p) for p in pp[:i+1]]
units['preambulo'] = {'label': 'Preámbulo', 'kind': 'preamble', 'text': '# Preámbulo\n' + '\n'.join(pp) + '\n'}
seq = []
for part in parts[1:]:
    m = re.match(r'Art\. ?(\d+)\.-', part)
    n = int(m.group(1)); seq.append(n)
    ps = paras(part)
    ps = drop_struct(ps)
    ps = [clean(p) for p in ps]
    ps = [p for p in ps if p]
    body = ps[0]
    units['art-%03d' % n] = {'label': 'Art. %d' % n, 'kind': 'art', 'text': '# Art. %d\n' % n + '\n'.join(ps) + '\n'}
assert seq == list(range(1, 275)), seq[:5]
bad = [k for k,u in units.items() if re.search(r'\(\d+\)', u['text'])]
print(len(units), 'bad', bad)
law = {'label': 'D.L. 570/2026', 'title': 'Reforma a la Constitución de la República (última reforma recogida: Decreto Legislativo n.º 570, 7 de mayo de 2026)', 'kind': 'decree', 'enacted': '2026-05-07', 'published': '2026-05-07', 'url': 'https://www.asamblea.gob.sv/sites/default/files/2026-05/1.%20CONSTITUCI%C3%93N%20DE%20LA%20REP%C3%9ABLICA.pdf', 'temporary_until': None, 'restores': None, 'note': None}
corpus = {
 'country': {'code':'SV','name':'El Salvador','slug':'el-salvador','lang':'es','tz':'America/El_Salvador','future_branch':'futuro',
   'publisher': {'name':'Asamblea Legislativa de la República de El Salvador (Índice Legislativo)','email':'indice@asamblea.invalid'},
   'default_in_force_rule': {'text':'Constitución art. 140: la ley entra en vigencia ocho días después de su publicación en el Diario Oficial, salvo que el propio decreto disponga otra cosa','source':'https://www.asamblea.gob.sv'},
   'licence_note':'Texto oficial de la Constitución según el Índice Legislativo de la Asamblea Legislativa de El Salvador (asamblea.gob.sv). La Ley de Propiedad Intelectual (D.L. 66/2024), art. 50, permite publicar las leyes con apego al texto oficial.'},
 'sources':[{'name':'Asamblea Legislativa de El Salvador, Índice Legislativo','url':'https://www.asamblea.gob.sv/leyes-y-decretos','retrieved':'2026-10-29','requests':1,'licence':'Official legislative text; Ley de Propiedad Intelectual (D.L. 66/2024) art. 50 allows publication of laws faithful to the official text','notes':'Constitution, 60-page text-layer PDF, 2026 consolidation.'}],
 'laws': {},
 'acts':[{'slug':'constitucion','short':'Cn','title':'Constitución de la República de El Salvador (Decreto Constituyente n.º 38, 1983)','url':'https://www.asamblea.gob.sv/sites/default/files/2026-05/1.%20CONSTITUCI%C3%93N%20DE%20LA%20REP%C3%9ABLICA.pdf','first_law':None,
   'earlier_laws':[],'versions':[{'from':'2026-05-07','source_url':'https://www.asamblea.gob.sv/sites/default/files/2026-05/1.%20CONSTITUCI%C3%93N%20DE%20LA%20REP%C3%9ABLICA.pdf','sha256':sha,'units':units,'credits':{},'note':'Oldest version available: the Índice Legislativo text including all reforms to D.L. 570 of 7 May 2026 (D.O. 83, Tomo 451). Reformed passages are printed in capitals in the source.'}]}],
 'applies':[],
 'decisions':['Only the current consolidated text was available from the Asamblea, so the repository holds one version, dated 2026-05-07, the Diario Oficial date of the last reform listed in the source (D.L. 569 and 570, D.O. 83); the in-force day of the most recent reforms was not checked separately.',
   'Footnote markers (n) for reform references, page headers and the list of signatories were removed; title, chapter and section headings between articles were not kept as units.',
   'Reform references were not credited to individual provisions (the source lists them only as numbers), so the single version is credited to the publisher as oldest version available.'],
 'ai_use':['none']}
json.dump(corpus, open('corpus.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)
