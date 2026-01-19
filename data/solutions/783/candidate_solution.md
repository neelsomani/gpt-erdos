Let
[
U_A(n):=|\\{m\le n:\ \forall a\in A,\ a\nmid m\\}|
]
be the number you want to **minimise**.

## 1) For pairwise coprime $A$, the problem is essentially a product minimisation

Write (A={a_1,\dots,a_k}) with ((a_i,a_j)=1) for (i\ne j). Consider a “random” integer $m$. The events “(a_i\mid m)” behave like independent congruence conditions because the moduli are coprime (Chinese remainder theorem intuition). In particular, the *natural density* of integers not divisible by any (a_i) is
[
\prod_{i=1}^k \\(1-\frac1{a_i}\\).
]
For the kind of extremisers that are relevant here [[nomath]](they have $k=O(1)$ or at worst $k\ll \log\log n$)[[/nomath]], one can turn this into an asymptotic
[
U_A(n)=n\prod_{a\in A}\\(1-\frac1a\\)+o(n),
]
so **minimising (U_A(n))** is, for large $n$, the same as **minimising**
[
P(A):=\prod_{a\in A}\\(1-\frac1a\\)
\quad\text{subject to}\quad
\sum_{a\in A}\frac1a\le C.
]

So the combinatorial question becomes:

> choose pairwise coprime $a$’s with (\sum 1/a\le C) to make (\prod(1-1/a)) as small as possible.

## 2) Why “many huge primes near $n$” is the wrong shape

If all chosen $a$’s are very large, then $1/a$ is tiny, and you get the approximation
[
\log\\(1-\frac1a\\)=-\frac1a+O\\(\frac1{a^2}\\),
]
hence
[
\log P(A)
=\sum_{a\in A}\log\\(1-\frac1a\\)
=-\sum_{a\in A}\frac1a + O\\(\sum_{a\in A}\frac1{a^2}\\).
]
If your set is made of primes all (\gg n^\alpha) [[nomath]](which is what happens in your “descending primes from $n$” construction for fixed $C$)[[/nomath]], then (\sum 1/a^2) is negligible, so
[
P(A)\approx \exp\\(-\sum_{a\in A}\frac1a\\)\approx e^{-C}.
]

That is: your strategy produces uncovered proportion (\approx e^{-C}).

But you can do **strictly better** by spending some of the “reciprocal budget” on *small* moduli, because
[
\log\\(1-\frac1a\\)=-\frac1a-\frac1{2a^2}-\frac1{3a^3}-\cdots,
]
and for small $a$ the extra negative terms (\frac1{2a^2}+\cdots) are **not** negligible. Intuitively: a unit of budget spent at $a=2$ decreases the product more than the same unit of budget spent spread across enormous primes.

## 3) Concrete counterexample to the “largest primes” proposal

Take $C=1$ and $n$ very large.

* Your proposal [[nomath]](largest primes downwards until $\sum 1/p\le 1$)[[/nomath]] gives
  [
  P(A)\approx e^{-1}\approx 0.368.
  ]
* But take instead
  [
  A={2,3,7,43}.
  ]
  These are pairwise coprime and
  [
  \frac12+\frac13+\frac17+\frac1{43}=\frac{1805}{1806}<1.
  ]
  The uncovered density is
  [
  P(A)=\\(1-\frac12\\)\\(1-\frac13\\)\\(1-\frac17\\)\\(1-\frac1{43}\\)
  =\frac12\cdot\frac23\cdot\frac67\cdot\frac{42}{43}
  =\frac{84}{301}\approx 0.279.
  ]
  So for large $n$,
  [
  U_A(n)\approx 0.279,n,
  ]
  which is **far smaller** than (\approx 0.368,n). Hence your “descending primes from $n$” choice is **not** optimal.

[[nomath]](And you can continue ${2,3,7,43,1807,\dots}$ to push it a tiny bit further.)[[/nomath]]

## 4) What does an optimal $A$ look like?

The right heuristic is:

* You want (\sum_{a\in A}\frac1a) to be as close to $C$ as the constraints allow [[nomath]](otherwise you can add another coprime $a$ and strictly decrease $P(A)$)[[/nomath]].
* For fixed total (\sum 1/a), the product (\prod(1-1/a)) is pushed down by making the reciprocals $1/a$ as **uneven / concentrated** as possible [[nomath]](because $\log(1-x)$ is concave)[[/nomath]].

That leads to a very natural “coprime Egyptian-fraction greedy” construction:

### C**oprime greedy algorithm**

Let (r_0=C) and (M_0=1). For (j=1,2,\dots):

* choose (a_j) to be the **smallest integer** such that
  [
  a_j\ge \frac1{r_{j-1}},\qquad (a_j,M_{j-1})=1;
  ]
  equivalently, (1/a_j\le r_{j-1}) and (a_j) is minimal subject to being coprime to the previously chosen ones.
* update (r_j=r_{j-1}-1/a_j) and (M_j=M_{j-1}a_j).
* stop when you can’t add another (a\le n) [[nomath]](for large $n$ this typically happens only when $r_j<1/n$, i.e. the leftover budget is too tiny to spend)[[/nomath]].

For $C=1$ this produces the classical Sylvester sequence
[
2,\ 3,\ 7,\ 43,\ 1807,\ \dots
]
because at each step the remainder is exactly (1/M_{j-1}), so the smallest coprime integer (\ge M_{j-1}) is (M_{j-1}+1).

### Why this is the right “shape”

This procedure always tries to spend the remaining reciprocal budget on the **single smallest available** modulus that doesn’t violate coprimality. That is exactly the direction you want if your goal is to minimise (\prod(1-1/a)): a small modulus gives you a big $1/a$, and big $1/a$ is disproportionately effective at shrinking the product.

I’m not claiming here a fully formal uniqueness theorem [[nomath]](“this greedy set is *the* unique minimiser for every $C$ and every $n$”)[[/nomath]], because discrete effects [[nomath]](and the “$\le n$” cutoff when $n$ is not astronomically large relative to $C$)[[/nomath]] can create ties or tiny adjustments. But:

* it gives the *correct extremal phenomenon* (few small moduli, then rapidly growing ones), and
* it decisively beats the “largest primes near $n$” strategy already for $C=1$ [[nomath]](and similarly for other $C$)[[/nomath]].

## 5) Bottom line

* Your proposed choice (A={q_1,\dots,q_k}) with (q_i) the largest primes (\le n) is **not** optimal in general.
* For large $n$, an optimal (or essentially optimal) $A$ is obtained by taking **as small coprime moduli as possible**, i.e. a coprime-greedy Egyptian-fraction type set [[nomath]](Sylvester-type for $C=1$)[[/nomath]], not by taking a huge block of primes near $n$.

If you tell me a specific value of $C$ [[nomath]](say $C=0.7$, $1$, $2$, etc.)[[/nomath]], I can write down the first few terms of the coprime-greedy $A$ explicitly and compute the resulting product (\prod(1-1/a)) to show the resulting uncovered proportion.
