Let (f_n(z)=\sum_{k=0}^n \epsilon_k z^k) with i.i.d. (\epsilon_k\in{-1,1}), and let (R_n) be the number of zeros in ({|z|\le 1}).

What **is known** is the following (this was Hayman’s Problem 4.15):

* Oren Yakir proved that for a random Littlewood polynomial (P(z)=\sum_{k=0}^{n-1}X_k z^k) (same model, just indexed slightly differently), if (\nu_n(\mathbb D)) denotes the number of zeros in the **open** unit disk (\mathbb D={|z|<1}), then
  [
  \mathbb P\Big(\big|\nu_n(\mathbb D)-\tfrac n2\big|>n^{9/10}\Big)\to 0,
  ]
  and in particular (\nu_n(\mathbb D)/n\to \tfrac12) **in probability**. 

* He also notes (using a result of Konyagin–Schlag) that the probability of having any zero **on** the unit circle tends to $0$:
  [
  \mathbb P\big(\nu_n({|z|=1})>0\big)\to 0.
  ]

  So counting zeros in (|z|\le 1) vs (|z|<1) makes no asymptotic difference **in probability**.

Translating this to your notation (degree shift by 1 is negligible), the upshot is:

[
\frac{R_n}{n}\to \frac12\quad\text{in probability,}
]
equivalently (\frac{R_n}{n/2}\to 1) **in probability**.

---

### About “almost surely”

Yakir’s theorem is explicitly **in probability**, not almost sure.   In fact, his proof yields only a polynomially small error probability at the (n^{9/10}) deviation scale [[nomath]](one sees a bound of order $n^{-1/10}(\log n)^2$ in the argument)[[/nomath]], which is not summable in $n$ and so does **not** immediately upgrade to an a.s. statement via Borel–Cantelli. 

I did not find a reference that proves the stronger a.s. convergence
[
\frac{R_n}{n}\to \frac12\quad\text{a.s.}
]
for Littlewood/Rademacher coefficients.

So: **the “half the roots” law is proved in probability**, but the **almost sure** version is not (at least not from the currently standard published results around this problem).
