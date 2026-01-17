As of January 2026, **no example is known that is *proved* to be a Sierpiński number while also being *proved* to admit *no* finite prime covering set**. In other words: **the existence of “non‑covering” Sierpiński numbers is an open problem.** ([Erdős Problems][1])

That said, there is substantial evidence pointing toward a “yes” answer, and there are **specific, rigorously proved Sierpiński numbers that are widely believed not to have any finite covering set**, even though nobody has been able to prove the nonexistence of such a set.

## What is known

### Many Sierpiński numbers do have finite covers

The classical way to prove “(m2^n+1) is always composite” is exactly to exhibit a finite set of primes $P$ and a finite covering of the exponents $n$ (via congruences) so that one of those primes divides (m2^n+1) for every $n$. This is how Selfridge proved $78557$ is Sierpiński, for example. 

Sierpiński’s original construction likewise produces infinitely many such $m$ by solving a system of congruences tied to a finite set of primes. 

### The “non‑covering” question is an Erdős–Graham / Guy open problem

The precise question you ask—whether there exists a Sierpiński number for which *no* finite prime set $P$ covers all (m2^n+1)—is recorded as an open Erdős problem (and in Guy’s list). ([Erdős Problems][1])

## Why people think the answer might be “yes”

### Izotov (1995) proved Sierpiński numbers by a *different mechanism*

Izotov constructed infinitely many Sierpiński numbers of the form (k=t^4) where:

* for exponents (n\equiv 2 \pmod 4), one uses an **algebraic (Aurifeuillean) factorization** of (t^4\cdot 2^{n}+1), giving compositeness without appealing to any fixed prime divisor; and
* for the remaining residue classes of $n$, one still uses a **finite set of primes** to cover those $n$. ([FQ Math][2])

Importantly, Izotov explicitly notes that Sierpiński’s “standard” prime set does **not** cover his $k$ [[nomath]](e.g. his terms in the $n\equiv 2\pmod4$ class behave differently modulo 5)[[/nomath]], and he raises the possibility that the least Sierpiński number might have no covering set. ([FQ Math][2])

This is not yet a proof of “no covering set exists,” but it produces **provable Sierpiński numbers whose compositeness is not explained purely by a covering set.**

### Filaseta–Finch–Kozek (2008) gave concrete candidates and computational evidence

Filaseta, Finch, and Kozek expanded Izotov’s idea and singled out a particularly notable fourth‑power example
[
k=\ell^4\quad\text{with}\quad \ell=734110615000775,
]
which is **proved to be Sierpiński** by this “factorization + partial cover” method, and they present evidence suggesting it “does not arise from a covering argument,” i.e. is a strong candidate for having **no finite covering set at all**. 

A MathOverflow discussion later summarized the situation bluntly: no full covering set has been found for these Izotov-type numbers, and it is conjectured that none exists. ([MathOverflow][3])

## Bottom line

* **Proved:** There are infinitely many Sierpiński numbers with finite covering sets (classical constructions). 
* **Open:** Whether **there exists a Sierpiński number with *no* finite covering set**. ([Erdős Problems][1])
* **Strong evidence / leading candidates:** Izotov-type perfect powers, especially (734110615000775^4), are *proved* Sierpiński and are widely believed to have **no** finite prime cover, but this has **not** been proved. ([FQ Math][2])

If you want, I can also rephrase the problem in equivalent terms [[nomath]](e.g. in terms of boundedness of the least prime factor of $m2^n+1$, which is closely tied to this question)[[/nomath]] and explain why “proving no finite cover exists” is so hard compared to proving “all terms are composite.”

[1]: https://www.erdosproblems.com/1113 "
  
    Erdős Problem #1113
  
"
[2]: https://www.fq.math.ca/Scanned/33-3/izotov.pdf "fq1995.pdf"
[3]: https://mathoverflow.net/questions/361835/do-sierpi%C5%84ski-numbers-of-izotov-type-have-a-covering-set "nt.number theory - Do Sierpiński numbers of Izotov type have a covering set? - MathOverflow"
