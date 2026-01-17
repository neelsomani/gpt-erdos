This is **not known** (as of January 16, 2026). It is an open Erdős–Graham problem.

A useful rephrasing of the second condition is:

* An integer (m>1) “has a common factor with every term” iff for every $n$, (\gcd(m,a_n)>1).
* Writing (m=\prod_{p\in S}p), this means **every** term (a_n) is divisible by **at least one** prime in the **finite** set $S$.
* So the problem is asking for an all-composite Lucas/Fibonacci-type sequence whose terms **cannot** be “covered” by any **finite** set of primes.

It has been known since Graham (1964) that there are Lucas sequences with **all terms composite**, but the standard constructions use **covering systems** (a finite set of congruences and primes that force each index $n$ to land on a term divisible by one of those primes). In such a construction, if $S$ is the finite set of primes used, then (m=\prod_{p\in S}p) automatically shares a factor with every term, so these examples do **not** satisfy the “no such $m$” requirement. ([Erdős Problems][1])

There is, however, a **conjectural** example due to Ismailescu and Son (2014). They construct a specific Lucas sequence ((x_n)) with
[
x_0=p^2+q^2,\qquad x_1=2pq+q^2,\qquad x_{n}=x_{n-1}+x_{n-2}\ (n\ge2),
]
with (p=1) and a particular 129-digit integer (q), and prove:

* All odd-indexed terms are composite because they factor as
  [
  x_{2n+1}=(pF_n+qF_{n+1})(pL_n+qL_{n+1}),
  ]
  so each odd term is a nontrivial product. 
* All even-indexed terms are composite because they arrange a **finite covering** that guarantees each (x_{2n}) is divisible by one of 30 specified primes. 

What they **cannot** prove is exactly what your question asks: that there is **no** integer $m$ that shares a factor with **every** term (equivalently, that the odd-indexed terms are not also “covered” by some finite prime set). They give computational evidence suggesting no such finite covering exists for the whole sequence, but it remains unproved. 

So the current state is:

* **All-composite Lucas sequences exist** (many, via covering systems),
* but **whether one can do this without any finite prime “cover”**—i.e. satisfying your “no integer shares a factor with every term” condition—remains **open**. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/276 "
  
    Erdős Problem #276
  
"
