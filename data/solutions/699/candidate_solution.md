This is **not known** in general: it’s an **open conjecture** of **Erdős and Szekeres** (1978).

They formulate it equivalently by letting $P(a,b)$ be the **largest prime divisor of (\gcd(a,b))**, and conjecturing that for every (1\le i<j\le n/2),
[
P\left(\binom{n}{i},\binom{n}{j}\right)\ \ge\ i,
]
which is exactly the same as saying “there exists a prime (p\ge i) dividing (\gcd!\left(\binom{n}{i},\binom{n}{j}\right)).” 

What *is* known:

* Erdős–Szekeres prove that (\gcd\left(\binom{n}{i},\binom{n}{j}\right)>1) for (1\le i<j\le n/2), and in fact give a lower bound
  [
  \gcd\left(\binom{n}{i},\binom{n}{j}\right)\ \ge\ \frac{\binom{n}{i}}{\binom{j}{i}}\ \ge\ 2^i,
  ]
  so there is **always at least one prime** dividing the gcd — the conjecture is about forcing **a prime (\ge i)**. ([Erdős Problems][1])

* A related “stronger” hope, replacing (p\ge i) by (p>i), is known to fail in some cases [[nomath]](e.g. certain $i=2$ and powers of $2$, and scattered $i=3$ examples)[[/nomath]]. Erdős–Szekeres already discuss such counterexamples, and note [[nomath]](for $i\ge 4$)[[/nomath]] the example
  [
  \gcd\left(\binom{28}{5},\binom{28}{14}\right)=2^3\cdot 3^3\cdot 5,
  ]
  where the largest prime factor is $5=i$, so “(>i)” fails but “(\ge i)” still holds. 

Computational evidence:

* Extensive computations have found **no counterexample** to the (\ge i) version in large ranges [[nomath]](e.g. one report checks all $n\le 10^7$, and also targeted families up to about $1.3\times 10^8$)[[/nomath]]. But this still doesn’t settle the conjecture. ([Erdős Problems][2])

So, the best current answer is: **it is conjectured to be true, but remains open** (Erdős Problem #699). ([Erdős Problems][3])

[1]: https://www.erdosproblems.com/search_bib/ErSz78/no "
  
    Erdős Problems
  
"
[2]: https://www.erdosproblems.com/forum/thread/699 "

    Erdős Problem #699 - Discussion thread

"
[3]: https://www.erdosproblems.com/699 "
  
    Erdős Problem #699
  
"
