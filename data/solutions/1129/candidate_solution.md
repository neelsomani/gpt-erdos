Write the **Lebesgue function**
[
\lambda(x):=\sum_{k=1}^n |l_k(x)|\qquad (x\in[-1,1]),
]
so your quantity is the **Lebesgue constant**
[
\Lambda(x_1,\dots,x_n)=\max_{x\in[-1,1]}\lambda(x).
]
This is exactly the operator norm of the Lagrange interpolation projector, and minimizing it over the node set ({x_i}) is the classical “optimal nodes” problem. ([publikacio.uni-eszterhazy.hu][1])

## What is known about the minimizers

### 1) There is no simple closed-form formula for the minimising nodes (in general)

Despite a lot of work, **no explicit general formula** for the minimising node set (X^*={x_i}) is known. ([publikacio.uni-eszterhazy.hu][1])

So the honest answer is: **the exact minimiser is not known in a simple explicit form for general $n$**; the problem is typically treated via characterization + computation. ([Erdős Problems][2])

### 2) But the minimisers are *characterised* by an equioscillation (“equal peaks”) condition

Assume the nodes are ordered (x_1<\cdots<x_n). Consider the maxima of (\lambda) on the subintervals between consecutive nodes [[nomath]](and, if the endpoints $\pm1$ are not included as nodes, also on the two edge intervals)[[/nomath]]. Roughly, define
[
\mu_i := \max_{x\in[x_i,x_{i+1}]}\lambda(x),
]
with the convention (x_0=-1,; x_{n+1}=1) when needed.

A theorem of Kilgore, completed/extended by de Boor–Pinkus, implies that **an optimal configuration is characterized by “equioscillation” of the Lebesgue function**: in an optimal configuration, the “peaks” of (\lambda) between successive nodes are all level (equal). ([Allan Pinkus][3])

This gives a practical description:

* the optimal node set is the one for which the Lebesgue function (\lambda(x)) has **equal maximal values** on each subinterval between consecutive nodes. ([Allan Pinkus][3])

### 3) Uniqueness depends on a normalisation: “canonical” nodes

Without extra constraints, **optimal node systems are not unique**; in fact, there are [[nomath]](for $n\ge3$)[[/nomath]] uncountably many optimal node systems in $[-1,1]$. ([cs.ubbcluj.ro][4])

A standard way to remove this non-uniqueness is to restrict to **canonical** configurations, meaning you force the endpoints to be included:
[
x_1=-1,\qquad x_n=1.
]
In that canonical setting, there is a **unique** minimising set, and it is **symmetric about $0$** (zero-symmetric). ([cs.ubbcluj.ro][4])

So, in words:

* **Among all node sets** there are many minimisers.
* **Among canonical node sets** [[nomath]]($\pm1$ included)[[/nomath]], there is a **unique minimiser**, symmetric about $0$, and characterised by the equioscillation/level-peaks property of (\lambda). ([cs.ubbcluj.ro][4])

## Small $n$ (where the minimiser is explicitly known)

For canonical minimisers, the explicit solution is only known for very small $n$:

* $n=2$: $\\{-1,1\\}$, with (\Lambda=1).
* $n=3$: $\\{-1,0,1\\}$, with (\Lambda=1.25).
* $n=4$: $\\{-1,-t,t,1\\}$ where (t\approx 0.4177), with (\Lambda\approx 1.4229). ([Erdős Problems][2])

Beyond this, the canonical minimiser exists and is uniquely determined by the equioscillation condition, but no simple closed-form description is known. ([Erdős Problems][2])

## What you *can* say asymptotically (and what to use in practice)

### Optimal order of growth

A classical theorem chain (Faber → Bernstein → Erdős) shows that **for any** choice of nodes,
[
\Lambda(x_1,\dots,x_n)\ \ge\ \frac{2}{\pi}\log n - O(1),
]
and this is sharp in order. ([Erdős Problems][2])

### Chebyshev-type nodes are near-optimal and achieve the sharp leading term

If you take the **Chebyshev nodes** [[nomath]](zeros of $T_n$)[[/nomath]],
[
x_k=\cos\frac{(2k-1)\pi}{2n},\qquad k=1,\dots,n,
]
then
[
\Lambda = \frac{2}{\pi}\log n + O(1),
]
so they match the optimal (\frac{2}{\pi}\log n) growth. ([publikacio.uni-eszterhazy.hu][1])

Even better (and closer to the *true* canonical minimiser) are the **extended Chebyshev nodes** [[nomath]](a simple rescaling of the Chebyshev zeros so the largest ones hit $\pm1$)[[/nomath]]:
[
x_k=\frac{\cos!\big(\frac{(2k-1)\pi}{2n}\big)}{\cos!\big(\frac{\pi}{2n}\big)},\qquad k=1,\dots,n,
]
which strictly improve the Lebesgue constant compared to unscaled Chebyshev nodes. ([publikacio.uni-eszterhazy.hu][1])

Moreover, de Boor–Pinkus report that such “extended Chebyshev” nodes produce a Lebesgue norm extremely close (within a small additive constant) to the optimal one, and numerical evidence suggests the gap is tiny. ([Allan Pinkus][3])

## Final “description” of the minimising choice

* The exact minimiser ({x_i}) of (\Lambda) on $[-1,1]$ is a **classical optimal-nodes problem with no known simple explicit formula for general $n$**. ([publikacio.uni-eszterhazy.hu][1])
* The minimisers are **characterised** by an **equioscillation/level-peaks property** of the Lebesgue function (\lambda(x)=\sum|l_k(x)|): in an optimal configuration, the maximal values of (\lambda) on each interval between consecutive nodes are all equal. ([Allan Pinkus][3])
* If you restrict to **canonical** node sets with endpoints included $(x_1=-1, x_n=1)$, then the minimiser is **unique** and **symmetric** about $0$; explicit closed forms are known only for (n\le4). ([cs.ubbcluj.ro][4])
* For practical purposes (and asymptotically optimal growth), use **Chebyshev** or better **extended Chebyshev** nodes, which achieve the best possible (\sim \frac{2}{\pi}\log n) behaviour. ([publikacio.uni-eszterhazy.hu][1])

[1]: https://publikacio.uni-eszterhazy.hu/3018/1/AMI_33_from109to123.pdf "beliv.dvi"
[2]: https://www.erdosproblems.com/forum/thread/1129 "

    Erdős Problem #1129 - Discussion thread

"
[3]: https://pinkus.net.technion.ac.il/files/2021/02/conj.pdf "PII: 0021-9045(78)90014-X"
[4]: https://www.cs.ubbcluj.ro/journal/studia-mathematica/archive/2015-2/01-Rack-Vajda-final.pdf "01-Rack-Vajda-final.dvi"
