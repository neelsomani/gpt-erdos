What you’re asking is exactly the **Erdős–Hajnal conjecture**.

* **Conjecture (Erdős–Hajnal, 1977).** For every fixed graph $H$ there exists a constant (c(H)>0) such that every $n$-vertex graph $G$ with **no induced** copy of $H$ contains either a clique or an independent set of size at least (n^{c(H)}). ([labri.fr][1])

### Status

This is **still open in general** (i.e., not known for every graph $H$). Even for families like *paths*, it’s not known in full generality (though there has been significant progress). ([labri.fr][1])

### Best general bound known for arbitrary $H$

Although the polynomial bound (n^{c(H)}) is unproven in general, there are unconditional “Ramsey-type” guarantees that grow faster than any power of (\log n). The classical Erdős–Hajnal bound was
[
\exp!\big(c\sqrt{\log n}\big),
]
and this was improved (for **all** $H$) to
[
\exp!\big(c\sqrt{\log n,\log\log n}\big)
]
[[nomath]](or equivalently $2^{c\sqrt{\log n,\log\log n}}$)[[/nomath]]. ([arXiv][2])

This is still **subpolynomial** in $n$ [[nomath]](it’s $n^{o(1)}$)[[/nomath]], so it falls short of the conjectured (n^{c(H)}).

### Some important verified cases

The conjecture *is* known for many specific forbidden induced graphs $H$. For example:

* (H=C_5) (the 5-cycle): proved by Chudnovsky–Scott–Seymour–Spirkl. ([arXiv][3])
* (H=P_5) (the 5-vertex path): proved by Nguyen–Scott–Seymour, and this “completes” the verification for **all graphs on 5 vertices**. ([arXiv][4])

And along one major frontier:

* For **paths** (H=P_k) in general, the full conjecture is not known for longer paths, but there is a strong “nearly Erdős–Hajnal” bound: for every fixed path $H$, every $H$-free $n$-vertex graph has a clique or independent set of size at least (2^{(\log n)^{1-o(1)}}). ([arXiv][5])

So: **the statement is believed to be true for every $H$, but remains unproved in general**—with the best known general bound currently of the form (2^{c\sqrt{\log n\log\log n}}), and full polynomial bounds known for many special $H$ [[nomath]](including all $H$ with $\le 5$ vertices)[[/nomath]]. ([arXiv][2])

[1]: https://www.labri.fr/agenda/gtgo-recent-progress-erdos-hajnal-conjecture-paul-seymour "[gt.go] - \"Recent progress on the Erdos-Hajnal conjecture\" by Paul Seymour - LaBRI"
[2]: https://arxiv.org/abs/2301.10147 "[2301.10147] Induced subgraph density. I. A loglog step towards Erdos-Hajnal"
[3]: https://arxiv.org/abs/2102.04994 "[2102.04994] Erdos-Hajnal for graphs with no 5-hole"
[4]: https://arxiv.org/abs/2312.15333 "[2312.15333] Induced subgraph density. VII. The five-vertex path"
[5]: https://arxiv.org/abs/2307.15032 "[2307.15032] Induced subgraph density. V. All paths approach Erdos-Hajnal"
