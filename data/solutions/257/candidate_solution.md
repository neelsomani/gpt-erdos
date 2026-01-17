No one currently knows the answer in full generality.

This question is a well-known open problem of Erdős (often listed as **Erdős Problem #257**): for an *arbitrary* infinite (A\subseteq\mathbb N), it is not known whether
[
\sum_{n\in A}\frac{1}{2^n-1}
]
must be irrational. ([Erdős Problems][1])

### Why it’s nontrivial

Using the geometric series identity
[
\frac{1}{2^n-1}=\sum_{k\ge1}2^{-nk},
]
one can rewrite the subsum as a Lambert-series-type base‑2 expansion:
[
\sum_{n\in A}\frac{1}{2^n-1}
=\sum_{m\ge1}\frac{f_A(m)}{2^m},
]
where (f_A(m)) is the number of divisors of (m) that lie in $A$. ([Erdős Problems][1])
Determining whether this can ever produce a rational number for some infinite $A$ is hard.

### What *is* known (examples of $A$ where irrationality is proved)

* **(A=\mathbb N)** (the full series): this is the Erdős–Borwein constant, and Erdős proved it is irrational [[nomath]](more generally $\sum_{n\ge1}1/(t^n-1)$ is irrational for integer $t>1$)[[/nomath]]. ([Mathematics Stack Exchange][2])

* **Some structured sparse sets $A$**: Erdős proved irrationality under extra hypotheses, e.g. when $A$ is pairwise coprime [[nomath]]($\gcd(a,b)=1$ for distinct $a,b\in A$) and (\sum_{n\in A}\frac1n<\infty)[[/nomath]]. ([Erdős Problems][1])

* **$A$ = primes**: very recently, Tao and Teräväinen proved the “primes” subseries is irrational:
  [
  \sum_{p\ \text{prime}}\frac{1}{2^p-1}\ \text{is irrational}.
  ]
  In their paper, this is stated as irrationality of (\sum_{n\ge1}\omega(n)/2^n), which equals the prime sum above. ([ar5iv][3])
  They also note their method can be modified to handle **prime powers** [[nomath]](corresponding to $A={p^k}$)[[/nomath]], though they leave those details to the reader. ([ar5iv][3])

### “Almost all” $A$ give an irrational sum

Even though the universal statement is open, Kovač and Tao proved strong genericity results: for natural random models of choosing $A$, the sum is **irrational with probability 1**, and the set of $A$ giving a rational value is meagre (first category) in the Cantor space of subsets. ([arXiv][4])

### Bottom line

* **For every infinite $A$?** Open.
* **For many specific infinite $A$?** Yes, irrationality is known [[nomath]](notably $A=\mathbb N$, and $A=$ primes)[[/nomath]]. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/257 "
  
    Erdős Problem #257
  
"
[2]: https://math.stackexchange.com/questions/2363830/is-sum-limits-n-frac12n-1-irrational?utm_source=chatgpt.com "Is $\sum\limits_n\frac{1}{2^{n}-1}$ irrational?"
[3]: https://ar5iv.org/pdf/2512.01739 "[2512.01739] Quantitative correlations and some problems on prime factors of consecutive integers"
[4]: https://arxiv.org/html/2406.17593v3 "On several irrationality problems for Ahmes series"
