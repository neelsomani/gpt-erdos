This is currently **open** (in the sense of “no proof known either way”), even in the special case $k=2$. It appears as **Erdős Problem #386**. ([Erdős Problems][1])

What *is* known is essentially a short list of examples and some strong computational evidence:

## Known examples

Besides your example
[
\binom{21}{2}=210=2\cdot 3\cdot 5\cdot 7,
]
Erdős Problems records these further “consecutive-prime product” binomial coefficients: ([Erdős Problems][1])

* (\displaystyle \binom{7}{3}=35=5\cdot 7)
* (\displaystyle \binom{10}{4}=210=2\cdot 3\cdot 5\cdot 7)
* (\displaystyle \binom{14}{4}=1001=7\cdot 11\cdot 13)
* (\displaystyle \binom{15}{6}=5005=5\cdot 7\cdot 11\cdot 13)

And for $k=2$ specifically [[nomath]](so $\binom{n}{2}$ is a triangular number)[[/nomath]], the **known values of $n$** for which (\binom{n}{2}) is a product of consecutive primes are
[
n\in{4,6,15,21,715},
]
giving
[
\binom{4}{2}=6,\quad \binom{6}{2}=15,\quad \binom{15}{2}=105,\quad \binom{21}{2}=210,\quad \binom{715}{2}=255255.
]
([Erdős Problems][1])

## Computational evidence for $k=2$

OEIS sequence **A280992** is exactly “squarefree triangular numbers that are products of consecutive primes,” listing
[
6,\ 15,\ 105,\ 210,\ 255255
]
(as the nontrivial terms), and reports: **“No more terms up to the 5,000,000th triangular number.”** ([OEIS][2])

So if another (\binom{n}{2}) example exists, it’s already forced to be very large by computation, but there is **no proof** that none exist.

## Status of the “infinitely often” question

* Erdős and Graham are quoted as saying that *“a proof that this cannot happen infinitely often for (\binom{n}{2}) seems hopeless”* and they *expected* it probably never happens for (3\le k\le n-3), but the four examples above show it can happen for some (k\ge 3). ([Erdős Problems][1])
* **No one currently knows** whether such binomial coefficients occur **infinitely often** [[nomath]](either for some varying $k$, or even just for $k=2$)[[/nomath]]. ([Erdős Problems][1])

So the best accurate answer right now is: **we don’t know**; the problem is open, with only the examples above known and with large-scale computation ruling out small additional cases for $k=2$. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/386 "
  
    Erdős Problem #386
  
"
[2]: https://oeis.org/A280992 "A280992 - OEIS"
