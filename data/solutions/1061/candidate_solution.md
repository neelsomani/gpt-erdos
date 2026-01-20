Short answer: **mostly open**.

More precisely:

* **Concrete / proved:**
  There is a **positive linear lower bound**. One can rigorously show
  [
  N(x)\ge c,x
  ]
  for some explicit (c>0) [[nomath]](for example $c=2/9$ from the family $(n,2n)$ with $(n,6)=1$)[[/nomath]].

* **Open:**
  It is **not known** whether
  [
  N(x)\sim c,x
  ]
  for any constant (c>0). In fact, it is not even known whether (N(x)/x) stays bounded.

* **Heuristic / numerical:**
  Computations strongly suggest **superlinear growth**, plausibly
  [
  N(x)\asymp \kappa,x\log x,
  ]
  but there is **no proof** of an (x\log x) asymptotic (or even a matching upper bound of that order).

So the current state is:

> **Linear lower bound: concrete.
> Exact order of growth [[nomath]](linear vs. $x\log x$, existence of an asymptotic)[[/nomath]]: open.**

If you want, I can sketch what a proof of (x\log x) would likely require, or explain why standard multiplicative-function techniques don’t yet seem to be enough.
