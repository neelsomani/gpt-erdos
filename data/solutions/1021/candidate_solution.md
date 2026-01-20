Yes.

Your (G_k) is exactly the **1‑subdivision of (K_k)**: the (y_i)’s are the original vertices of (K_k), and each (z_{ij}) is the new subdivision vertex inserted on the edge (y_i y_j). In particular, (G_k) is bipartite, every $z$-vertex has degree $2$, and it is (C_4)-free [[nomath]](a $4$-cycle would require two distinct $z$’s joined to the same pair of $y$’s, which doesn’t happen here)[[/nomath]].

Conlon and Lee proved a general theorem that directly covers this situation:

* If $H$ is bipartite, has **maximum degree $2$ on one side**, and is **(C_4)-free**, then there exist constants (C,\delta>0) [[nomath]](depending on $H$)[[/nomath]] such that
  [
  \mathrm{ex}(n,H)\le C n^{3/2-\delta}.
  ]


Applying this to (H=G_k) gives exactly your statement: for each fixed (k\ge 3) there is a (c_k>0) with
[
\mathrm{ex}(n,G_k)\ll n^{3/2-c_k}.
]

Moreover, for the specific case (H_t=) the subdivision of (K_t) [[nomath]](which is your $G_t$)[[/nomath]], Conlon–Lee proved an explicit (though very small) exponent saving:
[
\mathrm{ex}(n,H_t)\le C, n^{3/2-6^{-t}}
\quad(\text{equivalently }3/2-1/6^t).
]


And Janzer later improved this substantially to a **polynomial-in-$t$** saving:
[
\mathrm{ex}(n,H_t)\le C' ,n^{3/2-\frac{1}{4t-6}}.
]
So for your graph (G_k), you can take for instance (c_k=\frac{1}{4k-6}). 
