No. In fact there are **infinitely many** such identities with all indices distinct.

Write
[
B_t:=\binom{2t}{t}\qquad(t\in\mathbb Z_{\ge 0}).
]
A standard ratio computation gives
[
\frac{B_t}{B_{t+1}}
=\frac{\binom{2t}{t}}{\binom{2t+2}{t+1}}
=\frac{(t+1)^2}{(2t+2)(2t+1)}
=\frac{t+1}{2(2t+1)}.
\tag{1}
]

Now fix an integer (a\ge 2) and set
[
c:=8a^2+8a+1.
]
Consider the six indices
[
m\text{-side: } {a,;2a+2,;c},
\qquad
n\text{-side: } {a+1,;2a,;c+1}.
]
For (a\ge2) these are **pairwise distinct** (in particular the two sides are disjoint).

We claim
[
B_a,B_{2a+2},B_c ;=; B_{a+1},B_{2a},B_{c+1},
\tag{2}
]
i.e.
[
\binom{2a}{a}\binom{4a+4}{2a+2}\binom{2c}{c}
=
\binom{2a+2}{a+1}\binom{4a}{2a}\binom{2c+2}{c+1}.
]

To prove (2), divide both sides by (B_{a+1}B_{2a}B_{c+1}); it suffices to show
[
\frac{B_a}{B_{a+1}}\cdot \frac{B_{2a+2}}{B_{2a}}\cdot \frac{B_c}{B_{c+1}}=1.
\tag{3}
]
Using (1),
[
\frac{B_a}{B_{a+1}}=\frac{a+1}{2(2a+1)},
\qquad
\frac{B_c}{B_{c+1}}=\frac{c+1}{2(2c+1)}.
]
Also,
[
\frac{B_{2a+2}}{B_{2a}}
=\frac{B_{2a+2}}{B_{2a+1}}\cdot \frac{B_{2a+1}}{B_{2a}}
=\frac{2a+2}{2(4a+3)}\cdot \frac{2a+1}{2(4a+1)}\Bigg)^{-1}
=\frac{2(4a+3)(4a+1)}{(a+1)(2a+1)}.
]
So the product of the first two factors in (3) is
[
\frac{a+1}{2(2a+1)}\cdot \frac{2(4a+3)(4a+1)}{(a+1)(2a+1)}
=\frac{(4a+3)(4a+1)}{(2a+1)^2}.
]
Thus (3) will hold provided
[
\frac{B_c}{B_{c+1}}=\frac{(2a+1)^2}{(4a+3)(4a+1)}.
]
But with (c=8a^2+8a+1),
[
c+1=8a^2+8a+2=2(2a+1)^2,\qquad
2c+1=16a^2+16a+3=(4a+3)(4a+1),
]
so indeed
[
\frac{B_c}{B_{c+1}}=\frac{c+1}{2(2c+1)}
=\frac{2(2a+1)^2}{2(4a+3)(4a+1)}
=\frac{(2a+1)^2}{(4a+3)(4a+1)}.
]
This completes the proof of (2).

So for every (a\ge2) we get a distinct solution with all indices distinct:
[
\boxed{\binom{2a}{a}\binom{4a+4}{2a+2}\binom{2(8a^2+8a+1)}{8a^2+8a+1}
=
\binom{2a+2}{a+1}\binom{4a}{2a}\binom{2(8a^2+8a+2)}{8a^2+8a+2}}
]
and hence there are **infinitely many** solutions.

Example (a=2):
[
\binom{4}{2}\binom{12}{6}\binom{98}{49}
=
\binom{6}{3}\binom{8}{4}\binom{100}{50},
]
i.e. (6\cdot924\cdot\binom{98}{49}=20\cdot70\cdot\binom{100}{50}), with indices ({2,6,49,3,4,50}) all distinct.
