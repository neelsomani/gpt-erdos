Let

[
A={1^k,2^k,3^k,\dots}\subset\mathbb N,\qquad
r_k(n):=1_A^{(k)}(n)
=|\\{(x_1,\dots,x_k)\in \mathbb N^k:\ x_1^k+\cdots+x_k^k=n\\}|,
]

[[nomath]](counting **ordered** representations; if you mod out by permutations you only change things by a factor $\le k!$, irrelevant for “$n^c$” questions)[[/nomath]].

## What one “expects” on average

A basic scaling argument shows the **average size is constant**. Indeed,
[
\sum_{m\le N} r_k(m)
=|\\{(x_1,\dots,x_k)\in\mathbb N^k:\ x_1^k+\cdots+x_k^k\le N\\}|.
]
Put (x_i=N^{1/k}y_i). The region (\sum y_i^k\le 1) in the positive orthant has fixed volume, so the count is (\asymp N). Hence the mean value of (r_k(n)) for (n\le N) is (\asymp 1). In particular there is **no global power-law growth** in a typical sense [[nomath]](many $n$ have $r_k(n)=0$, and among the representable ones, heuristically $r_k(n)$ is usually $O(1)$)[[/nomath]].

The real difficulty is the **maximal order** or “how large can (r_k(n)) get along some sequence of $n$?”

## What is known about large values

### A general lower bound for every (k\ge 3): sub-polynomial but unbounded

Hardy–Littlewood conjectured the famous **Hypothesis $K$** that for each fixed $k$,
[
r_k(n)\le n^\varepsilon \quad\text{for every }\varepsilon>0,
]
i.e. $r_k(n)=n^{o(1)}$. A 1936 paper of Erdős already proved that (r_k(n)) is **unbounded** and in fact that for each (k\ge 3) there are infinitely many $n$ with
[
r_k(n)\ \ge\ \exp\Big(c(k),\frac{\log n}{\log\log n}\Big)
\ =\ n^{,c(k)/\log\log n},
]
for some constant (c(k)>0). 

This grows faster than any power of (\log n), but it is still **smaller than (n^\varepsilon) for every fixed (\varepsilon>0)** once $n$ is large enough, because the exponent (c(k)/\log\log n\to 0).

So this result does **not** give a fixed (c>0) with (r_k(n)>n^c); it only shows a slowly growing (\limsup).

### The special case $k=3$: there *is* polynomial growth infinitely often

For cubes, Hypothesis $K$ is known to be **false**. Mahler (and also the presentation in Hardy–Wright/related discussions) gives an explicit parametric construction showing that infinitely often,
[
r_3(n)\ \gg\ n^{1/12}.
]
For example, it is known that every twelfth power (t^{12}) has (\gg t) representations as a sum of three **positive** cubes [[nomath]](hence $r_3(t^{12})\gg t=(t^{12})^{1/12}$)[[/nomath]]. 

One concrete identity (attributed in the literature to Gérardin and discussed in standard references) is of the shape
[
t^{12}=(t^4-9tm^3)^3+(3mt^3-9m^4)^3+(9m^4)^3,
]
and by letting $m$ range over (\asymp t) values where all three terms stay positive, one gets (\asymp t) distinct representations. ([MathOverflow][1])

So for **$k=3$**, the answer to your second question is **yes**: take (c=1/12) and (n=t^{12}), giving infinitely many $n$ with (r_3(n)\gg n^{1/12}). 

### For (k\ge 4): the “(n^c) infinitely often?” question is open

For (k\ge 4), the status of Hypothesis $K$ [[nomath]](and in particular whether one can force $r_k(n)$ to exceed a fixed power $n^c$ infinitely often)[[/nomath]] is **not settled** in the literature summarized in standard surveys: it is stated as open, with Erdős believing failure for all (k\ge 4) but without a proof. 

## Direct answers to your questions

1. **Order of growth of (1_A^{(k)}(n)):**

* In an *average* sense, (r_k(n)) has mean (\asymp 1) [[nomath]](since $\sum_{n\le N} r_k(n)\asymp N$)[[/nomath]].
* In a *maximal/limsup* sense, the exact order is unknown in general; it is connected to Hardy–Littlewood Hypothesis $K$. 

2. **Does there exist (c>0) and infinitely many $n$ with (1_A^{(k)}(n)>n^c)?**

* **Yes for $k=3$**: one can take (c=1/12) [[nomath]](e.g. along $n=t^{12}$)[[/nomath]]. 
* **For (k\ge 4)**: this is **open**. The best general lower bounds known are of the sub-polynomial form (n^{c(k)/\log\log n}), which do not imply (n^c) for fixed (c>0). 

If you tell me whether you want **ordered** or **unordered** representations [[nomath]](and whether $0^k$ is allowed)[[/nomath]], I can restate the same conclusions in your preferred normalization; none of the exponents change.

[1]: https://mathoverflow.net/questions/413031/how-many-cubes-are-the-sum-of-three-positive-cubes?utm_source=chatgpt.com "How many cubes are the sum of three positive cubes?"
