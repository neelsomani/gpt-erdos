For (G\sim G_{n,1/2}) one has
[
\chi(G)\sim \frac{n}{2\log_2 n}
\qquad\text{and}\qquad
\zeta(G)\sim \frac{n}{2\log_2 n}
]
with high probability [[nomath]](so $\chi/\zeta\to 1$)[[/nomath]]. 

The question whether the **difference** (\chi(G)-\zeta(G)\to\infty) w.h.p. (this is exactly the Erdős–Gimbel problem) has seen major recent progress:

### What is known now (as of the latest papers available)

**Heckel (arXiv v2, Feb 2025)** proves a *strong* lower bound on the gap for “most” values of $n$. Let
[
\alpha_0(n)=2\log_2 n-2\log_2\log_2 n+2\log_2(e/2)+1,\quad \alpha=\lfloor \alpha_0\rfloor,
]
and
[
\mu_\alpha=\binom{n}{\alpha},2^{-\binom{\alpha}{2}},
]
the expected number of independent sets of size (\alpha) [[nomath]](equivalently, cliques of size $\alpha$)[[/nomath]]. If for some fixed (\varepsilon>0),
[
n^{0.05+\varepsilon}\le \mu_\alpha \le n^{1-\varepsilon},
]
then with high probability,
[
\chi(G)-\zeta(G) ;>; n^{1-\varepsilon}.
]


Moreover, she shows that this condition on $n$ holds for a set of integers $n$ of “about 95% density” [[nomath]](more precisely, the applicable fraction fluctuates between about $0.9413$ and $0.9578$)[[/nomath]]. 

So: **for roughly 95% of all $n$, the answer is “yes” (and in fact the gap is polynomially large).** 

### What is *not* fully settled

The above does **not** yet prove the statement for **all** $n$ [[nomath]](i.e., it does not yet establish $\chi(G)-\zeta(G)\to\infty$ w.h.p. along the full sequence $n=1,2,3,\dots$)[[/nomath]]. Heckel explicitly discusses the remaining (\sim 5%) of values of $n$ and **conjectures** the theorem should hold for all $n$, with the “true” order expected to be
[
\chi(G)-\zeta(G) \asymp \frac{n}{(\log n)^3}
\quad\text{w.h.p.}
]


### Related evidence: the gap is definitely not bounded

Independently, Heckel (2024 note) and Steiner observed a connection to non-concentration of (\chi(G_{n,1/2})). In particular, it is known that (\chi(G)-\zeta(G)) is **not** bounded w.h.p., and more quantitatively any function $f(n)$ that upper-bounds (\chi(G)-\zeta(G)) w.h.p. must be at least (n^{1/2-o(1)}) along an infinite subsequence [[nomath]](in Heckel’s note: $\gtrsim \sqrt{n\log\log n}/\log^3 n$ along some $n^*$)[[/nomath]]. 

---

### Bottom line

* **Yes for a density (\approx 95%) of integers $n$**: (\chi(G)-\zeta(G)) not only diverges, it is (\ge n^{1-\varepsilon}) w.h.p. for any fixed (\varepsilon>0) [[nomath]](under the stated condition on $n$)[[/nomath]]. 
* **For the remaining (\approx 5%) of $n$**, the full “w.h.p. as (n\to\infty)” statement (in the usual random-graph sense) is **not yet proved** as far as the current literature indicates; it remains open but is conjectured true, with predicted order (\Theta(n/(\log n)^3)). 
