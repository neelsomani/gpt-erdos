Let (A\subseteq \mathbb N) and write
[
r_A(n):=(1_A*1_A)(n)=|\\{(a,b)\in A^2:a+b=n\\}|.
]

This question is **open in general**: it is exactly **Erdős Problem #40**. ([Erdős Problems][1])
In fact, any positive answer for *any* diverging $g(N)$ would imply the (also open) **Erdős–Turán conjecture** on additive bases of order $2$. ([Erdős Problems][1])

What *is* known is the following clean obstruction.

## It is false for any $g$ that is at least a fixed power of $N$

Erdős and Rényi constructed, for every fixed (\varepsilon>0), a set (A\subset\mathbb N) such that

* (|A\cap{1,\dots,N}|\gg_\varepsilon N^{1/2-\varepsilon}) for all large $N$, and
* (r_A(n)=(1_A*1_A)(n)\ll_\varepsilon 1) for all (n) (so in particular (\limsup r_A(n)<\infty)). ([Erdős Problems][2])

Now if your $g$ satisfies (g(N)\ge N^{\varepsilon}) for all large $N$ (for some fixed (\varepsilon>0)), then
[
\frac{\sqrt N}{g(N)} \le N^{1/2-\varepsilon},
]
so that Erdős–Rényi example satisfies your density hypothesis but has bounded (r_A(n)). Hence the implication fails for such (g).

So a **necessary condition** for the implication to have any chance is:
[
g(N)=N^{o(1)}\quad\text{(i.e. }g(N)\ll N^\varepsilon\text{ for every }\varepsilon>0\text{)}.
]

## What happens for subpolynomial $g$ [[nomath]](like $\log N$, $\log\log N$, etc.)[[/nomath]]?

As far as I can tell from the standard references collected for this problem, **no nontrivial subpolynomial $g$ is known** for which the implication has been proved.

And conversely, **no counterexample is known** at densities as large as (\sqrt N / g(N)) when $g$ is subpolynomial [[nomath]](e.g. $g(N)=\log N$, $g(N)=(\log N)^C$, $g(N)=\exp(\sqrt{\log N})$, …)[[//nomath]].

That “unknown zone” is exactly why Erdős posed Problem #40, and why the problem page notes it is a stronger form of Erdős–Turán. ([Erdős Problems][1])

## Bottom line

* If $g(N)$ eventually dominates a power (N^\varepsilon), then **the implication is false** (Erdős–Rényi counterexample). ([Erdős Problems][2])
* For genuinely subpolynomial (g(N)\to\infty), the problem is **open** (and proving it for any such $g$ would settle Erdős–Turán). ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/40 "
  
    Erdős Problem #40
  
"
[2]: https://www.erdosproblems.com/39 "
  
    Erdős Problem #39
  
"
