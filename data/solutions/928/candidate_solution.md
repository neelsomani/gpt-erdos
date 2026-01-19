Let
$
A_{\alpha,\beta}:={n\ge 1:\ P(n)<n^{\alpha}\ \text{and}\ P(n+1)<(n+1)^{\beta}},
\qquad \alpha,\beta\in(0,1),
$
and ask whether the **(natural) asymptotic density**
[
d(A_{\alpha,\beta})=\lim_{x\to\infty}\frac{1}{x}|\\{n\le x:\ n\in A_{\alpha,\beta}\\}|
]
exists.

As of the current literature, **this is open in general**: it is essentially the Erdős–Pomerance conjecture on the independence of smoothness of consecutive integers. ([Erdős Problems][1])

What *is* known is:

* **Conjectural value (independence prediction).** Erdős–Pomerance conjecture predicts that the asymptotic density exists and equals
  [
  d(A_{\alpha,\beta})\stackrel{?}{=} \rho(1/\alpha),\rho(1/\beta),
  ]
  where (\rho) is the Dickman function (the same function that governs the density of “power-smooth” integers). 

* **Unconditional: logarithmic density exists and equals the predicted product.** Teräväinen (2018) proved that the **logarithmic density**
  [
  \delta(A_{\alpha,\beta})=\lim_{x\to\infty}\frac{1}{\log x}\sum_{\substack{n\le x\ n\in A_{\alpha,\beta}}}\frac1n
  ]
  exists and satisfies
  [
  \delta(A_{\alpha,\beta})=\rho(1/\alpha),\rho(1/\beta).
  ]


* **Conditional: natural density exists under an Elliott–Halberstam hypothesis for friable integers.** Wang (2021) proved that assuming the **Elliott–Halberstam conjecture for friable (smooth) integers**, one gets the full asymptotic density statement with the same product (\rho(1/\alpha)\rho(1/\beta)). ([ScienceDirect][2])

A small technical note: many papers state the condition as (P(n+1)\le n^{\beta}) rather than (P(n+1)<(n+1)^{\beta}), or use (\le) instead of (<). For (\beta<1) these variants differ on a set of size $o(x)$ up to $x$, so they don’t affect whether a natural density exists (nor its value, if it exists).

So the best current answer is:

* **Unconditionally:** existence of the **natural density** is **unknown** (open), but the **logarithmic density exists** and equals (\rho(1/\alpha)\rho(1/\beta)). 
* **Conditionally (EH for friable integers):** the **natural density exists** and equals (\rho(1/\alpha)\rho(1/\beta)). ([ScienceDirect][2])

[1]: https://www.erdosproblems.com/928 "
  
    Erdős Problem #928
  
"
[2]: https://www.sciencedirect.com/science/article/pii/S0022314X21000196 "Three conjectures on P+$n$ and P+(n + 1) hold under the Elliott-Halberstam conjecture for friable integers - ScienceDirect"
