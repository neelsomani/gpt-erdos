Interpreting “(k) consecutive primes” in the standard way (consecutive in the ordered list of primes), this is the problem of finding

[
p_n,;p_{n+1},;\dots,;p_{n+k-1}
]

such that they form an arithmetic progression (equivalently, the prime gaps
(p_{n+1}-p_n=\cdots=p_{n+k-1}-p_{n+k-2}=d) are all equal). These are often called **CPAP-(k)**: *(k) Consecutive Primes in Arithmetic Progression*. ([Wikipedia][1])

### What is known

* **Yes for small (k)** (explicitly known examples):

  * (k=3): (3,5,7) (difference (2)). ([OEIS][2])
  * (k=4): (251,257,263,269) (difference (6)). ([OEIS][2])
  * (k=5): (9843019,9843049,9843079,9843109,9843139) (difference (30)). ([OEIS][2])
  * (k=6): (121174811,121174841,121174871,121174901,121174931,121174961) (difference (30)). ([OEIS][2])

* **In fact, examples are known up to (k=10)**: a CPAP-10 exists (first found in 1998), and **10 is the longest length currently known** in the usual record lists. ([PrimePages][3])

### What is *not* known (the key point)

* It is **conjectured** that there are **arbitrarily long** CPAPs (so, for every (k) there would be some CPAP-(k), and in fact infinitely many). But this is **not proved**. ([Wikipedia][1])
* No CPAP-11 is currently known in the standard references/record pages, and finding one is believed to be extremely difficult. ([PrimePages][3])

### A simple necessary condition on the common difference (d)

Suppose (p, p+d, \dots, p+(k-1)d) are primes.

Let (q) be a prime with (q\le k). If (q\nmid d), then the residues (p, p+d, \dots, p+(q-1)d) run through **all** classes mod (q), so one term is (0 \pmod q). That term would be composite unless it equals (q) itself.
So, unless the progression actually contains the small prime (q), you are forced to have (q\mid d).

In particular, for a “large” CPAP-(k) (where none of the terms is (2,3,5,\dots,k)), the step (d) must be divisible by the **primorial**
[
\prod_{q\le k} q.
]
This is why (for example) any CPAP-11 would need a step divisible by (11#=2\cdot3\cdot5\cdot7\cdot11=2310), making the search space huge. ([Wikipedia][1])

---

**Bottom line:**

* There **do** exist (k) consecutive primes in arithmetic progression for many (k) (certainly for (3\le k\le 10)). ([OEIS][2])
* Whether this happens for **every** (k\ge 3) is **open** (conjectured “yes,” unproved). ([Wikipedia][1])

[1]: https://en.wikipedia.org/wiki/Primes_in_arithmetic_progression?utm_source=chatgpt.com "Primes in arithmetic progression"
[2]: https://oeis.org/A006560 "A006560 - OEIS"
[3]: https://t5k.org/top20/page.php?id=13 "PrimePage Primes: Consecutive Primes in Arithmetic Progression"
