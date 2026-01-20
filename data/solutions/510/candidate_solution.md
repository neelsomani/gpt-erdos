As stated for **arbitrary** finite (A\subset\mathbb Z), the answer is **no**.

Take (A={0,m}) [[nomath]](so $N=2$)[[/nomath]]. Then for every (\theta),
[
\sum_{n\in A}\cos(n\theta)=\cos(0\cdot\theta)+\cos(m\theta)=1+\cos(m\theta)=2\cos^2!\Big(\frac{m\theta}{2}\Big)\ge 0,
]
so it can never be (< -c\sqrt{2}) for any (c>0).

---

If you **exclude this trivial obstruction** [[nomath]](e.g. assume $0\notin A$, or work with $A\subset \mathbb Z_{>0}$)[[/nomath]], then your question is essentially **Chowla’s cosine problem**: for an $n$-element set $A$ of positive integers,
[
\min_{x\in[0,2\pi]}\sum_{a\in A}\cos(ax)\ \stackrel{?}{\le}\ -\Omega(\sqrt n),
]
which is exactly the (-c\sqrt n) bound you’re asking about. ([arXiv][1])

### Current status (as of late 2025 / early 2026)

The (\sqrt n) bound is **conjectured** but **not proved** in general. The best unconditional results are weaker [[nomath]](smaller exponent than $1/2$)[[/nomath]]:

* **Bedert (2025)** proved a *polynomial* bound:
  [
  \min_{x\in[0,2\pi]}\sum_{a\in A}\cos(ax)\ \le\ -n^{,1/7-o(1)}.
  ]
  ([arXiv][2])

* **Jin–Milojević–Tomon–Zhang (2025)** independently proved another polynomial bound:
  [
  \min_{x\in[0,2\pi]}\sum_{a\in A}\cos(ax)\ \le\ -|A|^{,1/10-o(1)}.
  ]
  ([arXiv][1])

[[nomath]](Previously the best general bounds were only “quasipolynomial”; e.g. Bedert summarizes Ruzsa’s earlier record as $K(n)\gtrsim \exp(c'(\log n)^{1/2})$, which corresponds to $\min \sum \cos(ax)$ being at most about $-\exp(\Omega(\sqrt{\log n}))$. $[arXiv][2]$)[[/nomath]]

### Why the exponent $1/2$ is the “right” target

There are explicit constructions showing you **can’t hope for an exponent bigger than $1/2$** in general: Bedert notes there are $n$-element sets $A$ for which
[
\sum_{a\in A}\cos(ax)\ \ge\ -10\sqrt n\quad\text{for all }x,
]
(using difference sets of Sidon sets), giving the matching *upper* order (\sqrt n). ([arXiv][2])
So if the conjectured (-c\sqrt n) lower bound holds, it would be sharp up to constants.

---

So the clean answer is:

* **No** for general (A\subset\mathbb Z) [[nomath]](because $0$ can be in $A$)[[/nomath]].
* For the usual nonzero/positive-integer version, your (-c\sqrt N) inequality is **exactly Chowla’s conjecture** and remains open, with best known guarantees currently of size (-N^{1/7-o(1)}). ([arXiv][2])

[1]: https://arxiv.org/pdf/2509.03490 "From small eigenvalues to large cuts, and Chowla's cosine problem"
[2]: https://arxiv.org/pdf/2509.05260 "Polynomial bounds for the Chowla Cosine Problem"
