This is **an open problem** (still unsolved).

It was posed by **Erdős, Graham, Ruzsa, and Straus** (1975), who wrote that they had “no doubt” the answer should be **yes**, but they were not able to prove it. ([Erdős Problems][1])

What *is* known:

* There **do** exist distinct pairs $(n,m)$ with the same set of prime divisors. Classic examples given in the literature are
  ((n,m)=(87,88)) and $(607,608)$. ([Erdős Problems][1])
* Many more examples are known computationally; the values of $n$ for which there exists some (m>n) with this property are tabulated as **OEIS A129515**, and (for the entries currently listed there) the matching $m$ is (m=n+1). ([OEIS][2])
* There is even a known **triple** $(10003,10004,10005)$ where all three central binomial coefficients share the same set of prime divisors. ([Erdős Problems][1])

A useful reformulation comes from **Kummer’s theorem**: for a prime $p$, the exponent of $p$ in (\binom{2n}{n}) equals the number of carries when adding $n$ and $n$ in base $p$. In particular,
[
p \mid \binom{2n}{n}\quad\Longleftrightarrow\quad \text{adding }n+n\text{ in base }p\text{ produces at least one carry.}
]
So the problem is equivalent to asking for infinitely many distinct (n\neq m) whose “carry/no-carry” behavior matches for every prime. ([Wikipedia][3])

Despite the many examples, **no proof is known** that there are infinitely many such pairs, and related strengthenings [[nomath]](e.g. whether one can always find a pair of the form $(n,n+k)$ for every fixed $k$)[[/nomath]] are also open. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/730 "
  
    Erdős Problem #730
  
"
[2]: https://oeis.org/A129515 "A129515 - OEIS"
[3]: https://en.wikipedia.org/wiki/Kummer%27s_theorem?utm_source=chatgpt.com "Kummer's theorem"
