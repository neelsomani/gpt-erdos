Write your family (\mathcal H={A_i}) as a $k$-uniform hypergraph and let (\tau(\mathcal H)) be its transversal (hitting) number. Your hypothesis is exactly that **every subhypergraph on $r$ edges has (\tau\le 2)** [[nomath]](often called “property $(r,2)$” in the Erdős–Hajnal–Tuza / Erdős–Fon-Der-Flaass–Kostochka–Tuza notation)[[/nomath]]. Then $f(k,r)$ is the **maximum possible** (\tau(\mathcal H)) over all such $k$-uniform (\mathcal H).

## The case $r=7$

As far as the published literature I can access, the asymptotic
[
f(k,7)=(1+o(1))\frac34,k
]
is **not known**.

What *is* known is that $f(k,7)$ is sandwiched between linear bounds with constants $3/4$ and $7/8$:

* **Lower bound (\ge (3/4)k - O(1))**: Fon-Der-Flaass, Kostochka, and Woodall construct examples with $k$ divisible by $4$ showing
  [
  f(4m,7)\ge 3m+1 \qquad (m\ge 10),
  ]
  i.e. $f(k,7)\ge \tfrac34k+1$ for (k\equiv 0\pmod 4) and $k$ large. ([Kostochka Lab][1])
  [[nomath]](They also point out the complete $k$-uniform clique example giving essentially the same $\tfrac34k$ lower bound asymptotically.)[[/nomath]] ([Kostochka Lab][1])

* **Upper bound (\le (7/8)k + O(1))**: the same paper proves
  [
  f(k,7)\le \left\lceil \frac{7k}{8}\right\rceil .
  ]
  ([Kostochka Lab][1])

So currently one has
[
\frac34,k+O(1)\ \le\ f(k,7)\ \le\ \frac78,k+O(1),
]
and the conjectured (\frac34) asymptotic constant is still open.

## Existence of a linear asymptotic constant (c_r) for general $r$

For small $r$ the answer is “yes” and the constant is explicitly known:

[
f(k,3)=2k,\quad f(k,4)=\left\lfloor \frac{3k}{2}\right\rfloor,\quad
f(k,5)=\left\lfloor \frac{5k}{4}\right\rfloor,\quad f(k,6)=k.
]
([Erdős Problems][2])

So for (r=3,4,5,6) you can take
[
c_3=2,\quad c_4=\tfrac32,\quad c_5=\tfrac54,\quad c_6=1.
]

For (r\ge 7), the existence of a sharp asymptotic constant (c_r) [[nomath]](i.e. the existence of a limit $f(k,r)/k\to c_r$)[[/nomath]] is, at least in the same sense as the $r=7$ question, **not settled**: already $r=7$ is open, so the general statement is also open.

That said, two basic (and useful) facts are easy:

### 1) $f(k,r)$ is always (O_r(k)) (trivial linear upper bound)

Your property implies there is **no matching of size $r$** [[nomath]](because $r$ disjoint $k$-sets would require a transversal of size $\ge r$, contradicting “every $r$ edges are hit by 2 points”)[[/nomath]]. Hence the matching number (\nu(\mathcal H)\le r-1). A maximal matching has at most $r-1$ edges and its vertices cover all edges, so
[
\tau(\mathcal H)\le k,\nu(\mathcal H)\le k(r-1).
]
Therefore
[
f(k,r)\le (r-1)k
]
for every fixed $r$.

So “linear in $k$” [[nomath]](in the weak sense $f(k,r)=O_r(k)$)[[/nomath]] is straightforward; the nontrivial part is pinning down the best constant and whether the ratio converges.

### 2) There are natural linear lower bounds (clique constructions)

For (r\ge 7), the complete $k$-uniform hypergraph on $n$ vertices with (n<2k) is intersecting, and if $n$ is also small enough compared to (rk) then among any $r$ edges one vertex appears in (\ge r-2) of them, leaving only (\le2) edges to be hit; the (n<2k) condition forces those remaining two to intersect, giving the required 2-point transversal.

This is exactly the mechanism behind the (\tfrac34) lower bound example for $r=7$ discussed in Fon-Der-Flaass–Kostochka–Woodall. ([Kostochka Lab][1])

It suggests a **candidate constant** for (r\ge 6),
[
c_r \stackrel{?}{=} \frac{3}{r-3},
]
since the corresponding clique has (\tau \approx \big(\frac{r}{r-3}-1\big)k = \frac{3}{r-3}k). This matches the known exact case $r=6$ ((c_6=1=3/(6-3))) and the conjecture in your first question ((c_7=3/4)), but it is **not proved** in general [[nomath]](and even $r=7$ is open)[[/nomath]].

## Bottom line

* The asymptotic (f(k,7)=(\tfrac34+o(1))k) is **open**; the best published bounds I can point to are
  [
  \tfrac34,k+O(1)\ \le\ f(k,7)\ \le\ \tfrac78,k+O(1).
  ]
  ([Kostochka Lab][1])

* For (r=3,4,5,6) the linear asymptotics are known exactly [[nomath]](with constants $2,\tfrac32,\tfrac54,1$)[[/nomath]]. ([Erdős Problems][2])
  For (r\ge 7), even the existence/value of the asymptotic constant is not settled in the literature I found; the general “(f(k,r)\sim c_r k)” question is therefore also **open**.

If you want, I can also write out (cleanly) the pigeonhole/intersection argument that shows the complete $k$-graph on (\big\lfloor \frac{rk}{r-3}\big\rfloor-1) vertices has property $(r,2)$ for (r\ge 7), since that’s the main heuristic reason the constant (3/(r-3)) is the “obvious” candidate.

[1]: https://kostochk.web.illinois.edu/docs/2000/dm1999FlaWoo.pdf "https://kostochk.web.illinois.edu/docs/2000/dm1999FlaWoo.pdf"
[2]: https://www.erdosproblems.com/forum/thread/644 "https://www.erdosproblems.com/forum/thread/644"
