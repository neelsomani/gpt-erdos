This is **open**.

It’s an Erdős problem (often listed as “Erdős Problem #10”): whether there exists an absolute constant (k) such that **every** integer (n) can be written
[
n ;=; p ;+; 2^{a_1}+\cdots+2^{a_j}\qquad (j\le k),
]
with (p) prime (and typically (a_i\ge 0), so (1=2^0) is allowed). ([Erdős Problems][1])

### What is known

* **For (k=1)** (prime + one power of 2): false.
  Polignac’s old conjecture in this direction has counterexamples; for instance (127) and (331) are not of the form “odd prime + power of 2”, and Erdős proved there is even an **infinite arithmetic progression** of such “obstinate numbers”. ([MathOverflow][2])

* **For (k=2)** (prime + two powers of 2): also false.
  There are infinitely many odd integers not representable as (p+2^k+2^\ell) (with (k,\ell\ge 0)); moreover, results of Crocker and later Pan show the exceptional set is quite large (e.g. (\gg_\varepsilon N^{1-\varepsilon}) up to (N)). ([Erdős Problems][3])

* **“Almost all” integers are representable if you allow (k) to be large enough.**
  Gallagher proved that for every (\varepsilon>0) there exists (k(\varepsilon)) such that the integers representable as “prime + at most (k(\varepsilon)) powers of 2” have **lower density at least (1-\varepsilon)**. ([Erdős Problems][1])
  So the obstruction is not that such representations are rare; the difficulty is ruling out an infinite exceptional set for *some fixed* (k).

### What people conjecture

* Granville and Soundararajan conjectured that **3 powers of 2 suffice for all odd integers**, which would imply **4 powers suffice for all even integers** (since adding (1=2^0) flips parity). ([Erdős Problems][1])
* But for *all integers* with (k=3), there are known even counterexamples; e.g. (1117175146) is **not** the sum of a prime and at most 3 powers of 2. ([Erdős Problems][1])

### Bottom line

No one currently knows whether there exists a universal (k) that works for **every** integer. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/latex/10 "
  
    Erdős Problems
  
"
[2]: https://mathoverflow.net/questions/49786/form-of-primesprime-plus-a-power-of-2 "form of primes:prime plus a power of 2? - MathOverflow"
[3]: https://www.erdosproblems.com/9 "
  
    Erdős Problem #9
  
"
