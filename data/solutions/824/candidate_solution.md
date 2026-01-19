This is **open**.

It is recorded as an Erdős problem (Erdős Problem #824): given
$
h(x)=|\\{(a,b): 1\le a<b<x,\ (a,b)=1,\ \sigma(a)=\sigma(b)\\}|,
$
Erdős asked whether one has the near–quadratic lower bound (h(x) > x^{2-o(1)}). ([Erdős Problems][1])

What *is* known is much weaker but still nontrivial:

* Erdős proved that (\limsup_{x\to\infty} h(x)/x = \infty), i.e. $h(x)$ is arbitrarily large compared to $x$ along some sequence of $x$. ([Erdős Problems][1])
* Pollack and Pomerance later gave a complete proof that in fact
  [
  \frac{h(x)}{x}\to\infty,
  ]
  so $h(x)$ grows **superlinearly** (by an unbounded factor). ([Erdős Problems][1])

So we know $h(x)$ is “quite large” in the sense (h(x)\gg x\cdot g(x)) with (g(x)\to\infty), but this is still extremely far from (x^{2-o(1)}).

There is also strong structural evidence that coprime collisions (\sigma(a)=\sigma(b)) are not ubiquitous:

* Pollack proved that for **asymptotically 100% of (\sigma)-values $v$**, *all* integers $n$ with (\sigma(n)=v) share the **same largest prime factor**. ([Pollack][2])
  In particular, for such $v$, there cannot be any coprime pair (a\ne b) with (\sigma(a)=\sigma(b)=v), since that common largest prime would divide both.
* He also quantified the exceptional set: the number of “exceptional” (\sigma)-values (v\le x) (those having two preimages with different largest prime factor) is at most
  [
  \frac{V_\sigma(x)}{(\log_2 x)^{1/2+o(1)}},
  ]
  where (V_\sigma(x)) counts distinct (\sigma)-values (\le x). ([Pollack][2])

This doesn’t settle the growth of $h(x)$ (exceptional values could, in principle, have large fibers), but it shows a major obstacle: **most (\sigma)-values contribute zero coprime pairs**, so any near-quadratic lower bound would have to come from a relatively sparse set of exceptional (\sigma)-values.

So: **no proof or disproof is currently known** for (h(x) > x^{2-o(1)}); the best unconditional results are the superlinear growth (h(x)/x\to\infty) together with structural theorems indicating that coprime collisions are forced into a sparse exceptional subset of (\sigma)-values. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/latex/824 "https://www.erdosproblems.com/latex/824"
[2]: https://pollack.uga.edu/preimages-maier3.pdf "https://pollack.uga.edu/preimages-maier3.pdf"
