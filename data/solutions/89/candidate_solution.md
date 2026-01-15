We do not know.

This is basically the remaining gap in the **Erdős distinct distances problem**. Erdős showed that a (\sqrt n \times \sqrt n) integer grid can have only about
[
\Theta!\left(\frac{n}{\sqrt{\log n}}\right)
]
distinct distances, so you cannot hope for a general lower bound bigger than this (up to constants). ([MIT OpenCourseWare][1])

But the **best general theorem** we have for *every* set of (n) planar points is still weaker: Guth and Katz (2015) proved
[
\Omega!\left(\frac{n}{\log n}\right)
]
distinct distances for any (n)-point set in (\mathbb{R}^2). ([Annals of Mathematics][2])

So at the moment we only know (for the worst case over all (n)-point sets)
[
c,\frac{n}{\log n}\ \le\ g(n)\ \le\ C,\frac{n}{\sqrt{\log n}},
]
and whether one can always get (\gg \frac{n}{\sqrt{\log n}}) is still open. ([combinatorics.org][3])

[1]: https://ocw.mit.edu/courses/18-225-graph-theory-and-additive-combinatorics-fall-2023/mit18_225_f23_lec_full.pdf?utm_source=chatgpt.com "Graph Theory and Additive Combinatorics"
[2]: https://annals.math.princeton.edu/2015/181-1/p02?utm_source=chatgpt.com "On the Erdős distinct distances problem in the plane"
[3]: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v28i4p33/pdf/?utm_source=chatgpt.com "On Bipartite Distinct Distances in the Plane"
