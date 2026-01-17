Let
[
f(n,r):=\max{|E(G)|:\ |V(G)|=n,\ \text{every edge of }G\text{ lies in a triangle, and every edge lies in }\le r-1\text{ triangles}}.
]
Then by definition (e(n,r)=f(n,r)+1).

### What is known about the size of $e(n,r)$

* For every fixed (r\ge 2), one has
  [
  e(n,r)=o(n^2)\qquad (n\to\infty),
  ]
  proved by Ruzsa and Szemerédi. ([Erdős Problems][1])

* The case $r=2$ is exactly the classical **Ruzsa–Szemerédi (6,3)-problem**: graphs in which *every edge belongs to a unique triangle* (equivalently, every edge is in at least one triangle and no edge is in two). ([Wikipedia][2])
  For this case [[nomath]](hence for every $r\ge 2$, since such graphs also avoid having an edge in $\ge r$ triangles)[[/nomath]], the best general bounds are of the form
  [
  \frac{n^2}{\exp(O(\sqrt{\log n}))}\ \lesssim\ e(n,2)\ \lesssim\ \frac{n^2}{\exp(\Omega(\log^* n))}.
  ]
  The lower bound comes from Behrend-type 3AP-free set constructions, and the upper bound from Fox’s improved graph/triangle removal lemma. ([Wikipedia][2])

* The same removal-lemma argument gives, for each fixed $r$, an upper bound of the same qualitative type [[nomath]](up to an $O_r(1)$ factor)[[/nomath]], so at present $e(n,r)$ is only pinned down to within a very large “subpolynomial” gap even for $r=2$. ([Annals of Mathematics][3])

### Your two questions

These are **open** (and in fact are posed verbatim as Erdős Problem #600). ([Erdős Problems][1])

In particular, since we do not know the asymptotic behavior of $e(n,r)$ even for $r=2$ (the Ruzsa–Szemerédi problem), there is currently no known way to decide either

[
e(n,r+1)-e(n,r)\to\infty
\qquad\text{or}\qquad
\frac{e(n,r+1)}{e(n,r)}\to 1
\quad (n\to\infty)
]
for any fixed (r\ge 2). ([Erdős Problems][1])

If you want, I can also sketch the standard reduction from your $r=2$ case to the triangle removal lemma [[nomath]](the usual way one proves $e(n,2)=o(n^2)$)[[/nomath]], because it clarifies why quantitative progress here is tied to quantitative removal-lemma bounds.

[1]: https://www.erdosproblems.com/600 "
  
    Erdős Problem #600
  
"
[2]: https://en.wikipedia.org/wiki/Ruzsa%E2%80%93Szemer%C3%A9di_problem "https://en.wikipedia.org/wiki/Ruzsa%E2%80%93Szemer%C3%A9di_problem"
[3]: https://annals.math.princeton.edu/wp-content/uploads/annals-v174-n1-p17-p.pdf "https://annals.math.princeton.edu/wp-content/uploads/annals-v174-n1-p17-p.pdf"
