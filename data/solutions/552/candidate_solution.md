Let
[
f(n):=R(C_4,S_n)=R(C_4,K_{1,n}),
]
where (S_n=K_{1,n}) is the star on $n+1$ vertices.

A convenient equivalent formulation (used throughout the literature) is:

* (\overline G) contains (K_{1,n}) iff some vertex of $G$ has at least $n$ **non-neighbors**, i.e. iff (\delta(G)\ge |V(G)|-n) fails.
* Thus $f(n)$ is the least $N$ such that **no** (C_4)-free graph $G$ on $N$ vertices can have (\delta(G)\ge N-n). 

## What is known about $R(C_4,S_n)$

### General upper bound (Parsons)

Parsons proved an essentially best-possible general upper bound of the form
[
f(n)\le n+\lceil\sqrt n\rceil+1,
]
and in fact one can state it in the slightly sharper form
[
f(n)\le n+\left\lceil\sqrt{n-1}\right\rceil+1\qquad(n\ge2).
]
This appears as Corollary 4 in the 2024 Boza paper (citing earlier work). 

[[nomath]](Older statements are often written as $f(n)\le n+\lfloor\sqrt{n-1}\rfloor+2$, with a refinement by 1 in certain cases; see below. ([SciSpace][1]))[[/nomath]]

### General lower bound (Burr–Erdős–Faudree–Rousseau–Schelp)

A classical lower bound due to Burr et al. (1989) is
[
f(n)\ \ge\ n+\sqrt n-6n^{11/40}.
]
This is explicitly recorded in multiple modern summaries of the problem. ([Erdős Problems][2])

So, quantitatively,
$
n+\sqrt n-O(n^{11/40})\ \le\ f(n)\ \le\ n+ \sqrt n+O(1).
$
([Erdős Problems][2])

### Exact values for infinitely many (n) (prime power constructions)

Parsons also determined $f(n)$ exactly for two infinite families (coming from finite geometry / projective planes). In the formulation consistent with your (S_n=K_{1,n}):

If $q$ is a prime power, then
$
f(q^2)=q^2+q+1 = q^2+\lceil\sqrt{q^2}\rceil+1,
$
and
$
f(q^2+1)=q^2+q+2 = (q^2+1)+\lceil\sqrt{q^2+1}\rceil.
$
In particular, both “(n+\lceil\sqrt n\rceil)” and “(n+\lceil\sqrt n\rceil+1)” occur infinitely often. ([SciSpace][1])

There are also many further exact evaluations when (n=q^2\pm t) with (0\le t\le q) [[nomath]](for prime power $q$)[[/nomath]], but no general closed form is known for all $n$. ([Erdős Problems][2])

## Your “(n+\sqrt n-c)” question

Your inequality
$
R(C_4,S_n)\le n+\sqrt n-c \quad\text{infinitely often for every fixed }c>0
$
is a famous open problem (an Erdős $100 problem). It is stated explicitly as an open problem in modern sources tracking Erdős’s problem lists, and it originates in Burr–Erdős–Faudree–Rousseau–Schelp (1989). ([Erdős Problems][2])

### What evidence points which way?

* **No known examples** currently force $f(n)$ below (n+\sqrt n) by a fixed constant; in all *known exact* cases one has
  [
  f(n)=n+\lceil\sqrt n\rceil \quad\text{or}\quad f(n)=n+\lceil\sqrt n\rceil+1,
  ]
  hence (f(n)\ge n+\sqrt n). ([Erdős Problems][2])
* Some authors have even speculated that the pattern (f(n)=n+\lceil\sqrt n\rceil+{0,1}) might hold for **all** (n\ge2); if that were true, then your inequality would be **false** for every (c>0). But this speculation is itself unproved. ([Erdős Problems][2])

## Bottom line

* The exact determination of $R(C_4,S_n)$ for **all** $n$ is **unknown**.
* Best general bounds currently:
  [
  n+\sqrt n-6n^{11/40}\ \le\ R(C_4,S_n)\ \le\ n+\left\lceil\sqrt{n-1}\right\rceil+1.
  ]
  ([Erdős Problems][2])
* Infinitely many exact values are known, e.g. for (n=q^2) and (n=q^2+1) with $q$ a prime power. ([SciSpace][1])
* Your “(n+\sqrt n-c)” statement is **open**. ([Erdős Problems][2])

[1]: https://scispace.com/pdf/a-remark-on-star-c4-and-wheel-c4-ramsey-numbers-1yzuvi3id8.pdf "A remark on star-C4 and wheel-C4 Ramsey numbers"
[2]: https://www.erdosproblems.com/prizes/100 "https://www.erdosproblems.com/prizes/100"
