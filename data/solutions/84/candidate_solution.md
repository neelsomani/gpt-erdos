Let (f(n)) be the number of sets (A\subseteq{3,\dots,n}) that occur as the **cycle set** of some graph on (n) vertices.

## 1) Proof that (f(n)=o(2^n))

A result of Nenadov (improving an earlier bound of Verstraëte) says that there is a function (\varepsilon(n)\to 0) such that
[
f(n)\ \le\ 2^{,n - n^{1/2-\varepsilon(n)}} .
]
([Erdős Problems][1])

Divide by (2^n):
[
\frac{f(n)}{2^n}\ \le\ 2^{-,n^{1/2-\varepsilon(n)}}.
]
Since (n^{1/2-\varepsilon(n)}\to\infty), the right-hand side tends to (0). Hence
[
\frac{f(n)}{2^n}\to 0,
]
which is exactly (f(n)=o(2^n)).

That finishes the first part. ([Erdős Problems][1])

---

## 2) About (\displaystyle \frac{f(n)}{2^{n/2}}\to\infty)

### What we can prove easily: (f(n)\ge 2^{\lfloor n/2\rfloor})

This is Faudree’s lower-bound construction (often stated for even (n); odd (n) is similar).

Assume (n) is even. Label vertices (1,2,\dots,n) and start with the path
[
1-2-3-\cdots-n.
]
Now pick any subset
[
S\subseteq\left{\frac n2+1,\frac n2+2,\dots,n\right}.
]
For each (a\in S), add the chord edge ({1,a}).

Call the resulting graph (G_S). Then:

* For every (a\in S), the edge ({1,a}) together with the path (1-2-\cdots-a) gives a cycle of length exactly (a).
* Any cycle of length (>\frac n2) must use exactly one chord ({1,a}), and then it is forced to be that same “path + chord” cycle. In particular,
  [
  C(G_S)\cap\left{\frac n2+1,\dots,n\right} = S.
  ]

So different choices of (S) give different cycle sets. Since there are (2^{n/2}) choices of (S), we get
[
f(n)\ \ge\ 2^{n/2}.
]
This is the standard “(2^{n/2})” lower bound. ([arXiv][2])

### Why the limit-to-infinity claim is not currently settled in the literature

The statement
[
\frac{f(n)}{2^{n/2}}\to\infty
]
is exactly the second part of Erdős problem #84 as stated on the Erdős Problems site. The page explicitly lists it under an **OPEN** problem, and only records the known lower bound (2^{n/2}) (Faudree) and the upper bounds proving (f(n)=o(2^n)). ([Erdős Problems][1])

Also, Nenadov’s paper (which gives the best known upper bound) states that the best known lower bound is still Faudree’s (2^{n/2}), and notes that even an exponential improvement (2^{(1+c)n/2}) would be very interesting. This strongly suggests there is no published proof known there for any significant strengthening of the (2^{n/2}) lower bound (and in particular the (\omega(1)) factor asked here is not recorded as solved). ([arXiv][2])

So, at the level of currently documented results:

* First part (f(n)=o(2^n)): **proved** (Verstraëte, improved by Nenadov). ([Erdős Problems][1])
* Second part (f(n)/2^{n/2}\to\infty): **still open** as stated there. ([Erdős Problems][1])

---

### Summary

* (f(n)=o(2^n)) follows immediately from the known upper bound (f(n)\le 2^{n-n^{1/2-o(1)}}). ([Erdős Problems][1])
* The best standard general lower bound is (f(n)\ge 2^{n/2}) (Faudree’s construction). ([arXiv][2])
* The stronger claim (f(n)/2^{n/2}\to\infty) is listed as open in the standard reference for this Erdős problem. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/84 "
  
    Erdős Problem #84
  
"
[2]: https://arxiv.org/html/2501.09904v2 "Improved bound on the number of cycle sets"
