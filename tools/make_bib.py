"""Generate paper/refs.bib from verified metadata only.

Sources:
  corpus/foundations_meta.json  arXiv API metadata for background papers
  corpus/notes/*.json           reader notes (title/authors read from the paper itself)
  corpus/corpus.json            arXiv API / record metadata (fallback for authors)
  corpus/manual_refs.bib        hand-entered non-arXiv references (listed in UNVERIFIED.md)

Keys: arXiv papers use  ax<id with dot replaced>  (e.g. ax2611_14210), Zenodo records
use  zen<record>. Background papers additionally get a readable alias table in
corpus/bib_aliases.json, but the canonical key is still the id-based one, so a key can
never point at a paper that was not resolved.
"""
import json, re, glob, os, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C = os.path.join(ROOT, 'corpus')


def tex_escape(s):
    s = s.replace('\\', ' ').replace('&', r'\&').replace('%', r'\%').replace('#', r'\#').replace('_', r'\_').replace('$', r'\$')
    return s


def key_for(pid):
    if pid.startswith('zenodo.'):
        return 'zen' + pid.split('.', 1)[1]
    return 'ax' + pid.replace('.', '_').replace('/', '_')


def year(d):
    return d[:4]


SURNAME = {  # compound surnames BibTeX would split wrongly
    'Eduardo C. Garrido-Merchán': '{Garrido-Merchán}, Eduardo C.',
    'Eduardo C. Garrido Merchán': '{Garrido-Merchán}, Eduardo C.',
    'Miquel Noguer i Alonso': '{Noguer i Alonso}, Miquel',
    'Miquel Noguer Alonso': '{Noguer i Alonso}, Miquel',
}

entries = {}

found = json.load(open(os.path.join(C, 'foundations_meta.json')))
for pid, m in found.items():
    entries[key_for(pid)] = dict(type='misc', title=m['title'], author=' and '.join(m['authors']),
                                 year=year(m['published']), eprint=pid, url=f'https://arxiv.org/abs/{pid}')

corpus = {p['id']: p for p in json.load(open(os.path.join(C, 'corpus.json')))}
for f in sorted(glob.glob(os.path.join(C, 'notes', '*.json'))):
    n = json.load(open(f))
    pid = n['id']
    base = corpus.get(pid, {})
    # record metadata (arXiv API / Zenodo record) is authoritative for title and authors,
    # so a reader searching the listing finds the cited title; notes are the fallback
    authors = [a.strip() for a in (base.get('authors') or n.get('authors') or [])]
    title = base.get('title') or n.get('title')
    authors = [SURNAME.get(a, a) for a in authors]
    date = n.get('date') or base.get('published', '2026')
    authors = ['{' + a + '}' if re.search(r'\b(Research|scientist|AI)\b', a) else a for a in authors]
    e = dict(type='misc', title=title, author=' and '.join(authors), year=year(date))
    if pid.startswith('zenodo.'):
        e['url'] = base.get('url') or n.get('url')
        e['howpublished'] = 'Zenodo record'
    else:
        e['eprint'] = pid
        e['url'] = f'https://arxiv.org/abs/{pid}'
    entries[key_for(pid)] = e

out = []
for k in sorted(entries):
    e = entries[k]
    lines = [f"@{e['type']}{{{k},"]
    lines.append(f"  title = {{{{{tex_escape(e['title'])}}}}},")
    lines.append(f"  author = {{{tex_escape(e['author'])}}},")
    lines.append(f"  year = {{{e['year']}}},")
    if 'eprint' in e:
        lines.append(f"  eprint = {{{e['eprint']}}},")
        lines.append("  archivePrefix = {arXiv},")
        lines.append(f"  howpublished = {{arXiv:{e['eprint']}}},")
    elif 'howpublished' in e:
        lines.append(f"  howpublished = {{{e['howpublished']}}},")
    lines.append(f"  url = {{{e['url']}}}")
    lines.append('}')
    out.append('\n'.join(lines))

manual = os.path.join(C, 'manual_refs.bib')
if os.path.exists(manual):
    out.append(open(manual).read())

open(os.path.join(ROOT, 'paper', 'refs.bib'), 'w').write('\n\n'.join(out) + '\n')
print(len(entries), 'generated entries')
