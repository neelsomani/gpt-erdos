Let (f(n)) be the **maximum** possible number of pairs ({p,q}) with (|p-q|=1), where (p_1,\dots,p_n) are the vertices of a convex (n)-gon.

Your claim “(f(n)=O(n))” is **not known to be true or false**. It is a famous open problem of Erdős–Moser: they conjectured that (f(n)=\Theta(n)), i.e. a linear bound should hold, but no accepted proof is known. 

What *is* known is:

* **Best known general upper bound:**
  [
  f(n)\le n\log_2 n+4n,
  ]
  so in particular (f(n)=O(n\log n)). 

* **Best known general lower bound:** there are convex (n)-gons with at least
  [
  f(n)\ge 2n-7
  ]
  unit-distance pairs. 

* **A special case where linear is proved:** if the convex (n)-gon is **centrally symmetric**, then
  [
  f_{\text{sym}}(n)\le 2n-3.
  ]
  ([California State University, Northridge][1])

So the correct “safe” statement right now is:

[
\text{For vertices of a convex (n)-gon, the number of unit-distance pairs is } O(n\log n),
]
and improving this to (O(n)) is still open. 

[1]: https://www.csun.edu/~sf70713/publications/unit.pdf "unit.dvi"
