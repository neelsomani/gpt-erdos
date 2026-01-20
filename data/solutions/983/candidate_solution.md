There is a small (but important) mismatch between your definition and the classical Erdős–Straus one.

* In Erdős’s 1970 paper, $f(k,x)$ is defined with **“more than $r$”** [[nomath]](i.e. $\ge r+1$)[[/nomath]] integers supported on $r$ primes. ([Renyi Institute][1])
* Your version uses **“at least $r$”** supported integers, which is strictly weaker. Many of the sharp results and the specific benchmark (2\pi(\sqrt n)) are tied to the “(>r)” version. [[nomath]](I’ll answer for the classical “$>r$” version, and briefly comment on the “$\ge r$” variant at the end.)[[/nomath]]

Below I write $f$ for the Erdős–Straus function [[nomath]](the “$>r$” one)[[/nomath]].

---

## 1) The limit (2\pi(\sqrt n)-f(\pi(n)+1,n)\to\infty) is **false**

Erdős and Straus conjectured exactly this divergence [[nomath]](it appears as $18$ in Erdős’s paper)[[/nomath]]. ([Renyi Institute][1])

However, Carl Pomerance showed that this conjecture is **false**: he proves that the upper-bound inequality can be met with equality for arbitrarily large $x$, and explicitly states that the conjecture [[nomath]](his $5.7$, corresponding to the Erdős–Straus conjecture)[[/nomath]] is false.

Concretely, Pomerance shows there are arbitrarily large $x$ for which
[
f(\pi(x)+1,x)=2\pi(\sqrt x)+1,
]
so
[
2\pi(\sqrt x)-f(\pi(x)+1,x)=-1
]
infinitely often. This alone prevents the difference from tending to (+\infty).

Pomerance also adds the (still open, to my knowledge) refinement: although the *limit* to (+\infty) is false, he conjectures the expression is **unbounded** (oscillates with arbitrarily large values), but he could not prove unboundedness.

---

## 2) Sharp asymptotics for (f(\pi(n)+1,n))

Erdős (with Straus) proved:

* the clean **upper bound**
  [
  f(\pi(x)+1,x)\le 2\pi(\sqrt x)+1,
  ]
  appearing as (14) in the paper’s development. ([Renyi Institute][1])

* a matching lower bound up to very small relative error, giving the strong asymptotic
  [
  f(\pi(x)+1,x)=2\pi(\sqrt x)+o!\left(\frac{\sqrt x}{(\log x)^k}\right)
  \quad\text{for every fixed }k,
  ]
  which is stated immediately after combining their upper/lower bound constructions. ([Renyi Institute][1])

In particular,
[
f(\pi(n)+1,n) \sim 2\pi(\sqrt n) \sim \frac{4\sqrt n}{\log n}.
]

So the main term (2\pi(\sqrt n)) is correct, but the *sign/size* of the second-order difference is delicate, and in fact the “(\to+\infty)” conjecture fails (Pomerance).

---

## 3) What is known for general $k$

### 3.1 Monotonicity

By definition, $f(k,n)$ is **non-increasing in $k$**: larger sets $A$ only make it easier to find the required configuration, so the worst-case minimum $r$ cannot go up.

So for every (k\ge \pi(n)+1),
[
f(k,n)\le f(\pi(n)+1,n) = 2\pi(\sqrt n)+o(\pi(\sqrt n)).
]

### 3.2 The “dense” regime (k \asymp n)

Erdős also proved a very different asymptotic when $k$ is a *positive fraction* of $x$. In the paper this is formula (11), derived from the Erdős–Kac normal law for (\omega(n)) (number of distinct prime factors). ([Renyi Institute][1])

If $k=cx$ with fixed (0<c<1), then
[
f(k,x)=\log\log x + \bigl(c_1+o(1)\bigr)\sqrt{2\log\log x},
]
where (c_1) is determined by
[
c=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{c_1} e^{-t^2/2},dt
\quad(\text{i.e. }c_1=\Phi^{-1}(c)).
]
([Renyi Institute][1])

So in the linear regime (k\sim cn), $f(k,n)$ is of size (\asymp \log\log n), dramatically smaller than the (\asymp \sqrt n/\log n) scale at (k=\pi(n)+1).

---

## 4) The intermediate regime (\pi(n)+1<k=o(n))

This is exactly the “hard middle.” Erdős explicitly remarks (after proving the two sharp extremes above) that one *could* study $f(k,x)$ for (k=o(x)) and (k>\pi(x)+1), but he did **not** obtain results as sharp as the (\pi(x)+1) and (cx) cases. ([Renyi Institute][1])

So, rigorously, what you can currently say “for free” is mostly:

* **Upper envelope:** for all (k\ge \pi(n)+1),
  [
  f(k,n)\le 2\pi(\sqrt n)+o(\pi(\sqrt n)).
  ]
  [[nomath]](by monotonicity + the sharp $k=\pi(n)+1$ asymptotic)[[/nomath]]

* **When (k\ge c n)** you have the sharp Erdős–Kac/Erdős–Straus asymptotic above.

Between (k\approx n/\log n) and (k\approx cn), the behavior is governed by how well one can construct large sets of integers whose prime-divisor incidence graph has strong “Hall-type expansion” (equivalently, avoids small prime-support redundancies). That becomes a genuinely mixed extremal-combinatorics/analytic-number-theory problem; the (\sqrt n) barrier enters because products of two primes both (>\sqrt n) exceed $n$, so “large-prime edges” must be routed through primes (\le \sqrt n), which is exactly why (\pi(\sqrt n)) appears in the extremal case. [[nomath]](This is the backbone of the Erdős–Straus proof of $14$/$10$.)[[/nomath]] ([Renyi Institute][1])

If you want a **practical summary** for (\pi(n)+1<k=o(n)):

* We have a good understanding at the **bottom** end (k=\pi(n)+O(1)): $f$ stays on the (\asymp 2\pi(\sqrt n)) scale.
* We have a good understanding at the **top** end (k\sim cn): $f$ is on the (\asymp \log\log n) scale.
* In between, there isn’t (at least in these classical sources) a generally accepted sharp asymptotic formula; even Erdős flagged it as not sharp in 1970. ([Renyi Institute][1])

---

## 5) Quick note on your “(\ge r)” variant

Let me denote your version by (f_{\ge}(k,n)) and the Erdős–Straus one by (f_{>}(k,n)). Then always
[
f_{\ge}(k,n)\le f_{>}(k,n),
]
because “(\ge r+1)” supported integers implies “(\ge r)” supported integers.

But the gap between these two variants can be more than a constant [[nomath]](the underlying combinatorics shifts from forcing a substructure with “edges >,vertices” to one with “edges $\ge$,vertices”, i.e. from “bicyclic” to “unicyclic” in the graph-theoretic model)[[/nomath]]. So if your goal is specifically the (2\pi(\sqrt n)) benchmark and the Erdős–Straus conjecture, you almost certainly want the (>r) definition (the one used in the literature and in the sources above). ([Renyi Institute][1])

---

If you tell me which definition you want to stick to [[nomath]](your “$\ge r$” or the classical “$>r$”)[[/nomath]], I can tailor the “intermediate regime” discussion more tightly to the right combinatorial model (cycle vs. bicyclic obstruction).

[1]: https://users.renyi.hu/~p_erdos/1970-20.pdf "https://users.renyi.hu/~p_erdos/1970-20.pdf"
