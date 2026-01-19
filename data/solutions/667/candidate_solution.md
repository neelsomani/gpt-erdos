For fixed $p$, the condition “every $p$-set spans at least $q$ edges” gets stronger as $q$ increases, so

[
H(n;p,q_2)\ge H(n;p,q_1)\quad\text{whenever }q_2\ge q_1,
]

and therefore $c(p,q)$ is **nondecreasing** in $q$.

The **strict** monotonicity you ask about is (still) an **open problem** in general: it is posed as a conjecture of Erdős–Faudree–Rousseau–Schelp and is listed as open (Erdős Problems #667), with only partial endpoint information known. ([Erdős Problems][1])

### What is known (and shows at least one strict jump)

* **$q=1$** is exactly the classical off-diagonal Ramsey setting [[nomath]](“no independent set of size $p$”)[[/nomath]], and one gets bounds such as
  [
  \frac{1}{p-1}\le c(p,1)\le \frac{2}{p+1}.
  ]
  ([Erdős Problems][1])

* **(q=\binom{p-1}{2}+1)** forces (c(p,q)=1) [[nomath]](a clique linear in $n$)[[/nomath]]. ([Erdős Problems][1])
  [[nomath]](One quick way to see why: in $\overline G$, any $p$-set spans at most $p-2$ edges, so $\overline G$ cannot have a connected $p$-vertex subgraph; hence all components have size $\le p-1$, yielding an independent set of size $\Omega(n)$ in $\overline G$, i.e. a clique of size $\Omega(n)$ in $G$.)[[/nomath]]

* Erdős–Faudree–Rousseau–Schelp also showed
  [
  c\left(p,\binom{p-1}{2}\right)\le \tfrac12.
  ]
  ([Erdős Problems][1])

So in particular the **final step** is strictly increasing:
[
c!\left(p,\binom{p-1}{2}\right)\le \tfrac12 ;<; 1 = c!\left(p,\binom{p-1}{2}+1\right).
]
([Erdős Problems][1])

### Cases where strictness is actually known

* For **$p=3$**, the only possible $q$ in your range are (q=1,2), and one indeed has strict increase:

  * $q=1$: (\overline G) is triangle-free, and (R(3,t)=\Theta(t^2/\log t)) implies the guaranteed clique size in $G$ is (\Theta(\sqrt{n\log n})), hence (c(3,1)=\tfrac12). ([Wiley Online Library][2])
  * $q=2$: (\overline G) has maximum degree (\le 1) (it’s a matching plus isolates), so $G$ has a clique of size (\ge \lceil n/2\rceil), hence (c(3,2)=1).

### Bottom line

Beyond these endpoint results and the $p=3$ case, **it is not currently known** whether $c(p,q)$ is **strictly** increasing for every increment of $q$ in
[
1\le q\le \binom{p-1}{2}+1,
]
even though it is trivially **nondecreasing** and there is at least one strict jump at the very end. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/latex/667 "https://www.erdosproblems.com/latex/667"
[2]: https://onlinelibrary.wiley.com/doi/abs/10.1002/rsa.3240070302?utm_source=chatgpt.com "The Ramsey number R(3, t) has order of magnitude t2/log t"
