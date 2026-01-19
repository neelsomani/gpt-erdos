No.

There are **consecutive powerful (squarefull) numbers where neither term is a square**. The smallest “Type II” example (in Golomb’s terminology) is
[
12167 = 23^3,\qquad 12168 = 2^3\cdot 3^2\cdot 13^2,
]
and **Walker proved there are infinitely many such pairs** by showing that
[
7^3x^2 = 3^3y^2 + 1
]
has infinitely many integer solutions, producing infinitely many consecutive powerful pairs with neither term a square. ([Erdős Problems][1])

That said, there is an important nuance about “Pell”:

* If by “Pell equation” you mean the **classical** form (X^2 - DY^2 = 1), then the resulting consecutive powerful pairs always have a square term (X^2). Your “in other words” interpretation (“must one be a square?”) matches this classical setup, and the answer is **no** by the examples above. ([Erdős Problems][1])

* If instead you allow the **generalized Brahmagupta–Pell equation**
  [
  dX^2 - bY^2 = 1\qquad (b,d\ \text{squarefree}),
  ]
  then in fact **every** pair of consecutive powerful numbers arises from such an equation: write
  [
  n=a^2b^3,\quad n+1=c^2d^3\quad (b,d\ \text{squarefree}),
  ]
  and set (X=cd,\ Y=ab). Then (dX^2-bY^2=1). 
  This does *not* force a square term, because (dX^2) and (bY^2) can both be “cube times square”.

So: **not every pair has a square term**, but **every pair can be encoded as a generalized Pell/BP norm equation** with varying coefficients. 

---

## How many such (n\le x) can there be?

Let
[
S(x)=|\\{n\le x:\ n\ \text{and}\ n+1\ \text{are powerful}\\}|.
]

Erdős conjectured that there is a constant (A>0) such that
[
S(x) \ll (\log x)^A,
]
i.e. the quantity is **polylogarithmically bounded**. This is often referred to as (a form of) the **Erdős conjecture on consecutive squarefull numbers** and it remains **open**. 

### Heuristics and a necessary lower bound

A standard heuristic is: [[nomath]](\Pr$n\text{ squarefull}$\approx n^{-1/2})[[/nomath]], so [[nomath]](\Pr$n,n+1\text{ both}$\approx n^{-1})[[/nomath]], and summing (\sum_{n\le x}1/n) suggests $S(x)$ should be about (\asymp \log x). 

Also, $S(x)$ cannot be smaller than a constant multiple of (\log x), because classical Pell families already give (\gg \log x) examples up to $x$. 
So any bound of the form ((\log x)^{O(1)}) would have to have exponent at least $1$.

### Best known upper bounds (unconditional)

The known unconditional bounds are much weaker than polylog. For example:

* Chan proved [[nomath]](for general shift $\ell$)[[/nomath]] an upper bound
  [
  N(x;\ell)\ll d_3(\ell),x^{2/5}(\log x)^2,
  ]
  and for fixed (\ell) an improvement
  [
  N(x;\ell)\ll_\ell x^{7/19}\log x,
  ]
  where (N(x;\ell)=|\\{n\le x: n,n+\ell\ \text{squarefull}\\}|). ([Cambridge University Press & Assessment][2])

* For the consecutive case (\ell=1), Reuss proved the currently best published exponent I’m aware of:
  [
  S(x)=N(x;1)\ll_\varepsilon x^{29/100+\varepsilon}.
  ]


These are far from any ((\log x)^A) bound.

### Conditional bounds

Assuming the **abc conjecture**, one can prove a very strong “subpolynomial” upper bound:
[
N(x;\ell)\ll_{\varepsilon,\ell} x^\varepsilon\quad \text{for every }\varepsilon>0,
]
but this still does not directly give a polylog bound. ([Cambridge University Press & Assessment][2])

---

## Bottom line

* “Must one of (n,n+1) be a square?” **No.** There are explicit counterexamples (e.g. (23^3, 2^3\cdot 3^2\cdot 13^2)), and in fact **infinitely many** such pairs are known via Walker. ([Erdős Problems][1])

* “Is (|\\{n\le x:\ n,n+1\ \text{powerful}\\}|) bounded by ((\log x)^{O(1)})?” This is **conjectured by Erdős** but **open**. The best unconditional upper bounds are of the form (x^\theta) with (\theta<1/2) [[nomath]](notably $29/100+\varepsilon$)[[/nomath]], while there is a **lower bound (\gg \log x)** coming from Pell-type families. 

[1]: https://www.erdosproblems.com/365 "
  
    Erdős Problem #365
  
"
[2]: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/C4AA9EF0768E23BB5A215C22393BFD69/S144678871200016Xa.pdf/twin_squareful_numbers.pdf "TWIN SQUAREFUL NUMBERS"
