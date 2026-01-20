This is **not known in general**. It’s an old conjecture of **Erdős**.

* In his 1988 problems paper, Erdős wrote that if (n_k\to\infty) “rapidly” then (\sum \frac1{n_k n_{k+1}}) is irrational, and he added that **he believed** the weaker hypothesis
  [
  \liminf_{k\to\infty} n_k^{1/2^k}>1
  ]
  “should suffice.” ([renyi.hu][1])
* The same question is listed as **open** on the Erdős Problems site (Problem #1051). ([Erdős Problems][2])

So, with your exact condition (\liminf a_n^{1/2^n}>1), the statement “the sum is always irrational” is **conjectured true but currently unproved**, and no counterexample is known (at least as reflected in these sources). ([Erdős Problems][3])

## A standard partial result (what *can* be proved easily)

If you strengthen the growth to something like
[
a_{n+1}\ge a_n^2 \quad\text{for all sufficiently large }n,
]
then one can prove the irrationality by a classic “integer between 0 and 1” argument.

Here’s the idea in a clean form.

Let
[
S=\sum_{n=1}^\infty \frac{1}{a_n a_{n+1}},\qquad
S_N=\sum_{n=1}^N \frac{1}{a_n a_{n+1}},\qquad
Q_N=\prod_{k=1}^{N+1} a_k.
]
Then (Q_N S_N\in\mathbb Z) because each denominator (a_n a_{n+1}) divides (Q_N).

If (S=\frac pq) were rational, then
[
qQ_N(S-S_N)=qQ_N\sum_{n=N+1}^\infty \frac1{a_n a_{n+1}}
]
would be a **positive integer** for every $N$.

Under (a_{n+1}\ge a_n^2) (eventually), one can show the tail is so tiny that
[
Q_N(S-S_N) < \frac{2}{a_{N+1}}
]
for all large $N$, hence [[nomath]](qQ_N$S-S_N$ < 1)[[/nomath]] for all large $N$, contradicting that it is a positive integer. Therefore $S$ must be irrational.

This kind of proof is what Erdős alluded to by “(n_k\to\infty) rapidly.” ([renyi.hu][1])

---

If you want, I can also:

* show the estimate (Q_N(S-S_N) < 2/a_{N+1}) in full detail under (a_{n+1}\ge a_n^2), or
* discuss why the original (\liminf a_n^{1/2^n}>1) condition is trickier (it allows “bursty” growth that breaks the clean tail bounds).

[1]: https://renyi.hu/~p_erdos/1988-22.pdf "https://renyi.hu/~p_erdos/1988-22.pdf"
[2]: https://www.erdosproblems.com/latex/1051 "https://www.erdosproblems.com/latex/1051"
[3]: https://www.erdosproblems.com/forum/thread/1051 "https://www.erdosproblems.com/forum/thread/1051"
