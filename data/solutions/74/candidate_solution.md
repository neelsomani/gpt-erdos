This is a well-known Erdős–Hajnal–Szemerédi problem, and in full generality it is **still open**. In particular, nobody knows whether you can do this for an *arbitrary* function (f(n)\to\infty) that grows very slowly. ([Erdős Problems][1])

What is known:

* **Yes for linear $f$.** Rödl (1982) proved that for every fixed (\varepsilon>0) there is a graph $G$ with chromatic number (\aleph_0) such that every $n$-vertex subgraph can be made bipartite by deleting at most (\varepsilon n) edges. So the answer is “yes” when $f(n)$ is (at least) a constant times $n$. ([Erdős Problems][1])

* **Open for much smaller $f$.** The problem is open even for (f(n)=\sqrt n). ([Erdős Problems][1])

A related side note (only if you care about uncountable chromatic number): for graphs with (\chi(G)=\aleph_1), one can prove you need to delete at least on the order of $n$ edges in some $n$-vertex subgraphs, and Erdős–Hajnal–Szemerédi also built examples with an upper bound around (n^{3/2}) for this “best possible deletion function” $h_G(n)$. ([Erdős Problems][2])

[1]: https://www.erdosproblems.com/latex/74 "
  
    Erdős Problems
  
"
[2]: https://www.erdosproblems.com/111 "
  
    Erdős Problem #111
  
"
