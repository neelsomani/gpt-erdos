Write (\omega(m)) for the number of **distinct** prime divisors of $m$.

### 1) What your main term is really counting

For a prime (p>k), we have (v_p(k!)=0), and the interval $(n-k,n]$ has length (k<p), so there is **at most one** multiple of $p$ among
[
n-k+1,\dots,n.
]
Hence
[
v_p\binom{n}{k}=v_p\bigl(n(n-1)\cdots(n-k+1)\bigr)\in{0,1}
]
and in fact
$
p\mid \binom{n}{k}\quad\Longleftrightarrow\quad \exists,j\in{0,1,\dots,k-1}:\ p\mid(n-j)
\quad\Longleftrightarrow\quad n\bmod p<k.
$
This is an immediate special case of Kummer’s theorem [[nomath]](the $p$-adic valuation of $\binom{n}{k}$ is the number of carries when adding $k$ and $n-k$ in base $p$)[[/nomath]]; when (p>k) there is only the “units digit” to worry about, giving exactly the condition (n\bmod p<k). ([DMS UMontreal][1])

So the “large prime” contribution is exactly
$
S(n,k)\ :=\ |\\{,p:\ k<p\le n,\ n\bmod p<k,\\}|
\ =\ \sum_{k<p\le n}\mathbf 1_{n\bmod p<k}.
$

Moreover, in your range (n^\varepsilon<k\le n^{1-\varepsilon}), primes (\le k) are negligible for the *leading* term you propose: trivially
[
|\\{p\le k:\ p\mid\tbinom{n}{k}\\}|\le \pi(k)=o(k),
]
while your main term is (\asymp k) [[nomath]](indeed $\sum_{k<p<n}1/p$ is bounded away from $0$ and $\infty$ when $k\in[n^\varepsilon,n^{1-\varepsilon}]$)[[/nomath]]. So your conjecture is essentially about $S(n,k)$.

### 2) Why the conjectured main term is the “right” heuristic

If you treat (n \bmod p) as “random” in ({0,1,\dots,p-1}), then for each (p>k),
$
\mathbb E,\mathbf 1_{n\bmod p<k}=k/p,
$
so
$
\mathbb E,S(n,k)=k\sum_{k<p\le n}\frac1p.
$
By Mertens’ theorem,
$
\sum_{p\le x}\frac1p=\log\log x+M+O(1/\log x),
$
so
$
\sum_{k<p\le n}\frac1p
=\log\log n-\log\log k+o(1). ([Wikipedia][2])
$
For (k=n^\alpha) [[nomath]](with $\alpha\in[\varepsilon,1-\varepsilon]$)[[/nomath]], this becomes
$
k\sum_{k<p\le n}\frac1p
=(1+o(1))k\log!\\(\frac1\alpha\\),
$
a constant multiple of $k$, matching the intuition that each of the $k$ consecutive integers (n-k+1,\dots,n) typically contributes $O(1)$ “new” primes (>k).

### 3) Status: this is (as of early 2026) an open Erdős problem

The statement you wrote down is literally Erdős Problem #685, currently listed as **open** [[nomath]](with the same ranges $n^\varepsilon<k\le n^{1-\varepsilon}$ and the same asymptotic)[[/nomath]]. ([Erdős Problems][3])

A comment there (Tao, Sep 10 2025) explains a key reduction/difficulty: up to $O(k)$ lower-order terms, you are counting primes $p\in(k,n]$ that divide at least one integer in a short interval of length $k$, and this is “somewhat comparable” in difficulty to prime number theorem–type control in short intervals $[x,x+x^\varepsilon]$. $[Erdős Problems][4]$

So: **no**, at present there is no known theorem guaranteeing your asymptotic uniformly for *all* $n$ large and *all* $k$ in that range.

### 4) What *is* known unconditionally (deterministic bounds)

There are strong **linear** lower bounds for (\omega\binom{n}{k}) in great generality, but they do not identify the constant (\sum_{k<p<n}1/p).

For instance, Shorey–Tijdeman prove (Theorem 1) that for (n>2k),
[
\omega\binom{n}{k}\ \ge\ k-\frac{\log(k!)}{\log(n-k)}.
]
In particular, if (k=n^\alpha) then (\log(k!)/\log(n-k)\sim \alpha k), giving a bound (\omega\binom{n}{k}\gtrsim (1-\alpha)k). 

They also show (\omega\binom{n}{k}\ge k) once (n\ge k\pi(k)+k) [[nomath]](and remark this threshold is about $e^k$ by the PNT)[[/nomath]]. 

On the other hand, in your range (k\ge n^\varepsilon), each individual integer $m\in(n-k,n]$ can have at most $\lfloor 1/\varepsilon\rfloor$ prime factors $>k$ $since ((n^\varepsilon)^{t}\le m\le n\Rightarrow t\le 1/\varepsilon)$. This gives a crude but uniform upper bound $\omega(\binom{n}{k})=O_\varepsilon(k)$, consistent with the conjectured $\asymp k$.

### 5) What can be proved “for most $n$” (and why that’s much easier)

If you **average over $n$** instead of fixing $n$, the heuristic essentially becomes a theorem quickly:

* For each fixed $k$, the indicators (\mathbf 1_{n\bmod p<k}) are independent across distinct primes (p>k) when $n$ is uniformly random modulo the product (this is just CRT).
* Thus (\mathbb E S(n,k)=\mu:=k\sum_{k<p\le n}1/p) and (\mathrm{Var}(S(n,k))\asymp \mu).
* Chebyshev then gives (S(n,k)=\mu+o(\mu)) for “almost all” $n$ as soon as (\mu\to\infty), i.e. as soon as (k\to\infty).

This kind of argument strongly supports that your asymptotic is **true for typical $n$** whenever $k$ grows [[nomath]](including $k\ge (\log n)^c$)[[/nomath]], but it does **not** address the “for all $n$” uniformity.

### 6) About the ((\log n)^c) regime

The same problem (#685) explicitly asks whether one can go down to (k\ge(\log n)^c). ([Erdős Problems][3])
As far as I can tell from the available literature/discussions, this is also **open** in the strong “for all $n$” sense, and (per Tao’s remark) sits in the territory of deep “short interval” phenomena. ([Erdős Problems][4])

---

If you tell me whether you care about:

* **$A$** “for all $n$” vs “for almost all $n$”,
* and whether you want the **full** (\omega\bigl(\binom{n}{k}\bigr)) or just the contribution of primes (>k),

…I can outline a clean probabilistic/second-moment proof of the “almost all $n$” statement (with explicit error terms), and explain precisely where the “for all $n$” version seems to run into current limits.

[1]: https://dms.umontreal.ca/~revealed/App3A.pdf?utm_source=chatgpt.com "Factoring binomial coefficients, and Pascal's Triangle mod p"
[2]: https://en.wikipedia.org/wiki/Mertens%27_theorems?utm_source=chatgpt.com "Mertens' theorems"
[3]: https://www.erdosproblems.com/685 "
  
    Erdős Problem #685
  
"
[4]: https://www.erdosproblems.com/forum/discuss/685 "

    Erdős Problem #685 - Discussion thread

"
