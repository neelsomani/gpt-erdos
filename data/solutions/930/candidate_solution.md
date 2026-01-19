Assuming the intervals are intervals of **positive** integers [[nomath]](if an interval is allowed to contain $0$, the product is $0$, which *is* a perfect power)[[/nomath]], then **this is currently an open problem**. It appears as **Erdős Problem #930**. ([Erdős Problems][1])

What *is* known:

* **$r=1$**: Yes. Erdős–Selfridge proved that the product of (k\ge 2) consecutive integers is **never** a perfect power, so you can take $k=2$ for $r=1$. ([Project Euclid][2])

* **(r\ge 2)**: The question is **unsolved in general**, and the first genuinely open case is already $r=2$. ([Erdős Problems][1])

* There are many **infinite families of counterexamples for small block lengths**, showing you can’t hope for a statement with a fixed “small” $k$ once you have more than one block:

  * For example, with **two blocks of length $3$** there are infinitely many perfect squares (hence perfect powers): Bauer–Bennett note that taking $[n,n+2]$ and $[2n,2n+2]$ works whenever ((n+2)(2n+1)) is a square, which happens infinitely often. 
    [[nomath]](E.g. $n=73$ gives $(73\cdot74\cdot75)(146\cdot147\cdot148)=1134420^2$.)[[/nomath]]
  * With **three or more blocks**, there are also infinite square-producing constructions even when every block has length $4$. ([Personal Math UBC][3])
  * With **(r\ge 5)**, Bennett–van Luijk construct infinitely many examples where **$r$ disjoint blocks of length $5$** have square product. ([Personal Math UBC][4])

* More broadly, Skálba showed that **products of disjoint blocks can be perfect powers** even when the block length is fixed (\ell\ge 4), provided you allow *enough* blocks; he gives quantitative estimates for how many solutions exist below a bound. ([EuDML][5])

So the current situation is:

* The “one interval” case is completely settled (Erdős–Selfridge).
* For multiple disjoint intervals, perfect powers definitely **do occur** for small lengths / many blocks.
* But the exact statement you asked—**for each fixed $r$, does there exist a length threshold $k(r)$ beyond which no perfect power is possible?**—remains **open** as of now. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/930 "https://www.erdosproblems.com/930"
[2]: https://projecteuclid.org/journals/illinois-journal-of-mathematics/volume-19/issue-2/The-product-of-consecutive-integers-is-never-a-power/10.1215/ijm/1256050816.full "https://projecteuclid.org/journals/illinois-journal-of-mathematics/volume-19/issue-2/The-product-of-consecutive-integers-is-never-a-power/10.1215/ijm/1256050816.full"
[3]: https://personal.math.ubc.ca/~bennett/Erdos-Graham.pdf "https://personal.math.ubc.ca/~bennett/Erdos-Graham.pdf"
[4]: https://personal.math.ubc.ca/~bennett/BeVL-Oct18-2011b.pdf "https://personal.math.ubc.ca/~bennett/BeVL-Oct18-2011b.pdf"
[5]: https://eudml.org/doc/284443 "https://eudml.org/doc/284443"
