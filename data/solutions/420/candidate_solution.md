Write (k=\lfloor f(n)\rfloor) and (F_k(n):=\dfrac{\tau((n+k)!)}{\tau(n!)}).  This is exactly the quantity studied by Erdős–Graham–Ivić–Pomerance [[nomath]](they write $d(\cdot)$ for $\tau(\cdot)$)[[/nomath]]. ([Erdős Problems][1])

A key point is that (F_k(n)) is controlled by how “large” the prime factors of the integers (n+1,\dots,n+k) are.  EGIP introduce
[
S(m)=\text{sum of the prime factors of }m\text{ counted with multiplicity},
]
and prove the very useful two–sided bound
[
1+\frac{S(m)}{2m}\ \le\ \frac{\tau(m!)}{\tau((m-1)!)}\ \le\ 1+\frac{2S(m)}{m}\qquad(m\ge1). \tag{★}
]
So (\log F_k(n)) is essentially governed by (\sum_{i=1}^k \frac{S(n+i)}{n+i}). ([Dartmouth Math][2])

With that context, here is what is known about your three questions.

---

## 1) Does (F((\log n)^C,n)\to\infty) for large $C$?

### If (0<C<2): **No**

EGIP show that if (k=k(n)=o((\log n)^2)), then the **normal order** of (F_k(n)) is $1$: i.e. (F_k(n)\sim 1) as (n\to\infty) through a set of integers of asymptotic density $1$. ([Dartmouth Math][2])

Since ((\log n)^C=o((\log n)^2)) for every fixed (C<2), this implies that for “almost all” $n$,
[
F((\log n)^C,n)\approx 1,
]
so the full limit (\lim_{n\to\infty}F((\log n)^C,n)=\infty) cannot hold when (C<2). ([Dartmouth Math][2])

### If (C\ge 2): **Open (unconditionally)**

This is exactly the first part of Erdős Problem #420 and is currently listed as **open**. ([Erdős Problems][1])
In particular, as far as the cited sources indicate, *no fixed polylogarithmic* (f(n)=(\log n)^C) is known to force (F(f,n)\to\infty) for all sufficiently large $n$.

What *is* known is much larger: EGIP proved (and the problem page summarizes) that
[
F(n^{4/9},n)\to\infty,
]
and that (with that scale) one can force $F$ to grow without bound because many integers in $(n,n+n^{4/9}]$ have large prime divisors. ([Dartmouth Math][2])
[[nomath]](They remark the exponent $4/9$ can be improved a bit, but it’s still a power of $n$, far larger than any $(\log n)^C$.)[[/nomath]] ([Erdős Problems][1])

### Conditional evidence

The #420 page records two widely believed conditional implications: ([Erdős Problems][1])

* **Cramér’s conjecture** on prime gaps would imply
  [
  F(g(n)(\log n)^2,n)\to\infty \quad\text{for any }g(n)\to\infty,
  ]
  and in particular it would imply (F((\log n)^C,n)\to\infty) for every (C>2) [[nomath]](take $g(n)=(\log n)^{C-2}$)[[/nomath]]. ([Erdős Problems][1])

So: the statement is **false for (C<2)**, and **open for (C\ge 2)** [[nomath]](with strong heuristic/conditional support once you are above $(\log n)^2$)[[/nomath]]. ([Erdős Problems][1])

---

## 2) Is (F(\log n,n)) everywhere dense in $(1,\infty)$?

This is also explicitly asked in Erdős Problem #420 and is **open**. ([Erdős Problems][1])

What we *do* know (unconditionally) is that (F(\log n,n)) has very large oscillations:

* **It gets arbitrarily close to $1$** along a subsequence: EGIP proved that for any fixed (c>0),
  [
  \liminf_{n\to\infty} F(c\log n,n)=1,
  ]
  so in particular (\liminf_{n\to\infty}F(\log n,n)=1). ([Erdős Problems][1])

* **It is unbounded above in the limsup sense**: the #420 page notes (and this follows from modern “many primes in bounded intervals” results) that bounded prime-gap technology implies
  [
  \limsup_{n\to\infty}F(g(n),n)=\infty
  \quad\text{for every }g(n)\to\infty,
  ]
  hence in particular (\limsup_{n\to\infty}F(\log n,n)=\infty). ([Erdős Problems][1])

Those two facts give “values arbitrarily close to 1” and “values arbitrarily large”, but they do **not** settle density: density would require hitting *every* interval ((a,b)\subset(1,\infty)), and that seems to require extremely fine control over the large-prime-factor statistics of ((n+1)\cdots(n+\lfloor\log n\rfloor)), which is exactly what (★) reduces the problem to. ([Dartmouth Math][2])

So: **unknown**.

---

## 3) If (f(n)\le \log n), $f$ monotone, (f(n)\to\infty): is (F(f,n)) dense?

This is also part of the same open Erdős problem and is **open** as stated. ([Erdős Problems][1])

But there is a strong “almost all $n$” statement in the opposite direction:

Because (f(n)\le \log n) implies (f(n)=o((\log n)^2)), EGIP’s “normal order $1$” theorem applies, giving that for **almost all** $n$,
[
F(f,n)\sim 1.
]
([Dartmouth Math][2])

At the same time, as soon as (f(n)\to\infty), the “prime cluster” phenomenon forces (\limsup_{n\to\infty}F(f,n)=\infty) (again, as summarized on the #420 page). ([Erdős Problems][1])

So for such $f$ we know:

* (F(f,n)) is “typically” near $1$ [[nomath]](density‑1 set of $n$)[[/nomath]]. ([Dartmouth Math][2])
* but it also takes arbitrarily large values along some subsequence. ([Erdős Problems][1])

Whether these values are **everywhere dense** is precisely the difficult, currently unresolved part. ([Erdős Problems][1])

---

### Takeaway

* (F((\log n)^C,n)\to\infty) is **definitely false for (C<2)** [[nomath]](since $F\sim 1$ for almost all $n$)[[/nomath]]. ([Dartmouth Math][2])
* For **(C\ge 2)**, the corresponding limit-to-(\infty) question is **open**; Cramér’s conjecture would imply it for every (C>2). ([Erdős Problems][1])
* The two **density** questions you ask are **open** (Erdős Problem #420), although one has strong partial information: (\liminf=1) in the (\log n) regime and (\limsup=\infty) for any (f(n)\to\infty). ([Erdős Problems][1])

If you want, I can also translate EGIP’s inequalities into explicit “if you can prove X about large prime factors in intervals of length (\log n), then density / divergence would follow” statements, i.e. a clean reduction of your questions to a more standard “smooth numbers in short intervals” problem via (★). ([Dartmouth Math][2])

[1]: https://www.erdosproblems.com/forum/thread/420 "

    Erdős Problem #420 - Discussion thread

"
[2]: https://math.dartmouth.edu/~carlp/factorial.pdf "https://math.dartmouth.edu/~carlp/factorial.pdf"
