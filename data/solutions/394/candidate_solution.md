These are classical open questions of Erdős–Hall (1978) / Erdős–Graham (1980). They appear as Erdős Problem #394 and are still listed as open. ([Erdős Problems][1])

## 1) A power saving in (\sum_{n\le x} t_2(n))

What is known unconditionally is an **$o(x^2)$** estimate, but not a power of (\log x).

* Erdős and Hall proved
  [
  \sum_{n\le x} t_2(n)\ \ll\ \frac{\log\log\log x}{\log\log x},x^2,
  ]
  which in particular implies (\sum_{n\le x} t_2(n)=o(x^2)). ([Erdős Problems][2])

* A simple lower bound comes from primes: for prime $p$, (t_2(p)=p-1), so
  [
  \sum_{n\le x} t_2(n)\ \ge\ \sum_{p\le x} (p-1)\ \gg\ \frac{x^2}{\log x}.
  ]
  ([Erdős Problems][2])

* Erdős and Hall **conjectured** a much stronger upper bound: that
  [
  \sum_{n\le x} t_2(n)=o!\left(\frac{x^2}{(\log x)^c}\right)\quad\text{for every }c<\log 2.
  ]
  ([Erdős Problems][2])

So your first question [[nomath]](“does there exist *some* $c>0$ with $\sum_{n\le x} t_2(n)\ll x^2/(\log x)^c$?”)[[/nomath]] is **open**: the best published bound is the (\frac{\log\log\log x}{\log\log x}) saving, which is far weaker than any fixed power of (\log x). ([Erdős Problems][2])

[[nomath]](Also, the prime lower bound shows you **cannot** hope for such an estimate with $c>1$, but your question only asks for existence of *some* $c>0$, and that remains unresolved. $[Erdős Problems][2]$)[[/nomath]]

## 2) Does (\sum_{n\le x} t_{k+1}(n)=o\left(\sum_{n\le x} t_k(n)\right)) for (k\ge2)?

This is also **open** (again due to Erdős and Hall). They explicitly pose this type of question and remark that they had not even proved the first nontrivial case. ([Erdős Problems][2])

One basic obstruction to “too fast” decay is that primes contribute at the same order for every fixed $k$: for primes $p$ one has
[
t_k(p)=p+1-k \quad (p\ge k),
]
so (\sum_{n\le x} t_k(n)) is always (\gg x^2/\log x) for every fixed $k$. ([Cambridge University Press & Assessment][3])
Thus, if the ratio (\sum_{n\le x} t_{k+1}(n)/\sum_{n\le x} t_k(n)\to 0) were true, it would force (\sum_{n\le x} t_k(n)) to be asymptotically much larger than (x^2/\log x) (so that primes are negligible in the denominator), and this is precisely the kind of global information that is currently missing.

So, as of the current state of the problem literature summarized above, both of your statements are **not known** (and are considered open problems). ([Erdős Problems][2])

[1]: https://www.erdosproblems.com/forum/thread/394 "https://www.erdosproblems.com/forum/thread/394"
[2]: https://www.erdosproblems.com/latex/394 "https://www.erdosproblems.com/latex/394"
[3]: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/2E0CB335DDC15ED4B49894D180CBE883/S1446788700021455a.pdf/on-some-unconventional-problems-on-the-divisors-of-integers.pdf "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/2E0CB335DDC15ED4B49894D180CBE883/S1446788700021455a.pdf/on-some-unconventional-problems-on-the-divisors-of-integers.pdf"
