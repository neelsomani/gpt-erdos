This is a well known conjecture (Erdős–Herzog–Piranian).

Let
[
L(p)=\text{(arc length of the curve)}\quad {z\in\mathbb C:\ |p(z)|=1}
]
for a monic polynomial $p$ of degree $n$. The conjecture says that $L(p)$ is **largest** when (p(z)=z^n-1) (more precisely, up to moving and rotating the picture, (p(z)=(z-z_0)^n-e^{i\theta}) gives the same curve length). ([arXiv][1])

### What is known today

* **(n=1)**: trivial (the curve is a circle of length (2\pi)). ([arXiv][1])
* **(n=2)**: **yes, it is true**. Eremenko and Hayman proved the conjecture in degree 2 (the maximiser gives Bernoulli’s lemniscate, i.e. the curve (|z^2-1|=1) up to a rotation). 
* **General (n)** (older progress): Fryntov and Nazarov proved that (z^n-1) is a **local** maximiser, and they proved an **asymptotically sharp** upper bound (L(p)\le 2n+o(n)) as (n\to\infty). ([arXiv][2])
* **Big new result (Dec 2025)**: Terence Tao proved the full “maximised by (z^n-1)” statement for **all sufficiently large $n$**, and he also proved the equality case: for large $n$, equality happens only for translates/rotates ((z-z_0)^n-e^{i\theta}). ([arXiv][1])

He also gives an exact special‑function formula for the length in the model case:
[
L(z^n-1)=2^{1/n},B!\left(\tfrac12,\tfrac{1}{2n}\right)
=2n+4\log 2+O(1/n),
]
so the extremal length grows like $2n$. ([arXiv][1])

### So is it maximised by (z^n-1)?

* **For all large enough degrees $n$**: **yes (proved).** ([arXiv][1])
* **For every single degree $n$**: as of now, the literature still treats the full “all $n$” statement as **not completely finished**, because Tao’s theorem leaves only **finitely many small $n$** to check separately (he remarks that it reduces to a finite verification problem, but does not claim every small case is done). ([arXiv][1])

Forward-looking: the problem is now “almost solved”: it is proven for $n=2$ and for all large $n$, and what is left is a finite list of small degrees. ([arXiv][1])

[1]: https://arxiv.org/pdf/2512.12455 "The maximal length of the Erd\H{o}s--Herzog--Piranian lemniscate in high degree"
[2]: https://arxiv.org/abs/0808.0717 "[0808.0717] New estimates for the length of the Erdos-Herzog-Piranian lemniscate"
