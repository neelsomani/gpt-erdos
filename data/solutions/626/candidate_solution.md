### 1) Fixed chromatic number $k$: the function (g_k(n))

For fixed (k\ge 4), (g_k(n)) grows on the order of (\log n), but the *constant* in front of (\log n) is not known sharply.

A standard reduction is: any $k$-chromatic graph contains a $k$-**critical** subgraph, and a $k$-critical graph has minimum degree at least $k-1$. Once you have minimum degree $k-1$, a Moore–type BFS/tree growth argument forces a short cycle, giving an upper bound of the form
[
g_k(n)\ \le\ \frac{2}{\log(k-2)}\log n + O(1).
]
Erdős proved [[nomath]](with an explicit “$+1$” term)[[/nomath]] the bound
[
g_k(n)\ \le\ \frac{2}{\log(k-2)}\log n + 1.
]
([Erdős Problems][1])

On the other hand, Kostochka proved a logarithmic lower bound
[
g_k(n)\ \ge\ \frac{1}{4\log k}\log n.
]
([Erdős Problems][1])

So we know
[
\frac{1}{4\log k}\ \le\ \liminf_{n\to\infty}\frac{g_k(n)}{\log n}
\ \le\
\limsup_{n\to\infty}\frac{g_k(n)}{\log n}
\ \le\ \frac{2}{\log(k-2)}.
]
([Erdős Problems][1])

**Does (\displaystyle \lim_{n\to\infty}\frac{g_k(n)}{\log n}) exist?**
As far as currently known, **this is open** (it is explicitly listed as an open Erdős problem). ([Erdős Problems][1])

---

### 2) Fixed girth threshold $m$: the function (h^{(m)}(n))

Here
[
h^{(m)}(n)=\max{\chi(G): |V(G)|=n,\ \text{girth}(G)>m}.
]

Erdős proved that (h^{(m)}(n)) is at least a polynomial in $n$ of exponent (\Omega(1/m)), in the sense that
[
\lim_{n\to\infty}\frac{\log h^{(m)}(n)}{\log n}\ \gg\ \frac{1}{m}.
]
([Erdős Problems][1])

He also proved an **upper bound for odd $m$**:
[
\limsup_{n\to\infty}\frac{\log h^{(m)}(n)}{\log n}\ \le\ \frac{2}{m+1},
\qquad (m\ \text{odd}),
]
and conjectured this (\frac{2}{m+1}) is the truth (i.e., sharp). ([Erdős Problems][1])

For **even $m$**, Erdős did not have a firm conjecture beyond expecting the exponent should lie in the interval
[
\Big[\frac{2}{m+2},\frac{2}{m}\Big],
]
and noted he could not prove this even for $m=4$. ([Erdős Problems][1])

#### A solved benchmark case: $m=3$ (triangle-free graphs)

When $m=3$, “girth (>3)” means triangle-free. The known Ramsey-theoretic asymptotics [[nomath]](Kim’s breakthrough on $R(3,t)$)[[/nomath]] imply that the maximum chromatic number of an $n$-vertex triangle-free graph satisfies
[
h^{(3)}(n)=\Theta!\left(\sqrt{\frac{n}{\log n}}\right),
]
so
[
\lim_{n\to\infty}\frac{\log h^{(3)}(n)}{\log n}=\frac12.
]
([People.tamu.edu][2])

#### So: does (\displaystyle \lim_{n\to\infty}\frac{\log h^{(m)}(n)}{\log n}) exist in general?

* For $m=3$: **yes**, and the value is **$1/2$**. ([People.tamu.edu][2])
* For general (m\ge 4): **open**. What is known is the bracket

  * lower exponent (\Omega(1/m)), and
  * for odd $m$, upper exponent (\le 2/(m+1)),
    with sharpness conjectured for odd $m$. ([Erdős Problems][1])

---

### Relationship between the two questions

These two extremal functions are (informally) inverse to each other: fixing $m$, (h^{(m)}(n)) asks “how large a chromatic number can you force while forbidding short cycles,” while fixing $k$, (g_k(n)) asks “how long can you make the shortest cycle while forcing (\chi=k).” The best known bounds in each direction are consistent with the picture that both are governed by power/log laws, but **the exact constants/exponents (and therefore the existence of the stated limits in the open cases) remain unresolved**. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/626 "https://www.erdosproblems.com/626"
[2]: https://people.tamu.edu/~huafei-yan/Teaching/Math689/ramsey5.pdf "https://people.tamu.edu/~huafei-yan/Teaching/Math689/ramsey5.pdf"
