There’s a notational mismatch here.

* In **two‑colour Ramsey theory**, it’s very common to write
  [
  R(G;k):=R(G,K_k),
  ]
  i.e. the least $m$ such that **every red/blue colouring** of $E(K_m)$ contains a red copy of $G$ or a blue (K_k) [[nomath]](equivalently: every $m$-vertex graph contains $G$ or an independent set of size $k$)[[/nomath]].
  With this convention, the statement you ask for is a standard (known) consequence of known asymptotics/bounds.

* Under your written definition [[nomath]](“edges of $K_m$ are **$k$-coloured**”)[[/nomath]], $R(K_3;k)$ is the *multicolour triangle Ramsey number*, whose growth is tied to the difficult Schur–Erdős problem; the ratio you ask about is not something I can justify from currently standard, established bounds alone.

So below I give the proof under the **standard two‑colour** meaning (R(G;k)=R(G,K_k)), which is the setting where the limit is known and the proof is short.

---

## Proof for (R(G;k)=R(G,K_k)) (two colours)

Fix (n\ge 2). We will compare known bounds for
[
R(C_{2n+1};k)=r(C_{2n+1},K_k)
\quad\text{and}\quad
R(K_3;k)=r(K_3,K_k)=r(3,k).
]

### Step 1: $r(3,k)$ has order (k^2/\log k)

Kim proved that
[
r(3,k)=\Theta\left(\frac{k^2}{\log k}\right),
]
in particular there exists a constant (c>0) such that for all large $k$,
[
r(3,k)\ \ge\ c\frac{k^2}{\log k}.
]
This is stated in the abstract/intro of Kim’s paper. ([TAMU People][1])

### Step 2: $r(C_{2n+1},K_k)$ is at most (k^{1+1/n}/(\log k)^{1/n}) up to constants

Sudakov proved that for each fixed integer (n\ge 2), there is a constant (C_n>0) such that, as (k\to\infty),
[
r(C_{2n+1},K_k)\ \le\ C_n\frac{k^{1+1/n}}{(\log k)^{1/n}}.
]
This is exactly Theorem 1.1 in his note (with his parameters renamed to match ours). ([combinatorics.org][2])

### Step 3: Take the ratio

Combine the two inequalities:
$
\frac{R(C_{2n+1};k)}{R(K_3;k)}
=\frac{r(C_{2n+1},K_k)}{r(3,k)} \le
\frac{C_n\dfrac{k^{1+1/n}}{(\log k)^{1/n}}}{c\dfrac{k^2}{\log k}}
= \frac{C_n}{c}
k^{1+1/n-2}
(\log k)^{1-1/n}.
$
Simplify the exponent:
$
1+\frac1n-2= -\\(1-\frac1n\\),
$
so
[
\frac{R(C_{2n+1};k)}{R(K_3;k)}
\le
\frac{C_n}{c}
\left(\frac{\log k}{k}\right)^{1-1/n}.
]
Since (n\ge 2), we have (1-1/n>0), and (\log k/k\to 0). Therefore the right-hand side tends to $0$, hence
[
\lim_{k\to\infty}\frac{R(C_{2n+1};k)}{R(K_3;k)}=0.
]

That’s the desired limit.

---

If you *did* intend the **multicolour** definition you wrote [[nomath]](edges $k$-coloured)[[/nomath]], tell me and I’ll lay out what is known in that setting and what extra input would be needed to make the limit follow; but the clean argument above is for the standard two‑colour “$G$ vs (K_k)” meaning of $R(G;k)$.

[1]: https://people.tamu.edu/~huafei-yan/Teaching/Math689/ramsey5.pdf "C:\\"
[2]: https://www.combinatorics.org/volume_9/pdf/v9i1n1.pdf "v9i1n1.dvi"
