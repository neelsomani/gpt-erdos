Let $P$ be a set of $n$ points in the plane in *general position* (no three collinear and no four concyclic), and let
[
R(P)=|\\{\text{distinct radii of circumcircles of triples of }P\\}|.
]
Then your $h(n)$ is exactly
[
h(n)=\min_{|P|=n} R(P),
]
i.e. the minimum possible number of distinct circumradii among the (\binom{n}{3}) circles determined by triples of points. Erdős explicitly asked to “estimate or determine $h(n)$” in this general-position setting. ([Renyi Users][1])

## A clean universal lower bound: (h(n)\ge \lceil (n-2)/2\rceil)

Fix a radius (\rho). Let (T_\rho) be the number of triangles (ABC\subset P) whose circumradius equals (\rho).

Count *edge–triangle incidences* among these triangles:

* Each triangle contributes **3** incidences (its 3 edges), so total incidences for radius (\rho) equals (3T_\rho).
* Fix an unordered pair ({A,B}). For a **fixed** (\rho), there are at most **two** circles of radius (\rho) through $A$ and $B$ [[nomath]](centers are the two intersection points of the circles of radius $\rho$ around $A$ and $B$)[[/nomath]].
  By the “no four concyclic” assumption, each such circle can contain **at most one** additional point of $P$. Hence, for this fixed pair ({A,B}), there are **at most 2** triangles (ABC) with circumradius (\rho).

Therefore, summing over all (\binom{n}{2}) pairs,
[
3T_\rho \le 2\binom{n}{2}
\quad\Longrightarrow\quad
T_\rho \le \frac{2}{3}\binom{n}{2}.
]

Now sum over all distinct radii (\rho) that occur:
[
\binom{n}{3}=\sum_{\rho} T_\rho
\le |R(P)|\cdot \frac{2}{3}\binom{n}{2}.
]
So
[
|R(P)| \ge \frac{\binom{n}{3}}{\frac{2}{3}\binom{n}{2}}
= \frac{n-2}{2}.
]
Since (|R(P)|) is an integer,
[
R(P)\ge \left\lceil\frac{n-2}{2}\right\rceil
\quad\text{for every such }P,
]
and hence
[
\boxed{h(n)\ \ge\ \left\lceil\frac{n-2}{2}\right\rceil.}
]

So (h(n)=\Omega(n)) with an explicit constant $1/2$.

## What about an upper bound / the true order?

This is where the difficulty lies. Erdős posed this as an open-ended estimate problem in 1975, and it is still listed as open in that form. ([Renyi Users][1])

The lower bound above uses only the “at most two circles of a fixed radius through a fixed pair” fact plus “no four concyclic,” and it is not known (as far as standard references indicate) whether $h(n)$ is actually (\Theta(n)) or must grow faster.

### Related result without the “no four concyclic” restriction

A closely related (but weaker) problem asks for the minimum number of distinct radii of circles spanned by $n$ points **without** requiring general position (just “not all on a line or a circle”). In that setting:

* A construction [[nomath]](vertices + centroid of a regular $(n-1)$-gon)[[/nomath]] shows an $O(n)$ upper bound.
* Elekes proved an (\Omega(n)) lower bound.

So in that weaker setting the answer is (\Theta(n)). ([NoZDR][2])

Your general-position condition rules out that very efficient construction [[nomath]](it puts $n-1$ points on one circle)[[/nomath]], so it’s plausible $h(n)$ could be larger here — but the sharp growth is not settled.

### Connection to “many congruent circles”

If one could prove that, in general position, **no fixed radius** can occur for more than $o(n^2)$ of the (\binom{n}{3}) triples, then automatically
[
h(n)\ =\ \omega(n),
]
because (\binom{n}{3}) triangles would have to be spread across more than linear many radii. This connects $h(n)$ to the difficult extremal questions about how many circles of a fixed radius can be “3-rich” in an $n$-point set, which are also widely studied and not fully resolved. ([NoZDR][2])

## Summary of the best clean estimate you can state unconditionally

* **Provable (elementary):**
  [
  \boxed{h(n)\ \ge\ \left\lceil\frac{n-2}{2}\right\rceil\ =\ \frac{n}{2}-O(1).}
  ]
* **Trivial upper bound:**
  [
  h(n)\le \binom{n}{3}\sim \frac{n^3}{6}.
  ]
* **Status:** determining the true asymptotic growth of $h(n)$ under the general-position assumptions is an Erdős problem and is still regarded as open. ([Renyi Users][1])

If you want, I can also spell out what kind of configuration would have to exist to make the lower bound (\sim n/2) tight (it would require near-saturation of the “2 triangles per pair per radius” bound across many radii), and why that seems geometrically nontrivial.

[1]: https://users.renyi.hu/~p_erdos/1975-41.pdf "https://users.renyi.hu/~p_erdos/1975-41.pdf"
[2]: https://nzdr.ru/data/media/biblio/kolxoz/M/MD/Brass%20P.%2C%20Moser%20W.%2C%20Pach%20J.%20Research%20problems%20in%20discrete%20geometry%20%28Springer%2C%202005%29%28ISBN%200387238158%29%28O%29%28513s%29_MD_.pdf "https://nzdr.ru/data/media/biblio/kolxoz/M/MD/Brass%20P.%2C%20Moser%20W.%2C%20Pach%20J.%20Research%20problems%20in%20discrete%20geometry%20%28Springer%2C%202005%29%28ISBN%200387238158%29%28O%29%28513s%29_MD_.pdf"
