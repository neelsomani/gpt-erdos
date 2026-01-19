Let $G$ be an $n$-vertex graph in which **every** set of $7$ vertices spans a triangle. Define
[
h(n):=\min{\omega(G): |V(G)|=n,\ \text{every 7-set spans a }K_3}.
]

A useful reformulation is via the complement (H=\overline G). A triangle in $G$ is an **independent triple** in $H$, so the condition becomes:

* **every 7 vertices of $H$ contain an independent set of size 3**, i.e. (\alpha_7(H)\ge 3) in the “local independence” notation of Bucić–Sudakov, and
* (\omega(G)=\alpha(H)).

So $h(n)$ is equivalently the minimum possible (\alpha(H)) over $n$-vertex graphs $H$ with (\alpha_7(H)\ge 3). ([Springer][1])

## Best known bounds (as of 2026)

### Upper bound: (h(n)\ll n^{1/2}) [[nomath]](in fact $O(\sqrt{n\log n})$)[[/nomath]]

Take $H$ to be a **triangle-free** $n$-vertex graph with very small independence number. Triangle-free implies that every 7-vertex induced subgraph is triangle-free, hence [[nomath]](by $R(3,3)=6$)[[/nomath]] it contains an independent triple, so (\alpha_7(H)\ge 3); thus (G=\overline H) satisfies your “every 7 vertices contain a triangle” property, and (\omega(G)=\alpha(H)).

Kim (1995) constructs triangle-free graphs $H$ with
[
\alpha(H)\le C\sqrt{n\log n},
]
indeed Theorem 1.1 gives (\alpha(H)\le 9\sqrt{n\log n}) for all large $n$. ([People at Texas A&M][2])
Therefore
[
h(n)\le O(\sqrt{n\log n})\ll n^{1/2+o(1)}.
]

This matches the classical Erdős–Hajnal upper bound (h(n)\ll n^{1/2}). ([Erdős Problems][3])

### Lower bounds: $h(n)$ is **polynomially larger** than (n^{1/3})

Erdős–Hajnal already proved
[
n^{1/3}\ll h(n)\ll n^{1/2}.
]
([Erdős Problems][3])

More recently, Bucić and Sudakov proved the stronger bound
[
h(n)\ge n^{5/12-o(1)}.
]
([Erdős Problems][3])

So the current best “exponent window” is
[
n^{5/12-o(1)}\ \le\ h(n)\ \le\ O(\sqrt{n\log n}),
]
i.e. roughly (n^{0.416\ldots}) to (n^{0.5}) up to subpolynomial factors.

## Answer to your “(c_1,c_2)” question

* **Yes for (c_1):** Bucić–Sudakov gives (h(n)\ge n^{5/12-o(1)}), so you can take any fixed (c_1<\frac{1}{12}) [[nomath]](for all sufficiently large $n$)[[/nomath]]. ([Erdős Problems][3])
* **For (c_2): currently open.** The best known constructions still only give $h(n)$ about (n^{1/2}) up to logs (via triangle-free complements as above), and no polynomial improvement to (n^{1/2-c_2}) is known. In fact, Bucić–Sudakov explicitly pose the question whether one always has
  [
  h(n)=\alpha(H)\ge n^{1/2-o(1)}
  ]
  under the local condition (\alpha_7(H)\ge 3), which (if true) would mean **no such (c_2) exists**. ([Springer][1])

So, summarizing the state of the art:

[
\boxed{,n^{5/12-o(1)}\ \le\ h(n)\ \le\ O(\sqrt{n\log n}),}
]

and the **lower** exponent has been pushed above $1/3$ [[nomath]](so $c_1>0$ exists)[[/nomath]], while whether one can push the **upper** exponent below $1/2$ [[nomath]](i.e., whether $c_2>0$ exists)[[/nomath]] remains open.

[1]: https://link.springer.com/article/10.1007/s00493-023-00023-w "Large Independent Sets from Local Considerations | Combinatorica | Springer Nature Link"
[2]: https://people.tamu.edu/~huafei-yan/Teaching/Math689/ramsey5.pdf "C:\\"
[3]: https://www.erdosproblems.com/813 "Erdős Problem #813"
