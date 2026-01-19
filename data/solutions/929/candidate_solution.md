I’m going to read “$n+i$ is divisible by primes (\le x)” as: **each** (n+1,\dots,n+k) has **at least one** prime divisor (\le x) [[nomath]](equivalently, none of them is coprime to the primorial $\prod_{p\le x}p$)[[/nomath]]. Under that interpretation, your $S(k)$ is essentially the inverse of the **primorial Jacobsthal function**.

## 1) Reformulation via the primorial and Jacobsthal’s function

Let
[
P(x):=\prod_{p\le x} p
]
[[nomath]](the primorial up to $x$)[[/nomath]]. Then
[
(\exists,p\le x: p\mid (n+i))\quad\Longleftrightarrow\quad \gcd(n+i,,P(x))>1.
]
So your condition is
[
\gcd(n+1,P(x))>1,;\gcd(n+2,P(x))>1,;\dots,;\gcd(n+k,P(x))>1.
]

Crucially, this depends only on (n \bmod P(x)). Hence:

* either there is **no** such $n$, giving density $0$;
* or there is at least one residue class (n\equiv a\pmod{P(x)}) that works, giving a **positive density** set [[nomath]](density $\ge 1/P(x)$)[[/nomath]].

So “positive density” is equivalent to “there exists at least one solution residue class.”

Now recall Jacobsthal’s function $j(m)$: it is the **maximal gap between consecutive integers coprime to $m$**. For primorials, Ford–Green–Konyagin–Tao note that

> (j(P(x))) is “1 plus the longest string of consecutive integers, each divisible by some prime (p\le x).” ([Annals of Mathematics][1])

Therefore, your $S(k)$ is exactly the inverse relation
[
S(k)=\min\\{x: j(P(x))\ge k+1\\}.
]

Equivalently, in the Ford–Green–Konyagin–Tao notation, define $Y(x)$ to be the largest $y$ such that one can choose residue classes (a_p\bmod p) for each prime (p\le x) that **cover** $[1,y]$. ([Annals of Mathematics][1])
Then $Y(x)$ is the “maximal interval length you can sieve out using primes (\le x),” and it is “intimately related” to $j(P(x))$. ([Annals of Mathematics][1])
In particular, $S(k)$ is essentially (\min{x:Y(x)\ge k}).

## 2) Best unconditional bounds [[nomath]](translated into $S(k)$)[[/nomath]]

### (A) Upper bound for $j(P(x))$ (\Rightarrow) lower bound for $S(k)$

Ford–Green–Konyagin–Tao state that the **best known upper bound** for this covering function is
[
Y(x)\ \ll\ x^2,
]
coming from Iwaniec’s work on Jacobsthal’s function. ([Annals of Mathematics][1])

Since (k\le Y(S(k))\ll S(k)^2), this gives the unconditional lower bound
[
S(k)\ \gg\ \sqrt{k}.
]

This is (essentially) the strongest general lower bound currently available “for free” from the literature quoted in the prime gaps papers.

### (B) Lower bounds for (j(P(x)))  (\Rightarrow) upper bounds for $S(k)$

A classical lower bound (Pintz) quoted by Hagedorn is
[
j(P(x)) \ge (2e^\gamma+o(1)),x\log x,\frac{\log_3 x}{(\log_2 x)^2},
]
where (\log_2 x=\log\log x), (\log_3 x=\log\log\log x). 

Ford–Green–Konyagin–Tao prove a stronger “arbitrarily large constant” version for the covering function $Y(x)$:
[
Y(x) ;>; R,x\log x,\frac{\log_3 x}{(\log_2 x)^2}
\quad\text{for any fixed }R>0\text{ and all sufficiently large }x. ([Annals of Mathematics][1])
(So (Y(x)) grows faster than any fixed multiple of that base expression.)

Inverting even the Pintz-form bound gives an unconditional *upper* bound of the shape
[
S(k)\ \ll\ \frac{k}{\log k}\cdot \frac{(\log_2 k)^2}{\log_3 k}
\qquad (k\to\infty),
]
up to constants [[nomath]](and with the usual “$\log$” meaning natural log)[[/nomath]].

So unconditionally we currently have a wide bracket:
[
\boxed{\ \sqrt{k}\ \ll\ S(k)\ \ll\ \frac{k}{\log k}\cdot \frac{(\log_2 k)^2}{\log_3 k}\ }.
]

In particular, this shows $S(k)$ is **at most** (k^{1-o(1)}), but does not prove any comparable **lower** bound.

## 3) About the specific question (S(k)\ge k^{1-o(1)})

To get (S(k)\ge k^{1-o(1)}), you’d need an upper bound on the maximal coverable length $Y(x)$ [[nomath]](or $j(P(x))$)[[/nomath]] of the form
[
Y(x)\ \le\ x^{1+o(1)} \quad\text{(or even } x(\log x)^{O(1)}\text{)}.
]
But the **best known** general upper bound in this framework is only (Y(x)\ll x^2) (Iwaniec). ([Annals of Mathematics][1])
So, **unconditionally**, the statement (S(k)\ge k^{1-o(1)}) is not currently proved (at least not from the standard Jacobsthal-function technology referenced in the prime gaps literature).

### What is conjectured / expected?

Ford–Green–Konyagin–Tao also record the **Maier–Pomerance conjecture**:
[
Y(x)\ \ll\ x(\log x)^{2+o(1)}. ([Annals of Mathematics][1])
If you assume this conjecture, then inverting gives
[
S(k)\ \gg\ \frac{k}{(\log k)^{2+o(1)}} = k^{1-o(1)},
]
so the answer would be **yes** (and in fact stronger than your inequality).

## 4) Bottom line

* Your $S(k)$ is [[nomath]](up to the $+1$)[[/nomath]] the inverse of the **primorial Jacobsthal function** $j(P(x))$, or equivalently the inverse of the “covering length” function $Y(x)$. ([Annals of Mathematics][1])
* Best unconditional bounds currently give
  [
  \sqrt{k}\ \ll\ S(k)\ \ll\ \frac{k}{\log k}\cdot \frac{(\log_2 k)^2}{\log_3 k}.
  ]
  [[nomath]](Upper bound from Pintz / Ford–Green–Konyagin–Tao; lower bound from Iwaniec’s $Y(x)\ll x^2$.)[[/nomath]] ([Annals of Mathematics][1])
* The claim (S(k)\ge k^{1-o(1)}) is **not known unconditionally** from these results; it **would follow** from the Maier–Pomerance conjectural upper bound (Y(x)\ll x(\log x)^{2+o(1)}). ([Annals of Mathematics][1])

If you tell me whether you want an **unconditional best-known bound summary** or also a more detailed **heuristic** [[nomath]](random model for reduced residues mod $P(x)$)[[/nomath]] explaining why one expects $Y(x)$ to be only (x\log^{O(1)}x), I can expand in that direction.

[1]: https://annals.math.princeton.edu/wp-content/uploads/annals-v183-n3-p04-p.pdf "Large gaps between consecutive prime numbers"
