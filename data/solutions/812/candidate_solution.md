Let me assume $R(n)$ means the **diagonal (two–colour) Ramsey number**
[
R(n)=r(n,n),
]
i.e. the least $N$ such that every red/blue colouring of $E(K_N)$ contains a monochromatic (K_n).

## 1) A fixed multiplicative gap (R(n+1)\ge (1+c)R(n))?

This is **not known**.

In fact, even the *weaker* “near-diagonal” version is a listed open problem: Burr and Erdős asked to prove that there is a fixed (c>0) such that
[
r(n+1,n)>(1+c),r(n,n)
]
for all large $n$. 

Since (r(n+1,n+1)\ge r(n+1,n)), a positive solution of that problem would immediately imply your desired inequality
[
\frac{R(n+1)}{R(n)}=\frac{r(n+1,n+1)}{r(n,n)}\ge 1+c
]
for all large $n$. But as far as the standard references/surveys indicate, this remains open. 

So: **no known constant (c>0)** is proved to work for all sufficiently large $n$.

## 2) A quadratic gap (R(n+1)-R(n)\gg n^2)?

Also **not known**. What *is* known unconditionally is much weaker: only a **linear** lower bound.

A classical result of Burr–Erdős–Faudree–Schelp (1989) proves that for all (m,n\ge 2),
[
r(m,n)\ \ge\ r(m,n-1)+ (2m-3). \tag{*}
]


Apply ((*)) twice:

1. with ((m,n)=(n,n+1)):
   [
   r(n,n+1)\ge r(n,n) + (2n-3),
   ]
2. with ((m,n)=(n+1,n+1)):
   [
   r(n+1,n+1)\ge r(n+1,n) + (2n-1)=r(n,n+1)+(2n-1).
   ]

Combining gives
[
R(n+1)-R(n)=r(n+1,n+1)-r(n,n)\ \ge\ (2n-3)+(2n-1)=4n-4.
]

So we do have
[
R(n+1)-R(n)\ \ge\ 4n-4\qquad\text{for all }n\ge 2,
]
i.e. $R(n+1)-R(n)=\Omega(n)$. 

But this is **far** from (\gg n^2). Indeed, the same paper explicitly remarks that their bound is “far short” of what should be true and that $r(n,n)-r(n-1,n-1)$ must be exponentially large on average (and they believe an exponential lower bound should hold), but this is not proved. 

## Bottom line

* (\displaystyle \frac{R(n+1)}{R(n)}\ge 1+c) for some fixed (c>0) and all large $n$: **open** (even a weaker near-diagonal version is a stated open problem). 
* (\displaystyle R(n+1)-R(n)\gg n^2): **also open**; the best general unconditional lower bound I know is only **linear**, e.g. $R(n+1)-R(n)\ge 4n-4$. 
