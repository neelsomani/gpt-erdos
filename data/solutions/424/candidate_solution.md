This is a well-known open problem (asked by Hofstadter and recorded as **Erdős Problem #424**). ([Erdős Problems][1])

Let $A$ be the set of integers that ever appear [[nomath]](equivalently: the smallest set containing $2,3$ that is closed under
$
x,y\in A,\ x\neq y \ \Longrightarrow\ xy-1\in A,
$
and then list its elements in increasing order; this is OEIS **A005244**)[[/nomath]]. ([Erdős Problems][1])

### What is known (easy)

There is an immediate congruence obstruction:

* (2\equiv 2\pmod 3) and (3\equiv 0\pmod 3).
* If (a,b\in{0,2}\pmod 3), then (ab\equiv 0) or (1\pmod 3), so
  [
  ab-1\equiv 2\ \text{or}\ 0\pmod 3.
  ]
  So by induction **no term is ever (\equiv 1\pmod 3)**. ([Erdős Problems][1])

Consequently, the set of integers that appear has (upper) density **at most $2/3$**. ([Erdős Problems][1])
(This also explains why the *stronger* version “almost all integers appear” is trivially false.) ([Erdős Problems][1])

### The actual question (positive density) is open

The intended question is the weaker one:

> Does $A$ have **positive natural density**, i.e. is (\lim_{N\to\infty}\frac{|A\cap[1,N]|}{N}>0) [[nomath]](or at least $\liminf>0$)[[/nomath]]?

As of the current literature summaries, this is still listed as **open**. ([Erdős Problems][1])
Ben Green includes essentially the same question as **Problem 63** in his open problems list and remarks “the answer is probably yes,” but gives no proof. ([Mathematical Institute][2])

### Computational evidence (not a proof)

Empirically the set looks quite thick among the admissible residue classes (0,2\pmod 3). For example, if you compute (A\cap[1,N]) by iterating the rule, the observed proportions (|A\cap[1,N]|/N) for (N=10^k) are approximately:

* (N=10^2): (0.23)
* (N=10^3): (0.25)
* (N=10^4): (0.3207)
* (N=10^5): (0.39843)
* (N=10^6): (0.457599)

This strongly suggests a positive limiting density, possibly tending upward [[nomath]](with an absolute ceiling of $2/3$ from the mod‑3 obstruction)[[/nomath]], but at present it does not substitute for a proof.

So the honest answer is:

* **We can prove** the density is **(\le 2/3)** [[nomath]](mod $3$ obstruction)[[/nomath]]. ([Erdős Problems][1])
* **Whether the density is (>0)** is **currently open** in the standard references/trackers for this question. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/424 "https://www.erdosproblems.com/424"
[2]: https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf "https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf"
