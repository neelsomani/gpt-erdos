Let $R(k,\ell)$ denote the usual 2–colour Ramsey number.

### 1. Status of the statement you ask to prove

The claim

[
\exists,c>0\ \text{ such that }\ \lim_{k\to\infty}\frac{R(k+1,k)}{R(k,k)} > 1+c
]

is **a well-known open problem** (posed by Erdős and Sós, listed as Erdős Problem #1030). In particular, it is explicitly recorded as open, and even much weaker superlinear lower bounds on the *difference* (R(k+1,k)-R(k,k)) are not known. ([Erdős Problems][1])

So there is currently no published proof (as of the sources cited) establishing such a constant (c>0).

### 2. What *is* known unconditionally (and why it’s far from what you want)

Write
[
r_k := R(k,k),\qquad s_k := R(k+1,k).
]

#### A “trivial” linear lower bound on the difference

One can always get a linear additive gap (not multiplicative):

**Claim.** (R(k+1,k)\ge R(k,k)+k-1) for all (k\ge2).

**Proof.** Let (n=r_k-1). By definition of (r_k), there exists a red/blue colouring of (K_n) with **no** red (K_k) and **no** blue (K_k).

Now add a new set $B$ of $k-1$ vertices. Keep the colouring on the old vertex set $A$ as it was, and colour:

* every edge inside $B$ **blue**;
* every edge between $A$ and $B$ **red**.

Check forbidden configurations:

* **No blue (K_k):** any blue clique cannot use vertices from both $A$ and $B$ because all cross-edges are red. So a blue (K_k) would have to lie entirely inside $A$ (impossible by construction) or entirely inside $B$ [[nomath]](impossible since $|B|=k-1$)[[/nomath]].

* **No red (K_{k+1}):** any red clique can use at most one vertex from $B$ because edges inside $B$ are blue. So a red clique has size at most (1+(k-1)=k) [[nomath]](since $A$ contains no red $K_k$)[[/nomath]].

Thus we have a colouring on (n+(k-1)=r_k+k-2) vertices avoiding red (K_{k+1}) and blue (K_k), hence
[
R(k+1,k) \ge (r_k+k-2)+1 = r_k+k-1.\quad\square
]

The Erdős-problems page phrases a very similar “trivial” bound as (R(k+1,k)-R(k,k)\ge k-2). ([Erdős Problems][1]) [[nomath]](The minor $+1$ improvement above comes from choosing $k-1$ new vertices.)[[/nomath]]

#### Best published improvement is still only linear

Burr–Erdős–Faudree–Schelp (1989) proved the stronger linear bound
[
R(k+1,k)-R(k,k)\ \ge\ 2k-5.
]
([Erdős Problems][1])

#### Why this doesn’t give a constant-factor ratio

Even the stronger $2k-5$ difference yields only
[
\frac{R(k+1,k)}{R(k,k)}
\ge
1+\frac{2k-5}{R(k,k)}.
]

But $R(k,k)$ grows at least exponentially in $k$; e.g. Erdős’ classical probabilistic lower bound gives
[
R(k,k) \ge (1+o(1))\frac{k}{\sqrt{2}e},2^{k/2}.
]
([Wikipedia][2])

So (\frac{k}{R(k,k)}\to 0), and all known additive bounds imply only
[
\frac{R(k+1,k)}{R(k,k)} \ge 1+o(1),
]
which is **much weaker** than (>1+c) for a fixed (c>0).

### 3. Why proving a fixed (c>0) is hard (and what it seems to require)

Erdős and Sós noted that they “could not even prove” that
[
R(k+1,k)-R(k,k) > k^c \quad\text{for any } c>1,
]
let alone a multiplicative gap (\Omega(R(k,k))). ([Erdős Problems][1])

A natural strategy (discussed on MathOverflow) is to start with an extremal $(k,k)$-avoiding colouring on $R(k,k)-1$ vertices and try to add many new vertices, colouring new edges randomly and using a first-moment/LLL argument. This runs into the need for strong information about how many $(k-1)$-cliques of each colour exist in such extremal colourings—an area tied to “Ramsey multiplicity,” where essentially “nothing is known” at the needed strength. ([MathOverflow][3])

---

## Bottom line

What you asked to prove is **not currently known**: it’s a classical Erdős–Sós open problem (Erdős Problem #1030). ([Erdős Problems][1])

Unconditionally, the best general results are only **linear** lower bounds on the difference $R(k+1,k)-R(k,k)$ [[nomath]](e.g. $\ge 2k-5$)[[/nomath]], which are far too small to imply any fixed multiplicative gap $1+c$. ([Erdős Problems][1])

If you want, I can also:

* rewrite the above as a clean “lecture-note style” summary (definitions, known bounds, and the precise obstacle), or
* show how a strong enough “multiplicity” statement about $(k-1)$-cliques in $(k,k)$-Ramsey colourings would *imply* such a constant $c$ via the random-extension heuristic discussed in the MO thread.

[1]: https://www.erdosproblems.com/search_bib/Er93?sources_only=1 "
  
    Erdős Problems
  
"
[2]: https://en.wikipedia.org/wiki/Ramsey%27s_theorem?utm_source=chatgpt.com "Ramsey's theorem"
[3]: https://mathoverflow.net/questions/39823/differences-of-near-diagonal-ramsey-numbers "graph theory - Differences of near diagonal Ramsey numbers.  - MathOverflow"
