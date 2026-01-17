This is **not known** (at least according to the standard references and the more recent papers/surveys I can find). What *is* known is much weaker.

Write $N(n)$ for the maximum size of a set of MOLS of order $n$ [[nomath]](this is your $f(n)$)[[/nomath]]. One always has the trivial upper bound
[
N(n)\le n-1\qquad(n>1),
]
and equality holds for prime powers $q$ (via the finite field construction), i.e. $N(q)=q-1$. 
So along the subsequence of prime powers we certainly have (N(n)\asymp n), hence (N(n)\gg n^{1/2}) there. The issue is whether one can guarantee (\gg \sqrt n) **uniformly for all** large $n$.

The **best general asymptotic lower bounds known** are of the form (N(n)\ge n^{c}) for a small constant (c>0), not anywhere near $1/2$. For example:

* Chowla–Erdős–Straus (1960) proved (N(n)\to\infty) and gave an explicit power bound, in particular (N(n) > \tfrac14 n^{1/91}) for all sufficiently large (n). 
* Wilson (1974) improved this substantially [[nomath]](one formulation in his paper gives $N(n)\ge n^{1/17}-2$ for large $n$)[[/nomath]]. ([DCS][1])
* Beth (1983), using a number sieve plus recursive constructions, improved the exponent further to
  [
  N(n)\ge n^{1/14.8}
  ]
  for all sufficiently large $n$ [[nomath]](and refinements note $14.8$ can be replaced by $14.7994$)[[/nomath]]. 

So at present the strongest generally cited guarantee is roughly
[
N(n)\ \ge\ n^{0.0675\ldots}
\quad\text{for all large }n,
]
and a bound (N(n)\gg n^{1/2}) would be a dramatic strengthening beyond what’s currently proved. 

One extra historical remark: Chowla–Erdős–Straus already observed that the particular recursion they were exploiting (their “Theorem A”) cannot on its own yield an exponent as large as $1/2$; that’s a limitation of that *method*, not a proof that (N(n)\not\gg \sqrt n). 

[1]: https://www.dcs.gla.ac.uk/~pat/cpM/jchoco/latinSquares/papers/dm9.pdf "https://www.dcs.gla.ac.uk/~pat/cpM/jchoco/latinSquares/papers/dm9.pdf"
