Let (L) be the number of distinct lines that contain at least (4) of the (n) points, and assume
[
L \ge c n^{2}.
]
Define (h_c(n)) as the largest function such that **every** such configuration has **some** line containing at least (h_c(n)) points.

## Two easy bounds you always have

### 1) (c) cannot be too big

Each line with (\ge 4) points contains at least (\binom{4}{2}=6) unordered pairs of points, and different lines contain disjoint sets of pairs (a pair of points determines a unique line). So
[
6L \le \binom{n}{2} \sim \frac{n^{2}}{2}.
]
Hence
[
L \le \frac{n(n-1)}{12} \quad\text{so necessarily}\quad c \le \frac{1}{12}.
]

So the problem is only meaningful for (0<c\le 1/12).

### 2) Trivial lower bound

Since you already have lines with (>3) points, you automatically have a line with at least (4) points. So
[
h_c(n)\ge 4.
]

## What is known (and what is not)

### Lower bounds: basically nothing beyond (4)

It is currently **open** to prove even the next step:

> for fixed (c>0), must there always be a line with (5) points?

In fact, the Erdős–Purdy problem statement notes that *it is not even known whether (h_c(n)\ge 5).* ([Erdős Problems][1])

So, at the moment, there is **no proved lower bound** that grows with (n). In particular, the question “does (h_c(n)\to\infty) for fixed (c)?” is **open**. ([Erdős Problems][1])

### Upper bounds: there are constructions where the “largest line” is quite small

There are explicit constructions showing you cannot hope for a very large guaranteed line.

* It is “easy to see” that one can have (\ge c n^{2}) such rich lines while keeping the largest collinear set (\ll_c n^{1/2}). ([Erdős Problems][1])
  (Erdős also states this type of (\sqrt n) upper bound in his discussion of the problem.) 

* Even more strongly, there is a construction idea (points in a high-dimensional grid ({1,\dots,m}^d), then randomly project to (\mathbb R^2)) that keeps **every** line intersection small, yet still produces (\gg c n^{2}) rich lines. This yields an upper bound of the form
  [
  h_c(n) \ll n^{,1/\log(1/c)}.
  ]
  ([Erdős Problems][1])

So (h_c(n)) cannot be forced to be as large as (n^{1/2}) in general; that “(\sqrt n)” lower-bound guess is false. ([Erdős Problems][1])

(Example to calibrate: if (c=10^{-6}), then (\log(1/c)\approx 13.8), so this gives a construction with largest line size (\ll n^{0.072}).)

## Relation to a nearby famous open problem

A closely related question is:

> If no (5) points are collinear, is the number of (4)-point lines always (o(n^2))?

This is also open (Erdős Problem #101). ([Erdős Problems][2])
There are constructions (Solymosi–Stojaković) with **no five collinear** but with at least
[
n^{2-O(1/\sqrt{\log n})}
]
lines containing exactly (4) points, which is very close to quadratic (but still (o(n^2))). ([Erdős Problems][2])

This shows why proving even (h_c(n)\ge 5) is hard: we already know you can get “almost” (n^2) four-point lines without ever creating a five-point line, just not with a *fixed positive* density (c). ([Erdős Problems][2])

## Best current “estimate” summary

For fixed (0<c\le 1/12), the state of knowledge is:

[
\boxed{4 \ \le\ h_c(n)\ \le\ n^{,1/\log(1/c)} \quad\text{(and also } h_c(n)\ll_c n^{1/2}\text{)}.}
]
([Erdős Problems][1])

And the key point:

[
\boxed{\text{It is not known whether, for fixed } c>0,\ h_c(n)\to\infty.}
]
In fact, it is not even known whether (h_c(n)\ge 5). ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/102 "
  
    Erdős Problem #102
  
"
[2]: https://www.erdosproblems.com/101 "
  
    Erdős Problem #101
  
"
