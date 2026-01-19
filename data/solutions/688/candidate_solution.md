Let $n$ be large and fix (\varepsilon\in(0,1)).  Write
$
\mathcal P_\varepsilon(n)\ :=\ {p\ \text{prime}: n^\varepsilon<p\le n}.
$
For each (p\in\mathcal P_\varepsilon(n)) we choose one residue class (a_p\pmod p), and we ask that
[
\forall m\in[1,n]\cap\mathbb Z\quad \exists p\in\mathcal P_\varepsilon(n)\ \text{ with }\ m\equiv a_p\pmod p.
]
Then (\varepsilon_n) is the maximal (\varepsilon) for which such a choice is possible.

This is Erdős problem #688 (open). ([Erdős Problems][1])

## A clean necessary upper bound: (\varepsilon_n\le e^{-1+o(1)})

If we have a covering for some (\varepsilon), then counting “incidences” $(m,p)$ with (m\le n) and (m\equiv a_p\pmod p) gives a simple constraint.

For each prime (p\le n), a single residue class modulo $p$ hits at most (\lceil n/p\rceil) integers in $[1,n]$. Thus
[
|\\{(m,p):1\le m\le n,\ p\in\mathcal P_\varepsilon(n)\ m\equiv a_p!\pmod p\\}|
\ \le\ \sum_{p\in\mathcal P_\varepsilon(n)}\\(\frac np+1\\)
= n\sum_{p\in\mathcal P_\varepsilon(n)}\frac1p\ +\ O(\pi(n)).
]
But if every (m\in[1,n]) is covered at least once, the left-hand side is (\ge n). Hence
$
1 \ \le\ \sum_{p\in\mathcal P_\varepsilon(n)}\frac1p\ +\ O(\frac{\pi(n)}n)
\ =\ \sum_{n^\varepsilon<p\le n}\frac1p\ +\ o(1)
\qquad(n\to\infty),
$
using (\pi(n)=o(n)). By Mertens’ theorem for the prime harmonic series,
[
\sum_{p\le x}\frac1p=\log\log x + M + o(1),
]
so
$
\sum_{n^\varepsilon<p\le n}\frac1p
= (\log\log n + M + o(1)) - (\log\log(n^\varepsilon)+M+o(1))
= \log\log n - \log(\varepsilon\log n) + o(1)
= -\log\varepsilon + o(1).
$
Therefore the necessary condition ( \sum_{n^\varepsilon<p\le n} 1/p \ge 1-o(1)) implies
[
-\log\varepsilon \ \ge\ 1+o(1)\qquad\Longrightarrow\qquad \varepsilon \ \le\ e^{-1+o(1)}.
]
So
[
\boxed{\ \varepsilon_n \ \le\ e^{-1+o(1)}\ }.
]
[[nomath]](Mertens’ estimate is standard; see e.g. Tao’s exposition. $[What's new][2]$)[[/nomath]]

This is the best “soft” upper bound you get just from total coverage capacity.

## Erdős’ lower bound: (\varepsilon_n \gg \dfrac{\log\log\log n}{\log\log n})

Erdős proved
[
\boxed{\ \varepsilon_n \ \gg\ \frac{\log\log\log n}{\log\log n}\ }.
]
([Erdős Problems][1])

A useful way to understand why this scale appears is via **smooth numbers**.

Let (y=n^\varepsilon). If (as a first pass) you take (a_p\equiv 0\pmod p) for many primes (p>y), then you automatically cover every integer (\le n) having a prime factor (>y). The only integers this “multiples only” choice fails to cover are the $y$-smooth numbers [[nomath]](all prime factors $\le y$)[[/nomath]].

The count of $y$-smooth numbers up to $n$ is classically denoted (\Psi(n,y)), and for (y=n^\varepsilon) one has asymptotics of the shape
[
\Psi(n,y)\ \approx\ n,\rho!\left(\frac{\log n}{\log y}\right)
\ =\ n,\rho(1/\varepsilon),
]
where (\rho) is the Dickman–de Bruijn function. ([What's new][3])
For large $u$, (\rho(u)) decays very rapidly [[nomath]](roughly like $\exp(-u\log u(1+o(1)))$)[[/nomath]], so if you take
[
\varepsilon \asymp \frac{\log\log\log n}{\log\log n},
]
then (u=1/\varepsilon \asymp \frac{\log\log n}{\log\log\log n}) and one gets (\rho(u)) on the order of about (1/\log n), making (\Psi(n,y)) about (n/\log n). That size is small enough to be “mopped up” by the very large primes near $n$, which (because their modulus is so large) can be used to target individual remaining exceptions. [[nomath]](And $\pi(n)-\pi(n/2)\sim n/(2\log n)$ gives you $\asymp n/\log n$ such primes. $[Wikipedia][4]$)[[/nomath]]

This is essentially the heuristic behind Erdős’ bound.

## So what is known about (\varepsilon_n) and the question (\varepsilon_n=o(1))?

Putting the two displayed bounds together, the current state (as recorded in the Erdős problems database) is:

[
\frac{\log\log\log n}{\log\log n}\ \ll\ \varepsilon_n\ \le\ e^{-1+o(1)}.
]
([Erdős Problems][1])

And **the specific question “is (\varepsilon_n=o(1))?” is open** (again, as stated on the problem page). ([Erdős Problems][1])

* The **lower bound** already tends to $0$, so we know (\varepsilon_n) is *at least* a quantity that goes to $0$.
* But we do **not** have an **upper bound tending to $0$**; the simple counting argument only forces (\varepsilon_n\le 1/e+o(1)).

So at present the data are consistent with either:

* (\varepsilon_n\to 0) [[nomath]](perhaps on the Erdős scale $\sim \frac{\log\log\log n}{\log\log n}$, or another slowly vanishing scale)[[/nomath]], **or**
* (\varepsilon_n) staying bounded away from $0$ [[nomath]](up to the barrier $1/e$)[[/nomath]].

If you want, I can also sketch a more detailed version of the “smooth-number mop-up” construction that leads to the Erdős lower bound, and where the logarithmic ratio comes from quantitatively.

[1]: https://www.erdosproblems.com/688 "
  
    Erdős Problem #688
  
"
[2]: https://terrytao.wordpress.com/2013/12/11/mertens-theorems/?utm_source=chatgpt.com "Mertens' theorems | What's new"
[3]: https://terrytao.wordpress.com/2025/09/15/smooth-numbers-and-max-entropy/?utm_source=chatgpt.com "Smooth numbers and max-entropy | What's new - Terence Tao"
[4]: https://en.wikipedia.org/wiki/Prime_number_theorem?utm_source=chatgpt.com "Prime number theorem"
