# Reproduce the validation and action playbook

Run from the repository root with Python 3.12:

```sh
python -m pip install -r work/requirements-audit.txt
python work/scripts/execute_notebook.py work/notebooks/w06_validation_audit.ipynb
python work/scripts/execute_notebook.py work/notebooks/w07_action_playbook.ipynb
```

The runner executes every plain Python cell in order in one shared namespace and
saves the actual stdout, stderr and execution counts into the notebook. Any error
stops execution. Standard Jupyter Run All also works from the repository root or
the notebook directory; the notebooks search their parents for the starter CSV.

The validation notebook creates `work/outputs/validation_metrics.json` and
`work/figures/validation_comparison.png`. The playbook reads that receipt, checks
the source SHA-256 and creates `work/outputs/playbook_metrics.json`,
`work/figures/action_mix.png`, and the local, gitignored
`work/outputs/ranked_action_queue.csv`. No live content change is made.

These experiments use the bundled 30,000-row starter sample only. No warehouse
credentials or access are required. The model scores are retrospective and
uncalibrated. Group separation is not a substitute for future-time validation.

The original Week-5 notebook is preserved so readers can inspect the before/after.
The audit explicitly corrects its unsupported perfect-ranking and seasonal-error
interpretations rather than silently rewriting the earlier submission.
