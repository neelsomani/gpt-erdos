No one knows in ZFC.

Let me rewrite your question in a standard way.
Saying that

* $G$ is the union of countably many triangle‑free graphs

means you can write (E(G)=\bigcup_{n\in\omega}E_n) where each ((V(G),E_n)) has no triangle. This is the same as saying:

* you can color the edges of $G$ with countably many colors so that **no triangle is monochromatic** (each color class is triangle‑free).

So your question is exactly:

> Is there a (K_4)-free graph $G$ such that **every** edge‑coloring (c:E(G)\to\omega) contains a monochromatic triangle?

This is an old problem of Erdős. Shelah lists it as Question 8.11 and says the answer is **consistently yes**, but that **it is not clear whether ZFC proves it**. ([arXiv][1])

A more recent survey by Reiher restates it (as Question 4.16) and again says it is open “provably in ZFC”, while noting that Shelah’s work gives consistency of a positive answer. 

One easy side remark: if such a graph exists, it cannot be countable, because a countable graph has only countably many edges, so you can color each edge with its own color and make every color class triangle‑free.

So the best current answer is:

* **Consistently (in some models of set theory): yes.**
* **Provable in ZFC: unknown / open.** ([arXiv][1])

[1]: https://arxiv.org/pdf/math/9906113 "arXiv:math/9906113v1  [math.LO]  16 Jun 1999"
