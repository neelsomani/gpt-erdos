Write
[
\Sigma^*(A):=\\{\sum_{a\in S}a:\ \emptyset\neq S\subseteq A\\}
]
(the nonempty subset–sums / finite sums set). Your $F(k)$ is exactly the **two–colour Folkman number for finite sums** (a finite version of Hindman/Folkman–Rado–Sanders). Its existence is guaranteed by **Folkman’s theorem**. ([Combinatorics][1])

What is known quantitatively is very far from sharp: the best lower bound is already *doubly exponential*, while the best upper bound is still *tower-type*.

## Best known bounds (two colours)

**Lower bound (Balogh–Eberhard–Narayanan–Treglown–Wagner, 2017).**
They proved
[
F(k)\ \ge\ 2^{2^{k-1}/k}.
]
Equivalently, (\log_2 F(k)\ge 2^{k-1}/k), so $F(k)$ is at least (2^{2^{(1-o(1))k}}). ([arXiv][2])

**Upper bound (A. Taylor, 1980; “tower-type”).**
The best known general upper bound is an **exponentiation tower** of height linear in $k$. One convenient way it is stated in the literature is
[
F(k)\ \le\ 2^{2^{3^{2^{3^{\cdot^{\cdot^{3}}}}}}}
\qquad\text{(a power tower of total height }4k-3\text{).}
]
([Combinatorics][1])

So, in “order-of-growth” language:
[
2^{,2^{k-1}/k}\ \le\ F(k)\ \le\ \text{(an exponential tower of height }O(k)\text{)}.
]
([Combinatorics][1])

## Heuristic “right scale” (why doubly–exponential is plausible)

For a fixed $k$-set $A$, the probability (under a random 2–colouring) that $\Sigma^*(A)$ is monochromatic is about $2^{1-|\Sigma^*(A)|}$. Typically $|\Sigma^*(A)|$ is close to (2^k) (all subset sums distinct), so the probability is roughly (2^{1-2^k}). Since there are about (N^k) candidate $k$-sets, a first-moment heuristic suggests the “threshold” near
$
N^k\cdot 2^{-2^k}\approx 1
\quad\Rightarrow\quad
N\approx 2^{2^k/k},
$
which matches the **shape** of the best known lower bound (2^{2^{k-1}/k}) up to constants in the exponent. (Making this rigorous for an *adversarial* colouring is the hard part.) ([arXiv][2])

## Status

Closing the huge gap between “doubly exponential” and “tower-type” is open; this is listed as an Erdős problem in this form. ([erdosproblems.com][3])

[1]: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v26i2p22/pdf/ "https://www.combinatorics.org/ojs/index.php/eljc/article/download/v26i2p22/pdf/"
[2]: https://arxiv.org/abs/1703.02473 "https://arxiv.org/abs/1703.02473"
[3]: https://www.erdosproblems.com/531 "https://www.erdosproblems.com/531"
