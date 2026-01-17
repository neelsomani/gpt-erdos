No — this is not known in full generality.

What you stated is exactly **Erdős’s 1946 conjecture** about “almost everywhere monotone” additive functions, and it is currently listed as **open** (e.g. as Erdős Problem #1122). ([Erdős Problems][1])

### What is known

* **Erdős (classical rigidity).** If the set of decreases is empty [[nomath]](i.e. $f(n+1)\ge f(n)$ for all $n$)[[/nomath]], or if the gaps satisfy (f(n+1)-f(n)=o(1)), then (f(n)=c\log n) for some constant $c$. ([Erdős Problems][2])

* **Wirsing (bounded gaps).** If (|f(n+1)-f(n)|) is uniformly bounded, then (f(n)=c\log n+O(1)) for some constant $c$. ([Erdős Problems][2])

* **Mangerel (2022) — a conditional/strong-sparseness implication.** Writing (B={n:, g(n)<g(n-1)}) [[nomath]](the same “decrease set” as your $A$, up to a shift)[[/nomath]], Mangerel proves that if
  [
  |B(X)|\ll \frac{X}{(\log X)^{2+\delta}}
  ]
  for some (\delta>0) **and** $g$ is completely additive **and** $g(p)$ is not “extremely large too often” on the primes (a precise technical condition), then (g(n)=c\log n) identically. ([Springer][3])

* **Mangerel (2022) — an unconditional approximate form under (|B(X)|=o(X)).** Under only (|B(X)|=o(X)), he proves an **approximate logarithm law**: there exist slowly varying parameters (\lambda(X)), (\eta(X)) such that for all but $o(X)$ integers (n\le X),
  [
  g(n)=\lambda(X)\log n-\eta(X)+o(B_g(X)),
  ]
  where (B_g(X)) is the standard “variance” scale for additive functions. ([Springer][3])
  He also proves that $g(p^k)$ is close [[nomath]](in a weighted $L^2$ sense over prime powers $\le X$)[[/nomath]] to (\lambda(X)\log(p^k)). 

### Why the $o(X)$ threshold is genuinely the hard one

Mangerel also notes that you **cannot** hope for the conclusion if you only assume the decrease set has *small positive density*: for any (\varepsilon>0) one can construct a completely additive $g$ that is monotone except on a set of density (<\varepsilon), yet is **not** a constant multiple of (\log n). ([Springer][3])
So the conjecture really lives at the “density $0$” frontier.

### What remains open (the gap between “approximate” and “exact”)

Mangerel explicitly identifies two main obstructions to proving the full conjecture from (|B(X)|=o(X)):

1. (|B(X)|=o(X)) may still be *too large* (not sparse enough) to force full rigidity by current methods.
2. The additive function may take *very large values on primes* in a way that is hard to rule out. 

He also remarks that if one could make the approximation hold simultaneously on multiplicatively related triples (n,m,nm) in a suitable range, one would be able to force away the “(-\eta)” term (and get closer to a true homomorphism). But establishing this kind of simultaneous control is precisely what is not currently available. 

### Bottom line

As of **January 2026**, the implication

[
|A\cap[1,X]|=o(X)\quad\Longrightarrow\quad f(n)=c\log n\ \text{for all }n
]

is a well-known **open Erdős conjecture**; the best unconditional results give strong approximation to (c\log n) on a density $1$ set, and a full rigidity theorem under substantially stronger sparseness assumptions plus constraints on prime values. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/1122 "
  
    Erdős Problem #1122
  
"
[2]: https://www.erdosproblems.com/search_bib/Er82e?sources_only=1 "
  
    Erdős Problems
  
"
[3]: https://link.springer.com/content/pdf/10.1007/s11139-022-00623-y.pdf "Additive functions in short intervals, gaps and a conjecture of Erdős"
