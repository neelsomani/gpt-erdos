This is the **Erdős–Selfridge classification** [[nomath]](often written “class $r+$”)[[/nomath]]. A convenient way to restate your recursive definition is:

* A prime $p$ is **class 1** iff all prime factors of $p+1$ are $2$ or $3$ [[nomath]](equivalently, the largest prime factor of $p+1$ is $2$ or $3$)[[/nomath]].
* Otherwise,
  [
  \mathrm{class}(p)=1+\max{\mathrm{class}(q): q\mid (p+1),\ q\ \text{prime}},
  ]
  which is exactly the “(\le r-1) for all factors, and equality for at least one factor” condition. ([OEIS][1])

## Are there infinitely many primes in each class?

**Open.** This is an Erdős problem (and appears as Problem A18 in Guy’s *Unsolved Problems in Number Theory*). ([Erdős Problems][2])

It is not even known for **class 1**: class‑1 primes are precisely primes of the form
[
p = 2^a3^b-1,
]
and proving infinitely many such primes would in particular imply infinitely many primes in some famous subfamilies (e.g. Mersenne-type forms). ([OEIS][3])

What *is* known (and is “easy to prove” in the sense of Erdős/Selfridge/Guy) is that for each fixed $r$, the number of class‑$r$ primes (\le n) is extremely sparse—at most (n^{o(1)}). ([Erdős Problems][2])
[[nomath]](This still allows infinitude; it just says the counting function grows slower than $n^\varepsilon$ for every fixed $\varepsilon>0$.)[[/nomath]]

### Non-emptiness of all classes

While infinitude is open, it’s not hard to see that **every class occurs at least once**: starting from any class‑1 prime (p_1>3) (e.g. (p_1=5)), Dirichlet’s theorem gives infinitely many primes (p_{k+1}\equiv -1\pmod{p_k}). Then (p_k\mid (p_{k+1}+1)), so (\mathrm{class}(p_{k+1})\ge \mathrm{class}(p_k)+1). Hence classes are unbounded, and therefore no class can be empty [[nomath]](if class $r$ were empty, no class $>r$ could exist by the recursion)[[/nomath]].

## Least prime (p_r) in class $r$, and (p_r^{1/r})

The least primes (p_r) (OEIS A005113) currently listed are: ([OEIS][1])
[
\begin{aligned}
&p_1=2,\ p_2=13,\ p_3=37,\ p_4=73,\ p_5=1021,\ p_6=2917,\ p_7=15013,\ p_8=49681,\
&p_9=532801,\ p_{10}=1065601,\ p_{11}=8524807,\ p_{12}=68198461,\ p_{13}=545587687,\
&p_{14}=1704961513,\ p_{15}=23869461181,\ p_{16}=288310406533.
\end{aligned}
]
([OEIS][1])

Taking $r$-th roots (rounded) gives:

| $r$ |        (p_r) | (p_r^{1/r}) |
| --: | -----------: | ----------: |
|   1 |            2 |       2.000 |
|   2 |           13 |       3.606 |
|   3 |           37 |       3.332 |
|   4 |           73 |       2.923 |
|   5 |         1021 |       3.998 |
|   6 |         2917 |       3.780 |
|   7 |        15013 |       3.950 |
|   8 |        49681 |       3.864 |
|   9 |       532801 |       4.328 |
|  10 |      1065601 |       4.006 |
|  11 |      8524807 |       4.266 |
|  12 |     68198461 |       4.496 |
|  13 |    545587687 |       4.700 |
|  14 |   1704961513 |       4.565 |
|  15 |  23869461181 |       4.919 |
|  16 | 288310406533 |       5.203 |

So **empirically** (up to what’s been computed), (p_r^{1/r}) is in the single digits and has drifted upward to about (5.2) by $r=16$.

### Proven general bounds (very weak)

From the OEIS notes one has the simple inequality
[
p_{r+1}\ \ge\ 2p_r-1,
]
so in particular (p_r \ge 2^r-1) and therefore
[
\liminf_{r\to\infty} p_r^{1/r}\ \ge\ 2.
]
([OEIS][1])
No nontrivial unconditional upper/lower asymptotic for (p_r^{1/r}) is known.

### What is conjectured about (p_r^{1/r})?

Erdős and Selfridge disagreed:

* Erdős thought it was plausible that (p_r^{1/r}\to\infty).
* Selfridge thought it “quite likely” that (p_r^{1/r}) stays bounded. ([Erdős Problems][2])

At present, **either behavior is consistent with what is known**.

---

If you want, I can also spell out the (standard) heuristic that pushes toward Selfridge’s boundedness guess: class $r$ typically contains *many* primes, and each such prime $q$ generates lots of “candidates” (q\cdot m-1) for class $r+1$ with small $m$ whose prime factors lie in earlier classes; having many $q$’s to try makes it plausible that some small multiplier works early, keeping (p_{r+1}) on an approximately exponential scale. But turning that heuristic into a theorem is far beyond current methods (it would require strong control over prime values of very thin structured sequences).

[1]: https://oeis.org/A005113 "https://oeis.org/A005113"
[2]: https://www.erdosproblems.com/1055 "https://www.erdosproblems.com/1055"
[3]: https://oeis.org/A005105 "https://oeis.org/A005105"
