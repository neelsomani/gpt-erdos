This question is *exactly* a conjecture of Carl Pomerance from his work on the “prime number graph,” and as far as the published literature I can locate goes, it is still **open**.

### What is known

Write
$
M_n := f(n)-2p_n = \min_{1\le i<n}\\(p_{n+i}+p_{n-i}-2p_n\\).
$
Then your question is whether (\limsup_{n\to\infty} M_n = \infty).

* Pomerance **conjectured** that this (\limsup) is infinite. ([OEIS][1])
* What he **proved** is the weaker unconditional lower bound
  $
  \limsup_{n\to\infty} (f(n)-2p_n)\ \ge\ 2,
  $
  i.e. $M_n\ge 2$ for infinitely many $n$. ([OEIS][1])

So at present the best rigorously established statement is that the limsup is at least $2$, but **no proof is known** that it is unbounded.

### Geometric / structural interpretation

The condition (M_n>0) is equivalent to
$
2p_n < p_{n-i}+p_{n+i}\quad\text{for all }1\le i<n,
$
and primes (p_n) satisfying this are called **midpoint convex primes** in later work on the convex hull of the prime number graph. 
In that language, your question asks whether the “midpoint convexity margin” (M_n) can be arbitrarily large.

### Computational evidence

McNew (in work on the convex hull of the prime number graph) explicitly introduces the same quantity
$
M_n=\min_{1\le i<n}(p_{n+i}+p_{n-i})-2p_n
$
and reports computations of its distribution for (n<1.6\times 10^8). He remarks that, **based on the data**, it “appears likely that (M_n) can be arbitrarily large,” but does not claim a proof. 

### Bottom line

* **Status:** Open; it is recorded as a conjecture of Pomerance (Erdős Problems #454 / OEIS A389676). ([OEIS][1])
* **Best unconditional result:** (\limsup_{n}(f(n)-2p_n)\ge 2) (Pomerance). ([OEIS][1])
* **Heuristic/numerical evidence:** suggests unboundedness, but no proof known. 

If you want, I can also sketch how Pomerance’s convex-hull argument yields (\limsup\ge 2), and why pushing it to (\infty) seems to require substantially finer control of local prime-gap asymmetries.

[1]: https://oeis.org/A389676 "A389676 - OEIS"
