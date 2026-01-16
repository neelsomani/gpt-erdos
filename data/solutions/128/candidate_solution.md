No one knows the full answer yet.

This is a famous open problem of Erdős and Rousseau (often called the **“sparse half” conjecture**). It asks exactly whether your condition forces a triangle. ([Erdős Problems][1])

### Why this is the right constant (why “50” shows up)

There is a standard triangle-free construction that hits the value (n^2/50) right on the nose:

* Split the vertices into 5 equal parts (V_1,\dots,V_5) (each about (n/5)).
* Put **all** edges between (V_i) and (V_{i+1}) (indices mod 5), and no other edges.

This is a “blow-up” of the 5-cycle (C_5), so it has **no triangles**.

Now take the set
[
S ;=; V_1 \cup V_3 \cup (\text{half of }V_5),
]
so (|S| = n/5+n/5+n/10 = n/2).
Inside (S), the only edges come from the pair ((V_5,V_1)), giving
[
e(G[S]) ;=; (n/10)(n/5) ;=; n^2/50.
]
So you cannot hope to replace (n^2/50) by any smaller bound in the “triangle-free implies there is a sparse half” direction. ([Erdős Problems][1])

Your question is whether **strictly more** than this, in every half-sized induced subgraph, forces a triangle. That is exactly the open conjecture. ([Erdős Problems][1])

### What *is* known (partial results)

People can prove the same kind of statement with a weaker constant (meaning they require more edges in each half to force a triangle), or under extra assumptions.

Some highlights:

* Erdős–Faudree–Rousseau–Schelp proved it if (n^2/50) is replaced by the larger threshold (n^2/16). ([Erdős Problems][1])
* Razborov proved that every triangle-free graph has a half-sized induced subgraph with at most (\frac{27}{1024}n^2 \approx 0.02637n^2) edges. So if every half has **more** than (\frac{27}{1024}n^2) edges, then a triangle is forced. ([arXiv][2])
* The conjectured (1/50) bound is also proved for several special families (for example, graphs homomorphic to Andrásfai graphs; and it holds under certain minimum-degree conditions). ([arXiv][3])
* There are also results proving it for “dense enough” triangle-free graphs (extra assumptions on minimum/average degree). ([arXiv][4])

### Bottom line

As of now, the statement with the exact threshold (n^2/50) is **open**: it is not known whether your condition must force a triangle. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/128 "
  
    Erdős Problem #128
  
"
[2]: https://arxiv.org/abs/2104.09406 "[2104.09406] More about sparse halves in triangle-free graphs"
[3]: https://arxiv.org/abs/1609.05712 "[1609.05712] On the local density problem for graphs of given odd-girth"
[4]: https://arxiv.org/abs/1311.5818 "[1311.5818] Sparse halves in dense triangle-free graphs"
