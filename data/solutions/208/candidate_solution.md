Both inequalities are **open unconditionally**. What is known is (roughly) that we can prove only **power–type** upper bounds on the maximal gap, while Erdős already proved in 1951 that gaps of the size in your second display occur infinitely often (so if an upper bound of that form is true, the constant would be best possible). ([Erdős Problems][1])

---

## 1) The “(s_n^\varepsilon)” bound

Let (s_1<s_2<\dots) be the squarefree numbers, and write
[
G(x):=\max{s_{n+1}-s_n:\ s_n\le x}.
]
Your first question is equivalent to (G(x)\ll_\varepsilon x^\varepsilon) for every (\varepsilon>0).

### Conditional result (ABC)

This **does follow from the abc conjecture**: Granville showed that (s_{n+1}-s_n\ll_\varepsilon s_n^\varepsilon) for all (\varepsilon>0) assuming abc. ([Erdős Problems][1])

### Best unconditional results (as of the cited literature)

Unconditionally, the best theorems are much weaker:

* Filaseta–Trifonov proved that there is a constant (c>0) such that for all sufficiently large (x), the interval
  [
  (x,\ x+c,x^{1/5}\log x]
  ]
  contains a squarefree integer. In particular this gives
  [
  s_{n+1}-s_n \ll s_n^{1/5}\log s_n.
  ]
  ([people.math.sc.edu][2])

* Pandey (2024) improved the exponent $1/5$: he proves that there exists (\eta>0) such that intervals of length (X^{1/5-\eta}) always contain squarefrees for large $X$, and in fact obtains an asymptotic formula for the count of squarefrees in such intervals. This implies an unconditional gap bound
  [
  s_{n+1}-s_n \ll s_n^{1/5-\eta}
  ]
  for some (ineffective/unspecified) (\eta>0). 

So the “(s_n^\varepsilon)” bound is **known conditionally (abc)** and **wide open unconditionally**. ([Erdős Problems][1])

---

## 2) The (\frac{\pi^2}{6}\frac{\log s_n}{\log\log s_n}) bound

This is also open, and it is essentially the sharp form of the problem.

### Erdős’s 1951 lower bound (showing sharpness of the constant)

Erdős proved that there are infinitely many (n) such that
[
s_{n+1}-s_n > (1+o(1))\frac{\pi^2}{6}\frac{\log s_n}{\log\log s_n}.
]
So any upper bound of the same shape cannot have a smaller leading constant. ([Erdős Problems][1])

(In fact this is recorded already in Erdős’s 1951 paper as inequality (20), together with his speculation that the matching upper bound might hold. )

### Status of the matching upper bound

No method currently comes close to proving
[
s_{n+1}-s_n \le (1+o(1))\frac{\pi^2}{6}\frac{\log s_n}{\log\log s_n}
]
(or even (O(\log s_n))); the best unconditional upper bounds remain of the form (s_n^{1/5-\eta}) as above. ([Erdős Problems][1])

Erdős later commented that perhaps (s_{n+1}-s_n\ll \log s_n), but he was “very doubtful”. ([Erdős Problems][1])

---

## A small numerical/data point

Kumchev–McCormick–McNew–Park–Scherr–Ziehr (2024) discuss explicit versions of the Filaseta–Trifonov bound and note that computational work up to (10^{18}) finds maximum gaps that are tiny compared with current theoretical upper bounds [[nomath]](e.g. a longest gap of length 18 up to $10^{18}$)[[/nomath]]. ([TigerWeb][3])

---

### Bottom line

* **First inequality:** open unconditionally; **true under abc**. ([Erdős Problems][1])
* **Second inequality:** open; Erdős proved the corresponding **lower bound with the same constant** infinitely often, so if true it would be best possible. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/208 "
  
    Erdős Problem #208
  
"
[2]: https://people.math.sc.edu/filaseta/papers/squarefreepaper.pdf "https://people.math.sc.edu/filaseta/papers/squarefreepaper.pdf"
[3]: https://tigerweb.towson.edu/akumchev/a46.pdf "https://tigerweb.towson.edu/akumchev/a46.pdf"
