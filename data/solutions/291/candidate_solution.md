Write the harmonic number as
[
H_n:=\sum_{k=1}^n \frac1k=\frac{a_n}{L_n},\qquad L_n=\mathrm{lcm}(1,2,\dots,n),
]
so (a_n=L_nH_n\in\mathbb Z). Let (\frac{u_n}{v_n}) be the reduced fraction for (H_n). Then
[
\frac{a_n}{L_n}=\frac{u_n}{v_n}\quad\Longrightarrow\quad v_n=\frac{L_n}{\gcd(a_n,L_n)}.
]
So (\gcd(a_n,L_n)=1) is equivalent to (v_n=L_n), while (\gcd(a_n,L_n)>1) is equivalent to (v_n<L_n). This is exactly the “(d_n=D_n) vs. (d_n<D_n)” question in the literature on denominators of harmonic numbers. ([arXiv][1])

## The case (\gcd(a_n,L_n)>1) does occur infinitely often (in fact, trivially)

There is a clean criterion for when a prime (p\le n) divides (\gcd(a_n,L_n)).

Let (p\le n) be prime, and let $e$ be maximal such that (p^e\le n) [[nomath]](so $p^e$ is the highest power of $p$ appearing in $L_n$)[[/nomath]]. Write
$
n = k,p^e + r,\qquad 0\le r<p^e,
$
so (k=\lfloor n/p^e\rfloor) is the leading digit of $n$ written in base $p$.

Then one checks [[nomath]](by reducing $a_n=\sum_{m=1}^n L_n/m$ mod $p$)[[/nomath]] that
[
a_n \equiv \frac{L_n}{p^e}\left(1+\frac12+\cdots+\frac1k\right)\pmod p,
]
where the fractions on the right are interpreted modulo $p$ (i.e. (j^{-1}\bmod p)); importantly (k<p), so all those inverses exist. Since (p\nmid (L_n/p^e)), this yields:

> **Criterion.** A prime (p\le n) divides (\gcd(a_n,L_n)) **iff** $p$ divides the numerator of (1+\frac12+\cdots+\frac1k), where $k$ is the leading base-$p$ digit of $n$. ([Erdős Problems][2])

Now take (p=3). If $n$ begins with digit $2$ in base $3$, i.e.
[
2\cdot 3^e \le n \le 3^{e+1}-1
]
for some (e\ge 0), then (k=2), and
[
1+\frac12=\frac{3}{2}
]
has numerator divisible by $3$. By the criterion, (3\mid \gcd(a_n,L_n)), hence (\gcd(a_n,L_n)>1) for all such $n$. There are infinitely many such $n$. ([Erdős Problems][2])

More generally, for any odd prime $p$, if the leading base-$p$ digit of $n$ is $p-1$, then (k=p-1) and
[
\sum_{j=1}^{p-1} j^{-1}\equiv \sum_{j=1}^{p-1} j \equiv 0 \pmod p,
]
so (p\mid \gcd(a_n,L_n)). ([Erdős Problems][2])

So the “(\gcd(a_n,L_n)>1) infinitely often” half is completely settled (and easy).

## The case (\gcd(a_n,L_n)=1) infinitely often is open

The other half—whether (\gcd(a_n,L_n)=1) happens for infinitely many $n$—is **not known** in general. It is posed as Erdős problem #291 and is listed as open. ([Erdős Problems][2])

In the notation common in the literature, this is the conjecture that the reduced denominator (v_n) equals (L_n) infinitely often [[nomath]](Shiu explicitly conjectures $d_n=D_n$ infinitely often)[[/nomath]]. ([arXiv][1])

There are also heuristics predicting that the count of (n\le x) with (\gcd(a_n,L_n)=1) should be (\asymp x/\log x) [[nomath]](so infinite but density $0$)[[/nomath]], but turning this into a proof seems out of reach at present. ([Erdős Problems][2])

Finally, there is a conditional density result in the opposite direction: Wu–Yan (2022) prove (assuming a linear-independence hypothesis implied by Schanuel’s conjecture) that the set of $n$ with (\gcd(a_n,L_n)>1) has **upper asymptotic density (1)**, so even if (\gcd(a_n,L_n)=1) is infinite it would be very sparse. ([Comptes Rendus][3])

## Bottom line

* (\gcd(a_n,L_n)>1) occurs for infinitely many (n) (indeed, for infinitely many explicit families). ([Erdős Problems][2])
* Whether (\gcd(a_n,L_n)=1) occurs for infinitely many (n) is **open** (conjectured yes). ([Erdős Problems][2])

So the combined statement “both occur infinitely often” is **not currently proved**, because the (\gcd(a_n,L_n)=1) half is unresolved.

[1]: https://arxiv.org/abs/1607.02863?utm_source=chatgpt.com "The denominators of harmonic numbers (Revised)"
[2]: https://www.erdosproblems.com/291 "
  
    Erdős Problem #291
  
"
[3]: https://comptes-rendus.academie-sciences.fr/mathematique/item/10.5802/crmath.282.pdf "On the denominators of harmonic numbers. IV"
