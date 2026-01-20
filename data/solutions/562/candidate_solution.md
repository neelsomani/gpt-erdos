Let me restate your claim in a convenient “tower” language, then I’ll prove the *known* matching upper bound and the *best known* lower bound, and finally explain why the desired two–sided statement is (as of now) a famous open problem already for $r=3$.

Throughout, (\log^{(k)} x) means the $k$-fold iterated base‑2 logarithm, and I’ll write (t_k(x)) for the “tower function”
[
t_1(x)=x,\qquad t_{k+1}(x)=2^{t_k(x)}.
]
So (t_2(x)=2^x,\ t_3(x)=2^{2^x}), etc., and (\log^{(k)} t_{k+1}(x)=x).

With this notation, your statement
[
\log^{(r-1)} R_r(n)\asymp_r n
]
is equivalent to the existence of constants (0<c_r<C_r) such that
[
t_r(c_r n)\ \le\ R_r(n)\ \le\ t_r(C_r n),
]
i.e. “a tower of height $r-1$” with top exponent linear in $n$.

---

## 1) The (known) upper bound: (R_r(n)\le t_r(C_r n))

This is classical and comes from the Erdős–Rado “stepping‑down” recursion.

### Lemma (Erdős–Rado recursion)

For every (r\ge 3) and (n\ge r), letting (m=R_{r-1}(n-1)),
[
R_r(n)\ \le\ 2^{\binom{m}{r-1}} + (r-2).
\tag{ER}
]

#### Proof

Take
[
N:=2^{\binom{m}{r-1}}+(r-2)
]
and 2‑color all $r$-edges of ([N]={1,\dots,N}). We will greedily build vertices
[
v_1< v_2< \cdots < v_{m+1}
]
and nested “reservoir” sets
[
S_0\supset S_1\supset \cdots \supset S_m\neq\varnothing
]
with the key property:

> [[nomath]](**$\star_i$**)[[/nomath]] After choosing (v_1,\dots,v_i) [[nomath]](for $i\le m$)[[/nomath]], for every ((r-1))-subset
> (A\subseteq{v_1,\dots,v_i}), all $r$-edges (A\cup{x}) with (x\in S_i) have the **same** color.

Start with (S_0=[N]). For (i=0,1,\dots,r-3) we can simply set (v_{i+1}=\min S_i) and (S_{i+1}=S_i\setminus{v_{i+1}}); since (i+1<r-1), there are no $(r-1)$-subsets yet, so ((\star_{i+1})) holds vacuously. After $r-2$ steps we have
[
|S_{r-2}| = N-(r-2)=2^{\binom{m}{r-1}}.
]

Now suppose (r-2\le i\le m-1) and we already have ((\star_i)). Pick (v_{i+1}=\min S_i). Consider the family (\mathcal B) of all ((r-2))-subsets of ({v_1,\dots,v_i}); it has size (\binom{i}{r-2}).
For each (x\in S_i\setminus{v_{i+1}}), define its “color pattern”
[
F(x): \mathcal B \to {\text{red, blue}},\qquad F(x)(B)=\text{color}(B\cup{v_{i+1},x}).
]
There are at most (2^{\binom{i}{r-2}}) possible patterns. Partition (S_i\setminus{v_{i+1}}) by these patterns and let (S_{i+1}) be the largest class. Then
[
|S_{i+1}|\ \ge\ \frac{|S_i|-1}{2^{\binom{i}{r-2}}}.
\tag{1}
]
By construction, for every (B\in\mathcal B), all edges (B\cup{v_{i+1},x}) with (x\in S_{i+1}) have the same color, so ((\star_{i+1})) holds for ((r-1))-subsets that *include* (v_{i+1}). For ((r-1))-subsets not including (v_{i+1}), ((\star_{i+1})) holds because (S_{i+1}\subseteq S_i) and ((\star_i)) already held. Thus ((\star_{i+1})) holds.

Iterating $1$ from (i=r-2) to $m-1$ and using the binomial identity
[
\sum_{i=r-2}^{m-1}\binom{i}{r-2}=\binom{m}{r-1},
]
we get [[nomath]](ignoring the harmless “$-1$” terms, since the set sizes are huge)[[/nomath]]
[
|S_m|\ \ge\ \frac{|S_{r-2}|}{2^{\sum_{i=r-2}^{m-1}\binom{i}{r-2}}}
=\frac{2^{\binom{m}{r-1}}}{2^{\binom{m}{r-1}}}=1.
]
So (S_m\neq\varnothing), and we can pick (v_{m+1}\in S_m).

Now define a derived 2‑coloring (\chi) of ((r-1))-subsets of ({v_1,\dots,v_m}) by
[
\chi(A):=\text{color}(A\cup{v_{m+1}}).
]
This is well-defined because ((\star_m)) says the color of (A\cup{x}) is constant over all (x\in S_m).

Since (m=R_{r-1}(n-1)), the ((r-1))-uniform complete hypergraph on ({v_1,\dots,v_m}) contains a monochromatic $(r-1)$-clique $T$ of size $n-1$ in the coloring (\chi). Suppose (\chi) is red on all $(r-1)$-subsets of $T$.

I claim (T\cup{v_{m+1}}) is a red $r$-uniform clique of size $n$ in the original coloring. Take any $r$-subset (E\subseteq T\cup{v_{m+1}}). Order its vertices increasingly (x_1<\cdots<x_r). Then (x_1,\dots,x_{r-1}\in T). If (x_r=v_{m+1}), then $E$ is red by definition of (\chi). If (x_r\in T), then (x_r<v_{m+1}), and when the first $r-1$ vertices ({x_1,\dots,x_{r-1}}) were selected, property ((\star)) ensured that the color of ({x_1,\dots,x_{r-1},y}) is independent of the choice of later $y$, so in particular
[
\text{color}(x_1,\dots,x_r)=\text{color}(x_1,\dots,x_{r-1},v_{m+1})=\chi({x_1,\dots,x_{r-1}})=\text{red}.
]
Thus every $r$-subset of (T\cup{v_{m+1}}) is red, as desired.

So every 2-coloring of (K_N^{(r)}) contains a monochromatic (K_n^{(r)}), i.e. (R_r(n)\le N), proving (ER). ∎

### From the recursion to a tower upper bound

The recursion (ER) implies
[
R_r(n)\ \le\ 2^{\binom{R_{r-1}(n-1)}{r-1}} + O_r(1)\ \le\ 2^{(R_{r-1}(n-1))^{r-1}}.
]
Starting from the standard graph bound (R_2(n)\le 4^n), iterating this inequality in $r$ yields
[
R_r(n)\ \le\ t_r(C_r n)
]
for some constant (C_r) depending only on $r$. [[nomath]](The point is that taking a fixed power $(\cdot)^{r-1}$ only changes the “top exponent” by a constant factor, which can be absorbed into $C_r n$.)[[/nomath]]

Consequently,
[
\log^{(r-1)} R_r(n)\ \le\ C_r n.
\tag{2}
]

So the **upper** half of your desired (\asymp_r n) statement is true.

---

## 2) The (known) lower bound: one fewer exponential than conjectured

Here the situation changes: the matching lower bound (R_r(n)\ge t_r(c_r n)) is **not known**, and already the case $r=3$ is a famous open problem. What we *can* prove is a tower of height $r-2$:

### Step 1: a base lower bound for $r=3$ by the probabilistic method

A random 2-coloring of triples shows there exists (c>0) such that
[
R_3(n)\ \ge\ 2^{c n^2}.
\tag{3}
]
Sketch: for (N=2^{c n^2}), the expected number of monochromatic (K_n^{(3)}) is
[
\mathbb E[|\text{ mono }K_n^{(3)}|]\le 2\binom{N}{n}2^{-\binom{n}{3}},
]
which is (<1) for small enough (c<1/6) and $n$ large, so some coloring has none.

These are the classical best-known lower bounds for $r=3$: Erdős–Hajnal–Rado proved (2^{c n^2}< r_3(n)<2^{2^{c'n}}). ([ETH Zurich Math Homepages][1])

### Step 2: stepping-up lemma gives one extra exponential per uniformity increment [[nomath]](starting at $k=3$)[[/nomath]]

A standard tool is the **Erdős–Hajnal stepping‑up lemma**. One convenient formulation is:

> **Stepping‑up lemma.** If (k\ge 3) and there is an (\ell)-coloring of the $k$-tuples of an $N$-set with no monochromatic $n$-set, then there is an (\ell)-coloring of the ((k+1))-tuples of a (2^N)-set with no monochromatic ((2n+k-4))-set. ([ETH Zurich Math Homepages][1])

In 2‑color Ramsey language this implies a recurrence of the form
[
R_{k+1}(2n+k-4)\ >\ 2^{R_k(n)-1}.
\tag{4}
]

Iterating $4$ starting from the $k=3$ lower bound $3$ yields, for each fixed (r\ge 3),
[
R_r(n)\ \ge\ t_{r-1}(c_r n^2)
\tag{5}
]
for some (c_r>0) [[nomath]](indeed Conlon–Fox–Sudakov show a clean statement $r_k(n)\ge t_{k-1}(c n^2)$ for $n$ sufficiently large compared to $k$)[[/nomath]]. ([ETH Zurich Math Homepages][1])

**Important:** (t_{r-1}) is a tower of height $r-2$. So $5$ is *one exponential shorter* than the conjectured (t_r(c_r n)).

In iterated‑log terms, $5$ gives only
[
\log^{(r-1)} R_r(n)\ \ge\ \log(c_r n^2)\ =\ \Theta(\log n),
\tag{6}
]
not (\Omega(n)).

---

## 3) What is actually known, and what is open

Putting together $2$ and $5$, the best general bounds for fixed (r\ge 3) are of the form
[
t_{r-1}(c_r n^2)\ \le\ R_r(n)\ \le\ t_r(C_r n),
]
i.e. a **one-exponential gap** between lower and upper bounds. This “one exponential” gap is already visible at $r=3$:
[
2^{c n^2}\ \le\ R_3(n)\ \le\ 2^{2^{C n}}.
]
These bounds (and the conjectured improvement) are explicitly stated in the literature: Erdős–Hajnal–Rado proved the above bounds and conjectured the doubly exponential lower bound (r_3(n)>2^{2^{c n}}); Erdős even offered a $500 reward for proving such a bound. ([ETH Zurich Math Homepages][1])

So the answer to your final question

> “does (R_r(n)) grow like a tower of height $r-1$ with top exponent (\Theta(n))?”

is:

* **Upper bound:** yes, (R_r(n)) is at most such a tower (Erdős–Rado), so (\log^{(r-1)} R_r(n)=O_r(n)).
* **Matching lower bound:** **unknown**. It is a major open problem already for (r=3). The conjecture (R_3(n)\ge 2^{2^{c n}}) would, via stepping‑up, imply the full statement (\log^{(r-1)} R_r(n)\asymp_r n) for all (r\ge 3). ([ETH Zurich Math Homepages][1])

---

## Bottom line

What you *can* prove today (and I’ve sketched the full proofs/tools above) is:
[
\boxed{\ \log^{(r-1)} R_r(n)\ \le\ C_r n\quad\text{and}\quad \log^{(r-1)} R_r(n)\ \ge\ \Theta(\log n)\ }
]
and more precisely,
[
\boxed{\ t_{r-1}(c_r n^2)\ \le\ R_r(n)\ \le\ t_r(C_r n)\ }.
]
The sharpened two‑sided estimate (\log^{(r-1)} R_r(n)\asymp_r n) is exactly the unresolved “tower height” problem for diagonal hypergraph Ramsey numbers; it is conjectured but not proved.

If you want, I can also write out a complete, self-contained proof of the stepping‑up lemma [[nomath]](the $\delta$-function / binary expansion construction)[[/nomath]] and then explicitly derive $5$ from $3$ and $4$ with all constants tracked.

[1]: https://people.math.ethz.ch/~sudakovb/stepping-up-lemma.pdf "https://people.math.ethz.ch/~sudakovb/stepping-up-lemma.pdf"
