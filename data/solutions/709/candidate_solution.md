Let me rewrite your $f(n)$ in the language that makes the combinatorics visible, and then I’ll give the best unconditional bounds I know (and what’s believed to be the truth).

---

## 1) Reformulation as a matching / Hall problem

Fix a set (A={a_1,\dots,a_n}\subset\mathbb N\cap[2,\infty)) and an interval (I) of (L) consecutive integers.

Build a bipartite graph with left vertices (a_i\in A) and right vertices (x\in I), and an edge (a_i\sim x) iff (a_i\mid x).

Your requirement is exactly:

> In this bipartite graph there is a matching that covers all $n$ left vertices.

By Hall’s theorem, this fails iff there exists a subset (B\subseteq A) such that
$
|\\{x\in I:\exists,b\in B\text{ with }b\mid x\\}|<|B|.
$
So $f(n)$ is the least multiplier such that for every $A$ [[nomath]](size $n$)[[/nomath]] and every interval $I$ of length (f(n)\max(A)), every subset (B\subseteq A) “hits” at least (|B|) integers in $I$ by divisibility.

---

## 2) A universal easy upper bound: (f(n)\le n)

Let (M=\max(A)). Take any interval $I$ of length $nM$ and partition it into $n$ consecutive blocks (I_1,\dots,I_n), each of length $M$.

For each (a_i\le M), **every** block of length $M$ contains at least one multiple of (a_i) (pigeonhole / periodicity of multiples). So in block (I_i) choose a multiple (x_i) of (a_i). The blocks are disjoint, hence the (x_i)’s are automatically distinct.

This gives the general bound
[
f(n)\le n.
]

This is crude, but it is unconditional and works for all $A$.

---

## 3) A nontrivial lower bound from Erdős–Pomerance / van Doorn: (f(n)\gtrsim \dfrac{\log n}{\log\log n})

The “hard” instances are already present in the forced-minimum-max case:
if (|A|=n) and (\max(A)=n+1), then necessarily (A={2,3,\dots,n+1}).

So any lower bound for the set ({1,2,\dots,n+1}) (or ({2,\dots,n+1})) in intervals transfers directly into a lower bound for your $f(n)$.

There is a classical function studied by Erdős and Pomerance: define (f_{\mathrm{EP}}(n,m)) to be the least $L$ such that $(m,m+L]$ contains **distinct** integers (x_1,\dots,x_n) with (i\mid x_i) for each (1\le i\le n). [[nomath]](This is the “distinct multiples of $1,2,\dots,n$” problem.)[[/nomath]]

A 2026 paper of van Doorn proves (confirming an Erdős–Pomerance conjecture) that for all large $n$ there exist intervals of length
[
0.36\frac{n\log n}{\log\log n}
]
that **do not** contain distinct multiples of (1,2,\dots,n). 

Translate this to your setting by taking (A={2,3,\dots,n+1}) and (M=n+1). An interval that fails for ({1,\dots,n+1}) also fails for ({2,\dots,n+1}) [[nomath]](since $1$ is the “easiest” modulus: if you can match $2,\dots,n+1$ inside an interval of length $>n$, you can always add $1$ using any remaining unused integer)[[/nomath]].

Hence, for all sufficiently large $n$,
[
f(n)\ge0.36\frac{\log(n+1)}{\log\log(n+1)}
]
[[nomath]](up to the obvious $n\leftrightarrow n+1$ harmless shift)[[/nomath]]. 

So unconditionally,
[
f(n)=\Omega!\left(\frac{\log n}{\log\log n}\right).
]

---

## 4) What’s known (and unknown) beyond that: connection to Erdős Problem #711

The same Erdős–Pomerance framework studies the **worst starting point**
[
\max_m f_{\mathrm{EP}}(n,m),
]
and Erdős–Pomerance proved a general upper bound
[
f_{\mathrm{EP}}(n,m)\le 4n(\lfloor\sqrt n\rfloor+1)\qquad\text{for all }m,n,
]
so in particular (\max_m f_{\mathrm{EP}}(n,m)\ll n^{3/2}). ([Dartmouth Math][1])

If you divide by $n$ [[nomath]](the relevant $\max(A)$ in the special case $A={1,\dots,n}$)[[/nomath]], you get that for that special family the needed **multiplier** is (\ll \sqrt n).

However, **getting a substantially better upper bound [[nomath]](even just $n^{1+o(1)}$ for $\max_m f_{\mathrm{EP}}(n,m)$)[[/nomath]] is a famous open direction**; it is explicitly listed as Erdős Problem #711. 

Why this matters for your $f(n)$: your problem *contains* the $\\{2,3,\dots,n+1\\}$ instance, so any strong general upper bound on your $f(n)$ [[nomath]](say $f(n)=n^{o(1)}$, or even polylogarithmic)[[/nomath]] would immediately imply a major improvement on the classical Erdős–Pomerance “first $n$ integers” problem as well. 

---

## 5) Summary of current unconditional bounds

From the general block argument and the van Doorn/Erdős–Pomerance lower bound, we have [[nomath]](for large $n$)[[/nomath]]
$
0.36\frac{\log n}{\log\log n}\ \lesssim\ f(n)\ \le\ n.
$
The lower bound is genuinely number-theoretic and comes from the extremal forced set (A={2,\dots,n+1}). 

Closing the gap between (\frac{\log n}{\log\log n}) and $n$ is tightly intertwined with the long-standing problem of bounding (\max_m f_{\mathrm{EP}}(n,m)) better than (O(n^{3/2})). 

---

## 6) What an asymptotic *might* look like (conjectural)

Given the nature of the lower bound construction [[nomath]](which produces intervals of length $\asymp n\log n/\log\log n$ with no distinct multiples of $1,\dots,n$)[[/nomath]], a natural guess is that the true order of magnitude for the “hard” forced case $\\{2,\dots,n+1\\}$ — and hence plausibly for your $f(n)$ — is
[
f(n)\asymp \frac{\log n}{\log\log n}.
]
But at present (as far as the cited sources indicate), there is no matching general upper bound even for the classical ({1,\dots,n}) case. 

---

If you want, I can also:

* work out the exact relationship between your $f(n)$ and the Erdős–Pomerance “$h(n,k)$” parameters [[nomath]](they define variants designed for arbitrary $k$-subsets)[[/nomath]], and
* show how your question reduces to bounding a suitable “worst-case Hall deficit” over unions of arithmetic progressions, which is the structural heart of the problem.

[1]: https://math.dartmouth.edu/~carlp/PDF/matching.pdf "PII: 1385-7258(80)90018-9"
