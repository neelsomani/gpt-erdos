This is an **open problem** (asked by Erdős). Primes $p$ with your property are called **cluster primes**: an odd prime $p$ such that every even (k\le p-3) can be written as (k=q_1-q_2) with primes (q_1,q_2\le p). ([Wikipedia][1])

What is known:

* **It is not known whether there are infinitely many such primes $p$.** ([Wikipedia][1])
* The **first prime that fails** the property is $97$. ([Erdős Problems][2])
  [[nomath]](Equivalently: the first 23 odd primes up to $89$ are cluster primes; $97,127,149,\dots$ are among the first non‑cluster primes.)[[/nomath]] ([Wikipedia][1])
* There are strong results showing cluster primes are **extremely sparse**. If $C(x)$ is the number of cluster primes (\le x), Blecksmith–Erdős–Selfridge (1999) proved
  [
  C(x)\ll_A \frac{x}{(\log x)^A}\quad\text{for every }A>0,
  ]
  and Elsholtz (2003) improved this to
  [
  C(x)\ll x\exp\big(-c(\log\log x)^2\big)\quad\text{for every }c<1/8.
  ]
  ([Erdős Problems][2])
  So even if there are infinitely many, they form a very thin set.
* A useful necessary condition: the **prime gap immediately before a cluster prime is always (\le 6)** [[nomath]](if the preceding gap were $\ge 8$, then $p-9$ can’t be formed as a difference of primes $\le p$)[[/nomath]]. ([Wikipedia][1])
* Computationally, many are known: OEIS records the cluster primes (sequence **A038134**) and notes a table of cluster primes below (10^6) (8287 of them are listed there). ([oeis.org][3])

So the best current answer is: **we don’t know** whether there are infinitely many primes $p$ with this property, though the phenomenon is well-studied under the name *cluster primes* and we do know they are very rare. ([Wikipedia][1])

[1]: https://en.wikipedia.org/wiki/Cluster_prime "Cluster prime - Wikipedia"
[2]: https://www.erdosproblems.com/latex/17 "
  
    Erdős Problems
  
"
[3]: https://oeis.org/A038134 "A038134 - OEIS"
