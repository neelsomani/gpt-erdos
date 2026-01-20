This is Erdős’s Problem #451 and (as far as is currently recorded) it remains open in the sense that no rigorous asymptotic for (n_k) is known. ([Erdős Problems][1])

That said, there is a clean “density” computation and a very plausible heuristic that leads to a sharp-looking estimate.

## 1) Reformulation and exact density of admissible $n$

Let
$
\mathcal P_k={p\ \text{prime}: k<p<2k},\qquad M_k=\prod_{p\in\mathcal P_k}p.
$
The condition
[
\prod_{i=1}^k (n-i)\ \text{has no prime factor in }(k,2k)
]
is equivalent to: for every (p\in\mathcal P_k), none of the integers (n-1,n-2,\dots,n-k) is divisible by $p$.

Fix (p\in\mathcal P_k). Since (p>k), the congruences (n\equiv 1,2,\dots,k\pmod p) are all distinct, and they are exactly the “bad” residues [[nomath]](they make some $n-i\equiv 0\pmod p$)[[/nomath]]. Hence the allowed residues mod $p$ are the remaining $p-k$ classes:
[
n\bmod p\in {0,k+1,k+2,\dots,p-1}.
]
By the Chinese Remainder Theorem [[nomath]](the moduli $p$ are coprime)[[/nomath]], the number of admissible residue classes mod (M_k) is
[
A_k=\prod_{p\in\mathcal P_k}(p-k),
]
so the **exact density** of admissible $n$ is
$
D_k=\frac{A_k}{M_k}=\prod_{k<p<2k}(1-\frac{k}{p}).
$
This computation appears explicitly in the Erdős Problems forum discussion of #451. ([Erdős Problems][2])

## 2) Estimating (D_k) via the prime number theorem: the constant (\log 4)

Take logs:
$
\log\frac1{D_k}=-\sum_{k<p<2k}\log(1-\frac{k}{p}).
$

Using the prime number theorem in the form (\pi(x)\sim x/\log x) to replace sums over primes by an integral (the standard heuristic/first-order asymptotic step), one gets
$
\sum_{k<p<2k} f(p)\ \approx\ \frac1{\log k}\int_k^{2k} f(t),dt,
$
for reasonably nice $f$ on $[k,2k]$. ([Wikipedia][3])

Apply this with (f(t)=\log!\left(1-\frac{k}{t}\right)). Then
[
\int_k^{2k}\log\left(1-\frac{k}{t}\right),dt
= k\int_1^2 \log\left(1-\frac1u\right),du.
]
And
[
\int_1^2 \log\left(1-\frac1u\right),du
=\int_1^2 \bigl(\log(u-1)-\log u\bigr),du
= (-1)-(2\log2-1)=-2\log2=-\log 4.
]
So the main term is
[
\log\frac1{D_k}=(\log 4+o(1))\frac{k}{\log k},
]
equivalently
[
D_k=\exp\left(-(\log 4+o(1))\frac{k}{\log k}\right).
]
This ((\log 4)k/\log k) heuristic asymptotic is also stated in the Erdős Problems forum thread for #451. ([Erdős Problems][2])

## 3) Heuristic estimate for (n_k)

If admissible $n$’s have density (D_k), a natural guess is that the first admissible $n$ after $2k$ is on the order of the typical gap, i.e.
[
n_k \asymp \frac{1}{D_k}.
]
Plugging the asymptotic for (D_k) gives the heuristic estimate
[
\boxed{\ \log n_k \sim (\log 4)\frac{k}{\log k}\ }\qquad\text{or}\qquad
\boxed{\ n_k=\exp!\left((\log 4+o(1))\frac{k}{\log k}\right)\ }.
]
This is exactly the “expected” order of growth discussed in the forum comment: the remaining difficulty is to make the step (n_k\asymp D_k^{-1}) rigorous. ([Erdős Problems][2])

## 4) What is known unconditionally

The Erdős Problems page records:

* A lower bound of the shape (n_k>k^{1+c}) for some constant (c>0) (Erdős–Graham).
* A simple upper bound (n_k \le \prod_{k<p<2k} p = e^{O(k)}) [[nomath]](take $n$ divisible by every prime $p\in(k,2k)$)[[/nomath]]. ([Erdős Problems][1])

Erdős also conjectured that (n_k) should be **subexponential** (n_k<e^{o(k)}) but **superpolynomial** (n_k>k^d) for every fixed $d$, which is consistent with the heuristic (\exp((\log4)k/\log k)). ([Erdős Problems][1])

## 5) Numerical evidence

The values of (n_k) are tabulated as OEIS A386620 [[nomath]](e.g. up to $k=92$)[[/nomath]], and the OEIS entry explicitly points back to this Erdős problem. ([OEIS][4])

They show very rapid [[nomath]](but clearly sub-$e^{ck}$)[[/nomath]] growth and are consistent with (\log n_k) being on the (k/\log k) scale, as described in the forum post. ([Erdős Problems][2])

[1]: https://www.erdosproblems.com/451 "
  
    Erdős Problem #451
  
"
[2]: https://www.erdosproblems.com/forum/thread/451 "

    Erdős Problem #451 - Discussion thread

"
[3]: https://en.wikipedia.org/wiki/Prime_number_theorem?utm_source=chatgpt.com "Prime number theorem"
[4]: https://oeis.org/A386620 "A386620 - OEIS"
