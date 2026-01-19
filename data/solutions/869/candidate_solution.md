As far as I can tell, this is **still open**.

It is explicitly posed by **Erdős–Nathanson (1988)** in their paper on partitioning bases into disjoint unions, in exactly the form you wrote: if (A_1,A_2) are disjoint asymptotic bases of order $2$, does (A=A_1\cup A_2) necessarily **contain** a minimal asymptotic basis of order $2$? 

And it is currently listed as **open** (Erdős Problem #869) in the Erdős Problems database (accessed Jan 18, 2026). ([Erdős Problems][1])

Some context for why this isn’t automatic:

* The general statement “every asymptotic basis contains a minimal asymptotic basis” is **false**: Härtter (1956) and Nathanson (1974) constructed asymptotic bases that contain **no** minimal asymptotic basis. 
  [[nomath]](A particularly strong modern formulation of this phenomenon appears in Nathanson’s survey: there exists an order‑2 asymptotic basis $A$ such that $A\setminus S$ is an order‑2 asymptotic basis **iff** $S$ is finite—so removing a single element never kills the basis property, hence $A$ cannot contain a minimal basis.)[[/nomath]] ([arXiv][2])

* On the other hand, there are **sufficient conditions** guaranteeing that an order‑2 asymptotic basis $A$ *does* contain a minimal one: Erdős–Nathanson proved that if the representation function is large enough [[nomath]](a $\gtrsim \log n$ lower bound)[[/nomath]], then $A$ contains a minimal asymptotic basis of order 2. 

Your hypothesis (A=A_1\cup A_2) with (A_1,A_2) disjoint order‑2 bases gives a kind of “built‑in redundancy” [[nomath]](each large $n$ has at least one representation using only $A_1$ and at least one using only $A_2$)[[/nomath]], but this is far weaker than the known (\log n)–type representation lower bounds, and the known counterexamples to “contains a minimal basis” don’t obviously admit a decomposition into two disjoint order‑2 bases. The point of Erdős–Nathanson’s question is exactly whether **this extra structure** (already being a disjoint union of two bases) forces the existence of a minimal basis inside the union. 

[1]: https://www.erdosproblems.com/869 "
  
    Erdős Problem #869
  
"
[2]: https://arxiv.org/pdf/2310.18277 "Extremal problems and the combinatorics of sumsets"
