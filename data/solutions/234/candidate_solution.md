Let (d_n := p_{n+1}-p_n). The statement you wrote is asking for a **limiting distribution** of the normalized gaps
[
\frac{d_n}{\log n}
]
in the following very strong sense:

Define (if it exists)

$$
f(c)\ :=\ \lim_{N\to\infty}\frac{1}{N}|\\{1\le n\le N:\ \frac{d_n}{\log n}<c\\}|,\qquad c\ge 0.
$$

Erdős asked whether **this limit exists for every (c\ge 0)** and whether the resulting function $f(c)$ is **continuous**.

### Status: open

This is **open** (Erdős problem #234), i.e. currently unproved for the actual primes. ([Erdős Problems][1])

---

## What is expected if primes behaved “randomly”?

A standard heuristic is that primes near size (x) behave like a Poisson process with intensity (\approx 1/\log x). In that model, **waiting times** (gaps) are exponential, so the normalized gaps (d_n / \log x) have an exponential distribution, which would give
[
f(c)\ =\ 1-e^{-c}.
]

More than just heuristics: Gallagher showed that a sufficiently strong Hardy–Littlewood prime tuples conjecture implies that prime gaps (with (p_n\le x)) are asymptotically exponentially distributed with mean (\log x). ([What's new][2])
This is also noted in the Erdős problem discussion: “on the prime tuples conjecture … (f(c)=1-e^{-c}).” ([Erdős Problems][1])

So **conditionally** (on strong prime tuples asymptotics), the statement holds and (f) is not just continuous but smooth.

---

## What *is* known unconditionally (partial progress)

Even though the full density/continuity statement is open, several nontrivial partial results are known.

### 1) Small normalized gaps occur with positive proportion (but no limiting density known)

Goldston–Pintz–Yıldırım define, for (\eta>0),
[
P(x,\eta)\ :=\ \frac{1}{\pi(x)}|\\{p_n\le x:\ d_n\le \eta \log p_n\\}|.
]
They prove that for every fixed (\eta>0),
[
P(x,\eta)\ \gg_\eta\ 1 \quad (x\to\infty),
]
i.e. **a positive proportion of gaps are (\le \eta) times the average gap**. ([arXiv][3])

They also obtain an upper bound of the “right” order for small (\eta) in a range:
[
P(x,\eta)\ \ll\ \eta \qquad (1/\log x \ll \eta \ll 1). ([arXiv][3])
]
Under the Poisson/Hardy–Littlewood picture one expects (P(x,\eta)\sim 1-e^{-\eta}), and they explicitly state this as the predicted behavior (via Gallagher). ([arXiv][3])

What this **doesn’t** give is the existence of a limit (P(\infty,\eta)) [[nomath]](or $f(\eta)$)[[/nomath]]; it only gives bounds that hold along the full limit (x\to\infty).

### 2) The set of limit points of (\frac{d_n}{\log p_n}) is very large (but again this is weaker than a density)

Let (\mathbb{L}) be the set of limit points of ({d_n/\log p_n}). Merikoski (building on earlier work of Banks–Freiberg–Maynard and Pintz) proves strong results about how large (\mathbb{L}) is, including:

* (\mu(\mathbb{L}\cap [0,T]) \ge T/3) for all (T\ge 0) [[nomath]](Lebesgue measure $\mu$)[[/nomath]], and
* (\mathbb{L}) is **syndetic**: every interval $[T,T+C]$ meets (\mathbb{L}) for some absolute $C$. ([arXiv][4])

This says that normalized gaps hit a “large” set of values infinitely often, but it does **not** control *frequencies* well enough to produce a limiting distribution $f(c)$.

---

## Why continuity is (probably) “easier” than existence

If the limits $f(c)$ existed, one expects (and Tao remarks) that **upper-bound sieve estimates** should give a quantitative continuity property (e.g. Lipschitz-type control), hence continuity. ([Erdős Problems][1])
But the *existence of the limits* is the hard part: it requires showing the proportion of gaps below (c\log n) actually stabilizes as (n\to\infty), not merely that it has subsequential limits or bounds.

---

## A quick note on (\log n) vs (\log p_n)

Many papers normalize by (\log p_n) (the local average gap), while your statement uses (\log n). Since (p_n \sim n\log n), one has (\log p_n = \log n + \log\log n + o(1)), so (\log p_n/\log n \to 1). In the *expected* limiting distribution picture [[nomath]](and especially if $f$ is continuous)[[/nomath]], this distinction should not matter—but making that fully rigorous at the level of pointwise limiting densities is delicate.

---

### Bottom line

* The claim “for every (c\ge 0) the density exists and $f$ is continuous” is a **famous open problem of Erdős**. ([Erdős Problems][1])
* Under strong Hardy–Littlewood prime tuples assumptions, one gets an **exponential limiting law** (f(c)=1-e^{-c}). ([What's new][2])
* Unconditionally, we have significant partial information (positive proportion of small gaps; large limit-point set), but not the existence of $f(c)$ for all $c$. ([arXiv][3])

If you want, I can also spell out how Gallagher’s exponential law translates into the exact (f(c)=1-e^{-c}) formula [[nomath]](and how the $p_n\le x$ normalization relates to indexing by $n$)[[/nomath]].

[1]: https://www.erdosproblems.com/forum/thread/234 "https://www.erdosproblems.com/forum/thread/234"
[2]: https://terrytao.wordpress.com/2019/08/26/large-prime-gaps-and-probabilistic-models/ "https://terrytao.wordpress.com/2019/08/26/large-prime-gaps-and-probabilistic-models/"
[3]: https://arxiv.org/pdf/1103.3986 "https://arxiv.org/pdf/1103.3986"
[4]: https://arxiv.org/pdf/1811.03008 "https://arxiv.org/pdf/1811.03008"
