This is **open** in the plane.

It is exactly **Erdős problem #657** [[nomath]](sometimes written in the notation $\phi(n,3,3)$)[[/nomath]], asking whether an $n$-point set in (\mathbb R^2) with **no isosceles triangles** must span **(\omega(n))** distinct distances [[nomath]](equivalently: at least $n,f(n)$ with $f(n)\to\infty$)[[/nomath]]. ([Erdős Problems][1])

### What is known

Let (A\subset\mathbb R^2), (|A|=n), and assume every triple determines three distinct distances.

**1) Only linear lower bounds are known.**
A standard “pinned” argument gives (D(A)\ge n-1): fix (p\in A). If (|pp_1|=|pp_2|) for two distinct (p_1,p_2\in A), then $(p,p_1,p_2)$ is isosceles, forbidden. Hence the $n-1$ distances from $p$ to (A\setminus{p}) are all distinct. ([NYU Math][2])

There is a small sharpening (essentially a matching/edge-coloring count): color the edges of (K_n) by their lengths. Since equal-length edges cannot meet at a vertex, each color class is a matching of size at most (\lfloor n/2\rfloor), so
[
\binom{n}{2}\le D(A)\lfloor n/2\rfloor
\quad\Rightarrow\quad
D(A)\ge
\begin{cases}
n, & n\ \text{odd},\
n-1, & n\ \text{even}.
\end{cases}
]
([Erdős Problems][3])

**Crucially:** no superlinear lower bound (D(A)\ge nf(n)) with (f(n)\to\infty) is known in (\mathbb R^2). ([Erdős Problems][1])

**2) There is a near-linear upper bound construction.**
Using a 1D construction (Behrend-type sets with no 3-term arithmetic progression) and placing the points on a line in (\mathbb R^2), one gets isosceles-free sets with
[
D(A)\ \le\ n\cdot 2^{O(\sqrt{\log n})}
\quad\text{(equivalently }n,e^{O(\sqrt{\log n})}\text{)}.
]
So (\phi(n,3,3)) is known to be at most $n$ times a **subpolynomial** factor. ([NYU Math][2])

**3) Context from other dimensions (to calibrate expectations).**
In sufficiently high dimension (e.g. (2^k\ge n)), there are constructions of $n$ points in (\mathbb R^k) with no isosceles triangles that determine only $n-1$ distances, showing that superlinearity is not true in general dimensions. ([Erdős Problems][1])

### Bottom line

As of the most recent sources (edited Oct 15, 2025; and surveyed in the literature cited there), it is **not known** whether forbidding isosceles triangles in (\mathbb R^2) forces more than $O(n)$ distinct distances, let alone (n,f(n)) with (f(n)\to\infty). The best current bounds are essentially
[
n-1\ \text{(or }n\text{)}\ \le\ \phi(n,3,3)\ \le\ n\cdot 2^{O(\sqrt{\log n})},
]
and improving the **lower bound beyond linear** is the main open difficulty. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/657 "
  
    Erdős Problem #657
  
"
[2]: https://math.nyu.edu/~pach/publications/ddistances052116-1.pdf "ddistances052116.dvi"
[3]: https://www.erdosproblems.com/forum/thread/657 "

    Erdős Problem #657 - Discussion thread

"
