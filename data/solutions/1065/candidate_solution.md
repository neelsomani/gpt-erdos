For $k=0$, (p=2^{0}q+1=q+1) is even for every odd prime $q$, so the only case is (q=2\Rightarrow p=3). So the real question is for (k\ge 1).

## 1) Primes $p$ with (p-1=2^{k}q) [[nomath]]($q$ prime)[[/nomath]]

This asks for primes $p$ such that the **odd part** of $p-1$ is prime [[nomath]](equivalently, $p-1$ has no odd prime factors besides one prime $q$)[[/nomath]].

This is **open**. Already the special case $k=1$ is exactly the “safe prime / Sophie Germain prime” problem: (p=2q+1) with $q$ prime. It is conjectured there are infinitely many Sophie Germain primes (equivalently, safe primes), but this is not proved. ([Wikipedia][1])

Even the next fixed case $k=2$, i.e. primes of the form (p=4q+1) with $q$ prime, is explicitly described as unknown in expository work by Murty (with Jensen) on sieve methods and Artin’s conjecture: they remark that it is “at present unknown” whether there are infinitely many primes with (p-1=4q) and $q$ prime. ([womengovtcollegevisakha.ac.in][2])

So, with current methods, we cannot prove infinitude for your first family.

### What *is* known in the direction of “$p-1$ has very few prime factors”

There are unconditional sieve results showing that $p-1$ can be forced to have **very few** prime factors, but not as few (and as structured) as (2^{k}q) with $q$ prime. For example, Murty–Seguín–Stewart quote a theorem of Gupta–Murty that produces (\gg x/(\log x)^2) primes (p\le x) with
[
p-1 = 2n,\quad n \in P_2(x),
]
where (P_2(x)) means $n$ has **at most two prime factors** [[nomath]](either $n=q_1$ or $n=q_1q_2$ with primes $q_i$ in a specified size range)[[/nomath]], together with some extra quadratic nonresidue conditions. ([mast.queensu.ca][3])
This gives infinitely many primes where ((p-1)/2) is “almost prime” (prime or semiprime), but it does **not** isolate the case “((p-1)/2) is prime,” and it is far from forcing the remaining cofactor to be a power of $2$.

## 2) Primes $p$ with (p-1=2^{k}3^{\ell}q) [[nomath]]( $q$ prime)[[/nomath]]

This is also **open**.

* It contains your first problem as the subcase (\ell=0).
* In particular, it contains safe primes $(k=1,\ell=0)$, whose infinitude is unproved. ([Wikipedia][1])

So there is no known proof of infinitude here either.

## 3) What the standard conjectures predict

For any *fixed* multiplier $A$, the condition “$q$ and $Aq+1$ are both prime” is a special case of the Hardy–Littlewood/Dickson/Schinzel/Bateman–Horn prime $k$-tuple heuristics (two linear forms). The Sophie Germain page explicitly notes that Dickson’s conjecture, Schinzel’s hypothesis H, and Bateman–Horn generalize the Sophie Germain/safe prime problem. ([Wikipedia][1])

Under those conjectures, one expects:

* For each fixed (k\ge 1), infinitely many primes $q$ with (2^{k}q+1) prime.
* For each fixed (k,\ell), infinitely many primes $q$ with (2^{k}3^{\ell}q+1) prime.
* Hence (a fortiori) infinitely many primes $p$ in both of your unions over $k$ [[nomath]](or over $k,\ell$)[[/nomath]], with an expected count (\asymp \text{const}\cdot x/(\log x)^2) up to $x$.

But unconditionally, we are nowhere close to proving even the simplest fixed-$k$ cases [[nomath]](like $k=1$ or $k=2$)[[/nomath]].

**Bottom line:** both questions are currently **unsolved**; they are natural strengthenings/variants of the Sophie Germain (safe prime) problem. ([Wikipedia][1])

[1]: https://en.wikipedia.org/wiki/Safe_and_Sophie_Germain_primes "https://en.wikipedia.org/wiki/Safe_and_Sophie_Germain_primes"
[2]: https://womengovtcollegevisakha.ac.in/departments/Number%20theory%20%5Bp177-192%5D.pdf "https://womengovtcollegevisakha.ac.in/departments/Number%20theory%20%5Bp177-192%5D.pdf"
[3]: https://mast.queensu.ca/~murty/murty-seguin-stewart.pdf "https://mast.queensu.ca/~murty/murty-seguin-stewart.pdf"
