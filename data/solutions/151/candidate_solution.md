This is **not known in general**.

It is an old question of **Erdős and Gallai** (later appearing with Tuza), and it is still listed as **open**. ([Erdős Problems][1])

### Why it is true for triangle‑free graphs

If $G$ is triangle‑free, then every clique has size at most $2$, so the maximal cliques are exactly the edges.
So a clique transversal is the same thing as a **vertex cover**, and
[
\tau(G)=n-\alpha(G),
]
where (\alpha(G)) is the independence number. Since by definition every triangle‑free (n)-vertex graph has (\alpha(G)\ge H(n)), we get (\tau(G)\le n-H(n)) in the triangle‑free case (as you noted).

### What is known for general graphs

For arbitrary graphs, the inequality
[
\tau(G)\le n-H(n)
]
is **open**, and Erdős even commented that it might be “wrongheaded”. ([Erdős Problems][1])

What *is* known is a weaker general upper bound. It is “easy to see” that
[
\tau(G)\le n-\sqrt{n}.
]
([Erdős Problems][1])

And Erdős–Gallai–Tuza proved a stronger form
[
\tau(G)\le n-\sqrt{2n}+O(1).
]
([Erdős Problems][2])

### Why your bound would be much stronger

The function $H(n)$ is essentially the “worst‑case” independence number in triangle‑free graphs, and it grows like (\Theta(\sqrt{n\log n})) (up to constants), coming from classical Ramsey‑theory results [[nomath]](Ajtai–Komlós–Szemerédi give a $\sqrt{n\log n}$ lower bound, and Kim’s work shows this order is tight)[[/nomath]]. ([Erdős Problems][2])

So $n-H(n)$ is about (n-\Theta(\sqrt{n\log n})), which is stronger than the known (n-\Theta(\sqrt n)) bounds by a factor of about (\sqrt{\log n}). ([Erdős Problems][2])

### Bottom line

* **Triangle‑free $G$:** yes, the inequality holds for the simple reason above.
* **General $G$:** the statement (\tau(G)\le n-H(n)) is an **open problem** (Erdős Problem #151). ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/151 "
  
    Erdős Problem #151
  
"
[2]: https://www.erdosproblems.com/latex/610 "
  
    Erdős Problems
  
"
