No.

A simple counterexample uses only **bipartite forests**. Let

* (H_1 = K_{1,2}) [[nomath]](a 2-edge star, i.e. a path $P_3$)[[/nomath]], and
* (H_2 = 2K_2) (a matching of two disjoint edges), and set (\mathcal F={H_1,H_2}).

### Step 1: (\mathrm{ex}(n;\mathcal F)=1)

Any graph with at least **two** edges contains either

* two edges sharing a vertex, which gives a copy of (K_{1,2}), or
* two vertex-disjoint edges, which gives a copy of (2K_2).

So an (\mathcal F)-free graph can have **at most one edge**, hence
[
\mathrm{ex}(n;\mathcal F)=1 \qquad (n\ge 2).
]
This exact observation appears explicitly in Wigderson’s note. 

### Step 2: each bipartite member has (\Theta(n)) extremal number

* For (H_1=K_{1,2}): an (H_1)-free graph has maximum degree (\le 1), so it is a matching, hence
  [
  \mathrm{ex}(n;K_{1,2})=\left\lfloor \frac n2\right\rfloor = \Theta(n).
  ]
* For (H_2=2K_2): being (2K_2)-free means the matching number is (\le 1); the star (K_{1,n-1}) is (2K_2)-free and has $n-1$ edges, so
  [
  \mathrm{ex}(n;2K_2)=n-1=\Theta(n).
  ]
  (These are also noted in the same short proof sketch. )

### Conclusion

For every bipartite (G\in\mathcal F),
[
\frac{\mathrm{ex}(n;G)}{\mathrm{ex}(n;\mathcal F)} \asymp n \to \infty,
]
so there is **no** bipartite (G\in\mathcal F) with (\mathrm{ex}(n;G)\ll_{\mathcal F}\mathrm{ex}(n;\mathcal F)).

---

**Remark.** This counterexample is “trivial” in the sense that it exploits the presence of **forests**. A natural modified conjecture (suggested by Simonovits, as reported by Wigderson) is to **exclude families containing a forest**; with that extra assumption the question becomes genuinely nontrivial. 
