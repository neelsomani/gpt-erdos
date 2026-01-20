As far as I can tell, this is **still open** in the “for all sufficiently large $d$” form you stated. It is listed as Erdős problem #971 in the Erdős problems database, and that page explicitly records it as open. ([Erdős Problems][1])

What *is* known (already from Erdős) is weaker in the quantifiers:

* Erdős proved that the desired phenomenon happens for **infinitely many moduli $d$** [[nomath]](i.e. along an infinite sequence of $d$’s, not for every large $d$)[[/nomath]]. ([Erdős Problems][1])
* He also proved the opposite-direction statement that for any (\varepsilon>0), there are (\gg_\varepsilon \varphi(d)) residue classes with **very small** least prime: (p(a,d)<\varepsilon\varphi(d)\log d). ([Erdős Problems][1])

### Why one expects the answer “yes” heuristically

A standard heuristic is that primes in reduced residue classes mod $d$ behave “randomly” with the expected count up to $x$ in a fixed class (\approx \mathrm{Li}(x)/\varphi(d)). If you take
[
x=(1+c)\varphi(d)\log d,
]
then
[
\frac{\mathrm{Li}(x)}{\varphi(d)} \approx \frac{x}{\varphi(d)\log x}\approx (1+c)\frac{\log d}{\log x}\approx 1+c
]
since (\log x\sim \log d) for large $d$. In a Poisson (or geometric) model, the probability a given class has **no** prime up to $x$ is then about (\exp(-(1+c))), so one would predict about
[
\exp(-(1+c)),\varphi(d)
]
classes with (p(a,d)>x), i.e. (\gg\varphi(d)) many. This is exactly the kind of reasoning sketched in the discussion thread for the problem. ([Erdős Problems][2])

### Related context (but not solving this)

There are much stronger lower-bound results for the *maximum* least prime
[
P(d):=\max_{(a,d)=1} p(a,d),
]
showing that for many moduli $d$, **some** residue class has a least prime far larger than (\varphi(d)\log d) (by iterated-log factors). For instance, the survey/introduction in Li–Pratt–Shakan summarizes earlier work of Pomerance and Granville–Pomerance giving such lower bounds for $P(d)$ [[nomath]](and even stronger ones for many $d$)[[/nomath]]. ([Jligit][3])
But these are “there exists an $a$” statements about $P(d)$, not “(\gg\varphi(d)) many $a$” statements, and they don’t currently bridge the gap to your question.

**So the short status is:** the “positive proportion of residue classes” lower-tail statement at the scale ((1+c)\varphi(d)\log d) is **conjecturally true** [[nomath]](indeed one expects it for every fixed $c>0$)[[/nomath]], but **no proof is known for all large $d$**; Erdős only established it along an infinite sequence of $d$. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/971 "https://www.erdosproblems.com/971"
[2]: https://www.erdosproblems.com/forum/thread/971 "https://www.erdosproblems.com/forum/thread/971"
[3]: https://jligit.github.io/paper/PrimesAps.pdf "https://jligit.github.io/paper/PrimesAps.pdf"
