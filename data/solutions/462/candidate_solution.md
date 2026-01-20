This is **open** (as of Jan 2026). It is listed as Erdős Problem **#462** (Erdős–Graham, p. 92) and currently marked **OPEN** with no known resolution. ([Erdős Problems][1])

A key subtlety (noted by Terence Tao) is that your second display is **ambiguous** about whether primes are excluded. ([Erdős Problems][1])

## If primes are included in the short-interval sum

For a prime $n$, (p(n)=n), so (\frac{p(n)}{n}=1). Therefore
[
\sum_{x\le n\le x+C\sqrt{x}(\log x)^2}\frac{p(n)}{n}\gg 1
]
would follow as soon as **every** such interval contains **at least one prime**. Tao remarks that, interpreted this way, it is “basically a weaker version of Legendre’s conjecture.” ([Erdős Problems][1])

Unconditionally, this is still out of reach: the best “for all sufficiently large $x$” prime-in-short-interval results only guarantee primes in intervals of length (x^\theta) with (\theta>1/2). For example, a recent refinement (Runbo Li) proves that for all sufficiently large $x$, the interval $[x-x^{0.52},x]$ contains a prime [[nomath]](equivalently, prime gaps $\ll x^{0.52}$)[[/nomath]].  This does **not** reach (\sqrt{x}(\log x)^2) [[nomath]](which is $x^{0.5+o(1)}$)[[/nomath]].

Conditionally: under the Riemann hypothesis one gets prime gaps (\ll \sqrt{x}\log x), which would imply the desired bound (with primes included) because (\sqrt{x}(\log x)^2) is larger. ([What's new][2])

## If primes are excluded (the more natural analogue of the first asymptotic)

Then the problem becomes essentially about **balanced semiprimes** $n=pq$ with (p,q\approx x^{1/2}): for such $n$,
[
\frac{p(n)}{n}=\frac{p}{pq}=\frac1q\asymp \frac1{\sqrt{x}},
]
and heuristically there should be about (\asymp \sqrt{x}) of them in an interval of length (\sqrt{x}(\log x)^2), giving total mass (\asymp 1).

Indeed, if
$
S(x):=\sum_{\substack{n<x\ n\ \text{not prime}}}\frac{p(n)}n \sim c\frac{\sqrt{x}}{(\log x)^2},
$
then for (h=C\sqrt{x}(\log x)^2) a formal differentiation heuristic gives
$
S(x+h)-S(x)\approx S'(x),h \approx \frac{c}{2}\frac{1}{\sqrt{x}(\log x)^2}\cdot C\sqrt{x}(\log x)^2=\frac{cC}{2},
$
so the *expected* increment is a positive constant. Proving a **uniform** lower bound for **every** large $x$, however, is not currently known; Tao explicitly describes this as a question about the distribution of such semiprimes in those short intervals. ([Erdős Problems][1])

## Bottom line

No unconditional proof (or counterexample) is known at present; the problem is open in the Erdős problem collection. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/forum/thread/462 "

    Erdős Problem #462 - Discussion thread

"
[2]: https://terrytao.wordpress.com/2014/08/21/large-gaps-between-consecutive-prime-numbers/?utm_source=chatgpt.com "Large gaps between consecutive prime numbers - Terence Tao"
