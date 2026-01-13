# GPT-Erdos

GPT-Erdos is a collection of autoformalized Erdős problems and candidate solutions, using LLM-driven proof search. Erdős problems provide a compact testbed for studying how LLMs handle open-ended mathematical reasoning. We produce candidate solutions with corresponding Lean proof attempts, to surface successes, failures, and limitations of current approaches.

This project uses data from the Erdos Problems repository:
Teorth et al., *Erdos Problems*, GitHub repository.
https://github.com/teorth/erdosproblems/tree/main/data

We scrape publicly available problem data from https://www.erdosproblems.com.

## What the script does

`scripts/export_unsolved.py`:

- reads `data/problems.yaml` for problem numbers and status
- keeps only `open` and `falsifiable` problems
- downloads LaTeX from `https://www.erdosproblems.com/latex/{number}`
- writes a JSONL dataset containing `number`, `state`, and `latex`

## Run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 scripts/export_unsolved.py --input data/problems.yaml --output data/unsolved.jsonl --delay 1.0
```

## Downstream plan

- Feed unsolved problems into OpenAI Deep Research to gather known solutions.
- For open problems with no prior solutions, run GPT-5.2 Pro and Gemini.
- Check the interactive table at https://teorth.github.io/erdosproblems/ to see whether a problem statement has already been formalized.
- Send candidate proofs to Harmonic for formalization and track success.
