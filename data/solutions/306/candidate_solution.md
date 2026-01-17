A necessary condition is exactly the one you assumed: if
[
\frac{a}{b}=\sum_{i=1}^k\frac1{n_i}
\quad\text{with }n_i=p_iq_i\text{ (distinct primes),}
]
then each (n_i) is squarefree, hence (\operatorname{lcm}(n_1,\dots,n_k)) is squarefree, and after reduction the denominator of the sum must also be squarefree. So $b$ must be squarefree.

The converse [[nomath]](that **every** $\tfrac{a}{b}$ with $b$ squarefree admits such a representation)[[/nomath]] is **open**. In fact, your question is stated verbatim as an open Erdős problem (Erdős–Graham, 1980) and is listed as open as of today. ([Erdős Problems][1])

To put this in context:

* Even the special case (b=1) (i.e. **integers**) is not known in general for “two distinct prime factors.” In the paper of Butler–Erdős–Graham they explicitly *conjecture* the analogous statement for (\omega=2) (two distinct prime factors), while proving the (\omega=3) case. ([SunSITE][2])
* What *is* known is that if you relax “two primes” to “three distinct primes,” then **every natural number** has such an Egyptian fraction expansion (Butler–Erdős–Graham, 2015). ([SunSITE][2])

There are, however, explicit examples showing the two-prime-factor condition is sometimes achievable. For instance, $1$ has a representation as a sum of $48$ reciprocals of products of two distinct primes; one such set of denominators is:
[
6,10,14,15,21,22,26,33,34,35,38,39,
]
[
46,51,55,57,58,62,65,69,77,82,85,86,
]
[
87,91,93,95,115,119,123,133,155,187,203,209,
]
[
215,221,247,265,287,299,319,323,391,689,731,901,
]
and indeed (\sum 1/n_i = 1) (after ordering increasingly). ([SunSITE][2])

So the best current answer to your “for all (\tfrac{a}{b}) with $b$ squarefree?” is: **unknown/open**.

[1]: https://www.erdosproblems.com/forum/thread/306 "

    Erdős Problem #306 - Discussion thread

"
[2]: https://sunsite3.icm.edu.pl/packages/EMIS/journals/INTEGERS/papers/p51/p51.pdf "p51"
