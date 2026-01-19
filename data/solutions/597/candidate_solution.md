Let me first unpack the notation the way it is usually meant in this part of partition calculus.

* (\omega_1^2) is the ordinal product (\omega_1\cdot\omega_1) [[nomath]](lexicographic order on $\omega_1\times\omega_1$)[[/nomath]].
* (\omega_1\omega) is (\omega_1\cdot\omega) [[nomath]](a countable concatenation of $\omega_1$-blocks)[[/nomath]].
* (\alpha\to(\beta,G)^2) (graph version) means: for every 2–coloring (c:[\alpha]^2\to{0,1}), either there is a set (H\subseteq\alpha) of order type (\beta) such that all pairs from $H$ have color $0$, **or** there is an embedding (f:V(G)\hookrightarrow \alpha) such that every edge ({u,v}\in E(G)) is sent to a pair colored $1$ [[nomath]](non-edges of $G$ may go to either color)[[/nomath]].

With that understood, here’s what is definitely known and what (as far as I can tell from accessible sources) remains unsettled.

## What is known

Even very nearby statements are independent of ZFC. In particular, Baumgartner–Hajnal showed that **CH implies**
[
\omega_1^2 \not\to (\omega_1\omega,4)^2,
]
i.e. there is (under CH) a 2–coloring of ([\omega_1^2]^2) with **no** $0$-homogeneous set of type (\omega_1\omega) and **no** $1$-homogeneous 4–set [[nomath]](no monochromatic $K_4$ in color 1)[[/nomath]]. ([Cambridge University Press & Assessment][1])

This already tells you that you cannot hope for a blanket ZFC theorem of the form “(\omega_1^2\to(\omega_1\omega,H)^2) for every fixed finite $H$”, because taking (H=K_4) fails in a model of ZFC (namely CH). ([Cambridge University Press & Assessment][1])

## Your specific question [[nomath]](graphs with no $K_4$ and no $K_{\aleph_0,\aleph_0}$)[[/nomath]]

Your hypothesis rules out exactly the two obstructions (K_4) and (K_{\aleph_0,\aleph_0}) **inside $G$**, not inside the coloring. The CH counterexample above rules out (K_4) in *one color* of the coloring, so it does not directly answer your question.

From what I can verify without access to the full paywalled text, I do **not** see a published ZFC resolution that settles

[
\omega_1^2 \to (\omega_1\omega, G)^2
\quad\text{for every }G\text{ on }\le\aleph_1\text{ with no }K_4\text{ and no }K_{\aleph_0,\aleph_0}.
]

This type of question is very much in the “Erdős–Hajnal problem list” ecosystem [[nomath]](and the 2025 update exists and discusses related $\omega_1^2$-partition phenomena, including the CH implication above)[[/nomath]]. ([Cambridge University Press & Assessment][2])
But I can’t honestly claim a definitive yes/no for the general $G$-statement on the basis of the sources I can currently access.

## What about finite $G$?

For *finite* $G$, the “no (K_{\aleph_0,\aleph_0})” condition is automatic, so you’re really asking about **finite (K_4)-free** graphs.

Here again, the CH counterexample for ((\omega_1\omega,4)^2) shows that if you *drop* “(K_4)-free” then the answer is negative [[nomath]](already for $G=K_4$)[[/nomath]]. ([Cambridge University Press & Assessment][1])
But for finite (K_4)-free graphs $G$, I do not have a reliable reference (from what I could access) that settles (\omega_1^2\to(\omega_1\omega,G)^2) in ZFC in either direction.

## A useful way to rephrase the difficulty

If you fix a coloring and let $B$ be the color–1 graph on (\omega_1^2), then the relation
[
\omega_1^2\to(\omega_1\omega,G)^2
]
is equivalent to:

> Every graph $B$ on (\omega_1^2) which contains **no** copy of $G$ must have an **independent** set of order type (\omega_1\omega).

So the “shape” requirement [[nomath]](order type $\omega_1\omega$, not just size $\aleph_1$)[[/nomath]] is what makes these questions much subtler than the cardinal partition relation (\aleph_1\to(\aleph_1,G)^2).

---

If you want, tell me which concrete finite (K_4)-free graph you care about most [[nomath]](e.g. $C_4$, $C_5$, a tree, etc.)[[/nomath]], and I can at least walk through what the CH counterexample does and does not rule out for that $G$, and what kind of additional structure (e.g. forcing axioms) is typically used to get positive results in this neighborhood.

[1]: https://www.cambridge.org/core/product/9FBE6099BE9441516445D0B95F4B1208 "https://www.cambridge.org/core/product/9FBE6099BE9441516445D0B95F4B1208"
[2]: https://www.cambridge.org/core/journals/bulletin-of-symbolic-logic/article/erdoshajnal-problem-list/9FBE6099BE9441516445D0B95F4B1208 "https://www.cambridge.org/core/journals/bulletin-of-symbolic-logic/article/erdoshajnal-problem-list/9FBE6099BE9441516445D0B95F4B1208"
