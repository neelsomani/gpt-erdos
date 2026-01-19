These three questions are exactly the “Translation Properties” problem posed by Erdős (1979), and (at least in the form you’ve stated) the first two parts are still open. 

## 1) Sums of two squares

**Unknown / open.** Erdős explicitly wrote that he did not know whether the integers representable as a sum of two squares have the translation property. 
The Erdős Problems database still lists this as open. ([Erdős Problems][1])

[[nomath]](Just for context: the set is multiplicative, characterized by “every prime $p\equiv 3 \pmod 4$ occurs to an even exponent”, but it does not fit into the “avoid multiples of a coprime family $B$” framework where sieve methods easily give the property.)[[/nomath]]

## 2) Integers composed only of primes from $P$ in a “dense” partition (P\sqcup Q)

Again **unknown / open** in general. Erdős specifically asked this case [[nomath]](two disjoint prime sets each having $\gg x/\log x$ primes $\le x$)[[/nomath]] and said he did not know. 

What *is* known (and is essentially what Erdős points out) is a much “thinner complement” regime:

* If you have a set (B\subset\mathbb N) of pairwise coprime integers with
  [
  \sum_{b<x}\frac1b=o(\log\log x),
  ]
  then (A={n: b\nmid n\ \forall b\in B}) has the translation property by Brun/sieve methods. 

But if $Q$ contains a positive proportion of primes, then (\sum_{q\in Q,\ q\le x} 1/q) diverges on the (\log\log x) scale, so the above “easy sieve” condition is far from being satisfied; that is exactly the difficult range Erdős flagged. 

## 3) (A={\text{squarefree integers}}): existence, and growth of the minimal (t_n)

### Existence (translation property)

**Yes, squarefree numbers have the translation property.** Erdős says it is “not hard” (via elementary sieve/Eratosthenes), and the Erdős Problems page records the same. 

One way to see why this sits in the “easy sieve” class: squarefree integers are precisely those not divisible by any (p^2), and the family ({p^2}) is pairwise coprime with (\sum_p 1/p^2<\infty). 

### Lower bound on the *minimal* (t_n)

Let (t_n) be the *smallest* shift that works for the first $n$ integers.

A useful necessary-condition lemma is:

> **Lemma.** Fix $n$ and suppose $t$ works [[nomath]](i.e. for all $1\le a\le n$, $a$ is squarefree iff $a+t$ is squarefree)[[/nomath]].
> If for some prime $p$ the squarefree numbers in $[1,n]$ hit **every nonzero residue class mod (p^2)**, then (p^2\mid t).

**Proof sketch:** If (t\not\equiv 0\pmod{p^2}), let (r\equiv -t\pmod{p^2}) with (r\not\equiv 0). By hypothesis pick a squarefree (a\le n) with (a\equiv r\pmod{p^2}). Then (a+t\equiv 0\pmod{p^2}), hence $a+t$ is not squarefree, contradicting the translation property for this $a$. ∎

So to force (p^2\mid t_n), it suffices to know that **every** nonzero class mod (p^2) contains at least one squarefree integer (\le n).

This is exactly a “least squarefree in an arithmetic progression” question. Let $n(q,a)$ be the least positive squarefree integer congruent to (a\pmod q) [[nomath]](typically with $(a,q)=1$)[[/nomath]]. Heath‑Brown proved the general upper bound
[
n(q,a)\ll_\varepsilon q^{3/2+\varepsilon}
]
for ((a,q)=1). ([ar5iv][2])

Apply this with (q=p^2). Then for every residue class (a\pmod{p^2}) with (p\nmid a) there is a squarefree representative (\le C_\varepsilon p^{3+2\varepsilon}). So as soon as
[
C_\varepsilon p^{3+2\varepsilon}\le n,
]
all the classes $(\bmod,p^2)$ that are coprime to $p$ are hit by squarefree numbers (\le n).

For the remaining nonzero classes (a\equiv p b\pmod{p^2}) with (p\nmid b), you can reduce to modulus $p$: any number of the form (p\cdot m) with (m\equiv b\pmod p), (p\nmid m), and $m$ squarefree will do. Heath‑Brown’s type of bound (or even weaker ones) for modulus $p$ gives such an $m$ well below $n/p$ for $p$ in the same range. ([ar5iv][2])

Putting this together yields:

* For any fixed (\delta>0), for all sufficiently large $n$, **every** prime
  [
  p\le n^{1/3-\delta}
  ]
  has the property that the squarefree numbers (\le n) hit every nonzero residue class mod (p^2). Hence (p^2\mid t_n) for all such $p$.

Therefore
[
t_n \ \ge\ \prod_{p\le n^{1/3-\delta}} p^2.
]
Taking logs and using (\sum_{p\le x}\log p = \vartheta(x)\sim x) gives
[
\log t_n \ \ge\ 2,\vartheta(n^{1/3-\delta}) \ =\ (2+o(1)),n^{1/3-\delta},
]
so
[
t_n \ \ge\ \exp!\big(c_\delta,n^{1/3-\delta}\big)
]
for some (c_\delta>0) and all large $n$.

### So: is (t_n>\exp(n^c)) true?

**Yes.** The argument above gives (t_n \ge \exp(n^{c})) for every (c<1/3) [[nomath]](eventually, for large $n$)[[/nomath]]. The original Erdős text conjectured some (\exp(n^c)) lower bound (and in particular “faster than polynomial”), but did not specify the best possible $c$. 

---

If you want, I can also spell out the reduction for the residue classes (a\equiv pb\pmod{p^2}) more explicitly, but the core point is: **current unconditional bounds for the least squarefree in a progression** [[nomath]](Heath‑Brown’s $q^{3/2+\varepsilon}$)[[/nomath]] already force a **stretched-exponential** lower bound on the minimal translation length for the squarefree set. ([ar5iv][2])

[1]: https://www.erdosproblems.com/675 "
  
    Erdős Problem #675
  
"
[2]: https://ar5iv.org/pdf/1605.03347 "[1605.03347] A note on the least squarefree number in an arithmetic progression"
