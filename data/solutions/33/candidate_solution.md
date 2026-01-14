Let
[
A(N):=\bigl|A\cap{1,\dots,N}\bigr|.
]
Your hypothesis says that (A) is an **additive complement of the squares**: for all sufficiently large (m) there exist (n\ge 0) and (a\in A) with (m=n^2+a). ([Erdős Problems][1])

## The (\liminf) question

Yes: in fact one knows a quantitative lower bound
[
\liminf_{N\to\infty}\frac{A(N)}{\sqrt N}\ \ge\ \frac{4}{\pi}\ \approx\ 1.2732395\ldots,
]
proved independently by Cilleruelo (1993), Habsieger (1995), and Balasubramanian–Ramana (2001). ([Erdős Problems][1])

So the answer to
[
\liminf_{N\to\infty}\frac{A(N)}{\sqrt N}>1?
]
is **yes** (indeed (\ge 4/\pi>1)). ([Erdős Problems][1])

(For context: Moser had already shown (\liminf>1.06).) ([Erdős Problems][1])

## The “smallest possible (\limsup)” question

Let
[
L_S:=\inf_A\ \limsup_{N\to\infty}\frac{A(N)}{\sqrt N},
]
where the infimum is over all such complements (A). This is **still open** as an exact value; only bounds are known. ([Erdős Problems][1])

### Best current lower bound (strictly bigger than (4/\pi))

A December 2025 preprint of Ding–Zhang proves an explicit absolute constant (c_0\approx 5.463\times10^{-5}) and deduces in particular that every additive complement (W) satisfies
[
\limsup_{N\to\infty}\frac{W(N)}{\sqrt N}\ \ge\ \frac{4}{\pi}\bigl(1+c_0\bigr).
]
([arXiv][2])

Numerically,
[
\frac{4}{\pi}(1+c_0)\approx 1.2733091\ldots
]
(using (c_0\approx 5.463\times 10^{-5}) as stated). ([arXiv][2])

So in particular (L_S>4/\pi) is now known. ([arXiv][2])

### Best current upper bound

The same preprint records an explicit construction of van Doorn giving an additive complement (W_0) with
[
\limsup_{N\to\infty}\frac{W_0(N)}{\sqrt N}\ \le\ 2\Bigl(\frac{1+\sqrt5}{2}\Bigr)^{5/2}\ \approx\ 6.66.
]
([arXiv][2])

### Summary of what is known (as of Jan 2026)

Putting these together,
[
1.2733091\ldots\ \le\ L_S\ \le\ 6.6603813\ldots,
]
and the exact value of (L_S) remains unknown. ([arXiv][2])

## Why (\frac{4}{\pi}) shows up (intuition)

A useful heuristic is that the number of pairs ((a,n)) with (a\in A) and (a+n^2\le N) is
[
\sum_{n^2\le N} A(N-n^2).
]
If (A(x)) behaved like (c\sqrt{x}), this sum looks like
[
c\sum_{n<\sqrt N}\sqrt{N-n^2}\ \approx\ c\int_0^{\sqrt N}\sqrt{N-t^2},dt
\ =\ c\cdot\frac{\pi}{4}N,
]
so to cover (\sim N) integers you’d need (c\gtrsim 4/\pi). The sharp (\liminf\ge 4/\pi) theorem makes this philosophy rigorous. ([arXiv][2])

If you want, I can also summarize how the Ding–Zhang argument upgrades “(\limsup\ge 4/\pi)” to a strict inequality by forcing a positive linear excess in (\sum_{n\le N} f(n)-N) and then converting that into a (\limsup) bound. ([arXiv][2])

[1]: https://www.erdosproblems.com/tags/additive%20basis "
  
    Erdős Problems
  
"
[2]: https://arxiv.org/pdf/2512.15407 "No exact on average additive complements of squares"
