Let

* (D(A)={,|x-y|:x,y\in A,\ x\neq y,}) be the **set of pairwise distances**, and
* for a “pinned” point (p\in A), (D_p(A)={,|p-q|:q\in A\setminus{p},}).

### 1) Must $A$ determine at least (\lfloor n/2\rfloor) distinct distances?

This is **open** in general. It is a conjecture attributed to **Szemerédi** (and appears as Erdős Problem #1082). ([Erdős Problems][1])

What *is* known is a weaker linear bound: Szemerédi proved the statement with (\lfloor n/2\rfloor) replaced by roughly $n/3$; in particular one can guarantee
[
|D(A)|\ \ge\ \max_{p\in A}|D_p(A)|\ \ge\ \frac{n-1}{3}.
]
([Erdős Problems][1])

A standard way to see the ((n-1)/3) is via double-counting **isosceles triangles**: assuming every point has at most $k$ distinct distances forces many equal-radius pairs around each point, while “no three collinear” bounds how many apices can lie on a perpendicular bisector—leading to (k\ge (n-1)/3). 

[[nomath]](For comparison: if the points are the vertices of a convex $n$-gon, then the *global* bound $|D(A)|\ge\lfloor n/2\rfloor$ is known—proved by Altman—so the difficulty here is really the general-position setting.)[[/nomath]] ([Erdős Problems][2])

### 2) Must there exist a point with at least (\lfloor n/2\rfloor) distinct distances to the others?

**No.** This stronger “pinned” statement is false even when no three points are collinear.

A concrete counterexample uses $n=42$ points arranged as **two concentric regular 21-gons** with a carefully chosen radius ratio (r_0\approx 0.445) [[nomath]](a root of $x^3-x^2-2x+1=0$)[[/nomath]]. In that configuration, **every point** determines only (20) distinct distances to the other (41) points, whereas (\lfloor 42/2\rfloor=21). ([Erdős Problems][3])

This counterexample has been checked (including a formal Lean 4 verification) and is recorded in the discussion of Erdős Problem #1082. ([Erdős Problems][3])

---

So, as of the current literature:

* **Global** (|D(A)|\ge \lfloor n/2\rfloor) under “no three collinear”: **open** [[nomath]](best general guarantee is $\ge (n-1)/3$)[[/nomath]]. ([Erdős Problems][1])
* **Pinned** existence of $p$ with (|D_p(A)|\ge \lfloor n/2\rfloor): **false** (explicit 42-point counterexample). ([Erdős Problems][3])

[1]: https://www.erdosproblems.com/1082 "
  
    Erdős Problem #1082
  
"
[2]: https://www.erdosproblems.com/93 "
  
    Erdős Problem #93
  
"
[3]: https://www.erdosproblems.com/forum/discuss/1082 "

    Erdős Problem #1082 - Discussion thread

"
