Yes.

Voss proved (answering a conjecture of Erdős) that **every graph with chromatic number (\ge 4) and with no (K_4) subgraph contains an odd cycle with at least two chords** (i.e., at least two “diagonals” of that cycle). ([ScienceDirect][1])
In particular, if $G$ is (K_4)-free and (\chi(G)=4), then $G$ must contain an odd cycle with at least two diagonals.

As for your more general question: **it is (as far as currently recorded) still open** whether one can force the number of diagonals to go to infinity as the “local 3-colorability radius” $r$ grows. ([Erdős Problems][2])
What is known from the same problem record:

* Erdős originally asked just for **one** diagonal; that was proved by Larson. ([Erdős Problems][2])
* Voss’s result gives a uniform lower bound **(f(r)\ge 2)** [[nomath]](once $r\ge 4$, since then the hypothesis “every subgraph on $\le r$ vertices is 3-colorable” in particular excludes $K_4$)[[/nomath]]. ([ScienceDirect][1])
* You **cannot** hope for (f(r)\ge 3) in general: the **pentagonal wheel** shows “three diagonals are not guaranteed.” ([Erdős Problems][2])

So: the first question is settled “yes” (Voss, 1982), while the unbounded-growth version is still open in general (at least in the standard tracking source). ([Erdős Problems][2])

[1]: https://www.sciencedirect.com/science/article/pii/0095895682900041 "https://www.sciencedirect.com/science/article/pii/0095895682900041"
[2]: https://www.erdosproblems.com/1091 "https://www.erdosproblems.com/1091"
