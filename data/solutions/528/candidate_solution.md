Write (c_n=f(n,k)) for the number of $n$-step self–avoiding walks (SAWs) in (\mathbb Z^k) starting at the origin.

## 1) The limit exists

Take any $(m+n)$-step SAW (\omega=(\omega_0,\omega_1,\dots,\omega_{m+n})) with (\omega_0=0). Split it at time $m$:

* the prefix $(\omega_0,\dots,\omega_m)$ is an $m$-step SAW from the origin;
* the suffix $(\omega_m,\omega_{m+1},\dots,\omega_{m+n})$, translated by (-\omega_m), becomes an $n$-step SAW from the origin.

Thus each ((m+n))-step SAW determines a **pair** $(\text{prefix},\text{translated suffix})\in {\text{SAWs of length }m}\times{\text{SAWs of length }n}$, and this mapping is injective. Hence
[
c_{m+n}\le c_m,c_n \qquad (m,n\ge 0).
]
So (\log c_n) is subadditive. By Fekete’s lemma,
[
\lim_{n\to\infty}\frac1n\log c_n=\inf_{n\ge 1}\frac1n\log c_n,
]
and therefore
[
C_k=\lim_{n\to\infty}c_n^{1/n}
]
**exists**, and equals
[
C_k=\inf_{n\ge 1} c_n^{1/n}.
]
This constant (C_k) is the **connective constant** (\mu(\mathbb Z^k)). ([MathWorld][1])

## 2) Trivial exact case: $k=1$

In (\mathbb Z), a SAW cannot ever reverse direction (it would revisit a point), so for every (n\ge1) there are exactly two SAWs: all steps $+1$ or all steps $-1$. Thus (c_n=2) and
[
C_1=\lim_{n\to\infty}2^{1/n}=1.
]

[[nomath]](If you allow $k=0$, then $c_n=0$ for $n\ge1$, so $C_0=0$.)[[/nomath]]

## 3) General bounds [[nomath]](all $k\ge 1$)[[/nomath]]

Two simple estimates give
[
k^n \le c_n \le 2k(2k-1)^{n-1}\qquad (n\ge1),
]
hence
[
k \le C_k \le 2k-1.
]
Reason:

* lower bound: walks using only the $k$ positive coordinate directions are monotone and hence self-avoiding;
* upper bound: $2k$ choices for the first step, and thereafter you can’t step back to the immediately previous vertex, so at most $2k-1$ choices each time. ([MathWorld][1])

## 4) What is known for (k\ge 2)?

For (\mathbb Z^k) with (k\ge2), **no closed form is known** for (C_k); determining it exactly is a major open problem. ([Institut Henri Poincaré][2])

What we do have are high-precision **numerical estimates** (and also rigorous upper/lower bounds). For example:

* $k=2$ (square lattice):
  [
  C_2 \approx 2.63815853032790(3).
  ]
  ([arXiv][3])
* $k=3$ (simple cubic):
  [
  C_3 \approx 4.684039931(27).
  ]
  ([arXiv][4])
* (k=4,5,6,7,8) (hypercubic), estimates reported (among others) include
  [
  \begin{aligned}
  C_4&\approx 6.774043(5),\
  C_5&\approx 8.838544(3),\
  C_6&\approx 10.878094(4),\
  C_7&\approx 12.902817(3),\
  C_8&\approx 14.919257(2).
  \end{aligned}
  ]
  ([Webspace][5])

## Conclusion

[
\boxed{,C_k=\lim_{n\to\infty} f(n,k)^{1/n}\ \text{ exists for every }k\ge1,\ \text{and is the connective constant }\mu(\mathbb Z^k).,}
]
Moreover (C_1=1), and for (k\ge2) it is not known exactly (only bounds and numerical estimates are available). ([Institut Henri Poincaré][2])

[1]: https://mathworld.wolfram.com/Self-AvoidingWalkConnectiveConstant.html "Self-Avoiding Walk Connective Constant -- from Wolfram MathWorld"
[2]: https://www.ihes.fr/~duminil/publi/saw_lecture_notes.pdf "saw.dvi"
[3]: https://arxiv.org/abs/1607.02984?utm_source=chatgpt.com "On the growth constant for square-lattice self-avoiding walks"
[4]: https://arxiv.org/pdf/1302.2106?utm_source=chatgpt.com "Calculation of the connective constant for self-avoiding ..."
[5]: https://webspace.maths.qmul.ac.uk/t.prellberg/papers/pub035.pdf "d:\\"
