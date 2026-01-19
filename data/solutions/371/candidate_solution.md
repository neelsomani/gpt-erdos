A quick (but important) clarification about what is currently known:

* The statement **with ordinary asymptotic (natural) density**
  $
  \lim_{x\to\infty}\frac1x|\\{n\le x: P(n)<P(n+1)\\}|=\tfrac12
  $
  is the classical **Erdős–Turán conjecture** and is **still open** as of the current literature. ([Erdős Problems][1])

* What *is* known (and can be proved) is that the set has **logarithmic density** $1/2$, and even that the “$1/2$” law holds for **unweighted averages at almost all scales**. 
  Also, assuming an Elliott–Halberstam–type conjecture for friable integers, the **natural density** statement follows. ([ScienceDirect][2])

So, below I’ll **prove the logarithmic density $1/2$** result [[nomath]](which is the strongest unconditional “density $1/2$” theorem currently available in full generality)[[/nomath]].

---

## 1) Logarithmic density and the goal

For a set (A\subset\mathbb N), the **logarithmic density** (if it exists) is
[
\delta(A):=\lim_{x\to\infty}\frac{1}{\log x}\sum_{\substack{n\le x\ n\in A}}\frac1n.
]

Let
$
A:={n\in\mathbb N:\ P(n)<P(n+1)}.
$
Note that (\gcd(n,n+1)=1), so (P(n)\neq P(n+1)) for all (n\ge 2). Thus [[nomath]](ignoring $n=1$, which does not affect densities)[[/nomath]], exactly one of (P(n)<P(n+1)) and (P(n)>P(n+1)) holds.

We will show:
[
\delta(A)=\tfrac12.
]

This is precisely Theorem 1.16 in Teräväinen (2018). 
I’ll explain the key argument (the last step is a clean symmetry computation).

---

## 2) Teräväinen’s “independence in logarithmic density” input

A central input is a logarithmic-density analogue of an Erdős–Pomerance independence conjecture: in logarithmic averages, the events “$n$ is (n^a)-smooth” and “$n+1$ is (n^b)-smooth” behave independently, with probabilities governed by the Dickman function (\rho). Concretely, Teräväinen proves:

For any (a,b\in(0,1)),
[
\delta\big({n:\ P(n)\le n^a, P(n+1)\le n^b}\big)
= \rho(1/a),\rho(1/b).
]
This is Theorem 1.14 of the paper. 

From this, by inclusion–exclusion and differentiation, Teräväinen derives an explicit **joint limiting law** (in logarithmic density) for the normalized variables
[
X_n:=\frac{\log P(n)}{\log n},\qquad Y_n:=\frac{\log P(n+1)}{\log n}.
]
Namely: for every “nice” (Riemann integrable) set (S\subset[0,1]^2),
[
\delta\big({n:\ (X_n,Y_n)\in S}\big)=\iint_S u(x)u(y),dx,dy,
]
where
$
u(x)=\frac{1}{x},\rho(\frac1x-1)\qquad (0<x<1).
$
[[nomath]](See equation $4.14$ and the discussion around Theorem 1.17 in the paper.)[[/nomath]] 

Interpretation: under logarithmic sampling, (X_n) and (Y_n) become **independent**, identically distributed with density $u$.

---

## 3) Conclude ( \delta(P(n)<P(n+1)) = 1/2) by symmetry

Now observe:
$
P(n)<P(n+1)\quad\Longleftrightarrow\quad \log P(n) < \log P(n+1).
$
In terms of (X_n,Y_n) (which are just log-normalizations), this is equivalent to (X_n<Y_n), up to the harmless normalization by (\log n). Teräväinen packages this directly as Theorem 1.17 with (\alpha=0), yielding
[
\delta(A)=\iint_{y\ge x} u(x)u(y),dx,dy.
]
[[nomath]](And because $P(n)\neq P(n+1)$ for $n\ge 2$, the diagonal $x=y$ is negligible.)[[/nomath]] 

But now the computation is purely symmetric:

* The function (u(x)u(y)) is symmetric in $(x,y)$.
* The square ([0,1]^2) splits into two congruent regions ({y>x}) and ({x>y}), plus the diagonal ({x=y}) of measure zero.

Hence
$
\iint_{y>x} u(x)u(y),dx,dy = |\iint_{x>y} u(x)u(y),dx,dy|
\frac12\iint_{[0,1]^2} u(x)u(y),dx,dy.
$

Finally,
[
\iint_{[0,1]^2} u(x)u(y),dx,dy
=\left(\int_0^1 u(x),dx\right)^2=1,
]
because $u$ is a probability density on $(0,1)$ [[nomath]](equivalently $\int_0^1 u= \rho(1)-\lim_{t\to\infty}\rho(t)=1-0=1$)[[/nomath]]. 

Therefore,
[
\delta(A)=\tfrac12.
]

This proves: **the set ({n:\ P(n)<P(n+1)}) has logarithmic density $1/2$**. 

---

## 4) If you meant ordinary asymptotic density

If by “density” you meant the **natural density** (\lim_{x\to\infty} |\\{n\le x:\cdots\\}|/x), that exact limit being $1/2$ remains **unproved unconditionally** (it is Erdős–Turán’s conjecture). ([Erdős Problems][1])

What is known in that direction includes:

* **Almost-all scales:** outside an exceptional set of $X$ of logarithmic density $0$, the unweighted average (\frac1X\sum_{n\le X} 1_{P(n)<P(n+1)}) tends to $1/2$. 
* **Conditional full asymptotic density $1/2$:** it follows from the Elliott–Halberstam conjecture for friable integers. ([ScienceDirect][2])

If you tell me what notion of density your course/text is using (natural vs logarithmic), I can tailor the presentation accordingly—but the argument above is the clean “$1/2$” proof that is currently fully established in the literature.

[1]: https://www.erdosproblems.com/371 "
  
    Erdős Problem #371
  
"
[2]: https://www.sciencedirect.com/science/article/pii/S0022314X21000196 "Three conjectures on P+(n) and P+(n + 1) hold under the Elliott-Halberstam conjecture for friable integers - ScienceDirect"
