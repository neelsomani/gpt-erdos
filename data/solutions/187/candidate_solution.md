This is a classical Erdős–Cohen problem (Erdős Problem #187), and **the exact “best” growth of $f(d)$ is not known**. What *is* known is a fairly sharp **upper bound** (via an explicit 2‑colouring construction) and only a very weak **lower bound** (that $f(d)$ must be unbounded).

A standard way to formalize “best” is: among all functions (f:\mathbb N\to\mathbb N) with the property

> for every 2‑colouring of (\mathbb Z), there is a colour class containing a monochromatic arithmetic progression of length $f(d)$ and common difference $d$ for infinitely many $d$,

determine/estimate the largest possible growth rate of such an $f$.

## What is known (best current bounds)

### Upper bound: $f(d)$ cannot beat (\log_2 d) (up to $1+o(1)$)

Beck proved (using the probabilistic method) that there exists a 2‑colouring of the integers in which **every** monochromatic arithmetic progression with common difference (d) has length at most about (\log_2 d). Concretely, this shows that any “best possible” $f$ must satisfy
[
f(d)\ \le\ (1+o(1)),\log_2 d\qquad (d\to\infty).
]
This is the strongest published upper bound and is the one usually cited today. ([Erdős Problems][1])

Earlier (weaker) explicit upper bounds were known before Beck:

* Erdős gave an explicit colouring (via the fractional parts ({\sqrt2,n})) implying (f(d)\ll d). ([Erdős Problems][1])
* Petruska–Szemerédi improved this to (f(d)\ll d^{1/2}) (as reported by Erdős–Graham). ([Rényi Institute][2])
  Beck’s (\log d) upper bound supersedes these asymptotically.

### Lower bound: $f(d)$ must be unbounded, but no effective rate is known

Van der Waerden’s theorem implies that in any 2‑colouring there are monochromatic arithmetic progressions of **arbitrarily large length** (with some common differences), so any “best” $f$ cannot be bounded; it must take arbitrarily large values. ([Erdős Problems][1])

However—and this is the key point—**there is currently no “usable” quantitative lower bound on the growth of the optimal $f(d)$** [[nomath]](e.g. nothing like $f(d)\ge c\log\log d$ is known in general)[[/nomath]]. This lack of a meaningful lower bound is explicitly noted in the Erdős–Graham discussion of the problem. ([Rényi Institute][2])

[[nomath]](Trivially, if one doesn’t insist that $f(d)\to\infty$, you can take $f(d)=2$, since some colour class is infinite and hence produces same‑colour pairs $(a,a+d)$ for infinitely many $d$. The real content is how fast $f(d)$ can be forced to grow.)[[/nomath]]

## So what is the “best” $f(d)$ today?

As of the current literature summaries, the situation is:

[
\textbf{Unbounded (no effective lower bound known)}\ \ \le\ f(d)\ \ \le\ (1+o(1))\log_2 d.
]

Closing this gap—proving any substantial lower bound, or showing Beck’s logarithmic upper bound is essentially tight—is the open part of the problem. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/latex/187 "https://www.erdosproblems.com/latex/187"
[2]: https://www.renyi.hu/~p_erdos/1979-07.pdf "https://www.renyi.hu/~p_erdos/1979-07.pdf"
