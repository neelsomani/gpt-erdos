Write the squarefree indicator as (\mu^2(n)), so
[
Q(x)=\sum_{n\le x}\mu^2(n).
]
Use the standard identity
[
\mu^2(n)=\sum_{d^2\mid n}\mu(d),
]
because if $n$ has a squared prime factor then the sum cancels to $0$, and if $n$ is squarefree then only $d=1$ contributes.

Then
[
Q(x)=\sum_{n\le x}\ \sum_{d^2\mid n}\mu(d)
=\sum_{d^2\le x}\mu(d)\sum_{\substack{n\le x\ d^2\mid n}}1
=\sum_{d\le \sqrt x}\mu(d)\\\lfloor \frac{x}{d^2}\\\rfloor.
]
Now split off the main term by replacing (\lfloor x/d^2\rfloor) with (x/d^2):
[
Q(x)=\sum_{d\le\sqrt x}\mu(d)\left(\frac{x}{d^2}+O(1)\right)
= x\sum_{d\le\sqrt x}\frac{\mu(d)}{d^2}+O!\left(\sum_{d\le\sqrt x}1\right).
]
The error from the floors is $O(\sqrt x)$.

For the main sum,
[
\sum_{d\le\sqrt x}\frac{\mu(d)}{d^2}
=\sum_{d=1}^\infty\frac{\mu(d)}{d^2}+O\left(\sum_{d>\sqrt x}\frac1{d^2}\right)
=\frac{1}{\zeta(2)}+O!\left(\frac1{\sqrt x}\right)
=\frac{6}{\pi^2}+O!\left(\frac1{\sqrt x}\right).
]
Multiplying by $x$ gives an additional $O(\sqrt x)$ contribution. Putting everything together,
[
Q(x)=\frac{6}{\pi^2}x + O(\sqrt x).
]

So the error term has order of magnitude
[
E(x)=O\left(x^{1/2}\right).
]
