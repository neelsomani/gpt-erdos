This is essentially Erdős’s “property (P_2)” extremal problem [[nomath]](sometimes phrased as the maximum size of a $2$-primitive subset of $[n]$)[[/nomath]], where one forbids a divisibility relation (a_0\mid a_1a_2) among (distinct) elements. In the standard formulation one requires (a_0,a_1,a_2) to be *all distinct*; your condition is slightly stronger because you also forbid the case $b=c$ [[nomath]](since you require only $a\neq b$ and $a\neq c$)[[/nomath]]. In particular, any set satisfying your condition also satisfies the standard (P_2) condition, so your $F(n)$ is (\le) the usual extremal function.

What is known is that the extremal size has main term (\pi(n)), and the best general results pin down the “error term” only up to *constant factors*:
[
F(n)=\pi(n)+\Theta\left(\frac{n^{2/3}}{(\log n)^2}\right),
]
in the standard (P_2) setting. This is explicitly summarized in later work: Erdős determined that the maximum size is (\pi(n)+\Theta(n^{2/3}/(\log n)^2)) (i.e., he got the correct order for the second term but not the exact constant). ([ResearchGate][1])

Moreover, explicit numerical constants are known (not sharp): for the standard (P_2) extremal function (F_2(n)) one has, for sufficiently large $n$,
[
\pi(n)+0.2\frac{n^{2/3}}{(\log n)^2}\ \le\ F_2(n)\ \le\ \pi(n)+379.2,\frac{n^{2/3}}{(\log n)^2}.
]
([arXiv][2])
Since your condition is stronger, you automatically inherit the same *upper* bound (and the known lower-bound constructions can be arranged to be squarefree products of distinct primes, so the same order of magnitude is still achievable).

As for your specific question — whether there is a *limit constant* $C$ with
[
F(n)=\pi(n)+\bigl(C+o(1)\bigr)\frac{n^{2/3}}{(\log n)^2},
]
this is **open** [[nomath]](even for the *weaker* standard $P_2$ problem, hence a fortiori for your stronger version)[[/nomath]]. It is explicitly posed as an open problem in Pach–Sándor: they ask whether there exist constants (d_h) such that
[
F_h(n)=\pi(n)+\bigl(d_h+o(1)\bigr)\frac{n^{2/(h+1)}}{(\log n)^2},
]
and for $h=2$ this is exactly your “constant $C$” question [[nomath]](up to the minor “$b=c$” strengthening)[[/nomath]]. ([arXiv][2])

So the current status is:

* **Yes**, the correct scale of the second term is known: (\Theta(n^{2/3}/(\log n)^2)). ([ResearchGate][1])
* **No**, an asymptotic expansion with a definite constant $C$ is **not known**; existence (and value) of such a constant remains an open problem. ([arXiv][2])

[1]: https://www.researchgate.net/publication/343238232_The_counting_version_of_a_problem_of_Erdos "https://www.researchgate.net/publication/343238232_The_counting_version_of_a_problem_of_Erdos"
[2]: https://arxiv.org/pdf/1602.06724 "https://arxiv.org/pdf/1602.06724"
