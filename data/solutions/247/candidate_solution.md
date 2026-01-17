This is **not known in general**. It is an **open problem of Erdős** (often listed as Erdős Problem #247). ([Erdős Problems][1])

What *is* known:

* Erdős proved the sum is **transcendental** under a **much stronger growth condition**, namely that
  [
  \limsup_{n\to\infty}\frac{a_n}{n^t}=\infty \quad \text{for every } t\ge 1,
  ]
  [[nomath]](so $a_n$ eventually beats every power of $n$)[[/nomath]]. ([Erdős Problems][1])

* There are also “gap” conditions that imply transcendence using Diophantine approximation theorems (Roth/Ridout style arguments). Roughly: if the exponents jump fast enough, then truncating the binary expansion gives **too-good rational approximations** for an algebraic irrational, forcing transcendence. ([MathOverflow][2])
  But your hypothesis (\limsup a_n/n=\infty) does **not** force such big jumps [[nomath]](for example $a_n\approx n\log n$ already makes $a_n/n\to\infty$ while $a_{n+1}/a_n\to 1$)[[/nomath]].

* Erdős also remarked that even proving weaker statements [[nomath]](like: if $a_n>c n^2$ then the sum is **not** a root of any quadratic polynomial)[[/nomath]] seemed hard. ([Erdős Problems][1])

So the best honest answer is:

**With only** (\displaystyle \limsup \frac{a_n}{n}=\infty), it is **currently open** whether
(\displaystyle \sum_{n=1}^\infty 2^{-a_n}) must be transcendental. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/latex/247 "
  
    Erdős Problems
  
"
[2]: https://mathoverflow.net/questions/41609/have-all-numbers-with-sufficiently-many-zeros-been-proven-transcendental "nt.number theory - Have all numbers with \"sufficiently many zeros\" been proven transcendental? - MathOverflow"
