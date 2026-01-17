Let (A\subseteq \mathbb N) (positive integers). Write

* (jA:={a_1+\cdots+a_j:\ a_i\in A}) (repetitions allowed),
* (j\times A:={a_1+\cdots+a_j:\ a_i\in A\ \text{pairwise distinct}}) [[nomath]](restricted/distinct sums; many authors write $j\wedge A$)[[/nomath]].

Say (S\sim\mathbb N) if $S$ contains all but finitely many positive integers.

**(Ordinary) order.** $A$ is an *asymptotic basis of order* $h$ if
[
\bigcup_{j=1}^h jA \ \sim\ \mathbb N,
]
and $h$ is minimal with that property.

**Restricted order.** The *restricted order* (\operatorname{ord}*R(A)) is the least $t$ (if it exists) such that
[
\bigcup*{j=1}^t (j\times A)\ \sim\ \mathbb N,
]
i.e. every sufficiently large integer is a sum of (\le t) **distinct** elements of $A$. ([ScienceDirect][1])

A couple of immediate (but useful) observations:

* If (\operatorname{ord}_R(A)) exists, then (\operatorname{ord}(A)\le \operatorname{ord}_R(A)), hence
  [
  \operatorname{ord}_R(A)\ge \operatorname{ord}(A),
  ]
  because a representation by distinct elements is in particular a representation allowing repetition.
* “(\operatorname{ord}_R(A)) exists” is exactly the same as saying “$A$ is a restricted asymptotic basis of some finite order” (just unpacking the definitions).

With that setup, here is what is currently known (and what remains open).

---

## 1) When does the restricted order exist?

### Complete answers in small orders

* **Order (1):** If (\operatorname{ord}(A)=1), then (A) is cofinite, so (\operatorname{ord}_R(A)=1) (trivial).
* **Order (2):** If (\operatorname{ord}(A)=2), then the restricted order **always exists** and satisfies
  [
  2\ \le\ \operatorname{ord}_R(A)\ \le\ 4.
  ]
  This is due to Kelly (1957) and sharpened/extended by Hennecart (2005); Hennecart also constructs an order‑2 basis with restricted order $4$. ([Erdős Problems][2])

So, for (\operatorname{ord}(A)=2), the necessary and sufficient condition for existence is simply: *$A$ is an asymptotic basis of order 2.*

### For order (\boldsymbol{h\ge 3}), existence can fail

Bateman observed a very simple obstruction: for any (h\ge 3), the set
[
A={1}\ \cup\ {x>0:\ h\mid x}
]
is an asymptotic basis of order $h$, **but has no restricted order at all**, because any sum of **distinct** elements uses at most one “$1$” and the rest are multiples of $h$, so you can only hit residues $0$ and (1\pmod h), never (2,\dots,h-1). ([Erdős Problems][2])

So for (\operatorname{ord}(A)\ge 3), there is **no** “purely order‑theoretic” criterion: being a basis of order $h$ does *not* force the restricted order to exist.

### What is known in general?

Beyond the (h=2) case, **a clean necessary-and-sufficient structural characterization is not currently known**; this is essentially Erdős–Graham problem #338 as recorded in the literature. ([Erdős Problems][2])

That said, there are **necessary conditions** that are easy to state and often useful:

* **No modular obstruction (in every modulus).** If (\operatorname{ord}_R(A)=t) exists, then for every modulus (m), every residue class mod (m) must be representable as a sum of (\le t) *distinct* residues from (A\pmod m). Otherwise, taking large integers in the missing residue class gives a contradiction. [[nomath]](Bateman’s example fails exactly this condition for $m=h$.)[[/nomath]]

But turning such modular conditions into a full characterization for (\mathbb N) is exactly where the open difficulty lies.

---

## 2) Can (\operatorname{ord}_R(A)) be bounded in terms of (\operatorname{ord}(A))?

### Order (2): yes, uniformly

As noted above, if (\operatorname{ord}(A)=2), then (\operatorname{ord}_R(A)\le 4) for **every** such basis. ([Springer][3])

### Orders (\boldsymbol{h\ge 3}): open in general, and any bound must be large

Because some order‑$h$ bases have **no** restricted order at all (Bateman’s example), the only sensible version of the question is:

> Among those $A$ with (\operatorname{ord}(A)=h) *and* (\operatorname{ord}_R(A)<\infty), is (\operatorname{ord}_R(A)) bounded above by a function of $h$?

This is **open** for (h\ge 3) (again part of #338). ([Erdős Problems][2])

What we *do* know is that if such a universal bound $f(h)$ exists, it cannot be small. Hegyvári–Hennecart–Plagne show that for every (k\ge 2) there exists a basis of order $k$ whose restricted order is at least
[
2^{k-2}+k-1.
]
So any putative $f(k)$ must grow at least exponentially. ([Erdős Problems][2])

---

## 3) When is the restricted order equal to the (ordinary) order?

First, the taut but important point:

* Since (\operatorname{ord}_R(A)\ge \operatorname{ord}(A)) whenever (\operatorname{ord}_R(A)) exists, equality (\operatorname{ord}*R(A)=\operatorname{ord}(A)=h) means precisely that **every sufficiently large integer is a sum of at most $h$ *distinct* elements of $A$**, i.e. $\bigcup*{j\le h} (j\times A)\sim \mathbb N$.

A general “if and only if” structural characterization of this equality [[nomath]](for arbitrary $h$)[[/nomath]] is **not known** at present; it’s part of the same circle of open questions. ([Erdős Problems][2])

What *is* known are representative examples and some sufficient conditions in special cases:

* **Equality can hold:** the triangular numbers form an asymptotic basis of order $3$ and also a restricted basis of order $3$ (so (\operatorname{ord}_R=\operatorname{ord}=3)). ([Erdős Problems][2])
* **Equality can fail:** the squares have ordinary order $4$ but restricted order $5$. ([Erdős Problems][2])
* **Order $2$ special information:** there are order‑2 bases with (\operatorname{ord}_R=4) (Hennecart) so equality need not hold. ([Springer][3])

  On the other hand, Chen–Yu (2023) give a strong **sufficient condition** for equality in the order‑2 case: if $A$ has lower asymptotic density (>1/2), then the restricted order is $2$ [[nomath]](so for an order‑2 basis this forces $\operatorname{ord}_R=\operatorname{ord}=2$)[[/nomath]], and they show the threshold $1/2$ is optimal. ([ScienceDirect][1])

---

## Bottom line summary

* **Existence:**

  * If (\operatorname{ord}(A)=2), then (\operatorname{ord}_R(A)) exists always and (\le 4). ([Springer][3])
  * For every (h\ge 3), there are order‑$h$ bases with **no** restricted order (Bateman’s example). ([Erdős Problems][2])
  * A full general necessary-and-sufficient characterization for (h\ge 3) is currently **open**. ([Erdős Problems][2])

* **Bounding (\operatorname{ord}_R) in terms of (\operatorname{ord}):**

  * Yes for (h=2): (\operatorname{ord}_R\le 4). ([Springer][3])
  * For (h\ge 3), whether there is a universal bound among those bases where (\operatorname{ord}_R<\infty) is **open**, and any bound must be at least exponential in $h$ (Hegyvári–Hennecart–Plagne). ([Hegyvári][4])

* **Equality (\operatorname{ord}_R=\operatorname{ord}):**

  * No general characterization known; examples go both ways (triangular numbers vs squares). ([Erdős Problems][2])
  * In order $2$, strong sufficient conditions for (\operatorname{ord}_R=2) are known [[nomath]](e.g. lower density $>1/2$)[[/nomath]]. ([ScienceDirect][1])

If you tell me whether you’re thinking of (A\subseteq\mathbb N) with (0\in A) (common in some conventions) or strictly positive $A$, I can restate the key examples/definitions in exactly that normalization, but the substantive statements above are invariant under the usual “add $0$” bookkeeping.

[1]: https://www.sciencedirect.com/science/article/abs/pii/S0012365X23000742 "https://www.sciencedirect.com/science/article/abs/pii/S0012365X23000742"
[2]: https://www.erdosproblems.com/338 "https://www.erdosproblems.com/338"
[3]: https://link.springer.com/article/10.1007/s11139-005-0830-8 "https://link.springer.com/article/10.1007/s11139-005-0830-8"
[4]: https://hegyvari.web.elte.hu/artEB4.pdf "https://hegyvari.web.elte.hu/artEB4.pdf"
