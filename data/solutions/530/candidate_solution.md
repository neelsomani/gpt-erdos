Write
[
s(A):=\max{|S|:S\subseteq A\ \text{is Sidon}},
\qquad
\ell(N)=\min_{|A|=N}s(A).
]
This is the usual “worst–case” size of the largest Sidon subset. In the integer setting this function is commonly denoted $g(n)$. 

## Upper bound: (\ell(N)\lesssim \sqrt N)

Take (A={1,2,\dots,N}). Then (\ell(N)\le s([N])=:f(N)). Classical results (Singer; Erdős–Turán; Bose–Chowla, etc.) imply
[
f(N)=\sqrt N(1+o(1))
]
[[nomath]](and in particular $f(N)\le \sqrt N+O(N^{1/4})$)[[/nomath]]. 
Hence
[
\ell(N)\le (1+o(1))\sqrt N.
]

[[nomath]](For just the order of magnitude, even the elementary counting bound in $[N]$ gives $f(N)\le 2\sqrt N+O(1)$ since $|S+S|=\binom{|S|+1}{2}\le 2N-1$.)[[/nomath]]

## Lower bound: (\ell(N)\gtrsim \sqrt N)

A theorem of Komlós–Sulyok–Szemerédi shows that there is an absolute constant (c>0) such that every finite set $A$ contains a Sidon subset of size at least (c|A|^{1/2}). This is stated (and used) in the real setting (A\subset\mathbb R) as well. 

Therefore,
[
\ell(N)\ge c\sqrt N.
]

[[nomath]](If you care about explicit constants: in the integer version $g(n)\ge c\sqrt n$ was proved by KSS with a tiny constant, and Abbott improved it to allow any $c<2/25$ for all sufficiently large $n$. )[[/nomath]]

## Conclusion: the order of (\ell(N))

Putting the two bounds together,
[
c\sqrt N \ \le\ \ell(N)\ \le\ (1+o(1))\sqrt N,
]
so
[
\boxed{\ \ell(N)=\Theta(\sqrt N)\ }.
]

## Is (\ell(N)\sim \sqrt N) [[nomath]](ratio $\to 1$)[[/nomath]]?

This is **not known**. In Abbott’s notation, one asks whether the worst–case $g(n)$ is asymptotically as large as (f(n)=s({1,\dots,n})), i.e.
[
\lim_{n\to\infty}\frac{g(n)}{f(n)}=1,
]
and Abbott explicitly notes that Erdős asked this and that it “has not been answered.” 

So: **the exponent $1/2$ is correct**, but the stronger statement (\ell(N)\sim \sqrt N) [[nomath]](constant $1$)[[/nomath]] remains open.
