Let

[
f_{r,k}(n):=\frac{\mathrm{ex}_r(n,K_k^r)}{\binom nr},
]

i.e. the **maximum edge–density** of an $r$-uniform hypergraph on $n$ vertices with no copy of the complete $r$-graph on $k$ vertices.

## What is known in general

A standard averaging argument shows that the sequence (f_{r,k}(n)) is **monotone decreasing in $n$**, hence it has a limit as (n\to\infty). This limit is called the **Turán density** of (K_k^r):

[
\pi(K_k^r):=\lim_{n\to\infty}\frac{\mathrm{ex}_r(n,K_k^r)}{\binom nr}.
]

So asymptotically,
[
\mathrm{ex}*r(n,K_k^r)=\bigl(\pi(K_k^r)+o(1)\bigr)\binom nr,
\qquad\text{equivalently}\qquad
f*{r,k}(n)=\pi(K_k^r)+o(1).
]


## The punchline for (k>r>2)

For **every** (k>r\ge 3), the exact value of (\pi(K_k^r))—and therefore the asymptotic value of (f_{r,k}(n))—is a famous open problem in extremal combinatorics. In particular, *no* Turán density (\pi(K_k^r)) is known exactly for any (k>r\ge 3). ([Mathematics and Statistics at GSU][1])

Even the smallest nontrivial case (r=3,k=4) [[nomath]](i.e. forbidding $K_4^3$)[[/nomath]] is still open and is widely conjectured to have (\pi(K_4^3)=5/9). 

## Best general bounds (what you can “determine” today)

Although the exact value is unknown, there are general bounds (due to Sidorenko and de Caen) that hold for all (k>r\ge 3):

[
1-\left(\frac{r-1}{k-1}\right)^{r-1}
\le
\pi(K_k^r)
\le
1-\frac{1}{\binom{k-1}{r-1}}.
]


Equivalently, for large $n$,

[
\left(1-\left(\frac{r-1}{k-1}\right)^{r-1}-o(1)\right)\binom nr
;\le;
\mathrm{ex}_r(n,K_k^r)
;\le;
\left(1-\frac{1}{\binom{k-1}{r-1}}+o(1)\right)\binom nr.
]


These show, for fixed $r$, that (\pi(K_k^r)\to 1) as (k\to\infty), with the “gap to 1” on the order of (k^{-(r-1)}), but they do **not** pin down the exact constant.

## Example: the first open case (K_4^3)

* Conjectured: (\pi(K_4^3)=5/9). 
* Known lower bound: (\pi(K_4^3)\ge 5/9) (many constructions attain this density). 
* Best-known upper bounds are obtained by flag algebra methods: Razborov gave (\pi(K_4^3)\le 0.561666). 
  Baber later reported a slight improvement to (\pi(K_4^3)\le 0.5615) using “partially defined” objects/regularity constraints. 

---

### Bottom line

For (k>r>2),
[
\frac{\mathrm{ex}_r(n,K_k^r)}{\binom nr}
]
has a well-defined limit (\pi(K_k^r)) as (n\to\infty), but **determining that limit (and thus the asymptotic value of the ratio) is open in general**; the best general statement is that it lies between the Sidorenko and de Caen bounds above. view0

[1]: https://math.gsu.edu/yzhao6/turan_den.pdf "An Exact Result for Hypergraphs and Upper Bounds for the Turán Density of $K^r_{r+1}$ | SIAM Journal on Discrete Mathematics | Vol. 23, No. 3 | Society for Industrial and Applied Mathematics"
