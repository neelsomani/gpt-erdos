This is **open**.

It is recorded (verbatim) as **Erdős Problem #312** (from Erdős–Graham, 1980): asking whether there is an absolute constant (c>0) such that whenever a finite multiset $A$ of (positive) integers has
[
R(A):=\sum_{n\in A}\frac1n>K,
]
one can find a submultiset (S\subseteq A) with
[
1-e^{-cK}<\sum_{n\in S}\frac1n\le 1.
]
The Erdős Problems site lists it as **OPEN** as of Jan 16, 2026. ([Erdős Problems][1])

A common reformulation is to define the “best deficit below (1)”:
$
\varepsilon(A):=\min\\{1-\sum_{n\in S}\frac1n:\ S\subseteq A,\ \sum_{n\in S}\frac1n\le 1\\},
$
so the question is whether there is (c>0) with
[
\varepsilon(A)\ \le\ e^{-c,R(A)}
]
for all sufficiently large $A$. ([Erdős Problems][2])

### What *is* known

Erdős and Graham proved a **much weaker** (polynomial) approximation: they “knew this” with the exponential term (e^{-cK}) replaced by a bound of the form (C/K^2). In other words, there is an absolute constant $C$ such that from (R(A)>K) one can always extract (S\subseteq A) with
[
1-\frac{C}{K^2}\ <\ \sum_{n\in S}\frac1n\ \le\ 1.
]
This is explicitly noted on the Erdős Problems entry for #312. ([Erdős Problems][1])

### Why the exponential version is nontrivial

It’s not even true that (R(A)>K>1) forces a subset sum **equal** to $1$; one can build multisets where no submultiset has reciprocal sum exactly $1$. For example, a construction discussed on the Erdős Problems forum takes, for each prime (p\le N), exactly $p-1$ copies of $p$. It has (R(A)\sim N/\log N) but still no subset sums to $1$; in that example one can lower-bound (\varepsilon(A)) by about (1/N#\approx e^{-N}), which corresponds to (\varepsilon(A)\gtrsim e^{-R(A)\log R(A)}). ([Erdős Problems][2])
(That discussion is informal, but it illustrates the kind of number-theoretic obstructions people think about.)

### Bottom line

As of the current literature summaries, **no one knows** whether you can always push the deficit down to something **exponentially small in $K$** [[nomath]](i.e., $\varepsilon(A)\le e^{-cK}$ for a universal $c>0$)[[/nomath]]. The best generally stated guarantee in this direction remains the **(O(1/K^2))**-type bound attributed to Erdős–Graham. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/312 "
  
    Erdős Problem #312
  
"
[2]: https://www.erdosproblems.com/forum/thread/312 "

    Erdős Problem #312 - Discussion thread

"
