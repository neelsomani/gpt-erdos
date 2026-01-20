Not known in general — this is an open problem.

### Why $k=1$ is special

If (2^n \equiv 1 \pmod n) with (n>1), let $p$ be the smallest prime divisor of $n$. Then (2^n\equiv 1\pmod p), so the multiplicative order (\operatorname{ord}_p(2)) divides $n$. But (\operatorname{ord}_p(2)\mid (p-1)), hence (\operatorname{ord}_p(2)<p). Since $p$ is the smallest prime factor of $n$, the only way a positive integer (<p) can divide $n$ is if it equals $1$. Thus (\operatorname{ord}_p(2)=1), i.e. (2\equiv 1\pmod p), impossible. So there is **no** solution for (n>1). ([OEIS][1])

[[nomath]](So excluding $k=1$ is necessary.)[[/nomath]]

### The general statement is a conjecture (open)

Your question is exactly **Erdős Problem #479**, attributed to a conjecture of Ron Graham:

> For every (k\neq 1), are there infinitely many $n$ with (2^n\equiv k\pmod n)?

This is currently listed as **open**. ([Erdős Problems][2])

A nice indication of how hard it is: for $k=3$, the *smallest* (n>1) with (2^n\equiv 3\pmod n) is already
[
n = 4{,}700{,}063{,}497,
]
and OEIS records only a handful of solutions below (10^{18}). ([Erdős Problems][2])

### What *is* known (examples where “infinitely many” is proved)

Although the full “all (k\neq 1)” statement is open, there are specific $k$ for which infinitely many solutions are known:

* $k=0$: take (n=2^m). Then (2^n) is divisible by $n$, so (2^n\equiv 0\pmod n).
* $k=2$: every odd prime $p$ satisfies (2^p\equiv 2\pmod p) by Fermat, so infinitely many $n$.
* More generally, it is reported/proved for (k=2^i) ((i\ge1)) and also for (k=-1). ([Erdős Problems][2])

### Bottom line

* The claim “for all (k\neq 1) there are infinitely many $n$” is **conjectured**, but **unproved** in general. ([Erdős Problems][2])
* For some $k$ [[nomath]](notably $k=0$, $k=2$, and $k=2^i$, plus $k=-1$)[[/nomath]] there are **known infinite families**. ([Erdős Problems][2])
* $k=1$ is the only residue known to be impossible for (n>1). ([OEIS][1])

[1]: https://oeis.org/wiki/2%5En_mod_n "2^n mod n - OeisWiki"
[2]: https://www.erdosproblems.com/479 "
  
    Erdős Problem #479
  
"
