This property is studied in the literature under the name **Type 3 irrationality sequence** (Erdős–Graham): an increasing integer sequence ((a_n)) such that for **every bounded** integer sequence ((b_n)) with (b_n\neq 0) and (a_n+b_n\neq 0) for all $n$, the “perturbed” Ahmes series
[
\sum_{n=1}^\infty \frac{1}{a_n+b_n}
]
is **irrational**. ([arXiv][1])

### 1) (a_n=2^n): **not** an example

This case is now known to fail. Kovač and Tao proved that **no** strictly increasing integer sequence with *essentially exponential growth* [[nomath]](more precisely, with $\limsup a_{n+1}/a_n<\infty$)[[/nomath]] can have the Type 3 property; in particular this rules out (a_n=2^n). ([arXiv][1])

Even more concretely, they show [[nomath]](specializing their construction to $a_n=2^n$)[[/nomath]] that there exists a bounded choice of (b_n) with values in $\\{1,2,3,4,5\\}$ such that
[
\sum_{n=1}^\infty \frac{1}{2^n+b_n}=0.75=\frac34\in\mathbb{Q},
]
so (2^n) definitely does **not** satisfy your condition. ([arXiv][1])

### 2) (a_n=n!): **open / unknown**

For (a_n=n!), the question is still **open**: there is no known proof (as of the latest updates I could find) that $n!$ does or does not have the Type 3 property. The same Kovač–Tao paper explicitly notes that the factorial variant is “probably more difficult,” and in particular points out that even the special case
[
\sum_{n=2}^\infty \frac{1}{n!-1}
]
[[nomath]](which corresponds to the bounded perturbation $b_n\equiv -1$)[[/nomath]] is itself an **open** irrationality problem. ([arXiv][1])

So at present:

* (a_n=2^n): **No**, not an example [[nomath]](there exists bounded $(b_n)$ making the sum rational)[[/nomath]]. ([arXiv][1])
* (a_n=n!): **Not known** (still an open problem). ([arXiv][1])

[1]: https://arxiv.org/pdf/2406.17593 "On several irrationality problems for Ahmes series"
