This is **open in general**.

In fact, your question is a classical Erdős problem (often phrased in terms of “LCM triangles”): does every *positive-density* subset (A\subseteq{1,\dots,N}) contain three **distinct** (a,b,c\in A) with
[
\operatorname{lcm}(a,b)=\operatorname{lcm}(b,c)=\operatorname{lcm}(a,c), ?
]
As of the current literature summaries (e.g. Erdős Problems database), this is **unknown** for an arbitrary fixed (\epsilon>0). ([Erdős Problems][1])

### A useful reformulation (what such triples look like)

Call ({a,b,c}) an **lcm triangle** if ([a,b]=[b,c]=[a,c]). If this common value is $L$, then setting
[
x=\frac{L}{a},\quad y=\frac{L}{b},\quad z=\frac{L}{c},
]
one can check that the condition is equivalent to
[
\gcd(x,y)=\gcd(x,z)=\gcd(y,z)=1,
]
i.e. (x,y,z) are pairwise coprime, and then [[nomath]](writing $t=L/(xyz)$)[[/nomath]] you get the structural form
[
{a,b,c}={t,yz,\ t,xz,\ t,xy}
]
with (x,y,z) pairwise coprime.
Example: ({6,10,15}={(2\cdot 3),(2\cdot 5),(3\cdot 5)}) has pairwise lcm (=30).

So the problem asks whether every positive-density set must contain a triple of this “pairwise products” type.

### What *is* known

#### 1) If (\epsilon) is very close to $1$, then **yes**

There is a simple argument (attributed in the Erdős Problems forum to Weisenberg) showing that any lcm-triangle-free set must miss a positive proportion of ({1,\dots,N}). Concretely:

For each integer $m$, the triple
[
{6m,,10m,,15m}
]
is an lcm triangle, since
[
[6m,10m]=[6m,15m]=[10m,15m]=30m.
]
Moreover, if one restricts to (m\le N/15) with (\gcd(m,30)=1), then these triples are **pairwise disjoint** (no integer can lie in two different such triples). The count of such $m$ is asymptotic to
[
\frac{N}{15}\cdot \frac{\varphi(30)}{30}
=\frac{N}{15}\cdot \frac{8}{30}
=\frac{4}{225}N.
]
Hence, to avoid containing an entire lcm triangle, a set (A\subseteq{1,\dots,N}) must omit at least one element from each of these (\sim \frac{4}{225}N) disjoint triangles, giving
[
|A|\le \\(1-\frac{4}{225}+o(1)\\)N=\\(\frac{221}{225}+o(1)\\)N.
]
Therefore, the statement in your question **is true** whenever
[
\epsilon>\frac{221}{225}\approx 0.9822.
]
([Erdős Problems][2])

This is far from settling the “every fixed (\epsilon>0)” question, but it shows the phenomenon is forced for sufficiently high density.

#### 2) There are fairly large triangle-free sets, but still **density $0$**

There are constructions of lcm-triangle-free sets (A\subseteq{1,\dots,N}) of size much larger than (N/\log N), for example using carefully chosen families of $k$-almost primes; one can get
[
|A|\gg \frac{N(\log\log N)^{f(N)}}{\log N}
\quad\text{for some } f(N)\to\infty,
]
as sketched in the Erdős Problems discussion. ([Erdős Problems][1])

This shows the best-known lower bounds are **sublinear** (so they don’t contradict the conjectured “yes”), but they also show the problem is subtle: you can avoid lcm triangles in quite large sets, just not known at *linear* size (\epsilon N) for a fixed (\epsilon>0).

#### 3) For 4 elements, the analogous statement is **false**

Erdős showed that if you ask for **four** elements with the same pairwise lcm, one can avoid that even with (|A|\gg N) (linear-size sets). This is part of the motivation for focusing on the $3$-element case. ([Erdős Problems][1])

---

### Bottom line

* For general fixed (\epsilon>0): **unknown / open**. ([Erdős Problems][1])
* For (\epsilon>221/225): **yes**, by a simple disjoint-triangle counting argument. ([Erdős Problems][2])
* There are **large** (but sublinear-density) constructions with no such triple. ([Erdős Problems][1])

If you want, I can also write out the “$\\{txy,txz,tyz\\}$ with (\gcd(x,y)=\gcd(x,z)=\gcd(y,z)=1)” characterization as a clean lemma (it’s a handy way to search for or rule out examples).

[1]: https://www.erdosproblems.com/536 "
  
    Erdős Problem #536
  
"
[2]: https://www.erdosproblems.com/forum/discuss/536 "

    Erdős Problem #536 - Discussion thread

"
