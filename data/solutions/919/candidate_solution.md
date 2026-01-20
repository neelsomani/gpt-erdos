This is (essentially verbatim) **Erdős’ problem #919**, and as far as I can verify it is **still open**. ([Erdős Problems][1])

## What is known

### The ω₁² precedent (Erdős–Hajnal)

Erdős and Hajnal gave a graph on a vertex set of order type (\omega_1^2) which is **uncountably chromatic**, but every subgraph whose vertex set has **smaller order type** is **countably chromatic**.

One convenient formulation (in ordinal-coded form) is:

* Vertex set
  [
  V=\bigcup_{\alpha\in\omega_1}V_\alpha,\qquad
  V_\alpha=[,\omega_1\cdot\alpha+\alpha,\ \omega_1\cdot(\alpha+1),)
  ]
* Edge relation: for vertices (\omega_1\cdot\alpha+\beta) and (\omega_1\cdot\alpha'+\beta'),
  [
  {\omega_1\cdot\alpha+\beta,\ \omega_1\cdot\alpha'+\beta'}\in E
  \iff (\alpha<\alpha'\ \wedge\ \beta>\beta').
  ]
  This graph is uncountably chromatic, and **every set of order type (\omega_1)** induces a **countably chromatic** subgraph [[nomath]](and hence, by a simple decomposition argument, every set of order type $<\omega_1^2$ does as well)[[/nomath]]. 

*[[nomath]](This is equivalent to the “$\beta_1<\beta_2$” version you may have seen after reversing the order of the second coordinate; the phenomenon is the same.)[[/nomath]]* ([Erdős Problems][1])

### The straightforward ω₂² analogue only gives “≤ ℵ₁ on smaller type”

There is an analogous construction on (\omega_2^2) [[nomath]](replace $\omega_1$ by $\omega_2$ in the definition above)[[/nomath]] that produces a graph with

* (\chi(G)=\aleph_2), but
* every subgraph on a vertex set of **strictly smaller order type** has (\chi\le \aleph_1),

not (\le\aleph_0). ([Erdős Problems][1])

This is exactly the “gap” your question is asking to close: can one push the “(\le\aleph_1)” down to “(\le\aleph_0)”?

## Your two questions

### 1) (\chi(G)=\aleph_2) on (\omega_2^2) with all smaller-type subgraphs countably chromatic

**Open.** ([Erdős Problems][1])

The known (\omega_2^2) analogue only guarantees (\le\aleph_1) on smaller type, and it is not known (in ZFC, and as far as I can tell not even consistently in either direction in the public literature) whether one can force the smaller-type bound all the way down to (\aleph_0). ([Erdős Problems][1])

### 2) Same “smaller type ⇒ ≤ ℵ₀”, but only (\chi(G)=\aleph_1)

Also **open** as stated in the same problem. ([Erdős Problems][1])

It’s not a trivial weakening: the small-subgraph requirement already rules out the obvious ways of getting (\aleph_1)-chromaticity [[nomath]](e.g. you cannot simply “hide” an $\omega_1^2$-type Erdős–Hajnal example inside $\omega_2^2$, because that would give a smaller-type subgraph with uncountable chromatic number)[[/nomath]].

## A useful structural observation (why ω₁² behaves “easier” than ω₂²)

In the (\omega_1^2) case, it essentially suffices to control subgraphs on sets of order type (\omega_1), because any (\alpha<\omega_1^2) can be written (\alpha=\omega_1\cdot\xi+\beta) with (\xi<\omega_1) **countable**, so a set of type (\alpha) breaks into **countably many** (\omega_1)-type “chunks”. A countable union of countably colorable induced subgraphs is still countably colorable.

For (\omega_2^2), the analogous decomposition of (\alpha<\omega_2^2) may require (\omega_1)-many chunks [[nomath]](since $\xi<\omega_2$ can have size $\omega_1$)[[/nomath]], which is exactly why the direct analogue naturally gives a (\le\aleph_1) bound on smaller type rather than (\le\aleph_0). ([Erdős Problems][1])

So, informally: to get “(\le\aleph_0) for all smaller types” at (\omega_2^2), you’d need a mechanism that stays countably colorable even after taking (\omega_1)-many successive pieces—something substantially stronger than what works at (\omega_1^2).

---

If you tell me which exact convention you’re using for (\omega_2^2) [[nomath]](ordinal product $\omega_2\cdot\omega_2$ vs. Cartesian square $\omega_2\times\omega_2$)[[/nomath]], I can rewrite the known Erdős–Hajnal-style construction and the “(\le\aleph_1)” argument in your preferred coordinates.

[1]: https://www.erdosproblems.com/forum/thread/919 "https://www.erdosproblems.com/forum/thread/919"
