Let (\Delta=\Delta(G)) be the maximum degree of $G$.

### A quick guaranteed bound: ({\ge \lfloor \sqrt n\rfloor})

Pick a vertex $v$ with (\deg(v)=\Delta).

* Because $G$ is (K_4)-free, the induced subgraph on the neighborhood $N(v)$ is **triangle-free**: if (a,b,c\in N(v)) formed a triangle, then ({v,a,b,c}) would span a (K_4).
  Hence (G[N(v)]) is triangle-free and has (|N(v)|=\Delta) vertices.

So $G$ contains a triangle-free induced subgraph on (\Delta) vertices.

On the other hand, every graph with maximum degree (\Delta) has an independent set of size at least (\left\lceil \dfrac{n}{\Delta+1}\right\rceil) [[nomath]](greedy algorithm: each chosen vertex deletes at most $\Delta+1$ vertices)[[/nomath]]. An independent set is certainly triangle-free.

Therefore $G$ contains a triangle-free induced subgraph on at least
[
\max\\{\Delta\ \lceil \frac{n}{\Delta+1}\rceil\\}
]
vertices. The minimum of this expression over (\Delta) occurs around (\Delta\approx \sqrt n), giving
[
\max\\{\Delta\ \frac{n}{\Delta+1}\\}\ \ge\ \lfloor \sqrt n\rfloor.
]

So **every $n$-vertex (K_4)-free graph contains a triangle-free induced subgraph on at least (\lfloor\sqrt n\rfloor) vertices.**

---

### Best-known asymptotic bounds (the Erdős–Rogers problem)

If one asks for the *largest function $f(n)$* such that every $n$-vertex (K_4)-free graph contains an induced triangle-free subgraph on at least $f(n)$ vertices [[nomath]](this is the classical Erdős–Rogers function $f_3(n)=f_{3,4}(n)$)[[/nomath]], then the exact order is still not fully pinned down, but it is known up to polylogarithmic factors.

* A result of Shearer (combined with the “neighborhood is triangle-free” observation) yields the lower bound
  [
  f(n)\ =\ \Omega\left(\sqrt{\frac{n\log n}{\log\log n}}\right).
  ]

* Mubayi and Verstraëte (2024) constructed (K_4)-free graphs showing the upper bound
  [
  f(n)\ =\ O\big(\sqrt n,\log n\big).
  ]


In particular, (f(n)=n^{1/2+o(1)}). 

So, depending on whether you want an elementary guaranteed bound or the sharpest known asymptotics:

* **Always:** at least (\boxed{\lfloor \sqrt n\rfloor}) vertices (simple proof above).
* **Best known [[nomath]](for large $n$)[[/nomath]]:** between (\boxed{c\sqrt{\tfrac{n\log n}{\log\log n}}}) and (\boxed{C\sqrt n\log n}). 
