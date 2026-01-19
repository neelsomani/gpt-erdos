Let

[
H(n)=\min\\{\ell\ge 3:\ \exists,k\in{2,\dots,\ell-1}\text{ with }\gcd(k^n-1,\ell^n-1)=1,\\}.
]

## 1) Is (H(n)=3) infinitely often?

This is the question whether
[
\gcd(2^n-1,3^n-1)=1
]
for infinitely many $n$.

As far as currently known, this is **open**. In fact it is the special case (a=2,b=3) of **Ailon–Rudnick’s Conjecture A**: for multiplicatively independent integers (a,b) with (\gcd(a,b)=1), one should have (\gcd(a^n-1,b^n-1)=1) for infinitely many $n$. ([Columbia Mathematics][1])

[[nomath]](Computationally, many $n$ do give $\gcd(2^n-1,3^n-1)=1$; see OEIS A263647, but there is no proof of infinitude.)[[/nomath]] ([Erdős Problems][2])

## 2) Lower bounds for $H(n)$: what is known

A very clean obstruction comes from primes $p$ with (p-1\mid n). Define
[
\omega^*(n)=|\\{,\text{primes }p:\ p-1\mid n,\\}|.
]

**Key lemma (Fermat obstruction).**
If $p$ is prime with (p-1\mid n), then for every integer $m$ with (p\nmid m),
[
m^n\equiv 1 \pmod p\quad\Rightarrow\quad p\mid (m^n-1).
]
So such a prime $p$ divides (m^n-1) for **every** $m$ not divisible by $p$.

Now suppose (\gcd(k^n-1,\ell^n-1)=1). For any prime $p$ with (p-1\mid n), if (p\nmid k) and (p\nmid \ell), then (p\mid(k^n-1)) and (p\mid(\ell^n-1)), contradicting coprimality. Hence:

> For every $p$ with (p-1\mid n), at least one of (k,\ell) must be divisible by $p$.

Equivalently, (k\ell) is divisible by the product of all primes with (p-1\mid n), and since (k<\ell),
[
\ell^2>k\ell\ \ge\ \prod_{p-1\mid n} p
\quad\Longrightarrow\quad
H(n)\ \ge\ \sqrt{\prod_{p-1\mid n} p}.
]

This is exactly the mechanism behind the known lower bounds. Erdős proved a weaker [[nomath]](but still superpolynomial-in-$n$)[[/nomath]] form:
[
H(n)>\exp\\(n^{c/(\log\log n)^2}\\)
\quad\text{for infinitely many }n
]
for some constant (c>0). ([Erdős Problems][2])

Using a stronger theorem about (\omega^*(n)), one can upgrade this to the shape you wrote.

### Using Adleman–Pomerance–Rumely (APR)

APR show that there is an absolute (c>0) such that for infinitely many $n$,
[
\omega^*(n) > n^{c/\log\log n}
]
[[nomath]](equivalently $>\exp(c\log n/\log\log n)$)[[/nomath]]. ([Erdős Problems][2])

Plugging this into the (\sqrt{\prod p}) obstruction [[nomath]](and using the prime number theorem to bound the product of $m$ distinct primes from below)[[/nomath]] gives, for some (possibly different) constant (c>0), infinitely many $n$ with
[
H(n)>\exp\\(n^{c/\log\log n}\\).
]
A sketch of this deduction is written out in the Erdős-problems discussion thread. ([Erdős Problems][2])

So: the **first inequality** in your “(c\pm\varepsilon)” statement [[nomath]](a lower bound of type $\exp(n^{(c-\varepsilon)/\log\log n})$ infinitely often)[[/nomath]] is known to hold for some (c>0).

## 3) Upper bounds of the same shape: status

The “matching” upper bound
[
H(n) < \exp\\(n^{(c+\varepsilon)/\log\log n}\\)\quad\text{for all large }n
]
with the **same** $c$ is **not known** (this is part of why the problem is still listed as open). ([Erdős Problems][2])

What one *can* say is:

* The obstruction above suggests that (\omega^*(n)) is the main driver for large $H(n)$.
* Trivially (\omega^*(n)\le d(n)) (number of divisors), and the maximal order of $d(n)$ is
  [
  d(n)\le n^{(\log 2+o(1))/\log\log n}.
  ]
  This makes it tempting to guess that the “right” constant in a maximal-order statement might be (\log 2), but this is explicitly stated as speculation. ([Erdős Problems][2])

There are of course very crude general upper bounds [[nomath]](e.g. exponential in $n^2$)[[/nomath]] that one can manufacture by explicit constructions, but nothing close to the conjectured (\exp(n^{O(1)/\log\log n}))-scale upper bound is currently established in the literature tied to this problem statement. ([Erdős Problems][2])

## 4) The “fixed $2$” variant: smallest $k$ with (\gcd(k^n-1,2^n-1)=1)

Let $K(n)$ be the smallest integer (k\ge 2) such that (\gcd(k^n-1,2^n-1)=1).

The *same Fermat obstruction* immediately gives a lower bound on $K(n)$:

* If $p$ is an odd prime with (p-1\mid n), then (p\mid (2^n-1)) [[nomath]](because $2^{p-1}\equiv 1\pmod p$ and $p-1\mid n$)[[/nomath]].
* For such $p$, if (p\nmid k), then (p\mid (k^n-1)) as well.

So to have (\gcd(k^n-1,2^n-1)=1), one must have (p\mid k) for every odd prime $p$ with (p-1\mid n). Therefore
[
K(n)\ \ge\ \prod_{\substack{p-1\mid n\ p\ \text{odd prime}}} p,
]
and the APR theorem about many such primes implies $K(n)$ is also (\ge \exp(n^{c/\log\log n})) for infinitely many $n$ [[nomath]](for some $c>0$)[[/nomath]], by the same reasoning as for $H(n)$. ([ar5iv][3])

As for a **similar upper bound** of the form (K(n)\le \exp(n^{(c+\varepsilon)/\log\log n})) [[nomath]](or even $K(n)\le \exp(n^{o(1)})$ uniformly)[[/nomath]]: that is likewise **open in spirit** of the same problem. ([Erdős Problems][2])

[[nomath]](There is a trivial construction $k=\operatorname{rad}(2^n-1)$, the squarefree kernel, which forces $\gcd(k^n-1,2^n-1)=1$, but it only gives $K(n)\le 2^n-1$, far larger than the conjectural scale.)[[/nomath]]

## Takeaway

* **(H(n)=3) infinitely often** [[nomath]](equivalently $\gcd(2^n-1,3^n-1)=1$ infinitely often)[[/nomath]] is a well-known **open** conjecture (Ailon–Rudnick). ([Columbia Mathematics][1])
* **Lower bounds:** Erdős proved (\exp(n^{c/(\log\log n)^2})) infinitely often, and with APR input one gets the stronger (\exp(n^{c/\log\log n})) infinitely often. ([Erdős Problems][2])
* The existence of a **sharp “(c\pm\varepsilon)” upper/lower law** for $H(n)$ [[nomath]](and similarly for the least $k$ coprime to $2^n-1$ in the $k^n-1$ sense)[[/nomath]] is **not currently proved**; (\log 2) is a natural speculative candidate for the constant in such a maximal-order statement. ([Erdős Problems][2])

[1]: https://www.math.columbia.edu/~goldfeld/JNT-ALevin.pdf "Greatest common divisors and Diophantine approximation"
[2]: https://www.erdosproblems.com/forum/thread/820 "

    Erdős Problem #820 - Discussion thread

"
[3]: https://ar5iv.org/abs/math/0202102 "[math/0202102] Torsion points on curves and common divisors of ^-1 and ^-1"
