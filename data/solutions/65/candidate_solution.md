Yes.

Write (\mathcal C(G)={a_1<a_2<\cdots}) for the *set* of cycle lengths in (G), and let (m=|E(G)|=kn). Then the average degree is
[
d(G)=\frac{2m}{n}=2k.
]

### Lower bound (\sum 1/a_i \gg \log k)

Gyárfás–Komlós–Szemerédi (1984) proved that for a graph of average degree (d),
[
\sum_{\ell\in \mathcal C(G)}\frac1\ell = \Omega(\log d),
]
so in your notation (\sum_i \frac1{a_i}\gg \log k) since (d=2k). 

Moreover, Liu–Montgomery proved the asymptotically sharp form: if (G) has average degree (d\to\infty), then
[
\sum_{\ell\in \mathcal C(G)}\frac1\ell ;\ge;\Bigl(\tfrac12-o_d(1)\Bigr)\log d.
]


Translating (d=2k), this gives
[
\sum_i\frac1{a_i};\ge;\Bigl(\tfrac12-o_k(1)\Bigr)\log(2k)
=\Bigl(\tfrac12-o_k(1)\Bigr)\log k + O(1),
]
so not only is (\sum 1/a_i\gg \log k) true, but the best possible leading constant is (1/2) (as (k\to\infty)).

### Why the constant (1/2) is best possible

For the complete balanced bipartite graph (K_{t,t}) (average degree (d=t)), the cycle lengths are exactly
[
\mathcal C(K_{t,t})={4,6,8,\dots,2t},
]
so
[
\sum_{\ell\in\mathcal C(K_{t,t})}\frac1\ell
=\sum_{j=2}^{t}\frac1{2j}
=\frac12,(H_t-1)
=\Bigl(\tfrac12+o(1)\Bigr)\log t
=\Bigl(\tfrac12+o(1)\Bigr)\log d,
]
matching the lower bound up to (o(1)). This is exactly the comparison Liu–Montgomery make in their introduction. 

### Is the sum *minimised* by a complete bipartite graph?

* **Asymptotically (in terms of average degree):** the minimum possible value of (\sum_{\ell\in\mathcal C(G)}\frac1\ell) among graphs with average degree (d) is
  [
  \Bigl(\tfrac12+o(1)\Bigr)\log d,
  ]
  and complete balanced bipartite graphs achieve this, so they are *asymptotically extremal*.

* **Exactly for given (n) and (m=kn):** the sharper “structure” question “is the sum minimised when (G) is complete bipartite?” remains open as stated on the Erdős Problems site (they note the (\gg\log k) part is proved and “only the second question remains”). ([Erdős Problems][1])

A small caveat: for fixed (n), a complete bipartite graph has at most (\lfloor n^2/4\rfloor) edges (Turán), i.e. (k\le n/4). So for (k>n/4) the “complete bipartite minimiser” can’t literally apply (there is no bipartite graph with that many edges), and in that dense regime the sum is in any case much larger.

If you tell me whether you care about the **exact** minimiser for each ((n,m)) or only the **asymptotic** extremal behaviour as (k\to\infty), I can frame the remaining open part more precisely.

[1]: https://www.erdosproblems.com/65 "
  
    Erdős Problem #65
  
"
