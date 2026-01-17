No.

A very small counterexample is
[
\mathcal F={K_{1,2},,2K_2},
]
where (K_{1,2}) is a “cherry” (two edges sharing a vertex) and (2K_2) is a matching of two disjoint edges.

**Step 1: (\mathrm{ex}(n;\mathcal F)=1).**
Any graph with at least two edges has either

* two edges sharing a vertex (\Rightarrow) it contains (K_{1,2}), or
* two vertex-disjoint edges (\Rightarrow) it contains (2K_2).

So an (\mathcal F)-free graph can have at most one edge, hence (\mathrm{ex}(n;\mathcal F)=1). 

**Step 2: each single forbidden graph still allows (\Theta(n)) edges.**

* If you only forbid (K_{1,2}), then no vertex can have degree (\ge 2), so the graph is a matching and
  [
  \mathrm{ex}(n;K_{1,2})=\left\lfloor\frac n2\right\rfloor.
  ]
* If you only forbid (2K_2), then the graph has matching number $1$, and for $n$ large the star (K_{1,n-1}) is allowed, giving
  [
  \mathrm{ex}(n;2K_2)\ge n-1,
  ]
  so (\mathrm{ex}(n;2K_2)=\Theta(n)). 

Therefore, for every (G\in\mathcal F) we have (\mathrm{ex}(n;G)=\Theta(n)) but (\mathrm{ex}(n;\mathcal F)=1), so
[
\frac{\mathrm{ex}(n;G)}{\mathrm{ex}(n;\mathcal F)}\to\infty,
]
and there is no constant [[nomath]](depending only on $\mathcal F$)[[/nomath]] making (\mathrm{ex}(n;G)\ll_{\mathcal F}\mathrm{ex}(n;\mathcal F)).

This question is basically the Erdős–Simonovits “compactness conjecture” as often stated; the example above is a known obstruction when (\mathcal F) is allowed to contain forests. 
