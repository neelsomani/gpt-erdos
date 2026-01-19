Let
[
\Phi^{-1}(n):={m\ge 1:\varphi(m)=n},\qquad
f_{\min}(n)=\min\Phi^{-1}(n),\quad f_{\max}(n)=\max\Phi^{-1}(n),
]
and define
[
R(x):=\max_{\substack{n\le x\ \Phi^{-1}(n)\neq\varnothing}}\frac{f_{\max}(n)}{f_{\min}(n)}.
]
[[nomath]](This is exactly Erdős problem #694, and it is listed as open. $[Erdős Problems][1]$)[[/nomath]]

## Basic inequalities

1. **Trivial lower bound on (f_{\min}).**
   For (m>1), (\varphi(m)\le m-1), with equality iff $m$ is prime. Hence for any totient value (n\ge 1),
   [
   f_{\min}(n)\ge n+1,
   ]
   and if (n=p-1) with $p$ prime then (f_{\min}(n)=p=n+1).

2. **Relating the ratio to (m/\varphi(m)).**
   If (M=f_{\max}(n)), then
   [
   \frac{f_{\max}(n)}{f_{\min}(n)}\le \frac{f_{\max}(n)}{n}
   =\frac{M}{\varphi(M)}.
   ]
   So controlling $R(x)$ reduces to controlling the maximal size of (m/\varphi(m)).

A classical theorem of Landau gives
[
\limsup_{m\to\infty}\frac{m}{\varphi(m)\log\log m}=e^\gamma,
]
and explicit inequalities of Rosser–Schoenfeld type give an upper bound of the shape
[
\frac{m}{\varphi(m)}\le e^\gamma\log\log m+\text{(smaller error)}\qquad (m\ \text{large}),
]
as quoted for instance in Nicolas’ paper (which cites Landau and Rosser–Schoenfeld). ([arXiv][2])

## Consequence: an unconditional upper bound for $R(x)$

Let (n\le x) be a totient and (M=f_{\max}(n)). Then
[
\frac{f_{\max}(n)}{f_{\min}(n)}\le \frac{M}{\varphi(M)}.
]
By Landau/Rosser–Schoenfeld type bounds, (M/\varphi(M)\ll \log\log M). ([arXiv][2])

Also, since (\varphi(M)=n\le x), those same bounds imply (M\ll x\log\log M), hence (M\ll x\log\log x) and therefore (\log\log M=\log\log x+o(1)). Putting these together yields
[
R(x)\le (e^\gamma+o(1))\log\log x\qquad (x\to\infty).
]

So **the maximum spread between preimages cannot grow faster than a constant multiple of (\log\log x)**, and the “right” constant for the upper bound is (e^\gamma).

## Heuristics and conjectured sharpness

The natural conjecture is that the upper bound is essentially sharp:
[
R(x)\stackrel{?}{\sim} e^\gamma\log\log x,
\quad\text{or at least}\quad
\limsup_{x\to\infty}\frac{R(x)}{\log\log x}=e^\gamma.
]

A standard way to *try* to realize the (e^\gamma\log\log) behavior is to force (f_{\max}(n)) to have **many small prime factors**, because
[
\frac{m}{\varphi(m)}=\prod_{p\mid m}\frac{p}{p-1}.
]
Mertens’ product theorem implies
[
\prod_{p\le y}\frac{p}{p-1}\sim e^\gamma \log y,
]
so if one can build a solution $m$ to (\varphi(m)=n) whose prime divisors are (essentially) all primes (\le y), then (m/\varphi(m)) is about (e^\gamma\log y), i.e. about (e^\gamma\log\log(\text{size})). ([Wikipedia][3])

A concrete heuristic suggested in the Erdős-problems discussion thread is:

* Take the primorial (x_0=p_r).
* Let $q$ be the first prime with (q\equiv 1\pmod{\varphi(x_0)}).
* Experiments [[nomath]](for $r\le 200$)[[/nomath]] found (q-1=b\varphi(x_0)) with (b\le p_r), which then gives
  $\varphi(bx_0)=b\varphi(x_0)=\varphi(q)$, producing two very different preimages for the same totient value. ([Erdős Problems][4])

If one could prove such a phenomenon in general [[nomath]](or anything comparably strong about *small* primes in the progression $1\bmod \varphi(p_r)$)[[/nomath]], it would yield
[
\frac{f_{\max}(n)}{f_{\min}(n)}\approx \frac{p_r}{\varphi(p_r)}
=\prod_{p\le p_r}\frac{p}{p-1}\sim e^\gamma\log p_r\sim e^\gamma\log\log(p_r),
]
matching the upper bound. The thread notes that proving the needed statement looks “very hard” and ties into the state of the art around Linnik-type problems on the least prime in an arithmetic progression. ([Erdős Problems][4])

This is consistent with the “open” status of the problem. ([Erdős Problems][1])

## Computational evidence for the (\log\log x) growth

A quick computation [[nomath]](enumerating $\varphi(m)$ up to a safe cutoff for $x\le 10^6$)[[/nomath]] shows the following maximizing examples:

* (x=10^2): best ratio (\approx 4.330) at $n=96$, with ((f_{\min},f_{\max})=(97,420)).
* (x=10^3): best ratio (\approx 4.731) at $n=576$, with $(577,2730)$.
* (x=10^4): best ratio (\approx 5.113) at $n=7680$, with $(7681,39270)$.
* (x=10^5): best ratio (\approx 5.213) at $n=63360$, with $(63361,330330)$.
* (x=10^6): best ratio (\approx 5.539) at $n=921600$, with $(921601,5105100)$.

In all these cases, the maximizing $n$ is $p-1$ with $p$ prime, i.e. $f_{\min}(n)=n+1$, which is exactly what you’d expect when trying to maximize the ratio: make the minimum preimage as small as possible and push the maximum preimage into a “many small primes” regime.

These values are also within a slowly shrinking constant factor of (e^\gamma\log\log x), which is what the conjectured asymptotic would predict.

## Summary of what is known/expected

* Unconditionally,
  [
  R(x)\le (e^\gamma+o(1))\log\log x
  ]
  via the classical maximal-order theory of (m/\varphi(m)). ([arXiv][2])

* Matching lower bounds of order (\log\log x) with the same constant (e^\gamma) appear **plausible** and are supported by computation, but **a proof is not currently known** (the problem is explicitly listed as open). ([Erdős Problems][1])

If you want, I can also write out the cleanest “conditional proof” template [[nomath]](exactly what hypothesis about primes in the progression $1 \bmod \varphi(p_r)$ would be sufficient to force $R(x)\gg \log\log x$)[[/nomath]], since that seems to be the main bottleneck discussed in the heuristic approach.

[1]: https://www.erdosproblems.com/694 "
  
    Erdős Problem #694
  
"
[2]: https://arxiv.org/pdf/1202.0729?utm_source=chatgpt.com "Small values of the Euler function and the Riemann ..."
[3]: https://en.wikipedia.org/wiki/Mertens%27_theorems "Mertens' theorems - Wikipedia"
[4]: https://www.erdosproblems.com/forum/thread/694 "

    Erdős Problem #694 - Discussion thread

"
