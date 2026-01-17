As of **January 16, 2026**, this is **not known**: the existence of such a sequence $A$ with
[
\lim_{n\to\infty}\frac{a_{n+1}}{a_n}=2
]
and with the property that **for every cofinite subsequence** (A'\subseteq A), the finite subset-sum set
[
P(A')=\\{\sum_{n\in B} n : B\subseteq A'\ \text{finite}\\}
]
has **(natural) density $1$**, is an **open problem** (it is listed as Erdős Problem #347). ([Erdős Problems][1])

### Related context (what *is* known)

* There is a **stronger** “robust completeness” phenomenon known at **slower growth**: in a 1964 paper, Graham proved that the sequence
  [
  s_n = F_n - (-1)^n
  ]
  [[nomath]](with $F_n$ Fibonacci)[[/nomath]] has the property that **deleting any finite subsequence** leaves a sequence whose subset sums contain **all sufficiently large integers** (i.e., it remains *complete* after any finite deletion). ([fq.math][2])
  But this sequence grows like (\varphi^n) [[nomath]](golden ratio $\varphi\approx 1.618$)[[/nomath]], not like (2^n), so it does **not** answer your ( \lim a_{n+1}/a_n=2 ) question.

* There are also **near-miss constructions**: Terence Tao posted a sketch of a construction where the growth ratio is **very close to $2$** [[nomath]](of the form $2 - O(2^{-k})$ for large fixed $k$)[[/nomath]] and the subset sums of tails give density $1$; he notes that upgrading this to a true **limit (=2)** would require letting parameters vary with $n$, and that this is not carried out in that sketch. ([Erdős Problems][3])

So the best honest answer right now is: **we don’t know** whether such an $A$ exists (and no counterexample is known either). ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/347 "
  
    Erdős Problem #347
  
"
[2]: https://www.fq.math.ca/Scanned/2-1/graham.pdf "fq1964.pdf"
[3]: https://www.erdosproblems.com/forum/thread/347 "

    Erdős Problem #347 - Discussion thread

"
