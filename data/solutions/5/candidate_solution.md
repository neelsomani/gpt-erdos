Let (d_n:=p_{n+1}-p_n). Your question is asking whether, for each prescribed (C\ge 0), one can find infinitely many indices (n_i) such that
[
\frac{d_{n_i}}{\log n_i}\to C.
]
Equivalently, is $C$ a **limit point** of the sequence ({d_n/\log n})?

This is essentially a famous conjecture of Erdős: he conjectured that the normalized prime gaps (d_n/\log n) are **everywhere dense** in ([0,\infty)), i.e. that *every* (C\ge 0) should occur as a limit point. ([arXiv][1])
That conjecture is **still open** for a general prescribed (C>0).

### What is known unconditionally

* **(C=0): yes.**
  It is known that $0$ is a limit point [[nomath]](indeed $\liminf d_n/\log n=0$)[[/nomath]]; Pintz’s note explicitly highlights that $0$ is a proven element of the limit-point set (coming from the small-gaps work of Goldston–Yıldırım–Pintz and subsequent developments). ([arXiv][2])

* **A whole interval $[0,c]$: yes (for some ineffective (c>0)).**
  Pintz proved that the set $J$ of limit points of (d_n/\log n) contains an interval ([0,c]) with some positive (but ineffective) constant $c$. ([arXiv][1])
  So for every (C\in[0,c]), such a subsequence (n_i) exists.

* **For “many” $C$, yes (positive proportion/positive measure).**
  Let (\mathbb L) be the set of limit points of ({(p_{n+1}-p_n)/\log p_n}) [[nomath]](this is the normalization most papers use; it is essentially equivalent to $\log n$ for limit-point questions)[[/nomath]].
  Banks–Freiberg–Maynard showed that at least **12.5%** of nonnegative real numbers lie in (\mathbb L). ([arXiv][3])
  Pintz improved the quantitative “how many” statement (in terms of Lebesgue measure up to (T)). ([arXiv][2])
  Merikoski improved further: for all (T\ge 0),
  [
  \lambda(\mathbb L\cap[0,T])\ge \tfrac{T}{3},
  ]
  and moreover (\mathbb L) is **relatively dense**: there is an absolute constant $K$ such that (\mathbb L\cap[T,T+K]\neq\emptyset) for every (T\ge 0). ([arXiv][4])

### Bottom line

* The statement “**for every** (C\ge 0) there exists an infinite subsequence with limit $C$” is **not known** (it’s Erdős’ conjecture). ([arXiv][1])
* We **can** say “yes” for (C=0), and in fact for all $C$ in some (ineffective) interval ([0,c]). ([arXiv][1])
* Beyond that, we know it holds for a **large** set of constants $C$ (at least one third of them in every ([0,T]) in the sense of Lebesgue measure), but we cannot currently guarantee it for an arbitrary specified $C$ like (C=1) or (C=10). ([arXiv][4])

[1]: https://arxiv.org/abs/1407.2213 "[1407.2213] On the distribution of gaps between consecutive primes"
[2]: https://arxiv.org/abs/1510.04577 "[1510.04577] A note on the distribution of normalized prime gaps"
[3]: https://arxiv.org/abs/1404.5094 "[1404.5094] On limit points of the sequence of normalized prime gaps"
[4]: https://arxiv.org/abs/1811.03008 "[1811.03008] Limit points of normalized prime gaps"
