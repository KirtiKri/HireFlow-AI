# Evaluation and reliability

## Scope

HireFlow's rule-based extraction is evaluated using fictional fixtures. It recognizes a fixed set of skill aliases and selects excerpts containing those aliases, subject to conservative negation rules. This is **document mention detection**, not a skill or candidate quality assessment.

## Reproduce

From the repository root after installing `requirements.txt`:

```powershell
python -m pytest -q
python -m eval.run_golden
python -m eval.run_stage3
```

`eval/run_stage3.py` regenerates `eval/stage3_results.json`. The three Stage 3 fixtures check expected supported/missing requirements, evidence report coverage, and workflow trace. Golden cases include negated claims and prompt injection. Regression tests cover additional negation patterns and clause boundaries.

## Known failure modes

- A mention of a skill is not verified competence or experience.
- Aliases may miss equivalent terms and domain-specific phrasing.
- Negation and speculation can be more complex than a short context window.
- Quoted or fabricated statements may still be treated as evidence.
- Some job requirements are outside the fixed vocabulary.
- Synthetic examples do not establish performance on real-world resumes.

## Reporting results

Report the **actual output of the three commands** from the environment used for submission. Do not describe fixture pass rates as real-world accuracy, precision, recall, or fairness. Avoid using the tool on real applicants without extensive independent validation, consent, access controls, and human governance.
