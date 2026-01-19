This is an old Erdős question (now “Erdős Problem #385”) and it is **still open** in general. ([Erdős Problems][1])

### Some easy reductions and bounds

Write (m=n-d) [[nomath]](so $1\le d\le n-4$ when $m$ is composite)[[/nomath]]. Then
[
m+p(m)>n \iff p(n-d)>d,
]
and
$
F(n)-n=\max_{\substack{m<n\ m\ \text{composite}}}(p(m)-(n-m))
=\max_{\substack{d\ge1\ n-d\ \text{composite}}}(p(n-d)-d).
$

Two immediate facts:

* **Odd (n\ge 5):** $n-1$ is even composite, (p(n-1)=2), so (F(n)\ge (n-1)+2=n+1). Thus (F(n)>n) is trivial for all odd (n\ge5).
* **Even (n\ge 6):** $n-2$ is even composite, (p(n-2)=2), so (F(n)\ge (n-2)+2=n). Hence for even (n\ge6) the “bad” case is exactly (F(n)=n) [[nomath]](it can’t be $<n$)[[/nomath]].

Also, for any (m<n),
[
m+p(m)\le m+\sqrt m < n+\sqrt n,
]
so
[
0 \le F(n)-n \le \sqrt n
]
for all sufficiently large $n$ [[nomath]](and in fact for all $n\ge 5$ up to minor edge cases)[[/nomath]].

### When can (F(n)\le n) happen?

If $n$ is even and $n-1$ is composite, then (p(n-1)\ge 3) and
[
(n-1)+p(n-1)\ge n+2,
]
so (F(n)>n). Therefore any “bad” $n$ with (F(n)\le n) must have **$n-1$ prime**, i.e. (n=p+1) with $p$ an odd prime.

This is exactly the phenomenon Erdős discusses when he introduces $F(n)$. He notes that “plausible conjectures on primes” would imply only **finitely many** solutions to (F(n)\le n), and even suggests the much stronger lower bound (F(n) > n + (1-\varepsilon)\sqrt n) for all large $n$. 

### What is known computationally?

The “bad” $n$ [[nomath]](those with $F(n)\le n$)[[/nomath]] are tabulated as OEIS **A322293**. The OEIS entry records that Erdős conjectured this set is finite, and provides data “[[nomath]](all terms $\le 10^8$)[[/nomath]]”. ([OEIS][2])

As of those computations, there are exactly **100** such (n\le 10^8), and the largest is
[
267680.
]
So **for every $n$ with (267680<n\le 10^8)**, the computed data indicate (F(n)>n). ([OEIS][3])
(Of course, this does not prove anything beyond the computation range.)

### Why is it hard (and what would imply a “yes”)?

Tao’s 2024 blog post unpacks the condition “$n$ is bad” as a **covering/sieving statement** about the interval $[n-h,n]$ by residue classes (0 \bmod p) for primes (p\le h), and explains that intermediate scales (\log n \ll h \ll \sqrt n) run into the **parity barrier** in sieve theory, with potential obstructions connected to Siegel zeroes. ([What's new][4])

He also describes a route that would settle the first question (and likely the second) via strong control on **gaps between certain semiprimes** in short intervals—something far beyond current unconditional methods (and not even known under RH at the required strength). ([What's new][4])

### Your two questions

**1) Is (F(n)>n) for all sufficiently large $n$?**
Unproved. This is exactly Erdős Problem #385 and is listed as open. ([Erdős Problems][1])
What we do have:

* It is trivially true for all odd (n\ge 5).
* Computations show no counterexample beyond (267680) up to (10^8). ([OEIS][3])
* Erdős reported that “plausible conjectures on primes” would imply only finitely many counterexamples. 

**2) Does (F(n)-n\to\infty)?**
Also unproved [[nomath]](and in particular would follow from sufficiently strong versions of the “yes” to $1$)[[/nomath]]. ([What's new][4])

What *is* easy is that (F(n)-n) is **unbounded along a subsequence**: if (n=p^2+1) [[nomath]](with $p$ prime)[[/nomath]], then taking (m=p^2) gives
[
F(n)\ \ge\ p^2+p \ =\ n + (p-1),
]
so (F(n)-n\ge p-1\sim \sqrt n). Thus (\limsup_{n\to\infty} (F(n)-n)=\infty) [[nomath]](indeed of order $\sqrt n$)[[/nomath]].
But whether the **full limit** (F(n)-n\to\infty) holds [[nomath]](i.e. a growing lower bound for *all* large $n$)[[/nomath]] is the open part.

If you want, I can also restate Tao’s “bad $n$” condition in a clean equivalent form (the covering formulation) and show explicitly why only the even (n=p+1) can be bad; that reformulation is often the most useful starting point for thinking about the problem.

[1]: https://www.erdosproblems.com/385 "
  
    Erdős Problem #385
  
"
[2]: https://oeis.org/A322293 "A322293 - OEIS"
[3]: https://oeis.org/A322293/b322293.txt "oeis.org"
[4]: https://terrytao.wordpress.com/2024/08/19/erdos-problem-385-the-parity-problem-and-siegel-zeroes/ "Erdos problem #385, the parity problem, and Siegel zeroes | What's new"
