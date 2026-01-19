Write
[
A_+={n\in A:f(n)=1},\qquad A_-={n\in A:f(n)=-1}.
]
Then your condition is equivalent to asking whether there must exist finite, nonempty (P\subseteq A_+) and (N\subseteq A_-) with
[
\sum_{n\in P}\frac1n=\sum_{n\in N}\frac1n,
]
since (\sum_{n\in S} \frac{f(n)}n=0) is exactly “positive-signed reciprocals = negative-signed reciprocals”.

## 1) $A$ an infinite arithmetic progression

Yes. This is known to be true: **for every infinite arithmetic progression (A\subseteq\mathbb N) and every non-constant (f:A\to{-1,1}), there exists a finite nonempty (S\subset A) with (\sum_{n\in S} f(n)/n=0)**. This was proved by Sattler (1982b). ([Erdős Problems][1])

For context, the same record notes earlier special cases: Erdős–Straus proved it for (A=\mathbb N), and Sattler proved it for $A$ the odd numbers. ([Erdős Problems][1])

(Separately, arithmetic progressions have very strong “Egyptian fraction” properties—e.g. they are reciprocal bases for integers in the sense that every positive integer can be written as a finite sum of reciprocals of distinct elements of the progression—which helps explain why these problems tend to be tractable on progressions. )

## 2) $A$ an arbitrary set of positive density

No, not in general: **positive density alone does not force such an $S$**. In fact, the statement can fail even for quite dense sets. The Erdős-problems record explicitly notes that it fails for any set $A$ containing exactly one even number. ([Erdős Problems][1])

Here is a concrete counterexample [[nomath]](density $1/2$)[[/nomath]]:

* Let (A = {2}\cup{ \text{all odd positive integers}}). Then $A$ has natural density $1/2$.
* Define (f(2)=-1) and (f(n)=+1) for every odd (n\in A).

Then any finite sum (\sum_{n\in S} \frac{f(n)}n) is either:

* a sum of reciprocals of odd integers (hence a rational number whose reduced denominator is odd), if (2\notin S); in particular it cannot be $0$ unless (S=\varnothing); or
* [[nomath]]($\text{odd-denominator rational} - \frac12$)[[/nomath]], if (2\in S). But (\frac12) has even reduced denominator, so it cannot equal a sum of reciprocals of odd integers (which always has odd reduced denominator). Hence it still cannot be $0$.

So no such nonempty $S$ exists.

It’s worth noting that this “signed zero” question is different in flavor from the (unsigned) Erdős–Graham-type phenomenon: for instance, there is a deep theorem (Bloom, 2022) that any positive-density set contains a finite subset whose reciprocals sum to $1$. ([Quanta Magazine][2]) But that does not prevent the simple parity obstruction above for the *signed* cancellation question.

## 3) $A$ the set of squares excluding $1$

This case is (as far as the same record indicates) **open**: for (A={n^2:n\ge2}), it is not currently settled whether every non-constant $f$ forces a finite $S$ with (\sum_{n\in S} f(n)/n=0). The record also notes that Sattler announced a proof, but it did not appear. ([Erdős Problems][1])

(There are many nontrivial identities among reciprocal squares—e.g. coming from Pythagorean triples after suitable scaling—so some sign patterns give an immediate 3-term cancellation, but the question is whether **every** non-constant sign pattern must.)

[1]: https://www.erdosproblems.com/favourites/Woett?utm_source=chatgpt.com "Erdős Problem Favourites"
[2]: https://www.quantamagazine.org/maths-oldest-problem-ever-gets-a-new-answer-20220309/ "https://www.quantamagazine.org/maths-oldest-problem-ever-gets-a-new-answer-20220309/"
