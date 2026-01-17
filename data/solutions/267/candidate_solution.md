This is an Erdős–Graham problem (1980), and as stated with only the hypothesis
(\displaystyle \frac{n_{k+1}}{n_k}\ge c>1), it is **not known in full generality**.

What is known (and essentially the current “boundary” of the theory) is:

* **If (c>2)**, then the sum is not only irrational but **transcendental**. This is proved by Khoa D. Nguyen (2020) via a Subspace Theorem argument [[nomath]](in fact in a more general setting allowing $F_{n_k}$ or $L_{n_k}$ in the denominators)[[/nomath]]. 

* **The transcendence threshold (c>2) is sharp**, because for the lacunary sequence (n_k=2^k) [[nomath]](which has ratio exactly $2$)[[/nomath]] there is the classical “Millin series” identity
  [
  \sum_{k=0}^\infty \frac1{F_{2^k}}=\frac{7-\sqrt5}{2},
  ]
  which is **algebraic** (hence not transcendental), though still irrational. 

* The Erdős Problems archive currently lists the original question as **OPEN**, with the note that it “remains open” in the range **(1<c<2)** [[nomath]](and references work of Badea for $c\ge 2$)[[/nomath]]. ([Erdős Problems][1])

### Why (c>2) is “easy” for irrationality (proof sketch)

Nguyen’s paper points out the simple irrationality mechanism for (c>2): if (n_{k+1}/n_k\ge c>2), then the product of the first (N) denominators is negligible compared to the next Fibonacci number,
[
F_{n_1}\cdots F_{n_N} = o!\left(F_{n_{N+1}}\right).
]
From this, one can combine:

* the fact that the (N)-th partial sum is a rational with denominator dividing (F_{n_1}\cdots F_{n_N}), and
* the tail is (\ll 1/F_{n_{N+1}}),

to contradict the lower bound on the distance between two distinct rationals with a given denominator. 

### Bottom line

* **Yes (in fact transcendental)** if (c>2). 
* **At (c=2)** there are explicit closed forms (algebraic irrational values) for some sequences, e.g. (n_k=2^k). 
* **For (1<c<2)**: no proof is known either way in general; it remains an open Erdős–Graham question. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/forum/thread/267 "

    Erdős Problem #267 - Discussion thread

"
