Write the prime gap (g_n:=p_{n+1}-p_n). Then
[
u_{n+1}>u_n \iff \frac{p_{n+1}}{n+1}>\frac{p_n}{n}
\iff n(p_{n+1}-p_n)>p_n
\iff g_n>\frac{p_n}{n}=u_n.
]
So the question is asking whether **a positive proportion of prime gaps exceed the “average spacing so far”** (p_n/n) [[nomath]](which, by the prime number theorem, is $\sim \log n+\log\log n-1$, i.e. essentially $\log p_n -1$)[[/nomath]]. ([Erdős Problems][1])

### What is known unconditionally

This is an **Erdős problem and is currently open**: no unconditional proof is known that the set
[
{n:\ u_n<u_{n+1}}
]
has positive asymptotic density. ([Erdős Problems][1])

What *is* known is a kind of complementary statement: Erdős–Prachar $1961/62$ proved, among other things, that

* (\sum_{p_n<x}\lvert u_{n+1}-u_n\rvert \asymp (\log x)^2), and
* the set ({n:\ u_n>u_{n+1}}) (i.e. (g_n<p_n/n)) has **positive density**. ([Erdős Problems][1])

There are also later results (Goldston–Pintz–Yıldırım) showing that **small prime gaps occur with positive proportion** in a quantitative sense (their paper is explicitly about “density of small gaps”). ([ar5iv][2])
These reinforce that “(u_n>u_{n+1})” happens often, but they do **not** settle whether “(u_n<u_{n+1})” happens with positive density.

### Conditional results (why people expect “yes”)

There are standard conjectural frameworks under which the answer becomes “yes”.

* Under a sufficiently uniform form of the **Hardy–Littlewood prime $k$-tuples conjecture**, Gallagher’s calculation predicts that the normalized gaps ((p_{n+1}-p_n)/\log p_n) are asymptotically **exponentially distributed**. ([ar5iv][2])
  In that exponential model with mean $1$, one expects
  [
  \mathbb{P}\left(\frac{p_{n+1}-p_n}{\log p_n} > 1\right)=e^{-1}\approx 0.368,
  ]
  hence a **positive density** [[nomath]](indeed about $36.8%$)[[/nomath]] of indices with (u_{n+1}>u_n).

* Terence Tao noted (on the Erdős Problems discussion thread) that one can also get a **conditional affirmative answer** assuming the **Riemann hypothesis** plus a weak form of the **pair correlation conjecture** (in the style of Heath-Brown’s work relating pair correlation to prime gaps). ([Erdős Problems][3])

### Bottom line

Unconditionally: **open** (no proof known). ([Erdős Problems][1])
Heuristically and under standard conjectures: **yes**, and in the “Poisson/exponential gap” picture one even expects a limiting density close to (e^{-1}\approx 0.368). ([ar5iv][2])

[1]: https://www.erdosproblems.com/968 "
  
    Erdős Problem #968
  
"
[2]: https://ar5iv.org/abs/1103.5886 "[1103.5886] Primes in Tuples IV: Density of small gaps between consecutive primes"
[3]: https://www.erdosproblems.com/forum/discuss/968 "

    Erdős Problem #968 - Discussion thread

"
