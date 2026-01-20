No one currently knows.

Your question is exactly the **Gaussian moat problem**: view the Gaussian primes as vertices in a graph, connect two primes if their Euclidean distance is at most some fixed constant $C$, and ask whether there is an **infinite path** [[nomath]](equivalently, an infinite sequence $x_1,x_2,\dots$ of distinct Gaussian primes with $|x_{n+1}-x_n|\le C$)[[/nomath]]. This problem remains **unresolved** in the literature. ([MathWorld][1])

What *is* known (partial progress):

* **Small step sizes are provably/computationally insufficient (from the origin-component formulation).**
  Gethner–Wagon–Wick (1998) showed that steps of length (<\sqrt{26}) do not allow a walk to infinity (there is a “moat” of that width). ([MathWorld][1])
  Tsuchimura (2004) pushed the computational barrier further, reporting that even for step size (k=\sqrt{36}=6) the connected component containing the origin is finite [[nomath]](so there is a moat of width $6$ around that component)[[/nomath]]. 

* **There are arbitrarily large *local* gaps** (Gaussian primes whose nearest Gaussian-prime neighbor is very far away), even constrained to the real axis. But such gaps do **not** by themselves rule out an infinite bounded-step route that “goes around” them in the plane. ([Wikipedia][2])

Heuristics (not proofs):

* **Percolation/random models suggest a negative answer.**
  Vardi’s “prime percolation” model treats Gaussian primes as a kind of sparse random set and predicts that to have an unbounded walk, the step size should grow on the order of (\sqrt{\log |z|}) at scale (|z|); in particular, a *fixed* step bound would be expected to fail. This is heuristic guidance, not a theorem about actual Gaussian primes. 

Finally, there have been **claimed proofs** of “no” that did not stand up: for example, a 2019 arXiv preprint has an explicit note that a key theorem/argument is incorrect, and a 2024 arXiv submission claiming a proof was withdrawn. ([arXiv][3])

So the honest state of play is:

* Existence of such a bounded-step infinite sequence is **open**.
* The best-established results are **lower bounds** (you can’t do it with very small steps), plus substantial computational and heuristic evidence pointing toward “probably no,” but no definitive proof either way. ([MathWorld][1])

[1]: https://mathworld.wolfram.com/Moat-CrossingProblem.html "Moat-Crossing Problem -- from Wolfram MathWorld"
[2]: https://en.wikipedia.org/wiki/Gaussian_moat?utm_source=chatgpt.com "Gaussian moat"
[3]: https://arxiv.org/list/math.NT/2019-08?show=500&skip=40&utm_source=chatgpt.com "Number Theory Aug 2019"
