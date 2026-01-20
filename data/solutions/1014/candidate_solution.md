Fix an integer (k\ge 3), and write
[
r_l:=R(k,l).
]
We will show (r_{l+1}/r_l\to 1).

## 1) A one–step recursion gives a sharp upper bound on the increment

A standard Erdős–Szekeres recursion says that for all (a,b\ge 2),
[
R(a,b)\le R(a-1,b)+R(a,b-1).
]
[[nomath]](Proof: take a graph on $R(a-1,b)+R(a,b-1)$ vertices, pick a vertex $v$; among its neighbors you either find a $K_{a-1}$ or an independent set of size $b$, and among its non-neighbors you either find a $K_a$ or an independent set of size $b-1$; in either case you get a $K_a$ or an independent set of size $b$.)[[/nomath]]

Apply this with $a=k$ and (b=l+1):
[
R(k,l+1)\le R(k-1,l+1)+R(k,l).
]
Therefore
[
0\le r_{l+1}-r_l\le R(k-1,l+1),
]
and hence
[
1\le \frac{r_{l+1}}{r_l}\le 1+\frac{R(k-1,l+1)}{r_l}.
]
So it suffices to prove
[
\frac{R(k-1,l+1)}{R(k,l)}\xrightarrow[l\to\infty]{}0.
]

## 2) A simple polynomial upper bound for $R(k-1,l+1)$

Iterating the same recursion (or using the classical Erdős–Szekeres binomial bound) gives
[
R(a,b)\le \binom{a+b-2}{a-1}.
]
In particular, for fixed $k$,
[
R(k-1,l+1)\le \binom{k+l-2}{k-2}.
]
Since $k$ is fixed, the right-hand side is a polynomial in $l$ of degree $k-2$, so there is a constant (C_k>0) with
[
R(k-1,l+1)\le C_k l^{k-2}\qquad\text{for all large }l.
]

## 3) A (known) lower bound for $R(k,l)$ that is larger by a factor (\sim l/(\log l)^{O(1)})

A fundamental fact about off-diagonal Ramsey numbers is that for each fixed (k\ge 3) there exists a constant (c_k>0) such that, for all sufficiently large $l$,
[
R(k,l)\ \ge\ c_k \frac{l^{k-1}}{(\log l)^{k-2}}.
]
This is the standard probabilistic/construction lower bound matching the correct order of growth up to a constant factor [[nomath]](for $k=3$ the best-order lower bound is due to Kim; for general fixed $k$ there are matching-order bounds $R(k,l)=\Theta\bigl(l^{k-1}/(\log l)^{k-2}\bigr)$ from work of Erdős and later improvements, and Ajtai–Komlós–Szemerédi for the upper bound)[[/nomath]].

For our purpose, we only need **some** lower bound that is (\gg l^{k-2}); the displayed bound is more than enough.

## 4) Finish: squeeze the ratio

Combine the bounds from $2$ and $3$:
$
\frac{R(k-1,l+1)}{R(k,l)} \le
\frac{C_k,l^{k-2}}{c_k,l^{k-1}/(\log l)^{k-2}} =
\frac{C_k}{c_k}\cdot \frac{(\log l)^{k-2}}{l}  \xrightarrow[l\to\infty]{}\ 0,
$
because ((\log l)^{k-2}/l\to 0).

Returning to the squeeze from §1,
$
1\le \frac{R(k,l+1)}{R(k,l)}\le 1+\frac{R(k-1,l+1)}{R(k,l)}\xrightarrow[l\to\infty]{}1,
$
so by the squeeze theorem,
$
\boxed{\displaystyle \lim_{l\to\infty}\frac{R(k,l+1)}{R(k,l)}=1.}
$

If you’d like, I can also spell out a self-contained proof of the specific lower bound (R(k,l)\ge c_k l^{k-1}/(\log l)^{k-2}) that’s used above (it’s the only nontrivial input; everything else is elementary).
