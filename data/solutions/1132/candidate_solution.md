Let
[
L_n(x)=\sum_{k=1}^n |l_k(x)|
]
be the **Lebesgue function** for Lagrange interpolation at the nodes (x_1,\dots,x_n), and let
[
\Lambda_n:=\max_{x\in[-1,1]}L_n(x)
]
be the **Lebesgue constant**.

A foundational fact is that (\Lambda_n) must grow at least logarithmically for *every* choice of nodes: Erdős proved
[
\Lambda_n \ge \frac{2}{\pi}\log n - C
]
for an absolute constant $C$, and this is sharp in order [[nomath]](Chebyshev nodes have $\Lambda_n\le \frac{2}{\pi}\log n + O(1)$)[[/nomath]]. 

With that context:

## 1) Existence of a single $x$ with (L_n(x)\ge \frac{2}{\pi}\log n - O(1)) infinitely often

This is **open in general**.

In fact, Erdős already singled out essentially your question in 1961: after discussing Bernstein’s local lower bounds, he wrote that he had claimed a related result, and then stated that the stronger fixed-point statement “is quite possibly true” but that he was “very far” from proving it. 

So, as of the material I can locate (and consistent with how the problem is currently recorded), there is **no known general proof** that for *every* infinite sequence ((x_k)\subset[-1,1]) one can find a fixed (x\in(-1,1)) such that
[
L_n(x) > \frac{2}{\pi}\log n - O(1)
\quad\text{for infinitely many }n.
]

### What *is* known in this direction (weaker)

A theorem of Bernstein (as summarized in modern compilations of Erdős problems) implies that the set of points $x$ for which
[
\limsup_{n\to\infty}\frac{L_n(x)}{\log n}\ge \frac{2}{\pi}
]
is **everywhere dense** in $(-1,1)$. ([Erdős Problems][1])
This gives, in particular, existence of some $x$ with the **multiplicative** (\frac{2}{\pi}) limsup bound, but it does **not** automatically upgrade to the **additive** form (\frac{2}{\pi}\log n - O(1)) along infinitely many $n$.

## 2) Almost-everywhere statement (\displaystyle \limsup_{n\to\infty}\frac{L_n(x)}{\log n}\ge \frac{2}{\pi})

This is also **open** (it is listed as Erdős Problem #1132 in one standard online registry), with Bernstein’s result giving denseness but not measure information. ([Erdős Problems][1])

A key point is that “dense” can still mean “measure zero” (like the rationals), so Bernstein’s density result does not settle the “almost all $x$” question.

### Best partial “large set” results I know [[nomath]](but not $\frac{2}{\pi}$, and not a.e. limsup)[[/nomath]]

Erdős–Vértesi proved a strong *per-$n$* statement: for any fixed (\varepsilon>0), there is (\eta(\varepsilon)>0) such that for all sufficiently large $n$ one can remove an exceptional set (H_n) of measure (<\varepsilon) so that
[
L_n(x)\ge \eta(\varepsilon),\log n\qquad\text{for all }x\in(-1,1)\setminus H_n.
]
So, for each fixed $n$, (L_n(x)) is (\gtrsim \log n) on “most” $x$, but this does **not** force any given $x$ to see the sharp (\frac{2}{\pi}) coefficient infinitely often, nor does it identify the coefficient (\frac{2}{\pi}). ([Renyi Institute][2])

## Bottom line

* The **global** lower bound (\max_x L_n(x)\ge \frac{2}{\pi}\log n - O(1)) is known and sharp. 
* Your **fixed $x$, infinitely many $n$** additive form is **not known in full generality** and appears already in Erdős’s 1961 discussion as an open challenge. 
* The **almost-everywhere** limsup (\ge \frac{2}{\pi}) is also **open**, though the limsup-(\ge \frac{2}{\pi}) set is known to be **dense** (Bernstein). ([Erdős Problems][1])

If you want, I can also sketch how Bernstein’s “every interval contains points with large limsup” translates into the statement “the (\limsup\ge 2/\pi) set is dense [[nomath]](indeed a dense $G_\delta$)[[/nomath]]”, and why that still leaves open the measure (“almost all”) question.

[1]: https://www.erdosproblems.com/1132 "https://www.erdosproblems.com/1132"
[2]: https://users.renyi.hu/~p_erdos/1981-18.pdf "https://users.renyi.hu/~p_erdos/1981-18.pdf"
