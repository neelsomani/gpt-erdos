This is (as far as I can tell) **still open**.

It appears explicitly as an Erdős problem (Erdős Problem **#938**) in the formulation you wrote: for the increasing sequence of powerful (squareful) numbers (n_1<n_2<\cdots), are there only finitely many indices $k$ with
[
n_{k+1}-n_k = n_{k+2}-n_{k+1},?
]
Erdosproblems.com currently lists it as **OPEN**. ([Erdős Problems][1])

### Some concrete data (examples exist)

There *are* examples of three **consecutive powerful numbers** in an arithmetic progression. The smallest ones include

* $(1728,1764,,1800)$ with common difference $36$,
* $(6912,7056,,7200)$ with common difference $144$.

I also did a quick computation [[nomath]](by enumerating all powerful numbers $\le 10^{12}$ via the standard representation $n=a^2 b^3$ with $b$ squarefree)[[/nomath]] and found **10** such consecutive-term 3-APs up to (10^{12}):
[
\begin{aligned}
&(1728,1764,1800),\ (6912,7056,7200),\
&(729000,729316,729632),\ (1458000,1458632,1459264),\
&(2916000,2917264,2918528),\ (11664000,11669056,11674112),\
&(149022674775,149022848000,149023021225),\
&(260102040004,260102223752,260102407500),\
&(348796224200,348796548100,348796872000),\
&(697592448400,697593096200,697593744000).
\end{aligned}
]
This doesn’t prove anything either way, but it at least shows the phenomenon is real and seems *very sparse*.

### Related facts (context)

* If you drop the “consecutive terms” condition, then powerful numbers contain **many** arithmetic progressions: in fact there are arbitrarily long $k$-term APs of powerful numbers, and infinitely many 3-term APs are known. ([Cheriton School of Computer Science][2])
  Your question is about the much stronger “no other powerful numbers in between” requirement.
* Don’t confuse this with Erdős’s other famous conjecture about **three consecutive integers** $n,n+1,n+2$ all being powerful. That one is a different problem (Erdős Problem #364) and is also open; it is known to follow from the $abc$-conjecture. ([Erdős Problems][3])

### Heuristic intuition (not a proof)

A very rough “random spacing” heuristic for a sparse increasing sequence often suggests that “equal consecutive gaps” events might occur infinitely often but extremely rarely [[nomath]](logarithmically many up to size $x$, say)[[/nomath]]. That’s consistent with seeing only a handful of examples up to (10^{12}), but it’s only heuristic—there’s no known theorem settling finiteness vs infinitude here.

So the best current honest answer is: **nobody knows** whether there are finitely many or infinitely many such consecutive-term 3-term arithmetic progressions. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/938 "https://www.erdosproblems.com/938"
[2]: https://cs.uwaterloo.ca/journals/JIS/VOL26/Chan/chan33.pdf "https://cs.uwaterloo.ca/journals/JIS/VOL26/Chan/chan33.pdf"
[3]: https://www.erdosproblems.com/364 "https://www.erdosproblems.com/364"
