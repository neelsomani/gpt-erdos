Let (P) denote the primes, and write the counting function
[
A(N):=\lvert A\cap{1,\dots,N}\rvert .
]
Your condition is that (P+A) contains all sufficiently large integers (i.e. all but finitely many).

### 1) Can one get (A(N)=o((\log N)^2)) and still cover **every** large integer?

As far as I can tell from the current literature/summaries, this is **still open**.

What is known unconditionally is Erdős’s classical probabilistic construction: there exists an additive complement (A) to the primes with
[
A(N)=O\big((\log N)^2\big)
]
such that every sufficiently large integer is (p+a). ([arXiv][1])

But no unconditional improvement to (o((\log N)^2)) is currently known for covering **all** sufficiently large integers; the best improvements are for “almost all integers” (density (1)), not for all. ([Erdős Problems][2])

### 2) Can one achieve (A(N)=O(\log N)) (still covering **every** large integer)?

Also **open**.

This is stated explicitly in Dai–Pan (2011): “no one knows” whether there exists an additive complement (A) of (P) with (A(x)=O(\log x)). ([arXiv][1])
And the Erdős Problems site (updated Dec 2025) likewise treats the (O(\log N)) target as open. ([Erdős Problems][3])

What *is* known very close to (O(\log N)), but only for **almost all** integers: Ruzsa showed that for any function (\omega(N)\to\infty) there exists an “almost additive complement” (A) with
[
A(N)\ll \omega(N)\log N
]
such that all but a density-zero set of integers are representable as (p+a). ([Erdős Problems][2])
So we can get (A(N)) as close to (c\log N) as we like (up to a slowly growing factor), but we currently lose finitely-many? no: we lose an exceptional set of density (0).

There is also a different (stronger) statement if you allow **two** elements of (A): Vu proved that there exists (A) with (A(N)=O(\log N)) such that every sufficiently large integer is
[
n=a_1+a_2+p,
]
i.e. (A+A+P) covers all large integers. ([arXiv][1])
This does not resolve the one-shift problem (A+P).

### 3) Must such an (A) satisfy (\displaystyle \liminf \frac{A(N)}{\log N}>1)?

Yes — in fact a stronger lower bound is known.

A very basic counting heuristic already forces (A(N)\gg \log N): up to (N), each fixed (a) can contribute at most (\pi(N)) representable integers (p+a\le N), and (\pi(N)\sim N/\log N), so you need on the order of (\log N) different shifts (a) to cover (N) integers.

Ruzsa proved a sharp constant-level obstruction:
[
\liminf_{N\to\infty}\frac{A(N)}{\log N}\ \ge\ e^\gamma \approx 1.781\ldots,
]
where (\gamma) is the Euler–Mascheroni constant. ([MATWBn][4])
So the answer to your last question is **yes**, and in fact the liminf must be at least (e^\gamma>1).

---

**Summary of the current state (Jan 2026):**

* For covering **all sufficiently large integers**: best known is Erdős’s (A(N)=O((\log N)^2)). ([arXiv][1])
  Improving this to (o((\log N)^2)) (in particular (O(\log N))) is **open**. ([arXiv][1])
* For covering **almost all integers**: one can get (A(N)\ll \omega(N)\log N) for arbitrarily slowly growing (\omega). ([Erdős Problems][2])
* Any (A) that covers **all** large integers must satisfy
  (\liminf A(N)/\log N \ge e^\gamma). ([MATWBn][4])

If you want, I can also sketch the idea behind Ruzsa’s (e^\gamma) lower bound (it’s a “small primes / Mertens product” obstruction), but the headline result is as above.

[1]: https://arxiv.org/pdf/1101.1653?utm_source=chatgpt.com "arXiv:1101.1653v3 [math.NT] 28 Apr 2011"
[2]: https://www.erdosproblems.com/32?utm_source=chatgpt.com "Erdős Problem #32"
[3]: https://www.erdosproblems.com/forum/thread/32?order=oldest&utm_source=chatgpt.com "Erdős Problem #32 - Discussion thread"
[4]: https://matwbn.icm.edu.pl/ksiazki/aa/aa86/aa8638.pdf?utm_source=chatgpt.com "On the additive completion of primes"
