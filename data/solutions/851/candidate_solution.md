This is **open**.

In fact it is explicitly listed as **Erdős Problem #851**: whether for every (\epsilon>0) there is a bounded (r=r(\epsilon)) so that the set
[
{,2^k+n:\ k\ge 0,\ n\ \text{has at most }r\text{ prime divisors},}
]
has (natural) density at least (1-\epsilon). ([Erdős Problems][1])

### What is known

* **For $r=1$** [[nomath]](so $n$ is prime, i.e. numbers of the form $p+2^k$)[[/nomath]]: Romanov (1934) proved this set has **positive lower density**. Moreover, van der Corput and Erdős showed that a **positive proportion** of integers are *not* of the form (p+2^k), and Erdős even constructed an **arithmetic progression** containing no such integers (via covering congruences). ([Mathematics Universität Rostock][2])
  So $r=1$ definitely cannot give density (1-\epsilon) for small (\epsilon).

* There are **explicit numerical bounds** for the $r=1$ density (“Romanov’s constant”): e.g. Elsholtz–Schlage-Puchta prove a lower density (\ge 0.107648) and cite an upper bound (\le 0.49095). ([Mathematics Universität Rostock][2])

* A closely related question (Erdős Problem #205) asked whether **every sufficiently large** $n$ can be written as (n=2^k+m) with (\Omega(m)<\log\log m). That “for all sufficiently large $n$” statement was recently recorded as **disproved**, with an explicit quantitative strengthening: there are infinitely many $n$ such that **for every** (2^k<n), the number (n-2^k) has (\gg \bigl(\frac{\log n}{\log\log n}\bigr)^{1/2}) prime factors (counted with multiplicity). ([Erdős Problems][3])
  This does **not** settle #851, since #851 only asks for density (1-\epsilon), not “all sufficiently large”.

### Heuristic picture

If you model “(n-2^k) is $r$-almost prime” as a random event, then for a typical large $n$ you have about (\log n) choices of $k$, and the chance that a random integer near $n$ has (\le r) prime factors is about (\asymp (\log\log n)^{r-1}/\log n) [[nomath]](for fixed $r$)[[/nomath]]. So the *expected* number of successful $k$’s is (\asymp (\log\log n)^{r-1}), which tends to infinity as soon as (r\ge 2). This strongly suggests that already $r=2$ should give density $1$.

But turning that heuristic into a proof seems to be the hard part, and as of the current status recorded for Erdős Problem #851, no such theorem is known. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/851 "https://www.erdosproblems.com/851"
[2]: https://www.mathematik.uni-rostock.de/storages/uni-rostock/Alle_MNF/Mathematik/Struktur/Lehrstuehle/Algebra/papers/Rom6k.pdf "https://www.mathematik.uni-rostock.de/storages/uni-rostock/Alle_MNF/Mathematik/Struktur/Lehrstuehle/Algebra/papers/Rom6k.pdf"
[3]: https://www.erdosproblems.com/205 "https://www.erdosproblems.com/205"
