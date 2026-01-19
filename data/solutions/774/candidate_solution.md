This is **open** (as of at least **28 Dec 2025**, and still listed open on 18 Jan 2026).

* The question appears (in essentially this form) in work of **Alon–Erdős**, and it is recorded as **Erdős Problem #774**. ([Erdős Problems][1])
* Pisier showed that being *proportionately dissociated* (often phrased “proportionally quasi‑independent/free”) is **equivalent** to being a **Sidon set in the harmonic analysis sense**. Under this equivalence, your question becomes the classical “Pisier problem”:

  > does $2$ “every finite subset contains a free subset of linear size” imply $1$ “the whole set is a finite union of free (i.e. dissociated) sets”?
  > This implication is explicitly stated as **still open** in Nešetřil–Rödl–Sales (2024). ([NSF Public Access Repository][2])

### What is known (and why the problem is subtle)

* The forward direction is easy: if (A=\bigcup_{i=1}^t A_i) with each (A_i) dissociated, then every finite (B\subset A) has some (B\cap A_i) of size (\ge |B|/t), hence contains a dissociated subset of size (\gg |B|) (take that intersection). This is the “pigeonhole” implication $1$ (\Rightarrow) $2$ discussed in the literature. ([NSF Public Access Repository][2])

* A key obstruction is that the naive analogue of **Horn/Edmonds matroid union** reasoning fails for quasi‑independence in (\mathbb Z). Grow–Whicher (1984) exhibit a **finite** set
  [
  E=E_0\cup E_1\cup E_2,\quad E_k={3^j+kj:1\le j\le 5},
  ]
  such that **every** (F\subseteq E) contains a quasi‑independent (dissociated) subset (F') with (|F'|\ge (1/2)|F|), **but** $E$ **cannot** be written as the union of **two** quasi‑independent sets. ([Cambridge University Press & Assessment][3])
  So even if the answer to your question were “yes”, the number of dissociated pieces cannot in general be taken as simply (\lceil 1/c\rceil).

* Grow–Whicher also reduce the infinite question [[nomath]](in $\mathbb Z$)[[/nomath]] to an equivalent **finite** formulation: for each $k$, does there exist $n(k)$ such that any finite (E\subset \mathbb Z) with the “every subset has a $1/k$-fraction quasi‑independent subset” property can be partitioned into $n(k)$ quasi‑independent sets? (This is their “Problem 2”.) ([Cambridge University Press & Assessment][3])

### Related negative results (but not for full dissociation)

Nešetřil–Rödl–Sales (2024) prove that for several **weaker/variant** notions [[nomath]](e.g. $B_h$-sets / $h$-free variants)[[/nomath]] the implication $2$ (\Rightarrow) $1$ **fails**, i.e. there are sets not decomposable into finitely many “independent” pieces despite having large “independent” subsets in every finite subset. But they stress that the original “free/quasi‑independent” (i.e. full dissociated) case remains open. ([NSF Public Access Repository][2])

### Bottom line

No general proof or counterexample is known: **it is currently unknown whether every proportionately dissociated (A\subset\mathbb N) must be a finite union of dissociated sets.** ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/774 "https://www.erdosproblems.com/774"
[2]: https://par.nsf.gov/servlets/purl/10584370 "https://par.nsf.gov/servlets/purl/10584370"
[3]: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/1174FB55D7CFE16B357F38BA76E01B0B/S0008439500069010a.pdf/finite-unions-of-quasi-independent-sets.pdf "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/1174FB55D7CFE16B357F38BA76E01B0B/S0008439500069010a.pdf/finite-unions-of-quasi-independent-sets.pdf"
