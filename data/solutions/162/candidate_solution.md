There is a problem with the definition as you wrote it.

### 1) With your definition, (F(n,\alpha)=n) for every fixed (\alpha<\tfrac12)

Take (k=n). Then the only induced subgraph (H) with (|H|\ge k) is (H=K_n) itself.

Now colour the edges of (K_n) so that each colour has about half the edges [[nomath]](for example, colour exactly $\lfloor \binom{n}{2}/2\rfloor$ edges red and the rest blue)[[/nomath]]. Then each colour has (\ge \tfrac12\binom{n}{2}-1) edges, so for any fixed (\alpha<\tfrac12) and all large $n$,
[
e_{\text{red}}(K_n)>\alpha\binom{n}{2}\quad\text{and}\quad e_{\text{blue}}(K_n)>\alpha\binom{n}{2}.
]
So (k=n) is always achievable, hence (F(n,\alpha)=n). This cannot be asymptotic to (c_\alpha\log n).

So the statement you want (“(\sim c_\alpha\log n)”) cannot be true for the function as currently defined.

---

### 2) The nontrivial version people study [[nomath]](and which *does* have size $\Theta(\log n)$)[[/nomath]]

The Erdős problem usually meant here is the *threshold* version:

> Let (f(n,\alpha)) be the **smallest** $k$ such that there exists a 2-colouring of (E(K_n)) in which **every** induced subgraph (H) with (|H|\ge k) has more than (\alpha\binom{|H|}{2}) edges of each colour.

This is exactly the version that is known to satisfy
[
f(n,\alpha)=\Theta_\alpha(\log n),
]
and the stronger statement
[
f(n,\alpha)\sim c_\alpha\log n
]
is explicitly listed as open in the Erdős problems collection. ([Erdős Problems][1])

Below I prove the standard (and “easy”) (\Theta(\log n)) bound.

---

## 3) Key reduction: it is enough to check sets of size exactly (k)

Call a vertex set $S$ “good” if in the induced subgraph on $S$ each colour has (>\alpha\binom{|S|}{2}) edges.

**Lemma.** If every induced subgraph on exactly $k$ vertices is good, then every induced subgraph on at least $k$ vertices is good.

**Proof (simple averaging).**
Suppose some $S$ with (|S|=m>k) is bad, say it has (\le \alpha\binom{m}{2}) red edges. Pick a uniformly random $k$-subset (T\subseteq S). Each red edge inside $S$ appears in exactly (\binom{m-2}{k-2}) different $k$-subsets, so
[
\mathbb{E},e_{\text{red}}(T)=e_{\text{red}}(S)\cdot \frac{\binom{k}{2}}{\binom{m}{2}}
\le \alpha\binom{k}{2}.
]
So some $k$-subset $T$ has (e_{\text{red}}(T)\le \alpha\binom{k}{2}), i.e. $T$ is bad. Contradiction. ∎

So for existence it is enough to build a colouring where **every** $k$-set is good.

---

## 4) Upper bound: (f(n,\alpha)\le C_2(\alpha)\log n) (random colouring)

Fix (\alpha<\tfrac12). Let (\delta=\tfrac12-\alpha>0).

Colour each edge independently red/blue with probability $1/2$.

Fix a particular $k$-set $S$. Let
[
N=\binom{k}{2},\quad X=e_{\text{red}}(S).
]
Then (X\sim\mathrm{Bin}(N,1/2)). By a standard Chernoff/Hoeffding bound,
[
\Pr\big(X\le (\tfrac12-\delta)N\big)\le \exp(-2\delta^2 N),
]
and similarly
[
\Pr\big(X\ge (\tfrac12+\delta)N\big)\le \exp(-2\delta^2 N).
]
So
[
\Pr(S\text{ is bad})\le 2\exp(-2\delta^2 N)\le 2\exp(-\delta^2 k(k-1)).
]

There are (\binom{n}{k}\le (en/k)^k) many $k$-sets. By the union bound,
[
\Pr(\exists\text{ a bad }k\text{-set})\le \binom{n}{k}\cdot 2e^{-\delta^2 k(k-1)}
\le 2\left(\frac{en}{k}\right)^k e^{-\delta^2 k(k-1)}.
]

Now take (k=C\log n). Then the exponent is of order
[
k\log n-\delta^2 k^2 \approx C(\log n)^2-\delta^2 C^2(\log n)^2.
]
If (C>1/\delta^2) [[nomath]](say $C=2/\delta^2$)[[/nomath]], the negative term wins for large $n$, so the probability above is (<1). Hence there exists a colouring with **no bad $k$-set**, and by the lemma, no bad set of size (\ge k).

So for some constant (C_2(\alpha)) [[nomath]](for example $C_2(\alpha)=2/(1/2-\alpha)^2$)[[/nomath]],
[
f(n,\alpha)\le C_2(\alpha)\log n.
]

---

## 5) Lower bound: (f(n,\alpha)\ge C_1\log n) (Ramsey)

A monochromatic clique on $t$ vertices is certainly bad for every (\alpha>0), because one colour has $0$ edges.

But every 2-colouring of (E(K_n)) contains a monochromatic clique of size at least (c\log n) (a classical Ramsey lower bound). Using the standard bound (R(t,t)\le 4^t), we get that any colouring of (K_n) contains a monochromatic clique of size at least
[
t \ge \frac12\log_2 n = \frac{1}{2\ln 2},\ln n.
]
Therefore every colouring has a bad induced subgraph on at least (C_1\log n) vertices, where (C_1=1/(2\ln 2)) works. So you cannot make “all sets of size (\ge k) good” when $k$ is smaller than this. Hence
[
f(n,\alpha)\ge C_1\log n.
]

---

## 6) Conclusion: the “easy part” is (f(n,\alpha)=\Theta_\alpha(\log n))

Putting the two bounds together:
[
C_1\log n \le f(n,\alpha)\le C_2(\alpha)\log n,
]
so (f(n,\alpha)=\Theta_\alpha(\log n)).

This is exactly what is recorded in the Erdős problems entry, and the stronger claim (f(n,\alpha)\sim c_\alpha\log n) is listed there as open. ([Erdős Problems][1])

---

## 7) Why people expect a constant (c_\alpha) (heuristic)

In a random colouring, a fixed $k$-set is bad with probability roughly
[
\exp\big(-I(\alpha)\binom{k}{2}\big)
]
for a large-deviation “rate” (I(\alpha)>0), and there are about (n^k) many (k)-sets. Balancing
[
n^k\cdot \exp\big(-I(\alpha)\tfrac{k^2}{2}\big)\approx 1
]
suggests a threshold at (k\approx \frac{2}{I(\alpha)}\log n). Proving that this threshold is the true optimum (and that the ratio converges) is the hard open part.

---

If you tell me which exact definition you intended (because the “largest $k$” version is trivial), I can tailor the proof to match it. But for the standard nontrivial interpretation, the best unconditional result is exactly the (\Theta_\alpha(\log n)) bound above, and the “(\sim c_\alpha\log n)” limit is open. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/tags/hypergraphs/no "
  
    Erdős Problems
  
"
