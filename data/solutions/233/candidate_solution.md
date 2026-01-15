This is a famous **Erdős problem** (Erdős Problem #233), and **the bound you ask for is currently open** (i.e., no proof is known as of the latest references I can find). ([Erdős Problems][1])

What *is* known (and what you *can* prove right away) is the matching **lower bound**, and there are also weaker **upper bounds** (conditional and unconditional). I’ll lay these out clearly.

---

## 1) Why the conjectured upper bound would be best possible

Let
[
d_n = p_{n+1}-p_n,\qquad S(N):=\sum_{n\le N} d_n^2.
]
By Cauchy–Schwarz,
[
\Big(\sum_{n\le N} d_n\Big)^2 \le N\sum_{n\le N} d_n^2 = N S(N),
]
so
[
S(N)\ge \frac{1}{N}\Big(\sum_{n\le N} d_n\Big)^2.
]
But (\sum_{n\le N} d_n = p_{N+1}-p_1 = p_{N+1}-2). Using the prime number theorem estimate (p_{N+1}\asymp N\log N), ([arXiv][2]) we get
[
S(N)\ \gg\ \frac{(N\log N)^2}{N}\ =\ N(\log N)^2.
]
So the desired upper bound
[
S(N)\ \ll\ N(\log N)^2
]
would be **sharp up to constants**, i.e. it would imply (S(N)\asymp N(\log N)^2). This “correct-order” upper bound is exactly what makes the problem hard. ([Erdős Problems][1])

---

## 2) Status: it’s open

The Erdős Problems database explicitly lists your statement as **OPEN**, and notes that even conditional results are significantly weaker (in log-powers). ([Erdős Problems][1])

---

## 3) Best known results in the literature (what we can say instead)

### Conditional on the Riemann Hypothesis (RH)

* **Cramér (1936)** proved (on RH) an upper bound of the shape
  [
  \sum_{n\le N} d_n^2 = O!\big(N(\log N)^4\big).
  ]
* **Selberg (1943)** (still on RH) obtained a related improvement in a weighted form:
  [
  \sum_{n\le N}\frac{d_n^2}{n} \ll (\log N)^4.
  ]
  These are recorded on the Erdős Problem #233 page. ([Erdős Problems][1])

Also, in terms of primes up to (x), Selberg (assuming RH) is cited as showing
[
\sum_{p_n\le x} d_n^2 \ll x(\log x)^3,
]
which is consistent with the (N(\log N)^4) shape after translating (x\sim N\log N). ([arXiv][2])

### Best known unconditional bounds

Unconditionally, the strongest bound I can point to from the sources above is due to **Peck (1996)** (rediscovered by **Maynard (2012)**):
[
\sum_{p_n\le x} (p_{n+1}-p_n)^2 \ll_\varepsilon x^{5/4+\varepsilon}
\quad (x\ \text{large}).
]
([arXiv][2])

Translating this into an (N)-statement using (p_N\asymp N\log N), you get a rigorous (but much weaker than Erdős’s conjecture) estimate like
[
\sum_{n\le N} d_n^2 \ \ll_\varepsilon\ (N\log N)^{5/4+\varepsilon}.
]
This is far from (N(\log N)^2), but it is the kind of unconditional “(L^2)” control currently available. ([arXiv][2])

---

## 4) What proving (S(N)\ll N(\log N)^2) would mean

The conjectured bound is equivalent to saying the **root mean square** prime gap among the first (N) gaps is (O(\log N)), i.e. the same scale as the *average* prime gap. That’s a very strong regularity statement about primes in short intervals, and it’s why Erdős posed it as a problem—progress here tends to require genuinely new ideas. ([Erdős Problems][1])

---

If you tell me what tools you’re allowed to assume (e.g. RH, Bombieri–Vinogradov, Brun–Titchmarsh, Selberg sieve, etc.), I can tailor the strongest *provable* bound in that framework and show how it’s derived.

[1]: https://www.erdosproblems.com/233 "https://www.erdosproblems.com/233"
[2]: https://arxiv.org/pdf/1201.1787 "https://arxiv.org/pdf/1201.1787"
