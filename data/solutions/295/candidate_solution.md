This is **open** (as of the current literature I can find).

### Why $(e-1)N$ is the right main term

If you fix $N$ and choose $k$ distinct denominators (n_i\ge N), then for a given $k$ the **largest possible** sum (\sum 1/n_i) is obtained by taking the **smallest** allowed denominators:
[
\sum_{i=1}^k \frac1{n_i}\ \le\ \sum_{j=0}^{k-1}\frac{1}{N+j}
= H_{N+k-1}-H_{N-1}.
]
Since (H_m=\log m+\gamma+o(1)), this is
[
H_{N+k-1}-H_{N-1} \approx \log!\left(\frac{N+k}{N}\right)=\log!\left(1+\frac{k}{N}\right).
]
To make the sum reach $1$, you therefore need
[
\log!\left(1+\frac{k}{N}\right)\gtrsim 1 \quad\Rightarrow\quad \frac{k}{N}\gtrsim e-1,
]
so (k(N)) must be at least ((e-1)N) up to lower-order terms.

### What is known rigorously

Erdős and Straus proved there is a constant (c>0) such that
[
-c ;<; k(N)-(e-1)N ;\ll; \frac{N}{\log N}.
]
In particular, this pins down the leading asymptotic:
[
k(N) = (e-1)N + O!\left(\frac{N}{\log N}\right),
]
so (k(N)/N \to e-1). ([Erdős Problems][1])

Separately (addressing a *related* “short interval” question of Erdős–Graham), Croot proved that for any rational (r>0) one can represent $r$ as a sum of distinct unit fractions with all denominators in ((N,,(e^r+o_r(1))N)), with best-possible error (o_r(1)=O_r(\log\log N/\log N)). Taking (r=1) gives representations of (1) with all denominators (< (e+o(1))N). ([arXiv][2])

### Your specific limit question

Your question asks whether
[
k(N)-(e-1)N \longrightarrow +\infty.
]
The Erdős–Straus bounds show the difference is **bounded below** by a constant [[nomath]](so it cannot go to $-\infty$)[[/nomath]], but they do **not** show it grows, and no matching growing lower bound is currently known. The problem is explicitly listed as open (Erdős Problem #295). ([Erdős Problems][1])

So the best answer at present is:

**Unknown/open.** We only know
[
-c < k(N)-(e-1)N \ll \frac{N}{\log N},
]
and whether the left-hand side actually tends to (+\infty) is unresolved. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/forum/thread/295 "https://www.erdosproblems.com/forum/thread/295"
[2]: https://arxiv.org/abs/math/9904181 "[math/9904181] On Unit Fractions with Denominators in Short Intervals"
