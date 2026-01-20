Let me rename (m_n) as $E(n)$, since this is exactly the **Euler minimum function**
[
E(n):=\min{k\ge 1:\ n\mid \varphi(k)},
]
introduced/studied by Moree–Roskam and Sándor. 
Your (p_n) is the least prime (p\equiv 1\pmod n).

### Basic facts and two infinite families

1. **Always (m_n\le p_n).**
   Indeed (\varphi(p_n)=p_n-1) is divisible by $n$, so (p_n) is an admissible candidate in the definition of (m_n). (This is the “trivial” inequality noted in the Erdős problem statement.) ([Erdős Problems][1])

2. **Infinitely many $n$ with equality (m_n=p_n).**
   If (n=q-1) for a prime $q$, then (m_n=q). A quick proof: (\varphi(q)=q-1=n), so (m_n\le q); but for any (m<q) we have (\varphi(m)\le m-1<q-1=n), so (\varphi(m)) cannot be a positive multiple of $n$. Hence (m_n=q). Also (p_n=q) because (q\equiv 1\pmod{q-1}) and no smaller prime can be (1\pmod{q-1}). [[nomath]](Sándor records the identity $E(p-1)=p$ for primes $p$.)[[/nomath]] ([Erdős Problems][1])

So the strict inequality (m_n<p_n) cannot hold for all $n$, but it could still hold for “almost all” $n$.

3. **Infinitely many $n$ with strict inequality (m_n<p_n).**
   A very simple explicit family is
   [
   n=2^{2k+1}\quad (k\ge 1).
   ]
   Then (\varphi(2n)=\varphi(2^{2k+2})=2^{2k+1}=n), so (m_n\le 2n). On the other hand, the first number (>1) that is (\equiv 1\pmod n) is (n+1=2^{2k+1}+1), and for odd exponents (2^{2k+1}\equiv 2\pmod 3), so (n+1\equiv 0\pmod 3), hence $n+1$ is composite; therefore the first possible prime in that progression is (\ge 2n+1), so (p_n\ge 2n+1>2n\ge m_n). ([Erdős Problems][1])

So (m_n<p_n) holds infinitely often.

---

## What is known about your three questions?

These exact questions are listed as **Erdős Problem #456**, and (as of the most recent public tracking I can find) are regarded as **open** in general. ([Erdős Problems][1])

So:

### $A$ “Is it true that (m_n<p_n) for almost all $n$?”

**Open.** ([Erdős Problems][1])

A useful reformulation: since (p_n) is prime,
[
m_n<p_n \quad\Longleftrightarrow\quad m_n\ \text{is composite}.
]
Indeed, if (m_n) were prime, then (n\mid \varphi(m_n)=m_n-1), hence (m_n\equiv 1\pmod n), forcing (m_n\ge p_n), and since always (m_n\le p_n), we would have (m_n=p_n).

So Erdős’s question is essentially asking whether $E(n)$ is composite for density $1$ of integers $n$.

### $B$ “Does (p_n/m_n\to\infty) for almost all $n$?”

**Also open** (as posed). ([Erdős Problems][1])

Note that this is strictly stronger than $A$: if (p_n/m_n\to\infty) for almost all $n$, then in particular (m_n<p_n) for almost all $n$ [[nomath]](because the ratio would eventually be $>1$ on a density‑one set)[[/nomath]].

### $C$ “Are there infinitely many primes $p$ such that $p-1$ is the only $n$ for which (m_n=p)?”

**Open** (in this generality). ([Erdős Problems][1])

Some structure you can keep in mind:

* For every prime $p$, you always have (m_{p-1}=p) (as above). 
* If (m_n=p) for some prime $p$, then necessarily (n\mid p-1) [[nomath]](since $n\mid\varphi(p)=p-1$)[[/nomath]]. So any other $n$ with (m_n=p) must be a **proper divisor** of $p-1$.
* A concrete obstruction to “uniqueness” comes from prime divisors (q\mid(p-1)). For a prime $q$, Moree–Roskam show
  [
  E(q)=\min{q^2,\ p(q,1)},
  ]
  where $p(q,1)$ is the least prime (\equiv 1\pmod q). ([FQ Math][2])
  Thus if $p$ happens to be the least prime (\equiv 1\pmod q) and (p<q^2), then (E(q)=p), giving a second $n=q$ with (m_n=p). This is exactly what happens for “safe primes” (p=2q+1): there is no room for a smaller prime (\equiv 1\pmod q) because the only candidate below $p$ is $q+1$, which is even (>2), hence composite.

On the “positive” side: if $p$ is a **Fermat prime** (p=2^{2^t}+1), then $p-1$ is a power of $2$, and for every proper divisor (2^r\mid(p-1)) one has
[
\varphi(2^{r+1})=2^r,
]
so (m_{2^r}\le 2^{r+1}<p). Hence Fermat primes do satisfy the uniqueness property you ask about. (This doesn’t resolve the question, because it is unknown whether there are infinitely many Fermat primes.)

---

## Bottom line

* There are **infinitely many** $n$ with (m_n=p_n) [[nomath]](e.g. $n=p-1$)[[/nomath]]. ([Erdős Problems][1])
* There are **infinitely many** $n$ with (m_n<p_n) [[nomath]](e.g. $n=2^{2k+1}$, $k\ge 1$)[[/nomath]]. ([Erdős Problems][1])
* The three “almost all” / “ratio (\to\infty)” / “infinitely many unique primes” questions, as stated, are part of an Erdős problem and are currently regarded as **open**. ([Erdős Problems][1])

If you want, I can also lay out a couple of plausible heuristic models for $E(n)$ and (p_n) [[nomath]](and what they predict for the density of prime values of $E(n)$)[[/nomath]], but none of that is known to be provable at present.

[1]: https://www.erdosproblems.com/456 "https://www.erdosproblems.com/456"
[2]: https://www.fq.math.ca/Scanned/33-4/moree.pdf "https://www.fq.math.ca/Scanned/33-4/moree.pdf"
