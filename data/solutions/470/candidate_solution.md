### Odd weird numbers

No **odd** weird numbers are known, and their existence is still an open problem.

The best published exhaustive searches I’m aware of (as of 2022) prove:

* **There is no odd weird number below (10^{21}).** 
* More strongly (with an extra restriction), **there is no odd weird number below (10^{28})** among odd numbers whose abundance is (<10^{14}). 

So, **if an odd weird number exists, it must exceed (10^{21})**. 

There are also structural restrictions known; for instance, Liddy & Riedl (2018) report/prove that **an odd weird number would have to have at least 6 prime divisors**. ([IdeaExchange][1])

### Primitive weird numbers

Let “primitive weird” mean: weird and **no proper divisor is weird** (equivalently: not a multiple of another weird number).

* Unconditionally, **it is not currently proved that there are infinitely many primitive weird numbers.** This was already explicitly noted in the original Benkoski–Erdős paper: they say it “seems likely” but **they could not prove** that there are infinitely many primitive abundant numbers that are weird. 
* More recent work (Melfi 2015) likewise states that **whether infinitely many primitive weird numbers exist is an open problem**. ([Libra][2])

What *is* known is a strong **conditional** result:

* Melfi proves a large explicit family of **primitive weird numbers of the form**
  [
  n = 2^k p q
  ]
  for primes (p,q) satisfying certain inequalities (his Theorem 1). ([Libra][2])
* He then explains that **if one assumes a sufficiently strong upper bound on prime gaps** [[nomath]](e.g. $p_{n+1}-p_n < 0.1,p_n^{1/2}$ for all large $n$)[[/nomath]], which would follow from classical conjectures such as **Cramér’s conjecture**, then **his construction would yield infinitely many primitive weird numbers**. ([Libra][2])

So the status is:

* **Odd weird numbers:** open; none known; none below (10^{21}). 
* **Infinitely many primitive weird numbers:** open **unconditionally**; **conditionally yes** under standard (unproven) prime-gap conjectures, via Melfi’s work. ([Libra][2])

(For context: even though primitivity is subtle, weird numbers themselves are plentiful—Benkoski & Erdős proved weird numbers have **positive asymptotic density**, hence infinitely many. )

[1]: https://ideaexchange.uakron.edu/honors_research_projects/728/?utm_source=chatgpt.com "An algorithm to determine all odd primitive abundant numbers ..."
[2]: https://libra.unine.ch/bitstreams/9084975d-4950-470b-aa6e-4f3e564c2f4b/download "On the conditional infiniteness of primitive weird numbers"
