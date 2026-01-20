This is **open in general** (it’s listed as an open Erdős problem, #1004). ([Erdős Problems][1])

What *is* known is that you can prove the statement for a substantial range of exponents $c$, but current methods do not reach **all** (c>0).

## What’s known unconditionally

### 1) The full “for every (c>0)” statement is open

Exactly your question appears verbatim as Erdős Problem #1004 and is currently marked open. ([Erdős Problems][1])

A related (rather weak, but unconditional) upper bound due to Erdős–Pomerance–Sárközy says: if (\phi(n+k)) are all distinct for (1\le k\le K), then
[
K \le \frac{n}{\exp!\big(c(\log n)^{1/3}\big)}
]
for some absolute constant (c>0). ([Erdős Problems][1])
(This does **not** contradict the conjectured existence of polylogarithmic runs; it just rules out extremely long runs.)

### 2) You *can* prove it for every fixed (c<2)

Let
[
L:=\lfloor (\log x)^c\rfloor.
]
Call a starting point (n\le x) **bad** if there exist (1\le i<j\le L) with (\phi(n+i)=\phi(n+j)). Put (k=j-i) and (m=n+i). Then (\phi(m)=\phi(m+k)) with (1\le k\le L-1).

A standard counting/union-bound argument shows:
[
|\\{\text{bad }n\le x\\}|\ \le\ \sum_{k=1}^{L-1} (L-k),P(x+L;k),
]
where (P(X;k):=|\\{m\le X:\ \phi(m)=\phi(m+k)\\}|).

Now use the deep uniform bounds of Pollack–Pomerance–Treviño on solutions of (\phi(m)=\phi(m+k)). They split solutions into “non-structured” ones (P_1(X;k)) and “structured” ones (P_0(X;k)), with
[
P(X;k)=P_0(X;k)+P_1(X;k).
]

* **Uniform bound for (P_1):**
  [
  P_1(X;k)\ <\ \frac{X}{\exp((\log X)^{1/3})}
  \quad\text{uniformly for }k\le \exp((\log X)^{1/3}).
  ]

  Since (L=(\log x)^c \ll \exp((\log x)^{1/3})), this applies for all (k\le L) and is *tiny* [[nomath]](beats any power of $\log x$)[[/nomath]].

* **Uniform bound for (P_0) [[nomath]](even $k$)[[/nomath]]:**
  for even (k\le X^{\varepsilon(X)}) [[nomath]](with $\varepsilon(X)\to0$, $X^{\varepsilon(X)}\to\infty$)[[/nomath]],
  [
  P_0(X;k)\ \le\ (16C_2+o(1)),c(k),\frac{X}{(\log X)^2},
  ]
  and crucially $c(k)$ is bounded by (\ll k^{-1}) up to very slowly growing factors [[nomath]](they explicitly give $(2k)^{-1}\le c(k)\le \text{(something)}\cdot k^{-1}$, and remark that $c(k)\ll k^{-1}\exp(O(\log k/\log\log(3k)))$)[[/nomath]]. 

Putting these together [[nomath]](and noting odd $k$ contribute only the exponentially small $P_1$ term)[[/nomath]], one gets for (k\le L):
[
P(x+L;k)\ \ll\ \frac{x}{k(\log x)^2}\cdot (\log x)^{o(1)}\ +\ \frac{x}{\exp((\log x)^{1/3})}.
]

Therefore
[
|\\{\text{bad }n\le x\\}|
\ \ll
\frac{x}{(\log x)^2}(\log x)^{o(1)}
\sum_{k=1}^{L-1}\frac{L-k}{k}
\ +\ x\cdot \frac{L^2}{\exp((\log x)^{1/3})}.
]
But (\sum_{k\le L}(L-k)/k \asymp L\log L), so the main term is
[
\ll\ x\cdot \frac{L\log L}{(\log x)^2}\cdot(\log x)^{o(1)}.
]
If (c<2), then (L=(\log x)^c) makes
[
\frac{L\log L}{(\log x)^2} = \frac{(\log x)^c \cdot \log\log x}{(\log x)^2} = (\log x)^{c-2}\log\log x \to 0,
]
so (|\\{\text{bad }n\le x\\}| = o(x)). Hence at least one **good** (n\le x) exists, i.e. (\phi(n+1),\dots,\phi(n+L)) are all distinct.

So:

* **Yes** for every fixed (c<2) (unconditionally, by the above bounds). 

## What remains open

For **(c\ge 2)**, the above approach no longer forces (#\text{bad }n < x), and at present there is no known method that settles the question for *all* (c>0). This is why the problem is still listed as open in the Erdős problems database. ([Erdős Problems][1])

If you’d like, I can also sketch the heuristic that suggests $c=2$ is a “natural barrier” for this particular counting method [[nomath]](because the main obstruction comes from the structured $P_0$-type solutions behaving like prime-pair events)[[/nomath]], but the rigorous status is exactly as above.

[1]: https://www.erdosproblems.com/1004 "https://www.erdosproblems.com/1004"
