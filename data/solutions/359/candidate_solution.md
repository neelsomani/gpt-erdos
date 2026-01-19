Let

[
a_1<a_2<\cdots,\qquad a_1=n,
]

and for each (i\ge 1), let (a_{i+1}) be the **least integer (>a_i)** that is **not** representable as a sum of **consecutive** earlier terms (a_j+\cdots+a_k) with (1\le j\le k\le i).  [[nomath]](This “$>a_i$” is implicit in the “infinite increasing sequence” condition; otherwise the rule could pick something $\le a_i$.)[[/nomath]]

### The case $n=1$: MacMahon’s “segmented numbers” (OEIS A002048)

For $n=1$ this is the classical sequence beginning

[
1,2,4,5,8,10,14,15,16,21,\dots
]

and is known as **MacMahon’s segmented numbers** / “prime numbers of measurement”; it is OEIS **A002048**. ([Erdős Problems][1])

### What is conjectured about density / growth

Write (A(x)=|\\{k: a_k\le x\\}|). Andrews conjectured the asymptotic

[
a_k \sim \frac{k\log k}{\log\log k},
]

equivalently

[
A(x)\sim \frac{x\log\log x}{\log x}.
]

If this is true, the (natural) density (A(x)/x) tends to $0$. ([Erdős Problems][1])

Under Andrews’ conjecture, your two limits would indeed follow immediately:

* (\displaystyle \frac{a_k}{k}\sim \frac{\log k}{\log\log k}\to\infty).
* (\displaystyle \frac{a_k}{k^{1+c}} \sim \frac{\log k}{k^c\log\log k}\to 0) for every fixed (c>0).

But these remain **unproved**.

### What is actually proved

The strongest standard “published facts” that are commonly cited (and recorded on the Erdős Problems site / OEIS) are due to Porubský:

1. **Infinitely often upper bounds near the conjecture [[nomath]](up to $(\log k)^\varepsilon$)[[/nomath]]**
   For every (\varepsilon>0), there are infinitely many $k$ such that
   [
   a_k < (\log k)^\varepsilon,\frac{k\log k}{\log\log k}.
   ]
   ([Erdős Problems][1])

   In particular, for every (c>0),
   [
   \liminf_{k\to\infty}\frac{a_k}{k^{1+c}}=0,
   ]
   because along that infinite subsequence the ratio is (\ll (\log k)^{1+\varepsilon}/(k^c\log\log k)\to 0).
   What this **does not** give is (\frac{a_k}{k^{1+c}}\to 0) along *all* $k$.

2. **A lower bound on how many terms occur up to $x$, in terms of primes**
   Porubský also proved
   [
   \limsup_{x\to\infty}\frac{A(x)}{\pi(x)}\ge \frac{1}{\log 2},
   ]
   where (\pi(x)) is the prime counting function. ([Erdős Problems][1])

   Since (\pi(x)\sim x/\log x), this says (very roughly) that **along some sequence of $x$**, one has
   [
   A(x)\gtrsim \frac{1}{\log 2}\cdot \frac{x}{\log x},
   ]
   i.e. the sequence is at least as numerous as a fixed positive fraction of the primes along a subsequence of $x$. This is still consistent with density $0$.

3. **Even the basic divergence ({a_k/k\to\infty}) was already noted as open by Erdős**
   In Erdős’ 1977 problem list discussion of this construction, he explicitly remarks that (at the time) it was not even known whether (x_n/n\to\infty) [[nomath]](here $x_n$ is your $a_n$ in the $n=1$ case)[[/nomath]]. 
   The modern Erdős Problems entry still lists the problem as **open**. ([Erdős Problems][1])

### So, can one prove your two limits?

* **(\displaystyle a_k/k\to\infty)**: as far as the current literature summarized on the Erdős Problems site and the historical Erdős source indicates, this is **still open** for the greedy MacMahon/Andrews sequence. ([Erdős Problems][1])

* **(\displaystyle a_k/k^{1+c}\to 0) for every (c>0)**: also **open** in this strong “full limit” form. What *is* known [[nomath]](from Porubský’s “infinitely many $k$” upper bounds)[[/nomath]] is the strictly weaker statement (\liminf a_k/k^{1+c}=0) for every (c>0). ([Erdős Problems][1])

### A related point about “density” in the broader class of sequences

If you drop the **greedy** rule and only require a sequence with “no term is a sum of consecutive earlier terms,” then positive upper density is possible (Erdős Problem #839 discusses such constructions and bounds). ([Erdős Problems][2])
So “density $0$” is not automatic from the avoidance condition alone; it is specifically the greedy MacMahon/Andrews sequence that is mysterious.

---

If you want, I can also restate these results in the equivalent language of the counting function $A(x)$ (upper/lower density, upper/lower order), and spell out exactly which implications between $A(x)$ and (a_k) are logically equivalent and which are not.

[1]: https://www.erdosproblems.com/359 "
  
    Erdős Problem #359
  
"
[2]: https://www.erdosproblems.com/839 "
  
    Erdős Problem #839
  
"
