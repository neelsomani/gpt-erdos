Let me write (f(n):=\tau_\perp(n)); this is exactly the function studied by Erdős–Hall in 1978. ([users.renyi.hu][1])

## Basic reformulation (squarefree case)

If (n=\prod_{j=1}^k p_j) is squarefree, then every divisor corresponds to a subset (A\subseteq{1,\dots,k}) via
[
d_A=\prod_{j\in A}p_j,\qquad \log d_A=\sum_{j\in A}\log p_j.
]
Ordering divisors increasingly is the same as ordering these subset sums (\sum_{j\in A}x_j) where (x_j:=\log p_j). For squarefree $n$,
[
(d_A,d_B)=1\iff A\cap B=\varnothing.
]
So $g(k)$ is equivalent to the following additive/combinatorial problem (stated by Erdős in 1981): choose (0<x_1<\cdots<x_k) with all (2^k) subset sums distinct, order subsets by increasing subset sum, and maximize the number of adjacent pairs $(A_i,A_{i+1})$ with (A_i\cap A_{i+1}=\varnothing). 

## 1) Does (\tau_\perp(n)/\omega(n)\to\infty) for almost all $n$?

This is **open** (it is essentially Erdős–Hall’s question). Erdős–Hall note the trivial lower bound
[
\tau_\perp(n)\ge \omega(n),
]
and they explicitly speculate that perhaps (f(n)/\nu(n)\to\infty) [[nomath]](their $\nu(n)$ is $\omega(n)$)[[/nomath]] after discarding a set of density $0$. ([users.renyi.hu][1])

What *is* known in the direction “typically bigger than (\omega(n))” is also limited: Erdős–Hall state that it is “not hard” to show the set of $n$ with (f(n) < (1+c)\omega(n)) has density $0$ for sufficiently small fixed (c>0). ([users.renyi.hu][1])
That is far weaker than (\tau_\perp(n)/\omega(n)\to\infty), but it at least rules out (\tau_\perp(n)) being ((1+o(1))\omega(n)) on a density‑$1$ set.

So: **no proof or disproof is currently known**, and it is listed as an open Erdős problem. ([Erdős Problems][2])

## 2) Is (\tau_\perp(n)<\exp((\log n)^{o(1)})) for all $n$?

Also **open**.

Erdős–Hall explicitly say they have “no good upper bound” for $f(n)$ and that it would be “reasonable to expect” that for every (\varepsilon>0),
[
f(n) < \exp\big((\log n)^\varepsilon\big),
]
which is the same qualitative claim as (f(n)<\exp((\log n)^{o(1)})). ([users.renyi.hu][1])

The only completely general upper bound is the trivial one
[
\tau_\perp(n)\le \tau(n)-1,
]
and the maximal order of (\tau(n)) is known (Wigert 1907) to satisfy
[
\log \tau(n)\le (1+o(1))(\log 2)\frac{\log n}{\log\log n},
]
so (\tau_\perp(n)\le \exp!\big((\log 2+o(1))\frac{\log n}{\log\log n}\big)). ([Pollack.UGA][3])
This is **much larger** than (\exp((\log n)^{o(1)})), so it does not address your question.

As noted on the current problem page, it’s not even known whether (\tau_\perp(n)=\exp(o(\log n/\log\log n))) holds. ([Erdős Problems][2])

## 3) Growth of $g(k)$ for squarefree $n$ with (\omega(n)=k)

Here there is a clean answer up to exponential constants: **$g(k)$ grows exponentially in $k$**.

Erdős reports a result of Erdős–Simonovits (proof not in that note) that there exists an absolute (c>0) such that
[
(2^{1/2}+o(1))^k < g(k) < (2-c)^k.
]


Equivalently,
[
2^{k/2+o(k)} \le g(k) \le (2-c)^k,
]
so
[
\log g(k)=\Theta(k).
]

What is *not* known (at least as of the latest compiled status) is the exact exponential base, i.e. whether (\lim_{k\to\infty} g(k)^{1/k}) exists and what its value is; Erdős already remarks “Perhaps $g(k)$ can be determined explicitly.” 

---

If you’d like, I can also:

* translate the $g(k)$ bounds into bounds on (\max_{n\le x,\ \text{squarefree}} \tau_\perp(n)) via (k\sim \log x/\log\log x) for primorial‑type sizes, and
* give a few explicit constructions that achieve the (\sqrt{2}^k) lower bound at the combinatorial level (subset sums), which then convert back to squarefree integers by choosing primes with (\log p_i) proportional to those (x_i).

[1]: https://users.renyi.hu/~p_erdos/1978-26.pdf "https://users.renyi.hu/~p_erdos/1978-26.pdf"
[2]: https://www.erdosproblems.com/forum/thread/1100 "

    Erdős Problem #1100 - Discussion thread

"
[3]: https://pollack.uga.edu/largedk3.pdf?utm_source=chatgpt.com "The maximal size of the k-fold divisor function for very large k"
