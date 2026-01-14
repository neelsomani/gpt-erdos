What you wrote is exactly the **Erdős–Rado Sunflower Conjecture** (1960): for each fixed number of petals (k\ge 3), does there exist a constant (c_k) (depending only on $k$) such that every $n$-uniform family of size (>c_k^n) contains a $k$-sunflower?

This conjecture is **still open**, even for (k=3). 

### What is known

Let me translate some standard results into your $f(n,k)$ notation [[nomath]](uniformity $=n$, petals $=k$)[[/nomath]].

#### Lower bound (sunflower-free constructions)

There is a simple construction of a $k$-sunflower-free $n$-uniform family of size ((k-1)^n): partition the ground set into $n$ blocks of size $k-1$, and take all sets choosing exactly one element from each block. Erdős and Rado already observed variants of this example; Rao’s survey writes it explicitly. 

So
[
f(n,k) > (k-1)^n,
]
and therefore any conjectured base must satisfy (c_k\ge k-1).

#### Classical upper bound (Erdős–Rado “sunflower lemma”)

Erdős–Rado proved a bound of the form
[
f(n,k) \le n!k^n
]
(up to small changes like $k-1$ vs $k$ depending on conventions). A modern statement in this style appears, for example, as Lemma 1.1 in Frankl’s 2025 paper [[nomath]](using a common notation $m_k(r)$ for the extremal function)[[/nomath]]. 

This is far from (c_k^n) because $n!$ grows super-exponentially.

#### Best *published* general upper bounds (as of early 2025)

A major breakthrough by Alweiss–Lovett–Wu–Zhang improved the bound dramatically, and subsequent work sharpened it. One clean “current best bound” summary (in Frankl 2025) is:

[
m_n(k)\ \le\ (Ck\log n)^n
]
for some absolute constant (C>0). [[nomath]](Frankl states this as $(C r\log k)^k$ with variables swapped: $k$ there is the uniformity and $r$ the number of petals.)[[/nomath]]

So at present the best *published* base is (O_k(\log n)), not a constant.

#### A newer (late 2025) preprint improvement

A December 2025 arXiv preprint by Fukuyama claims a further improvement to a **sub-logarithmic base**:
[
f(n,k)\ \le\ \left(\frac{c,k^2\ln n}{\ln\ln n}\right)^n
]
for an absolute constant (c>0). ([arXiv][1])
This is still not (c_k^n), but it improves the dependence on $n$ in the base from (\log n) to (\log n/\log\log n) (up to $k$-dependent constants).

### Bottom line

* The inequality (f(n,k) < c_k^n) for fixed $k$ is **conjectured** (Erdős–Rado sunflower conjecture) but **not proved**. 
* Best known bounds put (f(n,k)) between roughly ((k-1)^n) and ((\text{poly}(k)\cdot\log n)^n), with a claimed recent improvement to (\bigl(\text{poly}(k)\cdot\frac{\log n}{\log\log n}\bigr)^n). 

If you want, I can also rewrite everything using a single consistent notation and list the sharpest bounds separately for fixed $k$ vs growing $k$, since the literature switches variables a lot.

[1]: https://arxiv.org/abs/2510.19037 "[2510.19037] Sunflower Bound with a Sub-Logarithmic Base"
