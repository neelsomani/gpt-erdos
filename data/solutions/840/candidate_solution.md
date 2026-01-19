A quasi‑Sidon set (A\subset{1,\dots,N}) has “almost all” pairwise sums distinct, in the sense that
[
|A+A|=(1+o(1))\binom{|A|}{2}\sim \frac{|A|^2}{2}.
]

### Order of magnitude

Since (A+A\subset{2,3,\dots,2N}), we always have (|A+A|\le 2N-1). If (|A|=k), the quasi‑Sidon condition gives (|A+A|\sim k^2/2), so
[
\frac{k^2}{2}\lesssim 2N \quad\Rightarrow\quad k=O(\sqrt N).
]
So $f(N)$ must grow on the scale (\sqrt N). ([Erdős Problems][1])

### Best known bounds (constant-factor gap remains)

Erdős and Freud already showed that
[
\left(\frac{2}{\sqrt3}+o(1)\right)\sqrt N \le f(N)\le (2+o(1))\sqrt N,
]
so in particular (f(N)=\Theta(\sqrt N)). ([Erdős Problems][1])

Moreover, Pikhurko improved the upper constant to
[
f(N)\le \left(\left(\frac14+\frac{1}{(\pi+2)^2}\right)^{-1/2}+o(1)\right)\sqrt N
= (1.863\ldots+o(1))\sqrt N. \ ([Erdős Problems][1])

So the current best asymptotic constants are
[
1.1547\ldots=\frac{2}{\sqrt3}\ \le\ \liminf_{N\to\infty}\frac{f(N)}{\sqrt N}
\ \le\ \limsup_{N\to\infty}\frac{f(N)}{\sqrt N}
\ \le\ 1.863\ldots
]
and determining the true constant (or even substantially narrowing this gap) is the open part of the problem. ([Erdős Problems][1])

### A word on the lower-bound construction

The Erdős–Freud lower bound ((2/\sqrt3+o(1))\sqrt N) comes from taking a genuine Sidon set (B\subset[1,N/3]) of size (\sim \sqrt{N/3}) and forming
[
A:=B\ \cup\ {,N-b: b\in B,},
]
which roughly doubles the size while keeping the number of repeated sums negligible compared to (\binom{|A|}{2}), hence quasi‑Sidon. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/latex/840 "
  
    Erdős Problems
  
"
