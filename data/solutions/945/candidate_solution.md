Write (d(n)=\tau(n)) for the divisor function. Erdős–Mirsky introduced exactly this function $F(x)$ [[nomath]](they use $d(n)$ and the same definition of $F(x)$)[[/nomath]] and asked for its true order of magnitude. ([Rényi Institute][1])

## What is known unconditionally

### Erdős–Mirsky (1952)

They proved the first nontrivial lower bound and [[nomath]](via their work on how many *distinct* values $d(n)$ can take up to $x$)[[/nomath]] an upper bound; in modern asymptotic notation one can state it as
[
\frac{(\log x)^{1/2}}{\log\log x}\ \ll\ F(x)\ \ll\ \exp!\left(O!\left(\frac{(\log x)^{1/2}}{\log\log x}\right)\right).
]
([Erdős Problems][2])

They also explicitly conjectured that $F(x)$ should be a power of (\log x) (i.e. “polylogarithmic”) and remarked they had nothing better at the time. ([Rényi Institute][1])

Erdős later claimed that with “some more work” their method should improve the *lower* bound substantially [[nomath]](to $(\log x)^{1-o(1)}$)[[/nomath]], but this is stated as a claim/remark rather than a fully standard published sharpening. ([Erdős Problems][2])

### Best published upper bound (as reported)

A later improvement due to Beker is reported as
[
F(x)\ \ll\ \exp\left(O\left((\log x)^{1/3+o(1)}\right)\right),
]
which is currently (as far as the compiled references indicate) the strongest unconditional upper bound. ([Erdős Problems][2])

So, unconditionally, we only know that $F(x)$ grows at least like ((\log x)^{1/2}/\log\log x) and at most like (\exp\big((\log x)^{1/3+o(1)}\big)), leaving a very large gap. ([Erdős Problems][2])

## Is (F(x)\le (\log x)^{O(1)}) known?

No—this remains open in general. The problem statement on the Erdős problems site still lists it as open, and the best unconditional upper bounds are still of stretched-exponential type in (\log x), not a power of (\log x). ([Erdős Problems][2])

Equivalently: it is **not known** (unconditionally) whether there exists a constant (C>0) such that every interval ([x,x+(\log x)^C]) contains two integers with the same number of divisors.

## Conditional results supporting a “yes”

There are natural hypotheses under which a polylogarithmic bound *would* follow.

### From Cramér’s conjecture on prime gaps

Cramér’s conjecture asserts (p_{n+1}-p_n = O((\log p_n)^2)). ([Wikipedia][3])
If this were true, then intervals of length (\asymp (\log x)^2) would contain **two primes** for large $x$ [[nomath]](take the first prime $\ge x$, then the next one)[[/nomath]], hence two numbers with (\tau=2). This yields
[
F(x)\ \ll\ (\log x)^2
]
under Cramér. ([Erdős Problems][2])

### From very short gaps between squarefree numbers

A different sufficient condition is: if every interval in $[x,2x]$ of length (\gg \log x) contains a squarefree number, then one can force repeats of (\tau) in intervals of length (\gg (\log x)^2), and again conclude
[
F(x)\ \ll\ (\log x)^2.
]
This is linked to the (still open) problem of bounding gaps between consecutive squarefree numbers. ([Erdős Problems][2])

## Bottom line

* **Unconditional best bounds** (as currently recorded):
  [
  \frac{(\log x)^{1/2}}{\log\log x}\ \ll\ F(x)\ \ll\ \exp!\left(O!\left((\log x)^{1/3+o(1)}\right)\right).
  ]
  ([Erdős Problems][2])

* **Your polylog question** (F(x)\le (\log x)^{O(1)}): **open** unconditionally. ([Erdős Problems][2])

* **But** it would follow [[nomath]](with $F(x)\ll(\log x)^2$)[[/nomath]] from strong standard conjectures like Cramér’s prime-gap conjecture, or from sufficiently strong bounds on squarefree gaps. ([Erdős Problems][2])

[1]: https://www.renyi.hu/~p_erdos/1952-12.pdf "https://www.renyi.hu/~p_erdos/1952-12.pdf"
[2]: https://www.erdosproblems.com/945 "https://www.erdosproblems.com/945"
[3]: https://en.wikipedia.org/wiki/Cram%C3%A9r%27s_conjecture "https://en.wikipedia.org/wiki/Cram%C3%A9r%27s_conjecture"
