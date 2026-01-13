# GPT-Erdos

GPT-Erdos is a collection of autoformalized Erdős problems and candidate solutions, using LLM-driven proof search. Erdős problems provide a compact testbed for studying how LLMs handle open-ended mathematical reasoning. We produce candidate solutions with corresponding Lean proof attempts, to surface successes, failures, and limitations of current approaches.

This project uses data from the Erdos Problems repository:
Teorth et al., *Erdos Problems*, GitHub repository.
https://github.com/teorth/erdosproblems/tree/main/data

We scrape publicly available problem data from https://www.erdosproblems.com.

## Contributing

https://docs.google.com/document/d/1PS1lkdti3LboKjr8F1f7ldjYVTTRcz4cq1GXkem7834/edit?tab=t.0


## Appendix: Scrape Unsolved Problems

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 scripts/export_unsolved.py --input data/problems.yaml --output data/unsolved.jsonl --delay 1.0
```
