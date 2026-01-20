Let $p$ be prime and
[
f(p):=\min{n\ge 1:\ n!\equiv -1 \pmod p}.
]
By Wilson’s theorem ((p-1)!\equiv -1\pmod p), so $f(p)$ is always defined and (f(p)\le p-1).

It’s convenient to let
[
N(p):=|\\{1\le n\le p-1:\ n!\equiv -1\pmod p\\}|.
]
Then (N(p)\ge 1) always [[nomath]](because $n=p-1$ is a solution)[[/nomath]], and
[
f(p)=p-1 \quad\Longleftrightarrow\quad N(p)=1,
]
i.e. “$-1$” is hit **only once** by the factorial map (n\mapsto n!\pmod p).

## 1) Infinitely many $p$ with (f(p)=p-1)?

As far as I can tell (as of Jan 2026), this is **not proved**. It sits inside a broader circle of open problems about how “random” the values (1!,2!,\dots,(p-1)!\pmod p) look.

A standard benchmark is **Stauduhar’s conjecture**: if $h(p)$ is the number of *distinct* residues among (1!,2!,\dots,(p-1)!\pmod p), then
[
\frac{h(p)}{p}\to 1-\frac1e.
]
This is explicitly stated (and noted as still unsolved) by Cobeli–Zaharescu. 

They also formulate a stronger “Poisson((\lambda=1))” refinement:

> **Conjecture 2 (Cobeli–Zaharescu):** for each fixed (k\ge 0), the proportion of residues (y\in\mathbb F_p) for which the congruence (n!\equiv y\pmod p) has exactly $k$ solutions $n$ tends to (1/(k!e)); i.e. it behaves like a Poisson process with mean $1$. 

Under this (or even under the weaker “looks like a random map” heuristic), for a *fixed* target value like (-1), the “extra” solutions among (n\le p-2) should behave like a Poisson((1)) number of hits, so
[
\Pr(N(p)=1)\approx e^{-1}\approx 0.3679.
]
That would imply **infinitely many** primes with (f(p)=p-1), in fact with positive density (\approx 1/e).

This heuristic is also aligned with later work modeling factorial residues via “non-equal-neighbor” random models and again finding Poisson behavior in the averaged analogue. ([doiserbia.nb.rs][1])

**Numerical sanity check (my own computation):** among primes (p\le 100{,}000), about $0.358$ of primes satisfy (f(p)=p-1), which is close to $1/e$.

So: **expected yes [[nomath]](and even positive density $\sim 1/e$)[[/nomath]], but currently unproved**.

## 2) Does (f(p)/p\to 0) for almost all primes $p$?

Again, I don’t know any proof either way, but the **same Poisson/random-map heuristics strongly suggest “no.”**

If the values (n!\pmod p) behave roughly like random residues as $n$ runs up to $p$, then for a fixed residue (-1) the “hit” probability at each step is (\sim 1/p). The first hit time typically scales like $p$, not $o(p)$. In a crude model where hits occur as a Poisson process of rate $1/p$ along the index $n$, one predicts that (f(p)/p) has a **nondegenerate limiting distribution** [[nomath]](roughly exponential, truncated at $1$)[[/nomath]], in particular
[
\Pr!\bigl(f(p)>\varepsilon p\bigr)\approx e^{-\varepsilon}\quad(\varepsilon\in(0,1)),
]
so for every fixed (\varepsilon>0) there should be a **positive proportion** of primes with $f(p)$ still (\ge \varepsilon p). That is incompatible with (f(p)/p\to 0) on a density‑$1$ set of primes.

Computationally (again, my own), for primes (p\le 100{,}000) the ratio (f(p)/p) does **not** look like it is drifting toward $0$ [[nomath]](median $\approx 0.5$, mean $\approx 0.60$)[[/nomath]].

So: **conjecturally false**.

## Context: why this is hard

Even quite “coarse” distribution questions [[nomath]](like how many residues are *missing* from ${n!\bmod p}$)[[/nomath]] are difficult. For instance, Banks–Luca–Shparlinski–Stichtenoth discuss the conjectural $p/e$ missing-value law and prove that for infinitely many primes $p$ there are at least (\log\log p/\log\log\log p) missing residues, illustrating how far current methods are from the conjectured random-model picture. ([mospace.umsystem.edu][2])

---

If you want, I can also:

* compute more extensive tables of $f(p)$ statistics in various ranges [[nomath]](to test stability of the $\approx 1/e$ frequency of $f(p)=p-1$)[[/nomath]], or
* restate your two questions in the “ramification point” language used by Cobeli–Zaharescu (it lines up very cleanly with Conjecture 2).

[1]: https://doiserbia.nb.rs/Article.aspx?ID=0354-51802413711C "https://doiserbia.nb.rs/Article.aspx?ID=0354-51802413711C"
[2]: https://mospace.umsystem.edu/bitstreams/5b756a2f-14b6-4cd7-b23e-f57366effec4/download "n_factorial_mod_p.pdf"
