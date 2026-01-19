Write (A\subseteq [N]:={1,\dots,N}). Call $A$ **LCM-$k$-free** if it contains no distinct (a_1,\dots,a_k) such that
$
\mathrm{lcm}(a_i,a_j)\ \text{ is the same for all }1\le i<j\le k .
$
Your (f_k(N)) is exactly the extremal “harmonic weight” of an LCM-$k$-free set.

## What is known (best current bounds)

A 2025 paper of Tang–Zhang (written to address Erdős’s question) gives the sharpest general picture available. ([arXiv][1])

### Upper bounds

The trivial bound is just the harmonic sum:
[
f_k(N)\le \sum_{n\le N}\frac1n = \log N + O(1).
]
([arXiv][1])

Erdős proved the stronger
[
f_k(N)\ll_k \frac{\log N}{\log\log N}.
]
([arXiv][1])

And it is noted (via the Erdős Problems website discussion) that one can further improve this to
[
f_k(N)\ \le\ \log N\cdot \exp\Big(-\Omega_k\Big(\frac{\log\log N}{\log\log\log N}\Big)\Big),
]
which is still ((\log N)^{1-o(1)}) but with a power saving in the exponent. ([arXiv][1])

### Unconditional polylogarithmic lower bound

Tang–Zhang prove an explicit **power-of-(\log N)** lower bound: for fixed (k\ge 3),
[
f_k(N)\ \ge\ (\log N)^{,c_k-o(1)}
\qquad (N\to\infty),
]
where
[
c_k:=\frac{k-2}{e\big((k-2)!\big)^{1/(k-2)}}.
]
([arXiv][1])

Numerically this gives (approximately)
[
c_3=\tfrac1e\approx 0.368,\quad
c_4=\tfrac{\sqrt2}{e}\approx 0.520,\quad
c_5\approx 0.607,\quad
c_6\approx 0.665,\quad
c_7\approx 0.706,
]
and (c_k\uparrow 1) as (k\to\infty) (by Stirling’s formula).

So, **for every fixed (k\ge 3)** one has the growth window
[
(\log N)^{c_k-o(1)}\ \le\ f_k(N)\ \le\ (\log N)^{1-o(1)}.
]

## Connection to the sunflower problem (and a refined “exponent” sandwich)

Let (\mu_k^{\mathrm S}) be the Erdős–Szemerédi $k$-sunflower-free capacity [[nomath]](defined via the maximum size $F_k(n)$ of $k$-sunflower-free families on $[n]$)[[/nomath]]. Tang–Zhang prove the bounds
[
(\log N)^{\log \mu_k^{\mathrm S}-o(1)}\ \le\ f_k(N)\ \ll\ (\log N)^{\mu_k^{\mathrm S}-1+o(1)}.
]
([arXiv][1])

They also show the striking equivalence:
[
\mu_k^{\mathrm S}=2\ \Longleftrightarrow\ f_k(N)=(\log N)^{1-o(1)}.
]
([arXiv][1])

So determining the “true” polylog exponent of (f_k(N)) is tightly linked to deep open questions about sunflowers.

### Example: $k=3$

Using the best currently quoted bounds on (\mu_3^{\mathrm S}), they get
[
(\log N)^{\log(1.551)-o(1)}\ \le\ f_3(N)\ \ll\ (\log N)^{\frac{3}{2^{2/3}}-1+o(1)},
]
i.e. roughly
[
(\log N)^{0.439-o(1)} \ \lesssim\ f_3(N)\ \lesssim\ (\log N)^{0.890+o(1)}.
]
([arXiv][1])

## Bottom line estimate

* (f_k(N)) is **polylogarithmic** in $N$: it grows like a power of (\log N), not like (\log\log N) or (\log N) itself.
* Unconditionally, for fixed (k\ge 3),
  [
  (\log N)^{c_k-o(1)}\ \le\ f_k(N)\ \le\ \log N\cdot \exp!\Big(-\Omega_k!\Big(\frac{\log\log N}{\log\log\log N}\Big)\Big),
  ]
  with explicit (c_k=\dfrac{k-2}{e((k-2)!)^{1/(k-2)}}). ([arXiv][1])
* A more structural “best possible” exponent is currently unknown; it is bounded in terms of the sunflower capacity (\mu_k^{\mathrm S}) via
  [
  (\log N)^{\log \mu_k^{\mathrm S}-o(1)}\ \le\ f_k(N)\ \ll\ (\log N)^{\mu_k^{\mathrm S}-1+o(1)}.
  ]
  ([arXiv][1])

If you want, I can also sketch the “prime bucketing” construction behind the ((\log N)^{c_k}) lower bound [[nomath]](it’s quite clean: build many squarefree numbers from disjoint prime blocks so that equal-LCM $k$-tuples would force a forbidden $k$-cosunflower structure)[[/nomath]].

[1]: https://arxiv.org/pdf/2512.20055 "Harmonic LCM patterns and sunflower-free capacity"
