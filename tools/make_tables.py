"""Build the generated LaTeX pieces from reader notes.

Writes:
  paper/tables/stats.tex        \newcommand macros with corpus counts
  paper/tables/papers_table.tex full longtable of WSP studies (appendix)
  corpus/branch_counts.json     counts per branch / interface / loop / facet
"""
import json, glob, os, re, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C = os.path.join(ROOT, 'corpus')
P = os.path.join(ROOT, 'paper')

EXTRA = {}  # manual overrides: id -> dict(field=value), from corpus/overrides.json
ov = os.path.join(C, 'overrides.json')
if os.path.exists(ov):
    EXTRA = json.load(open(ov))


def key_for(pid):
    return ('zen' + pid.split('.', 1)[1]) if pid.startswith('zenodo.') else 'ax' + pid.replace('.', '_')


def esc(s):
    s = str(s)
    for a, b in [('\\', ' '), ('&', r'\&'), ('%', r'\%'), ('#', r'\#'), ('_', r'\_'), ('$', r'\$'), ('~', ' '), ('^', ' ')]:
        s = s.replace(a, b)
    return s


def brk(s):
    # let long model names wrap inside narrow columns
    return re.sub(r'([-/])(?=\S)', lambda m: m.group(1) + '\\allowbreak ', s)


def short(s, n):
    s = re.sub(r'\s+', ' ', str(s)).strip()
    s = re.split(r'[;(]|: |, also| plus ', s)[0].strip().rstrip(',') or s
    s = s.replace('"', '').replace("'", '')
    s = re.sub(r'\s*\(.*?\)', '', s) if len(s) > n else s
    if len(s) <= n:
        return s
    cut = s[:n].rsplit(' ', 1)[0].rstrip(',;:')
    return cut + '...'


def interface_code(n):
    if n.get('code_I'):  # hand-coded correction (corpus/overrides.json)
        return n['code_I']
    ed = (n.get('editor') or '').lower()
    it = (n.get('interface') or '').lower()
    if ed.startswith('none') or 'no llm' in ed:
        return 'I4'
    if 'solver' in it:
        return 'I3'
    if 'direct' in it:
        return 'I1'
    if 'code' in it or 'tool' in it or 'closed' in it:
        return 'I2'
    return '--'


def loop_code(n):
    if n.get('code_L'):  # hand-coded correction (corpus/overrides.json)
        return n['code_L']
    l = (n.get('loop') or '').lower()
    if 'search' in l:
        return 'S'
    if 'closed' in l or 'feedback' in l or 'iter' in l:
        return 'C'
    if 'one' in l:
        return 'O'
    return '--'


notes = []
for f in sorted(glob.glob(os.path.join(C, 'notes', '*.json'))):
    n = json.load(open(f))
    n.update(EXTRA.get(n['id'], {}))
    notes.append(n)

included = [n for n in notes if n.get('is_wsp') in ('core', 'peripheral')]
core = [n for n in notes if n.get('is_wsp') == 'core']
excluded = [n for n in notes if n.get('is_wsp') not in ('core', 'peripheral')]

prim = collections.Counter(n['primary_branch'] for n in included)
anyb = collections.Counter()
for n in included:
    for b in set([n['primary_branch']] + list(n.get('secondary_branches') or [])):
        anyb[b] += 1
iface = collections.Counter(interface_code(n) for n in included)
loops = collections.Counter(loop_code(n) for n in included)
facets = collections.Counter()
for n in included:
    fs = set()
    for f in (n.get('facets') or []):
        for k in ('evaluation', 'verification', 'safety', 'replication', 'benchmark'):
            if f.lower().startswith(k):
                fs.add(k)
    facets.update(fs)
selfed = [n['id'] for n in included if str(n.get('self_editing', '')).lower().startswith('yes')]

counts = dict(n_notes=len(notes), n_included=len(included), n_core=len(core), n_excluded=len(excluded),
              n_arxiv=sum(1 for n in included if not n['id'].startswith('zenodo')),
              n_zenodo=sum(1 for n in included if n['id'].startswith('zenodo')),
              primary=dict(prim), any=dict(anyb), interface=dict(iface), loop=dict(loops), facets=dict(facets),
              self_editing=selfed,
              by_branch={b: sorted(n['id'] for n in included if n['primary_branch'] == b) for b in prim},
              by_branch_any={b: sorted(n['id'] for n in included if b == n['primary_branch'] or b in (n.get('secondary_branches') or [])) for b in anyb},
              excluded=[(n['id'], n.get('is_wsp'), n.get('why_wsp', '')[:120]) for n in excluded])
counts = {k: (sorted(v) if isinstance(v, list) else {kk: (sorted(vv) if isinstance(vv, list) else vv) for kk, vv in sorted(v.items())} if isinstance(v, dict) else v) for k, v in counts.items()}
json.dump(counts, open(os.path.join(C, 'branch_counts.json'), 'w'), indent=1, sort_keys=True)

word = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}
macros = {
    'nIncluded': len(included), 'nCore': len(core), 'nArxiv': counts['n_arxiv'], 'nZenodo': counts['n_zenodo'],
    'nExcluded': len(excluded), 'nScreened': len(notes),
}
W = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six'}
for b in ['B1', 'B2', 'B3', 'B4', 'B5', 'B6']:
    macros['nB' + W[b[1]]] = prim.get(b, 0)
    macros['nAnyB' + W[b[1]]] = anyb.get(b, 0)
for i in ['I1', 'I2', 'I3', 'I4']:
    macros['nI' + W[i[1]]] = iface.get(i, 0)
macros['nOneShot'] = loops.get('O', 0)
macros['nClosedLoop'] = loops.get('C', 0) + loops.get('S', 0)
macros['nSelfEditing'] = len(selfed)
macros['nCodeOverrides'] = sum(1 for k, v in EXTRA.items() if 'code_I' in v or 'code_L' in v)
macros['nPartialAll'] = sum(1 for n in notes if not str(n.get('read_level','')).lower().startswith('full'))
macros['nPeripheral'] = len(included) - len(core)
macros['nPartial'] = sum(1 for n in included if not str(n.get('read_level','')).lower().startswith('full'))
for fct in ['evaluation', 'verification', 'safety']:
    macros['nFacet' + fct.capitalize()] = facets.get(fct, 0)
scr = []
for f in sorted(glob.glob(os.path.join(C, 'screening_*.json'))):
    scr += json.load(open(f))['records']
macros['nUpdateIdentified'] = len(scr)
macros['nUpdateTitleExcluded'] = sum(1 for r in scr if r['stage'] == 'excluded_title_abstract')
macros['nUpdateMerged'] = sum(1 for r in scr if r['stage'] == 'merged')
macros['nUpdateFullText'] = sum(1 for r in scr if r['stage'] == 'full_text')
macros['nFirstRound'] = len(notes) - macros['nUpdateFullText']
with open(os.path.join(P, 'tables', 'stats.tex'), 'w') as fh:
    fh.write('% generated by tools/make_tables.py; do not edit\n')
    for k, v in macros.items():
        fh.write(f'\\newcommand{{\\{k}}}{{{v}}}\n')

rows = []
for n in sorted(included, key=lambda n: (n.get('date', ''), n['id'])):
    br = n['primary_branch'] + ''.join('/' + b for b in (n.get('secondary_branches') or []) if b != n['primary_branch'])
    selfref = n['id'] in selfed
    rows.append(' & '.join([
        f"\\citet{{{key_for(n['id'])}}}",
        esc(n.get('date', '')[5:]),
        esc(br).replace('/', '/\\allowbreak ') + ('$^{\\ast}$' if selfref else '') + ('' if n.get('is_wsp') == 'core' else '$^{\\dagger}$'),
        interface_code(n), loop_code(n),
        brk(esc(short(n.get('domain', ''), 38))),
        brk(esc(short(n.get('editor', ''), 30))),
        brk(esc(short(n.get('target', ''), 34))),
    ]) + r' \\')

with open(os.path.join(P, 'tables', 'papers_table.tex'), 'w') as fh:
    fh.write('% generated by tools/make_tables.py; do not edit\n')
    fh.write(r'''{\footnotesize
\setlength{\tabcolsep}{3pt}
\begin{longtable}{>{\raggedright\arraybackslash}p{2.6cm} l >{\raggedright\arraybackslash}p{1.3cm} c c >{\raggedright\arraybackslash}p{3.3cm} >{\raggedright\arraybackslash}p{2.6cm} >{\raggedright\arraybackslash}p{3.0cm}}
\caption{All weight-space programming studies in the corpus, ordered by first-version date (2026). Branch: primary/secondary (\cref{sec:defs}); $^{\ast}$ marks the studies whose reference (axis 4) is the editor itself, all others edit another model; $^{\dagger}$ marks peripheral studies (closed-form or solver studies with no LLM editor, baselines and evaluations). If: who authors the numbers, I1--I4. L: loop (O one-shot, C closed-loop, S search); studies with both one-shot and closed-loop arms are coded C. -- means not applicable (no edit authored, proposal only) or not stated. If and L were first derived by rule from the free-text fields of the reading notes and then corrected by hand where the rule disagreed with the note. Domain, editor and target are abbreviated from the papers; see the cited work for full details.}\label{tab:papers}\\
\toprule
Study & Date & Branch & If & L & Domain & Editor & Target \\
\midrule
\endfirsthead
\toprule
Study & Date & Branch & If & L & Domain & Editor & Target \\
\midrule
\endhead
\bottomrule
\endfoot
''')
    fh.write('\n'.join(rows))
    fh.write('\n\\end{longtable}}\n')

print(json.dumps({k: v for k, v in counts.items() if k not in ('by_branch', 'by_branch_any', 'excluded')}, indent=0))
print('excluded:', counts['excluded'])

# consistency check: every study cited in a taxonomy leaf must be included and carry that branch
inc = {key_for(n['id']): n for n in included}
bad = []
for b in ['B1', 'B2', 'B3', 'B4', 'B5', 'B6']:
    t = open(os.path.join(P, 'figures', f'leaves_{b}.tex')).read()
    for k in re.findall(r'\\citep\{([^}]*)\}', t):
        for key in k.split(','):
            if key in ('takehi2026sparks',):
                continue
            n = inc.get(key)
            if n is None or (b != n['primary_branch'] and b not in (n.get('secondary_branches') or [])):
                bad.append((b, key, None if n is None else n['primary_branch']))
print('leaf check:', 'OK' if not bad else bad)
