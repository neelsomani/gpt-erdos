What you wrote is **exactly the classical Erdős–Turán angular discrepancy bound**, except that in the known theorem the parameter under the square root is the **degree** $d$, not the **number $n$ of nonzero coefficients**.

### What is known (true)

Let
[
f(z)=a_0+a_1z+\cdots+a_d z^d,\qquad a_0a_d\neq 0,
]
and let (z_1,\dots,z_d) be its roots with arguments (\theta_i\in[0,2\pi)). Define the angular counting function
[
N(I):=|\\{i:\theta_i\in I\\}|.
]
Then Erdős–Turán proved (and many later authors sharpened constants) that for every interval (I\subset[0,2\pi)),
[
\\|N(I)-\frac{|I|}{2\pi}d\\|
\le C,\sqrt{,d,\log\\(\frac{|f|*{\infty,|z|=1}}{\sqrt{|a_0a_d|}}\\)}\quad
\text{for an absolute constant }C,
]
where (|f|*{\infty,|z|=1}=\max_{|z|=1}|f(z)|). ([Numdam][1])

Since (\max_{|z|=1}|f(z)|\le \sum_{k=0}^d |a_k|), this immediately implies the same bound with your
[
M=\frac{|a_0|+\cdots+|a_d|}{\sqrt{|a_0a_d|}}
]
in place of (|f|_{\infty}/\sqrt{|a_0a_d|}):
[
\\|N(I)-\frac{|I|}{2\pi}d\\|;\ll;\sqrt{d\log M}.
]
This is the standard “Erdős–Turán theorem on the distribution of arguments of zeros.” ([Erdős Problems][2])

[[nomath]](There is also substantial work on sharpening the *constant* $C$, including a short Fourier-analytic proof by Soundararajan and later work giving sharp constants. $[ar5iv][3]$)[[/nomath]]

### Your question [[nomath]](replace $d$ by $n$)[[/nomath]]

Replacing $d$ by $n$, the number of nonzero coefficients, is **not known in general**.

This is an Erdős question (often cited in the form you wrote), and as of the current literature it is treated as **open**: Erdős–Turán proved the bound with $d$ in place of $n$, but whether one can generally strengthen it to (\sqrt{n\log M}) is unresolved. ([Erdős Problems][2])

### Related partial directions

There are results showing **extra regularity** (beyond the baseline Erdős–Turán scale) under additional hypotheses—e.g. Steinerberger relates angular clustering at finer scales to how often an associated trigonometric polynomial changes sign / has real zeros, which can be relevant in “fewnomial-like” situations. But this does **not** settle the general (\sqrt{n\log M}) replacement. ([ar5iv][4])

---

So:

* **Yes**, with $n$ replaced by **$d$** (degree): this is the classical Erdős–Turán bound (and refinements). ([ar5iv][3])
* **With $n$ = number of nonzero coefficients**, the asserted bound is (to the best of current knowledge) an **open problem**. ([Erdős Problems][2])

[1]: https://www.numdam.org/item/AIF_1996__46_5_1275_0.pdf "https://www.numdam.org/item/AIF_1996__46_5_1275_0.pdf"
[2]: https://www.erdosproblems.com/990 "
  
    Erdős Problem #990
  
"
[3]: https://ar5iv.org/pdf/1802.06506 "https://ar5iv.org/pdf/1802.06506"
[4]: https://ar5iv.org/abs/1903.09079 "https://ar5iv.org/abs/1903.09079"
