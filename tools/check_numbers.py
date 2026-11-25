"""Flag numbers in the LaTeX that do not appear in any source cited in the same sentence."""
import re, json, glob, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = {}
for f in glob.glob(os.path.join(ROOT, 'corpus', 'notes', '*.json')):
    n = json.load(open(f)); pid = n['id']
    k = ('zen' + pid.split('.', 1)[1]) if pid.startswith('zenodo.') else 'ax' + pid.replace('.', '_')
    src[k] = json.dumps(n, ensure_ascii=False)
# Sources outside the corpus (the original blog post, other surveys) have no stored note.
# Sentences citing only those are reported separately rather than flagged.
NONCORPUS = {'takehi2026sparks', 'turkoglu2026survey', 'emecii2026survey', 'liu2026pathrsi', 'wu2026rsisurvey',
             'arun2026modelsurgery', 'csefalvay2026misfolding', 'savoji2026awesome'}
rec = os.path.join(ROOT, 'RECOUNT.md')
if os.path.exists(rec):
    src['takehi2026sparks'] = open(rec).read()
unchecked = 0
def norm(x): return x.replace(',', '').replace('{', '').replace('}', '')
bad = 0
for f in sorted(glob.glob(os.path.join(ROOT, 'paper', 'sections', '*.tex'))):
    t = open(f).read()
    t = re.sub(r'%.*', '', t)
    for sent in re.split(r'(?<=[.;])\s+(?=[A-Z\\])|\n\s*\n|\\item', t):
        keys = [k.strip() for g in re.findall(r'\\cite[pt]?\{([^}]*)\}', sent) for k in g.split(',')]
        if not keys: continue
        body = re.sub(r'\\cite[pt]?\{[^}]*\}|\\(c|C)ref\{[^}]*\}|\\ref\{[^}]*\}|\\label\{[^}]*\}', '', sent)
        nums = set(re.findall(r'(?<![\w.])\d[\d,{}]*(?:\.\d+)?', body))
        if all(k in NONCORPUS and k not in src for k in keys):
            unchecked += 1
            continue
        hay = norm(' '.join(src.get(k, '') for k in keys))
        for x in nums:
            v = norm(x)
            if len(v.replace('.', '')) < 2 and v not in ('0',): continue
            if v in hay: continue
            bad += 1
            print(f"{os.path.basename(f)} | {x} | keys={','.join(keys)[:60]} | {' '.join(body.split())[:140]}")
print('flagged', bad, '| sentences citing only non-corpus sources (not checked):', unchecked, file=sys.stderr)
