This is **open**.

It is recorded as an Erdős problem (attributed to **Deaconescu**) and is currently listed as **“Open, but could be disproved with a finite counterexample.”** ([Erdős Problems][1])  In particular, the Erdős-problems site notes that **Deaconescu verified the statement computationally for (n\le 1000)**, and that Erdős expected the *least* such prime $p$ to be much smaller than $P$ [[nomath]](even $p\le n^{O(1)}$)[[/nomath]]. ([Erdős Problems][1])

### Why it looks very plausible (heuristics)

Let (P=\prod_{i=1}^n p_i) (a primorial). There are about (\pi(P)\sim \frac{P}{\log P}) primes (\le P), so roughly (\frac{P}{\log P}) candidate primes $p$ in $(p_n,P)$. For a “random-looking” integer around size $P$, primality has heuristic probability (\approx \frac{1}{\log P}). So the **expected** number of primes among the values $P+p$ [[nomath]](with $p$ prime in $(p_n,P)$)[[/nomath]] is on the order of
[
\frac{P}{\log P}\cdot \frac{1}{\log P};\approx;\frac{P}{(\log P)^2},
]
which grows huge, making failure seem extraordinarily unlikely. The Erdős-problems page makes this heuristic explicit and concludes that the probability of failure is “ridiculously small.” ([Erdős Problems][1])

### Connection to Fortunate numbers

Define the **Fortunate number** $a(n)$ to be the least integer (m>1) such that
[
P+m \text{ is prime}.
]
Fortune conjectured that **$a(n)$ is always prime**, and computations have checked this for thousands of terms (OEIS notes e.g. the first 2000 terms are prime). ([OEIS][2])

If Fortune’s conjecture is true *and* one also has (a(n)<P), then your question would follow [[nomath]](take $p=a(n)$)[[/nomath]]. But Fortune’s conjecture itself is unproved. ([OEIS][2])

### Small numerical evidence

For small $n$, one quickly finds such a prime $p$. Here are examples [[nomath]](in fact, these $p$’s coincide with the initial Fortunate numbers listed in OEIS A005235)[[/nomath]]: ([OEIS][2])

| $n$ | (p_n) | (P=\prod_{i\le n}p_i) | example prime $p$ |      $P+p$ |
| --: | ----: | --------------------: | ----------------: | ---------: |
|   2 |     3 |                     6 |                 5 |         11 |
|   3 |     5 |                    30 |                 7 |         37 |
|   4 |     7 |                   210 |                13 |        223 |
|   5 |    11 |                  2310 |                23 |       2333 |
|   6 |    13 |                 30030 |                17 |      30047 |
|   7 |    17 |                510510 |                19 |     510529 |
|   8 |    19 |               9699690 |                23 |    9699713 |
|   9 |    23 |             223092870 |                37 |  223092907 |
|  10 |    29 |            6469693230 |                61 | 6469693291 |

### A couple of quick observations

* The condition (p>p_n) is essentially forced: if (p\le p_n), then (p\mid P), so (P+p\equiv 0\pmod p) and $P+p$ is composite.
* Your statement implies that the primorial $P$ is a difference of two primes (((P+p)-p=P)), i.e. a very special case of the broader “difference of two primes” questions (which are also far beyond current methods).

So: **no general proof is known**, but it has been computationally verified quite far and has strong heuristic support. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/forum/thread/779 "

    Erdős Problem #779 - Discussion thread

"
[2]: https://oeis.org/A005235 "A005235 - OEIS"
