Let

[
f(k)\ :=\ \sup\\{\sum_{n\in A}\frac1n:\ A\subset\mathbb N,\ A\text{ contains no }k\text{-term arithmetic progression}\\}.
]

Two different issues are mixed into “estimate $f(k)$”:

1. **Is $f(k)$ even finite?**
2. **If it is finite, how fast does it grow with $k$?**

## 1) Finiteness

* For **(k=3)** it is known that (f(3)<\infty). This follows from Bloom–Sisask’s “logarithmic barrier” improvement to Roth’s theorem: if (A\subset{1,\dots,N}) has no nontrivial 3-term AP, then (|A|\ll N/(\log N)^{1+c}) for some absolute (c>0). That exponent (>1) is strong enough to force (\sum_{n\in A}1/n) to converge for every 3-AP-free (A). ([arXiv][1])

* For **(k\ge 4)**, the finiteness of (f(k)) is **open**. In fact, “(f(k)<\infty) for every (k)” is equivalent to the classical Erdős–Turán (Erdős) conjecture that any set with (\sum_{n\in A}1/n=\infty) must contain arbitrarily long arithmetic progressions. ([arXiv][2])

So at the moment:

* $f(3)$ is finite, but not known precisely.
* For (k\ge 4), we do not know whether $f(k)$ is finite at all. ([arXiv][2])

## 2) Lower bounds (how large (f(k)) can be)

There are strong constructions showing $f(k)$ must grow at least like (k\log k):

* **Berlekamp (1968):**
  [
  f(k)\ \ge\ \frac{\log 2}{2},k.
  ]
* **Gerver (1977):**
  [
  f(k)\ \ge\ (1-o(1)),k\log k\quad\text{as }k\to\infty.
  ]
  These are standard quoted lower bounds for this problem. ([Erdős Problems][3])

For small $k$, the best published numerical lower bounds include:

* (f(3)\ge 3.00849) (Wróblewski, 1984),
* (f(4)\ge 4.43975) (Walker, 2025). ([Erdős Problems][3])

## 3) The “trivial” link to van der Waerden numbers

Let (W(k)=W(2,k)) be the 2-color van der Waerden number. By definition, there exists a 2-coloring of ({1,\dots,W(k)-1}) with **no monochromatic** (k)-term AP. Let (A) be the red set and (B) the blue set. Then both (A) and (B) are (k)-AP-free, and

[
\sum_{n\in A}\frac1n\ +\ \sum_{n\in B}\frac1n\ =\ H_{W(k)-1},
]

so one color class has harmonic sum at least (H_{W(k)-1}/2). Therefore

[
f(k)\ \ge\ \frac12,H_{W(k)-1}\ \ge\ \frac12\log W(k).
]

This is exactly why one always has

[
\frac{f(k)}{\log W(k)}\ \ge\ \frac12.
]

([Erdős Problems][3])

## 4) Your limit question

You asked whether

[
\lim_{k\to\infty}\frac{f(k)}{\log W(k)}=\infty.
]

This is **open**. What is known is much weaker: we only have the universal lower bound (\ge 1/2) above, and (importantly) **even improving** that “$1/2$” to *any fixed constant bigger than $1/2$* is currently open. ([Erdős Problems][3])

So, as of now, nobody can prove that the ratio stays above $0.5001$ for all large $k$, let alone that it goes to infinity.

## Summary of the best “estimate” we can honestly give today

* $f(3)$ is finite (but its exact value is unknown). ([arXiv][1])
* For (k\ge 4), it is not even known whether $f(k)$ is finite; this is tied to the Erdős–Turán conjecture. ([arXiv][2])
* Unconditionally,
  [
  f(k)\ \ge\ (1-o(1)),k\log k
  \quad\text{and}\quad
  f(k)\ \ge\ \tfrac12\log W(k).
  ]
  ([Erdős Problems][3])
* The limit (\displaystyle \lim_{k\to\infty} f(k)/\log W(k)) is unknown; even showing it is (>1/2) is open. ([Erdős Problems][3])

[1]: https://arxiv.org/abs/2007.03528 "[2007.03528] Breaking the logarithmic barrier in Roth's theorem on arithmetic progressions"
[2]: https://arxiv.org/html/2203.06045v2 "Integer Sets of Large Harmonic Sum which Avoid Long Arithmetic Progressions"
[3]: https://www.erdosproblems.com/forum/thread/169 "

    Erdős Problem #169 - Discussion thread

"
