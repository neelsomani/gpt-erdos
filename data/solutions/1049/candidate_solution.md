Write (t>1) and expand each term as a geometric series:
[
\frac{1}{t^n-1}=\frac{t^{-n}}{1-t^{-n}}=\sum_{k\ge 1} t^{-nk}.
]
Summing over (n\ge 1) and regrouping by $m=nk$ gives
[
\sum_{n=1}^\infty \frac{1}{t^n-1}
=\sum_{n=1}^\infty\sum_{k\ge 1} t^{-nk}
=\sum_{m=1}^\infty \frac{|\\{(n,k):nk=m\\}|}{t^m}
=\sum_{m=1}^\infty \frac{\tau(m)}{t^m},
]
so this is indeed the classical Lambert series for the divisor function.

As for irrationality when $t$ is **rational** (>1):

* For **integer** (t\ge 2), Erdős proved in 1948 that the value is irrational. 
* Chowla conjectured that the same irrationality should hold for **every rational** (t>1), and Erdős later reiterated that this extension “is almost certainly true” but not reachable by his method. 
* This conjecture is **still open in general**. A modern reference (Duverney–Tachiya) explicitly states that the conjecture for
  [
  \sum_{n=1}^\infty \frac{1}{t^n-1}=\sum_{n=1}^\infty \frac{d(n)}{t^n}
  ]
  [[nomath]](with $d(n)=\tau(n)$)[[/nomath]] “is still open,” and records only partial results: it is known to be irrational for rationals (t=r/s\neq 0) satisfying
  [
  \frac{\log|s|}{\log|r|} < \frac13\\(1-\frac{3}{\pi^2}\\)\approx 0.232.
  ]

* The same question is listed as **open** as Erdős Problem #1049 on the Erdős Problems site (last edited Sept 28, 2025). ([Erdős Problems][1])

So: **for general rational (t>1), it is not currently known whether the sum must be irrational** (though it is widely believed to be).

[1]: https://www.erdosproblems.com/tags/irrationality "
  
    Erdős Problems
  
"
