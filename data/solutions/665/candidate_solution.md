Yes — as stated, the problem is *trivial* because you are allowed to take $m=1$.

For every $n$, let
[
m=1,\qquad A_1={1,2,\dots,n}.
]
Then:

* (|A_1|=n). For any fixed constant (c>0) (e.g. (c=1)), we have
  [
  n > \sqrt{n}-c
  ]
  for all (n\ge 1) [[nomath]](since $n\ge \sqrt n$, and the inequality is strict once $c>0$)[[/nomath]].
* The condition (|A_i\cap A_j|\le 1) for (i\ne j) is **vacuously true** because there are no distinct indices when $m=1$.
* Every pair ({x,y}\subseteq{1,\dots,n}) is contained in (A_1) by construction.

So **any** constant (c>0) works [[nomath]](for example $c=1$)[[/nomath]].
[[nomath]](If you intended $n\ge 2$, then even $c=0$ works with the same construction.)[[/nomath]]

---

If you meant an additional restriction such as “(|A_i|) is *also* at most (\sqrt n + O(1))” or “(m\ge 2)”, then the question becomes a much more interesting design-theory / clique-decomposition problem (related to projective planes and pairwise balanced designs).
