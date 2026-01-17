This is **not known in general**. It is recorded as **Erdős Problem #260** and is still listed as **open** (the problem page was last edited **19 October 2025**). ([Erdős Problems][1])

What *is* known is that the sum is irrational under **stronger** hypotheses. In particular, Erdős proved that if the consecutive gaps grow,
[
a_{n+1}-a_n\to\infty,
]
then
[
\sum_{n=1}^\infty \frac{a_n}{2^{a_n}}
]
is irrational [[nomath]](and he notes the same argument works with $2$ replaced by any integer base $t>1$)[[/nomath]]. ([old.renyi.hu][2])

Erdős also wrote that it “seems very plausible” that the weaker condition in your question,
[
\frac{a_n}{n}\to\infty,
]
should already be sufficient, but that his method breaks down there; he further suspected there might even exist a counterexample with (\limsup(a_{n+1}-a_n)=\infty) and the sum rational, though he did not have one. ([old.renyi.hu][2]) The Erdős Problems site likewise notes an additional sufficient growth condition (also attributed to Erdős): (a_n \gg n\sqrt{\log n\log\log n}). ([Erdős Problems][1])

So the current state is:

* **Under (a_{n+1}-a_n\to\infty)**: **yes**, the sum is irrational (Erdős, 1981). ([old.renyi.hu][2])
* **Under only (a_n/n\to\infty)**: **open**; no proof and no counterexample is known. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/260 "https://www.erdosproblems.com/260"
[2]: https://old.renyi.hu/~p_erdos/1981-36.pdf "https://old.renyi.hu/~p_erdos/1981-36.pdf"
