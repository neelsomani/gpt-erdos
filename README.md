# GPT-Erdos

*Last updated: January 2026*

GPT-Erdos is a collection of Erdős problems and candidate proofs, using LLM-driven proof search and (when possible) autoformalization. Erdős problems provide a compact testbed for studying how LLMs handle open-ended mathematical reasoning. We produce candidate proofs with corresponding Lean proof attempts, to surface successes, failures, and limitations of current approaches.

We view GPT-Erdos as both a benchmark of mathematical ability and as a controlled environment for studying how LLMs:

- represent partial proofs and conjectural reasoning,
- distinguish known results from novel arguments,
- fail under implicit constraints,
- interact with formal verification systems.

This project uses data from the Erdos Problems repository:
Tao et al., *Erdos Problems*, GitHub repository.
https://github.com/teorth/erdosproblems/tree/main/data

We scrape publicly available metadata from https://www.erdosproblems.com.

## Methodology

Each problem was submitted to GPT 5.2 Pro and Deep Research with an identical prompt. We indicate if a proof for the Erdős problem as stated exists in the literature. We also indicate whether GPT 5.2 Pro gives a purported solution (whether correct or not). Reviewer feedback is provided for each proof. When possible, we submit the proof to Aristotle (Harmonic) for autoformalization.

## Findings

| Category                              | Description                                                                                                                                                | Problem Numbers                                                  |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| New proofs                            | 3 problems with new proofs never seen in the literature*                                                                                                   | 281, 397, 652**                                                  |
| Exact literature solutions identified | 4 problems where GPT 5.2 Pro or Deep Research identifies an exact solution in the literature previously unidentified                                                            | 591, 847, 1129, 1130                                             |
| Partial literature extensions         | 3 problems where GPT 5.2 Pro or Deep Research identifies additional useful results in the literature to construct a stronger known solution, but does not fully solve the problem | 788***, 1084, 1105                                                     |
| Typos identified                      | 3 problems where GPT 5.2 Pro identifies a typo or otherwise malformed problem statement                                                                                    | 161, 662, 1022                                                         |
| Solved as stated, hidden constraints  | 15 problems where GPT 5.2 Pro gives a solution to the problem as stated, but there are hidden constraints that mathematicians don't explicitly note                                 | 78, 91, 274, 369, 524, 665, 686, 690, 850, 866, 906, 943, 954, 1021, 1092    |
| Valid but non-improving proofs        | 12 problems where GPT 5.2 Pro gives a valid proof, but does not improve beyond known solutions                                                             | 142, 180, 302, 332, 514, 655, 726, 792, 796, 858, 893, 969       |
| Conditional on conjectures            | 4 problems where GPT 5.2 Pro points out that an unproven conjecture can solve the problem                                                                  | 539, 647, 743, 1014                                              |
| Subtle errors                         | 13 problems where GPT 5.2 Pro gives a proof with a subtle error                                                                                            | 335, 517, 533, 538, 550, 602, 705, 731, 734, 783, 864, 888, 1063 |

Notes:

\* Literature search later found partial results that could be extended to solve the same problems.

\*\* Terence Tao classifies 652 as a Section 1 result, but Daniel Litt notes it is arguably literature search.

\*\*\* Proof still under review.

For the remainder of the open problems, GPT 5.2 Pro recites the existing literature on the problem, but does not claim to output a solution. When such outputs are presented in proof form rather than as literature summaries, we classify them as "valid but non-improving proofs."
