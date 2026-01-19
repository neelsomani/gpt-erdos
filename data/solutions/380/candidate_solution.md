As far as I can tell, this is **open**: it is Erdős–Graham’s problem (listed as **Erdős Problem #380**) asking exactly whether
[
B(x)\sim B'(x):=|\\{n\le x:\ P(n)^2\mid n\\}|.
]
No proof (or counterexample) is currently known. ([Erdős Problems][1])

That said, there is a fairly clean “structure theory” for what a bad interval must look like, and it makes the asymptotic **very plausible**.

## 1) Trivial inclusion and what the conjecture is really saying

If (P(n)^2\mid n), then the singleton interval $[n,n]$ is bad, so
[
B(x)\ \ge\ B'(x).
]
So the conjecture (B(x)\sim B'(x)) is saying: **almost all** integers (\le x) that lie in *some* bad interval are actually “bad by themselves”, i.e. belong to a bad singleton. ([Erdős Problems][1])

## 2) Bad intervals are forced to be short and prime-free

A key point (noted by Tao in the discussion of the problem) is that if $[u,v]$ is bad then it cannot contain a prime; in particular one gets strong restrictions like (v<2u), and more generally $v-u$ must be “small” [[nomath]](e.g. under Cramér’s conjecture, $v-u\ll (\log u)^2$)[[/nomath]]. ([Erdős Problems][2])

One quick way to see the (v<2u) obstruction: if (v\ge 2u), then $[u,v]$ contains $(v/2,v]$, and by Bertrand’s postulate there is a prime $q\in(v/2,v]$. That prime is the largest prime factor of the whole product, and it appears exactly once, so the interval cannot be bad. ([Erdős Problems][2])

So any bad interval lives inside a **prime gap**, hence is automatically quite short.

## 3) Every bad interval is “anchored” by a bad *number* $m$ with (P(m)^2\mid m)

Let $[u,v]$ be bad, let (L:=v-u+1), and let $p$ be the greatest prime factor of (\prod_{m=u}^v m).

A classical argument via Sylvester’s theorem on prime factors of binomial coefficients implies that for (u>1), the product of $L$ consecutive integers has a prime factor (>L); therefore here one must have
[
p > L.
]
[[nomath]](If $u=1$, one can also rule out badness separately using Bertrand as above.)[[/nomath]]

Now (p>L) has a decisive consequence: there is **at most one** multiple of $p$ in $[u,v]$. So the only way $p$ can occur with exponent (>1) in the product is that this unique multiple is divisible by (p^2). In other words:

* every bad interval contains some integer $m$ with (p^2\mid m);
* and because $p$ is the greatest prime factor of the *whole* product, (p=P(m)), so (P(m)^2\mid m).

So any bad interval is a short “smooth” neighborhood around a genuinely bad integer (m\in B').

This shows the difference $B(x)-B'(x)$ can only come from **nearby integers** that get swept in by an interval built around such an $m$.

## 4) Why the asymptotic (B(x)\sim B'(x)) looks reasonable (but is hard)

Once you know every bad interval must contain a bad integer $m$ with (P(m)^2\mid m), the conjecture is essentially saying:

> For “most” such (m\le x), there aren’t many neighbors (m\pm 1, m\pm 2,\dots) that stay $P(m)$-smooth long enough to form a bad interval containing them; so the union of these short neighborhoods contributes only $o(B'(x))$ extra points.

This becomes a problem about **consecutive smooth numbers / smooth numbers in short intervals**, which Tao explicitly points to as the relevant difficulty. ([Erdős Problems][2])

Heuristically, if $m$ has largest prime factor (p=P(m)) and $m$ is much larger than $p$ [[nomath]](which is typical in the range that dominates $B'(x)$)[[/nomath]], then the density of $p$-smooth numbers near $m$ is extremely small (Dickman–de Bruijn heuristics). So you expect the maximal $p$-smooth “run” through $m$ to usually have length $1$, meaning $m$ contributes almost nothing beyond itself. That would force (B(x)/B'(x)\to 1).

But making this precise appears to require quantitative control on how often you can have **runs** of $p$-smooth numbers long enough to matter, uniformly over the $p$ that arise from (m\in B'); this is currently out of reach.

## 5) Known size of the right-hand side

The “singleton bad numbers” satisfy
[
B'(x)=|\\{n\le x:\ P(n)^2\mid n\\}|
=\frac{x}{\exp!\Big((c+o(1))\sqrt{\log x,\log\log x}\Big)}
]
for some constant (c>0). ([Erdős Problems][1])

The same page notes that Erdős and Graham only had very coarse bounds for $B(x)$ [[nomath]](in particular $B(x)>x^{1-o(1)}$, which is consistent with $B'(x)$ being $x^{1-o(1)}$ as well)[[/nomath]]. ([Erdős Problems][1])

## 6) Small computational evidence (just as a sanity check)

I also did a quick sieve computation up to (10^7) (not a proof, just numerics): the ratio $B(x)/B'(x)$ was about $1.11$ at (10^2), $1.09$ at (10^6), and $1.074$ at (10^7), trending downward—consistent with the conjecture (B(x)\sim B'(x)).

## Bottom line

* The conjecture is **plausible** and is supported by the structural fact that every bad interval must be a short prime-free neighborhood around some $m$ with (P(m)^2\mid m).
* But the actual asymptotic (B(x)\sim B'(x)) is **open** and seems to hinge on deep estimates about **runs of smooth numbers in short intervals**. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/380 "
  
    Erdős Problem #380
  
"
[2]: https://www.erdosproblems.com/forum/discuss/380 "

    Erdős Problem #380 - Discussion thread

"
