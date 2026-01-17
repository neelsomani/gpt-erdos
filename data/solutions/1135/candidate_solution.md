Your $f$ is exactly the “shortcut” form of the **Collatz $ (3n+1) $ map**:

[
f(n)=\begin{cases}
n/2 & (n\ \text{even})[4pt]
(3n+1)/2 & (n\ \text{odd})
\end{cases}
]

The question

[
\forall m\ge 1\ \exists k\ge 1:\ f^{(k)}(m)=1
]

is **the Collatz conjecture** (in this shortcut formulation): it asks whether every positive integer, under repeated iteration, eventually reaches the cycle through $1$ [[nomath]](for this shortcut map the cycle is $1\leftrightarrow 2$)[[/nomath]]. It is explicitly noted in the literature that since $3n+1$ is even when $n$ is odd, one can replace the odd branch by $(3n+1)/2$ without changing the essential dynamics—and that the conjecture has never been proved. ([Springer][1])

### Status

* **Unknown / open problem.** No proof or disproof is known. ([Springer][1])
* Enormous computational evidence exists: for example, a 2025 open-access paper by Barina reports computational verification for all starting values up to (2^{71}). ([Springer][1])
* There are also partial theoretical results; e.g. Tao proved that (in a logarithmic-density sense) *almost all* starting values have orbits whose minimum value becomes “almost bounded” (in a precise quantitative sense), but this still does not settle reaching $1$ for every $m$. ([arXiv][2])

So the mathematically correct answer is:

**We do not know whether such a $k$ exists for every $m$.** It is a famous unsolved problem (the Collatz conjecture), though it has been verified for all $m$ up to extremely large bounds. ([Springer][1])

[1]: https://link.springer.com/article/10.1007/s11227-025-07337-0 "Improved verification limit for the convergence of the Collatz conjecture | The Journal of Supercomputing | Springer Nature Link"
[2]: https://arxiv.org/abs/1909.03562 "[1909.03562] Almost all orbits of the Collatz map attain almost bounded values"
