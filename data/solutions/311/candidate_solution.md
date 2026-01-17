Let

[
\delta(N)\ :=\ \min\\{|1-\sum_{n\in A}\frac1n|\ :\ A\subseteq{1,\dots,N}\\}\cap(0,\infty).
]

This is the same quantity as in the Erdős–Graham formulation with the extra condition that $A$ contain no (S\subseteq A) with (\sum_{n\in S}1/n=1): if $A$ contains such a *proper* subset $S$, then
[
\sum_{n\in A}\frac1n-1=\sum_{n\in A\setminus S}\frac1n \ge \frac1N,
]
so such sets can only ever produce an error (\ge 1/N), which is not relevant once (\delta(N)\ll 1/N); moreover this equivalence is explicitly noted in the discussion of the problem. ([Erdős Problems][1])

### What is known

**1) Trivial (but essentially best-possible in form) lower bound.**
Every (\sum_{n\in A}1/n) is a rational with denominator dividing ([1,\dots,N]) (the lcm), hence (\delta(N)\ge 1/[1,\dots,N]). Using (\log [1,\dots,N]=(1+o(1))N), this gives
[
\delta(N)\ \ge\ \frac{1}{[1,\dots,N]}\ =\ e^{-(1+o(1))N}.
]
([Erdős Problems][1])

**2) Best current upper bound (as of Jan 2026).**
Quanyu Tang obtained the first “genuinely small” upper bound of the form
[
\delta(N)\ \le\ \exp\left(-c_0,\frac{N}{(\log N)^3(\log\log N)^3}\right)
]
for some absolute constant (c_0>0). This is recorded on the Erdős Problems discussion thread (and the associated note is linked there), with the bound described as coming from strengthening an ingredient of Liu–Sawhney. ([Erdős Problems][1])

So at present the state of the art is roughly
[
e^{-(1+o(1))N}\ \le\ \delta(N)\ \le\ \exp\left(-c,\frac{N}{(\log N)^3(\log\log N)^3}\right),
]
with a large gap between the lower and upper bounds.

### Is (\delta(N)=e^{-(c+o(1))N}) for some (c\in(0,1))?

This remains **open**. It is posed exactly in that form on the Erdős Problems site, and no exponential-in-(N) upper bound (\exp(-cN)) [[nomath]](with constant $c>0$)[[/nomath]] is currently known. ([Erdős Problems][1])

There is some small-(N) numerical evidence: the first values up to (N=25) were computed in the discussion, and for (3\le N\le 25) one observes a rough window
[
e^{-0.71N}\ \lesssim\ \delta(N)\ \lesssim\ e^{-0.52N}.
]
But this is only experimental data at tiny (N) and doesn’t constitute an asymptotic law. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/forum/thread/311 "https://www.erdosproblems.com/forum/thread/311"
