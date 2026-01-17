Write the condition in the “distance from $n$” form.  Put (m=n-k) [[nomath]](so $1\le k\le n-1$)[[/nomath]].  Then
[
m+\omega(m)\le n \quad\Longleftrightarrow\quad \omega(n-k)\le k \ \ \text{for all }1\le k\le n-1.
]
Numbers $n$ with this property are exactly what Erdős called **barriers for (\omega)**. ([arXiv][1])

### 1) Infinitely many such $n$ for $m+\omega(m)\le n$?

This is **open**.

* A first necessary condition is immediate from (k=1):
  [
  \omega(n-1)\le 1,
  ]
  so for (n>2) you must have (n-1) a **prime power**.
* The question “are there infinitely many barriers?” is listed as an open Erdős problem (often cited as Erdős Problem #413) and discussed in Guy’s book; the known examples form OEIS **A005236**. ([Erdős Problems][2])
* Tao–Teräväinen (2025) explicitly remark that handling the small constraints [[nomath]](already $k=1,2$)[[/nomath]] appears to be of difficulty comparable to prime-tuple–type conjectures (they mention Sophie Germain primes as a benchmark), and they “make no progress on it” there. ([arXiv][1])

So: lots of examples are known computationally (OEIS A005236), but **no proof of infinitude** is currently available. ([OEIS][3])

### 2) Existence of some (\epsilon>0) with infinitely many $n$ such that $m+\epsilon\omega(m)\le n$ for all (m<n)?

This is also **open** in the literature as stated (it is asked as the “variant” immediately after the barrier question). ([Erdős Problems][2])

In the same “distance” notation, your relaxed condition is
[
m+\epsilon\omega(m)\le n \quad\Longleftrightarrow\quad \omega(n-k)\le \frac{k}{\epsilon}\ \ \text{for all }1\le k\le n-1.
]
This is a strictly weaker requirement when (\epsilon<1), but (as far as current published results go) even proving the existence of **any fixed** (\epsilon>0) that yields infinitely many such $n$ remains open. ([Erdős Problems][2])

### Related partial progress (but not resolving the barrier questions)

Tao–Teräväinen do prove a *one-sided* statement of a different flavor: there exists an absolute constant $C$ and infinitely many $n$ such that
[
\Omega(n+k)\le Ck \quad\text{for all }k\ge 1,
]
[[nomath]](and hence $\omega(n+k)\le Ck$ as well)[[/nomath]]. ([arXiv][1])
This gives strong control on prime factors of consecutive integers **after** $n$, but it does not settle the “barrier” inequalities **before** $n$ [[nomath]](nor the $\epsilon$-variant)[[/nomath]]. ([arXiv][1])

---

If you want, I can also:

* list the first several known barriers $n$ (from OEIS A005236), and/or
* show the quick implications of the small $k$ constraints [[nomath]](e.g. $n-1$ must be a prime power, $n-2$ must have $\le 2$ distinct prime divisors, etc.)[[/nomath]] and how that ties into prime-tuple–type difficulties.

[1]: https://arxiv.org/pdf/2512.01739 "Quantitative correlations and some problems on prime factors of consecutive integers"
[2]: https://www.erdosproblems.com/tags/number%20theory "
  
    Erdős Problems
  
"
[3]: https://oeis.org/A005236 "A005236 - OEIS"
