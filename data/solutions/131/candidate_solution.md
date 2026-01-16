People usually call such a set **non‑dividing**.

### What is known now

Write $F(N)$ for the largest (|A|\subseteq{1,\dots,N}) with the property that for every (a\in A), **no sum of distinct elements from (A\setminus\\{a\\})** is divisible by $a$.

#### A very strong upper bound [[nomath]](so the $\sqrt N$ guess is false)[[/nomath]]

If (a\in A) were the average of some other distinct elements (x_1,\dots,x_t\in A\setminus\\{a\\}) [[nomath]](with $t\ge 2$)[[/nomath]], then

$$
x_1+\cdots+x_t = ta,
$$

so (a\mid(x_1+\cdots+x_t)), which is forbidden.
So **every non‑dividing set is automatically non‑averaging**.

Pham and Zakharov (2024; published 2025) proved that the largest non‑averaging subset of $[N]$ has size
$$
N^{1/4+o(1)}.
$$
Therefore,
$$
F(N)\ \le\ N^{1/4+o(1)}.
$$
So the proposed lower bound
$$
F(N) > N^{1/2-o(1)}
$$
is **not true**. ([arXiv][1])

#### Lower bound (polynomial constructions exist)

There are explicit constructions (credited by Erdős to Csaba, and also given in later work) showing
$$
F(N)\ \gg\ N^{1/5}.
$$
One clean way to think about where $1/5$ comes from is an older reduction (Straus/Abbott style) that turns a non‑averaging set of size about (M^{1/4}) into a non‑dividing set inside $[N]$ of size about (N^{1/5}). ([MSP][2])

[[nomath]](There is also an older, weaker but still super‑polylog lower bound of the form $\exp(c\sqrt{\log N})$, but $N^{1/5}$ is much larger for large $N$.)[[/nomath]] ([Erdős Problems][3])

### Best “estimate” in the usual asymptotic sense

Putting the best current bounds together, we have
$$
N^{1/5}\ \ll\ F(N)\ \ll\ N^{1/4+o(1)}.
$$
So the true growth is known only to lie between exponents $0.2$ and $0.25$, and narrowing that gap is still open. ([Erdős Problems][3])

[1]: https://arxiv.org/abs/2410.14624?utm_source=chatgpt.com "Sharp bound for the Erdős-Straus non-averaging set problem"
[2]: https://msp.org/pjm/1980/91-1/pjm-v91-n1-p01-s.pdf "Extremal problems on nonaveraging and nondividing sets"
[3]: https://www.erdosproblems.com/131?utm_source=chatgpt.com "Erdős Problem #131"
