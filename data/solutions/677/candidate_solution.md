This is (as far as I can tell) **still open in general**.

It was posed by **Erdős** (1979) and is now listed as **Erdős Problem #677**:

> Let (M(n,k)=\operatorname{lcm}(n+1,\dots,n+k)).
> Is it true that if (m\ge n+k) then (M(n,k)\ne M(m,k))?

The current status on the problem page is **OPEN**. ([Erdős Problems][1])

### What *is* known

* **Trivial small cases.**

  * $k=1$: (M(n,1)=n+1), so equality forces $m=n$, hence certainly no equality for (m\ge n+1).
  * $k=2$: (M(n,2)=\mathrm{lcm}(n+1,n+2)=(n+1)(n+2)) (consecutive integers are coprime), and the map (x\mapsto x(x+1)) is strictly increasing on (\mathbb{N}), so again no equality for (m>n).

* **For fixed $k$, there can only be finitely many “disjoint” coincidences (if any exist).**
  The **Thue–Siegel theorem** implies that for each fixed $k$, there are only **finitely many** pairs $(m,n)$ with (m\ge n+k) such that (M(n,k)=M(m,k)). ([Erdős Problems][1])
  So: even if the conjecture were false for some $k$, it would fail only finitely often for that $k$.

* **Erdős knew coincidences only when the lengths differ.**
  For example,
  [
  M(4,3)=M(13,2),\qquad M(3,4)=M(19,2),
  ]
  but these have different $k$ on the two sides. ([Erdős Problems][1])

* Erdős even conjectured a **stronger** statement (again “aside from finitely many exceptions”): when (k>2) and (m\ge n+k), the two products (\prod_{i\le k}(n+i)) and (\prod_{i\le k}(m+i)) cannot even have the **same set of prime factors**. ([Erdős Problems][1])

### Bottom line

* For (k=1,2): **Yes**, your statement is true (easy).
* For general (k\ge 3): **Unknown**. It’s an Erdős conjecture and remains open in the general form you wrote. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/677 "
  
    Erdős Problem #677
  
"
