As of **January 2026**, this is **open for every (k\ge 3)**: there is **no known** constant (c(k)>0) that forces an additive basis $A$ of order $k$ with (r(n)\ge c(k)\log n) [[nomath]](for all large $n$)[[/nomath]] to contain a **minimal** basis of order $k$. ([Erdős Problems][1])

What *is* known [[nomath]](and why $\log n$ shows up)[[/nomath]] is roughly:

* **Order $2$ is special.** Erdős–Nathanson proved that if $A$ is an asymptotic basis of order $2$ and its 2-term representation function satisfies
  [
  r_{2,A}(n)>\frac{1}{\log(4/3)}\log n
  \quad\text{for all sufficiently large }n,
  ]
  then $A$ **does** contain a minimal asymptotic basis of order $2$. ([arXiv][2])
  [[nomath]](Even in order $2$, the appearance/optimality of the constant $1/\log(4/3)$ is not fully understood.)[[/nomath]] ([arXiv][2])

* **For (k\ge 3)**, Erdős already noted that the *method of proof* for the $k=2$ result “seems to work only in the case $h=2$,” and that for (h>2) it was not known even whether a sufficiently large constant times (\log n) would force the existence of a minimal subbasis. ([Renyi Institute][3])
  This is essentially the question you are asking, and it remains listed as open (Erdős Problem #870). ([Erdős Problems][1])

* The scale (\log n) is “natural” in this area: probabilistic constructions produce (strict) asymptotic bases of order $k$ whose representation functions are of order (\log n) (up to constants), so one cannot expect a blanket implication from a much smaller lower bound. ([Theory of Numbers][4])

So the honest current status is:

**No general theorem is known for (k\ge 3)**; the question is explicitly posed as an open problem in modern surveys and on the Erdős problems database. ([arXiv][2])

If you’re interested in why $k=2$ is tractable but (k\ge 3) isn’t (at least with current techniques): the $k=2$ arguments can be organized around *pairings* and “systems of distinct representatives”/Hall-type ideas; for (k\ge 3) one is pushed into genuinely **hypergraph**-type selection/matching phenomena where the same clean combinatorial control is missing in this additive setting. Erdős explicitly comments that the existing proof framework was confined to $h=2$. ([Renyi Institute][3])

[1]: https://www.erdosproblems.com/forum/discuss/870 "https://www.erdosproblems.com/forum/discuss/870"
[2]: https://arxiv.org/pdf/2310.18277 "Extremal problems and the combinatorics of sumsets"
[3]: https://users.renyi.hu/~p_erdos/1988-25.pdf?utm_source=chatgpt.com "Partitions of Bases into Disjoint Unions of Bases*"
[4]: https://www.theoryofnumbers.com/melnathanson/pdfs/nath1995-84.pdf?utm_source=chatgpt.com "Independence of solution sets and minimal asymptotic bases"
