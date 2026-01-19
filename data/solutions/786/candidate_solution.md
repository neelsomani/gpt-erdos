This is an old question of Erdős (it appears as **Erdős Problem #786**), and **as of Jan 2026 it is still open**. ([Erdős Problems][1])

### What is known for the infinite (density) question?

No construction is known with density (>1-\varepsilon) for arbitrarily small (\varepsilon). The best published lower bounds are constants bounded away from $1$:

* **Density $1/4$**:
  Take
  [
  A={n\in\mathbb N:\ n\equiv 2\pmod 4}.
  ]
  Then every (a\in A) has (v_2(a)=1). If (\prod_{i=1}^r a_i=\prod_{j=1}^s b_j) with all (a_i,b_j\in A), applying (v_2) gives
  [
  r=\sum_{i=1}^r v_2(a_i)=v_2!\Big(\prod a_i\Big)=v_2!\Big(\prod b_j\Big)=\sum_{j=1}^s v_2(b_j)=s.
  ]
  This is the “(\equiv 2!!\pmod 4)” example quoted in the problem summary. ([Erdős Problems][1])

* **Selfridge’s construction with density (1/e-\varepsilon)** [[nomath]](for any $\varepsilon>0$)[[/nomath]]:
  Choose large consecutive primes (p_1<\cdots<p_k) with (\sum_{i=1}^k \frac1{p_i}) just under $1$, and let $A$ be the set of integers divisible by **exactly one** of (p_1,\dots,p_k) [[nomath]](one typically also throws away the negligible set divisible by $p_i^2$ to make the “exactly one copy” argument completely clean)[[/nomath]]. Then each (a\in A) contributes exactly one unit of (p_i)-adic valuation among the chosen primes, so the same valuation-counting argument forces $r=s$. This yields density as close to $1/e$ as desired, and is the best standard construction cited in the literature summary. ([Erdős Problems][1])

So, **the answer “yes, density (>1-\varepsilon)” is not known**, and the best currently recorded constructions only give densities up to about (0.3679\ldots). ([Erdős Problems][1])

### What is known for the finite ({1,\dots,N}) version?

Again, **it is open** whether one can always find such an (A\subset{1,\dots,N}) with (|A|\ge (1-o(1))N). ([Erdős Problems][1])

Known constructions only give a **constant fraction** of $N$, not (1-o(1)):

* A standard example is
  [
  A_N={n\le N:\ \text{(n) has a prime factor }p>\sqrt N}.
  ]
  Any such $n$ has **exactly one** prime factor (> \sqrt N), and that large prime occurs to exponent $1$ [[nomath]](since $p^2>N$)[[/nomath]]. If (\prod a_i=\prod b_j) with all (a_i,b_j\in A_N), then counting the total exponent of primes (> \sqrt N) again forces $r=s$. Erdős’ problem page records that this gives (|A_N|\ge (\log 2)N), and that Erdős improved the constant slightly. ([Erdős Problems][1])

* On the *upper bound* side: Erdős reported that Ruzsa had a proof that the maximum size is (\le (1-c)N) for some absolute (c>0), but that proof was “not yet published”, and as far as the problem page knows, it never appeared. ([Erdős Problems][1])
  So even a **definitive published constant gap from $N$** is not currently pinned down in the standard references.

### Bottom line

* **Infinite-density version:** unknown whether densities can be arbitrarily close to $1$. Best recorded lower bound is (1/e-\varepsilon). ([Erdős Problems][1])
* **Finite $[1,N]$ version:** unknown whether (|A|=(1-o(1))N) is possible. Best recorded lower bounds are (\gg N) with explicit constants (e.g. ((\log 2)N)), but still far from $N$. ([Erdős Problems][1])

If you’d like, I can also write out a fully self-contained proof that the “exactly one of (p_1,\dots,p_k)” construction has the $r=s$ property [[nomath]](and sketch the density computation $\approx (1/e)$)[[/nomath]].

[1]: https://www.erdosproblems.com/786 "
  
    Erdős Problem #786
  
"
