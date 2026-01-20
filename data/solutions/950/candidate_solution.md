This is (essentially verbatim) **Erdős’s Problem #950**. Erdős wrote that it is *likely* that
$
\liminf_{n\to\infty} f(n)=1,\qquad \limsup_{n\to\infty} f(n)=\infty,
$
and he also asked whether perhaps (f(n)=o(\log\log n)). All of these are **open**. ([Rényi Institute][1])

## What is known unconditionally

### 1) First and second moment: $f(n)$ is typically (\asymp 1)

De Bruijn–Erdős–Turán proved the asymptotics
$
\sum_{n<x} f(n) \sim x,\qquad \sum_{n<x} f(n)^2 \sim x,
$
so the mean and mean square of $f(n)$ over (n\le x) are both asymptotically 1. ([Erdős Problems][2])
In particular, “on average” $f(n)$ behaves like 1; but this does not control (\liminf) or (\limsup).

A quick corollary of the second moment is that large values are rare in density: for any (T>0),
[
|\\{n\le x:\ f(n)\ge T\\}|\ \ll\ \frac{x}{T^2}.
]
[[nomath]](This is just Markov/Chebyshev using $\sum_{n\le x} f(n)^2\sim x$.)[[/nomath]] ([Erdős Problems][2])

### 2) A general upper bound: (f(n)\ll \log\log n) for all $n$

You can get a clean unconditional bound from the **Brun–Titchmarsh theorem in short intervals**, which gives [[nomath]](in particular, for $q=1$)[[/nomath]]
$
\pi(x)-\pi(x-y)\ \le\ \frac{2y}{\log y}\qquad (y<x).
$
([Oxford University Research Archive][3])

Now dyadically decompose the sum by the size of the gap (d=n-p). For (j\ge 1), let
$
\mathcal P_j={p<n:\ 2^j < n-p \le 2^{j+1}}.
$
Then for (p\in\mathcal P_j), we have (\frac{1}{n-p}\le 2^{-j}), hence
$
\sum_{p\in\mathcal P_j}\frac{1}{n-p}\ \le\ \frac{|\mathcal P_j|}{2^j}.
$
But (|\mathcal P_j|) is the number of primes in the interval $(n-2^{j+1},,n-2^{j}]$, which has length (2^j), so Brun–Titchmarsh gives
[
|\mathcal P_j| \le \pi(n-2^{j})-\pi(n-2^{j+1}) \ \ll\ \frac{2^j}{\log 2^j}\asymp \frac{2^j}{j}.
]
Therefore
[
\sum_{p\in\mathcal P_j}\frac{1}{n-p}\ \ll\ \frac{1}{j}.
]
Summing over (j\le \log_2 n) yields
[
f(n)\ =\ \sum_{j\le \log_2 n}\sum_{p\in\mathcal P_j}\frac{1}{n-p}\ \ll\ \sum_{j\le \log_2 n}\frac{1}{j}\ \asymp\ \log\log n.
]
So
[
\boxed{f(n)\ll \log\log n\quad\text{for all }n.}
]
(The implied constant is absolute.) ([Oxford University Research Archive][3])

This is the strongest “soft” unconditional statement of the type you asked: it shows $f(n)$ can’t grow faster than (\log\log n) up to constants.

## What is not known

### Is (\displaystyle \liminf f(n)=1)?

Open. Erdős stated this as the likely behavior. ([Rényi Institute][1])
In fact, even showing a **positive** lower bound (\liminf f(n)>0) is not presently known from standard unconditional results; Erdős/folklore links it to having sufficiently many primes in moderately short intervals. ([Erdős Problems][2])

### Is (\displaystyle \limsup f(n)=\infty)?

Also open. Erdős again called this the likely behavior. ([Rényi Institute][1])

A natural conditional route is via the **Hardy–Littlewood prime $k$-tuples conjecture**: if you can realize arbitrarily large admissible constellations of primes at prescribed offsets from $n$, then you can make (\sum 1/(n-p)) as large as you want (by choosing offsets whose reciprocal sum is large). This is a standard heuristic/conditional explanation for why one expects (\limsup f(n)=\infty). ([Erdős Problems][4])

### Is (f(n)=o(\log\log n))?

Open as well. Erdős explicitly asked whether perhaps (f(n)=o(\log\log n)). ([Rényi Institute][1])

What we *do* have is the unconditional upper bound (f(n)\ll \log\log n) shown above. ([Oxford University Research Archive][3])
But improving this to $o(\log\log n)$ [[nomath]](uniformly for all $n$)[[/nomath]] is not known.

There are also conditional improvements: the ErdősProblems page notes that certain strong “regularity” bounds for (\pi(x)) in short intervals would imply much smaller growth such as (f(n)\ll \log\log\log n). ([Erdős Problems][2])

## Bottom line answers to your three questions

* (\boxed{\liminf f(n)=1\ ?}) **Unknown (conjectured by Erdős).** ([Rényi Institute][1])
* (\boxed{\limsup f(n)=\infty\ ?}) **Unknown (conjectured by Erdős; would follow from very strong prime-pattern conjectures).** ([Rényi Institute][1])
* (\boxed{f(n)=o(\log\log n)\ ?}) **Unknown.** What is known unconditionally is (\boxed{f(n)\ll\log\log n}) for all $n$. ([Rényi Institute][1])

[1]: https://www.renyi.hu/~p_erdos/1977-27.pdf "https://www.renyi.hu/~p_erdos/1977-27.pdf"
[2]: https://www.erdosproblems.com/950 "https://www.erdosproblems.com/950"
[3]: https://ora.ox.ac.uk/objects/uuid%3Af34a2af4-c36d-4f9b-bad7-016a7a989203/files/m22685a8edf2e5142a452f7a8fd0f6ea3 "https://ora.ox.ac.uk/objects/uuid%3Af34a2af4-c36d-4f9b-bad7-016a7a989203/files/m22685a8edf2e5142a452f7a8fd0f6ea3"
[4]: https://www.erdosproblems.com/forum/discuss/950 "https://www.erdosproblems.com/forum/discuss/950"
