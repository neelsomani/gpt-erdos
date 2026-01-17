As far as is currently known, **no such pair of finite prime sets is known**. In fact, this is a recorded open problem of Erdős (often cited as **Erdős Problem #307**). ([Erdős Problems][1])

What *is* known are some necessary consequences if such sets (P,Q) existed:

### 1) If $P,Q$ work, then (P\cap Q=\varnothing), and the “numerators swap”

Let
[
A=\sum_{p\in P}\frac1p,\qquad B=\sum_{q\in Q}\frac1q.
]
Write $A$ over the common denominator (D_P:=\prod_{p\in P}p):
[
A=\frac{N_P}{D_P},\qquad N_P:=\sum_{p\in P}\frac{D_P}{p}\in\mathbb Z.
]
A key observation: for any fixed (p_0\in P),
[
N_P \equiv \frac{D_P}{p_0}\pmod{p_0},
]
and (\frac{D_P}{p_0}\not\equiv 0\pmod{p_0}). Hence **no prime in $P$ divides (N_P)**, so (\gcd(N_P,D_P)=1). Similarly, if (D_Q:=\prod_{q\in Q}q) and (N_Q:=\sum_{q\in Q}D_Q/q), then (\gcd(N_Q,D_Q)=1).

Now the equation (AB=1) becomes
[
\frac{N_P}{D_P}\cdot\frac{N_Q}{D_Q}=1\quad\Longrightarrow\quad N_PN_Q=D_PD_Q.
]
Because (\gcd(N_P,D_P)=1), all prime factors of (D_P) must divide (N_Q), so (D_P\mid N_Q). Likewise (D_Q\mid N_P).

But (D_P\mid N_Q) means every prime in $P$ divides (N_Q), and we already know **no prime in $Q$ divides (N_Q)**. Therefore (P\cap Q=\varnothing). Moreover, since (N_PN_Q) has *exactly* the prime factors in (P\cup Q), the divisibilities (D_Q\mid N_P) and (D_P\mid N_Q) force
[
N_P=D_Q,\qquad N_Q=D_P,
]
so
[
\sum_{p\in P}\frac1p=\frac{D_Q}{D_P},\qquad \sum_{q\in Q}\frac1q=\frac{D_P}{D_Q}.
]
(This disjointness and “swap” phenomenon is one of the standard first deductions about the problem.) ([Erdős Problems][1])

### 2) A size obstruction: (\displaystyle \sum_{r\in P\cup Q}\frac1r \ge 2)

Since (AB=1), we have (B=1/A). Thus
[
\sum_{r\in P\cup Q}\frac1r
= \sum_{p\in P}\frac1p+\sum_{q\in Q}\frac1q
= A+\frac1A \ge 2,
]
with equality only if (A=1). ([Erdős Problems][1])

Consequently, any hypothetical solution must use **a lot** of primes: you need at least enough distinct primes for their reciprocal sum to reach (2). [[nomath]](A quick computation shows that the first 58 primes fall just short of $2$, while the first 59 exceed $2$, so $|P\cup Q|\ge 59$. Some write this informally as “at least about 60 primes.”)[[/nomath]] ([Erdős Problems][1])

### 3) If you drop “prime” and only require coprime integers, solutions exist (but that’s a different problem)

If you allow $P,Q$ to be sets of pairwise coprime **integers** (not necessarily primes), then there are easy examples such as
[
1=\left(1+\frac15\right)\left(\frac12+\frac13\right),
]
but for the genuine “primes only” version, no example is known. ([Erdős Problems][1])

---

So the honest answer to your question is: **this is (still) open**—no one currently knows whether such finite prime sets (P,Q) exist. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/307 "https://www.erdosproblems.com/307"
