As stated, this claim is **false**.

### Counterexample (Ramsey–Turán theory)

There are explicit constructions of **(K_5)-free** graphs on $N$ vertices with **quadratically many edges** but with **no linear-size triangle-free vertex set**.

Concretely, Liu–Reiher–Sharifzadeh–Staden construct [[nomath]](for arbitrarily large $n$)[[/nomath]] a graph $G$ with a partition (V(G)=W\cup Z), (|W|=|Z|=n), such that

* (\alpha_3(G)=o(n)), i.e. **every triangle-free vertex set has size $o(n)$**,
* $e(G[W])$, (e(G[Z])=o(n^2)), but
* (e(W,Z)=(\ell/p-o(1))n^2).

Taking $p=3$ and (\ell=1), they also guarantee $G$ is **(K_{p+\ell+1}=K_5)-free**. 

Now set (N:=|V(G)|=2n). Then
[
e(G) = e(W,Z)+o(n^2)=\\(\tfrac13-o(1)\\)n^2
=\\(\tfrac1{12}-o(1)\\)N^2.
]
But (\alpha_3(G)=o(n)=o(N)), so $G$ has **no** triangle-free vertex subset of size $cN$ for any fixed (c>0) [[nomath]](for large enough $N$)[[/nomath]].

Therefore, for **any fixed** (\delta<\tfrac{1}{12}), these graphs satisfy (e(G)\ge \delta N^2) for all large $N$, yet still **do not** contain a triangle-free set of (\gg_\delta N) vertices.

This is tied to their determination (after decades of work) of the Ramsey–Turán density (\varrho_3(5)=1/6), which corresponds to edge count (\sim \frac16\binom{N}{2}\sim \frac1{12}N^2) in the (K_5)-free, (\alpha_3=o(N)) regime. 

### What *is* true (a corrected version)

A correct qualitative replacement is:

> If $G$ is (K_5)-free and (e(G)\ge \bigl(\tfrac{1}{12}+\varepsilon\bigr)n^2), then $G$ must contain a triangle-free vertex set of size (\Omega_\varepsilon(n)).

Informally: **above the $1/12$ edge-density threshold**, a linear-size triangle-free set is forced; **below** it, counterexamples exist.

If you tell me whether you intended a hypothesis like (e(G)\ge (1/12+\delta)n^2) [[nomath]](or $e(G)\ge (1/6+\delta)\binom{n}{2}$)[[/nomath]], I can write a clean proof of the corrected statement in the style you want (e.g., via the Ramsey–Turán extremal function / density argument).
