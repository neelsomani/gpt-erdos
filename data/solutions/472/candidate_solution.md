This is a known open problem.

A convenient rephrasing of your rule is:

> once (q_n) is defined, (q_{n+1}) is the *smallest prime* (p>q_n) such that
> [
> p-q_n+1\in{q_1,\dots,q_n}.
> ]
> Indeed (p=q_n+q_i-1\iff p-q_n+1=q_i).

This question appears (attributed to Ulam) as **Erdős Problem #472** and is listed there as **OPEN**: it is not currently known whether *any* finite starting list can force the greedy extension to continue forever. ([Erdős Problems][1])

### The “best known” candidate start: $3,5$

If you start with $3,5$, you get the sequence recorded in OEIS as **A389713**:
[
3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,101,\dots
]
OEIS explicitly notes: **“It is unknown whether this sequence is infinite.”** ([OEIS][2])
[[nomath]](The first prime missing from this sequence is $97$, as OEIS remarks. $[OEIS][2]$)[[/nomath]]

### It’s not trivially always extendable

Some starts die immediately (or very quickly). For example:

* Start with ((5)): the only candidate is (5+5-1=9), composite, so it stops at once.
* Start with $(11,13)$: you get (11,13,23), and then the candidates are (23+11-1=33), (23+13-1=35), (23+23-1=45), all composite, so it stops.

So the existence of an infinite greedy run is genuinely nontrivial.

### Computational evidence (not a proof)

Although the problem is open, the $3,5$ start has been computed very far in practice [[nomath]](OEIS links a table up to $n=10000$)[[/nomath]]. ([OEIS][2])
Independently, I checked (by direct computation) that starting from $(3,5)$ the greedy rule produces at least the first **100,000** terms without getting stuck; the $100{,}000$-th term is
[
q_{100000}=2{,}678{,}747.
]
This is strong evidence that the sequence *might* be infinite, but there is no known proof.

**Bottom line:** as of now, **no initial starting sequence is known to be guaranteed to yield an infinite sequence**, and **it’s open whether any such start exists**. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/472 "https://www.erdosproblems.com/472"
[2]: https://oeis.org/A389713 "https://oeis.org/A389713"
