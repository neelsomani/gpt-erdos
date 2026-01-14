This is **still open** (as of the last publicly curated status updates in late 2025).

Let
[
A={,n\ \text{odd}:\ n\neq p+2^k+2^\ell\ \text{for all primes }p\text{ and }k,\ell\ge 0,}.
]
The question is whether the **upper asymptotic density**
[
\overline d(A)=\limsup_{x\to\infty}\frac{|A\cap[1,x]|}{x}
]
is (>0).

### What is known

* **Infinitely many exceptions exist.**
  Roger Crocker proved in 1971 that there are infinitely many positive odd integers **not** representable as “prime + two powers of 2” (his Theorem I). ([MSP][1])

* **The exceptional set is very large in a quantitative sense, but still not known to have positive density.**
  Hao Pan (Acta Arith. 2011; preprint 2009) proved a strong lower bound of the shape
  [
  |A\cap[1,x]|\ \gg\ x\exp!\left(-C\log x\cdot\frac{\log\log\log\log x}{\log\log\log x}\right),
  ]
  which in particular implies
  [
  |A\cap[1,x]|\gg_\varepsilon x^{1-\varepsilon}\quad\text{for every }\varepsilon>0.
  ]

  This is (x^{1-o(1)}), but it still allows (|A\cap[1,x]|/x\to 0), so it does **not** settle whether (\overline d(A)>0).

* **The specific density question remains open in the Erdős problem lists.**
  The Erdős Problems Project lists exactly your question as **OPEN** and summarizes the above progress (Crocker; Pan) while noting that positive upper density is not known. ([Erdős Problems][2])

### Bottom line

No proof is known either that (\overline d(A)>0) **or** that (\overline d(A)=0). The best unconditional results show (A) is infinite and quite large ((\gg x^{1-\varepsilon})), but a **positive proportion** is still out of reach. ([Erdős Problems][2])

[1]: https://msp.org/pjm/1971/36-1/pjm-v36-n1-p09-p.pdf "On the sum of a prime and of two powers of two"
[2]: https://www.erdosproblems.com/9 "
  
    Erdős Problem #9
  
"
