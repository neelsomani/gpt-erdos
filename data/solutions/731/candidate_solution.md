Let
[
M(n):=\min{m\ge 2:\ m\nmid \binom{2n}{n}}.
]

### 1) Reduce to prime powers

Write (v_p(\cdot)) for the $p$-adic valuation. If (m\nmid \binom{2n}{n}), then for some prime (p\mid m) we have (v_p(m)>v_p!\binom{2n}{n}). Hence
[
p^{,v_p\left(\binom{2n}{n}\right)+1}\nmid \binom{2n}{n},
\qquad\text{and}\qquad
p^{,v_p\left(\binom{2n}{n}\right)+1}\le m.
]
So the *least* nondivisor must actually be a prime power, and in fact
[
M(n)=\min_{p\ \text{prime}} p^{,v_p\left(\binom{2n}{n}\right)+1}.
]
For “typical” $n$, this minimum is almost always attained already at exponent $1$, i.e. $M(n)$ is (typically) the **least prime** $p$ with (p\nmid \binom{2n}{n}). [[nomath]](The cases where a small square like $9$ or $25$ wins have density $0$ as $n\to\infty$.)[[/nomath]]

So it is natural to focus on the least prime $p$ such that (p\nmid \binom{2n}{n}).

### 2) Kummer’s theorem gives a digit condition

Kummer’s theorem says
[
v_p!\binom{2n}{n}=\text{(number of carries when adding }n+n\text{ in base }p).
]
In particular, for an odd prime $p$,
[
p\nmid \binom{2n}{n}
\iff v_p!\binom{2n}{n}=0
\iff \text{no carries in }n+n\text{ (base }p).
]
“No carries” for doubling is equivalent to **every base-$p$ digit of $n$ being (\le (p-1)/2)**. So among integers (n<p^k), the count with (p\nmid \binom{2n}{n}) is exactly (((p+1)/2)^k). Hence for $n$ of size (\asymp x) with (k\approx \log_p x),
[
\mathbb P\\(p\nmid \binom{2n}{n}\\)
\approx \left(\frac{p+1}{2p}\right)^{\log_p x}
\approx \left(\frac12\right)^{\log_p x}
= x^{-\log_p 2}
= \exp!\left(-(\ln 2),\frac{\ln x}{\ln p}\right).
]
Call this “failure probability” (q_p(x)).

### 3) Heuristic for the first failing prime

Treating the events ({p\nmid \binom{2n}{n}}) as roughly independent across primes (a standard “random model” heuristic), the least failing prime should occur when the **expected number** of failing primes up to $y$ is about $1$:
[
\sum_{p\le y} q_p(x)\ \approx\ 1.
]
Since (q_p(x)) increases with $p$, the sum is dominated by primes near $y$, giving the crude but effective approximation
[
\sum_{p\le y} q_p(x)
\approx \pi(y), q_y(x)
\approx \frac{y}{\ln y},
\exp!\left(-(\ln 2),\frac{\ln x}{\ln y}\right).
]
Set this (\approx 1), put (L=\ln x), (t=\ln y), so (y=e^t). The equation becomes
[
\frac{e^t}{t}\exp!\left(-(\ln 2)\frac{L}{t}\right)\approx 1
\quad\Longleftrightarrow\quad
t-\ln t-(\ln 2)\frac{L}{t}\approx 0.
]
Solving asymptotically gives
[
t=\sqrt{(\ln 2)L}+\frac14\ln\big((\ln 2)L\big)+o(1).
]
Exponentiating,
[
y
= \exp(t)
\sim \big((\ln 2)L\big)^{1/4}\exp\big(\sqrt{(\ln 2)L}\big).
]

Taking $x$ comparable to $n$ [[nomath]](so $L=\ln n$)[[/nomath]] suggests the **normal size** of $M(n)$ is
[
\boxed{
f(n):=\big((\ln 2)\ln n\big)^{1/4}
\exp\Big(\sqrt{(\ln 2)\ln n}\Big).
}
]

Equivalently, in logarithmic form,
[
\boxed{
\ln M(n)=\sqrt{(\ln 2)\ln n}+\frac14\ln\ln n+O(1)
\qquad\text{(typically)}.
}
]

### What this means in practice

* For almost all $n$, $M(n)$ is **a prime** and sits around the scale $f(n)$ above.
* The most robust “normal order” statement (and the one that is easiest to justify from Kummer + counting) is
  [
  \ln M(n)\sim \sqrt{(\ln 2),\ln n},
  ]
  i.e.
  [
  M(n)=\exp!\big((1+o(1))\sqrt{(\ln 2),\ln n}\big).
  ]
* The extra factor (\big((\ln 2)\ln n\big)^{1/4}) comes from the prime density (\pi(y)\sim y/\ln y) in the “first-failure” heuristic.

So a very reasonable choice is
[
\boxed{f(n)=\big((\ln 2)\ln n\big)^{1/4}\exp!\big(\sqrt{(\ln 2)\ln n}\big).}
]

[[nomath]](If you want the cleanest expression capturing the main growth: $f(n)=\exp(\sqrt{(\ln 2)\ln n})$ already gets the dominant scale.)[[/nomath]]