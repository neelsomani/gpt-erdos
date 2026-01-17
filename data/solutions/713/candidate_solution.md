Not known in general.

What you wrote is (essentially) the **Erdős–Simonovits “degenerate Turán numbers” conjecture**: for every *bipartite* forbidden graph (more generally, every finite family of graphs of chromatic number 2), there should be an exponent and a limiting constant so that
[
\frac{\mathrm{ex}(n;G)}{n^\alpha}\to c>0,
]
and Erdős–Simonovits even conjectured that the exponent can be taken **rational**. This conjecture is stated explicitly in the literature and is described as *wide open*. 

To give a sense of how open it is: even for very concrete bipartite graphs, we often don’t know whether the normalized ratio converges. For example, Füredi–Naor–Verstraëte (2006) give explicit lower/upper constants for (C_6) of the form
[
0.5338,n^{4/3} \lesssim \mathrm{ex}(n,C_6)\lesssim 0.6272,n^{4/3},
]
and they remark that there isn’t much evidence either way for the existence of (\lim_{n\to\infty}\mathrm{ex}(n,C_6)/n^{4/3}). ([Princeton Math][1])
So even in cases where the *exponent* (4/3) is the accepted growth rate, the existence (let alone value) of the *limit constant* is typically unknown.

### About “must (\alpha) be rational?”

Also unknown.

There is a well-known **rational exponents conjecture** (often attributed to Erdős–Simonovits in this form) asserting that for every bipartite $H$ there is a **rational** (r_H\in[1,2)) such that
[
\mathrm{ex}(n,H)=\Theta(n^{r_H}),
]
which is weaker than your “(\sim c n^\alpha)” statement (it doesn’t ask for a limiting constant). This conjecture remains open. ([Advances in Combinatorics][2])

What is known is consistent with “rational”: every exponent that has actually been determined for a *single* bipartite forbidden graph is rational [[nomath]](trees: $1$, many complete bipartite graphs: $2-1/s$, many “theta” graphs: $1+1/k$, the cube $Q_8$: $8/5$, etc.)[[/nomath]]. But there is **no theorem** ruling out irrational exponents, and no known example of a single bipartite graph with a proven irrational Turán exponent.

A related but different (and now solved) result is that **for every rational** (r\in(1,2)) there is a **finite family** of graphs (\mathcal H_r) with (\mathrm{ex}(n,\mathcal H_r)=\Theta(n^r)) (Bukh–Conlon). ([arXiv][3])
However, that does not settle the single-graph problem, and it also does not address the stronger “(\sim c n^r)” limit-constant form.

### Bottom line

* The claim “for every bipartite $G$, (\mathrm{ex}(n;G)\sim c n^\alpha) for some (\alpha\in[1,2))” is a major open conjecture. 
* Whether (\alpha) must be **rational** is likewise open; it’s conjectured “yes” in the rational-exponents framework, but unproved. ([Advances in Combinatorics][2])

If you tell me a specific bipartite graph $G$ you care about [[nomath]](cycles, $K_{s,t}$, subdivisions, grids, etc.)[[/nomath]], I can summarize what is currently known about its best bounds and whether any asymptotic constant is known.

[1]: https://web.math.princeton.edu/~naor/homepage%20files/final-hexagons.pdf "https://web.math.princeton.edu/~naor/homepage%20files/final-hexagons.pdf"
[2]: https://www.advancesincombinatorics.com/article/57310-rational-exponents-near-two "Rational exponents near two | Published in Advances in Combinatorics"
[3]: https://arxiv.org/abs/1506.06406?utm_source=chatgpt.com "Rational exponents in extremal graph theory"
