Let $p(m)$ denote the least prime factor of $m$. Your condition is exactly
[
p\left(\binom{n}{k}\right)>k,
]
and the resulting $g(k)$ is the **Erdős–Selfridge function** (OEIS A003458). ([OEIS][1])

A key structural fact is **Kummer’s theorem / Lucas-type criterion**: for a prime (p\le k),
[
p\nmid \binom{n}{k}
\quad\Longleftrightarrow\quad
\text{in base }p,\ \text{each digit of }n\text{ is }\ge\text{ the corresponding digit of }k,
]
equivalently there are *no carries* when adding $k$ and $n-k$ in base $p$. ([msp.org][2])
Thus $g(k)$ is the smallest (n>k+1) satisfying these digit-inequalities **simultaneously for every prime (p\le k)**.

## What is known unconditionally (best proven bounds)

Classical work of Ecklund–Erdős–Selfridge shows there is an absolute constant (c>0) such that, for large $k$,
[
k^{1+c} < g(k) \le \exp\big((1+o(1)),k\big).
]
([msp.org][2])

The **best published lower bound currently recorded** is much stronger than a fixed power:
[
g(k)\gg \exp\big(c(\log k)^2\big)
\quad\text{(equivalently }g(k) > k^{c\log k}\text{ for some }c>0\text{)}.
]
This is attributed to Konyagin (1999). ([msp.org][2])

So, in big-picture terms,
[
\exp\big(c(\log k)^2\big)\ \lesssim\ g(k)\ \lesssim\ \exp\big((1+o(1))k\big),
]
and closing this huge gap is open. ([Erdős Problems][3])

## Conjectural/heuristic “right size”

Ecklund–Erdős–Selfridge conjectured $g(k)$ should be below the lcm
[
L_k=\operatorname{lcm}(1,2,\dots,k),
]
which satisfies (\log L_k\sim k), so this is consistent with the exponential upper bound. ([Erdős Problems][3])

But the strongest *heuristic* estimate points to **subexponential** growth in $k$, around
[
\log g(k)\ \asymp\ \frac{k}{\log k}
\qquad\Longleftrightarrow\qquad
g(k)=\exp!\Big(\Theta!\big(\tfrac{k}{\log k}\big)\Big).
]
This heuristic is discussed explicitly on the Erdős Problems site. ([Erdős Problems][3])

More quantitatively, Sorenson–Sorenson–Webster (2020) define an “admissible residue” model coming from Kummer’s theorem and an approximating function (\hat g(k)) [[nomath]](essentially $\hat g(k)\approx M_k/R_k$ where $M_k$ is a product of prime powers up to $k$, and $R_k$ counts admissible residues)[[/nomath]]. They prove
[
0.530684+o(1)\ \le\ \frac{\log \hat g(k)}{k/\log k}\ \le\ 1+o(1),
]
and under a uniformity heuristic they expect (\log g(k)=\log \hat g(k)+O(\log k)), i.e. $g(k)$ is typically within a polynomial factor of (\hat g(k)). ([msp.org][2])
This supports the estimate (g(k)=\exp(\Theta(k/\log k))). ([Erdős Problems][3])

## Wild fluctuations

Computed values show $g(k)$ is highly irregular [[nomath]](e.g. $g(24)=193049$ but $g(25)=2105$)[[/nomath]], and EES74 even conjectured extreme oscillation:
[
\limsup_{k\to\infty}\frac{g(k+1)}{g(k)}=\infty,\qquad
\liminf_{k\to\infty}\frac{g(k+1)}{g(k)}=0.
]
([Erdős Problems][3])

## Summary estimate

* **Proved:** ( \exp(c(\log k)^2) \ll g(k) \le \exp((1+o(1))k)). ([Erdős Problems][3])
* **Heuristic “right order”:** ( \log g(k)\asymp k/\log k), i.e. $ g(k)=\exp(\Theta(k/\log k))$ (up to polynomial factors). ([Erdős Problems][3])

If you want, I can also sketch (at a high level) why the admissible-residue count leads naturally to the scale (M_k/R_k) and why (\log(M_k/R_k)) comes out proportional to (k/\log k) (the core heuristic behind the conjectured size).

[1]: https://oeis.org/A003458 "A003458 - OEIS"
[2]: https://msp.org/obs/2020/4-1/obs-v4-n1-p23-p.pdf "An algorithm and estimates for the Erdos–Selfridge function "
[3]: https://www.erdosproblems.com/1095 "
  
    Erdős Problem #1095
  
"
