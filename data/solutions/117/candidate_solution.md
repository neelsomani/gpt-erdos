Let

* (\omega(G)) = the largest size of a set (S\subseteq G) with **no two distinct elements commuting** (a “pairwise non‑commuting” set).
* (c(G)) = the **smallest** number of abelian subgroups whose union is (G).

Your hypothesis is exactly (\omega(G)\le n).
And (h(n)=\sup{c(G):\omega(G)\le n}) (then rounded up to the least integer that works for all such groups).

## Easy facts

1. If (G) is covered by (k) abelian subgroups, then (\omega(G)\le k).
   So always
   [
   h(n)\ \ge\ n .
   ]

2. If (\omega(G)) is finite, then (G) is **central-by-finite**, i.e. (|G:Z(G)|<\infty). This goes back to B. H. Neumann’s solution of Erdős’s question about infinite non‑commuting cliques. ([Cambridge University Press & Assessment][1])
   So (h(n)) is finite for each (n).

## A clean general upper bound: exponential

A very simple covering argument gives
[
c(G)\ \le\ |G:Z(G)|.
]
Reason: for each coset (gZ(G)), the subgroup (\langle g,,Z(G)\rangle) is abelian (it’s “cyclic times central”), and it contains the whole coset (gZ(G)). Taking one such subgroup for each coset covers all of (G).

So it is enough to bound (|G:Z(G)|) in terms of (\omega(G)).

Pyber proved that there is an absolute constant (C) such that for every finite group
[
|G:Z(G)|\ \le\ C^{\omega(G)} .
]

Putting this together:
[
\boxed{\ h(n)\ \le\ C^{,n}\ }\quad\text{for some absolute constant }C.
]

So the best known general upper bound is **exponential in (n)**.

## A strong lower bound: at least (\approx 2^{n/2})

There is a standard family that forces exponential growth.

Take an **extraspecial (2)-group** (E_m) of order (2^{2m+1}) (so (|Z(E_m)|=2)). ([MathOverflow][2])
It is known that
[
\omega(E_m)=2m+1.
]
([Umut Isik][3])

Now look at (V=E_m/Z(E_m)), which is a (2m)-dimensional vector space over (\mathbb F_2), with a nondegenerate alternating bilinear form coming from commutators. In this setting:

* If (A\le E_m) is abelian, we may replace it by (AZ(E_m)) (still abelian), so assume (Z(E_m)\le A).
* Then (A/Z(E_m)) is a totally isotropic subspace of (V).
* In a nondegenerate symplectic space of dimension (2m), any totally isotropic subspace has size at most (2^m), so (A) contains at most (2^m-1) nontrivial cosets of the center.

But (E_m/Z(E_m)) has (2^{2m}-1) nonzero vectors (nontrivial cosets). Therefore any cover of (E_m) by abelian subgroups needs at least
[
\frac{2^{2m}-1}{2^m-1}\ =\ 2^m+1
]
abelian subgroups.

On the other hand, there is an explicit partition of (V\setminus{0}) into exactly (2^m+1) totally isotropic (m)-subspaces (a “spread”), for example by identifying (V\cong \mathbb F_{2^m}^2) and taking the (2^m+1) one-dimensional (\mathbb F_{2^m})-subspaces (“lines through the origin”). Lifting these subspaces back to (E_m) gives (2^m+1) abelian subgroups covering (E_m).

So in fact
[
c(E_m)=2^m+1.
]

Since (\omega(E_m)=2m+1), this gives
[
h(2m+1)\ \ge\ 2^m+1 \ =\ 2^{(2m+1-1)/2}+1.
]

Equivalently, for all (n),
[
\boxed{\ h(n)\ \ge\ 2^{\lfloor (n-1)/2\rfloor}+1\ }.
]

So (h(n)) is **at least** on the order of ((\sqrt2)^{,n}).

## Best current estimate (shape)

Putting upper and lower bounds together:

[
\boxed{\ 2^{\lfloor (n-1)/2\rfloor}\ \lesssim\ h(n)\ \le\ C^{,n}\ }
]
for some absolute constant (C). ([Cambridge University Press & Assessment][1])

So the growth of (h(n)) is known to be **exponential in (n)**. The main remaining gap is the base of the exponential: we know it is at least (\sqrt2), and at most some absolute constant (C) coming from Pyber’s theorem.

If you want, I can also spell out the extraspecial (2)-group covering construction in full group-theoretic terms (no geometry language), since that example is what drives the lower bound.

[1]: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/43D46201BABB2E6319B72C008DC3F42B/S1446788700019303a.pdf/a-problem-of-paul-erdos-on-groups.pdf "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/43D46201BABB2E6319B72C008DC3F42B/S1446788700019303a.pdf/a-problem-of-paul-erdos-on-groups.pdf"
[2]: https://mathoverflow.net/questions/311654/number-of-elementary-abelian-subgroups-of-extraspecial-2-groups "https://mathoverflow.net/questions/311654/number-of-elementary-abelian-subgroups-of-extraspecial-2-groups"
[3]: https://www.isik.dev/files/nc.pdf "https://www.isik.dev/files/nc.pdf"
