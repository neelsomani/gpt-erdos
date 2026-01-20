This is **open** (no proof or disproof is known).

It appears as **Erdős Problem #463** (attributed to Erdős–Graham and later Erdős again), and the Erdős Problems database currently lists it as open. ([Erdős Problems][1])

### A couple of useful reformulations

Write $p(m)$ for the least prime factor of $m$, and set (d:=m-n>0).
Your inequality
$
n+f(n)<m<n+p(m)
$
is equivalent to the existence [[nomath]](for each large $n$)[[/nomath]] of a **composite** (m=n+d) with
$
f(n)< d < p(m).
$
So you are asking whether one can force (d\to\infty) **uniformly for all large $n$**, while still having (d<p(m)).

Also note that
[
m<n+p(m)\quad\Longleftrightarrow\quad m-p(m)<n.
]
Erdős asked in [Er92e] about the related function
[
F(n)=\min_{m>n}(m-p(m)),
]
and whether (n-F(n)\sim c,n^{1/2}) for some (c>0). ([Erdős Problems][1])

### A necessary growth restriction on $f$

If $m$ is composite then (p(m)\le \sqrt m). So from (m-n < p(m)) we get
[
m-n < \sqrt m \sim \sqrt n,
]
which means any such $f$ (if it exists) cannot grow faster than a constant multiple of (\sqrt n). [[nomath]](In particular you can’t hope for $f(n)$ of order $n^\alpha$ with $\alpha>1/2$.)[[/nomath]]

### Why this is believed hard

This question is closely related to Erdős Problem #385 [[nomath]](a “reverse-direction” version involving $\max_{m<n} (m+p(m))$)[[/nomath]], and Tao has explained that #385 is tied up with deep limitations of sieve theory (the **parity problem**) and subtle issues like possible Siegel zero obstructions. ([What's new][2])

Very roughly: proving statements like “every interval at scale between (\log n) and (\sqrt n) contains a semiprime with controlled prime factors” is far beyond what current unconditional methods can guarantee uniformly for **every** $n$. ([What's new][2])

### What *is* easy (but doesn’t solve it)

There are plenty of **individual** $n$ for which such an $m$ exists with quite large $m-n$. For instance, if (m=p^2) with $p$ prime, then for any $n$ in the range (p^2-p < n < p^2) we have (m-n < p = p(m)), so those $n$ admit solutions with $m-n$ as large as (p-1 \asymp \sqrt n).
The hard part is covering **all** sufficiently large $n$ with a single (f(n)\to\infty).

So the honest answer is: **nobody currently knows** whether such an $f$ exists. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/forum/thread/463 "https://www.erdosproblems.com/forum/thread/463"
[2]: https://terrytao.wordpress.com/2024/08/19/erdos-problem-385-the-parity-problem-and-siegel-zeroes/ "https://terrytao.wordpress.com/2024/08/19/erdos-problem-385-the-parity-problem-and-siegel-zeroes/"
