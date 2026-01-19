Not known in full generality.

Write the condition “the product is a perfect power” as the Diophantine equation
[
n(n+d)\cdots(n+(k-1)d)=y^\ell,\qquad \ell>1,
]
with (\gcd(n,d)=1) and (k\ge 4).

What is known is strongly consistent with the answer “no”:

* For $k=3$ there **are** infinitely many coprime progressions with a perfect power (in fact a square): the Pell-equation method gives infinitely many $(n,d)$ with (\gcd(n,d)=1) such that $n(n+d)(n+2d)$ is a square. ([Erdős Problems][1])
  [[nomath]](This is why the question becomes interesting starting at $k\ge 4$.)[[/nomath]]

* For the special case $d=1$ (consecutive integers), Erdős–Selfridge proved that a product of consecutive positive integers is **never** a perfect power. ([Springer][2])

* For general $d$ with (\gcd(n,d)=1), Győry–Hajdu–Pintér proved that for every $k$ with
  [
  3<k<35\quad(\text{i.e. }4\le k\le 34),
  ]
  the product (n(n+d)\cdots(n+(k-1)d)) **cannot** be a perfect power. ([Cambridge University Press & Assessment][3])
  So for all lengths (k=4,5,\dots,34) the answer is definitively **no**.

Beyond that range, the existence of any example with (k\ge 35) [[nomath]](still with $\gcd(n,d)=1$ and all terms positive)[[/nomath]] remains an **open problem**; Erdős conjectured the answer is always “no.” ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/672 "
  
    Erdős Problem #672
  
"
[2]: https://link.springer.com/article/10.1007/s00605-020-01422-7 "Polynomial values of products of terms from an arithmetic progression | Monatshefte für Mathematik | Springer Nature Link"
[3]: https://www.cambridge.org/core/journals/compositio-mathematica/article/perfect-powers-from-products-of-consecutive-terms-in-arithmetic-progression/AABF84B6AEDB5FF9A80D357180CE837D "Perfect powers from products of consecutive terms in arithmetic progression | Compositio Mathematica | Cambridge Core"
