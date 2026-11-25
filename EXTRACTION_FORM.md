# Extraction form

Every record in `corpus/notes/` was read from its full text (arXiv HTML or PDF, or the files of the Zenodo record) and summarized in one JSON file with the fields below. Where only part of a record could be read, `read_level` says which parts.

## Rules
1. Every number recorded must carry a verbatim quote from the source (under about 40 words) and its location (section, table or page). Numbers that appear only in a figure are marked as such.
2. Title and full author list come from the paper itself; differences from the arXiv or Zenodo metadata are recorded in `metadata_mismatch`.
3. Notes record what a study claims and what evidence it gives. They do not rank studies.

## Scope
A study is WSP if an editor, in practice a language model possibly using tools, determines the new weights or the edit by reasoning about the architecture, the weights and the specification, and no gradient optimizer fitting a training loss is the primary author of the values. Closed-form or solver studies without a language model, and studies that only evaluate, replicate or provide baselines for WSP work, are included as `peripheral` when they explicitly position themselves relative to WSP. Out-of-scope records are marked `not_wsp` with a one-line reason.

## Taxonomy
- **B1 Reading:** weights to description (what a network computes or was trained on, audits, backdoor detection). No weight change.
- **B2 Writing:** specification to weights, from scratch.
- **B3 Repairing and editing:** changing a trained network's weights to fix or alter behavior, including implanting backdoors.
- **B4 Feedback and search loops:** the editor iterates on experimental, verifier or benchmark feedback, or searches over edits.
- **B5 Efficient and non-LLM solvers:** replacing or amortizing the language-model editor (solvers, closed-form edits, trained editors).
- **B6 Self-editing:** a model edits its own weights, or a copy of itself.
- Facets: `evaluation`, `verification`, `safety`, and the application domain.

Interface (I1 to I4) and loop (O, C, S) codes in the paper's appendix table are derived from the `interface`, `editor` and `loop` fields by the rules in `tools/make_tables.py` and corrected by hand where the rule disagrees with the note (`code_I`, `code_L` in `corpus/overrides.json`).

## Fields

| Field | Content |
|---|---|
| `id`, `url`, `title`, `authors`, `date` | identifiers; `date` is the first version |
| `read_level` | `full`, or `partial` with what was read |
| `metadata_mismatch` | differences between the paper and its listing |
| `is_wsp` | `core`, `peripheral` or `not_wsp` |
| `why_wsp` | one sentence: who edits what, and how |
| `exclusion_reason` | for `not_wsp` records (update-search records only) |
| `primary_branch`, `secondary_branches`, `facets`, `domain` | taxonomy codes |
| `editor`, `target`, `interface`, `loop`, `self_editing` | who edits, what is edited, through what interface, with what loop, and whether the editor edits itself |
| `fraction_or_count_of_weights_changed` | with quote |
| `headline_results`, `cost` | lists of `{claim, quote, where}` |
| `baselines_and_controls`, `runs_and_variance`, `robustness_of_edits`, `verification`, `memorization_vs_reasoning` | evidence fields used in Section 6 of the paper |
| `limitations_stated`, `code_or_data`, `cites_or_builds_on`, `notes_for_survey` | context |
