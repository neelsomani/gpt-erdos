Write, for a finite set (A\subset\mathbb Z),
[
r_k(A):=\max{|B|:B\subseteq A\text{ and }B\text{ contains no }k\text{-term AP}}.
]
Then your quantity is
[
G_k(N)=\min_{\substack{A\subset\mathbb Z\ |A|=N}} r_k(A),
]
while
[
R_k(N)=r_k({1,2,\dots,N}).
]

## Basic comparison with (R_k(N))

Because ({1,2,\dots,N}) is one particular set of (N) integers, we immediately have
[
G_k(N)\le R_k(N).
]
Moreover, strict inequality can occur already for small (N): Riddell exhibited an (N=5) example (e.g. ({1,3,4,5,7})) showing (G_3(5)=3) but (R_3(5)=4), and also (G_3(14)=7< R_3(14)=8). ([Rényi Institute][1])

So (G_k(N)) is **not** identically equal to (R_k(N)).

## The Komlós–Sulyok–Szemerédi theorem: same order of magnitude

A deep theorem of Komlós, Sulyok, and Szemerédi (1975) implies that for each fixed (k) there is a constant (c_k>0) such that
[
G_k(N)\ \ge\ c_k,R_k(N)\qquad\text{for all }N.
]
Equivalently, (R_k(N)\le C_k,G_k(N)) for some constant (C_k) depending only on (k). ([Rényi Institute][1])

Combining with the trivial upper bound gives the clean sandwich:
[
c_k,R_k(N)\ \le\ G_k(N)\ \le\ R_k(N).
]
In particular,
[
G_k(N)=\Theta_k(R_k(N)),
]
i.e. (G_k(N)) and (R_k(N)) have the **same growth rate up to a multiplicative constant depending only on (k)**.

So “determining (G_k(N))” is essentially as hard as determining (R_k(N)): any known upper/lower bounds for (R_k(N)) automatically transfer to (G_k(N)) (up to constant factors).

## What does this say concretely? (Example (k=3))

The exact asymptotics of (R_3(N)) (hence also (G_3(N))) are unknown, but the best-known bounds imply the same style of bounds for (G_3(N)):

* **Lower bounds (Behrend/Rankin/Elkin/O’Bryant line):** there are very dense 3-AP-free subsets of ({1,\dots,N}), e.g. of size (N\exp(-C\sqrt{\log N})) up to subexponential factors; O’Bryant states explicit versions. ([arXiv][2])
* **Upper bounds (Kelley–Meka, improved by Bloom–Sisask):** if (A\subset{1,\dots,N}) has no nontrivial 3-term AP, then (|A|\le N\exp(-c(\log N)^{1/9})). ([arXiv][3])

By (G_3(N)=\Theta(R_3(N))), the same type of upper/lower bounds (up to constants) hold for (G_3(N)).

## Is (\displaystyle \lim_{N\to\infty}\frac{R_3(N)}{G_3(N)}=1)?

You always have (\frac{R_3(N)}{G_3(N)}\ge 1) (since (G_3(N)\le R_3(N))), and the KSS theorem gives a uniform upper bound (\frac{R_3(N)}{G_3(N)}\le C_3).

But whether the ratio actually tends to (1) is **open**. In fact, Erdős notes that it is *not even known* whether (G_3(N)<R_3(N)) for infinitely many (N), and suggests the optimistic possibility that for large (n) one might have (g_k(n)=r_k(n)) (in our notation, (G_k(N)=R_k(N))) or at least that the ratio tends to (1). ([Rényi Institute][1])

So the best current answer is:

* (G_3(N)) and (R_3(N)) are **within a constant factor** of each other for all (N),
* strict inequality happens for some small (N),
* the asymptotic limit (\lim_{N\to\infty}R_3(N)/G_3(N)) being (1) is **not proved** (and remains a natural conjecture). ([Rényi Institute][1])

[1]: https://www.renyi.hu/~p_erdos/1980-03.pdf "https://www.renyi.hu/~p_erdos/1980-03.pdf"
[2]: https://arxiv.org/abs/0811.3057 "https://arxiv.org/abs/0811.3057"
[3]: https://arxiv.org/abs/2309.02353 "https://arxiv.org/abs/2309.02353"
