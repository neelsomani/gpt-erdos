This is **Erdős Problem #670**. For (d\ge 2) it is **open**; for $d=1$ it is **true**. ([Erdős Problems][1])

Here’s what is known and what is easy.

## The trivial lower bound is (\binom n2)

Let the distinct interpoint distances be
[
0<r_1<r_2<\cdots<r_m,\qquad m=\binom n2.
]
Your hypothesis says (r_{k+1}-r_k\ge 1) for all $k$.

Also, when (n\ge 3), every distance is at least $1$: for any two points $x,y$ and any third point $z$,
[
|,|x-z|-|y-z|,|\le |x-y|
]
by the triangle inequality, while (|x-z|\neq |y-z|) and all distances differ by at least $1$, so (||x-z|-|y-z||\ge 1), hence (|x-y|\ge 1).

Therefore (r_1\ge 1), and
[
\operatorname{diam}(A)\ge r_m \ge r_1+(m-1)\ge 1+(m-1)=m=\binom n2.
]
This is the “trivial” (\binom n2) bound mentioned in the problem’s statement. ([Erdős Problems][1])

So in particular,
[
\operatorname{diam}(A)\ge \left(\tfrac12+o(1)\right)n^2.
]

## $d=1$: yes, (\operatorname{diam}(A)\ge (1+o(1))n^2)

Erdős proved the ((1+o(1))n^2) lower bound in **one dimension**. ([Erdős Problems][1])

Intuitively, in $d=1$ the problem becomes the asymptotics of **Golomb rulers / Sidon sets**: $n$ points on a line with all pairwise distances distinct correspond (after translation) to a set of $n$ marks whose difference set has no repeats, i.e. a Golomb ruler. ([Wikipedia][2])
Classical results on Sidon sets (Erdős–Turán upper bounds and Singer-type lower bound constructions) imply that the shortest such configuration has length (\sim n^2), giving (\operatorname{diam}(A)\ge (1+o(1))n^2). ([Erdős Problems][3])

## (d\ge 2): unknown

For (d\ge 2), it is **not known** whether the diameter must be ((1+o(1))n^2). The problem is explicitly listed as **open**. ([Erdős Problems][4])

What we *do* know in all dimensions is essentially the sandwich:
[
\binom n2 \le \inf \operatorname{diam}(A)\le (1+o(1))n^2,
]
where the upper bound comes from taking a near-optimal 1D construction (Golomb ruler / Sidon set) and embedding it on a line inside (\mathbb{R}^d). ([Wikipedia][2])

So the constant factor is currently only pinned down between (\tfrac12) and $1$ asymptotically, and the question is whether higher-dimensional geometry can beat the 1D “Sidon/Golomb” barrier or not.

[1]: https://www.erdosproblems.com/latex/670 "
  
    Erdős Problems
  
"
[2]: https://en.wikipedia.org/wiki/Golomb_ruler "https://en.wikipedia.org/wiki/Golomb_ruler"
[3]: https://www.erdosproblems.com/30 "
  
    Erdős Problem #30
  
"
[4]: https://www.erdosproblems.com/forum/thread/670 "

    Erdős Problem #670 - Discussion thread

"
