This is **not known in general**.

What you are asking is exactly the **Erdős–Nešetřil strong edge-colouring (strong chromatic index) conjecture**: you want to split the edges into induced matchings (your “strongly independent edge sets”), and the question is whether this always needs at most (\tfrac54\Delta^2) parts. ([Erdős Problems][1])

A few key facts:

* The bound (\tfrac54\Delta^2) would be **best possible** (you cannot hope for a smaller constant in general): a standard extremal example is a **blow-up of (C_5)** (replace each vertex of a 5-cycle by an independent set and each edge by a complete bipartite graph). For even (\Delta) this construction has strong chromatic index exactly (\tfrac54\Delta^2). ([Erdős Problems][1])

* The conjecture is only fully verified for **(\Delta \le 3)** (subcubic graphs). ([arXiv][2])
  For **(\Delta=4)** the conjectured number is (20), but the best published general upper bound I see is **21**. ([arXiv][2])

* For general graphs, a simple greedy argument gives the classic upper bound
  [
  \chi'_s(G)\le 2\Delta(\Delta-1)+1 = 2\Delta^2-2\Delta+1,
  ]
  which is still far above (1.25\Delta^2). 

* The best **asymptotic** bound known for large (\Delta) is
  [
  \chi'_s(G)\le 1.772\Delta^2
  \quad\text{for sufficiently large }\Delta,
  ]
  due to Hurley, de Joannis de Verclos, and Kang (improving earlier constants $1.998$, $1.93$, $1.835$). ([Erdős Problems][1])

So the direct answer to your question is: **it is a famous open problem**; we do not yet know whether (\tfrac54\Delta^2) always suffices. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/latex/149 "
  
    Erdős Problems
  
"
[2]: https://arxiv.org/abs/1806.07012 "[1806.07012] Strong chromatic index of graphs with maximum degree four"
