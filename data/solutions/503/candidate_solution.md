This is the **“isosceles set”** problem of Erdős.  Let

$
I(d):=\max\\{|A|:A\subset\mathbb{R}^d\ \text{and every triple in }A\text{ has two equal distances\\}}.
$

## General bound [[nomath]](all $d$)[[/nomath]]

Blokhuis proved the sharp **quadratic upper bound**
[
I(d)\ \le\ \binom{d+2}{2}=\frac{(d+1)(d+2)}{2}.
]
Moreover, equality forces very strong structure (essentially a 2‑distance set, or a spherical 2‑distance set together with its center). 

## Exact values known [[nomath]](dimensions $d\le 8$)[[/nomath]]

The exact maximum is known only up to (d=8). The values are 

$
\begin{array}{c|cccccccc}
d & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8\
I(d) & 3 & 6 & 8 & 11 & 17 & 28 & 30 & 45
\end{array}
$

Some “model” extremal configurations:

* (d=2): uniquely (up to similarity) **regular pentagon + its center** (6 points). ([Wikipedia][1])
* (d=3): 8 points: the planar 6‑point set above, plus **two points on the perpendicular line through the center** (symmetric above/below the plane). ([Wikipedia][1])

## What happens for (d\ge 9)?

As of the current literature summaries, **$I(d)$ is not known for any (d\ge 9)**. ([Wikipedia][1])

What *is* known are general bounds. A standard construction (attributed to Lisoněk in this context) produces isosceles sets of size
[
\binom{d+1}{2}+1=\frac{d(d+1)}{2}+1
]
in (\mathbb{R}^d) [[nomath]](for $d\ge 2$)[[/nomath]], by taking a certain (\binom{d+1}{2})-point two‑distance configuration [[nomath]](vertices of the hypersimplex $\Delta_{d+1,2}$)[[/nomath]] and adding its centroid. ([Wikipedia][1])

So for (d\ge 2) one has the clean “sandwich”:
[
\boxed{\ \binom{d+1}{2}+1\ \le\ I(d)\ \le\ \binom{d+2}{2}\ }.
]
([Wikipedia][1])

If you tell me a specific dimension $d$ you care about [[nomath]](e.g. $d=9,10,12$)[[/nomath]], I can spell out the numerical interval this gives and the known best constructions/bounds in that range.

[1]: https://en.wikipedia.org/wiki/Isosceles_set "Isosceles set - Wikipedia"
