This is Erdős’s “simultaneous rational Ahmes series” problem (#265). Two key points are known now:

### 1) It can grow at least polynomially (explicit example)

David Cantor observed that taking
[
a_n=\binom{n}{2}=\frac{n(n-1)}2 \qquad (n\ge 3)
]
works. ([Erdős Problems][1])

Indeed,
[
\sum_{n=3}^\infty \frac1{a_n}
=\sum_{n=3}^\infty \frac{2}{n(n-1)}
=2\sum_{n=3}^\infty\Bigl(\frac1{n-1}-\frac1n\Bigr)
=2\cdot\frac12=1,
]
and
[
\sum_{n=3}^\infty \frac1{a_n-1}
=\sum_{n=3}^\infty \frac{1}{\frac{n(n-1)}2-1}
=\sum_{n=3}^\infty \frac{2}{n(n-1)-2}
=\sum_{n=3}^\infty \frac{2}{(n-2)(n+1)}.
]
Using partial fractions
[
\frac{2}{(n-2)(n+1)}=\frac{2}{3}\Bigl(\frac1{n-2}-\frac1{n+1}\Bigr),
]
so the series telescopes to
[
\sum_{n=3}^\infty \frac1{a_n-1}
=\frac{2}{3}\Bigl(1+\frac12+\frac13\Bigr)=\frac{11}{9}.
]

So (a_n) can grow as slowly as (O(n^2)) and still satisfy the condition.

### 2) It cannot grow faster than “doubly exponential” (upper bound)

Already from the single requirement that (\sum 1/a_n) is rational, one has a well-known obstruction: if (a_n) grows *faster than* (C^{2^n}) for every fixed (C>1) [[nomath]](equivalently $\lim a_n^{1/2^n}=\infty$)[[/nomath]], then (\sum 1/a_n) is necessarily irrational. ([What's new][2])

So your situation cannot occur with growth faster than doubly exponential in $n$.

### 3) And it *can* grow doubly exponentially (existence, recent progress)

Kovač and Tao (2024) proved that such sequences exist with **double exponential growth**: for some (\beta>1) there is a strictly increasing integer sequence ((a_n)) such that
[
\lim_{n\to\infty} a_n^{1/\beta^n}=\infty
]
and simultaneously
[
\sum_{n=1}^\infty \frac{1}{a_n+j}\in\mathbb{Q}\quad \text{for } j=0,1,\dots,d-1
]
[[nomath]](in particular for $d=2$)[[/nomath]]. ([arXiv][3])

For your exact shift ((a_n-1)), just apply their (d=2) result to a sequence ((b_n)) with (\sum 1/b_n) and (\sum 1/(b_n+1)) rational, and set (a_n=b_n+1). Then (\sum 1/a_n) and (\sum 1/(a_n-1)) are both rational.

### What’s still open about the “fastest possible” rate

While “faster than doubly exponential” is impossible and “some doubly exponential” is possible, it remains open whether one can reach the *critical* (2^n)-scale in the strongest sense, e.g.
[
\limsup_{n\to\infty} a_n^{1/2^n}>1.
]
This is exactly the remaining gap noted on the Erdős problems page. ([Erdős Problems][1])

So, in current terms:

* **Impossible:** super–doubly-exponential growth (e.g. (\lim a_n^{1/2^n}=\infty)). ([What's new][2])
* **Possible:** doubly-exponential growth [[nomath]](there exist sequences with $a_n \approx \exp(\beta^n)$-type behaviour, in the sense $a_n^{1/\beta^n}\to\infty$)[[/nomath]]. ([arXiv][3])
* **Still open:** whether one can push it up to have (\limsup a_n^{1/2^n}>1). ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/265 "
  
    Erdős Problem #265
  
"
[2]: https://terrytao.wordpress.com/2024/11/27/on-several-irrationality-problems-for-ahmes-series/ "On several irrationality problems for Ahmes series | What's new"
[3]: https://arxiv.org/pdf/2406.17593 "On several irrationality problems for Ahmes series"
