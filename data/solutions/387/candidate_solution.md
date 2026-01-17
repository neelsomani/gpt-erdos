A few easy reductions first.

For (n\ge 5) the set of composites (m<n) is nonempty.  Also

* If $n$ is **odd** and (n\ge 5), then (m=n-1) is even composite and (p(m)=2), so
  [
  F(n)\ \ge\ (n-1)+2\ =\ n+1\ >\ n.
  ]
  So the only possible obstructions to (F(n)>n) occur for **even** $n$.

* If $n$ is **even** and (n\ge 6), then (m=n-2) is even composite and (p(m)=2), so
  [
  F(n)\ \ge\ (n-2)+2\ =\ n.
  ]
  Thus for (n\ge 6) one always has (F(n)\ge n). Any failure of strict inequality is exactly the case (F(n)=n).

* Trivially (p(m)\le \sqrt m<\sqrt n) for any composite (m<n), hence
  $
  F(n)\le (n-1)+\sqrt{n-1}<n+\sqrt n.
  $
  [[nomath]](This “$n+\sqrt n$” upper bound is the one explicitly noted in the Erdős-problems description. ([Erdős Problems][1]))[[/nomath]]

So the first question is really asking whether there are only finitely many **even** $n$ with (F(n)=n) [[nomath]](often called “bad” $n$ in the discussion of this problem ([What's new][2]))[[/nomath]].

## What is known about (F(n)>n) for all large $n$?

This is **open**: it is Erdős Problem #385 in the Erdős Problems database. ([Erdős Problems][1])

Some structure is clear:

* If $n-1$ is composite then (m=n-1) gives (F(n)\ge n-1+p(n-1)\ge n+1), so any “bad” $n$ must have $n-1$ prime. [[nomath]](Tao makes this a starting point by defining bad $n$ as those with $F(n)\le n$. ([What's new][2]))[[/nomath]]

* Tao unpacks “$n$ is bad” into a covering/sieving condition on the interval $[n-h,n]$ by residue classes (0\bmod p) for (p\le h), and explains that the difficult regime is intermediate scales (\log n \ll h \ll \sqrt n), where sieve theory runs into the “parity barrier” and related issues. ([What's new][2])

Computationally, the bad $n$ seem extremely sparse.  OEIS records (computed by Robert Israel in Maple) that **all** $n$ with $F(n)\le n$ up to (10^8) are the following 100 values, ending at $267680$:
[
6,8,12,14,\dots,8742,267672,267680.
]
([OEIS][3])
But no proof is known that the list is complete beyond that range, and the finiteness question is not resolved. (OEIS explicitly notes “Erdos conjectures that this sequence is finite.” ([OEIS][3]))

So: **it is not currently known** whether (F(n)>n) for all sufficiently large $n$. ([Erdős Problems][1])

## Does (F(n)-n \to \infty) as (n\to\infty)?

This is also **open**, and is part of the same Erdős problem. ([Erdős Problems][1])

What one can say unconditionally is limited:

* You always have (0\le F(n)-n < \sqrt n) for (n\ge 6) by the lower/upper bounds above.
* The quantity is **sometimes large**: for example, if (n=p^2+1) with $p$ prime, then taking (m=p^2) gives
  [
  F(n)\ \ge\ p^2+p\ =\ (p^2+1) + (p-1)\ =\ n + (p-1),
  ]
  so (F(n)-n \ge p-1 \asymp \sqrt n) along the subsequence (n=p^2+1). [[nomath]](This shows $\limsup (F(n)-n)/\sqrt n \ge 1$, but it does **not** address whether the difference is eventually large for *every* $n$.)[[/nomath]]

On the heuristic/conjectural side, Erdős–Eggleton–Selfridge already suggested that “plausible conjectures on primes” would imply there are only finitely many bad $n$, and even that $F(n)$ might typically be as large as (n+(1-o(1))\sqrt n). ([Erdős Problems][1])
Tao explains that a sufficiently strong statement about **gaps between certain semiprimes** in short intervals would imply both (F(n)>n) eventually and (F(n)-n\to\infty), but that such bounds are far beyond current methods (even assuming RH), in large part because of parity-barrier phenomena. ([What's new][2])

So: **it is not currently known** whether (F(n)-n\to\infty). ([Erdős Problems][1])

## A useful “big picture” summary

* The only possible failures of (F(n)>n) occur for even $n$, and in fact are exactly (F(n)=n) [[nomath]](“bad” $n$)[[/nomath]].
* It is a classical Erdős-type open problem whether there are finitely many bad $n$, and whether $F(n)-n$ must grow without bound.
* Computations strongly suggest bad $n$ are finite and may stop at $267680$ [[nomath]](none up to $10^8$)[[/nomath]], but this is not proved. ([OEIS][3])

[1]: https://www.erdosproblems.com/385 "
  
    Erdős Problem #385
  
"
[2]: https://terrytao.wordpress.com/2024/08/19/erdos-problem-385-the-parity-problem-and-siegel-zeroes/ "Erdos problem #385, the parity problem, and Siegel zeroes | What's new"
[3]: https://oeis.org/A322293 "A322293 - OEIS"