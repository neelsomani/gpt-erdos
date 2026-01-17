For (r\le 2) the condition is vacuous [[nomath]](simple graphs have no odd cycles of length $1$ or $2$)[[/nomath]], so you can just take $G$ itself.

For (r\ge 3) this is a well-known Erdős–Hajnal problem and, as far as is known, it is **open in ZFC in full generality**. ([Erdős Problems][1])

What *is* known is:

* **Countable case, ( \mathfrak m=\aleph_0), $r=3$: YES.**
  Rödl proved that every graph of chromatic number (\aleph_0) contains a **triangle-free** subgraph of chromatic number (\aleph_0). ([Erdős Problems][1])

* **Uncountable case: not provable in ZFC; consistent counterexamples exist already for $r=3$.**
  Komjáth and Shelah showed it is **consistent** (relative to ZFC) that there is a graph $X$ on (\omega_1) with (\chi(X)=\aleph_1) such that **every** subgraph (Y\subseteq X) which does not contain $K(\omega+1)$ is **countably chromatic**. 
  In particular, any triangle-free subgraph is $K(\omega+1)$-free [[nomath]](since $K(\omega+1)$ contains triangles)[[/nomath]], so in that model **there is no (\aleph_1)-chromatic triangle-free subgraph** of $X$. Hence the answer is **consistently “no”** for ((\mathfrak m,r)=(\aleph_1,3)), and therefore also consistently “no” for any (r\ge 3) [[nomath]](because “no odd cycle of length $\le r$” implies triangle-free)[[/nomath]]. 

* **The property is not vacuous at uncountable (\mathfrak m):**
  The same paper also shows it is consistent that for each (n<\omega) there is a graph on (\omega_1) of chromatic number (\aleph_1) with **no** (C_3,C_5,\dots,C_{2n+1}). 

* **Positive results under strong set-theoretic hypotheses:**
  They note, for example, that if (\kappa) is strongly compact and (\chi(X)=\kappa) [[nomath]](with an additional $K_4$-free hypothesis)[[/nomath]], then one can obtain a triangle-free (\kappa)-chromatic subgraph. 

So the best current summary is:

* **In ZFC:** open in general. ([Erdős Problems][1])
* **For (\mathfrak m=\aleph_0, r=3):** yes (Rödl). ([Erdős Problems][1])
* **For uncountable (\mathfrak m) [[nomath]](already $\aleph_1$)[[/nomath]], (r\ge 3):** it can **fail** in some models of ZFC, so the statement cannot be proved in ZFC. 

[1]: https://www.erdosproblems.com/740?utm_source=chatgpt.com "Erdős Problem #740"