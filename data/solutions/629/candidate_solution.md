Let

[
n(k)=\min{|V(G)|:G\text{ is bipartite and }\chi_L(G)>k},
]

i.e. the smallest order of a bipartite graph that is **not** $k$-choosable.

### 1) This is an Erdős–Rubin–Taylor open problem

Erdős–Rubin–Taylor explicitly posed this question [[nomath]](in their notation $N(2,k)$)[[/nomath]] and gave the basic bounds, but the exact value of $n(k)$ is not known in general. 

So “determine $n(k)$” currently means “give the best known bounds / exact values for small $k$, and explain what $n(k)$ is equivalent to.”

---

### 2) You may assume the extremal graph is complete bipartite

If a bipartite graph $G$ with bipartition $(A,B)$ is not $k$-choosable, then adding edges between $A$ and $B$ keeps the graph bipartite and cannot make it easier to list-color. Hence, the smallest counterexample may be taken to be some complete bipartite (K_{|A|,|B|}). This is the $N(2,k)$ viewpoint in Erdős–Rubin–Taylor. 

---

### 3) Connection to Property B (hypergraph 2-colorability)

Define (M_k) to be the minimum size of a family (\mathcal F) of $k$-subsets that **does not** have *Property B* [[nomath]](equivalently: a $k$-uniform hypergraph that is not 2-colorable)[[/nomath]]. Erdős–Rubin–Taylor show the key comparison

[
M_k \le n(k)\le 2M_k .
]

Sketch of why:

* (**Upper bound**) Take a minimum non–Property-B family (\mathcal F) with (|\mathcal F|=M_k). Put a copy of (\mathcal F) as the lists on each side of (K_{M_k,M_k}). Any proper list-coloring would induce a Property-B witness set, contradicting the choice of (\mathcal F). Hence (n(k)\le 2M_k). 
* (**Lower bound**) If a complete bipartite graph has fewer than (M_k) vertices total, then the family of its $k$-lists necessarily has Property B, and that witness set can be used to color one side from $B$ and the other from (B^c), giving a valid list-coloring. So no counterexample exists below (M_k). 

This equivalence is also emphasized cleanly by Kostochka. ([The Electronic Journal of Combinatorics][1])

So: **understanding $n(k)$ is essentially the same difficulty as understanding (M_k)** (the classic “Property B” extremal function). ([Erdős Problems][2])

---

### 4) Best general bounds for $n(k)$

From Erdős–Rubin–Taylor one already gets the “crude” exponential–polynomial bounds

[
2^{k-1} < n(k) < k^2,2^{k+2}.
]


Much stronger lower bounds are known via Property B. In particular, Radhakrishnan–Srinivasan (improving Beck) imply

[
n(k)=\Omega\left(2^k\sqrt{\frac{k}{\log k}}\right),
]
and the classical Erdős construction gives
[
n(k)=O\left(k^2 2^k\right).
]
([Erdős Problems][3])

So the currently best-known growth window is

[
c,2^k\sqrt{\frac{k}{\log k}}
\le
n(k)
\le
Ck^2 2^k
\qquad (k\ \text{large}),
]

for absolute constants (c,C>0). ([Erdős Problems][2])

It remains open to pin down the correct polynomial factor in front of (2^k) [[nomath]](even up to $k^{\Theta(1)}$)[[/nomath]]. ([Erdős Problems][3])

---

### 5) Exact values known

From Erdős–Rubin–Taylor and later work:

* (n(1)=2) (just an edge). 
* (n(2)=6). 
* (n(3)=14). ([Erdős Problems][3])

Also Hanson–MacGillivray–Toft prove the recurrence
[
n(k)\le kn(k-2)+2^k,
]
which yields e.g. $n(4)\le 40$, $n(6)\le 304$, etc. ([Erdős Problems][3])

---

### 6) A concrete explicit construction (not optimal asymptotically, but simple)

A standard explicit way to force (\chi_L>k) is: take colors ({1,\dots,2k-1}) and assign **every** $k$-subset as a list on each side of (K_{m,m}), where
[
m=\binom{2k-1}{k}.
]
Then (K_{m,m}) is not $k$-choosable. 

This gives an easy explicit bound (n(k)\le 2\binom{2k-1}{k}), though the best known general upper bounds are $O(k^2 2^k)$ by more delicate constructions. 

---

## Bottom line

* The **exact** function $n(k)$ is **unknown** in general (open since Erdős–Rubin–Taylor). ([Erdős Problems][3])
* It is tightly linked (within a factor of 2) to the Property B extremal function (M_k):
  [
  M_k \le n(k)\le 2M_k.
  ]

* The best general bounds currently are:
  [
  n(k)=\Omega!\left(2^k\sqrt{\frac{k}{\log k}}\right)
  \quad\text{and}\quad
  n(k)=O(k^2 2^k),
  ]
  with exact values (n(1)=2), (n(2)=6), (n(3)=14). ([Erdős Problems][3])

If you want, I can also spell out an explicit “bad” list assignment that witnesses (n(2)=6) and (n(3)=14) (the latter coming from the 7 triples of the Fano plane).

[1]: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v9i1n9/pdf/ "v9i1n9.dvi"
[2]: https://www.erdosproblems.com/901 "
  
    Erdős Problem #901
  
"
[3]: https://www.erdosproblems.com/629 "
  
    Erdős Problem #629
  
"
