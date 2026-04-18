# Grok Response for Problem 68

**The Sum and Its Properties**

Let
\[
S = \sum_{n=2}^\infty \frac{1}{n! - 1}.
\]
Each term satisfies \(n! - 1 > n!/2\) for all \(n \geq 4\), so the general term is \(O(1/n!)\). The series therefore converges (by comparison with \(\sum 1/n!\)), and
\[
1 < S < 2.
\]
A numerical approximation with remainder bound yields
\[
S = 1 + \frac{1}{5} + \frac{1}{23} + \frac{1}{119} + \frac{1}{719} + \frac{1}{5039} + R_7,
\]
where the partial sum up to \(n=7\) is already \(1.25347\ldots\) and the tail satisfies
\[
0 < R_7 < \sum_{k=8}^\infty \frac{2}{k!} < \frac{3}{7!},
\]
so \(1.253498 < S < 1.253499\). Higher partial sums tighten the interval further but do not reveal a simple rational.

**Series Expansion**
Rewrite each summand via geometric series:
\[
\frac{1}{n! - 1} = \frac{1}{n!} \cdot \frac{1}{1 - 1/n!} = \sum_{m=1}^\infty \frac{1}{(n!)^m}, \qquad n \geq 2.
\]
Thus
\[
S = \sum_{n=2}^\infty \sum_{m=1}^\infty \frac{1}{(n!)^m}.
\]
Interchanging sums (justified by positivity) produces a series whose terms are reciprocals of powers of factorials. No telescoping or closed form in elementary constants is apparent, and the expression does not match known series for \(e\), \(\pi\), or other numbers whose irrationality is settled.

**Attempted Proof of Irrationality**
Suppose for contradiction that \(S = a/b\) with \(a,b \in \mathbb{Z}\), \(b > 0\), \(\gcd(a,b)=1\). Fix \(N \geq 4\) large enough that the tail
\[
R_N := \sum_{n=N+1}^\infty \frac{1}{n! - 1}
\]
satisfies \(R_N < 1/(2b^2)\). Let
\[
S_N = \sum_{n=2}^N \frac{1}{n! - 1} = \frac{c}{d}
\]
in lowest terms. Then \(d\) divides \(\operatorname{lcm}[2!-1,\dots,N!-1]\), every prime factor of \(d\) divides at least one \(k!-1\) for \(2 \leq k \leq N\), and
\[
\left| \frac{a}{b} - \frac{c}{d} \right| = R_N.
\]
Clearing denominators gives
\[
|ad - bc| = b d R_N.
\]
The left side is a positive integer (since \(R_N > 0\)), hence \(\geq 1\). Also,
\[
|ad - bc| \geq 1 \implies R_N \geq \frac{1}{b d}.
\]
An upper bound on the denominator is
\[
d \leq \prod_{k=2}^N (k! - 1) < \exp(C N^2 \log N)
\]
for an absolute constant \(C > 0\) (using \(\log(k!) \sim k \log k\) and summing). Consequently
\[
\frac{1}{b d} > \exp(-C' N^2 \log N)
\]
for a slightly larger \(C'\). Meanwhile the tail satisfies
\[
R_N > \frac{1}{2(N+1)!} > \exp(-N \log N - O(N)).
\]
For all sufficiently large \(N\) we have
\[
\exp(-N \log N - O(N)) > \exp(-C' N^2 \log N),
\]
so the inequality \(R_N \geq 1/(b d)\) holds and yields no contradiction.

The obstacle is that the least common multiple of the first \(N\) denominators grows far faster than \((N+1)!\), making the Diophantine lower bound \(1/(b d)\) smaller than the tail. Standard arguments that succeed for \(\sum 1/n!\) therefore fail.

**Further Remarks**
All denominators \(n! - 1\) (\(n \geq 2\)) are coprime to 6. Consequently every partial sum \(S_N\), when written in lowest terms, has denominator coprime to 6. Passing to the limit cannot force a denominator divisible by 2 or 3 without the tail supplying exactly the needed cancellation, but the super-factorial decay of \(R_N\) makes controlled cancellation impossible to rule out by direct estimates. No alternative representation (continued fraction, integral, modular identity) that would settle rationality has been found.

After exhaustive examination of expansions, approximation techniques, and modular constraints, the question whether \(S\) is irrational remains unresolved.

**Final Answer**

I could not solve it.
