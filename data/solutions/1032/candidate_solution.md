As far as the literature currently records, this is **open**.

This is an old question of Erdős (Erdős Problems #1032). In particular, it is **not known** whether there are, for arbitrarily large $n$, **4-chromatic edge-critical** graphs $G$ on $n$ vertices with **linear** minimum degree (\delta(G)=\Omega(n)) [[nomath]](your $\gg n$)[[/nomath]]. ([Erdős Problems][1])

What *is* known is:

* For larger chromatic number, very large minimum degree is possible: **Dirac** exhibited a **6-chromatic** critical graph with (\delta(G) > n/2). ([Erdős Problems][1])
* For $k=4$, the best-known general lower bound is much smaller: **Simonovits** and **Toft** independently constructed **4-chromatic critical** graphs with
  [
  \delta(G)\ \gg\ n^{1/3}.
  ]
  ([Erdős Problems][1])
  [[nomath]](The same problem is also stated as open for $5$-chromatic critical graphs.)[[/nomath]] ([Erdős Problems][1])

A simple sanity check: even without criticality, a graph with (\chi(G)=4) has an independent set of size at least $n/4$, so some vertex has degree at most (n-n/4=3n/4); thus the best possible constant in a hypothetical $\delta(G)\ge cn$ would satisfy (c\le 3/4). But the real difficulty is whether **any** positive constant $c$ can be achieved under the **edge-critical** condition.

So the current state is: **no linear-minimum-degree construction is known for $4$-chromatic edge-critical graphs; the problem remains open; the best constructions give about (n^{1/3}).** ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/latex/1032 "https://www.erdosproblems.com/latex/1032"
