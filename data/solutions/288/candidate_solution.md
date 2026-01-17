This is **not known** in general — it’s an **open problem** of Erdős and Graham.

It appears explicitly as *Erdős Problem #288* (in the Erdős–Graham problem list) and is listed as **OPEN** as of late 2025 / early 2026. ([Erdős Problems][1])

A few remarks and examples:

* With **one interval** [[nomath]](just $\sum_{n\in I} \frac1n$)[[/nomath]], integrality is completely understood: a classical theorem of **Kürschák (1908)** implies that a sum of reciprocals of **consecutive** positive integers is never an integer [[nomath]](except the trivial $I={1}$, giving $1$)[[/nomath]]. ([John D. Cook][2])
  So your question is genuinely about the interaction between **two** such interval-sums.

* There are **nontrivial examples** with two intervals. For instance
  [
  \frac13+\frac14+\frac15+\frac16+\frac1{20}=1,
  ]
  i.e. $I_1=[3,6]$ and $I_2=[20,20]$. ([Erdős Problems][1])
  In fact, the problem is stated to remain open **even if (|I_2|=1)** (i.e., the second “interval” is just a singleton). ([Erdős Problems][1])

* What is *unknown* is whether there are **infinitely many** such pairs ((I_1,I_2)), or only **finitely many**.

If it’s helpful as context (not a proof of anything), a quick brute-force search over small endpoints suggests very few solutions occur at small sizes; e.g. among intervals with endpoints (\le 500), one finds only a handful [[nomath]](up to swapping $I_1,I_2$)[[/nomath]], including
$[1,1],[1,1]$, $[1,2],[1,2]$, $[1,2],[2,2]$, $[1,3],[6,6]$, $[2,3],[6,6]$, and $[3,6],[20,20]$.
But the existence/nonexistence of further solutions at large scales is exactly what’s open.

So the best current answer is: **nobody knows yet** whether your statement is true. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/288 "
  
    Erdős Problem #288
  
"
[2]: https://www.johndcook.com/blog/2021/01/23/sums-of-consecutive-reciprocals/ "Sums of consecutive reciprocals"
