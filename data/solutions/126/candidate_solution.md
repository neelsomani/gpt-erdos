This is **not known**. It is an old Erdős–Turán problem and it is still listed as open.

What is known is only “log size” lower bounds.

* Erdős and Turán (1934) proved
  [
  \log n \ll f(n) \ll \frac{n}{\log n},
  ]
  where the upper bound is just from taking (A={1,2,\dots,n}). ([Erdős Problems][1])

* A later result of Bing‑Ling Wu (2019) sharpened the constant in the **lower** bound: if
  [
  \prod_{1\le i<j\le n}(a_i+a_j)
  ]
  has at most (k) distinct prime divisors, then (n\le 2^k). Equivalently,
  [
  f(n)\ \ge\ \lceil \log_2 n\rceil.
  ]
  This is still only (\asymp \log n). ([Springer][2])

So at present we only know
[
\log_2 n \ \le\ f(n)\ \le\ \pi(2n)\sim \frac{2n}{\log n},
]
and nothing close to proving (f(n)/\log n\to\infty).

A useful way to think about your question is: “how large can a set be if *all* pairwise sums use only (k) primes?” The best general bounds known are still essentially exponential in (k), which matches only a (\log n) lower bound for (f(n)). In a closely related **two-set** version (products over (a\in A, b\in B)), the best general lower bound is also (\gg \log k), and in that setting stronger growth is known to be impossible in general, which is one reason people suspect the one-set problem might also be closer to (\log n) than to something much larger (but this does **not** settle your exact question). ([MathOverflow][3])

[1]: https://www.erdosproblems.com/126 "
  
    Erdős Problem #126
  
"
[2]: https://link.springer.com/content/pdf/10.1007/s10986-019-09441-0.pdf "Sumsets with restricted number of prime factors | Lithuanian Mathematical Journal | Springer Nature Link"
[3]: https://mathoverflow.net/questions/129645/composing-two-term-sums-from-the-same-primes "nt.number theory - Composing two-term sums from the same primes - MathOverflow"
