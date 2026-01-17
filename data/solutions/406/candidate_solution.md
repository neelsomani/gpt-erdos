This is a famous **open problem** (often called the **Erdős ternary digits problem / conjecture**).

If an integer has only digits $0$ and $1$ in base $3$, then it is a sum of **distinct powers of $3$**:
$
2^n=\sum_{j} 3^{m_j}\qquad (m_0<m_1<\cdots).
$
The known examples are

* (2^0=1=(1)_3)
* (2^2=4=(11)_3)
* (2^8=256=(100111)_3=3^5+3^2+3+1).

Erdős conjectured that these are **the only** powers of $2$ whose ternary expansion uses only $0$s and $1$s, i.e.
$
\\{n:\text{the base-3 expansion of }2^n\text{ has no digit }2\\}=\\{0,2,8\\},
$
and in particular that there are only **finitely many** such powers. ([arXiv][1])

As of the most reliable published/standard references, this conjecture is **still unproved**—and even the weaker statement “there are only finitely many such $n$” is described as “widely open” in expository sources. ([CIRM Math][2])

What *is* known is very strong computational evidence: Saye (2022) verified Erdős’s conjecture for all exponents
[
n \le 2\cdot 3^{45}\approx 5.9\times 10^{21},
]
finding no examples beyond (n=0,2,8). ([Cheriton School of Computer Science][3])

So: **it’s conjectured to be true, but not known.**

[1]: https://arxiv.org/abs/math/0512006 "[math/0512006] Ternary expansions of powers of 2"
[2]: https://www.cirm-math.fr/RepOrga/2077/Slides/Stoll.pdf "On a problem of Erdos concerning the digits of 2n in base 3 – and Hensel's lemma"
[3]: https://cs.uwaterloo.ca/journals/JIS/VOL25/Saye/saye3.html "
On Two Conjectures Concerning the Ternary Digits of Powers of Two
"
