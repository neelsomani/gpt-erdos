Let $R(N)$ denote the maximum size of a set (A\subseteq{1,\dots,N}) such that the map
[
S\subseteq A \ \longmapsto\ \sum_{n\in S}\frac1n
]
is injective (i.e., all these subset–reciprocal sums are distinct).

This is **Erdős problem #321**, and the exact asymptotic growth of $R(N)$ is **open**. ([Erdős Problems][1])

## Easy lower bound: (R(N)\gtrsim N/\log N)

A clean sufficient condition is that the denominators are **pairwise coprime**. If (A={n_1,\dots,n_m}) and (\gcd(n_i,n_j)=1) for (i\neq j), then any equality of two subset sums
[
\sum_{i\in S}\frac1{n_i}=\sum_{i\in T}\frac1{n_i}
]
implies $S=T$: multiply by (P=\prod_i n_i) to get an integer relation (\sum \varepsilon_i \frac{P}{n_i}=0) with (\varepsilon_i\in{-1,0,1}), and reduce mod (n_i) to force (\varepsilon_i=0) for each $i$.

So taking $A$ to be the set of all primes (\le N) gives
[
R(N)\ \ge\ \pi(N)\ \sim\ \frac{N}{\log N}.
]

## Best known general bounds (Bleicher–Erdős)

Write (\log_1 N=\log N), (\log_2 N=\log\log N), etc. for iterated natural logarithms.

Results of Bleicher and Erdős imply the following (as quoted on the Erdős problems site): for suitable parameters $k,r$,
[
\frac{N}{\log N}\prod_{i=3}^k \log_i N \ \le\ R(N)\ \le\ \frac{1}{\log 2},\log_r N\left(\frac{N}{\log N}\prod_{i=3}^r \log_i N\right),
]
valid for any (k\ge 4) with (\log_k N\ge k) and any (r\ge 1) with (\log_{2r} N\ge 1). ([Erdős Problems][1])

A particularly readable concrete instance [[nomath]](take $k=r=4$)[[/nomath]] is that for sufficiently large $N$,
[
\frac{N}{\log N},\log_3 N,\log_4 N
\ \lesssim\
R(N)
\ \lesssim
\frac{1}{\log 2},\frac{N}{\log N},\log_3 N,(\log_4 N)^2.
]
This is just the general inequality specialized, and already shows that $R(N)$ is bigger than (N/\log N) by an extra iterated-log factor. ([Erdős Problems][1])

## A compact way to summarize the growth

Those bounds imply that $R(N)$ is pinned down up to subpolynomial factors in (\log_3 N); equivalently,
[
R(N)\ =\ \frac{N}{\log N},(\log_3 N)^{1+o(1)}
\qquad (N\to\infty),
]
but the finer structure (e.g. the “right” iterated-log product, constants, etc.) is not known.

So: **the exact answer is unknown**, but **the best established range** is the Bleicher–Erdős iterated-log sandwich above. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/forum/thread/321 "https://www.erdosproblems.com/forum/thread/321"
