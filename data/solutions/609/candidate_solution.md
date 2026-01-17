Write $f(n)$ for the smallest $m$ such that **every** $n$-edge-colouring of (K_{2^n+1}) contains a monochromatic odd cycle of length (\le m).

A couple of basic facts frame the problem.

* For (K_{2^n}) there is an explicit $n$-colouring in which **every** colour class is bipartite [[nomath]](e.g. label vertices by ${0,1}^n$ and colour an edge by the first coordinate where the labels differ)[[/nomath]], so there are **no** monochromatic odd cycles at all. 
* For (K_{2^n+1}) this is impossible: if each colour class were bipartite, taking the bipartition in each colour gives each vertex an $n$-bit “side-vector”, forcing at most (2^n) distinct vertices. Hence some colour class is non-bipartite and contains an odd cycle. 

So $f(n)$ is finite, and the real question is its growth.

## Best current bounds

This is an Erdős–Graham problem $1973/75$. The sharp order of growth is **open**; the best known bounds are very far apart.

### Lower bound (Day–Johnson, 2017)

Day and Johnson proved (f(n)\to\infty), and quantitatively
[
f(n)\ \ge\ 2^{,c\sqrt{\log n}}
]
for some absolute constant (c>0) [[nomath]](the base of $\log$ only affects $c$)[[/nomath]]. 

Equivalently, $f(n)$ is **superconstant** but still much smaller than any fixed power (n^\varepsilon).

### Upper bounds (2024–2025 breakthroughs)

* Girão and Hunter (2024) gave the first nontrivial improvement over the trivial (f(n)\le 2^n+1), showing
  [
  f(n)=O!\left(\frac{2^n}{n^{1-o(1)}}\right),
  ]
  more concretely: for every (\varepsilon>0) and all large $n$,
  [
  f(n)\ \le\ \frac{2^{n+1}}{n^{1-\varepsilon}}.
  ]


* Janzer and Yip (2025) then obtained an **exponential improvement**:
  [
  f(n)=O!\left(n^{3/2},2^{n/2}\right).
  ]
  ([arXiv][1])

Putting these together, the currently best “estimate” is
[
2^{,c\sqrt{\log n}}
\ \le\
f(n)
\ \le\
C,n^{3/2}2^{n/2}
\qquad\text{for some constants }c,C>0.
]


## What’s unknown

The gap between (\exp(\Theta(\sqrt{\log n}))) and (\mathrm{poly}(n),2^{n/2}) is enormous. Determining the true order of growth of $f(n)$ remains open. ([Erdős Problems][2])

[1]: https://arxiv.org/pdf/2506.14910?utm_source=chatgpt.com "Short monochromatic odd cycles"
[2]: https://www.erdosproblems.com/609 "
  
    Erdős Problem #609
  
"
