Write “properly 2‑colorable” for a red/blue coloring with **no monochromatic edge** (this is *Property B*).
An $n$-uniform hypergraph is **3‑chromatic** iff it is **not** 2‑colorable but is 3‑colorable. For the extremal function here, you can identify $m(n)$ with the classical “minimum size of an $n$-uniform hypergraph without Property B”:

* If $H$ is edge‑minimal among non‑2‑colorable $n$-uniform hypergraphs, then $H$ is automatically 3‑colorable: pick an edge $e$. Since $H-e$ is 2‑colorable, take a proper red/blue coloring of $H-e$. Then $e$ must be monochromatic in that coloring [[nomath]](otherwise it would 2‑color $H$)[[/nomath]]. Recolor one vertex of $e$ with a third color; this cannot create a monochromatic edge elsewhere because every other edge already had both red and blue. Hence (\chi(H)=3).

So estimating $m(n)$ is exactly the famous Erdős–Lovász “Property B” extremal problem.

## Bounds

### Basic lower bound

A random 2‑coloring makes a fixed $n$-edge monochromatic with probability (2^{1-n}). If (m<2^{n-1}), then the expected number of monochromatic edges is (m,2^{1-n}<1), so some coloring has none; hence $H$ is 2‑colorable. Therefore
[
m(n)\ \ge\ 2^{,n-1}.
]


### Best known asymptotic lower bound (Radhakrishnan–Srinivasan)

The strongest general lower bound currently known is
[
m(n)\ =\ \Omega!\left(2^n\sqrt{\frac{n}{\log n}}\right),
]
coming from Radhakrishnan–Srinivasan’s (2000) improvement (via a random greedy recoloring argument / algorithmic analysis). In particular, they show that every $n$-uniform hypergraph with at most on the order of (2^n\sqrt{n/\log n}) edges is 2‑colorable, forcing $m(n)$ to be at least that large. ([UMD Computer Science][1])

### Best known asymptotic upper bound (Erdős)

Erdős gave a probabilistic construction of an $n$-uniform hypergraph with no proper 2‑coloring using
[
m(n)\ =\ O\left(n^2,2^n\right)
]
edges (and this remains the best general upper bound in order of magnitude). 

## Summary estimate

Putting the best known bounds together,
[
\boxed{\ c,2^n\sqrt{\frac{n}{\log n}}\ \le\ m(n)\ \le\ C,n^2,2^n\ }
]
for absolute constants (c,C>0). ([arXiv][2])

There is still a polynomial gap. Erdős–Lovász famously conjectured the “right” order is
[
m(n)=\Theta(n,2^n),
]
which would sit between the bounds above. 

[1]: https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf "aug16-99.dvi"
[2]: https://arxiv.org/abs/2403.05674 "[2403.05674] Improved Lower Bounds for Property B"
