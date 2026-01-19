I’ll take “mutually coprime” in the (standard in this Erdős-problem context) sense that the **whole set has gcd 1**, i.e.
[
h(n):=\min\\{m\ge 2:\gcd\bigl(2^n-1,3^n-1,\dots,m^n-1\bigr)=1\\},
]
which is exactly the formulation of Erdős Problem #770. ([Erdős Problems][1])
(If one interpreted “mutually coprime” as *pairwise* coprime, the definition would collapse: adding more terms can’t fix a bad pair.)

## Basic structural facts (unconditional)

### 1) $h(n)$ is always prime

Let (m=h(n)). Then
[
G:=\gcd(2^n-1,3^n-1,\dots,(m-1)^n-1) > 1.
]
Pick a prime (q\mid G). Then for every (2\le a\le m-1) we have (a^n\equiv 1\pmod q).

If $m$ were composite, write $m=ab$ with (2\le a,b<m). Then (a^n\equiv b^n\equiv 1\pmod q), hence
[
m^n=(ab)^n\equiv 1\pmod q \quad\Rightarrow\quad q\mid (m^n-1),
]
so $q$ would also divide (\gcd(2^n-1,\dots,m^n-1)), contradicting the defining property (\gcd(\dots)=1).
Therefore $m$ is prime, i.e. **$h(n)$ is prime for every $n$**.

So it makes sense that the question only asks about (\delta_p) for primes $p$.

### 2) A clean upper bound: (h(n)\le n+1)

Let (m=h(n)) and (q\mid \gcd(2^n-1,\dots,(m-1)^n-1)) be prime. Then (q>m-1) [[nomath]](since if $q\le m-1$ then $a=q$ is among the terms and $q\nmid(q^n-1)\equiv -1\pmod q$)[[/nomath]]. Thus (1,2,\dots,m-1) are **distinct** nonzero residues mod $q$, and all satisfy (x^n\equiv 1\pmod q).

In ((\mathbb Z/q\mathbb Z)^*) the set of $n$-th roots of unity is a subgroup of size (\gcd(n,q-1)\le n). Since it contains (1,2,\dots,m-1), it has size at least $m-1$. Hence (m-1\le n), i.e.
[
h(n)=m\le n+1.
]

### 3) Characterization (h(n)=n+1 \iff n+1) is prime

* If (h(n)=n+1), then $n+1$ must be prime because $h(n)$ is always prime.
* If (n+1=p) is prime, then (n=p-1), and by Fermat (p\mid (a^{p-1}-1)=a^n-1) for every (1\le a\le p-1). In particular (p\mid\gcd(2^n-1,\dots,(p-1)^n-1)), so (h(n)\ge p). Together with (h(n)\le n+1=p), this forces (h(n)=p=n+1).

This is one of the “easy to see” observations recorded on the Erdős-problems page. ([Erdős Problems][1])

### 4) A general lower bound from “(p-1\mid n)”

If $p$ is prime and (p-1\mid n), then for every (2\le a\le p-1) we have (a^n\equiv 1\pmod p), so (p\mid (a^n-1)). Hence
[
\gcd(2^n-1,\dots,(p-1)^n-1)\ \text{is divisible by }p,
]
so (h(n)\ge p).
In other words, your “largest prime with (p-1\mid n)” is an **automatic lower bound** for $h(n)$; your last question is asking when this lower bound is actually sharp.

## Unboundedness on odd $n$ (unconditional)

It is known (and noted on the Erdős-problems page) that $h(n)$ is **unbounded even when $n$ is restricted to odd integers**. ([Erdős Problems][1])

A standard way to see this is:

For any $K$, choose a prime (q\equiv 3\pmod 4) such that (2,3,\dots,K) are all **quadratic residues mod $q$** (existence follows from Chebotarev/Dirichlet in an appropriate compositum of quadratic fields). Then set
[
n=\frac{q-1}{2},
]
which is odd because (q\equiv 3\pmod4). For each (2\le a\le K), since $a$ is a quadratic residue, Euler’s criterion gives
[
a^{(q-1)/2}\equiv 1\pmod q,
]
so (q\mid(a^n-1)) for all (2\le a\le K). Therefore
[
\gcd(2^n-1,3^n-1,\dots,K^n-1)\ \text{is divisible by }q,
]
so (h(n)>K). As $K$ was arbitrary, $h(n)$ is unbounded along odd $n$.

## Now to your three questions

### $i$ Existence of densities (\delta_p)

As of the current state of the literature recorded for this Erdős problem, this is **open**. ([Erdős Problems][1])

A key point is that even the case $p=3$ is already deep:
[
h(n)=3 \iff \gcd(2^n-1,3^n-1)=1,
]
and the set of such $n$ is OEIS A263647, which is **conjectured to be infinite** (and the conjecture is tied to Ailon–Rudnick). ([OEIS][2])
Without even knowing infinitude, a fortiori the natural density (\delta_3) is not known to exist.

There is computational/heuristic evidence in the comments for #770 [[nomath]](e.g. among the first 20000 prime exponents $p$, most have $h(p)=3$)[[/nomath]], but this is far from a proof and is about primes $n$, not the full integers. ([Erdős Problems][1])

### (ii) Does (\liminf_{n\to\infty} h(n)=\infty)?

Also **open**. ([Erdős Problems][1])

* If one could prove (h(n)=3) infinitely often, then (\liminf h(n)=3), so the answer would be **no**.
* Erdős-problems commentary says it is “probably true” that (h(n)=3) infinitely often, which would indeed force (\liminf h(n)) to be finite [[nomath]](actually $=3$)[[/nomath]]. ([Erdős Problems][1])
* But this infinitude is currently conjectural and is connected to the Ailon–Rudnick circle of problems. ([OEIS][3])

So at present one cannot rule out (\liminf h(n)=\infty), but the prevailing heuristic expectation is that it is **finite**, likely $3$.

### (iii) The “largest $p$ with (p-1\mid n) and (p>n^\varepsilon)” criterion

As stated [[nomath]](without an “eventually for large $n$” qualifier)[[/nomath]], it is **false**: there is an explicit counterexample recorded in the discussion:
[
n=4044,\quad \max{p:\ p\text{ prime},\ p-1\mid n}=13,\quad \text{but }h(4044)=17>13.
]
Moreover (13>4044^{0.3}), so this violates the proposed implication for (\varepsilon=0.3). ([Erdős Problems][1])

Whether some **asymptotic** version holds [[nomath]](e.g. “for each fixed $\varepsilon>0$, for all sufficiently large $n$ …”)[[/nomath]] is not resolved there and appears to be part of what makes the problem hard; the comments give heuristic reasoning about runs of $k$-th power residues but no theorem. ([Erdős Problems][1])

---

If you want, I can also spell out the exact reformulation of “(h(n)=p)” in terms of *simultaneous power-residue conditions* modulo primes (q>p) (it’s the natural group-theoretic way to encode the obstruction), which is the lens through which both the odd-$n$ unboundedness proof and the last conjecture’s heuristics are usually viewed.

[1]: https://www.erdosproblems.com/forum/thread/770 "https://www.erdosproblems.com/forum/thread/770"
[2]: https://oeis.org/A263647 "A263647 - OEIS"
[3]: https://oeis.org/A086892 "A086892 - OEIS"
