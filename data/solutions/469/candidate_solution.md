Your set $A$ is exactly the set of **primitive pseudoperfect numbers** (also called *primitive semiperfect* or *irreducible semiperfect* numbers). ([OEIS][1])

### What is known about (\sum_{n\in A}\frac1n)

As of the current literature indexed online (and as of the most recent public status summaries), **it is not known** whether
[
\sum_{n\in A}\frac1n
]
converges.

* Benkoski and Erdős explicitly state that convergence “seems certain,” but that they **could not prove it**. ([Renyi Users][2])
* The Erdős Problems database lists this as **Erdős problem #469 (OPEN)** (last edited Oct 19, 2025). ([Erdős Problems][3])

So the honest answer is: **the convergence is an open problem** (in the usual sense: no published proof of convergence or divergence is currently known).

### Some context and partial results

#### 1) $A$ is infinite

Benkoski–Erdős give explicit infinite families of primitive pseudoperfect numbers. One particularly simple family is
[
n = 2^k p \quad\text{with (p) prime and } 2^k < p < 2^{k+1},
]
which they note are primitive abundant and pseudoperfect (indeed practical), hence lie in $A$. ([Renyi Users][2])

#### 2) A key structural constraint (largest prime factor divides a subset-sum)

Let (n\in A), let (p=P(n)) be the largest prime divisor, and write (n=p,n'). If
[
n = d_1+\cdots+d_t
]
is a representation by distinct proper divisors, then reducing mod $p$ forces that **$p$ divides the sum of some nonempty collection of divisors of (n')**. This is a standard “mod $p$” observation emphasized in modern expositions. ([Pollack at UGA][4])

A quick consequence (useful for intuition): since any such subset-sum is (\le \sigma(n')), one gets (p \le \sigma(n')). In particular, for any *fixed* (n'), there are only finitely many possible primes $p$ that could appear as $P(n)$ in a number (n=p n').

This kind of restriction is one reason convergence is viewed as plausible, but it has not (yet) been pushed to a full proof.

#### 3) A large subcollection is known to be summable

Kevin Pollack’s book splits $S=A$ into two parts
[
S = S_1 \cup S_2,\qquad
S_1 := {n\in S: \Omega(n) > 1.01\log\log n},
]
and then proves (as an exercise, with detailed guidance) that
[
\sum_{n\in S_2}\frac1n \quad\text{converges}.
]
([Pollack at UGA][4])

So, **the only potential obstruction** to convergence (in that framework) comes from the “many prime factors” part (S_1). Handling (S_1) is essentially where the genuine difficulty lies.

#### 4) Numerical evidence is inconclusive but consistent with convergence

OEIS A006036 lists the beginning of $A$. ([OEIS][1])
Using those listed terms up to (4970), the partial sum is about (0.3222) (computed directly from the OEIS initial segment). This neither proves nor disproves convergence, but it matches the heuristic expectation that the set is quite thin.

### Bottom line

* **Status:** Open (Erdős problem #469). ([Erdős Problems][3])
* **Expectation:** Many experts (going back to Benkoski–Erdős) expect convergence, but no proof is known. ([Renyi Users][2])
* **Partial progress:** A substantial subseries [[nomath]](those $n$ with “not too many” prime factors in the sense above)[[/nomath]] is known to converge. ([Pollack at UGA][4])

If you want, I can also outline the standard “mod $p$” argument in full detail and show precisely how it leads to the bound on the number of possible largest primes $p$ for a fixed cofactor (n'), since that’s the key combinatorial input in the known partial results.

[1]: https://oeis.org/A006036 "https://oeis.org/A006036"
[2]: https://users.renyi.hu/~p_erdos/1974-24.pdf "https://users.renyi.hu/~p_erdos/1974-24.pdf"
[3]: https://www.erdosproblems.com/469 "
  
    Erdős Problem #469
  
"
[4]: https://pollack.uga.edu/NABDofficial.pdf "book.dvi"
