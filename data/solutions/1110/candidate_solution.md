Let (R_{p,q}) be the set of representable integers and (N_{p,q}=\mathbb Z_{>0}\setminus R_{p,q}). By “density” I’ll mean **natural density**:
[
d(A)=\lim_{x\to\infty}\frac{|A\cap[1,x]|}{x}
\quad\text{(if the limit exists).}
]

### What is known in general [[nomath]](when ${p,q}\neq{2,3}$)[[/nomath]]

Erdős and Lewin proved that there are **finitely many** non‑representable integers **if and only if** ({p,q}={2,3}). In particular, for every coprime pair ({p,q}\neq{2,3}) there are **infinitely many** non‑representable integers. ([Erdős Problems][1])

### Density of non‑representables: almost always density $1$

A substantial partial answer is due to **Yu and Chen (2022)**. In the ranges

* (q>3), or
* $q=3$ and (p>6), or
* $q=2$ and (p>10),

they show that the set of **representable** numbers has density $0$, i.e. (d(R_{p,q})=0). Equivalently,
[
d(N_{p,q})=1
]
in all those cases. ([Erdős Problems][1])

So, except for a **finite list of small pairs**, the answer is very strong: **almost every integer is non‑representable**.

The only coprime pairs not covered by the above density‑$1$ conclusion are the small cases
[
( p,q )\in{(5,2),(7,2),(9,2),(4,3),(5,3)}
]
[[nomath]](and of course $(3,2)$ is the ${2,3}$ case)[[/nomath]]. For these remaining small pairs, the density question is still open in the sense of the Erdős problem entry. ([Erdős Problems][1])

### Infinitely many **coprime** non‑representables?

Interpreting “coprime non‑representable” as $\gcd(n,pq)=1$: Yu and Chen proved that there are **infinitely many** such $n$ [[nomath]](coprime to $pq$ and non‑representable)[[/nomath]] for every pair except
[
{p,q}\in\\{{2,3},{2,5},{2,9},{3,5}\\}.
]

Since your question assumes ({p,q}\neq{2,3}), this gives:

* **Yes**, there are infinitely many coprime non‑representables for all coprime (p>q\ge2) **except possibly** the three cases
  [
  (p,q)=(5,2),\ (9,2),\ (5,3),
  ]
  where the infinitude of coprime non‑representables is not settled by that result.

If you tell me which specific $(p,q)$ you care about [[nomath]](e.g. $(5,2)$ or $(7,2)$)[[/nomath]], I can summarize what the known results imply for that pair and what remains open.

[1]: https://www.erdosproblems.com/1110 "https://www.erdosproblems.com/1110"
