This is **not known** in full generality. It’s an **Erdős conjecture** (often listed as “Erdős Problem #11”): for every **odd** integer (n>1), there should exist an integer (k\ge 0) such that
[
n = s + 2^k
]
with $$s$$ **squarefree**. 

What *is* known is strong computational evidence:

* Odlyzko checked the conjecture for all odd (n\le 10^7), and McCranie extended this to (1.4\times 10^9) (as reported in later literature). 
* Much more recently, Christian Hercher verified it for **all odd (n<2^{50}\approx 1.12\times 10^{15})**. 
  Moreover, in that entire range, every such (n) had a representation with a **small** power of two: (1\le k\le 13) (so (2^k\le 8192)). 

Why people believe it’s true: squarefree integers have positive density ((6/\pi^2\approx 0.608)), so among the (\sim \log_2 n) candidates (n-2^k) one expects many to be squarefree. Hercher also computes (heuristically) that the probability that *none* of (n-2^1,\dots,n-2^6) is squarefree is already tiny ((\approx 2.7\times 10^{-7})). 

There’s also a nontrivial theoretical connection to **Wieferich primes**: Granville–Soundararajan showed the conjecture is strongly related to how often primes (p) satisfy (p^2\mid (2^{p-1}-1)), i.e. Wieferich-type behavior, and Hercher summarizes that the conjecture would imply infinitely many primes are **not** Wieferich primes. ([Springer][1])

So the current state is: **widely believed true, verified up to (2^{50}), but still an open problem.** ([Erdős Problems][2])

[1]: https://link.springer.com/content/pdf/10.1007/978-1-4757-4507-8_17 "A Binary Additive Problem of Erdős and the Order of 2 mod p 2 | Springer Nature Link (formerly SpringerLink)"
[2]: https://www.erdosproblems.com/11 "
  
    Erdős Problem #11
  
"
