# Recount of the 89.7M-token cost figure

A figure of 89.7M tokens and 15.6 hours for the original Qwen3.5-0.8B edit comes from the Tree-Ising paper (arXiv 2611.14210, Section 1 and Table 4), which derives it from the released logs of the original experiment.

The logs are at https://github.com/RikiyaT/lm_understand-logs. The 50-pass run is `exp8_math/runs/p50c` (158 turns in four conversations). The logs' README (`exp8_math/README.md`) says that per-turn usage "accumulates over a conversation, so do not sum it over turns".

`tools/recount_tokens.py` counts input plus output tokens in three ways:

| Method | Tokens |
|---|---|
| sum over all 158 turns (reproduces the published figure) | 89.69M |
| last turn of each conversation | 5.59M |
| plateau-aware count | 6.46M |

The plateau-aware count handles one feature of the logs. After a harness restart in the first conversation, the cumulative counter stays at about 348k for turns 15 to 40: each of those turns reports the restart state (turn 14) plus one call of about 34k tokens. The count takes the restart state once and adds each stalled turn's increment over it.

Either way, the usage is about 5.6M to 6.5M tokens, roughly an order of magnitude below 89.7M. The 15.6-hour figure is consistent with the logs: 20.3 hours of wall-clock time minus a 4.7-hour period when the model could not be reached.
