For **$r=3$** (triangle‑free graphs), **yes**: Ajtai–Komlós–Szemerédi proved that every triangle‑free $n$-vertex graph of average degree $t$ has an independent set of size (\Omega\left(\frac{\log t}{t}n\right)) [[nomath]](indeed they state an explicit constant like $0.01\cdot \frac{n}{t}\log t$)[[/nomath]]. 

For **(r\ge 4)**, the statement you wrote is **a well‑known open problem/conjecture** of Ajtai–Erdős–Komlós–Szemerédi (1981). As summarized in Alon’s 1996 paper (and also tracked as Erdős Problem #802), they proved the weaker bound
[
\alpha(G)\ \ge\ c(r)\frac{n}{t}\log\log(t+1),
]
and conjectured the stronger
[
\alpha(G)\ \ge\ c(r)\frac{n}{t}\log t.
]


The **best general bound currently recorded** toward the conjecture is due to **Shearer (1995)**, improving (\log\log) to (\log/\log\log):
[
\alpha(G)\ \ge\ c'(r)\frac{n}{t}\frac{\log t}{\log\log(t+1)}.
]


There are also **positive results under stronger “local” assumptions** [[nomath]](stronger than merely $K_r$-free)[[/nomath]], e.g. Alon proves the conjectured (\frac{\log t}{t}n) order [[nomath]](up to an $r$-dependent constant)[[/nomath]] if every vertex neighborhood has bounded chromatic number [[nomath]](roughly “each neighborhood is $(r-2)$-colorable”)[[/nomath]]. ([Erdős Problems][1])

So:

* **True for $r=3$**. 
* **Open for fixed (r\ge 4)** [[nomath]](best known is $\Omega_r\big(\frac{\log t}{t\log\log t}n\big)$)[[/nomath]]. 

[1]: https://www.erdosproblems.com/802 "
  
    Erdős Problem #802
  
"
