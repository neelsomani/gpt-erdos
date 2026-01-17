Let

$
\frac ab=\frac1{n_1}+\cdots+\frac1{n_k}\qquad (1<n_1<\cdots<n_k)
$

and write $N(a,b)$ for the minimal such $k$, and

$
N(b):=\max_{1\le a<b}N(a,b).
$

This quantity [[nomath]](often denoted $L(b)$ in the literature)[[/nomath]] is a classical Erdős problem.

## What is known (best general bounds)

As of the current literature, the sharpest general bounds are

[
\boxed{\ \log\log b\ \ll\ N(b)\ \ll\ \sqrt{\log b}\ }.
]

More precisely:

* Erdős (1950) proved the two-sided estimate
  [
  \log\log b \ll N(b)\ll \frac{\log b}{\log\log b}.
  ]
  ([Erdős Problems][1])

* Vose (1985) improved the upper bound to
  [
  N(b)\ll \sqrt{\log b},
  ]
  and this remains the best published general upper bound that is commonly cited as “current best”. ([Erdős Problems][1])

There is also an “average” lower bound [[nomath]](for fixed $b$)[[/nomath]]:
[
\frac1b\sum_{1\le a<b} N(a,b)\gg \log\log b,
]
which in particular forces (N(b)\gg\log\log b). ([Erdős Problems][1])

## Is (N(b)\ll \log\log b) true?

This is **conjectured**, going back to Erdős, but it is **open**:

[
\text{Conjecture: }\quad N(b)\ll \log\log b.
]

It is explicitly recorded as Erdős Problem #304, and is described as open there; it is also reiterated in recent notes discussing the state of the art. ([Erdős Problems][1])

If true, this would be essentially best possible up to constant factors, because we already know (N(b)\gg \log\log b). ([Erdős Problems][1])

## Why the upper bounds look like this (brief idea)

A standard mechanism behind many constructive upper bounds is:

* Try to force all denominators (n_i) to divide a common multiple (bm).
* If (n_i\mid bm), write (n_i=bm/d_i). Then
  [
  \frac1{n_i}=\frac{d_i}{bm},
  ]
  and the Egyptian fraction identity becomes
  [
  \frac ab=\sum_i\frac{d_i}{bm}
  \quad\Longleftrightarrow\quad
  am=\sum_i d_i.
  ]
  So one reduces to: **choose $m$ so that every $am$ ((1\le a<b)) can be written as a sum of few distinct divisors of $bm$**.

Vose’s (\sqrt{\log b}) bound comes from choosing $m$ so that $bm$ has a very “dense” divisor structure (many divisors with small ratios), allowing such divisor-sum representations with relatively few terms. ([arXiv][2])

Getting all the way down to (\ll\log\log b) would require substantially stronger uniform control on such divisor-sum phenomena than what current methods provide—hence the conjecture remains open.

---

So, the best “estimate” currently is the range
[
\log\log b \ \ll\ N(b)\ \ll\ \sqrt{\log b},
]
and **(N(b)\ll\log\log b)** is a well-known Erdős conjecture but **not proved**. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/304 "
  
    Erdős Problem #304
  
"
[2]: https://arxiv.org/pdf/2512.22083 "The smallest denominator not contained in a unit fraction decomposition of $1$ with fixed length"
