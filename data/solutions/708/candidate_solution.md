Interpreting your definition in the standard way (and the only way that makes a nontrivial asymptotic question possible), one takes

$
g(n)=\min\\{k:\ \forall A\subset{2,3,\dots},\ |A|=n,\ \forall I \text{ an interval of } \max(A)\text{ consecutive integers,}\
\exists B\subseteq I,\ |B|\le k,\ \prod_{a\in A}a\mid \prod_{b\in B}b\\}.
$

With “(|B|=g(n))” literally, $g(n)$ can’t exceed (\min\max(A)=n+1) [[nomath]](because you can always pick an $A$ with $\max(A)=n+1$)[[/nomath]], so the $2n$ question would be vacuous. In the literature around this problem, it is indeed “(|B|\le g(n))”. ([Erdős Problems][1])

With that understood:

* **A sharp lower bound is known:** Erdős–Surányi showed that
  [
  g(n)\ \ge\ (2-o(1)),n,
  ]
  via a construction where $A$ is built from products of primes [[nomath]](so one is essentially forced to “pay” almost two chosen integers in $I$ per element of $A$)[[/nomath]]. ([Erdős Problems][1])
  In particular, **any true upper bound must have constant at least $2$**.

* **Small values:** it is known that (g(3)=4) [[nomath]](Gallai observed $g(3)\ge 4$, and equality holds)[[/nomath]]. ([Erdős Problems][1])

* **Your question is exactly the famous open problem:** Erdős explicitly asked whether one can prove
  [
  g(n)<(2+\varepsilon)n\quad\text{for every }\varepsilon>0,
  ]
  or even the clean bound (g(n)\le 2n). ([Erdős Problems][1])
  The Erdős Problems site currently lists the problem as **open** (status page last updated December 28, 2025). ([Erdős Problems][2])

So: **as of the latest available references (through late 2025), neither (g(n)\le (2+o(1))n) nor (g(n)\le 2n) is proved, and no counterexample is known either.** ([Erdős Problems][2])

[1]: https://www.erdosproblems.com/latex/708 "https://www.erdosproblems.com/latex/708"
[2]: https://www.erdosproblems.com/708 "https://www.erdosproblems.com/708"
