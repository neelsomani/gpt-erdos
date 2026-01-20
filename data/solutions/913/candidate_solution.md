Let (v_p(m)) be the exponent of $p$ in $m$. Since (\gcd(n,n+1)=1),
[
v_p(n(n+1))=\begin{cases}
v_p(n),&p\mid n,[2pt]
v_p(n+1),&p\mid n+1.
\end{cases}
]
So “all exponents in $n(n+1)$ are distinct” is **equivalent** to

* the exponents in the prime factorization of $n$ are all distinct,
* the exponents in the prime factorization of $n+1$ are all distinct,
* and **no exponent occurs in both** $n$ and $n+1$.

In other words, $n$ and $n+1$ must both be “special numbers” (OEIS A130091: integers whose prime-factor exponents are all distinct), and their exponent-sets must be disjoint. ([OEIS][1])

There are plenty of examples:
[
\begin{aligned}
8\cdot 9&=2^3\cdot 3^2,\
24\cdot 25&=2^3\cdot 3^1\cdot 5^2,\
63\cdot 64&=2^6\cdot 3^2\cdot 7^1,\
2400\cdot 2401&=(2^5\cdot 3^1\cdot 5^2)\cdot 7^4,
\end{aligned}
]
so (n=8,24,63,2400) work, etc.

## But is it known that there are infinitely many such $n$?

As far as what’s currently in the literature around “special numbers”, there is **no known proof** (and no known disproof) that there are infinitely many such $n$. The condition forces $n$ and $n+1$ to be consecutive “special numbers” with an extra disjointness constraint, and questions about *consecutive* special numbers are treated as nontrivial and tied to deeper conjectural territory (OEIS mentions links to the ABC conjecture in the study of runs of consecutive special numbers). ([OEIS][1])

What *is* known is that special numbers themselves are infinite and have counting function (\sim c,x/\log x) for some (c>1) (Aktaş–Murty), and there is **no run of 24 consecutive** special numbers (so they’re sparse enough that “twin-like” questions are subtle). ([OEIS][1])

## Conditional observations

If one assumes conjectures about primes in very sparse sequences, then infinitude would follow. For example:

* If there are infinitely many **Mersenne primes** (2^p-1), then taking (n=2^p-1) gives
  [
  n(n+1)=(2^p-1)\cdot 2^p,
  ]
  whose exponents are $\\{1,p\\}$, hence distinct. (But infinitude of Mersenne primes is open.)
* More generally, infinitely many primes $q$ with $q-1$ having distinct exponents all (\ne 1) would also give infinitely many (n=q-1), etc.

## Bottom line

There are many $n$ with the required property, but **whether there are infinitely many is (as far as I can tell from the existing “special numbers” literature) an open problem**. ([OEIS][1])

[1]: https://oeis.org/A130091 "A130091 - OEIS"
