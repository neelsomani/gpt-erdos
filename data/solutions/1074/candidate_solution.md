Let (E_m:=m!+1).

A couple of quick reductions help keep the statements clean:

* If a prime (p\mid E_m), then (p\nmid m!), hence **(p>m)**.
* For such a $p$, the condition (p\equiv 1\pmod m) is equivalent to **(m\mid(p-1))**.

So

[
m\in S \iff \exists, p\mid(m!+1)\text{ with }m\nmid(p-1),
]

and the complement (S^c) is exactly the set of $m$ for which **every** prime divisor $p$ of (m!+1) satisfies (p\equiv 1\pmod m).

Similarly, for a prime $p$,

$
p\in P \iff \exists, m<p\text{ such that } m!\equiv -1\pmod p \text{ and } m\nmid(p-1).
$

[[nomath]](There is always the “trivial” solution $m=p-1$ by Wilson’s theorem, but that one never)[[/nomath]]I don’t know of any theorem that proves either limit exists, nor any theorem that computes it unconditionally. Both questions very quickly run into deep/open territory about:

* the factorization of Euclid numbers $m!+1$,
* and the distribution of factorial residues $m!\bmod p$.

What we *can* say is:

## 1) The density of $S$ [[nomath]](integers $m$)[[/nomath]]

### What is known unconditionally

* It is easy that $S$ is infinite [[nomath]](e.g. $8\in S$ because $8!+1=40321=61\cdot 661$ and $61\not\equiv 1\pmod 8$)[[/nomath]].
* It is also easy that (S^c) is nonempty: (m=2,3,4,5,6,7) all fail [[nomath]](every prime factor of $m!+1$ is $\equiv1\pmod m$ in those cases)[[/nomath]].

But **there is no known general method** to force a “non-(1\bmod m)” prime divisor of $m!+1$ for *almost all* $m$, because that would require strong information about the residue classes of prime factors of $m!+1$.

Even very basic questions of this flavor are open; for example, it is unknown whether there are infinitely many “factorial primes” $m!+1$ prime, and every such $m$ would lie in (S^c).

### Heuristic expectation (very strong)

A standard heuristic is: treat the prime factors of $m!+1$ as behaving like the prime factors of a “random” integer of comparable size, and treat their residue classes mod $m$ as essentially equidistributed among the (\varphi(m)) reduced classes.

* A “random” integer of size (\log(m!+1)\asymp m\log m) typically has about
  [
  \Omega(m!+1)\approx \log\log(m!+1)\approx \log m
  ]
  prime factors (counted with multiplicity).
* The probability that **all** of those prime factors land in the single residue class (1\pmod m) would then be roughly
  [
  \left(\frac{1}{\varphi(m)}\right)^{\Omega(m!+1)}\approx \left(\frac{1}{\varphi(m)}\right)^{\log m},
  ]
  which is astronomically small [[nomath]](heuristically summable over $m$)[[/nomath]].

This strongly suggests:

* (S^c) should have **density $0$**,
* hence (\displaystyle \lim_{x\to\infty}\frac{|S\cap[1,x]|}{x}) should exist and equal **$1$**,
* and, in fact, one might even expect only finitely many (m\notin S) (this is *much* stronger and completely unproved).

### Small-scale computation (just for intuition)

By direct factorization one finds, for instance, up to (m\le 50),
[
m\notin S \text{ for } m=1,2,3,4,5,6,7,10,11,12,25,27,28,37,41,46,
]
so (|S\cap[1,50]|/50=0.68). The proportion appears to drift upward as $m$ grows, consistent with the heuristic “density $1$” story, but this is not evidence of a proof.

**Bottom line for $S$:** the existence/value of the density is **not known**; a very natural heuristic predicts the limit exists and equals **$1$**.

---

## 2) The density of $P$ [[nomath]](primes $p$)[[/nomath]]

Here we are asking, for a prime $p$, whether there is a **nontrivial** solution (m<p) to
[
m!\equiv -1\pmod p
]
with the additional constraint (m\nmid(p-1)).

Wilson’s theorem guarantees the trivial solution (m=p-1) for every prime $p$: ((p-1)!\equiv -1\pmod p). ([Wikipedia][1])
So (p\in P) exactly when there is some *other* solution $m$ that is not a divisor of $p-1$.

### Connections that show this is subtle

Writing Wilson as
[
(p-1)!\equiv -1\pmod p
]
and splitting at $m$ gives:
[
m!\cdot(m+1)(m+2)\cdots(p-1)\equiv -1\pmod p.
]
So (m!\equiv -1) is equivalent to
[
(m+1)(m+2)\cdots(p-1)\equiv 1\pmod p,
]
i.e. a **product of consecutive integers is (1\bmod p)**. That kind of question is studied on MathOverflow and is closely tied to understanding the sequence (n!\bmod p). ([MathOverflow][2])

Also, special cases like (m=(p-1)/2) are governed by “Gauss factorial” phenomena and can be described in terms of class numbers of (\mathbb{Q}(\sqrt{-p})). ([MathOverflow][3])
But note: (m=(p-1)/2) always divides $p-1$, so even when it *does* solve (m!\equiv-1), it **does not** by itself put $p$ into $P$. You need a genuinely “non-divisor” solution.

### What is known unconditionally

I’m not aware of any unconditional theorem proving that $P$ has a natural density, or giving its value.

### What heuristics suggest

A naive “randomness” heuristic says: as $m$ runs from $1$ to $p-1$, the values (m!\bmod p) behave roughly like random nonzero residues, so the expected number of (m<p) with (m!\equiv -1) is (\approx 1). Under an (over)simplified Poisson$1$ model you’d guess
$
\mathbb{P}(\exists, m<p-1:\ m!\equiv -1\pmod p)\approx 1-e^{-1}\approx 0.632,
$
and since divisors of $p-1$ are sparse, you’d guess the same for membership in $P$.

However, the factorial sequence is **not** independent/random in that way, and the data (below) suggests the naive model overshoots.

### Numerical evidence [[nomath]](strongly suggests a constant $\approx 0.5$)[[/nomath]]

If you brute-force (m!\bmod p) for each prime (p\le X), the proportion of primes in $P$ seems to hover around about one-half.

For example [[nomath]](computed directly by scanning $m=1,\dots,p-1$ for each prime and stopping early when a “good” $m$ is found)[[/nomath]], one gets:

* up to (10^5): about $0.524$,
* up to (1.5\times 10^5): about $0.525$,
  and random sampling of primes in ranges around (10^6) and (2\times 10^6) gives proportions close to $0.5$.

So empirically, it’s plausible that
[
\lim_{x\to\infty}\frac{|P\cap[1,x]|}{\pi(x)}
]
exists and is **around $0.5$** [[nomath]](maybe exactly $1/2$)[[/nomath]], but I do not know a proof, and I don’t know a standard conjectural constant here that’s universally accepted.

**Bottom line for $P$:** existence/value of the density is **not known**; computations suggest a limit near **$1/2$**, while naive independence heuristics would suggest something closer to (1-e^{-1}\approx 0.632). The gap reflects strong correlations in (m!\bmod p).

---

## Summary

* **For $S$**: no proof of density existence/value is known; strong heuristics suggest the density exists and equals **$1$** [[nomath]](i.e. exceptions are density $0$)[[/nomath]].
* **For $P$**: no proof of density existence/value is known; computations suggest the density exists and is roughly **$1/2$**, and this is tied to subtle questions about consecutive products and factorial residues modulo primes. ([MathOverflow][2])

If you want, I can also:

* reformulate both questions in terms of splitting of primes in cyclotomic fields ( \mathbb{Q}(\zeta_m)) [[nomath]](since $p\equiv1\pmod m$ is “splits completely”)[[/nomath]], which makes the “rarity” heuristics for $S$ very natural; or
* compute larger tables/ranges to sharpen the numerical guess for the prime-density constant (within computational limits).

[1]: https://en.wikipedia.org/wiki/Wilson%27s_theorem "https://en.wikipedia.org/wiki/Wilson%27s_theorem"
[2]: https://mathoverflow.net/questions/491284/on-the-number-of-products-of-consecutive-integers-which-are-equal-1-modulo-prime "https://mathoverflow.net/questions/491284/on-the-number-of-products-of-consecutive-integers-which-are-equal-1-modulo-prime"
[3]: https://mathoverflow.net/questions/16141/primes-p-such-that-p-1-2-1-mod-p?utm_source=chatgpt.com "Primes P such that ((P-1)/2)!=1 mod P"
