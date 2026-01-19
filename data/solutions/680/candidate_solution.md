Let me write (\operatorname{lpf}(m)=p(m)) for the least prime factor.

## 1) The (k^2+1) version

A couple of quick observations:

* If $n$ is **even**, then $k=1$ works: $n+1$ is odd, so (p(n+1)\ge 3>2=1^2+1).
* So the only nontrivial case is **odd** $n$, and then any **odd** $k$ makes $n+k$ even, so (p(n+k)=2) and the inequality fails. So for odd $n$, any winning $k$ must be even.

### A key “large $k$” lemma

For large $n$, if
[
k \ge n^{1/4},
]
then **any** solution must have $n+k$ prime.

Reason: if $n+k$ is composite then (p(n+k)\le \sqrt{n+k}). Also for (k\le \sqrt n) we have (n+k\le n+\sqrt n<2n), so
[
p(n+k)\le \sqrt{n+k}<\sqrt{2n}.
]
But if (k\ge n^{1/4}), then (k^2\ge \sqrt n), so for large $n$,
[
k^2+1 \ge \sqrt n +1 > \sqrt{2n}\ge p(n+k),
]
contradicting (p(n+k)>k^2+1). Hence $n+k$ must be prime.

### What this means for the original question

* If you could prove that **every** interval $[x,x+\sqrt x]$ contains a prime for all large $x$, then your statement would follow immediately [[nomath]](take that prime as $n+k$)[[/nomath]].
* But that “prime in every (\sqrt x)-interval” statement is **open** with current methods. The best unconditional “prime in short intervals” results are still of the form “there is a prime in $[x-x^\delta,x]$” for (\delta>1/2); for example Baker–Harman–Pintz give (\delta=0.525). ([arXiv][1])

On the other hand, if your statement were **false** for infinitely many $n$, then for such an $n$ there could be **no prime** among $n+k$ for all (k\in[n^{1/4},\sqrt n]), i.e. you’d get prime gaps of size (\gg \sqrt n). That is far beyond what we can currently construct or rule out: the best *proven* lower bounds for large prime gaps are only on the order of (\log x\log\log x) times smaller iterated-log factors. ([arXiv][2])

So, as far as current unconditional knowledge goes:

* I don’t know a proof that the (k^2+1) statement is true for all sufficiently large $n$.
* I also don’t know a way to prove it false (a counterexample would essentially force an enormous prime gap regime).

In short: **this looks open**, and it sits in the terrain of very hard “uniform in $n$” short-interval/prime-gap phenomena.

[[nomath]](There are strong *average-case* and heuristic reasons to believe you should usually be able to find such a $k$, and recent work studies “rough numbers” in short intervals/gaps, but those don’t give a uniform-for-all-$n$ statement of the kind you’re asking.)[[/nomath]] ([arXiv][3])

## 2) Replacing (k^2+1) by (e^{(1+\varepsilon)\sqrt{k}}+C_\varepsilon)

Let
[
f_\varepsilon(k)=e^{(1+\varepsilon)\sqrt{k}}+C_\varepsilon.
]

### First, the range of $k$ that even has a chance

Since (p(n+k)\le n+k), the inequality (p(n+k)>f_\varepsilon(k)) is **impossible** unless
[
n+k>f_\varepsilon(k).
]
Ignoring the additive (C_\varepsilon) (it doesn’t matter asymptotically), this forces roughly
[
e^{(1+\varepsilon)\sqrt{k}} \lesssim n
\quad\Longrightarrow\quad
\sqrt{k}\lesssim \frac{\log n}{1+\varepsilon}
\quad\Longrightarrow\quad
k \lesssim \frac{(\log n)^2}{(1+\varepsilon)^2}.
]
So only $k$ up to about ((\log n)^2) are relevant.

### Why proving this false is essentially a Cramér-scale prime gap problem

Suppose there exists a prime (q=n+k) with
[
k \le \frac{(\log n)^2}{(1+\varepsilon)^2} - O(1).
]
Then (f_\varepsilon(k)\le n+O(1) < q) for large $n$, hence
[
p(n+k)=q > f_\varepsilon(k),
]
so that prime gives you a witness $k$.

Therefore, **if the statement were false for some large $n$** [[nomath]](no $k$ works)[[/nomath]], then there must be **no primes** in
[
(n, n+K],\qquad K \asymp \frac{(\log n)^2}{(1+\varepsilon)^2}.
]
So a counterexample would force prime gaps on the order of ((\log n)^2).

But producing (or proving existence of) prime gaps of length (\gg (\log x)^2) is *completely beyond* what is known unconditionally; the best proven lower bounds are much smaller, of size roughly (\log x\log\log x) times smaller iterated-log factors. ([arXiv][2])

So with current technology:

* **No**, we cannot presently *prove* your exponential-replacement statement is false [[nomath]](doing so would essentially require proving the existence of prime gaps of length $\gtrsim (\log x)^2$ infinitely often)[[/nomath]].

### What is believable under conjectures

* Heuristics (Cramér/Granville-type models) suggest that gaps of order ((\log x)^2) **do** occur, and if one had such a lower bound in the right form, it would indeed yield counterexamples for your (e^{(1+\varepsilon)\sqrt{k}}) threshold for each fixed (\varepsilon>0).
* But that remains conjectural; the strongest proven prime-gap constructions are far below this scale. ([arXiv][2])

---

If you want, I can also spell out the exact implication “counterexample (\Rightarrow) prime gap of length (\asymp (\log n)^2)” carefully including the (+C_\varepsilon) term, but the core obstruction is the same: **to prove falsity you’d need Cramér-scale gaps, and we can’t prove those.**

[1]: https://arxiv.org/abs/1707.05437 "[1707.05437] Bounded gaps between primes in short intervals"
[2]: https://arxiv.org/abs/1412.5029 "[1412.5029] Long gaps between primes"
[3]: https://arxiv.org/html/2508.06463v1?utm_source=chatgpt.com "Rough numbers between consecutive primes"
