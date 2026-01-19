This is **not known** in general — it’s an **open problem of Erdős**.

It appears explicitly as **Erdős Problem #683** (last edited Dec 31, 2025 on the Erdős Problems website), asking whether there exists an absolute constant (c>0) such that for all (1\le k\le n),
[
P\left(\binom{n}{k}\right)\ \ge\ \min!\bigl(n-k+1,\ k^{1+c}\bigr),
]
where $P(m)$ denotes the largest prime divisor of $m$. ([Erdős Problems][1])

### What *is* known (partial results)

* **Sylvester–Schur theorem (classical):** if (n\ge 2k) [[nomath]](equivalently $k\le n/2$)[[/nomath]], then (\binom{n}{k}) has a prime divisor (>k). ([MSP][2])
  So in that common range one always has
  [
  P\left(\binom{n}{k}\right) > k,
  ]
  but that is far weaker than (k^{1+c}).

* **Erdős (1955):** Erdős proved a stronger lower bound (still much smaller than a power):
  [
  P\left(\binom{n}{k}\right)\ \gg\ k\log k\qquad (k\le n/2),
  ]
  for some absolute implied constant. ([Erdős Problems][1])

* The same Erdős Problems page notes that **heuristics** (based on prime gaps) suggest the largest prime factor should typically be *much* larger [[nomath]](even something like $>e^{c\sqrt{k}}$ for $k\le n/2$)[[/nomath]], but this is **not proved**. ([Erdős Problems][1])

So: the proposed inequality with a fixed exponent gain (k^{1+c}) for all (n,k) remains **open**.

[1]: https://www.erdosproblems.com/tags/binomial%20coefficients/no "
  
    Erdős Problems
  
"
[2]: https://msp.org/pjm/1969/29-2/pjm-v29-n2-p04-p.pdf "On prime divisors of the binomial coefficient"
