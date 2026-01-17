Write the statement as the (graph‑theoretic) partition relation
[
\alpha\ \to\ (\alpha,\ \text{infinite path})^{2},
]
meaning: **every** graph $G$ on vertex set (\alpha) has either

* an **infinite (one‑way) path** (v_0,v_1,\dots) with ({v_i,v_{i+1}}\in E(G)) for all $i$, or
* an **independent** set (I\subseteq \alpha) whose induced order has **order type (\alpha)**.

Here is what is known.

## Things that are settled in ZFC

### 1) Successor ordinals are excluded for a reason

If (\alpha=\beta+1), the statement fails: take the star with center (\beta) adjacent to every (\xi<\beta). This graph has no infinite path, and any independent set of order type (\beta+1) would have to include (\beta), which is impossible. [[nomath]](So restricting to **limit** $\alpha$ is essential.)[[/nomath]] 

### 2) Every infinite cardinal (\kappa) (as an initial ordinal) works

If (\alpha=\kappa) is an infinite cardinal (i.e. an initial ordinal), then ZFC proves the desired dichotomy: by the Erdős–Dushnik–Miller theorem (\kappa\to(\kappa,\omega)^2), every graph on (\kappa) has either an independent set of size (\kappa) [[nomath]](hence order type $\kappa$)[[/nomath]] or a countably infinite clique (hence an infinite path). ([Wikipedia][1])

So all (\omega, \omega_1, \omega_2,\dots) satisfy your property in ZFC.

## The nontrivial ordinal regime and the “critical bound”

The real subtlety is for **limit ordinals that are not cardinals** [[nomath]](e.g. $\omega_1\cdot 2$, $\omega_1^\omega$, etc.)[[/nomath]].

### 3) Erdős–Hajnal–Milner: a large ZFC interval of positive results

Erdős–Hajnal–Milner proved that for **every limit ordinal**
[
\alpha<\omega_1^{\omega+2}
]
one has
[
\alpha\ \to\ (\alpha,\ \text{infinite path})^{2}.
]
Equivalently: every graph on such an (\alpha) with **no infinite path** must contain an **independent set of order type (\alpha)**. ([Springer Link][2])

This includes all countable limit ordinals and a substantial collection of uncountable, non‑cardinal order types.

## Where set theory intervenes: independence and consistency results

### 4) The case (\alpha=\omega_1^{\omega+2}) is independent of ZFC

Milner records that at the exact bound (\operatorname{otp}(V)=\omega_1^{\omega+2}), the assertion becomes **independent of the axioms of set theory** (i.e. it can neither be proved nor refuted from ZFC). ([Springer Link][2])

### 5) Consistent failure under ♦ (Diamond)

Assuming Jensen’s Diamond Principle (which implies CH), Baumgartner–Larson constructed **counterexamples** for all (\alpha) with
[
\omega_1^{\omega+2}\le \alpha<\omega_2,
]
i.e. graphs on (\alpha) with **no infinite path** and **no independent set of order type (\alpha)**. ([ScienceDirect][3])

### 6) Consistent success under Martin’s Axiom

On the other hand, Larson proved that assuming **Martin’s Axiom**, the positive relation holds for **all limit (\alpha<2^{\aleph_0})** (so in such models there are **no counterexamples** below the continuum). ([Erdős Problems][4])

### 7) Many counterexamples under GCH at higher (\aleph_n)

Larson also showed that under **GCH**, for every integer (n>2) there is a **cofinal** set of ordinals (\alpha<\omega_n) such that the **negative** relation holds:
[
\alpha\ \not\to\ (\alpha,\ \text{infinite path})^{2}.
]
So, in GCH models, “failures” occur abundantly at higher levels. 

## Bottom line

* **Provably in ZFC:**

  * all **infinite cardinals** (\kappa) (as ordinals) satisfy the property; ([Wikipedia][1])
  * every **limit** (\alpha<\omega_1^{\omega+2}) satisfies the property. ([Springer Link][2])
* **Not decidable in ZFC:**

  * already at (\alpha=\omega_1^{\omega+2}) the statement is **independent**, and beyond that the full classification depends on additional axioms. ([Springer Link][2])

So the complete answer “for which limit ordinals (\alpha)?” is not currently known as a ZFC theorem; it is exactly the open Erdős–Hajnal–Milner problem (#601). ([Erdős Problems][4])

[1]: https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Dushnik%E2%80%93Miller_theorem?utm_source=chatgpt.com "Erdős–Dushnik–Miller theorem"
[2]: https://link.springer.com/chapter/10.1007/978-94-009-0517-7_14 "Ordered Graphs Without Infinite Paths | Springer Nature Link"
[3]: https://www.sciencedirect.com/science/article/pii/016800729090013R?utm_source=chatgpt.com "A diamond example of an ordinal graph with no infinite paths"
[4]: https://www.erdosproblems.com/forum/discuss/601 "

    Erdős Problem #601 - Discussion thread

"
