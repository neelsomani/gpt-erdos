## This is (still) an open Erdős–Selfridge problem

What you ask for,
[
h(n)\sim c\Big(\frac{n}{\log n}\Big)^{1/2},
]
for some constant (c>0), is exactly the asymptotic Erdős conjectured in 1982, and (as far as the current literature indicates) it is **not proved**. Erdős proved only two–sided bounds
$
c_1(\frac{n}{\log n})^{1/2}<h$n$<c_2(\frac{n}{\log n})^{1/2}
$
for all large $n$, and explicitly remarked that getting a true asymptotic seems to require more knowledge about gaps between consecutive primes. 

So I can’t honestly give a complete unconditional proof of the stated (\sim) asymptotic, because it would resolve an open problem. What I *can* do is:

1. show the standard reduction to primes in short intervals,
2. prove the known (\asymp) result [[nomath]](order of magnitude $\sqrt{n/\log n}$)[[/nomath]], and
3. explain the (conjectural) value of $c$ predicted by probabilistic models.

That matches the state of the art described in the MathOverflow discussion and the Erdős-problems listing. ([MathOverflow][1])

---

## 1) Legendre’s formula and the key reduction

Let (v_p(n!)) be the exponent of a prime $p$ in $n!$. Legendre’s formula says
[
v_p(n!)=\sum_{j\ge 1}\Big\lfloor \frac{n}{p^j}\Big\rfloor.
]
([Erdős Problems][2])

**Observation 1.** If (p>\sqrt n) then (p^2>n), so all terms with (j\ge2) vanish and
[
v_p(n!)=\Big\lfloor\frac{n}{p}\Big\rfloor\qquad (p>\sqrt n).
]
This is the crucial simplification. ([MathOverflow][1])

**Observation 2.** The primes (p\le \sqrt n) contribute at most (\pi(\sqrt n)) exponents, hence at most (\pi(\sqrt n)) *distinct* exponents. Since
[
\pi(\sqrt n)\sim \frac{\sqrt n}{\log(\sqrt n)}=\frac{2\sqrt n}{\log n}=o!\left(\sqrt{\frac{n}{\log n}}\right),
]
their contribution is negligible on the (\sqrt{n/\log n}) scale. ([MathOverflow][1])

Therefore, the main term in $h(n)$ comes from primes (p>\sqrt n), and for those primes the exponent set is
[
\Big{\Big\lfloor\frac{n}{p}\Big\rfloor:\ p\ \text{prime},\ \sqrt n<p\le n\Big}.
]

Now note that (\lfloor n/p\rfloor=k) is equivalent to
[
\frac{n}{k+1}<p\le \frac{n}{k}.
]
So define intervals
[
I_k:=\Big(\frac{n}{k+1},\frac{n}{k}\Big]\qquad(1\le k\le \lfloor \sqrt n\rfloor).
]
Then for (k\le \sqrt n), the value $k$ occurs among the exponents (v_p(n!)) with (p>\sqrt n) **iff** (I_k) contains at least one prime.

So an equivalent formulation [[nomath]](up to an error $o(\sqrt{n/\log n})$)[[/nomath]] is:

> Count how many (1\le k\le \sqrt n) have (I_k\cap\mathbb P\neq \emptyset). ([MathOverflow][1])

This is exactly the reduction noted in the MathOverflow answer. ([MathOverflow][1])

---

## 2) What *is* known unconditionally: (h(n)\asymp \sqrt{n/\log n})

### Upper bound (h(n)\ll \sqrt{n/\log n})

Fix a parameter (y=y(n)) with (1\le y\le \sqrt n). Split the primes (p>\sqrt n) into:

* **Large primes:** (p> n/y). Then (\lfloor n/p\rfloor<y), so these primes can contribute **at most $y$** distinct values.

* **Medium primes:** (\sqrt n < p \le n/y). Each such prime can contribute at most one new exponent value, so the number of distinct exponents from this range is (\le \pi(n/y)-\pi(\sqrt n)\le \pi(n/y)).

Also add the (\pi(\sqrt n)) possible exponents from (p\le\sqrt n).

Thus
[
h(n)\ \le\ y\ +\ \pi(n/y)\ +\ \pi(\sqrt n).
]

Now choose
[
y=t\sqrt{\frac{n}{\log n}}
]
with fixed (t>0). By the prime number theorem [[nomath]](and $\pi(\sqrt n)=o(\sqrt{n/\log n})$)[[/nomath]],
[
\pi(n/y)\sim \frac{n/y}{\log(n/y)}\sim \frac{\frac{1}{t}\sqrt{n\log n}}{\frac12\log n}\sim \frac{2}{t}\sqrt{\frac{n}{\log n}}.
]
So
[
h(n)\ \le\ \Big(t+\frac{2}{t}+o(1)\Big)\sqrt{\frac{n}{\log n}}.
]
Optimizing (t+2/t) gives (t=\sqrt2) and hence
[
h(n)\ \le\ (2\sqrt2+o(1))\sqrt{\frac{n}{\log n}}.
]
This supplies an explicit admissible (c_2).

[[nomath]](These “split at $n/y$” upper bounds are the standard way to see $h(n)\ll \sqrt{n/\log n}$; Erdős proved such an upper bound in his 1982 paper. )[[/nomath]]

### Lower bound (h(n)\gg \sqrt{n/\log n})

This is subtler, because it needs a statement about primes not clustering too much in the relevant short intervals. Erdős uses a sieve (Brun’s method) input: for sufficiently small (\delta>0), the number of prime pairs (p<q\le X) with gap (q-p<\delta\log X) is (\ll \delta X/\log X). 

Here’s how that yields many **distinct** (\lfloor n/p\rfloor) values.

Let (K:=\sqrt{n/\log n}) and pick a **large fixed constant** (C>0). Set
[
y:=CK,\qquad x:=\frac{n}{y}\sim \frac{1}{C}\sqrt{n\log n}.
]
Consider primes in the interval $(x/2,x]$. For each prime $p\in(x/2,x]$ we have
[
\Big\lfloor\frac{n}{p}\Big\rfloor\in[y,2y],
]
so these primes contribute exponents among the set ${y,y+1,\dots,2y}$ and thus correspond exactly to the intervals $I_k$ with $k\in[y,2y]$.

Let $b_k$ be the number of primes in $I_k$ for $k\in[y,2y]$. Then:

* the number of **distinct** exponents in this range is
  $
  N:=|\\{k\in[y,2y]: b_k\ge1\\}|=\sum_{k=y}^{2y}\mathbf 1_{b_k\ge 1},
  $
* the total number of primes in the union $\bigcup_{k=y}^{2y}I_k=(x/2,x]$ is
  $
  P:=\sum_{k=y}^{2y} b_k=\pi(x)-\pi(x/2).
  $

By PNT,
$
P=\pi(x)-\pi(x/2)\sim \frac{x}{2\log x}\sim \frac{1}{C}\sqrt{\frac{n}{\log n}}=\frac{1}{C}K.
$

Now compare (N) to (P). If an interval (I_k) contains (b_k\ge2) primes, then it contributes at least (\binom{b_k}{2}\ge b_k-1) prime pairs whose gap is (\le |I_k|). But for (k\ge y),
[
|I_k|=\frac{n}{k}-\frac{n}{k+1}=\frac{n}{k(k+1)}\le \frac{n}{y^2}\asymp \frac{\log n}{C^2}.
]
Since (\log x\sim \tfrac12\log n), we can write (|I_k|\le \delta\log x) with (\delta\asymp 1/C^2), and by taking (C) large we can ensure (\delta) is “sufficiently small” for Erdős’s Brun-sieve bound. 

Let (S) be the number of prime pairs in $(x/2,x]$ with gap (\le \delta\log x). Erdős’s Brun-method estimate gives
[
S\ \ll\ \delta\cdot \frac{x}{\log x}\ \asymp\ \frac{1}{C^2}\cdot \frac{x}{\log x}\ \asymp\ \frac{1}{C^2}\cdot \frac{1}{C}K=\frac{1}{C^3}K.
]


But
[
P-N = \sum_{k=y}^{2y}\big(b_k-\mathbf 1_{b_k\ge1}\big)=\sum_{k=y}^{2y}\max(0,b_k-1)\ \le\ \sum_{k=y}^{2y}\binom{b_k}{2}\ \le\ S.
]
Therefore
[
N\ \ge\ P-S \ =\ \Big(\frac{1}{C}+O!\Big(\frac{1}{C^3}\Big)\Big)K.
]
Choosing (C) as a fixed large constant makes the coefficient positive, hence
[
h(n)\ \ge\ N\ \gg\ \sqrt{\frac{n}{\log n}}.
]

Putting upper and lower bounds together gives the unconditional theorem
[
h(n)\asymp \Big(\frac{n}{\log n}\Big)^{1/2},
]
which is exactly what Erdős and Selfridge proved. 

---

## 3) Why the asymptotic constant $c$ is out of reach (currently)

To upgrade $\asymp$ to
[
h(n)=(c+o(1))\sqrt{\frac{n}{\log n}}
]
one needs to understand, in the “critical range” $k\asymp \sqrt{n/\log n}$, the **limiting proportion** of the intervals $I_k$ that contain a prime. In that range the interval lengths $|I_k|$ are $\asymp \log n$, i.e. $\asymp \log x$ where $x\asymp n/k$, so this becomes a problem about primes in intervals of length comparable to $\log x$, essentially about the fine-scale statistics of prime gaps. Erdős already pointed to this obstruction, and the MathOverflow discussion reiterates that current technology does not give the needed full asymptotics in that regime. 

---

## 4) The predicted value of $c$ (heuristic / conditional)

Both the MathOverflow answer and the Erdős-problems discussion report that the **Cramér random model** suggests
[
c=\int_0^\infty \Big(1-e^{-2/t^2}\Big),dt=\sqrt{2\pi}.
]
([MathOverflow][1])

Very briefly: scale (k=t\sqrt{n/\log n}). Then (I_k) has length (\sim n/k^2\sim (\log n)/t^2), and it sits near (x=n/k\sim \sqrt{n\log n}/t), so the “expected number of primes” in (I_k) is (\lambda(t)\approx |I_k|/\log x\approx 2/t^2). If primes were Poisson with that mean, $\mathbb P(I_k\ \text{contains a prime})\approx 1-e^{-\lambda(t)}=1-e^{-2/t^2}$, and summing over $k$ becomes a Riemann integral giving (\sqrt{2\pi}). ([Erdős Problems][2])

But turning that heuristic into a proof appears to require very strong uniform “prime $k$-tuple”–type information [[nomath]](essentially controlling all moments of the prime counts in these $\asymp \log x$-length intervals)[[/nomath]], which is far beyond what is known unconditionally. ([MathOverflow][1])

---

If you want, I can also write up the above (\asymp) proof in a more “lecture notes” style, with all constants tracked explicitly and with the precise sieve lemma stated in the form Erdős uses.

[1]: https://mathoverflow.net/questions/413332/distinct-exponents-in-the-factorization-of-the-factorial-a-problem-of-erd%C5%91s "nt.number theory - Distinct exponents in the factorization of the factorial, a problem of Erdős - MathOverflow"
[2]: https://www.erdosproblems.com/forum/thread/912 "https://www.erdosproblems.com/forum/thread/912"
