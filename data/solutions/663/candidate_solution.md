This is **open** as far as current literature/status-tracking goes (it is listed as Erdős problem **#663**, attributed to **Erdős and Pomerance**). ([Erdős Problems][1])

### What *is* known unconditionally (easy upper bound)

Write
[
A(n,k)=\prod_{i=1}^k (n+i),
\qquad
q(n,k)=\min{p\text{ prime}: p\nmid A(n,k)}.
]
A standard “primorial” argument gives the **general bound**
[
q(n,k);<;(1+o(1)),k\log n \qquad (n\to\infty,\ \text{uniformly in fixed }k),
]
and Erdős explicitly records this as a “clearly very crude” estimate. 

Sketch of the argument: if (q(n,k)>y), then every prime (p\le y) divides $A(n,k)$, hence the primorial (\prod_{p\le y}p) divides $A(n,k)$. Taking logs,
[
\sum_{p\le y}\log p \le \log A(n,k)\le k\log(n+k)=k\log n+O_k(1).
]
By the prime number theorem [[nomath]](Chebyshev $\vartheta(y)\sim y$)[[/nomath]], (\sum_{p\le y}\log p=(1+o(1))y), yielding (y\le (1+o(1))k\log n), i.e. $q(n,k)\le (1+o(1))k\log n$.

### The conjectured improvement to ((1+o(1))\log n)

Your inequality
[
q(n,k)<(1+o(1))\log n \quad\text{for fixed }k
]
is exactly what Erdős suggested might be true [[nomath]](he even suggests it plausibly holds for the wider range $k=o(\log n)$)[[/nomath]]. 
But no proof is currently known (again, per the problem’s current “open” status). ([Erdős Problems][1])

### Why the constant “1” would be best possible

You can’t hope for (q(n,k)\le (1-\delta)\log n) uniformly in $n$, even for fixed $k$, because along primorial-type examples you get $q(n,k)$ of size (\sim \log n). For instance, let (P_y=\prod_{p\le y}p) and take (n=P_y-1). Then (n+1=P_y), so every prime (\le y) divides $A(n,k)$, hence (q(n,k)>y), while (\log n\sim \log P_y\sim y). So (q(n,k)\ge (1-o(1))\log n) infinitely often.

### Heuristic evidence (Tao’s comment)

Terry Tao gives a heuristic suggesting the conjecture should be true: for “random” (n\in[x,2x]), requiring that *all* primes in $((1+o(1))\log x,(1+\varepsilon)\log x]$ also divide one of (n+1,\dots,n+k) has an extremely small “probability” of order (x^{-\varepsilon+o(1)}), which should dominate the (x^{o(1)})-type combinatorial choices of allocating smaller primes among the $k$ shifts. This suggests only finitely many $n$ could violate (q(n,k)<(1+\varepsilon)\log n). ([Erdős Problems][2])
But turning this into a rigorous argument appears difficult. ([Erdős Problems][2])

### Bottom line

* The bound (q(n,k)<(1+o(1))k\log n) is known and easy. 
* The improvement to (q(n,k)<(1+o(1))\log n) for fixed $k$ is **conjectured/heuristically supported but currently unproved**. ([Erdős Problems][1])
* If true, it would be essentially sharp [[nomath]](up to the $1+o(1)$)[[/nomath]].

[1]: https://www.erdosproblems.com/663 "https://www.erdosproblems.com/663"
[2]: https://www.erdosproblems.com/forum/discuss/663 "https://www.erdosproblems.com/forum/discuss/663"
