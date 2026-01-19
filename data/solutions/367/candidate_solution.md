For (k\le 2) it’s trivial, but for (k\ge 3) the (\ll_k n^2) strengthening is **false**, and the remaining (n^{2+o(1)}) question is (as far as I can tell from the current literature/status pages) still **open**.

## The easy cases (k=1,2)

Since (B_2(m)\mid m) we have (B_2(m)\le m). Hence

* $k=1$: (B_2(n)\le n).
* $k=2$: (B_2(n)B_2(n+1)\le n(n+1)\le 2n^2).

So both (n^{2+o(1)}) and (\ll_k n^2) hold for (k\le 2) (indeed with a completely explicit constant). ([Erdős Problems][1])

## For (k\ge 3), the bound (\ll_k n^2) fails

Already for $k=3$ there is an explicit infinite family with a logarithmic overshoot:
[
\prod_{m=n}^{n+2} B_2(m);\gg; n^2 \log n
\quad\text{infinitely often.}
]
Consequently, for every fixed (k\ge 3),
[
\prod_{m=n}^{n+k-1} B_2(m)\ge\prod_{m=n}^{n+2} B_2(m);\gg;n^2\log n
]
infinitely often, so no bound of the form (\ll_k n^2) can hold for (k\ge 3). ([Erdős Problems][2])

### Sketch of the construction [[nomath]](Pell + $5^t$ divisibility)[[/nomath]]

The discussion thread for Erdős Problem #367 gives the following (and a streamlined verification):

1. Take Pell solutions $(x_j,y_j)$ to
   [
   x^2-8y^2=1,
   ]
   and set
   [
   n_j:=8y_j^2.
   ]
   Then (n_j) is $2$-full [[nomath]](it’s $8$ times a square)[[/nomath]], and (n_j+1=x_j^2) is a square, hence also $2$-full. Therefore
   [
   B_2(n_j)=n_j,\qquad B_2(n_j+1)=n_j+1.
   ]
   ([Erdős Problems][1])

2. Choose a rapidly growing subsequence of indices (j_t) [[nomath]](e.g. $j_t=(3\cdot 5^{t-1}-1)/2$ as in the streamlined argument)[[/nomath]] such that
   [
   5^t \mid (n_{j_t}+2).
   ]
   Then for (t\ge 2) this forces
   [
   B_2(n_{j_t}+2)\ge5^t,
   ]
   since (5^t) is itself $2$-full for (t\ge 2). ([Erdős Problems][1])

3. One also has exponential growth (n_{j_t}=\exp(\Theta(5^t))), so (5^t\gg \log n_{j_t}). Putting everything together:
   [
   \prod_{m=n_{j_t}}^{n_{j_t}+2} B_2(m)
   \ge n_{j_t}(n_{j_t}+1),5^t
   ;\gg; n_{j_t}^2 \log n_{j_t}.
   ]
   ([Erdős Problems][1])

This is exactly the mechanism behind the “(\gg n^2\log n) infinitely often” statement recorded on the problem page. ([Erdős Problems][2])

## What about the original (n^{2+o(1)}) bound?

The same sources list the (n^{2+o(1)}) question as **open** (Erdős Problem #367). ([Erdős Problems][2])

The construction above does **not** contradict (n^{2+o(1)}), because (n^2\log n = n^{2+o(1)}). What it *does* show is that if an upper bound of the form (n^{2+o(1)}) is true, then the exponent $2$ is essentially best possible [[nomath]](you can’t replace $n^{2+o(1)}$ by $O_k(n^2)$ once $k\ge 3$)[[/nomath]]. ([Erdős Problems][2])

[1]: https://www.erdosproblems.com/forum/discuss/367 "

    Erdős Problem #367 - Discussion thread

"
[2]: https://www.erdosproblems.com/367 "
  
    Erdős Problem #367
  
"
