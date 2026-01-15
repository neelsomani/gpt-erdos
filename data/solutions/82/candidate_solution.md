What you wrote is a famous **open** problem.

If we write (F(n)) for the largest number such that **every** (n)-vertex graph contains an **induced regular** subgraph on at least (F(n)) vertices, then the claim

[
\frac{F(n)}{\log n}\to\infty
]

is exactly the **Erdős–Fajtlowicz–Staton conjecture**. It is stated as a conjecture in the literature, and (as far as current references indicate) it is still not proved. ([Erdős Problems][1])

So I cannot honestly give a correct proof of that limit, because no proof is known from the standard sources.

What I *can* do is show you the best unconditional lower bound (the “Ramsey bound”), and tell you the best known upper bound and why the conjecture is hard.

---

## What is known: the Ramsey lower bound (F(n)\ge c\log n)

Let (R(k,k)) be the Ramsey number: the smallest (N) such that every graph on (N) vertices contains either a clique of size (k) or an independent set of size (k).

A standard bound is
[
R(k,k)\le 4^k.
]
(One can prove this by the usual recursion (R(k,k)\le R(k-1,k)+R(k,k-1)) and induction.)

Now fix (n), and choose (k) so that (4^k\le n<4^{k+1}). Equivalently,
[
k=\left\lfloor \log_4 n\right\rfloor = \left\lfloor \frac{1}{2}\log_2 n\right\rfloor.
]

Then every graph on (n) vertices contains (by Ramsey) either

* a **clique** on (k) vertices, which is ((k-1))-regular, or
* an **independent set** on (k) vertices, which is (0)-regular.

In both cases we get an **induced regular** subgraph on (k) vertices.

So
[
F(n)\ \ge\ k\ =\ \left\lfloor \log_4 n\right\rfloor\ =\Omega(\log n).
]

This is the “trivial” lower bound that everyone starts from. 

---

## Why your requested statement is not currently proved

The conjecture asks for *any* improvement over the Ramsey bound, even something tiny like
[
F(n)\ \ge\ (\log n)(\log\log n)
]
or even
[
F(n)\ \ge\ (\log n)\cdot \log\log\log n,
]
because any unbounded extra factor would imply (F(n)/\log n\to\infty).

But getting **any** such extra factor has resisted known methods. This is explicitly stated in Alon–Krivelevich–Sudakov (they say they are unable to prove or disprove the conjecture). 
It is also listed as an open Erdős problem as of late 2025. ([Erdős Problems][1])

---

## Best known upper bound (so (F(n)) is not too big)

Alon–Krivelevich–Sudakov proved an upper bound of the form
[
F(n)\le C, n^{1/2}(\log n)^{1/4}
]
for an absolute constant (C). 

So the truth is somewhere between (c\log n) and about (n^{1/2},\mathrm{polylog}(n)), and the main gap is on the lower bound side.

---

## Related partial progress (but it does not give regularity)

People can prove much stronger results if you relax “regular” to “almost regular”.

For example, for fixed (\varepsilon>0), every (n)-vertex graph contains an induced subgraph on (n^{\Omega(\varepsilon^2/\log(1/\varepsilon))}) vertices whose max degree is at most ((1+\varepsilon)) times its min degree. 

That is a big induced subgraph with degrees **close** to each other, but turning that into **exactly equal** degrees is exactly where things break.

---

## Bottom line

* The statement “(F(n)/\log n \to \infty)” is a well-known conjecture and is **still open** in the standard references. ([Erdős Problems][1])
* What you *can* prove today is the Ramsey bound (F(n)=\Omega(\log n)), as shown above. 
* Best known upper bound is (F(n)\le O(n^{1/2}(\log n)^{1/4})). 

If you tell me the context (homework vs. reading group vs. research), I can tailor what I give next: either a clean write-up of the Ramsey bound proof, or a more detailed explanation of the best known results and the main obstacles.

[1]: https://www.erdosproblems.com/forum/thread/82 "

    Erdős Problem #82 - Discussion thread

"
