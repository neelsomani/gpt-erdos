It depends on what you mean by “(>k) prime factors”.

### If you count prime factors **with multiplicity** ((\Omega(n)))

Then the answer is **yes, and it’s essentially immediate**.

Let (P:=p_1p_2\cdots p_k). In any block of $P$ consecutive integers $[n,n+P)$ there is exactly one multiple of $P$, namely (m=P\cdot\lceil n/P\rceil).
For all (n>P), this multiple satisfies (m\ge 2P), hence (\Omega(m)\ge \Omega(P)+1=k+1>k). So for all sufficiently large $n$, the interval contains an integer with (>k) prime factors (counted with multiplicity).

### If you count **distinct** prime factors ((\omega(n)))

This is the nontrivial interpretation, and under that interpretation the problem is **open**.

In fact, the question you wrote appears verbatim as **Erdős problem #891** (originally attributed to Erdős–Selfridge), and the current status is listed as **OPEN**. ([Erdős Problems][1])
It is stated there that the problem is **unknown even for $k=2$**, i.e. whether every sufficiently large interval of length $6$ must contain an integer divisible by at least $3$ *distinct* primes. ([Erdős Problems][1])

#### Partial/related results mentioned in the literature

* **Schinzel’s modification:** using a theorem of **Pólya (1918)** (implying unbounded gaps between integers supported on a fixed finite set of primes), Schinzel showed that the statement *does* hold if one replaces (p_1\cdots p_k) by (p_1\cdots p_{k-1}p_{k+1}). ([Erdős Problems][1])
* **A conditional “nearby” negative result:** it’s observed that **Dickson’s conjecture** would imply the answer becomes **no** if you shorten the interval length by $1$, i.e. replace (p_1\cdots p_k) with (p_1\cdots p_k-1). ([Erdős Problems][1])

So, under the distinct-prime-factor interpretation (\omega(\cdot)), your statement is a well-known open Erdős-style problem; under the multiplicity interpretation (\Omega(\cdot)), it’s true for a simple reason.

[1]: https://www.erdosproblems.com/forum/thread/891 "

    Erdős Problem #891 - Discussion thread

"
