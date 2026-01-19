As stated [[nomath]](allowing the $b_i$ to repeat)[[/nomath]], the threshold is completely controlled by **parity**, and one gets an exact answer:

[
g_k(N)=1\qquad \text{for every }k\ge 3\text{ and every }N\ge 1.
]

### Why (g_k(N)\ge 1)

Take
[
A={1,3,5,\dots,2N-1},
]
the set of all odds in ({1,\dots,2N}). Then (|A|=N).

If (k\ge 3) and (b_1,\dots,b_k) are integers, then among these $k$ integers at least two have the same parity (pigeonhole). Say (b_i\equiv b_j\pmod 2). Then (b_i+b_j) is even, hence (b_i+b_j\notin A). So **no** $k$-tuple can have *all* pairwise sums in $A$. Therefore sets of size $N$ do not force the configuration, so
[
g_k(N)\ge 1.
]

### Why (g_k(N)\le 1)

Now suppose (|A|\ge N+1). Since ({1,\dots,2N}) contains exactly $N$ odds and $N$ evens, any subset of size $N+1$ must contain at least one even number. So pick an even element (2t\in A).

Set
[
b_1=b_2=\cdots=b_k=t.
]
Then for every (i<j),
[
b_i+b_j=t+t=2t\in A.
]
So the required configuration exists. Hence
[
g_k(N)\le 1.
]

Combining both bounds gives (g_k(N)=1).

---

If you *intended* the (b_i) to be **distinct** (many people do in this kind of question), then the problem becomes genuinely nontrivial and the answer changes; tell me and I’ll treat that variant.
