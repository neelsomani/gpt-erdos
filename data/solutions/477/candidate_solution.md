Let (B=f(\mathbb Z)={f(n):n\in\mathbb Z}). Your condition is exactly that

[
\mathbb Z = A \oplus B
]

in the “tiling/factorisation” sense: every (n\in\mathbb Z) has a **unique** representation (n=a+b) with (a\in A), (b\in B).

### What is known

As far as the current literature summaries indicate, the general question is **open**: it is listed as an open Erdős–Graham problem (Erdős Problem #477). ([Erdős Problems][1])

What *is* known is that the answer is **no for degree $2$** (quadratic polynomials): no quadratic $f$ can work. [[nomath]](So any hypothetical example would have to have degree $\ge 3$.)[[/nomath]] ([Erdős Problems][2])

Below is a self-contained proof of the quadratic obstruction [[nomath]](and the classic $f(n)=n^2$ case)[[/nomath]].

---

## Two basic necessary facts

### 1) Difference sets must be essentially disjoint

If (\mathbb Z=A\oplus B), then uniqueness implies:
[
(A-A)\cap(B-B)={0}.
]
Reason: if (a_1-a_2=b_2-b_1\neq 0), then (a_1+b_1=a_2+b_2) gives two different representations.

A useful corollary: if (,m\mathbb Z \subseteq (B-B)) for some (m\neq 0), then $A$ can have **at most one element in each residue class mod $m$** [[nomath]](otherwise two elements of $A$ would differ by a nonzero multiple of $m$)[[/nomath]], hence (|A|\le |m|) is **finite**.

### 2) For (\deg f\ge 2), $A$ cannot be finite

If (\deg f=d\ge 2), then (|B\cap[-X,X]|) grows at most on the order of (X^{1/d}) [[nomath]](because $|f(n)|\sim c|n|^d$, so $|f(n)|\le X$ forces $|n|\ll X^{1/d}$)[[/nomath]].

But if $A$ were finite, say (|A|=k), then the sets $A+b$ [[nomath]](for $b\in B$)[[/nomath]] are disjoint and each has size $k$. Covering $[-N,N]$ would force (|B\cap[-N-O(1),N+O(1)]|\gtrsim N), i.e. **linear** growth—impossible for (d\ge 2).

So for (\deg f\ge 2), any such $A$ would have to be **infinite**.

---

## Why *no quadratic* polynomial can work

Every integer-valued quadratic (f:\mathbb Z\to\mathbb Z) can be written in the standard integer-valued basis as
[
f(n)=p\binom{n}{2}+qn+r
= \frac{p}{2}n(n-1)+qn+r
]
with (p,q,r\in\mathbb Z).

Consider the difference (f(k)-f(-k)):
[
f(k)-f(-k)
=\\(\frac{p}{2}k(k-1)+qk+r\\)-\\(\frac{p}{2}k(k+1)-qk+r\\)
=(2q-p),k.
]

* If (2q-p\neq 0), then as $k$ ranges over (\mathbb Z), ((2q-p)k) ranges over the whole subgroup ((2q-p)\mathbb Z). Hence
  [
  (2q-p)\mathbb Z \subseteq B-B.
  ]
  By the “difference-set disjointness” observation above, this forces $A$ to be **finite**, contradicting the fact that $A$ cannot be finite when (\deg f\ge 2).

* If (2q-p=0), then $p=2q$ and $p$ is even; write $p=2m$. Then
  [
  f(n)=m n^2 + r.
  ]
  Now
  [
  f(k+1)-f(k-1)=m\bigl((k+1)^2-(k-1)^2\bigr)=m(4k)=4m,k,
  ]
  so (4m\mathbb Z\subseteq B-B), again forcing $A$ finite, contradiction.

Thus **no integer-valued quadratic polynomial** $f$ can admit such a set $A$.

This matches the known special-case arguments [[nomath]](e.g. for $f(n)=n^2$)[[/nomath]] discussed in the problem’s public thread. ([Erdős Problems][2])

---

## What remains open

The original question [[nomath]](degree $\ge 2$)[[/nomath]] is therefore reduced to:

* **Is there such a decomposition for some polynomial of degree (\ge 3)?**

This is exactly the content of Erdős Problem #477, which is currently listed as open; the discussion notes that the square case is ruled out and asks about higher monomials like (x^k) for (k\ge 3). ([Erdős Problems][1])

So, in short:

* **Degree 2:** impossible (provable).
* **Degree (\ge 3):** no example is known, and no general impossibility proof is known (open problem as currently recorded). ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/477 "https://www.erdosproblems.com/477"
[2]: https://www.erdosproblems.com/forum/discuss/477 "https://www.erdosproblems.com/forum/discuss/477"
