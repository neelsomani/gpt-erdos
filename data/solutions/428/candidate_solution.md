For $r=2$, your $F(n)$ is the classical **multiplicative Sidon** problem [[nomath]](in the “distinct elements” version: only $a<b$)[[/nomath]]. The set of primes (\le n) shows (F(n)\ge \pi(n)), and Erdős proved that you can add a “second-order” number of composites, but only up to the same order.

### The known asymptotic scale for $F(n)$ (pairs)

What is known is that there exist absolute constants (c_1,c_2>0) such that, for all sufficiently large $n$,
[
\pi(n)+c_1\frac{n^{3/4}}{(\log n)^{3/2}}
\le
F(n)
\le
\pi(n)+c_2\frac{n^{3/4}}{(\log n)^{3/2}}.
]
This is explicitly summarized in Pach’s paper [[nomath]](reviewing Erdős’s construction and Erdős’s later improvement of the upper bound so that the $(\log n)^{-3/2}$ factor matches on both sides)[[/nomath]]. ([BME Computer Science Department][1])
The same “(\Theta(n^{3/4}(\log n)^{-3/2})) gap above (\pi(n))” statement is also recalled in modern literature. ([Springer][2])

### Is there a constant $c$ with a full second-term asymptotic?

I did **not** find any source proving the existence of a limiting constant $c$ in
[
F(n)=\pi(n)+\bigl(c+o(1)\bigr)\frac{n^{3/4}}{(\log n)^{3/2}},
]
and the standard state-of-the-art statement remains “matching upper/lower bounds up to an unspecified constant factor” [[nomath]](i.e. the inequalities with $c_1,c_2$ above)[[/nomath]]. ([BME Computer Science Department][1])
So, as far as the literature I located indicates, the existence/value of such a constant $c$ is **open** (it is posed explicitly as an Erdős-type problem). ([Erdős Problems][3])

---

## The $r$-fold distinct-products question

You ask: if (A\subseteq{1,\dots,n}) has the property that **all products**
$
a_1a_2\cdots a_r \quad (a_1<\cdots<a_r)
$
are distinct, is it true that
$
|A|\le \pi(n)+O(n^{\frac{r+1}{2r}})
]?

### What one can say quickly

For any fixed (r\ge 3), this condition is *strictly stronger* than being a multiplicative Sidon set (pairwise distinct products), once (|A|) is even moderately large: if $ab=cd$ with (a,b,c,d\in A) distinct, then multiplying both sides by any additional $r-2$ distinct elements of $A$ produces a collision of $r$-fold products. So [[nomath]](for $|A|\ge r+2$)[[/nomath]] your hypothesis implies the $r=2$ hypothesis, and therefore yields the (weaker) bound
[
|A|\le \pi(n)+O\left(\frac{n^{3/4}}{(\log n)^{3/2}}\right),
]
via the known $r=2$ theory. ([BME Computer Science Department][1])

That does **not** reach the conjectured exponent $(r+1)/(2r)$ for (r\ge 3), since $(r+1)/(2r)<3/4$.

### Why your exponent $(r+1)/(2r)$ is a very natural guess

There is a well-known graph-theoretic model behind these problems: if you look at sets built from products $pq$ [[nomath]](with $p$ in one prime set and $q$ in another)[[/nomath]], then controlling uniqueness of $h$-fold multiplicative representations is closely related to forbidding **short even cycles** in an associated bipartite graph; Jing–Mudgal explicitly point out that, for such “product-structured” sets, the problem is tied to finding large bipartite graphs with **no cycles of length (\le 2h)** and hence to extremal quantities like (\mathrm{ex}(|P|,|Q|,C_{2h})). ([Springer][4])
Combining that heuristic with the classical extremal-graph exponents for even cycles suggests that the “extra” elements beyond primes should scale like (n^{(r+1)/(2r)}) up to log factors [[nomath]](indeed for $r=2$ this is exactly how the $\tfrac{n^{3/4}}{(\log n)^{3/2}}$ term arises)[[/nomath]]. ([BME Computer Science Department][1])

### Is the stated bound known for general $r$?

I did **not** locate a proof in the literature that establishes your specific bound
[
|A|\le \pi(n)+O!\left(n^{\frac{r+1}{2r}}\right)
]
for the “all $r$-subset products distinct” condition, for general fixed $r$. What I did find are results for *other* natural generalisations [[nomath]](e.g. forbidding only solutions with $2r$ distinct variables, which is weaker than your requirement)[[/nomath]], where the main term and error terms can look different (Pach’s “generalized multiplicative Sidon sets” paper is an example of that different-but-related direction). ([BME Computer Science Department][1])

So the best accurate summary I can give is:

* For $r=2$: the order (n^{3/4}(\log n)^{-3/2}) is correct and sharp up to constants, but the existence of an asymptotic constant $c$ is not currently settled. ([BME Computer Science Department][1])
* For fixed (r\ge 3): the exponent $(r+1)/(2r)$ is strongly motivated by the cycle-free bipartite graph heuristic, but I have not found a definitive theorem confirming your precise (\pi(n)+O(n^{(r+1)/(2r)})) bound for the *full* “all $r$-subset products distinct” property. ([Springer][4])

If you want, I can also spell out the standard reduction from “distinct $r$-fold products of semiprimes $pq$” to “no even cycles up to length $2r$” in the corresponding bipartite graph, since that’s the clearest route to why $(r+1)/(2r)$ is the right exponent to expect.

[1]: https://cs.bme.hu/~ppp/publications/Generalized_multiplicative.pdf "https://cs.bme.hu/~ppp/publications/Generalized_multiplicative.pdf"
[2]: https://link.springer.com/content/pdf/10.1007/s00208-024-02932-7.pdf "https://link.springer.com/content/pdf/10.1007/s00208-024-02932-7.pdf"
[3]: https://www.erdosproblems.com/forum/thread/425?utm_source=chatgpt.com "Erdős Problem #425 - Discussion thread"
[4]: https://link.springer.com/article/10.1007/s00208-024-02932-7 "https://link.springer.com/article/10.1007/s00208-024-02932-7"
