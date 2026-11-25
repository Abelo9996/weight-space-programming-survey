"""Recount editor token usage of the original Sparks 50-pass Qwen run from the released logs.

Usage:
  git clone --depth 1 --filter=blob:none --sparse https://github.com/RikiyaT/lm_understand-logs.git logs
  (cd logs && git sparse-checkout set --no-cone 'exp8_math/runs/p50c/turns/*/run.json')
  python3 tools/recount_tokens.py logs/exp8_math/runs/p50c/turns
"""
import json, glob, sys, itertools, os
d = sys.argv[1]
rows = []
for f in sorted(glob.glob(os.path.join(d, '*', 'run.json'))):
    a = json.load(open(f))['audit']
    rows.append((a.get('thread_id'), a['usage']))
naive = sum(u['input_tokens'] + u['output_tokens'] for _, u in rows)
last = {}
for t, u in rows:
    last[t] = u
last_sum = sum(u['input_tokens'] + u['output_tokens'] for u in last.values())
peaks = 0
for t, g in itertools.groupby(rows, key=lambda r: r[0]):
    prev = None
    for _, u in g:
        if prev and u['input_tokens'] < prev['input_tokens']:
            peaks += prev['input_tokens'] + prev['output_tokens']
        prev = u
    peaks += prev['input_tokens'] + prev['output_tokens']
print(f'turns={len(rows)} conversations={len(last)}')
print(f'naive sum over turns:          {naive/1e6:.2f}M')
print(f'last turn per conversation:    {last_sum/1e6:.2f}M')
print(f'sum of peaks before drops:     {peaks/1e6:.2f}M  (overcounts plateaus; not used in the paper)')

# Plateau-aware count. After a harness restart, a conversation's cumulative counter can stall:
# each later turn reports the restart state plus one call. A stall is a run of >= 3 turns within
# 1% of each other. Count the restart state (the turn before the stall) once, plus each stalled
# turn's increment over it. Conversations without a stall contribute their last cumulative value.
plateau = 0
for t, g in itertools.groupby(rows, key=lambda r: r[0]):
    g = [u['input_tokens'] + u['output_tokens'] for _, u in g]
    total, i = None, 0
    while i < len(g):
        j = i
        while j + 1 < len(g) and abs(g[j + 1] - g[i]) <= 0.01 * g[i]:
            j += 1
        if j - i >= 2:
            prev = g[i - 1] if i else 0
            total = prev + sum(x - prev for x in g[i:j + 1])
            i = j + 1
        else:
            i += 1
    plateau += max(total, g[-1]) if total is not None else g[-1]
print(f'plateau-aware count:           {plateau/1e6:.2f}M')
