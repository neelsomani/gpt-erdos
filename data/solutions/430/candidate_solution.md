If you literally follow the rule all the way down, the sequence always ends with $1$ [[nomath]](since $1$ has no prime factors, it vacuously satisfies the condition)[[/nomath]], so in that literal sense “all terms are prime” is impossible for any $n$.

What Erdős and Graham (and almost everyone who discusses this) mean is:

> must there be a **composite** term (>1) somewhere in the sequence for all sufficiently large $n$?

With that interpretation, your question is a well-known open problem.

## A clean reformulation

Let $p(m)$ denote the least prime divisor of $m$ [[nomath]](and one can set $p(1)=\infty$)[[/nomath]].
Your condition “all prime factors of $m$ are (> n-m)” is equivalent to
[
p(m) > n-m.
]
Indeed, if the smallest prime factor exceeds $n-m$, then all prime factors do; conversely if all do, then in particular the smallest does.

So the sequence (a_1>a_2>\dots) is simply the list, in decreasing order, of all (m\in[1,n)) such that (p(m)>n-m).

For a **composite** $m$, the condition (p(m)>n-m) is the same as
[
m + p(m) > n.
]

Define
[
F(n) = \max_{\substack{m<n\ m\ \text{composite}}}\bigl(m+p(m)\bigr).
]
Then:

* there is a composite term in your sequence
  (\Longleftrightarrow)
  there exists a composite (m<n) with (m+p(m)>n)
  (\Longleftrightarrow)
  (F(n)>n).

And your question becomes exactly:

> Is (F(n)>n) for all sufficiently large $n$?

This is Erdős Problem #385, and the equivalence to your formulation is recorded as Erdős Problem #430. Both are listed as **OPEN** on the Erdős Problems site. ([Erdős Problems][1])

## What is known / easy observations

* If $n-1$ is composite, you are done immediately because (a_1=n-1) and $n-1$ always satisfies the prime-factor condition [[nomath]](its prime factors are all $\ge 2 > 1 = n-(n-1)$)[[/nomath]].
  So any “all-prime (>!1)” example must have $n-1$ prime, hence $n$ is even [[nomath]](except $n=3$)[[/nomath]].

* Any (m>1) satisfying (p(m)>n-m) must lie in the top half: (m>n/2).
  [[nomath]](If $m\le n/2$ then $n-m\ge m$, but $p(m)\le m$, so you can’t have $p(m)>n-m$.)[[/nomath]]

  In particular, all primes (q\in(n/2,n)) always appear in the sequence, because for a prime $q$ the condition is (q>n-q), i.e. $q>n/2$.

* There is a trivial upper bound (F(n)\le n+\sqrt n), because for composite $m$ one has (p(m)\le \sqrt m < \sqrt n). This is noted on the Erdős Problems page. ([Erdős Problems][1])

## Status: open (and why it’s hard)

Erdős and Graham already wrote that computations by Selfridge suggested the answer should be “yes” (i.e. eventually a composite must appear), but they had no proof. ([Erdős Problems][2])

Terence Tao has a detailed discussion of the equivalent $F(n)$ formulation (Erdős #385), explaining that ruling out “bad” $n$ [[nomath]](those with $F(n)\le n$)[[/nomath]] is closely tied to the **parity barrier in sieve theory** and potentially Siegel zero issues; even strong tools like RH don’t currently get one far enough in the key intermediate regime. ([What's new][3])

Very roughly, one needs to understand whether intervals $[n-h,n]$ can be “covered” by congruence classes coming from small primes in such a way that the only survivors are primes; Tao explains that small $h$ can be engineered, large (h>\sqrt n) is automatic, and the difficult regime is (\log n \ll h \ll \sqrt n). ([What's new][3])

## Some computational evidence (not a proof)

If we interpret your question as “are there only finitely many $n$ for which **all terms (>1)** in the sequence are prime?”, then there are definitely many such $n$ at small sizes, and they persist sporadically.

For example:

* $n=20$: the sequence is $19,17,13,11,1$ [[nomath]](all $>1$ are prime)[[/nomath]].
* $n=21$: the sequence starts with (20), already composite.

I also checked by computation that there are “all-prime (>!1)” cases well past (10^5); for instance $n=267672$ and $n=267680$ have this property [[nomath]](so if the conjecture is true, the cutoff $N_0$ would have to exceed $267680$)[[/nomath]]. This is consistent with the problem being genuinely difficult, not something that settles quickly.

## Bottom line

Interpreted in the nontrivial way [[nomath]](i.e. “must a composite $>1$ eventually appear?”)[[/nomath]], the answer is:

* **Unknown.** It is an open Erdős problem (Erdős–Graham #430), equivalent to Erdős–Eggleton–Selfridge problem #385 about (F(n)=\max_{m<n,\ \text{comp}}(m+p(m))). ([Erdős Problems][2])

If you want, I can also spell out the exact equivalence between your greedy sequence and the $F(n)$ formulation in a few lines (it’s short), or summarize Tao’s heuristic expectations for the typical size of $F(n)-n$.

[1]: https://www.erdosproblems.com/385 "https://www.erdosproblems.com/385"
[2]: https://www.erdosproblems.com/tags/number%20theory "https://www.erdosproblems.com/tags/number%20theory"
[3]: https://terrytao.wordpress.com/2024/08/19/erdos-problem-385-the-parity-problem-and-siegel-zeroes/ "https://terrytao.wordpress.com/2024/08/19/erdos-problem-385-the-parity-problem-and-siegel-zeroes/"
