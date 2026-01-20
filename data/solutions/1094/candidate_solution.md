What you wrote is a **well-known open conjecture** of **Erdős–Lacampagne–Selfridge** about the *least* prime factor of binomial coefficients (and it is recorded as **Erdős Problem #1094**). ([Erdős Problems][1])

### Precise status

* In their 1988 paper, Erdős–Lacampagne–Selfridge conjecture that for **all** (n\ge 2k),
  [
  \operatorname{lpf}\binom{n}{k}\ \le\ \max\left(\frac{n}{k},,k\right),
  ]
  with **only finitely many exceptions**, and they even propose an explicit finite list of exceptions. 
* The problem remains listed as **open** (with the same conjectured exception list) on the Erdős Problems site. ([Erdős Problems][1])

### The conjectured finite exception list (14 pairs)

The conjectured exceptions [[nomath]](all with $n\ge 2k$)[[/nomath]] are: ([Erdős Problems][1])
[
\binom{7}{3},\binom{13}{4},\binom{23}{5},\binom{14}{4},\binom{44}{8},\binom{46}{10},\binom{47}{10},\binom{47}{11},
\binom{62}{6},\binom{74}{10},\binom{94}{10},\binom{95}{10},\binom{241}{16},\binom{284}{28}.
]

For clarity, here are their **least prime factors** and the bound (\max(n/k,k)) (each one violates the inequality):

|  $(n,k)$ | (\operatorname{lpf}\binom{n}{k}) | (\max(n/k,k)) |
| -------: | -------------------------------: | ------------: |
|    (7,3) |                                5 |             3 |
|   (13,4) |                                5 |             4 |
|   (23,5) |                                7 |             5 |
|   (14,4) |                                7 |             4 |
|   (44,8) |                               11 |             8 |
|  (46,10) |                               11 |            10 |
|  (47,10) |                               11 |            10 |
|  (47,11) |                               13 |            11 |
|   (62,6) |                               19 |       10.333… |
|  (74,10) |                               11 |            10 |
|  (94,10) |                               11 |            10 |
|  (95,10) |                               11 |            10 |
| (241,16) |                               17 |            16 |
| (284,28) |                               29 |            28 |

### How this relates to other conjectures in the same circle

A useful way to parse (\max(n/k,k)) is by regimes:

* If (n\ge k^2), then (\max(n/k,k)=n/k). So the conjecture predicts
  [
  \operatorname{lpf}\binom{n}{k}\le \frac{n}{k}\quad (n\ge k^2),
  ]
  except finitely many $(n,k)$.
* If (2k\le n\le k^2), then (\max(n/k,k)=k), so it predicts
  [
  \operatorname{lpf}\binom{n}{k}\le k\quad (2k\le n\le k^2),
  ]
  except finitely many $(n,k)$.

Selfridge made a stronger related conjecture: that (\operatorname{lpf}\binom{n}{k}\le n/k) already for (n\ge k^2-1), with the famous single exception (\binom{62}{6}). ([Erdős Problems][1])

They also discuss still-stronger “dream bounds” like (\operatorname{lpf}\binom{n}{k}\le \max(n/k,\sqrt{k})) or even (\max(n/k,O(\log k))), again with only finitely many exceptions. ([Erdős Problems][1])

### What *is* known (qualitatively)

* Erdős observed that for **each fixed** $k$, once $n$ is large enough [[nomath]](depending on $k$)[[/nomath]], one always has (\operatorname{lpf}\binom{n}{k}\le n/k). ([Erdős Problems][1])
  So for any *fixed* $k$, there are only finitely many $n$ that can fail the $n/k$ bound.
* The difficulty is making this **uniform in $k$** strongly enough to force only **finitely many exceptional pairs $(n,k)$ overall**, which is exactly what your statement asserts. This uniform “global finiteness” remains open. ([Erdős Problems][1])

If you tell me what you want next—e.g. $i$ a clean restatement in equivalent forms, (ii) the “deficiency” framework Erdős–Lacampagne–Selfridge use, or (iii) the best partial theorems toward it—I can expand in that direction.

[1]: https://www.erdosproblems.com/1094 "
  
    Erdős Problem #1094
  
"
