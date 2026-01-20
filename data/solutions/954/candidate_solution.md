No.

Let
[
N(x):=|\\{(i,j): i\le j,\ a_i+a_j\le x\\}|.
]
Fix (k\ge 2) and look at (x=a_k). Since (a_k) is the **smallest** integer $n$ such that
[
|\\{(i,j): i\le j\le k-1,\ a_i+a_j\le n\\}|;<;n-(k-1),
]
we have two facts:

1. At (n=a_k),
   [
   |\\{(i,j): i\le j\le k-1,\ a_i+a_j\le a_k\\}|\ \le\ a_k-k.
   ]
   [[nomath]](because the left-hand side is an integer and it is $<a_k-(k-1)$)[[/nomath]].

2. At (n=a_k-1), the defining inequality fails (by minimality), so
   [
   |\\{(i,j): i\le j\le k-1,\ a_i+a_j\le a_k-1\\}|\ \ge\ (a_k-1)-(k-1)=a_k-k.
   ]

Monotonicity in $n$ then forces equality:
[
|\\{(i,j): i\le j\le k-1,\ a_i+a_j\le a_k\\}|=a_k-k.
]

But for (x=a_k), no pair involving (a_k) (or any later term) can satisfy (a_i+a_j\le x) because (a_1=1) and (a_k+1>x). Hence
[
N(a_k)=a_k-k.
]
So along the infinite subsequence (x=a_k),
[
N(x)-x=-k.
]

Now $N(a_k)$ counts pairs $(i,j)$ with (i\le j\le k-1), so trivially
[
N(a_k)\le \binom{k}{2}=\frac{k(k-1)}2.
]
Using (N(a_k)=a_k-k) gives
[
a_k-k\le \frac{k(k-1)}2
\quad\Rightarrow\quad
a_k\le \frac{k(k+1)}2.
]
Thus (k\ge \sqrt{2a_k}-\tfrac12), i.e. along (x=a_k),
[
|N(x)-x|=k ;\gg; \sqrt{x}.
]

Since (\sqrt{x}) is much larger than (x^{1/4+o(1)}), the estimate
[
N(x)=x+O(x^{1/4+o(1)})
]
cannot hold [[nomath]](it already fails at $x=a_k$ for infinitely many $k$)[[/nomath]].

---

If what you *meant* was a refined asymptotic after subtracting the inevitable (\asymp \sqrt{x}) term [[nomath]](coming from the fact that $N(a_k)=a_k-k$)[[/nomath]], then you’d be asking a different—and much subtler—question. But as stated with main term $x$, the answer is definitively negative.
