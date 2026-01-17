Let $P$ be a finite set of primes, (|P|\ge 2), and let (a_1<a_2<\cdots) be the increasing list of $P$-smooth numbers [[nomath]](i.e. all $n\in\mathbb N$ whose prime divisors lie in $P$)[[/nomath]]. Write
[
L_n=[a_1,\dots,a_n].
]

### 1) The series converges, and (L_n) has a simple description

Because the sequence ((a_n)) is increasing and contains **every** $P$-smooth number (\le a_n), the maximum exponent of a fixed (p\in P) among ({a_1,\dots,a_n}) is exactly the largest $k$ with (p^k\le a_n), i.e.
[
v_p(L_n)=\big\lfloor \log_p(a_n)\big\rfloor,
\qquad\text{so}\qquad
L_n=\prod_{p\in P}p^{\lfloor\log_p(a_n)\rfloor}.
]
In particular (L_n\ge a_n), hence
[
\sum_{n\ge 1}\frac1{L_n}\ \le\ \sum_{n\ge 1}\frac1{a_n}
=\sum_{\substack{m\ge 1\ \text{(P)-smooth}}}\frac1m
=\prod_{p\in P}\left(\sum_{e\ge 0}\frac1{p^e}\right)
=\prod_{p\in P}\frac1{1-1/p}<\infty,
]
so the series in the question is convergent.

### 2) What is known about irrationality?

* If (|P|=1), say (P={p}), then (a_n=p^{n-1}) and (L_n=p^{n-1}), so
  [
  \sum_{n\ge 1}\frac1{L_n}=\sum_{k\ge 0}\frac1{p^k}=\frac{p}{p-1}\in\mathbb Q.
  ]
  [[nomath]](You excluded this case by assuming $|P|\ge 2$.)[[/nomath]]

* If $P$ is **infinite**, Erdős states that the sum is irrational and calls it a “simple exercise.” ([Rényi Institute][1])

* For **finite** $P$ with (|P|\ge 2): this is (as of late 2025) an **open Erdős problem**. It appears as Erdős Problem #269 on the Erdős Problems website, explicitly marked OPEN, and Erdős himself wrote that the result “probably remains true” for finite $P$ but did not give a proof. ([Erdős Problems][2])

So, the best current answer is:

**No proof is known that the sum is irrational for every finite $P$ with (|P|\ge 2); the problem is open.** ([Erdős Problems][2])

### 3) A closely related variant Erdős said he could prove

Erdős also remarked (in a 1973 letter) that he could prove irrationality **if “duplicate summands are removed,”** i.e. if one collapses repetitions coming from indices $n$ with the same lcm value. ([Erdős Problems][2])

A quick explanation of why that modified series is much easier: if you keep only the strictly increasing values of (L_n), say (B_1<B_2<\cdots), then each ratio (B_{k+1}/B_k) is a prime in $P$, hence (\ge 2). That forces the tail after (B_k) to be (<1/B_k), which is incompatible with rationality once (B_k) is divisible by the denominator of a putative rational value. This “tail (<1/\text{denominator})” mechanism is exactly what fails in the original problem because (L_n) repeats many times.

### 4) Concrete example

Even for (P={2,3}) the irrationality is not known (in general). Numerically the sum is about
[
\sum_{n\ge 1}\frac1{[a_1,\dots,a_n]}\approx 1.93294997736922638906\ldots
]
but no irrationality proof is known in the finite-$P$ setting. ([Erdős Problems][2])

---

If you want, I can also outline the standard proof for the **infinite**-$P$ case (where Erdős calls it an exercise) and point out exactly where it breaks when $P$ is finite. ([Rényi Institute][1])

[1]: https://renyi.hu/~p_erdos/1988-22.pdf "https://renyi.hu/~p_erdos/1988-22.pdf"
[2]: https://www.erdosproblems.com/269 "https://www.erdosproblems.com/269"
