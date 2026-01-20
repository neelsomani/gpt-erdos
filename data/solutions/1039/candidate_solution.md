Write
[
\Lambda_f:={z\in\mathbb C:\ |f(z)|<1}
]
[[nomath]](the filled lemniscate of $f$)[[/nomath]]. Your (\rho(f)) is exactly the **inradius** of (\Lambda_f):
[
\rho(f)=\sup{r>0:\ \exists a\in\mathbb C\text{ with }D(a,r)\subset \Lambda_f}.
]

A natural way to phrase the “worst case in $n$” is
[
\rho_n:=\inf{\rho(f): f \text{ monic, }\deg f=n,\ \text{all zeros in }\overline{\mathbb D}}.
]
Then your question “is it always true that (\rho(f)\gg 1/n)?” is exactly: **is (\rho_n \gg 1/n)?**

## Upper bound: (\rho_n\lesssim 1/n) [[nomath]](so $1/n$ would be best possible)[[/nomath]]

Take the Erdős lemniscate polynomial
[
f(z)=z^n-1,
]
whose zeros are the $n$th roots of unity [[nomath]](all on $|z|=1$)[[/nomath]]. It is known (and easy to see) that its inradius is on the order of $1/n$; in particular (\rho(z^n-1)\asymp 1/n). This provides the general upper bound
[
\rho_n \le \rho(z^n-1) \asymp \frac1n.
]
So **no uniform lower bound can beat the order $1/n$**.

[[nomath]](You can see the scale quickly: near a root $\zeta$, $(z^n-1)\approx n\zeta^{n-1}(z-\zeta)$, so $|z-\zeta|\lesssim 1/n$ is the natural scale for $|z^n-1|<1$.)[[/nomath]]

## Lower bounds: what is known for all $f$ (and what is open)

The precise question “(\rho_n\gg 1/n)?” is **classical and open**. It was posed in a 1958 problem of Erdős–Herzog–Piranian, who conjectured that (z^n-1) is extremal and hence (\rho_n\asymp 1/n). 

What *is* known:

* **Pommerenke (1961)** proved the general lower bound (\rho_n \ge c/n^2) [[nomath]](for an absolute constant $c>0$)[[/nomath]]. 
* **Krishnapur–Lundberg–Ramachandran (2025)** improved this substantially to
  [
  \rho_n \ \ge\ \frac{c}{n\sqrt{\log n}}.
  ]
  This is their Theorem 8. 

So, at present the best general information is the two-sided estimate
[
\frac{c}{n\sqrt{\log n}} \ \lesssim\ \rho_n \ \lesssim\ \frac{C}{n},
]
and the missing piece is the removal of the (\sqrt{\log n}) factor on the lower bound.

### Why the (1/(n\sqrt{\log n})) shows up (very brief explanation)

The same 2025 paper proves an inequality relating inradius to area (confirming a conjecture of Solynin–Williams): for any degree-$n$ polynomial $p$,
[
\rho(\Lambda_p(t)) \ \gtrsim\ \frac{\sqrt{\mathrm{Area}(\Lambda_p(t))}}{n}
]
(up to an explicit absolute constant). 
Combining this with their lower bounds on the minimal area of (\Lambda_p) under the “zeros in (\overline{\mathbb D})” constraint yields the stated (\rho_n \gtrsim 1/(n\sqrt{\log n})). 

## Direct answer to your “in particular”

* The statement **(\rho(f)\gg 1/n) for all such $f$** is **conjectured but not proved** (as of the latest results I could find, up through 2025/early 2026). 
* What is proved unconditionally is the weaker but still polynomial-scale bound
  [
  \rho(f)\ \ge\ \frac{c}{n\sqrt{\log n}}
  \quad\text{for all monic }f\text{ of degree }n\text{ with zeros in }\overline{\mathbb D}.
  ]

* And there are examples [[nomath]](notably $z^n-1$)[[/nomath]] with (\rho(f)\asymp 1/n), so the conjectured order $1/n$ would be sharp. 

If you tell me whether you care about $i$ the worst-case (\rho_n) or (ii) bounds for a specific configuration of zeros [[nomath]](e.g. separated vs clustered, all on $\mathbb T$, etc.)[[/nomath]], I can tailor the discussion: in many restricted regimes one can prove stronger $c/n$-type bounds.
