What you wrote is *exactly* the “boundary case” of Erdős’s **jump problem** for $r$-uniform hypergraphs.

### Why this is the jump problem

The number ((n/r)^r) is the edge count of the **balanced complete $r$-partite $r$-graph** [[nomath]](the blow‑up of a single $r$-edge with $r$ equal parts)[[/nomath]]. In the usual normalization
[
d(G):=\frac{e(G)}{\binom{n}{r}},
]
your hypothesis
[
e(G)\ge (1+\varepsilon)\left(\frac nr\right)^r
]
is equivalent [[nomath]](up to a $(1+o(1))$ factor as $n\to\infty$)[[/nomath]] to
[
d(G)\ge(1+\varepsilon)\frac{r!}{r^r}.
]
And your desired conclusion “find a subgraph on (m\to\infty) vertices with at least (c_r m^r) edges, where (c_r>r^{-r})” translates to “find a subgraph whose normalized density is at least
[
\frac{e(H)}{\binom{m}{r}};\gtrsim; c_r,r! ;>;\frac{r!}{r^r},
]
by an amount bounded away from (\frac{r!}{r^r}), **independently of (\varepsilon)**.”

That is precisely the statement that the value (\frac{r!}{r^r}) [[nomath]](equivalently $r^{-r}$ under your $m^r$-normalization)[[/nomath]] is a **jump**. ([Cambridge University Press & Assessment][1])

A small remark: your formulation with “some (m=m(n)\to\infty)” is essentially as strong as the usual jump formulation [[nomath]](which quantifies over all fixed $t$)[[/nomath]]. Indeed, if $H$ has $m$ vertices and (e(H)\ge c_r m^r), then for any fixed (t\le m), a uniformly random $t$-subset (S\subseteq V(H)) satisfies
[
\mathbb E[e(H[S])] = e(H)\cdot \frac{\binom{t}{r}}{\binom{m}{r}}
\ge c_r m^r \cdot \frac{\binom{t}{r}}{\binom{m}{r}}
;\approx; c_r,r!,\binom{t}{r},
]
so some $t$-vertex subgraph has density (\gtrsim c_r r!). (So a theorem of the form you stated would imply the standard “jump” property.)

### Current status: this is **open** (and famous)

What is known (and what is not) is well documented:

* Erdős proved that **every** density (\alpha < \frac{r!}{r^r}) is a jump for (r\ge 3). ([Cambridge University Press & Assessment][1])
  In other words: *strictly below* the boundary, a uniform density increment phenomenon holds.

* However, whether the **boundary value** (\frac{r!}{r^r}) itself is a jump for (r\ge 3) is described as a **long-standing open problem of Erdős** in standard references/surveys, and it remains open in more recent papers discussing non-jumps. 

* Erdős also conjectured that *every* (\alpha\in[0,1)) is a jump for (r\ge 3), but Frankl and Rödl disproved this by constructing **non-jumps** for every (r\ge 3). ([mathweb.ucsd.edu][2])

* For $r=3$, where (\frac{r!}{r^r}=\frac{2}{9}), Baber–Talbot (flag algebras) proved the existence of jumps in intervals **above** $2/9$ [[nomath]](e.g. around $0.2299$–$0.2316$, and also $[0.2871,8/27)$)[[/nomath]], but this still does **not** settle the boundary $2/9$ case. ([Cambridge University Press & Assessment][1])

So, as written, your statement is not something with a standard known proof: it is [[nomath]](up to normalization and the $m\to\infty$ phrasing)[[/nomath]] *the* open “is (\frac{r!}{r^r}) a jump?” problem.

### What you *can* prove immediately (to calibrate)

* If you allow the constant to depend on (\varepsilon), then it’s trivial: take $m=n$ and (c_{r,\varepsilon}=(1+\varepsilon)r^{-r}).

* If you move **below** the boundary, i.e. replace (r^{-r}) by (r^{-r}-\delta) [[nomath]](or in the $\binom{n}{r}$ normalization replace $\frac{r!}{r^r}$ by any smaller $\alpha$)[[/nomath]], then Erdős’s theorem gives a genuine (\varepsilon)-independent jump. ([Cambridge University Press & Assessment][1])

If you tell me whether you want $i$ a careful equivalence proof between your formulation and the standard “jump” definition, or (ii) a proof sketch of Erdős’s theorem for all (\alpha<\frac{r!}{r^r}), I’ll write that out in full detail.

[1]: https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/hypergraphs-do-jump/4E4143FE155296C4F6E2299D6675EDE8 "Hypergraphs Do Jump | Combinatorics, Probability and Computing | Cambridge Core"
[2]: https://mathweb.ucsd.edu/~erdosproblems/erdos/newproblems/JumpingDensity.html?utm_source=chatgpt.com "Jumping densities for 3-hypergraphs"
