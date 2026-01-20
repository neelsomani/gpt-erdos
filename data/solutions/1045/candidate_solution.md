This question (in essentially this exact form) goes back to Erdős–Herzog–Piranian, and as of late 2025 the **exact maximum is not known in general**. What *is* known is:

* the value of (\Delta) for the “regular $n$-gon” configuration;
* that the regular polygon is **not** always optimal [[nomath]](already false for $n=4$, and in fact for all even $n\ge 4$)[[/nomath]];
* fairly nontrivial upper and lower bounds on the true maximum. ([Erdős Problems][1])

Below I’ll spell these out.

---

## 1) Regular $n$-gon value [[nomath]](scaled to diameter $2$)[[/nomath]]

Write
$
\Delta(z_1,\dots,z_n)=\prod_{i\ne j}|z_i-z_j|
=(\prod_{1\le i<j\le n}|z_i-z_j|)^2.
$

Let (\omega_k=e^{2\pi i k/n}). A standard Vandermonde computation gives
$
\prod_{1\le i<j\le n}|\omega_i-\omega_j|=n^{n/2}.
$
If we take points on a circle of radius $R$, i.e. $z_k=R\omega_k$, then every distance scales by $R$, so
$
\prod_{i<j}|z_i-z_j|=R^{\binom n2},n^{n/2}
\quad\Rightarrow\quad
\Delta = R^{n(n-1)},n^n.
$

Now impose **diameter (\le 2)**:

* **If $n$ is even**, the regular $n$-gon has opposite vertices, so the diameter is (2R). To make the diameter $2$ you take $R=1$. Hence
  [
  \Delta_{\text{reg}}(n)=n^n\qquad(n\ \text{even}).
  ]

* **If $n$ is odd**, there are no opposite vertices; the largest chord subtends angle (\pi-\frac{\pi}{n}), so the diameter is (2R\cos\big(\frac{\pi}{2n}\big)). Setting this equal to $2$ gives (R=\sec(\pi/2n)). Hence
  [
  \Delta_{\text{reg}}(n)=n^n\sec(\pi/2n)^{,n(n-1)}
  =n^n,\cos(\pi/2n)^{-n(n-1)}
  \qquad(n\ \text{odd}),
  ]
  and asymptotically (\Delta_{\text{reg}}(n)\sim e^{\pi^2/8}n^n). ([Erdős Problems][1])

These match the values quoted on the Erdős problems page. ([Erdős Problems][1])

---

## 2) Is the maximum achieved by a regular polygon?

### No for even (n\ge 4) [[nomath]](explicitly false already for $n=4$)[[/nomath]]

A concrete counterexample for $n=4$ is
[
z_1=0,\quad z_2=\sqrt3+i,\quad z_3=\sqrt3-i,\quad z_4=2.
]
All pairwise distances are (\le 2), and one computes
[
\Delta(z_1,z_2,z_3,z_4)=4096,(2-\sqrt3)^2\approx 294.08,
]
whereas the regular square [[nomath]](diameter $2$)[[/nomath]] has (\Delta=4^4=256). So the regular quadrilateral is **not** optimal. ([Erdős Problems][2])

Moreover, it is now known that **for every even (n\ge 4)**, the regular $n$-gon is not a maximiser [[nomath]](there are systematic perturbations that increase $\Delta$)[[/nomath]]. ([Erdős Problems][1])

### Odd $n$: still plausible, but not proved in general

For odd $n$, the regular $n$-gon gives the larger value
(\Delta_{\text{reg}}(n)=n^n\cos(\pi/2n)^{-n(n-1)}),
and as of the late‑2025 status update it **remains possible** that this is actually maximal for all odd $n$; no general proof is known. ([Erdős Problems][1])

---

## 3) So what *is* the maximum?

### In general: unknown, but bounded between explicit lower/upper bounds

Let (\Delta_{\max}(n)) be the maximum of (\Delta) over all $n$-tuples with (|z_i-z_j|\le 2).

* **Upper bound (Pommerenke)**: there is an exponential-in-$n$ factor bound of the shape
  [
  \Delta_{\max}(n)\ \le\ 2^{O(n)}n^n,
  ]
  and a concrete bound stated in the recent note is
  (\Delta_{\max}\le 2^{4(n-1)}n^n). ([Erdős Problems][1])

* **Lower bounds**:

  * Regular polygon gives (\Delta_{\text{reg}}(n)) as above. ([Erdős Problems][1])
  * For **even** $n$, we now know (\Delta_{\max}(n)) is *asymptotically* larger than (n^n) by a fixed constant factor (>1): one proven result is
    [
    \liminf_{\substack{n\to\infty\ n\ \mathrm{even}}}\frac{\Delta_{\max}(n)}{n^n}\ \ge\ 1.0378\ldots
    ]
    and subsequent constructions reach constants about (1.26853) for all even $n$, and about (1.304457) along multiples of $6$. ([Erdős Problems][1])

So at present, the best honest answer is:

* the **exact** value of (\Delta_{\max}(n)) is open in general;
* the **regular polygon is not optimal for even (n\ge 4)**;
* for **odd $n$**, the regular polygon value is a natural candidate and remains unrefuted, but is not proved to be optimal. ([Erdős Problems][1])

---

If you tell me a specific $n$ you care about [[nomath]](say $n=5,6,8$)[[/nomath]], I can also compute (\Delta_{\text{reg}}(n)) explicitly and compare it to the best known counterexamples/constructions for that $n$ from the current literature.

[1]: https://www.erdosproblems.com/1045 "
  
    Erdős Problem #1045
  
"
[2]: https://www.erdosproblems.com/forum/thread/1045 "

    Erdős Problem #1045 - Discussion thread

"
