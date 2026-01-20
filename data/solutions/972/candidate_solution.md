This is **open in general** for a fixed irrational (\alpha>1).

It is listed as **Erdős Problem #972** and marked **OPEN**: “Let (\alpha>1) be irrational. Are there infinitely many primes $p$ such that (\lfloor p\alpha\rfloor) is also prime?” ([erdosproblems.com][1])  (Terence Tao comments there that it “looks comparable in difficulty to the twin prime conjecture.”) ([erdosproblems.com][2])

### What *is* known

There is a strong **“metric”** $almost-everywhere$ result: Li and Pan (2008) consider the more general conjecture

[
\text{infinitely many primes }p\text{ such that }\lfloor \alpha p+\beta\rfloor\text{ is prime,}
]

and prove it for **almost all** irrational (\alpha) (in the sense of Lebesgue measure), with a quantitative lower bound:
[
\limsup_{x\to\infty} \pi^*_{\alpha,\beta}(x),\frac{(\log x)^2}{x} \ge 1,
]
where $\pi^*_{\alpha,\beta}(x)=|\\{p\le x:\ p \text{ and } \lfloor \alpha p+\beta\rfloor \text{ are prime}\\}|$. ([ar5iv][3])

In particular, taking (\beta=0), this implies that for **almost every** irrational (\alpha>1), there are infinitely many primes $p$ with (\lfloor \alpha p\rfloor) prime.

### Bottom line

* **For a specific given irrational (\alpha>1):** no proof is known in general; the problem is open. ([erdosproblems.com][1])
* **For “almost all” irrational (\alpha):** yes, infinitely many such primes exist (Li–Pan). ([ar5iv][3])

[1]: https://www.erdosproblems.com/972 "
  
    Erdős Problem #972
  
"
[2]: https://www.erdosproblems.com/forum/discuss/972 "

    Erdős Problem #972 - Discussion thread

"
[3]: https://ar5iv.org/abs/0803.1740 "[0803.1740] Primes in the form ⌊⁢+⌋"
