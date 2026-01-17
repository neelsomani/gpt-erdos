This is a well-known open Erdős–Duke–Rödl problem (it appears as Erdős Problem #584). As stated, **the full pair of assertions is not known in complete generality**, but there are strong partial results. ([Erdős Problems][1])

## The (H_1) statement [[nomath]](cycles $\le 6$, and incident edges on a $4$-cycle)[[/nomath]]

* **For graphs of constant density** [[nomath]](i.e. $\delta$ is a fixed positive constant)[[/nomath]], Duke–Erdős proved that for all sufficiently large $n$ one can find a subgraph (H\subseteq G) with (\Theta(n^2)) edges in which **every pair of edges lies on a cycle of length $4$ or $6$** and **every pair of incident edges lies on a $4$-cycle**. ([Renyi Users][2])

* **In the sparse regime (\delta=n^{-\varepsilon}) [[nomath]](with fixed $0<\varepsilon<1/2$)[[/nomath]]**, Duke–Erdős–Rödl (1984) showed:

  * If you **do not** insist on the “incident edges on a $4$-cycle” strengthening, then the (\delta^3 n^2) bound is essentially *right*: they obtain a subgraph with (\Theta(n^{2-3\varepsilon})=\Theta(\delta^3n^2)) edges where **every two edges lie on a cycle of length at most $6$**, and they also prove this exponent (3\varepsilon) is best possible up to constants. ([Renyi Users][3])
  * With the **extra requirement** that **incident edges must lie on a $4$-cycle**, their best general guarantee is only (\Theta(n^{2-5\varepsilon})=\Theta(\delta^5 n^2)) edges. They explicitly raise as an open question whether one can improve this to (\Theta(n^{2-3\varepsilon})=\Theta(\delta^3n^2)). ([Renyi Users][3])

So: **your exact (H_1) claim with (\gg \delta^3n^2) and the “incident (\Rightarrow C_4)” condition is open in general**; the best published bound in that direction is (\gg \delta^5 n^2). ([Erdős Problems][1])

## The (H_2) statement [[nomath]](cycles $\le 8$)[[/nomath]]

* Duke–Erdős–Rödl proved a **weaker** result: one can always get (\gg \delta^2 n^2) edges if one allows cycles of length up to **12** instead of 8, and they asked whether 12 could be reduced to 8. ([Renyi Users][3])

* Fox–Sudakov $2007/08$ then proved the desired **“(\le 8)”** conclusion (indeed in a strengthened form) in a substantial range of densities: for graphs with (n^{2-\beta}) edges with (\beta<1/5) [[nomath]](equivalently $\delta>n^{-1/5}$)[[/nomath]], they find a subgraph with (\gg n^{2-2\beta}=\gg\delta^2n^2) edges in which **every two edges lie on a cycle of length at most 8**, and moreover **incident edges lie on a cycle of length at most 6**. ([ar5iv][4])

* For *smaller* densities, the full picture is still not settled: Fox–Sudakov note it is “very interesting” to determine exactly for which (\beta) the 8-cycle statement holds, and point out that for sufficiently sparse graphs [[nomath]](certain $\beta$ close to 1)[[/nomath]] there are constructions with **no $8$-cycle at all**, so in that extreme range the answer must be negative. ([ar5iv][4])

So: **your exact (H_2) claim is known to be true when (\delta>n^{-1/5})** (and in the constant-density case), but **it remains open in full generality as a uniform statement in (\delta)**. ([ar5iv][4])

[1]: https://www.erdosproblems.com/584 "https://www.erdosproblems.com/584"
[2]: https://users.renyi.hu/~p_erdos/1982-35.pdf "https://users.renyi.hu/~p_erdos/1982-35.pdf"
[3]: https://users.renyi.hu/~p_erdos/1984-09.pdf "https://users.renyi.hu/~p_erdos/1984-09.pdf"
[4]: https://ar5iv.org/pdf/0706.1920 "https://ar5iv.org/pdf/0706.1920"
