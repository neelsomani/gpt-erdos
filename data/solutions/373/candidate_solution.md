Write the equation as
[
n! = a_1!a_2!\cdots a_k!,\qquad n-1>a_1\ge a_2\ge\cdots\ge a_k\ge 2.
]

## 1) Why the condition (a_1<n-1) matters

If you *don’t* impose (a_1<n-1), then there are infinitely many “trivial” solutions: take any choice of integers (a_2,\dots,a_k\ge 2) and set
[
n:=a_2!\cdots a_k!,\qquad a_1:=n-1.
]
Then
[
a_1!,a_2!\cdots a_k!=(n-1)!\cdot n=n!,
]
so you get infinitely many solutions with (a_1=n-1). This is exactly the family your hypothesis (n-1>a_1) excludes. ([MathOverflow][1])

So your question is about **nontrivial** solutions.

## 2) Unconditional status (important)

As of the current literature, the statement

> “There are only finitely many nontrivial solutions to (n!=\prod a_i!) with (a_1\le n-2)”

is a **well-known open problem** (it appears in sources discussing Hickerson’s conjecture / Erdős-type factorial product problems). ([DEA][2])

What *is* known unconditionally is extensive computation: it’s been checked that [[nomath]](aside from the trivial $a_1=n-1$ family)[[/nomath]] there are no further solutions up to very large bounds; for instance, comments in the MathOverflow thread report no nontrivial examples up to (n=1{,}000{,}000). ([MathOverflow][1])

## 3) What you *can* “show”: finiteness under the (abc) conjecture

There **is** a conditional theorem which implies exactly what you asked for (and more):

Assuming **Baker’s explicit (abc) conjecture**, Nair–Shorey prove that the *only* nontrivial solutions of
[
n!=a_1!a_2!\cdots a_t! \quad (n>a_1\ge \cdots \ge a_t>1,\ a_1\le n-2)
]
are the following four:
$$
9!=7!3!3!2!
$$
$$
10!=7!6!
$$
$$
10!=7!5!3!
$$
$$
16!=14!5!2!.
$$
In particular, **there are finitely many** solutions satisfying your inequalities (indeed, exactly these four). ([MathOverflow][1])

For completeness, Baker’s explicit (abc) conjecture is the inequality quoted in that MathOverflow answer: if (a,b,c) are coprime positive integers with (a+b=c), with $N=\mathrm{rad}(abc)=\prod_{p\mid abc}p$ and $\omega=\omega(abc)$ the number of distinct primes dividing $abc$, then
[
c< \frac{6}{5}N\frac{(\log N)^{\omega}}{\omega!}.
]
([MathOverflow][1])

## 4) Conclusion

* **Unconditionally:** it is *not* currently proved that there are only finitely many nontrivial solutions; it’s an open problem, though heavily computationally tested. ([DEA][2])
* **Conditionally [[nomath]](assuming Baker’s explicit $abc$)[[/nomath]]:** there are exactly four nontrivial solutions, so the equation has **only finitely many** solutions under your constraints. ([MathOverflow][1])

If you tell me the source of the problem (book/handout), I can tailor the write-up to match the intended assumptions [[nomath]](many texts that pose this explicitly mean “assuming $abc$”)[[/nomath]].

[1]: https://mathoverflow.net/questions/17058/factorials-in-pascals-triangle "co.combinatorics - Factorials in Pascal's triangle - MathOverflow"
[2]: https://dea.lib.unideb.hu/bitstreams/4c82a8d4-9da2-46a1-a81f-a688eac7c34a/download "https://dea.lib.unideb.hu/bitstreams/4c82a8d4-9da2-46a1-a81f-a688eac7c34a/download"
