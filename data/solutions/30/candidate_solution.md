This is **open**.

What is known is that the main term is (\sqrt N), but the best *proved* error term is still of order (N^{1/4}) (up to improving the constant).

### Best known upper bounds

Erdős–Turán (1941), with later simplifications (e.g. Lindström), proved the classical estimate
[
h(N)\le \sqrt N + N^{1/4}+1,
]
so in particular (h(N)=\sqrt N+O(N^{1/4})). ([Erdős Problems][1])

The constant in front of (N^{1/4}) has been improved several times. For example Balogh–Füredi–Roy showed
[
h(N)\le \sqrt N+0.998,N^{1/4}
\quad\text{for all sufficiently large }N,
]
([arXiv][2])
and the current record is
[
h(N)\le \sqrt N+0.98183,N^{1/4}+O(1),
]
due to Carter–Hunter–O’Bryant. ([arXiv][3])

### Best known lower bounds

Singer’s construction (for prime powers (q)) produces Sidon sets of size (q+1) in (\mathbb Z_{q^2+q+1}), which (viewed as integers) gives large Sidon sets near the (\sqrt N) barrier. ([Springer Link][4])
In particular one gets (h(N)\ge (1-o(1))\sqrt N), so (h(N)\sim \sqrt N). ([Erdős Problems][1])

### Where your (N^\varepsilon) error term fits

Your statement
[
h(N)=\sqrt N+O_\varepsilon(N^\varepsilon)\quad(\forall \varepsilon>0)
]
would be a **major strengthening** of the known (O(N^{1/4})) error term, and it is not currently proved. It is even conjectured by some that the stronger bound
[
h(N)=\sqrt N+O(1)
]
might hold, but this is also open. ([Erdős Problems][1])

So at present, the best unconditional understanding is:
[
\sqrt N,(1-o(1)) \le h(N)\le \sqrt N + 0.98183,N^{1/4}+O(1),
]
and improving the exponent (1/4) (let alone to (N^\varepsilon) for every (\varepsilon)) remains an outstanding problem. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/30 "
  
    Erdős Problem #30
  
"
[2]: https://arxiv.org/abs/2103.15850?utm_source=chatgpt.com "An upper bound on the size of Sidon sets"
[3]: https://arxiv.org/abs/2310.20032?utm_source=chatgpt.com "On the Diameter of Finite Sidon Sets"
[4]: https://link.springer.com/article/10.1007/s40590-024-00676-7?utm_source=chatgpt.com "Sidon–Ramsey and $$B_{h}$$ -Ramsey numbers | Boletín de"
