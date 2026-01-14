This is **exactly** the (still open) **Erdős conjecture on arithmetic progressions** (often called the **Erdős–Turán conjecture**):

> If (A\subseteq \mathbb N) and (\sum_{n\in A}\frac1n=\infty), must (A) contain arithmetic progressions of every finite length?

As of **January 2026**, the general question is **unknown**. ([MathOverflow][1])

## What is known

### 1) If (A) has positive density, then yes

If (A) has positive upper (natural) density, then (A) contains arbitrarily long arithmetic progressions by **Szemerédi’s theorem**. ([Wikipedia][2])
But (\sum_{n\in A}1/n=\infty) is **much weaker** than positive density, so Szemerédi does not apply directly.

### 2) The primes are a famous special case

(\sum_{p\ \text{prime}} 1/p = \infty), and the primes contain arbitrarily long arithmetic progressions by **Green–Tao**. ([Annals of Mathematics][3])
So the conjecture is true for that specific “very sparse but structured” set.

### 3) The case of **3-term** progressions is now settled: **yes**

A major breakthrough of **Bloom–Sisask (2020)** proves that if (A\subset{1,\dots,N}) has **no nontrivial 3-term AP**, then
[
|A| \ll \frac{N}{(\log N)^{1+c}}
]
for some absolute (c>0). They explicitly note this gives the *first nontrivial case* of Erdős’s conjecture. ([arXiv][4])

From this one can deduce (by a standard dyadic decomposition argument) that **any 3AP-free infinite set has a convergent reciprocal sum**, hence:

[
\sum_{n\in A}\frac1n=\infty \quad\Longrightarrow\quad A\text{ contains (indeed infinitely many) 3-term APs.}
]

This is also reflected in later discussions of “(k)-free” sets and their harmonic sums (where the (k=3) case is singled out as the one where finiteness is known). ([arXiv][5])

## What remains open

For **4-term arithmetic progressions and longer**, the conjecture is still open: we do **not** know whether (\sum_{n\in A}1/n=\infty) forces (A) to contain arbitrarily long APs. ([MathOverflow][1])

In fact, current work includes constructing (k)-AP-free sets with **very large (but still finite)** harmonic sums, which illustrates how subtle the problem is beyond (k=3). ([arXiv][5])

So the best accurate answer is:

* **For length 3:** yes (now a theorem). ([arXiv][4])
* **For arbitrarily long APs:** **open problem** (Erdős–Turán / Erdős conjecture on arithmetic progressions). ([MathOverflow][1])

[1]: https://mathoverflow.net/questions/489375/why-is-erd%C5%91s-conjecture-on-arithmetic-progressions-not-discussed-much-and-is-t?utm_source=chatgpt.com "Why is Erdős' conjecture on arithmetic progressions not ..."
[2]: https://en.wikipedia.org/wiki/Szemer%C3%A9di%27s_theorem?utm_source=chatgpt.com "Szemerédi's theorem"
[3]: https://annals.math.princeton.edu/wp-content/uploads/annals-v167-n2-p03.pdf?utm_source=chatgpt.com "The primes contain arbitrarily long arithmetic progressions"
[4]: https://arxiv.org/abs/2007.03528?utm_source=chatgpt.com "Breaking the logarithmic barrier in Roth's theorem on arithmetic progressions"
[5]: https://arxiv.org/html/2203.06045v2 "Integer Sets of Large Harmonic Sum which Avoid Long Arithmetic Progressions"
