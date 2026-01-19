Let (P^{+}(m)) denote the **largest prime factor** of $m$ [[nomath]](with the convention $P^{+}(1)=1$)[[/nomath]], and define
[
F(n):=P^{+}\bigl(n(n+1)\bigr).
]
Since (\gcd(n,n+1)=1), the prime factors of $n(n+1)$ are exactly the union of the prime factors of $n$ and of $n+1$, so
[
F(n)=\max{P^{+}(n),P^{+}(n+1)}\le n+1.
]

The nontrivial part of your question is the **growth of $F(n)$ as (n\to\infty)** [[nomath]](how small/large it must be in terms of $n$)[[/nomath]]. This is a classical Erdős problem and is still **open** in its sharp form. ([Erdős Problems][1])

## What is known (unconditional)

### 1) It goes to infinity

Pólya proved (in 1918) that
[
F(n)\to\infty \quad \text{as } n\to\infty,
]
so the largest prime factor of $n(n+1)$ cannot stay bounded. ([Erdős Problems][1])

### 2) Classical lower bound: $F(n)$ is at least on the order of (\log\log n)

Mahler showed a quantitative lower bound of the shape
[
F(n)\gg \log\log n,
]
i.e. $F(n)$ is at least a positive constant multiple of (\log\log n) for large $n$. ([Erdős Problems][1])

### 3) Best published lower bound (as of Pasten’s work): about ((\log\log n)^2/\log\log\log n)

Héctor Pasten proved a strong bound for largest prime factors of expressions [[nomath]](xy$x+y$)[[/nomath]]: for coprime integers (x<y),
[
P^{+}\bigl(xy(x+y)\bigr)\ge\kappa\cdot \frac{(\log_2 y)^2}{\log_3 y},
]
where (\log_2 y=\log\log y) and (\log_3 y=\log\log\log y). 

Taking $x=1$ and $y=n$ (which are coprime) gives [[nomath]](xy$x+y$=n$n+1$)[[/nomath]], so
[
F(n)=P^{+}(n(n+1));\gg;\frac{(\log\log n)^2}{\log\log\log n}.
]
This is the strongest general lower bound currently highlighted for this problem. 

### 4) There are infinitely many $n$ where $F(n)$ is “very small” relative to $n$

Schinzel observed that for infinitely many $n$,
[
F(n)\le n^{O(1/\log\log\log n)},
]
so along an infinite sequence of $n$’s, the exponent tends to $0$ and $F(n)$ can be far smaller than any fixed power (n^\varepsilon) [[nomath]](for large enough $n$ in that subsequence)[[/nomath]]. ([Erdős Problems][1])

## What is conjectured

A widely cited heuristic guess is that the “right” scale should be roughly ((\log n)^2). In particular, Erdős conjectured that for every (\varepsilon>0) there are infinitely many $n$ such that
[
F(n)<(\log n)^{2+\varepsilon},
]
and it is also suggested that one might have a general lower bound of order ((\log n)^2). ([Erdős Problems][1])

## Where to look up values

The sequence (F(n)=P^{+}(n(n+1))) is OEIS **A074399**, which lists the first values and references. ([OEIS][2])

So, in short: $F(n)$ can vary wildly with $n$, it does go to infinity, the best general lower bound known is on the order of ((\log\log n)^2/\log\log\log n), and determining the true order of magnitude remains open. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/368 "
  
    Erdős Problem #368
  
"
[2]: https://oeis.org/A074399 "A074399 - OEIS"
