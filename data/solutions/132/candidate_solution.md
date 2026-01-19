Write, for each distance value $d$,
$$
\mu(d)=|\\{{p,q}\subset A:\ |p-q|=d\\}|,
$$
the number of unordered pairs at distance $d$. Your question asks if there must be **at least two** different $d$’s with
[
1\le \mu(d)\le n.
]

### 1) Must there always be two such distances?

* You always get **at least one**: the **largest distance** (the diameter) occurs at most $n$ times (Hopf–Pannwitz, 1934). ([Erdős Problems][1])

* But **“two” is not always true for all $n$**: for (n=4) there is a counterexample (a rhombus made from two equilateral triangles). In that example one distance occurs (5>4) times, and only the other distance has multiplicity (\le 4), so you get only **one** qualifying distance. ([Erdős Problems][1])

* For (n\ge 5): the general case is **still open** as of January 2026. It is known to be true for (n=5) and (n=6) (Erdős–Fishburn), but for (n\ge 7) it is not settled in full generality. ([Erdős Problems][1])

* There are **special cases where it is proved**:

  * If the points are in **convex position** (no point inside the convex hull), then you do get a second distance with (\mu(d)\le n). ([Erdős Problems][1])
  * More generally, Clemen–Dumitrescu–Liu (2025) prove it for some “not too convex” point sets (a condition in terms of the first two convex layers). ([arXiv][2])

So the best short status is: **No for (n=4)**, **yes for (n=5,6)**, **open in general for (n\ge 7)**. ([Erdős Problems][1])

### 2) Must the number of such distances go to (\infty) with $n$?

This is also **open** in general. In fact, since we do not even know [[nomath]](for $n\ge 7$)[[/nomath]] whether there must be a *second* such distance, we certainly do not have a proof that the count must grow without bound. ([Erdős Problems][1])

What people *suspect* is much stronger: it “may be true” that there are almost linearly many such distances (something like (n^{1-o(1)})), but this is not proved. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/132 "
  
    Erdős Problem #132
  
"
[2]: https://www.arxiv.org/pdf/2505.04283v3 "On multiplicities of interpoint distances"
