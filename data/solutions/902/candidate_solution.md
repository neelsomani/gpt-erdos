Write (S\subseteq V(T)) is **dominated** if there is a vertex (x\notin S) with (x\to s) for every (s\in S). Your $f(n)$ is the minimum order of a tournament with the property that **every** $n$-set is dominated [[nomath]](this is often called the “weak $S_n$-property”)[[/nomath]]. 

## Known order of magnitude

The best general bounds (and the right “shape” of the answer) are

[
2^{,n-1}(n+2)-1 \le f(n) \le (1+o(1)),(\ln 2),n^2,2^n.
]

Equivalently,
[
f(n)=2^n\cdot \mathrm{poly}(n),
]
with the polynomial factor known to be between (\Theta(n)) and (\Theta(n^2)). 

So $f(n)$ is exponential in $n$ with base $2$, but the precise polynomial factor is not pinned down; there is still a gap by a factor of (\Theta(n)) between the best lower and upper bounds. 

---

## Why $f(n)$ is at most about ((\ln2)n^2 2^n) (probabilistic upper bound)

Take a random tournament on $N$ vertices [[nomath]](orient each edge independently with probability $1/2$)[[/nomath]].

Fix an $n$-set $S$. For a vertex (v\notin S), the probability that $v$ dominates $S$ is (2^{-n}) [[nomath]](it must beat each of the $n$ vertices of $S$)[[/nomath]]. Hence
[
\Pr(S\text{ has no dominator})=(1-2^{-n})^{N-n}.
]

By the union bound over all (\binom{N}{n}) choices of $S$,
[
\Pr(\exists\text{ undominated }S)\le\binom{N}{n}(1-2^{-n})^{N-n}.
]
So if (\binom{N}{n}(1-2^{-n})^{N-n}<1), then with positive probability **no** bad set exists, i.e. a tournament with the required property exists. 

Now estimate the threshold. Use
[
\binom{N}{n}\le \left(\frac{eN}{n}\right)^n,\qquad
(1-2^{-n})^{N-n}\le \exp!\left(-\frac{N-n}{2^n}\right).
]
It suffices that
[
n\ln!\left(\frac{eN}{n}\right) ;<; \frac{N}{2^n}.
]
Taking (N=(\ln2+\varepsilon)n^2 2^n) makes the right side ((\ln2+\varepsilon)n^2), while the left side is (n\ln(e(\ln2+\varepsilon)n2^n)=n^2\ln2+O(n\ln n)), and the inequality holds for large $n$. This yields
[
f(n)\le (1+o(1))(\ln2),n^2,2^n,
]
the classical Erdős-type bound. 

---

## Why $f(n)$ is at least about (\tfrac12 n2^n) (Szekeres–Szekeres lower bound)

Moon’s book (recounting Szekeres–Szekeres) proves a more general statement: if a tournament has the property $S(k,m)$ that **every** $k$-set is dominated by **at least $m$** vertices, then
[
N \ge 2^k(m+1)-1.
]
The proof is by induction on $k$, looking at the subtournament (T_d) induced by the in-neighbors of a vertex $p$; (T_d) inherits an $S(k-1,m)$-type property, forcing each vertex to have large in-degree, and then counting total in-degrees gives the inequality. ([Project Gutenberg][1])

From that, one derives the stronger corollary for $m=1$ (your setting): if a tournament has property $S(k,1)$, then in fact it must have property $S(k-1,k+1)$ (otherwise a short “double domination” contradiction occurs), and plugging (m=k+1) into the general bound gives
[
N \ge 2^{k-1}(k+2)-1.
]
Thus for your $f(n)$,
[
f(n)\ge 2^{n-1}(n+2)-1 = \left(\frac{n}{2}+1\right)2^n-1.
]
([Project Gutenberg][1])

---

## Bottom line

[
\boxed{ \left(\frac{n}{2}+1\right)2^n -1 \le f(n)\le (1+o(1))(\ln2),n^2 2^n. }
]

So $f(n)$ is exponential (2^n) with a polynomial factor between linear and quadratic in $n$; narrowing that (\Theta(n)) gap is (as far as these standard references indicate) nontrivial and not settled by the classic bounds alone. 

[1]: https://www.gutenberg.org/files/42833/42833-pdf.pdf "The Project Gutenberg eBook #42833: Topics on Tournaments."
