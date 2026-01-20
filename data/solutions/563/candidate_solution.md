As written [[nomath]](“**largest** $m$”)[[/nomath]], the parameter is trivial: for any (0\le \alpha<\tfrac12) you can pick a colouring with, say, about half the edges red/blue, and then taking $m=n$ makes the condition apply only to (X=[n]), so (F(n,\alpha)=n).
The interesting (and standard) formulation—e.g. Erdős Problem #563—is with **“smallest”** $m$, and in that form it is explicitly listed as **OPEN** to prove the full asymptotic constant. ([Erdős Problems][1])

So below I do two things:

1. I give a complete proof that for every fixed (0\le \alpha<\tfrac12),
   [
   F(n,\alpha)=\Theta_\alpha(\log n),
   ]
   including an essentially sharp upper bound constant from the random colouring.

2. I explain why upgrading (\Theta(\log n)) to (\sim c_\alpha\log n) [[nomath]](existence of the limit constant $c_\alpha$)[[/nomath]] is currently an open problem in general [[nomath]](already at $\alpha=0$ it ties into the famous “Ramsey limit” problem)[[/nomath]]. ([Erdős Problems][1])

Throughout I use (\ln) for the natural logarithm; switching log base just rescales constants.

---

## 1. Reformulation and a monotonicity lemma

Fix a 2‑colouring of $E(K_n)$. Let $G$ be the red graph. For (X\subseteq[n]) write
[
e_G(X)=|\\{\text{red edges inside }X\\}|.
]
Then the condition “$X$ contains more than (\alpha\binom{|X|}{2}) edges of **each** colour” is exactly
[
\alpha\binom{|X|}{2}<e_G(X)<(1-\alpha)\binom{|X|}{2}.
\tag{★}
]

A useful fact is that it is enough to check sets of **exactly** one size.

**Lemma (averaging down).**
Fix (m\le t). If some $t$-set $X$ violates the lower bound in (★), i.e.
[
e_G(X)\le \alpha\binom{t}{2},
]
then $X$ contains an $m$-subset (Y\subseteq X) with
[
e_G(Y)\le \alpha\binom{m}{2}.
]
Similarly, if (e_G(X)\ge (1-\alpha)\binom{t}{2}), then some $m$-subset (Y\subseteq X) also satisfies (e_G(Y)\ge(1-\alpha)\binom{m}{2}).

*Proof.* Choose $Y$ uniformly among the (\binom{t}{m}) $m$-subsets of $X$. Each red edge of $X$ lands inside $Y$ with probability (\binom{m}{2}/\binom{t}{2}). Hence
[
\mathbb E,e_G(Y)=e_G(X)\cdot \frac{\binom{m}{2}}{\binom{t}{2}}
\le \alpha\binom{m}{2}.
]
So some $Y$ has (e_G(Y)\le\alpha\binom{m}{2}). The upper-tail version is identical. ∎

**Consequence.** A colouring satisfies (★) for **all** (|X|\ge m) iff it satisfies (★) for **all** (|X|=m).

So from now on, we can talk about “no bad $m$-set”.

---

## 2. Upper bound (F(n,\alpha)\le \bigl(\frac{2}{D(\alpha|1/2)}+o(1)\bigr)\ln n)

Let us colour edges independently red/blue with probability $1/2$ each.

Fix $t$ and a particular $t$-set $X$. Then
[
e_G(X)\sim \mathrm{Bin}\left(\binom{t}{2},,\tfrac12\right).
]
For (\alpha<\tfrac12), a standard Chernoff/Cramér bound gives
[
\Pr\left[e_G(X)\le \alpha\binom{t}{2}\right]\le
\exp\\(-\binom{t}{2},D(\alpha|1/2)\\),
]
and by symmetry the same bound holds for (\Pr[e_G(X)\ge (1-\alpha)\binom{t}{2}]). Thus
[
\Pr[X\text{ is bad}]\le2\exp\\(-\binom{t}{2},D(\alpha|1/2)\\),
\tag{1}
]
where the Kullback–Leibler divergence is
[
D(\alpha|1/2)
=\alpha\ln\frac{\alpha}{1/2}+(1-\alpha)\ln\frac{1-\alpha}{1/2}
=\alpha\ln(2\alpha)+(1-\alpha)\ln(2(1-\alpha))>0.
]

Let (B_t) be the number of bad $t$-subsets. By linearity of expectation and $1$,
[
\mathbb E B_t
\le \binom{n}{t}\cdot 2\exp\\(-\binom{t}{2},D(\alpha|1/2)\\)
\le 2,n^t,\exp\\(-\tfrac{D(\alpha|1/2)}{2},t(t-1)\\).
\tag{2}
]

Now set
[
m=\left(\frac{2}{D(\alpha|1/2)}+\varepsilon\right)\ln n
]
for a fixed (\varepsilon>0). For any (t\ge m), the exponent in $2$ satisfies
[
t\ln n-\frac{D}{2}t(t-1)
\le t\ln n-\frac{D}{2}t^2+O(t)
= -\left(\frac{D}{2}t-\ln n\right)t+O(t).
]
But for (t\ge m),
[
\frac{D}{2}t-\ln n
\ge \frac{D}{2}\left(\frac{2}{D}+\varepsilon\right)\ln n-\ln n
= \frac{D\varepsilon}{2}\ln n,
]
so
[
t\ln n-\frac{D}{2}t(t-1)\le -\frac{D\varepsilon}{2},t,\ln n+O(t)
\le -c(\alpha,\varepsilon),(\ln n)^2
]
for some (c(\alpha,\varepsilon)>0) and all large $n$.

Therefore (\mathbb E B_t\le \exp(-c(\ln n)^2)), and summing over (t\ge m) gives
[
\mathbb E\@@MATH_0@@=o(1).
]
So with positive probability there are **no** bad $t$-sets for any (t\ge m). Hence there exists a colouring for which every (|X|\ge m) satisfies (★), and therefore
[
F(n,\alpha)\le \left(\frac{2}{D(\alpha|1/2)}+o(1)\right)\ln n.
\tag{3}
]

This is the standard “random colouring + union bound” upper bound.

---

## 3. Lower bound (F(n,\alpha)\ge c,\ln n) for a universal (c>0)

A crude but clean lower bound comes from the existence of monochromatic cliques (i.e. the ordinary Ramsey guarantee).

Let $R(k,k)$ be the diagonal Ramsey number. The classical Erdős–Szekeres bound gives
[
R(k,k)\le \binom{2k-2}{k-1}\le 4^k.
]
Thus if (n\ge 4^k), every 2‑colouring of (K_n) contains a monochromatic (K_k).

Take
[
k=\left\lfloor \log_4 n \right\rfloor = \left\lfloor \frac{1}{2}\log_2 n \right\rfloor.
]
Then every colouring of (K_n) has a monochromatic $k$-set $X$. Inside $X$, one colour has **zero** edges, so (★) fails for every (\alpha\ge 0). Consequently no colouring can satisfy (★) for all (|X|\ge k), hence
[
F(n,\alpha)\ge k+1 = \left(\frac{1}{2\ln 2}+o(1)\right)\ln n.
\tag{4}
]

Combining $3$ and $4$ proves the “easy” statement:
[
F(n,\alpha)=\Theta_\alpha(\ln n)\qquad(0\le \alpha<\tfrac12),
]
which is exactly what the Erdős problem page notes is straightforward. ([Erdős Problems][1])

---

## 4. About the requested asymptotic (F(n,\alpha)\sim c_\alpha\log n)

To strengthen (\Theta(\log n)) to
[
F(n,\alpha)\sim c_\alpha \log n
]
one needs to prove that the ratio (F(n,\alpha)/\log n) actually converges.

This is **not** currently known in general: Erdős Problem #563 asks precisely for this, and it is listed as **OPEN**. ([Erdős Problems][1])

Moreover, the case (\alpha=0) essentially encodes the famous “Ramsey limit” question about whether (\lim_{k\to\infty}R(k,k)^{1/k}) exists; that problem is also explicitly listed as open. ([Erdős Problems][2])

What *is* known (and what we proved above) is the order of growth (\Theta(\log n)) plus a very suggestive candidate for the constant from the random construction:

* Random colouring gives an **upper bound** with constant
  [
  c_\alpha^{\text{(upper)}}=\frac{2}{D(\alpha|1/2)}
  =\frac{2}{\alpha\ln(2\alpha)+(1-\alpha)\ln(2(1-\alpha))}.
  ]
* Proving the matching **lower bound**
  [
  F(n,\alpha)\ge \left(\frac{2}{D(\alpha|1/2)}-o(1)\right)\ln n
  ]
  for *every* colouring (or even showing the limit exists at all) is the difficult open part.

So the fully requested statement “(F(n,\alpha)\sim c_\alpha\log n) for some (c_\alpha)” is not something one can currently justify from known results; the best unconditional statement is (F(n,\alpha)=\Theta_\alpha(\log n)), with the explicit upper bound $3$ and the universal lower bound $4$. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/563 "https://www.erdosproblems.com/563"
[2]: https://www.erdosproblems.com/forum/thread/77 "https://www.erdosproblems.com/forum/thread/77"
