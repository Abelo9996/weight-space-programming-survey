# Weight-Space Programming: A Survey and Roadmap

Abel Yagubyan, University of Georgia

**Paper:** [`paper/wsp-survey.pdf`](paper/wsp-survey.pdf) (version of November 25, 2026; literature cut-off November 25, 2026)

Weight-space programming (WSP) is the practice of having a model, usually a large language model, read, write or edit the weights of a neural network directly, without an optimizer authoring the values. This survey covers 93 studies posted up to November 25, 2026. It contributes:

- a formal definition and a four-axis taxonomy: six branches from reading to self-editing, who authors the numbers, the loop, and the reference;
- lineage to fast weight programmers, compiled Transformers, weight space learning, hypernetworks, model editing and self-improvement;
- a reliability agenda: reading beyond priors, cheap baselines, variance, verification, and persistence of edits under fine-tuning and quantization, with a proposed retention-ratio protocol;
- five testable conditions under which WSP would amount to recursive self-improvement;
- eleven numbered open problems, each with a checkable target.

The companion paper list, organized by the same taxonomy, is in [`awesome/README.md`](awesome/README.md).

## What is in this repository

| Path | Contents |
|---|---|
| `paper/` | LaTeX source and the compiled PDF |
| `corpus/corpus.json` | the 101 records read from their full text (arXiv and Zenodo; 19 of them only in part), with metadata |
| `corpus/notes/<id>.json` | one reading note per record, following [`EXTRACTION_FORM.md`](EXTRACTION_FORM.md); every recorded number has a verbatim quote and its location in the source |
| `corpus/overrides.json` | hand corrections to the taxonomy codes, duplicate merges and date fixes |
| `corpus/search_log_2026-11-25.json` | every query of the November 25 update search, with hit counts and returned ids |
| `corpus/screening_2026-11-25.json` | every record considered in the update, with its screening stage and a one-line exclusion reason |
| `corpus/foundations_meta.json`, `corpus/manual_refs.bib` | background references (arXiv metadata and hand-entered entries) |
| `tools/` | scripts that generate every count, table, the bibliography and the paper list from the notes |
| [`RECOUNT.md`](RECOUNT.md) | how the 89.7M-token cost figure for the original edit was recounted from the released logs |

## Reproduce

```
python3 tools/make_bib.py        # paper/refs.bib from record metadata
python3 tools/make_tables.py     # paper/tables/stats.tex, papers_table.tex; checks the Figure 1 leaves
python3 tools/make_awesome.py    # awesome/README.md
python3 tools/check_numbers.py   # flags numbers in the text that are not in a cited note
cd paper && latexmk -pdf main.tex
```

The token recount needs the public logs of the original experiment:

```
git clone --depth 1 https://github.com/RikiyaT/lm_understand-logs.git logs
python3 tools/recount_tokens.py logs/exp8_math/runs/p50c/turns
```

## Corrections and additions

New WSP studies appear daily. Open an issue or a pull request with the link, or with a correction to a note (quote the source and give its location). The survey will be updated in dated versions.

## Citation

```bibtex
@misc{yagubyan2026wspsurvey,
  title  = {Weight-Space Programming: A Survey and Roadmap},
  author = {Abel Yagubyan},
  year   = {2026},
  url    = {https://github.com/Abelo9996/weight-space-programming-survey}
}
```

## License

The paper, the reading notes and the other data are licensed under [CC BY 4.0](LICENSE-CC-BY-4.0). The code in `tools/` is under the [MIT License](LICENSE). Quotes in the notes are short excerpts from the cited works, included for verification.
