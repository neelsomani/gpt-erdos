This is a well-known open problem.

In the language used in the recent literature, an ordering (a_1,\dots,a_t) of (A\subseteq \mathbb F_p\setminus{0}) is called **valid** if the partial sums
[
s_m:=a_1+\cdots+a_m\qquad(1\le m\le t)
]
are pairwise distinct [[nomath]](equivalently: no nonempty *consecutive* block $a_i+\cdots+a_j$ with $1<i\le j\le t$ sums to $0$)[[/nomath]]. 

### Status (January 2026)

The statement

> For every prime $p$, **every** subset (A\subseteq \mathbb F_p\setminus{0}) has a valid ordering

is known as **Graham’s rearrangement conjecture** (posed by Graham in 1971 and repeated by Erdős–Graham). It is **not proved in full generality**; “the intermediate regime remains open” is explicitly stated in a 2025 paper surveying the current best bounds. ([arXiv][1])

### What *is* known (some representative milestones)

* **Small sets:** the conjecture has been verified for (|A|\le 12) (via polynomial method/computation, with references collected in later papers). 

* **First bound growing with $p$:** Kravitz (2024) proved the conjecture for
  [
  |A|\ \le\ \frac{\log p}{\log\log p}.
  ]


* **Improved “quasipolynomial” range:** Bedert–Kravitz (arXiv 2024; journal version 2025) improved this to
  [
  |A|\ \le\ \exp\big(c(\log p)^{1/4}\big)
  ]
  for an absolute constant (c>0). 

* **Very large sets:** recent work shows that in *any* finite group $G$ (even nonabelian), every subset (S\subseteq G\setminus{\mathrm{id}}) of size at least (|G|^{1-c}) has a valid ordering for some absolute (c>0). Specializing to (G=\mathbb F_p) gives validity for all sets (A\subseteq\mathbb F_p\setminus{0}) with (|A|\ge p^{1-c}). ([arXiv][1])

So: **for prime $p$, it is conjectured “yes,” but it is still open in general**; we only know it in various ranges of (|A|) [[nomath]](very small, moderately small as a function of $p$, and very large)[[/nomath]].

If you tell me the regime you care about [[nomath]](e.g. $|A|$ fixed, $|A|=o(p)$, $|A|\approx p/2$, etc.)[[/nomath]], I can point to the sharpest known theorem in that range and explain the ideas (polynomial method / rectification / dissociated sets / probabilistic absorption) behind it.

[1]: https://arxiv.org/pdf/2508.18254 "On Graham's rearrangement conjecture over $\mathbb{F}_2^n$"
