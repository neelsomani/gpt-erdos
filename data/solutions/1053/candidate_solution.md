This is **open** (it’s an Erdős problem).

What *is* known is only the “right” **big‑O** upper bound: since
[
k=\frac{\sigma(n)}{n},
]
general results on the maximal order of (\sigma(n)/n) imply (k=O(\log\log n)). In fact Grönwall proved
[
\limsup_{n\to\infty}\frac{\sigma(n)}{n\log\log n}=e^\gamma,
]
so (\sigma(n)/n) can get as large as about (e^\gamma\log\log n) along suitable integers $n$. ([MathWorld][1])

More explicitly, Robin proved an unconditional bound of the shape
[
\frac{\sigma(n)}{n}\le e^\gamma\log\log n+\frac{0.6483}{\log\log n}\quad (n\ge 3),
]
and under the Riemann Hypothesis one can drop the (0.6483/\log\log n) term for (n\ge 5041). ([arXiv][2])
So for any $k$-perfect number $n$, one certainly has (k\ll \log\log n) [[nomath]](indeed $k\lesssim e^\gamma\log\log n$ for large $n$)[[/nomath]]. ([arXiv][2])

The stronger claim you asked about,
[
k=o(\log\log n)\quad\text{as }n\to\infty\text{ through }k\text{-perfect numbers},
]
is **exactly the conjecture Erdős made** [[nomath]](in the sense that if there are infinitely many multiperfect numbers, then their “multiplier” $k$ should grow slower than $\log\log n$)[[/nomath]]. 
It remains unresolved; it is listed as open in modern compilations of Erdős problems. ([Erdős Problems][3])

[1]: https://mathworld.wolfram.com/GronwallsTheorem.html?utm_source=chatgpt.com "Gronwall's Theorem -- from Wolfram MathWorld"
[2]: https://arxiv.org/pdf/2110.13478?utm_source=chatgpt.com "arXiv:2110.13478v3 [math.NT] 29 Oct 2021"
[3]: https://www.erdosproblems.com/1053 "
  
    Erdős Problem #1053
  
"
