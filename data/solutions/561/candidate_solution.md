First, a small indexing remark: for
[
F_1=\bigcup_{i=1}^s K_{1,n_i}\qquad\text{and}\qquad
F_2=\bigcup_{j=1}^t K_{1,m_j},
]
the natural symmetric formula has the sum running to $s+t$:
[
\boxed{\ \hat R(F_1,F_2)\stackrel{?}= \sum_{k=2}^{s+t}\max{,n_i+m_j-1:\ i+j=k,}\ }.
]
[[nomath]](Your upper limit $s+2$ is exactly the special case $t=2$.)[[/nomath]]

This identity is the **Burr–Erdős–Faudree–Rousseau–Schelp conjecture** for size Ramsey numbers of star forests. 
What *is* known unconditionally (and is the easy direction) is the “(\le)” bound; the “(\ge)” bound is the hard part and is not proved in full generality as of the modern literature I can access. 

Below I give a complete proof of the **upper bound**
[
\hat R(F_1,F_2)\ \le\ \sum_{k=2}^{s+t}\max{n_i+m_j-1:\ i+j=k},
]
which is the standard construction behind the conjectured exact value.

---

## Step 0: Normalize the parameters

Because (F_1) and (F_2) are **unions of stars**, the order of the components does not matter, so we may assume
[
n_1\ge n_2\ge \cdots\ge n_s,\qquad
m_1\ge m_2\ge \cdots\ge m_t.
]

For each (k=2,3,\dots,s+t), define the “diagonal maximum”
[
a_k \ :=\ \max{,n_i+m_j-1:\ 1\le i\le s,\ 1\le j\le t,\ i+j=k,}.
]
[[nomath]](If there is no pair $(i,j)$ with $i+j=k$, the max is over the empty set; but for $k=2,\dots,s+t$ there is always at least one such pair.)[[/nomath]]

Let
[
M\ :=\ \sum_{k=2}^{s+t} a_k.
]

---

## Step 1: Construct a witness graph $H$ with $M$ edges

Let $H$ be the disjoint union of stars
[
H \ :=\ \bigcup_{k=2}^{s+t} K_{1,a_k}.
]
So $H$ has exactly
[
e(H)=\sum_{k=2}^{s+t} a_k = M
]
edges, and its components are pairwise vertex-disjoint.

---

## Step 2: Show (H \to (F_1,F_2))

Take an arbitrary red/blue coloring of the edges of $H$.

For each component (K_{1,a_k}), let

* (r_k) be the number of **red** edges in that star (i.e., red degree of its center),
* (b_k) be the number of **blue** edges in that star,

so
[
r_k+b_k=a_k\qquad\text{for each }k.
]

### A lattice-walk (induction) argument

We will process the stars in increasing $k$, maintaining integers $(i,j)$ where:

* $i$ = how many red star-components we have already “secured” for (F_1),
* $j$ = how many blue star-components we have already “secured” for (F_2),

starting from ((i,j)=(0,0)).

At step $k$ we will ensure
[
i+j = k-2.
]

Now fix a step (k\in{2,\dots,s+t}) and assume we currently have some $(i,j)$ with (i+j=k-2).

Consider the ((k))-th star component, whose total size is (a_k).

Because ((i+1)+(j+1)=k), the pair $(i+1,j+1)$ is allowed in the definition of (a_k), hence
[
a_k \ \ge\ n_{i+1}+m_{j+1}-1.
]

Now we claim:

> **Claim.** At least one of the following holds:
> [
> r_k\ge n_{i+1}\quad\text{or}\quad b_k\ge m_{j+1}.
> ]

**Proof of claim.**
If (r_k\le n_{i+1}-1), then
[
b_k=a_k-r_k \ \ge\ (n_{i+1}+m_{j+1}-1) - (n_{i+1}-1) \ =\ m_{j+1},
]
so (b_k\ge m_{j+1}). Otherwise (r_k\ge n_{i+1}). ∎

So at step $k$, we can always do one of:

* If (r_k\ge n_{i+1}), **increase $i$** (take this component as the next required red star).
* Otherwise (b_k\ge m_{j+1}), **increase $j$** (take it as the next required blue star).

Either way, after processing component $k$, we move from $(i,j)$ to either $(i+1,j)$ or $(i,j+1)$, so $i+j$ increases by $1$, maintaining the invariant (i+j=k-2) at step $k$.

After the final step (k=s+t), we have processed (s+t-1) components, hence
[
i+j = (s+t)-2 \quad\text{initially }0\text{ then after }(s+t-1)\text{ moves gives } i+j=s+t-1.
]
But always (0\le i\le s) and (0\le j\le t). The only way to have (i+j=s+t-1) is that
[
i=s \quad\text{or}\quad j=t.
]

* If $i=s$, then along the process we selected **$s$ distinct components** whose red sizes satisfy
  [
  r_{k_1}\ge n_1,\ r_{k_2}\ge n_2,\ \dots,\ r_{k_s}\ge n_s,
  ]
  so within each selected star component we can choose (n_\ell) red edges to realize a red copy of (K_{1,n_\ell}). Since the components are vertex-disjoint, the union is a red copy of
  [
  \bigcup_{\ell=1}^s K_{1,n_\ell} = F_1.
  ]

* If $j=t$, similarly we obtain a blue copy of (F_2).

Thus **every** 2-coloring of $E(H)$ yields a monochromatic (F_1) or (F_2), i.e.
[
H\to(F_1,F_2).
]

Therefore,
[
\hat R(F_1,F_2)\ \le\ e(H)=M=\sum_{k=2}^{s+t}\max{n_i+m_j-1:\ i+j=k}.
]

This proves the claimed formula as an **upper bound**.

---

## About the reverse inequality (\ge)

The matching lower bound
[
\hat R(F_1,F_2)\ \ge\ \sum_{k=2}^{s+t}\max{n_i+m_j-1:\ i+j=k}
]
(i.e. the *equality* you wrote) is exactly the longstanding conjecture of Burr–Erdős–Faudree–Rousseau–Schelp for star forests. 

It is known in a variety of special cases (starting with multiple copies of the *same* star, and further families handled in later work), but the general case is treated as open/partial in modern references I can access. 

---

If you tell me whether your intended exercise is the special case $t=2$ [[nomath]](which matches your summation limit $s+2$)[[/nomath]], or another of the known proved regimes (e.g. one side is a single star, or all stars on each side have the same size), I can write the **full equality proof** for that regime in the same level of detail as the upper bound above.
