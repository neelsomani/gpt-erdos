Write $D_k$ for the set of all integers $m$ that occur as *some* denominator $n_i$ in at least one $k$-term Egyptian fraction representation
$
1=\frac1{n_1}+\cdots+\frac1{n_k},\qquad 1<n_1<\cdots<n_k .
$
[[nomath]](As you noticed, if $k\ge 2$ then $1$ can never occur among the $n_i$, so the standard definition is: **$v(k)$ is the smallest integer $>1$ not in $D_k$**.)[[/nomath]] ([arXiv][1])

The problem of estimating $v(k)$ was posed by Erdős–Graham and remains wide open in the sense that the best known upper and lower bounds are very far apart. The currently best published bounds (as of late 2025) are:

## Best known lower bound [[nomath]](how fast $v(k)$ must grow)[[/nomath]]

There is an absolute constant $c>0$ such that
[
v(k)\ \ge\ e^{c k^2}\qquad \text{for all }k\ge 1.
]
Equivalently: every integer $m<e^{c k^2}$ *does* occur as a denominator in some Egyptian-fraction decomposition of $1$ of length $\le k$, so the smallest “missing” denominator is at least $e^{c k^2}$. ([arXiv][1])

So $v(k)$ grows at least **super-exponentially** in $k$ [[nomath]](faster than $A^k$ for any fixed $A$)[[/nomath]].

## Best known upper bound [[nomath]](how large $v(k)$ could still be)[[/nomath]]

A general counting argument gives
[
v(k)\le |D_k|+2\le kF(k)+2,
]
where $F(k)$ is the number of $k$-term decompositions of $1$. ([arXiv][1])

Using the best available upper bounds for $F(k)$, one obtains a **doubly exponential** upper bound of the shape
[
v(k)\ \le\ c_0^{(1/5+o(1)),2^k}
]
[[nomath]](where $c_0\approx 1.264085$ is the Vardi constant).[[/nomath]] In particular,
[
\log v(k)=O(2^k)\quad\text{and}\quad v(k)\le \exp(C,2^k)
]
for some absolute $C>0$. ([arXiv][1])

## What this means as a “growth estimate”

Putting the two together, there exist absolute constants $c,C>0$ such that
[
\boxed{\ \exp(c k^2)\ \le\ v(k)\ \le\ \exp(C,2^k)\ }.
]
So at the level of logs,
[
ck^2 \ \le\ \log v(k)\ \le\ C2^k.
]

## Conjectural picture

Erdős–Graham speculated that $v(k)$ might grow **doubly exponentially** in $k$. The same 2025 note explains that if a certain $older$ conjecture about representing rationals by unit fractions were true, then their method would plausibly upgrade the lower bound all the way to something like
[
v(k)\ \ge\ \exp(\exp(c'k)),
]
i.e. doubly exponential, matching that speculation up to constants in the exponent. ([arXiv][1])

So the honest “state of the art” is: **provably at least $\exp(\Theta(k^2))$, provably at most $\exp(O(2^k))$, and it is open whether the true growth is closer to the lower bound or to doubly exponential.**

[1]: https://arxiv.org/pdf/2512.22083 "The smallest denominator not contained in a unit fraction decomposition of $1$ with fixed length"
