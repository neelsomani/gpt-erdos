# GPT-Erdos

GPT-Erdos is a collection of Erdős problems and candidate proofs, using LLM-driven proof search and (when possible) autoformalization. Erdős problems provide a compact testbed for studying how LLMs handle open-ended mathematical reasoning. We produce candidate proofs with corresponding Lean proof attempts, to surface successes, failures, and limitations of current approaches.

This project uses data from the Erdos Problems repository:
Teorth et al., *Erdos Problems*, GitHub repository.
https://github.com/teorth/erdosproblems/tree/main/data

We scrape publicly available metadata from https://www.erdosproblems.com.

## Methodology

Each problem was submitted to GPT 5.2 Pro and Deep Research with an identical prompt. We indicate if a proof for the Erdős problem as stated exists in the literature. We also indicate whether GPT 5.2 Pro gives a purported solution (whether correct or not). Reviewer feedback is provided for each proof.

## Findings

| Category                              | Description                                                                                                                                                | Problem Numbers                                                  |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| New proofs                            | 3 problems with new proofs never seen in the literature*                                                                                                   | 281, 397, 652**                                                  |
| Exact literature solutions identified | 4 problems where GPT 5.2 Pro or Deep Research identifies an exact solution in the literature previously unidentified                                                            | 591, 847, 1129, 1130                                             |
| Partial literature extensions         | 2 problems where GPT 5.2 Pro or Deep Research identifies additional useful results in the literature to construct a stronger known solution, but does not fully solve the problem | 788***, 1105                                                     |
| Typos identified                      | 2 problems where GPT 5.2 Pro identifies a typo in the problem statement                                                                                    | 161, 662                                                         |
| Solved as stated, hidden constraints  | 13 problems where GPT 5.2 Pro gives a solution to the problem as stated, but there are hidden constraints that are assumed                                 | 78, 91, 274, 369, 524, 665, 686, 690, 850, 866, 906, 943, 954    |
| Valid but non-improving proofs        | 12 problems where GPT 5.2 Pro gives a valid proof, but does not improve beyond known solutions                                                             | 142, 180, 302, 332, 514, 655, 726, 792, 796, 858, 893, 969       |
| Conditional on conjectures            | 4 problems where GPT 5.2 Pro points out that an unproven conjecture can solve the problem                                                                  | 539, 647, 743, 1014                                              |
| Subtle errors                         | 13 problems where GPT 5.2 Pro gives a proof with a subtle error                                                                                            | 335, 517, 533, 538, 550, 602, 705, 731, 734, 783, 864, 888, 1063 |

Notes:

\* Literature search later found partial results that could be extended to solve the same problems.

\*\* Terence Tao classifies 652 as a Section 1 result, but Daniel Litt notes it is arguably literature search.

\*\*\* Proof still under review.
