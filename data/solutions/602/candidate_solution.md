Yes.

Let $I$ be the index set and put (X=\bigcup_{i\in I}A_i).  Fix a well-ordering (I={i_\alpha:\alpha<\kappa}) (Choice).

### Key lemma

Suppose (c:X\to{0,1}) is a 2-coloring and (A_i) is monochromatic under $c$. Pick any (x\in A_i) and define a new coloring (c') by flipping $x$’s color and leaving all other points unchanged:
[
c'(x)=1-c(x),\qquad c'(y)=c(y)\ (y\neq x).
]
Then **no other** (A_j) ((j\neq i)) becomes monochromatic under (c').

**Proof.** If some (A_j) ((j\neq i)) were monochromatic under (c'), then (x\in A_j) [[nomath]](since only $x$ changed)[[/nomath]]. Also (A_j) cannot be monochromatic in color $c(x)$, because (c'(x)=1-c(x)). Hence (A_j) would have to be monochromatic in color (1-c(x)) under (c'), which means that under the old coloring $c$,

* $x$ had color $c(x)$, and
* every element of (A_j\setminus{x}) had color (1-c(x)).

But in (A_i) every element has color $c(x)$ [[nomath]](since $A_i$ was monochromatic)[[/nomath]]. Therefore, if there were any (y\in(A_i\cap A_j)\setminus{x}), then $y$ would simultaneously have color $c(x)$ [[nomath]](because $y\in A_i$)[[/nomath]] and (1-c(x)) [[nomath]](because $y\in A_j\setminus{x}$)[[/nomath]], impossible. So necessarily
[
A_i\cap A_j={x},
]
i.e. $|A_i\cap A_j|=1$, contradicting the hypothesis. ∎

So: flipping a point in a monochromatic (A_i) “repairs” (A_i) and does not break any other set, exactly because singleton intersections are forbidden.

### Construction of the coloring

We build a sequence of total colorings ((c_\alpha)_{\alpha\le\kappa}) by transfinite recursion.

* Start with the constant coloring (c_0(x)=0) for all (x\in X).
* Successor step: given (c_\alpha), look at (A_{i_\alpha}).

  * If (A_{i_\alpha}) is not monochromatic under (c_\alpha), set (c_{\alpha+1}=c_\alpha).
  * If (A_{i_\alpha}) is monochromatic under (c_\alpha), choose any (x_\alpha\in A_{i_\alpha}) and let (c_{\alpha+1}) be obtained from (c_\alpha) by flipping the color of (x_\alpha).
    By the lemma, this cannot make any previously non-monochromatic (A_j) become monochromatic.
* Limit step: if (\lambda) is a limit ordinal, define (c_\lambda(x)) to be the eventual value of (c_\alpha(x)) for (\alpha<\lambda). This is well-defined because each point changes color at most once: once a point $x$ is flipped, every set containing $x$ immediately has both colors, so by the lemma no set containing $x$ can ever again be monochromatic, hence $x$ will never be flipped again.

### Verification

By induction on (\alpha), after stage (\alpha) every set (A_{i_\beta}) with (\beta<\alpha) is non-monochromatic under (c_\alpha):

* At its own stage it is repaired if needed.
* Later stages never turn any other set monochromatic (by the lemma), so once repaired it stays repaired.

At the end we obtain (c_\kappa), and since every (i\in I) appears as some (i_\alpha), every (A_i) is non-monochromatic under (c_\kappa).

That (c_\kappa) is the desired 2-coloring of (\bigcup_i A_i).

*Remark.* In the proof, the “finite” part of “(|A_i\cap A_j|) is finite and (\neq 1)” is not used; the crucial hypothesis is just that **no pair intersects in exactly one point**.
