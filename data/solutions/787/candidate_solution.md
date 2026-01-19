This parameter is studied in additive combinatorics under the name

* **“sum-free with respect to $A$”** / **“sum-avoiding in $A$”**, and
* the extremal function is usually written (\varphi(n)).

Your $g(n)$ is exactly this (\varphi(n)): the minimum, over all (|A|=n), of the largest (|B|\subseteq A) with no **restricted** sum (b_1+b_2) [[nomath]](with $b_1\neq b_2$)[[/nomath]] landing back in $A$. ([arXiv][1])
Moreover, although you stated (A\subset\mathbb R), the integer and real versions are equivalent for this problem (one can transfer the additive relations), so results for (A\subset\mathbb Z) apply. 

## A clean, elementary lower bound: (g(n)\gtrsim \log n)

Here is the standard (Erdős–Moser/Turán-type) argument.

1. From (A\subset\mathbb R) with (|A|=n), at least $n/2$ elements are **positive** or at least $n/2$ are **negative**. Work with whichever has size (m\ge n/2). If they are negative, multiply by (-1) [[nomath]](this preserves the “sum in $A$” relations within that sign class)[[/nomath]]. ([arXiv][1])

2. So assume we have $m$ positive elements; list them increasingly:
   [
   0<a_1<a_2<\cdots<a_m.
   ]

3. Build a graph $G$ on these $m$ vertices where (a_i) is joined to (a_j) ((i\neq j)) iff (a_i+a_j\in A).
   An independent set in this graph is exactly a $B$ with the desired property.

4. Degree bound: fix (a_i). If (a_i) is adjacent to (a_j), then (a_i+a_j\in A), and because all numbers are positive we have (a_i+a_j>a_i). Thus (a_i+a_j) must be one of the elements of $A$ that are **larger than (a_i)**, of which there are at most $m-i$ among the positive elements. Also, for each possible sum $s$, the partner (a_j=s-a_i) is unique. Hence
   [
   \deg(a_i)\le m-i.
   ]

5. Apply the Caro–Wei/Turán bound:
   [
   \alpha(G)\ \ge\ \sum_{i=1}^m \frac{1}{\deg(a_i)+1}
   \ \ge\ \sum_{i=1}^m \frac{1}{m-i+1}
   \ =\ H_m
   \ =\ \log m + O(1).
   ]
   So
   [
   g(n)\ \ge\ \log(n/2) - O(1)\ =\ \log n - O(1).
   ]
   This argument (and variants) appears in standard references on the problem. ([arXiv][1])

So **at minimum** one can always guarantee a subset $B$ of size on the order of (\log n).

## Best known bounds as of 2025: between a power of (\log n) and (e^{C\sqrt{\log n}})

The real punchline is that $g(n)$ is known to be **much smaller than any power of $n$**, and its precise growth is a famous open problem (Erdős–Moser).

### Lower bound (superlogarithmic)

A deep result of Sanders shows there is an absolute (c>0) such that every $n$-element set (A\subset\mathbb Z) contains such a $B$ with
[
|B|\ \ge\ (\log n)^{1+c}.
]
([arXiv][2])

More recently, Beker (2025) gives another proof of a bound of the same *shape*, with an explicit (small) exponent: for any (c<1/68) and $n$ large enough,
[
g(n)\ \ge\ (\log n)^{1+c}.
]


### Upper bound [[nomath]](subpolynomial in $n$)[[/nomath]]

There are constructions (Ruzsa) of sets $A$ of size $n$ for which every sum-avoiding (B\subseteq A) is at most
[
|B|\ \le\ \exp\bigl( C\sqrt{\log n}\bigr)
]
for some absolute $C$. This is the **best known upper bound to date**. 

Equivalently, (g(n) \le n^{o(1)}): it grows more slowly than (n^\varepsilon) for every fixed (\varepsilon>0).

## Summary estimate

Putting the current best bounds together, one has [[nomath]](for $n$ sufficiently large)[[/nomath]]
[
(\log n)^{1+c_0}\ \lesssim\ g(n)\ \lesssim\ \exp!\bigl(C\sqrt{\log n}\bigr),
]
for some absolute constants (c_0,C>0). ([arXiv][2])

So $g(n)$ is known to go to infinity, but it is **subpolynomial** in $n$, and determining its true order of growth remains open.

If you want, I can also sketch the *idea* of Ruzsa’s construction for the upper bound [[nomath]](it’s quite nontrivial, but the “shape” $\exp(\Theta(\sqrt{\log n}))$ has a nice heuristic)[[/nomath]].

[1]: https://arxiv.org/pdf/1603.03068 "Sum-avoiding Sets in Groups"
[2]: https://arxiv.org/abs/1804.03356 "[1804.03356] The Erdos-Moser sum-free set problem"
