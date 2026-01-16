This is a well-known Erdős problem about **planar integer-distance sets in general position** (no three collinear, no four cocircular).

* For **(n=4,5,6,7)**: **yes**, such sets exist (just take $n$ points from a known 7-point example).
* For **(n\ge 8)**: it is **open** whether such a set exists; in particular, **no example with 8 points is known**. ([Erdős Problems][1])

## A concrete 7-point example [[nomath]](so $n\le 7$ is possible)[[/nomath]]

Kreisel and Kurz (2008) found a configuration of **7 points** in the plane with **all pairwise distances integers**, with **no three on a line** and **no four on a circle** (diameter $22270$). 

One coordinate realization they give is:

[
\begin{aligned}
P_1&=\left(0,0\right),\
P_2&=\left(22270,0\right),\
P_3&=\left(\frac{26127018}{2227},\frac{932064}{2227}\sqrt{2002}\right),\
P_4&=\left(\frac{245363}{17},\frac{3144}{17}\sqrt{2002}\right),\
P_5&=\left(\frac{17615968}{2227},\frac{238464}{2227}\sqrt{2002}\right),\
P_6&=\left(\frac{56068}{17},\frac{3144}{17}\sqrt{2002}\right),\
P_7&=\left(\frac{19079044}{2227},-\frac{54168}{2227}\sqrt{2002}\right).
\end{aligned}
]

These seven points realize an **integral distance matrix** (all interpoint distances are integers) and are in **general position** as required. 

Hence, for each (n=4,5,6,7), just select any $n$ of these points.

## What happens for (n\ge 8)?

As of the current literature status, the “next case” (n=8) is **not resolved**. Kreisel–Kurz explicitly pose the 8-point question as the natural continuation after their 7-point construction. 

Computational/constructive work also reports that **no 8-point configuration in general position has been found** (“the hunt … is still open”). 

## Partial evidence: strong sparsity / conditional boundedness

Recent work doesn’t settle existence of an 8th point, but it shows such sets are very constrained:

* Conditionally (assuming **Bombieri–Lang**), there is a **uniform upper bound** on the size of such a set. ([Erdős Problems][1])
* Unconditionally, Greenfeld–Iliopoulou–Peluse prove that if such a set lies in a box ([{-}N,N]^2), then its size is at most polylogarithmic in (N): (|S|\ll (\log N)^{O(1)}). They also note that **no larger example than 7 is known**. ([arXiv][2])

So the best current answer is:

* **Yes** for (4\le n\le 7).
* **Unknown/open** for (n\ge 8). ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/213 "
  
    Erdős Problem #213
  
"
[2]: https://arxiv.org/pdf/2401.10821?utm_source=chatgpt.com "On integer distance sets"
