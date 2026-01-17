Not known in general.

* If you allow **(n=1)**, then it is **false**: (\sigma(1)=1), so (\sigma_k(1)=1) for all $k$ and (\sigma_k(1)^{1/k}=1).

* For every **fixed (n>1)**, the question
  [
  \lim_{k\to\infty}\sigma_k(n)^{1/k}\stackrel{?}{=}\infty
  ]
  is a well-known **open problem of Erdős** (Erdős problem #410). ([Erdős Problems][1])

This is exactly statement (iii) in the list of six questions on iterating (\sigma) discussed by Cohen & te Riele (1996), where they say (following Erdős et al.) that they could not prove or disprove it, but provide computational evidence supporting it. 

### What evidence/heuristics suggest

* Cohen & te Riele computed large iterates for many starting values $n$ and found behavior consistent with
  [
  \big(\sigma_k(n)\big)^{1/k}\ \text{growing at least on the order of }\ \log k,
  ]
  based on their normalization (h(n)=\frac{(\sigma_m(n))^{1/m}}{\log m}) staying around a constant (\approx 1.1) in the data they could reach. 

* For the specific orbit starting at $2$, the OEIS entry for (a(k+1)=\sigma(a(k))) records the conjecture
  [
  \frac12\log k < \frac{a(k+1)}{a(k)} < 2\log k,
  ]
  which (if true) would imply (a(k)^{1/k}\asymp \log k\to\infty). ([OEIS][2])

So the consensus seems to be: **very plausibly true for (n>1), but currently unproved.** ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/410 "
  
    Erdős Problem #410
  
"
[2]: https://oeis.org/A007497 "A007497 - OEIS"
