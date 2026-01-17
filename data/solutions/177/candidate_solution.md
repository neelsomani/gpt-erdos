Let

[
D_f(d):=\max_{P_d}\left|\sum_{n\in P_d} f(n)\right|
]

[[nomath]](where $P_d$ runs over all finite arithmetic progressions with common difference $d$)[[/nomath]].
Your question asks for the *smallest possible* function $h(d)$ for which there exists some (f:\mathbb N\to{-1,1}) with

[
D_f(d)\le h(d)\qquad\text{for every }d\ge 1.
]

This exact “best” $h(d)$ is **not known**. What *is* known are the best current upper and lower bounds.

## What is known (best bounds)

### 1) $h(d)$ must go to infinity

You cannot have $h(d)$ bounded by a constant for all $d$. This already follows from van der Waerden–type phenomena: any 2‑coloring contains arbitrarily long monochromatic arithmetic progressions, which force large sums on some differences as $d$ grows. ([Erdős Problems][1])

So at minimum:
[
h(d)\to\infty.
]

### 2) Quantitative lower bound: at least about (\sqrt d)

A classical discrepancy lower bound of Roth implies that any such $h(d)$ must grow **at least on the order of** (d^{1/2}) (up to constants). In standard asymptotic notation:

[
h(d)\gg d^{1/2}.
]

([Erdős Problems][1])

### 3) Upper bounds (constructions exist)

* **Old (super‑exponential) upper bound:** Cantor–Erdős–Schreiber–Straus showed it is possible with something like
  [
  h(d)\ll d!
  ]
  ([Erdős Problems][1])

* **Best published general upper bound (polynomial):** József Beck (2017) proved a major improvement: for every (\varepsilon>0), one can build a coloring $f$ such that, for all sufficiently large $d$,
  [
  h(d)\le d^{8+\varepsilon}.
  ]
  ([IDEAS/RePEc][2])

## So the “smallest” $h(d)$ is only known within a big range

Putting the best known bounds together, the optimal growth rate (h_{\min}(d)) satisfies

[
c,\sqrt d \le h_{\min}(d)\le d^{8+\varepsilon}\quad(\text{for any }\varepsilon>0,\text{ for large }d),
]

for some absolute constant (c>0). ([Erdős Problems][1])

## What is still open

The big open part is: **close the exponent gap** between $1/2$ and $8$. Even improving $8$ down to (say) $2$, or showing the true answer is close to (\sqrt d), would be major progress. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/177?utm_source=chatgpt.com "Erdős Problem #177"
[2]: https://ideas.repec.org/h/spr/sprchp/978-3-319-55357-3_3.html "https://ideas.repec.org/h/spr/sprchp/978-3-319-55357-3_3.html"
