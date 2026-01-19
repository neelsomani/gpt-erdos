Write (P(n)={p\le n:\ p\ \text{prime}}); then (|P(n)|=\pi(n)), and the condition says:

> for every integer (m\ge 1), among the integers in $(m,m+h(n)$) one can choose (\pi(n)) **distinct** integers, one for each prime (p\le n), such that the chosen integer for $p$ is divisible by $p$.

Equivalently, if (I=(m,m+h)\cap\mathbb Z), we want an injection
[
\phi:P(n)\hookrightarrow I,\qquad p\mid \phi(p).
]
The quantity $h(n)$ is the least $h$ that works uniformly for all $m$.

## What is known about the size of $h(n)$

This problem (in essentially this form) is due to Erdős and Pomerance; it is listed as Erdős problem #860 and also appears as Problem B32 in Guy’s collection. The precise order of growth of $h(n)$ is **not known**; what is known are the following bounds:

* **Upper bound (Erdős–Pomerance):**
  [
  h(n)\ \ll\ \frac{n^{3/2}}{\sqrt{\log n}}.
  ]
  ([Erdős Problems][1])

* **Lower bounds:**

  * Erdős and Selfridge proved a **linear** lower bound in the limsup sense:
    [
    h(n)\ >\ (3-o(1))n \quad \text{(in particular, for infinitely many (n))}.
    ]
    ([Erdős Problems][1])
  * Much stronger, Ruzsa proved that the growth is **superlinear**:
    [
    \frac{h(n)}{n}\ \to\ \infty \quad (n\to\infty).
    ]
    ([Erdős Problems][1])

So the best “estimate” currently available is the very wide window
[
n\cdot \omega(1)\ \le\ h(n)\ \ll\ \frac{n^{3/2}}{\sqrt{\log n}},
]
and in particular $h(n)$ grows faster than any constant multiple of $n$ but no faster (so far) than about (n^{3/2}/\sqrt{\log n}). ([Erdős Problems][2])

## A quick sanity-check lower bound (elementary)

Even without the deep results above, you can see $h(n)$ must be at least on the order of $n$: if (p_{\pi(n)}) is the largest prime (\le n), then any interval of length (<p_{\pi(n)}) can miss multiples of (p_{\pi(n)}) entirely (choose it between consecutive multiples), so (h(n)\ge p_{\pi(n)}\sim n). But the known results go far beyond this, showing $h(n)$ is actually **superlinear**. ([Erdős Problems][2])

## Bottom line

The currently best-known bounds are:
[
\boxed{\ \frac{h(n)}{n}\to\infty\ \text{(Ruzsa)},\qquad h(n)\ll \frac{n^{3/2}}{\sqrt{\log n}}\ \text{(Erdős–Pomerance)}\ }
]
with the earlier linear lower bound (h(n)>(3-o(1))n) due to Erdős–Selfridge. ([Erdős Problems][2])

[1]: https://www.erdosproblems.com/860 "
  
    Erdős Problem #860
  
"
[2]: https://www.erdosproblems.com/latex/860 "
  
    Erdős Problems
  
"
