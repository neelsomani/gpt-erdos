What you wrote is **not known in full generality**. It is exactly the **El‑Zahar–Erdős anticomplete pair problem** (posed in 1986), and it **remains open** as of the most recent literature I can find. 

More precisely, Nguyen–Scott–Seymour restate your statement as their Problem 1.1 and explicitly say “**This remains open**.” 

## What is known

Let $d(t,c)$ be the least $d$ with the property you stated.

### Proven special cases

* **Case $c=2$** is known: El‑Zahar and Erdős note a result of Wagon implying
  [
  d(t,2)\le \binom{t}{2}+1,
  ]
  and some small exact values are also recorded. ([Erdős Problems][1])
  [[nomath]](Here $\chi(\cdot)\ge 2$ just means “contains an edge”, so this case is about forcing an induced $2K_2$ / an induced matching of size 2.)[[/nomath]]

* **Case $c=3$** is also known with explicit bounds: El‑Zahar and Erdős proved (d(3,3)\le 8) and for (t>3),
  [
  d(t,3) \le 2\binom{t-1}{3}+7\binom{t-1}{2}+t.
  ]
  ([Erdős Problems][1])

### Partial progress for general $c$

* El‑Zahar and Erdős proved a **one-sided** version: under the same hypotheses, there are anticomplete (A,B) with
  [
  \chi(A)\ge 3 \quad\text{and}\quad \chi(B)\ge c,
  ]
  but this does **not** force (\chi(A)\ge c) when (c>3). 

* Nguyen–Scott–Seymour (2024) prove a different strengthening/variant: for all (t,c) there exists $d$ such that if (\chi(G)\ge d) and (\omega(G)<t), then there are anticomplete (A,B) where **$B$** has (\chi(B)\ge c) and **$A$** has **large minimum degree** (equivalently, large “denseness” in their formulation). 
  This is consistent with your conjectured conclusion but does not yet give (\chi(A)\ge c) in general.

## Bottom line

* Your statement is a **famous open problem** [[nomath]](often phrased: bounded clique number + sufficiently large chromatic number $\Rightarrow$ two anticomplete subgraphs of large chromatic number)[[/nomath]]. 
* It **is proved** for $c=2$ and $c=3$, and there are **weaker/related results** for all $c$, but the full “(\chi(A)\ge \chi(B)\ge c)” conclusion is not currently settled for general $c$. ([Erdős Problems][1])

If you tell me which regime you care about [[nomath]](e.g. $c=2$, $c=3$, or general $c$)[[/nomath]], I can either $i$ outline the known proofs in those cases, or (ii) show how to substitute one of the proved variants (like the minimum-degree/chromatic version) in arguments where your statement would have been used.

[1]: https://www.erdosproblems.com/forum/thread/1111 "

    Erdős Problem #1111 - Discussion thread

"
