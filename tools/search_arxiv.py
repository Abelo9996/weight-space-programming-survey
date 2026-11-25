"""Rerun the Appendix B arXiv search and log every query and result.

Usage: python3 tools/search_arxiv.py YYYY-MM-DD
Writes corpus/search_log_<date>.json with each query, its total hits and the
returned ids, plus a list of candidate ids not yet in corpus.json.
"""
import json, os, sys, time, urllib.parse, urllib.request, re
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C = os.path.join(ROOT, 'corpus')
NS = {'a': 'http://www.w3.org/2005/Atom', 'o': 'http://a9.com/-/spec/opensearch/1.1/'}
QUERIES = [
    'all:"weight-space programming"', 'all:"weight space programming"',
    'abs:"edit its own weights"', 'abs:"writes the weights"', 'abs:"edits the weights"',
    'abs:"LLM edits weights"', 'abs:"directly edit" AND abs:weights AND abs:LLM',
    'abs:"weight editing" AND abs:"language model" AND abs:gradient-free',
    'ti:"weight space" AND abs:LLM AND abs:edit', 'abs:"rewriting its weights"',
    'abs:"tool-free" AND abs:weights AND abs:LLM',
]


def run(q, n=200):
    url = 'https://export.arxiv.org/api/query?' + urllib.parse.urlencode(
        dict(search_query=q, sortBy='submittedDate', sortOrder='descending', max_results=n))
    root = ET.fromstring(urllib.request.urlopen(url, timeout=90).read())
    total = int(root.find('o:totalResults', NS).text)
    out = []
    for e in root.findall('a:entry', NS):
        pid = re.sub(r'v\d+$', '', e.find('a:id', NS).text.rsplit('/abs/', 1)[1])
        out.append(dict(id=pid, title=' '.join(e.find('a:title', NS).text.split()),
                        published=e.find('a:published', NS).text[:10],
                        authors=[a.find('a:name', NS).text for a in e.findall('a:author', NS)],
                        cats=[c.get('term') for c in e.findall('a:category', NS)],
                        abstract=' '.join(e.find('a:summary', NS).text.split())))
    return total, out


date = sys.argv[1]
have = {p['id'] for p in json.load(open(os.path.join(C, 'corpus.json')))}
log, cand = [], {}
for q in QUERIES:
    total, res = run(q)
    log.append(dict(query=q, total=total, ids=[r['id'] for r in res]))
    for r in res:
        if r['id'] not in have and r['published'] >= '2026-11-02':
            cand.setdefault(r['id'], r)
    time.sleep(3.5)
json.dump(dict(run_date=date, queries=log, new_candidates=sorted(cand.values(), key=lambda r: r['id'])),
          open(os.path.join(C, f'search_log_{date}.json'), 'w'), indent=1)
for r in sorted(cand.values(), key=lambda r: r['id']):
    print(r['id'], r['published'], r['title'][:100])
print(len(cand), 'new candidates')
