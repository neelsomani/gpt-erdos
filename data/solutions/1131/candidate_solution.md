Let (P_{n-1}) be the space of real polynomials of degree (\le n-1), and let $\\{\phi_j\\}_{j=0}^{n-1}$ be any orthonormal basis of (L^2([-1,1])\cap P*{n-1}) (e.g. normalized Legendre polynomials).

Define the (n\times n) “evaluation matrix”
[
A_{k,j}=\phi_{j-1}(x_k)\qquad (k,j=1,\dots,n).
]
Since the Lagrange polynomials satisfy
[
l_k(x)=\sum_{j=1}^n c_{j,k},\phi_{j-1}(x),\qquad l_k(x_i)=\delta_{ik},
]
we have (A,C=I), i.e. (C=A^{-1}), where (C=(c_{j,k})). Therefore
[
|l_k|*{L^2([-1,1])}^2=\sum_{j=1}^n |c_{j,k}|^2,
]
and summing over $k$ gives the basis‐invariant identity
[
I(x_1,\dots,x_n)=\sum_{k=1}^n |l_k|_2^2
=|A^{-1}|_F^2
=\operatorname{tr}!\bigl((A^\top A)^{-1}\bigr).
]
So your problem is exactly the **$A$-optimal saturated design** problem for polynomial regression on $[-1,1]$.

## What is known rigorously

This is a classical Erdős extremal problem. Let
[
I_n^{\min}:=\inf_{x_1,\dots,x_n\in[-1,1]} I(x_1,\dots,x_n).
]

* There is an explicit **general upper bound** coming from the **Fejér–Legendre / Legendre–Gauss–Lobatto** nodes [[nomath]](endpoints $\pm1$ together with the zeros of $P_{n-1}'$)[[/nomath]]. For that choice one gets
  [
  I_n = 2-\frac{2}{2n-1},
  ]
  hence
  [
  I_n^{\min}\le 2-\frac{2}{2n-1}=2-\frac{1+O(1/n)}{n}.
  ]
* Erdős conjectured these nodes minimize $I$, but **Szabados showed they do not give the exact minimum for any (n>3)**. ([Erdős Problems][1])
* The best general lower bounds I know in the classical literature are of the form
  [
  I_n^{\min}\ge 2 - C\frac{(\log n)^2}{n}
  ]
  for an absolute constant (C>0). ([Erdős Problems][1])

So, rigorously, we know
[
2-C\frac{(\log n)^2}{n}\ \le\ I_n^{\min}\ \le\ 2-\frac{2}{2n-1},
]
hence (I_n^{\min}\to 2) as (n\to\infty), and the deficit (2-I_n^{\min}) is between (\asymp 1/n) and (\lesssim (\log n)^2/n). ([Erdős Problems][1])

## Is (I_n^{\min}=2-(1+o(1))\frac1n) true?

From the **upper bound** alone, you certainly get
[
I_n^{\min}\le 2-\frac{1+o(1)}{n},
]
but the sharp constant in front of $1/n$ is **not settled** by the known lower bounds (they allow larger constants, even slowly growing ones). And Szabados’s result only tells us the Fejér–Legendre construction is not *exactly* optimal for fixed (n>3), not what happens in the limit. ([Erdős Problems][1])

### Numerical evidence (not a proof)

I numerically minimized $I$ for (n\le 20) [[nomath]](multiple starts; the minimizers found are symmetric and include $\pm1$)[[/nomath]]. The table compares “best found” values with the Fejér–Legendre value (2-\frac{2}{2n-1}):

|  n | best found min $I$ | Fejér–Legendre $I=2-\frac{2}{2n-1}$ | improvement | $n(2-I)$ |
| -: | -----------------: | ----------------------------------: | ----------: | -------: |
|  2 |        1.333333333 |                         1.333333333 | 0.000000000 | 1.333333 |
|  3 |        1.600000000 |                         1.600000000 | 0.000000000 | 1.200000 |
|  4 |        1.710758107 |                         1.714285714 | 0.003527607 | 1.156968 |
|  5 |        1.772609338 |                         1.777777778 | 0.005168440 | 1.136953 |
|  6 |        1.812367305 |                         1.818181818 | 0.005814514 | 1.125796 |
|  7 |        1.840164797 |                         1.846153846 | 0.005989049 | 1.118846 |
|  8 |        1.860727827 |                         1.866666667 | 0.005938840 | 1.114178 |
|  9 |        1.876570791 |                         1.882352941 | 0.005782150 | 1.110863 |
| 10 |        1.889159043 |                         1.894736842 | 0.005577800 | 1.108410 |
| 12 |        1.907911928 |                         1.913043478 | 0.005131549 | 1.105057 |
| 14 |        1.921221201 |                         1.925925926 | 0.004704725 | 1.102899 |
| 16 |        1.931166235 |                         1.935483871 | 0.004317636 | 1.101340 |
| 18 |        1.938874467 |                         1.942857143 | 0.003982675 | 1.100260 |
| 20 |        1.945023473 |                         1.948717949 | 0.003694477 | 1.099531 |

For these best found minima, the coefficient (c_n:=n(2-I_n^{\min})) is around $1.10$ and slowly decreasing with $n$ [[nomath]](at least up to $n=20$)[[/nomath]].

A simple explicit *constructive* family that keeps doing similarly well for larger (n) is to take **Jacobi–Gauss–Lobatto** points for the weight ((1-x^2)^{\alpha}) with (\alpha\approx 1/4) [[nomath]](endpoints $\pm1$ plus zeros of $P_{n-2}^{(\alpha+1,\alpha+1)}$)[[/nomath]]. For example at (n=100) with (\alpha=\tfrac14) I get
[
I \approx 1.989050600,\qquad n(2-I)\approx 1.09494.
]
That is noticeably larger than (1).

### What I would conclude from this

* Rigorously: the exact asymptotic constant in front of (1/n) is **not known** from the classical bounds. ([Erdős Problems][1])
* Numerically [[nomath]](and consistently with Szabados’s fact that Fejér–Legendre isn’t exact for $n>3$)[[/nomath]]: the minimum seems to behave like
  [
  I_n^{\min}\approx 2-\frac{c}{n}\quad\text{with }c\approx 1.09,
  ]
  rather than (c=1).

So, on the specific question “is it true that (\min I=2-(1+o(1))/n)?”: **it’s not established in the literature cited above, and the numerics I get point away from the constant $1$** [[nomath]](suggesting a constant closer to $\approx 1.09$)[[/nomath]]. ([Erdős Problems][1])

If you want, I can also list the *best found node sets* for a given $n$, or derive the reformulation (I=\operatorname{tr}((A^\top A)^{-1})) into a condition that the minimizers must satisfy (Euler–Lagrange / KKT equations), which is usually the starting point for asymptotics.

[1]: https://www.erdosproblems.com/1131 "https://www.erdosproblems.com/1131"

