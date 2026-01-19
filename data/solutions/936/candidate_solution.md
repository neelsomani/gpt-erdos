Let “powerful” mean **squarefull**: a positive integer $m$ such that for every prime (p\mid m) we also have (p^2\mid m).

## What’s known unconditionally

### Factorial (n!\pm 1)

Already the **much more special** question “when is (n!+1) a square?” is the classical **Brocard–Ramanujan (Brocard’s) problem**:
[
n!+1=x^2.
]
Only three solutions are known:
[
(n,x)=(4,5),(5,11),(7,71),
]
i.e.
[
4!+1=25,\quad 5!+1=121,\quad 7!+1=5041,
]
and this problem is still unsolved [[nomath]](and computations up to $n=10^9$ found no further solutions)[[/nomath]]. ([MathWorld][1])

Since “powerful” includes “square,” this immediately tells you: **we can’t even prove finiteness for the square case**, so we certainly can’t prove (unconditionally) that (n!+1) is powerful only finitely often.

For (n!-1), there is no comparable classical classification; in particular, nothing known that would settle your “powerful” finiteness question.

### Exponential (2^n\pm 1)

Even for Mersenne numbers (2^n-1), the much weaker question “infinitely many are squarefree?” is open. A repeated prime factor is tied to Wieferich-type congruences, and the general problem is considered very hard for such thin sequences. ([MathOverflow][2])

So, again, your “powerful” question (which is vastly stronger than “not squarefree”) is **open** unconditionally.

**Bottom line (unconditional):** as of current knowledge, there is **no proof** that any of the four sequences (2^n\pm1), (n!\pm1) are powerful only finitely often. The situation is open, and in the factorial “(+1)” case it contains a famous open problem as a special case. ([MathWorld][1])

## What you can prove assuming the abc conjecture

Here is a clean conditional statement:

> **Assuming the abc conjecture, each of** (2^n-1), (2^n+1), (n!-1), (n!+1) **is powerful for only finitely many $n$.**

Recall the abc conjecture in the form: for every (\varepsilon>0) there is (K_\varepsilon) such that if (a,b,c) are coprime positive integers with (a+b=c), then
[
c< K_\varepsilon\mathrm{rad}(abc)^{1+\varepsilon},
]
where (\mathrm{rad}(m)) is the product of the **distinct** primes dividing $m$. ([Wikipedia][3])

### Key observation: powerful (\Rightarrow) small radical

If $M$ is powerful, every prime divisor occurs with exponent (\ge2), so
[
M \ge \prod_{p\mid M} p^2 = \mathrm{rad}(M)^2,
]
hence
[
\mathrm{rad}(M)\le \sqrt{M}.
]

### Case 1: (2^n-1)

Assume (2^n-1) is powerful. Apply abc to
[
(2^n-1)+1=2^n,
]
with (\gcd(2^n-1,1,2^n)=1). Then
[
\mathrm{rad}( (2^n-1)\cdot 1 \cdot 2^n) = 2,\mathrm{rad}(2^n-1)\le 2\sqrt{2^n-1}<2^{n/2+1}.
]
So abc gives
[
2^n < K_\varepsilon \left(2^{n/2+1}\right)^{1+\varepsilon}
=K_\varepsilon,2^{(n/2+1)(1+\varepsilon)}.
]
Taking base-2 logs,
[
n < \log_2 K_\varepsilon + (n/2+1)(1+\varepsilon).
]
For any fixed (\varepsilon<1), the coefficient of $n$ on the right is ((1+\varepsilon)/2<1), so this inequality forces **$n$ to be bounded**. Hence only finitely many $n$.

### Case 2: (2^n+1)

Assume (2^n+1) is powerful and apply abc to
[
2^n+1 = 2^n + 1
]
[[nomath]](i.e. $a=2^n$, $b=1$, $c=2^n+1$)[[/nomath]]. Again (\gcd(2^n,1,2^n+1)=1) and
[
\mathrm{rad}(2^n\cdot 1 \cdot (2^n+1)) = 2,\mathrm{rad}(2^n+1)\le 2\sqrt{2^n+1}<2^{n/2+3/2}.
]
abc gives
[
2^n+1 < K_\varepsilon,2^{(n/2+3/2)(1+\varepsilon)},
]
which similarly forces $n$ to be bounded [[nomath]](again pick $\varepsilon<1$)[[/nomath]].

### Case 3: $n!+1$ and $n!-1$

Do $n!+1$; the $-1$ case is analogous.

Assume $n!+1$ is powerful and apply abc to
$
n!+1 = n! + 1,
$
so $a=n!$, $b=1$, $c=n!+1$.

We need an upper bound on (\mathrm{rad}(n!)). Since
[
\mathrm{rad}(n!)=\prod_{p\le n} p,
\quad\text{and}\quad
\sum_{p\le n}\log p \le \pi(n)\log n,
]
using the (explicit) Chebyshev-type upper bound (\pi(n)\le \tfrac32 \frac{n}{\log n}) for (n\ge2), we get
[
\log \mathrm{rad}(n!) \le \pi(n)\log n \le \tfrac32,n,
\quad\text{so}\quad
\mathrm{rad}(n!) \le e^{\frac32 n}.
]
[[nomath]](The quoted $\pi(n)$ bound appears in the standard “Chebyshev refinement” form.)[[/nomath]] ([Colgate Math][4])

Also (\mathrm{rad}(n!+1)\le \sqrt{n!+1}) by “powerful (\Rightarrow \mathrm{rad}\le\sqrt{\cdot})”.

Hence
[
\mathrm{rad}(n!\cdot 1\cdot (n!+1))
\le \mathrm{rad}(n!)\mathrm{rad}(n!+1)
\le e^{\frac32 n},\sqrt{n!+1}.
]
abc gives, for any (\varepsilon>0),
[
n!+1 < K_\varepsilon \left(e^{\frac32 n}\sqrt{n!+1}\right)^{1+\varepsilon}.
]
Taking logs and using Stirling’s bounds for $n!$ (also recorded in the same source) ([Colgate Math][4]),
[
\log(n!) \sim n\log n
]
while the right-hand side contributes at most
[
(1+\varepsilon)\left(\tfrac32 n + \tfrac12\log(n!) + O(1)\right)
= (1+\varepsilon)\left(\tfrac12\log(n!)\right) + O(n).
]
Thus, for any fixed (\varepsilon<1), the (\log(n!)) term on the right has coefficient (\tfrac{1+\varepsilon}{2}<1), so for large $n$ this is impossible. Therefore **$n$ is bounded**, i.e. only finitely many solutions.

The exact same abc logic applies to $n!-1$ via $(n!-1)+1=n!$.

## Summary

* **Unconditionally:** these finiteness questions are **open** in general; in particular, the factorial “$+1$” case subsumes the unsolved Brocard–Ramanujan problem. ([MathWorld][1])
* **Assuming the abc conjecture:** **yes**, each of (2^n\pm1) and (n!\pm1) can be powerful for **only finitely many $n$**, by comparing abc’s radical bound with (\mathrm{rad}(M)\le\sqrt M) for powerful $M$. ([Wikipedia][3])

If you want, I can also spell out what the abc-based inequalities give as an explicit (though very ineffective) upper bound on $n$ in each of the four cases.

[1]: https://mathworld.wolfram.com/BrocardsProblem.html "https://mathworld.wolfram.com/BrocardsProblem.html"
[2]: https://mathoverflow.net/questions/425552/square-free-mersenne-numbers "https://mathoverflow.net/questions/425552/square-free-mersenne-numbers"
[3]: https://en.wikipedia.org/wiki/Abc_conjecture "https://en.wikipedia.org/wiki/Abc_conjecture"
[4]: https://math.colgate.edu/~integers/z71/z71.pdf "https://math.colgate.edu/~integers/z71/z71.pdf"
