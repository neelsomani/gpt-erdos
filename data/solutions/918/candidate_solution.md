Let me phrase your two requirements in the standard “incompactness for chromatic number” language.

A graph $G$ is **$(\aleph_0,\kappa)$-chromatic** if

* (\chi(G)=\kappa), and
* every subgraph (H\subseteq G) with (|V(H)|<|V(G)|) has (\chi(H)\le\aleph_0).

So your first question is exactly the statement $E(\aleph_0,\aleph_2)$: an $(\aleph_0,\aleph_2)$-chromatic graph of size (\aleph_2).
Your second question asks for a graph of size (\aleph_{\omega+1}) with (\chi(G)=\aleph_1) while all (\aleph_\omega)-sized subgraphs are countably chromatic [[nomath]](which in particular implies all $<\aleph_\omega$-sized subgraphs are countably chromatic too)[[/nomath]].

## 1) (\aleph_2) vertices, (\chi=\aleph_2), all (\aleph_1)-subgraphs countably chromatic

This is **independent of ZFC** (in the usual “relative to large cardinals” sense):

* **Consistently yes:** Baumgartner showed it is consistent with GCH that there exists an $(\aleph_0,\aleph_2)$-chromatic graph of size (\aleph_2). ([arXiv][1])
  Also, Shelah proved that in $V=L$ (hence GCH), for every regular non–weakly compact (\kappa) there is an $(\aleph_0,\kappa)$-chromatic graph of size (\kappa); in particular this gives one for (\kappa=\aleph_2). ([arXiv][1])

* **Consistently no:** Foreman–Laver proved (relative to a large cardinal hypothesis) that it is consistent with GCH that **no** $(\aleph_0,\aleph_2)$-chromatic graph of size (\aleph_2) exists. ([arXiv][1])

So ZFC alone cannot decide your first question.

## 2) (\aleph_{\omega+1}) vertices, (\chi=\aleph_1), all (\aleph_\omega)-subgraphs countably chromatic

This has a **consistent positive answer**, and in fact follows from a fairly standard square+CH-at-(\aleph_\omega) hypothesis.

Rinot proved (as summarized in Lambie-Hanson–Rinot) that if (\lambda) is an infinite cardinal with
[
2^\lambda=\lambda^+ \quad\text{and}\quad \square_\lambda
]
then for every infinite (\mu\le\lambda) there is an $(\aleph_0,\mu)$-chromatic graph of size (\lambda^+). ([arXiv][1])

Now take (\lambda=\aleph_\omega) and (\mu=\aleph_1) [[nomath]](indeed $\aleph_1\le\aleph_\omega$)[[/nomath]]. Under (2^{\aleph_\omega}=\aleph_{\omega+1}) and (\square_{\aleph_\omega}) [[nomath]](e.g. under GCH + square, which holds in $L$)[[/nomath]], you get a graph $G$ with

* (|V(G)|=\aleph_{\omega+1}),
* (\chi(G)=\aleph_1),
* and every subgraph of size (<\aleph_{\omega+1}) [[nomath]](hence in particular every subgraph on $\aleph_\omega$ vertices)[[/nomath]] is countably chromatic. ([arXiv][1])

### About “does ZFC prove this?” / “can it consistently fail?”

A strong *compactness* statement at (\aleph_{\omega+1}) would rule out such examples. Shelah proved (relative to large cardinals) that it is consistent with GCH that for each (1\le n<\omega), if an (\aleph_{\omega+1})-sized graph has all subgraphs of size (<\aleph_\omega) of chromatic number (\le\aleph_n), then the whole graph has chromatic number (\le\aleph_n). ([arXiv][1])
But the corresponding “$n=0$” version [[nomath]](with $\aleph_n=\aleph_0$)[[/nomath]] is explicitly noted as open in that source. ([arXiv][1])
So: you *can* build the graph in many natural models [[nomath]](e.g. $L$)[[/nomath]], but the full consistency picture for the “countable bound” compactness at (\aleph_{\omega+1}) is subtler.

If you want, I can also point you to the precise papers behind the bullet points (Baumgartner 1984; Foreman–Laver 1988; Rinot 2015; Shelah 1990/2013) and indicate exactly which hypotheses each construction uses.

[1]: https://arxiv.org/pdf/1708.06929 "https://arxiv.org/pdf/1708.06929"
