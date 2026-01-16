Write (E=\binom{n}{t}) for the number of (t)-edges in (K_n^{(t)}), and (as is standard) take (m\in{1,2,\dots,n}).

### Under your definition, (F^{(t)}(n,\alpha)) is essentially determined by ([n]) alone

If a colouring works for some (m\le n), then it must in particular work for the set (X=[n]) (since (|[n]|=n\ge m)). So we must have, for the whole hypergraph,
[
#\text{red edges}\ \ge \ \alpha E
\qquad\text{and}\qquad
#\text{blue edges}\ \ge \ \alpha E.
]
Equivalently, the *smaller* colour class must have size at least (\alpha E).

But in any 2-colouring of (E) edges, the smaller colour class has size at most (\lfloor E/2\rfloor). Hence a **necessary condition** for *any* (m\le n) to work is
[
\alpha E \le \Big\lfloor\frac{E}{2}\Big\rfloor
\qquad\Longleftrightarrow\qquad
\alpha \le \alpha_* := \frac{\lfloor E/2\rfloor}{E}.
]

Conversely, if (\alpha\le \alpha_*), then we can simply colour exactly (\lfloor E/2\rfloor) edges red and the remaining (E-\lfloor E/2\rfloor=\lceil E/2\rceil) edges blue. Then for (m=n) the condition only needs to hold for (X=[n]), and it does:
[
#\text{red}=\lfloor E/2\rfloor \ge \alpha E,\qquad
#\text{blue}=\lceil E/2\rceil \ge \alpha E.
]
So (m=n) is achievable, and since (m\le n) always, this forces (F^{(t)}(n,\alpha)=n).

Putting these together:

[
F^{(t)}(n,\alpha)=
\begin{cases}
n,& \text{if }\alpha \le \dfrac{\lfloor \binom{n}{t}/2\rfloor}{\binom{n}{t}},[1.2em]
\text{no such }m\le n\ \ (\text{often encoded as }0),& \text{if }\alpha > \dfrac{\lfloor \binom{n}{t}/2\rfloor}{\binom{n}{t}}.
\end{cases}
]

### So: are there jumps? at most one (and often none)

* If (\binom{n}{t}) is **even**, then (\alpha_*=\frac12). Since you only consider (\alpha<\frac12), the condition (\alpha\le\alpha_*) holds for all (\alpha\in[0,\frac12)).
  **Conclusion:**
  [
  F^{(t)}(n,\alpha)=n \quad\text{for all }\alpha\in[0,1/2),
  ]
  i.e. **no jumps at all**.

* If (\binom{n}{t}) is **odd**, then
  [
  \alpha_*=\frac{\binom{n}{t}-1}{2\binom{n}{t}}=\frac12-\frac{1}{2\binom{n}{t}}<\frac12.
  ]
  For (\alpha\le \alpha_*), (F=n). For (\alpha\in(\alpha_*,1/2)), the requirement already fails for (X=[n]), so no (m\le n) works (so (F) collapses to “undefined” or (0), depending on convention).
  **Conclusion:** **exactly one jump**, at (\alpha=\alpha_*).

Example: (n=3,t=2). Then (E=\binom32=3) (odd), so (\alpha_*=1/3).

* For (\alpha\le 1/3), colour 1 edge blue and 2 red: (F=3).
* For (\alpha>1/3), you would need (\ge 2) edges of each colour inside ([3]), impossible, so (F=0) (no (m\le 3)).

---

### Remark (in case you meant a different extremal direction)

As stated, maximizing (m) makes the problem collapse, because (m=n) reduces the condition to a single set (X=[n]). If you instead meant something like the **smallest** (m) for which such a colouring exists (i.e. you want the property to hold for *all sufficiently large* subsets in a nontrivial way), then the dependence on (\alpha) becomes genuinely combinatorial and you can get multiple steps/jumps.

But **for the function exactly as you defined it**, the answer is: it is constant (n) up to the global feasibility threshold, and then it dies—so **at most one jump (none if (\binom{n}{t}) is even)**.
