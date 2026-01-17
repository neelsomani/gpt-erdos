Let (A\subseteq \mathbb N) be written as a nondecreasing sequence (a_1\le a_2\le\cdots), and write
[
P(A)=\\{\sum_{x\in B}x:;B\subseteq A\text{ finite}\\}
]
for the set of finite subset sums. On the Erdős–Graham “complete sequence” convention, **$A$ is complete** if $P(A)$ contains **all sufficiently large** integers. ([Erdős Problems][1])

Two monotonicity facts to keep in mind:

* If (A\setminus S) is complete and (T\subseteq S), then (A\setminus T) is also complete (removing fewer elements can only help).
* If (A\setminus S) is *not* complete and (S\subseteq T), then (A\setminus T) is also *not* complete (removing more elements can’t restore missing subset sums).

So, for example, if a sequence is “not complete after removing **any 2** elements”, then it is automatically “not complete after removing **any (n\ge 2)** elements”.

## Existence for (m=0) and any (n\ge 1)

Take
[
A={1,2,4,8,\dots}={2^k:k\ge 0}.
]

* $A$ is (strongly) complete: every integer has a binary expansion as a sum of distinct powers of $2$.
* If you remove **any one** element (2^k), then (2^k) itself becomes unrepresentable: sums of smaller powers are (<2^k), and using any larger power makes the sum (>2^k). Hence (A\setminus{2^k}) is not complete.

By monotonicity, removing any (n\ge 1) elements also makes it not complete. Therefore **every pair ((m,n)=(0,n)) with (n\ge 1)** works. (This is the “powers of 2” example noted on the problem page.) ([Erdős Problems][2])

## Existence for (m=1) and any (n\ge 2)

Take the Fibonacci sequence
[
A={F_1,F_2,F_3,\dots}={1,1,2,3,5,8,\dots},\qquad F_{k+2}=F_{k+1}+F_k.
]

### Why removing any 1 element keeps it complete

A standard sufficient-and-necessary criterion for *full* coverage by subset sums of an increasing sequence starting with $1$ is:

> If (b_1=1) and (b_{t+1}\le 1+\sum_{i=1}^t b_i) for all $t$, then the subset sums of ({b_1,\dots,b_t}) fill the whole interval ([0,\sum_{i=1}^t b_i]), hence the infinite sequence is (strongly) complete.

Now delete one Fibonacci number (F_j). The resulting sequence is still nondecreasing. The key identity
[
\sum_{r=1}^{t}F_r = F_{t+2}-1
]
implies that at every stage, the “next” available Fibonacci number is (\le 1+) (sum of all previous available ones); the only time equality is tight is exactly at the jump where (F_j) is missing. In fact, one checks directly that the inequality (b_{t+1}\le 1+\sum_{i\le t}b_i) holds for all (t) after the deletion, so the sequence remains (strongly) complete.

This is the “Fibonacci shows (m=1,n=2) is possible” observation on the Erdős problems page. ([Erdős Problems][2])

### Why removing any 2 elements destroys completeness (infinitely many missing)

Remove (F_i) and (F_j) with (i<j). Consider the infinite family of integers
[
N_r:=F_{j+1+2r}-1\qquad(r=0,1,2,\dots).
]
I claim **none** of these (N_r) can be represented using the remaining Fibonacci numbers, so (A\setminus\\{F_i,F_j\\}) is not complete.

* **Base (r=0)**: (N_0=F_{j+1}-1=\sum_{t=1}^{j-1}F_t).
  After removing (F_i), the sum of *all* available Fibonacci numbers (<F_{j+1}) is at most (N_0-F_i), which is strictly smaller than (N_0). You cannot use (F_j) (it’s removed), and you cannot use any Fibonacci (\ge F_{j+1}) because that would overshoot (N_0<F_{j+1}). So (N_0) is unrepresentable.

* **Induction step**: assume (N_r=F_{k-2}-1) is unrepresentable for (k=j+3+2r). Consider (N_{r+1}=F_k-1).
  Look at all available Fibonacci numbers (<F_{k-1}), i.e. among (F_1,\dots,F_{k-2}). Since (k-2\ge j+1), both removed numbers (F_i) and (F_j) lie in this range, so the *maximum* sum achievable using only terms (<F_{k-1}) is
  [
  \sum_{t=1}^{k-2}F_t - (F_i+F_j) = (F_k-1) - (F_i+F_j) < F_k-1.
  ]
  Therefore any representation of (F_k-1) must use some term (\ge F_{k-1}). But (F_k) is too large [[nomath]](it exceeds $F_k-1$)[[/nomath]], so the only possibility is that **(F_{k-1}) must be used**. Subtracting it leaves
  [
  (F_k-1)-F_{k-1}=F_{k-2}-1=N_r,
  ]
  which is unrepresentable by the induction hypothesis. Hence (N_{r+1}) is also unrepresentable.

Thus (A\setminus\\{F_i,F_j\\}) misses infinitely many integers (N_r\to\infty), so it is not complete. This establishes the (m=1,n=2) example [[nomath]](and hence $m=1$ with **any** $n\ge 2$ by monotonicity)[[/nomath]]. ([Erdős Problems][2])

## What about (m\ge 2)?

With the “all sufficiently large integers” definition of completeness, **the general classification is open**: even the next case ((m,n)=(2,3)) is not known (as recorded on the Erdős problems page). ([Erdős Problems][2])

If instead you interpret “complete” in the **strong sense** (P(A)=\mathbb N) (no exceptions), then a result attributed there to van Doorn says **no such sequence exists for (2\le m<n)**. ([Erdős Problems][2])

## Answer summary

* **Yes** for all $(m,n)$ with $m=0$ and (n\ge 1) [[nomath]](powers of $2$)[[/nomath]]. ([Erdős Problems][2])
* **Yes** for all $(m,n)$ with (m=1) and (n\ge 2) (Fibonacci). ([Erdős Problems][2])
* For **(m\ge 2)** (under the standard “sufficiently large” definition), this is **open** as of the current literature/status reports; in particular $(2,3)$ is open. ([Erdős Problems][2])
* Under the **strong** interpretation (P(A)=\mathbb N), there are **no** examples for (2\le m<n). ([Erdős Problems][2])

[1]: https://www.erdosproblems.com/definitions "Erdős Problems Definitions"
[2]: https://www.erdosproblems.com/348 "
  
    Erdős Problem #348
  
"
