Let
[
V(x)=|\\{n\le x:\exists m\text{ with }\varphi(m)=n\\}|,
]
i.e. $V(x)$ counts the **distinct totients** (\le x).

### What is known about $V(x)$

Write (\log_1 x=\log x) and (\log_{k+1}x=\log(\log_k x)) (iterated natural logs). Maier–Pomerance proved the first essentially sharp “main-term-on-the-log-scale” asymptotic:
[
V(x)=\frac{x}{\log x}\exp\Big((C+o(1))(\log_3 x)^2\Big),
]
for an explicit constant (C>0). 

Ford later determined the **true order of magnitude** more precisely, showing
[
V(x)=\frac{x}{\log x}\exp\Big(C(\log_3 x-\log_4 x)^2 + D\log_3 x-(D+\tfrac12-2C)\log_4 x +O(1)\Big),
]
with explicit constants $C,D$. 

Moreover, in Ford’s normalization one can take
[
C=\frac1{2|\log\rho|}=0.8178146464\ldots,\qquad
D=2.1769687435\ldots,
]
where (\rho\in(0,1)) is the unique solution of (F(\rho)=1) for
[
F(x)=\sum_{n\ge1} a_n x^n,\qquad a_n=(n+1)\log(n+1)-n\log n-1.
]


In particular,
[
V(x)=\frac{x}{\log x},(\log x)^{o(1)}= \frac{x}{\log^{,1-o(1)}x},
]
so totients have density $0$, but $V(x)$ is still “close to” (x/\log x) up to a subpower factor (\exp((C+o(1))(\log_3 x)^2)). 

### Does (V(2x)/V(x)\to 2)?

This is **open**. In fact Erdős asked the more general question whether
[
V(cx)\sim c,V(x)\qquad (c>1\ \text{fixed}),
]
which would imply (V(2x)/V(x)\to2). Ford explicitly notes that the methods proving the “true order” above fall short of answering this. 

What *is* known in this direction is a weaker “same-order” statement: for each fixed (c>1),
[
V(cx)-V(x)\asymp_c V(x),
]
so $V(cx)$ and $V(x)$ are comparable up to constants depending on $c$, but this does **not** force $V(cx)/V(x)\to c$. 

### Is there an asymptotic formula?

Not in the strong sense $V(x)\sim \text{(explicit function)}$. The best results are the Maier–Pomerance “((C+o(1))(\log_3 x)^2)” form and Ford’s refinement with an $O(1)$ term in the exponent: these determine $V(x)$ up to multiplicative constants but still do not yield a full asymptotic constant, nor the limit (V(2x)/V(x)\to2). ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/416 "
  
    Erdős Problem #416
  
"
