No.

Here is a concrete construction that already forces a **second term of order (n/\log n)** [[nomath]](so it cannot be pushed down to order $n/(\log n)^2$)[[/nomath]].

## A large valid set for $k=3$

Let $n$ be large and define
$
A := {\text{primes } \le n}\cup{pq\le n:\ p\le \sqrt n<q,\ p,q \text{ primes}}.
$
So $A$ consists of **all primes**, plus **semiprimes with one prime factor (>\sqrt n)**.

### Claim: every $m$ has (<3) representations (m=a_1a_2) with (a_1<a_2\in A).

Any composite element of $A$ is of the form (pq) with (q>\sqrt n), so it has a **unique** prime factor (>\sqrt n).

Now consider a representation $m=ab$ with (a<b\in A). There are only three types:

1. **prime (\times) prime**: unique by unique factorization.

2. **prime (\times) semiprime**: write the semiprime as (pQ) with (Q>\sqrt n).
   Then (m = r\cdot pQ).
   If (r\le \sqrt n), then $Q$ is the unique prime factor (>\sqrt n) in $m$, so the only possible semiprimes in $A$ dividing $m$ are (pQ) and (rQ), giving at most the two representations
   [
   m=(pQ)\cdot r \quad\text{and}\quad m=(rQ)\cdot p
   ]
   [[nomath]](if both semiprimes happen to be in $A$)[[/nomath]].
   If (r>\sqrt n), then $m$ has two primes (>\sqrt n), namely $r$ and $Q$, and again you can only “attach” the small prime $p$ to one of them, giving at most two representations:
   [
   m=r\cdot(pQ)\quad \text{or}\quad m=Q\cdot(pr),
   ]
   and (pr\in A) because (r>\sqrt n) and (p\le \sqrt n).

3. **semiprime (\times) semiprime**: write them as (pQ) and (rS) with (Q,S>\sqrt n).
   Then
   [
   m=(pQ)(rS)=prQS.
   ]
   Any factor in $A$ dividing $m$ that is composite must contain exactly one of (Q,S), so the only possible pairings are
   [
   (pQ)(rS)\quad\text{and}\quad(pS)(rQ),
   ]
   i.e. at most **two** representations.

So $A$ is admissible for $k=3$, hence
[
g_3(n)\ge|A|.
]

## Size of this $A$

Let (\pi(n)) be the number of primes (\le n), and (\pi_2(n)) the number of semiprimes (\le n) (product of two primes, allowing equality).

The set ({pq\le n:\ p\le \sqrt n<q}) contains **all semiprimes except those with both prime factors (\le \sqrt n)**, and the excluded ones are at most (O(\pi(\sqrt n)^2)=O(n/(\log n)^2)). Thus
[
|A|=\pi(n)+\pi_2(n)-O\left(\frac{n}{(\log n)^2}\right).
]

Now, a precise two-term asymptotic for (\pi_2(x)) is known:
[
\pi_2(x)=\frac{x\log\log x}{\log x} + M\frac{x}{\log x} + o\left(\frac{x}{\log x}\right),
]
where (M\approx 0.261497\ldots) is the Meissel–Mertens constant. ([Colgate Math][1])
Also (\pi(x)\sim x/\log x). ([Colgate Math][1])

Therefore this construction gives
[
g_3(n)\ge\frac{n\log\log n}{\log n}+(1+M+o(1))\frac{n}{\log n}.
]

## Conclusion

Your proposed expansion
[
g_3(n)=\frac{n\log\log n}{\log n} + (c+o(1))\frac{n}{(\log n)^2}
]
cannot be true, because (g_3(n)) is already (\ge \frac{n\log\log n}{\log n} + \Theta\big(\frac{n}{\log n}\big)).

A more plausible “next term” (at least as a **lower bound**) is of order (n/\log n), and the construction above specifically gives the coefficient $(1+M)$ in front of (n/\log n).

If you want, I can also outline what one would need for an upper bound of the form
[
g_3(n)\le \pi(n)+\pi_2(n)+o\left(\frac{n}{\log n}\right),
]
which would essentially pin down the true second-order term.

[1]: https://math.colgate.edu/~integers/v122/v122.pdf "https://math.colgate.edu/~integers/v122/v122.pdf"
