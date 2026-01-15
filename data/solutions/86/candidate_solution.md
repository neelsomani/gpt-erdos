This is **not known**. In fact it is a well-known **Erdős open problem**.

Let
[
f(n)=\max\\{|E(G)|:G\subseteq Q_n\text{ and }G\text{ has no }C_4\\}.
]
Your question is exactly asking whether
[
f(n)\le \Big(\tfrac12+o(1)\Big)|E(Q_n)|=\Big(\tfrac12+o(1)\Big)n2^{n-1}.
]
Erdős conjectured this “(\tfrac12)” is the right asymptotic value. ([Erdős Problems][1])

### What is known

**Lower bounds [[nomath]](constructions with no $C_4$)[[/nomath]]:**

* There is a very simple (C_4)-free construction with **exactly half** the edges: keep only edges between Hamming-weight layers ((0,1),(2,3),(4,5),\dots) (i.e., “every second layer”). Any (C_4) in (Q_n) uses edges from two consecutive layer-gaps, so this kills all 4-cycles. This gives
  [
  f(n)\ge \tfrac12,|E(Q_n)|.
  ]

* Brass–Harborth–Nienborg gave a denser (C_4)-free example, with edge density about
  [
  \frac{1}{2}\Big(1+\frac{1}{\sqrt n}\Big),
  ]
  (stated in the later papers as valid for certain $n$, e.g. $n$ a power of $4$). So you can beat $1/2$ by a little bit, but only by $o(1)$. 

**Upper bounds (what we can prove you cannot exceed):**

* Balogh–Hu–Lidický–Liu proved
  [
  f(n)\le 0.6068,|E(Q_n)|.
  ]

* Baber improved this to
  [
  f(n)\le 0.60318,|E(Q_n)|.
  ]


So, at present,
[
0.5 ;\le; \limsup_{n\to\infty}\frac{f(n)}{|E(Q_n)|} ;\le; 0.60318,
]
and **whether the limit is $1/2$** (equivalently, whether your statement is true) is still open. Recent papers still refer to the (C_4) case as open and still cite Baber’s (0.60318) bound as best known. ([kam.mff.cuni.cz][2])

[1]: https://www.erdosproblems.com/86 "
  
    Erdős Problem #86
  
"
[2]: https://kam.mff.cuni.cz/~spring/media/papers/4/2402.19409.pdf?utm_source=chatgpt.com "C10 has positive Turán density in the hypercube"
