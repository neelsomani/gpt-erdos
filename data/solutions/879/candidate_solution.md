Both questions are **open** as stated (this is **Erdős problem #879**). What *is* known is the following. ([Erdős Problems][1])

## 1) Is (G(n) > H(n)-n^{1+o(1)}) true?

### Status

Unconditionally, this is **not known**. Erdős and van Lint proved the best general bounds recorded in the literature summary:

[
H(n)-n^{3/2-o(1)} < G(n) < H(n),
\qquad\text{and}\qquad
\frac{H(n)-G(n)}{n}\to\infty.
]
([Erdős Problems][1])

They also proved the desired-looking lower bound
[
G(n)>H(n)-n^{1+o(1)}
]
**conditionally**, assuming what they describe as “plausible (but hopeless)” hypotheses on prime distribution. ([Erdős Problems][1])

### Why $H(n)$ is the “right” upper bound

Every composite (a\le n) has some prime divisor (\le \sqrt n). In an admissible set, each prime can divide at most one chosen element, so for each prime (p\le\sqrt n) there is at most one chosen number divisible by $p$, and it contributes (\le n). Summing that over (p\le\sqrt n) gives the (n\pi(\sqrt n)) term. The remaining admissible elements that have no prime factor (\le \sqrt n) must be primes (or 1), so their contribution is at most (\sum_{p<n} p). This yields (G(n)\le H(n)).

### Heuristic expectation

A standard heuristic is that the “gap” $H(n)-G(n)$ should be about
[
\asymp n\sum_{p\le \sqrt n}\frac1p \sim n\log\log n,
]
which is indeed (n^{1+o(1)}). Very roughly: to make one “$p$-number” close to $n$, you want something like (p\cdot q) [[nomath]](or $p^e q$)[[/nomath]] with (q\approx n/p), and you “pay” by not being able to include $q$ itself as a prime, and by the shortfall $n-pq$. Summing those costs over many (p\le\sqrt n) leads naturally to an (n\log\log n) scale. This is consistent with the conditional result and with computations, but it remains unproved in full generality.

### Numerical sanity checks [[nomath]](from computed $G(n)$)[[/nomath]]

OEIS A186736 records $G(n)$ and gives explicit maximizing sets for some $n$. ([OEIS][2])
For instance:

* (G(30)=193), achieved by $\\{1,11,13,17,19,23,25,27,28,29\\}$. ([OEIS][2])
  Here (H(30)=219), so (H(30)-G(30)=26).
* (G(51)=453), achieved by $\\{1,13,19,23,25,29,31,37,41,43,44,47,49,51\\}$. ([OEIS][2])
  Here (H(51)=532), so (H(51)-G(51)=79).

The gap is already noticeably larger than a constant multiple of $n$ but much smaller than (n^{3/2}), which is exactly the range the proven bounds permit.

## 2) Must a maximizing admissible set contain an integer with (\ge k) prime factors?

### Status

* For $k=2$: **Yes** for all sufficiently large $n$ (Erdős–van Lint). ([Erdős Problems][1])
  In other words, eventually an optimal set cannot consist solely of primes (and 1); it must contain at least one composite.
* For **every fixed (k\ge 3)**: **open** as far as the standard references/summaries report. ([Erdős Problems][1])

### Remarks / intuition

Computational maximizers very quickly include numbers with several prime factors [[nomath]](e.g. at $n=30$, the example maximizer contains $28=2^2\cdot 7$ and $27=3^3$)[[/nomath]]. ([OEIS][2])
Heuristically, using higher prime powers [[nomath]](or $p^e\cdot q$ with $e$ growing slowly)[[/nomath]] can “move” the sacrificed cofactor $q$ downward while still keeping the product near $n$, which makes it plausible that optimal constructions might force some element to have many prime factors. Turning that intuition into a proof for arbitrary fixed $k$ is exactly what remains open.

---

If you want, I can also sketch the usual “matching” viewpoint [[nomath]](pairing small primes $p\le \sqrt n$ with large primes near $n/p$)[[/nomath]] that leads to the (n\log\log n) heuristic and explains why the first inequality is believed to be true under prime-gap–type hypotheses.

[1]: https://www.erdosproblems.com/latex/879 "
  
    Erdős Problems
  
"
[2]: https://oeis.org/A186736 "A186736 - OEIS"
