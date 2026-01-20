In full generality, this is **not currently known**. It is recorded as an **open Erdős problem** (Erdős Problems #489): given (A\subseteq\mathbb N) with (|A\cap[1,x]|=o(x^{1/2})) and (B={n\ge1:\ a\nmid n\ \forall a\in A}), it is **open** whether the limit
$
\lim_{x\to\infty}\frac1x\sum_{b_i<x}(b_{i+1}-b_i)^2
$
always exists and is finite. ([Erdős Problems][1])

What *is* known is that the answer is **yes in some important special cases**:

* **Squarefree numbers.** If (A={p^2:\ p\ \text{prime}}), then $B$ is the set of squarefree integers. In this case the existence and finiteness of the limit is known (already noted on the Erdős Problems page). ([Erdős Problems][1])
  In fact, much more is known: Filaseta–Trifonov (1996) proved asymptotics for moments of squarefree gaps, showing that for (0\le\gamma<43/13),
  [
  \sum_{s_{n+1}\le x}(s_{n+1}-s_n)^\gamma \sim B(\gamma),x,
  ]
  in particular for (\gamma=2) this gives exactly a linear asymptotic for the sum of squared gaps and hence a finite limit. ([MathOverflow][2])

* **Finite $A$** (or, more generally, when the exclusion is effectively periodic): then $B$ is eventually periodic, so the average of any reasonable gap statistic (including squared gaps) has a limit. (This is a straightforward periodicity argument.)

So the short answer is: **for general $A$ under your hypothesis, it remains an open problem; for some key cases (notably squarefree numbers) it is true.** ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/489 "
  
    Erdős Problem #489
  
"
[2]: https://mathoverflow.net/questions/291864/gaps-in-squarefree-numbers "nt.number theory - Gaps in Squarefree numbers - MathOverflow"
