Here are the main structural facts that sit behind all three questions, and what is (and isn’t) currently known.

This function (with essentially the same range for (k), by symmetry) was introduced by Erdős–Szekeres in 1978, and the three bullets you list are exactly the three questions they raise; the problem is still listed as open on the Erdős Problems site, with later discussion (incl. Tao/Cambie). ([Rényi Institute][1])

---

## Two basic lemmas you can use immediately

Write

* $p(n)$ = the smallest prime factor of $n$,
* $P(n)$ = the largest prime factor of $n$ (your notation),
* and let $v_p(\cdot)$ be the $p$-adic valuation.

### Lemma A (a universal lower bound)

For all integers (n\ge 2) and (1\le k\le n-1),
[
\frac{n}{\gcd(n,k)} \mid \binom{n}{k}.
]
Hence
$
\gcd(n,\binom{n}{k})\ \ge\ \frac{n}{\gcd(n,k)}\ > 1
\quad\text{for } 1<k< n,
$
so for composite $n$,
$
f(n)\ge p(n).
$

*Proof sketch.* Let (d=\gcd(n,k)), write (n=dn_1,\ k=dk_1) with (\gcd(n_1,k_1)=1). Using
(\binom{n}{k}=\frac{n}{k}\binom{n-1}{k-1}=\frac{n_1}{k_1}\binom{n-1}{k-1}),
integrality forces (k_1\mid \binom{n-1}{k-1}), hence (n_1=n/d\mid \binom{n}{k}).

This lower bound (f(n)\ge p(n)) is exactly $6$ in Erdős–Szekeres. ([Rényi Institute][1])

---

### Lemma B (a very useful exact evaluation at prime(-power) indices)

If $p$ is prime and (p^a\mid n) [[nomath]](with $a\ge 1$)[[/nomath]] and (1\le p^a\le n-1), then
[
\gcd\left(n,\binom{n}{p^a}\right)=\frac{n}{p^a}.
]
In particular, if (p\mid n) then
[
\gcd\left(n,\binom{n}{p}\right)=\frac{n}{p},
]
so taking (p=P(n)) gives the always-available upper bound
[
f(n)\ \le\ \frac{n}{P(n)}.
]

*Why the gcd is exactly (n/p^a).* Write (n=p^a m). Then
[
\binom{n}{p^a}=\frac{n}{p^a}\binom{n-1}{p^a-1}=m\binom{n-1}{p^a-1}.
]
One checks that (p\nmid \binom{n-1}{p^a-1}) [[nomath]](e.g. by Lucas’ theorem: in base $p$, $n-1$ ends with $a$ digits $p-1$, same as $p^a-1$, giving $\binom{n-1}{p^a-1}\equiv 1\pmod p$)[[/nomath]]. Therefore the $p$-adic valuation of (\binom{n}{p^a}) is exactly (v_p(n)-a), so the common $p$-power in $n$ and (\binom{n}{p^a}) is reduced by precisely $a$, i.e. the gcd is (n/p^a).

This “choose a prime power (j=p^a)” trick is exactly how Erdős–Szekeres obtain their upper bounds. ([Rényi Institute][1])

---

## 1) Characterise composite (n) with (f(n)=n/P(n))

What is **known cleanly**:

* **If (n=pq) with primes (p<q), then (f(n)=p=n/q=n/P(n)).**
  Upper bound: Lemma B with (k=q) gives a value (n/q=p).
  Lower bound: Lemma A gives (f(n)\ge p(n)=p).
  So equality holds. Erdős–Szekeres explicitly record this. ([Rényi Institute][1])

* **If (n=p^2), then (f(n)=p=n/P(n)).**
  More generally Erdős–Szekeres note that for a prime power (n=p^k), one has (f(p^k)=p). ([Rényi Institute][1])
  So for (k=2) this matches (n/P(n)=p); for (k\ge 3) it does **not** [[nomath]](since $n/P(n)=p^{k-1}$)[[/nomath]].

* There are “sporadic” further examples [[nomath]](they mention $f(30)=6$, i.e. $30/5$)[[/nomath]]. ([Rényi Institute][1])

What you can say **structurally** (easy necessary obstructions):

* If $n$ has some prime power divisor (p^a) with (p^a>P(n)) **and** (p^a\le n/2), then by Lemma B,
  [
  f(n)\ \le\ \gcd!\left(n,\binom{n}{p^a}\right)=\frac{n}{p^a}\ <\ \frac{n}{P(n)},
  ]
  so such an $n$ **cannot** satisfy (f(n)=n/P(n)).
  This rules out many (n) immediately [[nomath]](e.g. $40$: $8\mid 40$ and $8>5=P(40)$, giving $f(40)\le 40/8=5<8=40/5$)[[/nomath]].

What is **not known / no tidy classification**:

* Beyond the semiprime case (and the prime-square case as a special prime power), there is **no known clean characterisation**. The Erdős Problems discussion explicitly remarks how irregular the phenomenon is even among products of a fixed number of primes, and Tao comments that the first subquestion “seems hopeless” as a neat classification problem. ([Erdős Problems][2])

So the best honest state-of-play is:

* “(n=pq) (two primes) (\Rightarrow f(n)=n/P(n))” is proved.
* “prime powers (p^k): (f(p^k)=p)” is proved, hence equality with $n/P(n)$ happens only for (k=2).
* Beyond that, there are examples and necessary obstructions [[nomath]](such as the “large prime-power divisor $\le n/2$” test)[[/nomath]], but no full classification is currently available. ([Rényi Institute][1])

---

## 2) Infinitely many composite $n$ with (f(n) > n^{1/2})?

Two different thresholds matter:

### (a) “(\ge \sqrt n)” is easy and infinite

From (f(n)\ge p(n)), taking (n=p^2) gives
[
f(p^2)=p=\sqrt{p^2},
]
so there are infinitely many composite $n$ with (f(n)\ge \sqrt n). This is noted explicitly on the Erdős Problems page. ([Erdős Problems][2])

### (b) Strict “(> \sqrt n)” is the hard part

Erdős–Szekeres already give examples where strict inequality holds [[nomath]](they list $f(30)=6$, $f(70)=10$, $f(154)=14$, all with $f(n)>\sqrt n$)[[/nomath]], but they state they could not prove infinitely many. ([Rényi Institute][1])

As of the most recent public discussion I can find (Aug–Oct 2025 on the Erdős Problems thread), there is still **no unconditional infinite family** written down, though commenters express confidence it should be “yes” and propose **conditional / heuristic** families depending on unproved prime patterns or distribution assumptions. ([Erdős Problems][2])

Two such proposed (conditional/heuristic) constructions from that discussion:

* If there are infinitely many primes (q=2^k+3) with (k\equiv 4\pmod{20}), then (n=q(q+1)) should satisfy (f(n)=q+1), which is always (>\sqrt{q(q+1)}). ([Erdős Problems][2])
* A construction attributed there to Kadi Siigur: find primes $p,q$ in a dyadic interval with a congruence (pq\equiv 1\pmod{2^\ell}); then (n=2pq) is claimed to have (f(n)=2p), which can be (>\sqrt n) when (q<2p). Existence of infinitely many such pairs is argued heuristically. ([Erdős Problems][2])

So, with current knowledge:

* **Infinitely many with (f(n)\ge \sqrt n): yes (prime squares).**
* **Infinitely many with (f(n)>\sqrt n): appears open unconditionally.** ([Rényi Institute][1])

---

## 3) Is (f(n) \ll_A \dfrac{n}{(\log n)^A}) for every (A>0) and every composite $n$?

This is essentially the strong form of what Erdős–Szekeres suggest might be true after proving the “(n/\log n)” type upper bound; it remains open and is widely believed to be very hard.

What *is* known “for free” from Lemma B:

* For any prime power (p^a\le n/2) dividing $n$,
  [
  f(n)\le \frac{n}{p^a}.
  ]
  In particular, picking (p=P(n)) always gives
  [
  f(n)\le \frac{n}{P(n)}.
  ]

Erdős–Szekeres then argue (using distribution of primes/prime powers) that one can at least deduce a general upper bound of the shape
[
f(n)\ \le\ (1+o(1)),\frac{n}{\log n}
]
from these prime-power choices. ([Rényi Institute][1])

What is **not** known:

* The “for every $A$” bound you ask (a polylogarithmic saving of *arbitrary* order) is not proved in the sources above; it is posed as a conjectural strengthening in the original paper, and Tao’s comment on the modern thread emphasizes how difficult the third problem likely is. ([Rényi Institute][1])

So the best honest answer is:

* A bound like (f(n)\ll n/\log n) is supported by the prime-power argument and is stated in Erdős–Szekeres. ([Rényi Institute][1])
* The far stronger statement (f(n)\ll_A n/(\log n)^A) for **every** $A$ (uniformly over all composite (n)) remains open in the literature/discussion I can locate. ([Erdős Problems][2])

---

## Quick takeaway summary

* Always: (p(n)\le f(n)\le n/P(n)). [[nomath]](Both bounds are in Erdős–Szekeres; the upper bound comes from evaluating $\gcd(n,\binom{n}{p^a})$.)[[/nomath]] ([Rényi Institute][1])
* (f(n)=n/P(n)) is proved for (n=pq) (two primes), and holds for (n=p^2), but no full classification is known beyond such cases. ([Rényi Institute][1])
* Infinitely many $n$ with (f(n)\ge \sqrt n): yes (prime squares). Strict (>\sqrt n): examples exist, but infinitude appears open unconditionally. ([Rényi Institute][1])
* The “(n/(\log n)^A) for every $A$” bound is posed as a very strong conjectural direction and appears open; even experts in the thread consider it very hard. ([Erdős Problems][2])

[1]: https://www.renyi.hu/~p_erdos/1978-46.pdf "https://www.renyi.hu/~p_erdos/1978-46.pdf"
[2]: https://www.erdosproblems.com/forum/thread/700 "

    Erdős Problem #700 - Discussion thread

"