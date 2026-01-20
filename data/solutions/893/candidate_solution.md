No finite limit.

In fact, Kovač and Luca (2025) proved the ratio is **unbounded**:
[
\limsup_{n\to\infty}\frac{f(2n)}{f(n)}=\infty,
]
so $f(2n)/f(n)$ cannot converge to any real number. ([arXiv][1])

A (very) rough sketch of why unboundedness happens is:

* Let (\omega(m)) be the number of **distinct** prime divisors of $m$. Always (\tau(m)\ge 2^{\omega(m)}).
* By the Bang–Zsigmondy primitive prime divisor theorem, for each divisor (d\mid k) (with a tiny exceptional set), (2^d-1) contributes a “new” prime divisor, giving
  [
  \omega(2^k-1)\ \ge\ \tau(k)-2,
  ]
  hence
  [
  \tau(2^k-1)\ >\ 2^{\omega(2^k-1)}\ >\ \tfrac14,2^{\tau(k)}.
  ]
  Summing this yields (f(n) \ge \tfrac14 f'(n)) where (f'(n):=\sum_{k\le n}2^{\tau(k)}). ([arXiv][1])
* They then show (f'(2n)/f'(n)\to\infty) by choosing $k$ near highly–composite numbers [[nomath]](where $\tau(k)$ jumps a lot)[[/nomath]], and this forces (f(2n)/f(n)) to have arbitrarily large spikes, hence unboundedness. ([arXiv][1])

It’s also worth noting that a naive “random integer” heuristic would suggest a stable limit [[nomath]](they even compute it would be $4$)[[/nomath]], but that heuristic turns out to be misleading because $f$ has occasional huge jumps. ([arXiv][1])

Finally, Kovač–Luca also give **conditional** theorems implying the stronger conclusion
[
\frac{f(2n)}{f(n)}\to\infty,
]
and provide numerical evidence supporting this divergence, but this divergence is not proved unconditionally. ([arXiv][1])

[1]: https://arxiv.org/pdf/2506.04883 "On the number of divisors of Mersenne numbers"
