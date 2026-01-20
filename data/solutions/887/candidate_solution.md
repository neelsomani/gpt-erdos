This is **open** in general [[nomath]](already open for $C=1$)[[/nomath]].

It’s a question of Erdős–Rosenfeld (1997) and is listed as an open Erdős problem (#887). ([Erdős Problems][1])

### What is known

* **A universal bound would have to satisfy (K\ge 4).**
  Erdős and Rosenfeld constructed **infinitely many** $n$ having **4 divisors** in
  [
  \bigl(\sqrt n,\ \sqrt n+n^{1/4}\bigr),
  ]
  so if a constant $K$ exists in your statement, it cannot be (<4). ([Erdős Problems][1])

* **For perfect squares (n=N^2), the answer is “yes” [[nomath]](with an absolute $K$)[[/nomath]].**
  Chan proved that perfect squares have at most five divisors in a symmetric (N\pm cN^{1/2}) window [[nomath]](equivalently $\sqrt n\pm c,n^{1/4}$)[[/nomath]], and this gives an absolute bound for the one-sided question in the square case; he also shows examples demonstrating sharpness in that setting. 

* **For slightly *shorter* windows than (n^{1/4}), uniform bounds are known.**
  Letendre (2025) formulates the broader “Ruzsa/Erdős–Rosenfeld” conjecture and proves bounds in several parameter ranges. In particular, his Proposition 1 gives [[nomath]](specializing $\theta=\tfrac12$)[[/nomath]] a uniform estimate of the form
  [
  D_n!\left(n^{1/2},,n^{1/4-\delta}\right)\ \ll\ \frac{1}{\delta}
  \qquad(\delta>0),
  ]
  so **once the interval is (n^{1/4-\delta})** [[nomath]](even just a tiny power smaller than $n^{1/4}$)[[/nomath]], the number of divisors is (O_\delta(1)) uniformly in $n$. 
  [[nomath]](He also states the conjecture at the $\sqrt n + n^{1/2-\varepsilon}$ scale as “Conjecture 1”.)[[/nomath]] 

* **A simple unconditional bound depending on $C$ is easy.**
  Letendre’s discussion yields a general “convexity” type bound implying roughly
  [
  |\\{d\mid n:\ \sqrt n\le d\le \sqrt n + Cn^{1/4}\\}|\ \le\ C^2+1
  ]
  (up to rounding and endpoint conventions). 
  The hard part is removing the dependence on $C$ and replacing it by an **absolute** $K$.

### Bottom line

As of **January 2026**, there is **no known proof or disproof** of an absolute constant $K$ for your interval $(\sqrt n,\sqrt n + Cn^{1/4})$ in full generality; it remains an open Erdős–Rosenfeld/Ruzsa-type problem. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/887 "
  
    Erdős Problem #887
  
"
