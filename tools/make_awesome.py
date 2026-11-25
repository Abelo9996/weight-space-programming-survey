"""Generate awesome/README.md from the corpus notes, organized by the survey taxonomy."""
import json, glob, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ov = json.load(open(os.path.join(ROOT, 'corpus', 'overrides.json')))
found = json.load(open(os.path.join(ROOT, 'corpus', 'foundations_meta.json')))
notes = []
for f in glob.glob(os.path.join(ROOT, 'corpus', 'notes', '*.json')):
    n = json.load(open(f)); n.update(ov.get(n['id'], {}))
    if n.get('is_wsp') in ('core', 'peripheral'):
        notes.append(n)
BR = [('B1', 'Reading weights', 'Weights to description: what a network computes, what it was trained on, whether it hides a flaw.'),
      ('B2', 'Writing networks', 'Specification to weights, from scratch.'),
      ('B3', 'Repairing and editing', 'Changing a trained network to fix, alter or implant behavior.'),
      ('B4', 'Feedback and search loops', 'The editor iterates on experimental, verifier or benchmark feedback.'),
      ('B5', 'Efficient and non-LLM solvers', 'Replacing or amortizing the LLM editor: solvers, closed-form edits, theory.'),
      ('B6', 'Self-editing', 'A model edits its own weights. The open direction toward recursive self-improvement.')]
def link(n):
    return n.get('url') or (f"https://arxiv.org/abs/{n['id']}" if not n['id'].startswith('zenodo') else f"https://doi.org/10.5281/{n['id']}")
def auth(n):
    a = n.get('authors') or []
    return (a[0] + (' et al.' if len(a) > 2 else (' and ' + a[1] if len(a) == 2 else ''))) if a else ''
def one(s, k=200):
    s = ' '.join(str(s).split()); return s if len(s) <= k else s[:k].rsplit(' ', 1)[0] + '...'
L = ['# Awesome Weight-Space Programming', '',
     'A curated, taxonomy-organized list of research on **weight-space programming (WSP)**: a model, usually an LLM, reads, writes or edits the weights of a neural network directly, without an optimizer authoring the values.', '',
     'Companion to *Weight-Space Programming: A Survey and Roadmap* (Yagubyan, University of Georgia, 2026). Every entry below was read in full or partially (marked) for the survey. One-line summaries are neutral descriptions, not rankings.', '',
     '> Literature cut-off: 2026-11-25. Contributions welcome via pull request (see bottom).', '',
     '## Contents', '- [Origin](#origin)']
for b, t, _ in BR:
    L.append(f'- [{b} {t}](#{(b + "-" + t).lower().replace(" ", "-")})')
L += ['- [Evaluation, audits and replications](#evaluation-audits-and-replications)', '- [Safety and security](#safety-and-security)', '- [Verification](#verification)', '- [Surveys](#surveys)', '- [Foundations and precursors](#foundations-and-precursors)', '- [Taxonomy codes](#taxonomy-codes)', '- [Citation](#citation)', '',
      '## Origin', '- **Sparks of Weight-Space Programming: LLMs can natively read & write neural network weights**. Takehi, Teoh, Zhang, Khattab (MIT CSAIL). Blog post, 2026-11-02. [[Post](https://rikiyat.github.io/blog/weight-space-programming/)] [[Logs](https://github.com/RikiyaT/lm_understand-logs)]', '']
def entry(n):
    codes = n['primary_branch'] + ''.join('/' + x for x in (n.get('secondary_branches') or []))
    part = '' if str(n.get('read_level', '')).lower().startswith('full') else ' *(partially read)*'
    code = n.get('code_or_data') or ''
    m = re.search(r'https?://\S+', code)
    extra = f' [[Code]({m.group(0).rstrip(").,;")})]' if m else ''
    return f"- **{n['title']}**. {auth(n).rstrip('.')}. {n.get('date','')}. `{codes}` [[Paper]({link(n)})]{extra}{part}  \n  {one(n.get('why_wsp',''))}"
for b, t, d in BR:
    L += [f'## {b} {t}', f'*{d}*', '']
    for n in sorted([n for n in notes if n['primary_branch'] == b], key=lambda n: n.get('date', '')):
        L.append(entry(n))
    L.append('')
def facet(n, k): return any(str(f).lower().startswith(k) for f in (n.get('facets') or []))
for title, k in [('Evaluation, audits and replications', 'evaluation'), ('Safety and security', 'safety'), ('Verification', 'verification')]:
    L += [f'## {title}', '*Cross-listed from the branches above.*', '']
    for n in sorted([n for n in notes if facet(n, k)], key=lambda n: n.get('date', '')):
        L.append(f"- {n['title']} ({auth(n)}, {n.get('date','')}) [[Paper]({link(n)})] `{n['primary_branch']}`")
    L.append('')
L += ['## Surveys',
      '- Weight-Space Programming with Large Language Models: A Survey. B. Türkoğlu, 2026-11-23. [[Repo](https://github.com/bturkoglu/weight-space-programming-survey)]',
      '- Weight-space programming: methods, cost and limits (in Chinese). 2026-11-09. [[Repo](https://github.com/emecii/weight-space-programming-survey)]',
      '- Weight-Space Programming: A Survey and Roadmap. Abel Yagubyan, 2026. [[Paper](https://github.com/Abelo9996/weight-space-programming-survey/blob/main/paper/wsp-survey.pdf)]', '',
      '## Foundations and precursors', '*Background work WSP builds on (see Section 2 of the survey).*', '']
groups = {'Weights as programs': ['2102.11174', '2106.06981', '2301.05062'],
          'Weight space learning and symmetry': ['2002.11448', '2110.06296', '2209.04836', '2301.12780', '2302.14040', '2209.12892', '2603.10090'],
          'Hypernetworks and parameter generators': ['1609.09106', '2506.06105', '2506.16406'],
          'Model editing and interpretability': ['2104.08696', '2202.05262', '2210.07229', '2110.11309', '2212.04089', '2406.11717', '2307.12976', '2401.07453'],
          'Self-improvement': ['cs/0309048', '2310.02304', '2410.15639', '2506.10943', '2601.14532', '2505.22954', '2506.13131'],
          'Robustness of edits and unlearning': ['2410.16454', '2405.18137', '2401.01814', '2310.03693', '2409.18025'],
          'Trained weight readers (pre-WSP)': ['2610.07334']}
for g, ids in groups.items():
    L.append(f'**{g}**')
    for i in ids:
        if i in found:
            m = found[i]; L.append(f"- {m['title']}. {m['authors'][0]}{' et al.' if len(m['authors'])>1 else ''}, {m['published'][:4]}. [[arXiv](https://arxiv.org/abs/{i})]")
        else:
            n = next((n for n in notes if n['id'] == i), None)
            if n: L.append(f"- {n['title']}. {auth(n)}, {n.get('date','')[:4]}. [[arXiv]({link(n)})]")
    L.append('')
L += ['## Taxonomy codes', '| Code | Meaning |', '|---|---|'] + [f'| {b} | {t}: {d} |' for b, t, d in BR] + [
      '', 'Secondary codes follow a slash, e.g. `B3/B4`. See Section 3 of the survey for the authorship (I1-I4), loop and reference axes.', '',
      '## Contributing', 'Open a pull request adding one line in the matching branch: title, first author, first-version date, primary/secondary code, link, and a one-sentence neutral description of who edits what and how. Please do not add rankings or adjectives.', '',
      '## Citation', '```bibtex', '@misc{yagubyan2026wspsurvey,', '  title  = {Weight-Space Programming: A Survey and Roadmap},', '  author = {Yagubyan, Abel},', '  year   = {2026}', '}', '```', '']
open(os.path.join(ROOT, 'awesome', 'README.md'), 'w').write('\n'.join(L))
print(len(L), 'lines')
