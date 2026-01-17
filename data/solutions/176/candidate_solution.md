It helps to rephrase what you are asking in “discrepancy” language.

For fixed $k$ and $N$, let (\mathcal{A}*{k,N}) be the family of all $k$-term arithmetic progressions in ({1,\dots,N}).
For a colouring (f:{1,\dots,N}\to{-1,1}) write
[
S(P)=\sum*{n\in P} f(n).
]
Then (N(k,\ell)) is the smallest $N$ such that **every** $f$ has **some** (P\in\mathcal{A}_{k,N}) with (|S(P)|\ge \ell).

## General upper bound (the only general one people really have)

If you can force a **monochromatic** $k$-term progression, you automatically force (|S(P)|=k), hence (|S(P)|\ge \ell) for every (\ell\le k). So
[
N(k,\ell)\ \le\ W(k,2)\qquad (1\le \ell\le k),
]
where (W(k,2)) is the 2-colour van der Waerden number. ([Erdős Problems][1])

The best published *general* upper bounds for $W(k,2)$ are still enormous (tower-type). One explicit bound quoted in the literature is
[
W(k,2)\ \le\ 2^{2^{2^{2^{2^{k+9}}}}}
]
[[nomath]](a tower of five 2’s with top exponent $k+9$)[[/nomath]], coming from Gowers’ quantitative bounds. ([NSF PARN][2])

So, unconditionally, you always have the (very weak) bound
[
N(k,\ell)\ \le\ 2^{2^{2^{2^{2^{,k+9}}}}}.
]
([NSF PARN][2])

## The one case we understand well: (\ell=1) (Spencer)

Spencer proved an exact formula for $N(k,1)$. If
[
k=2^t m \quad\text{with (m) odd},
]
then
[
N(k,1)=2^t(k-1)+1.
]
([Erdős Problems][1])

A few quick consequences:

* If $k$ is odd ((t=0)), then (N(k,1)=k).
* If (k=2^t) is a power of 2, then (N(k,1)=k(k-1)+1\sim k^2).

This is essentially the only “clean” sharp result known for these (N(k,\ell)). ([Erdős Problems][1])

## What this gives for $N(k,2)$

A key parity point: if $k$ is even then $S(P)$ is always even [[nomath]](sum of an even number of $\pm 1$’s)[[/nomath]], so “(|S(P)|\ge 1)” is the same as “(|S(P)|\ge 2)”.

So for **even** $k$,
[
N(k,2)=N(k,1)=2^t(k-1)+1\ \le\ k^2.
]
([Erdős Problems][1])

For **odd** $k$, (|S(P)|\ge 2) really means (|S(P)|\ge 3), and this is where things get hard: Erdős and Graham explicitly said that “no decent bound” is known even for $N(k,2)$. ([Erdős Problems][1])

So:

* $k$ even: $N(k,2)$ is (\Theta(k^2)) (in fact known exactly by Spencer’s formula). ([Erdős Problems][1])
* $k$ odd: no good upper bound is known beyond the van der Waerden bound (N(k,2)\le W(k,2)) (tower-type). ([Erdős Problems][1])

## Lower bounds for linear bias (\ell = ck) (why exponential is necessary)

Erdős proved that for every fixed (c>0),
[
N(k,ck) > (1+\alpha_c)^k,
]
with (\alpha_c\to 0) as (c\to 0) and (\alpha_c\to \sqrt2-1) as (c\to 1). ([Erdős Problems][1])

So **at least exponential growth in $k$** is unavoidable for any fixed positive fraction bias.

Also, a standard random-colouring + Lovász Local Lemma type argument gives stronger exponential lower bounds [[nomath]](closer to $2^k$ when $c$ is close to 1)[[/nomath]]; this is mentioned in the discussion for this problem. ([Erdős Problems][1])

## Your “(C^k)?” questions

### 1) Is it true that for every (c>0) there is (C>1) with (N(k,ck)\le C^k)?

As far as the current literature summaries go, this is **open**. The best general upper bound is still the van der Waerden bound (N(k,ck)\le W(k,2)), which is far larger than (C^k). ([Erdős Problems][1])

### 2) What about (N(k,2)\le C^k)?

* For **even** $k$, yes in a very strong sense: (N(k,2)\le k^2), so certainly (N(k,2)\le C^k) for any fixed (C>1) once $k$ is large [[nomath]](and you can pick an explicit $C$ that works for all even $k$, e.g. $k^2\le 4^k$)[[/nomath]]. ([Erdős Problems][1])
* For **odd** $k$, this is part of the same difficulty: there is “no decent bound” known even for (N(k,2)) itself. ([Erdős Problems][1])

So the “(N(k,2)\le C^k) for all $k$” question is **open because of odd $k$**.

### 3) What about (N(k,\sqrt{k})\le C^k)?

This is also **open** [[nomath]](it is not even settled for $\ell=2$ with odd $k$)[[/nomath]]. ([Erdős Problems][1])

## Bottom line

* **Best known general upper bound:** (N(k,\ell)\le W(k,2)), and the best published upper bounds for $W(k,2)$ are tower-type. ([NSF PARN][2])
* **Best known sharp result:** (N(k,1)=2^t(k-1)+1) for (k=2^t m) with $m$ odd (Spencer). ([Erdős Problems][1])
* **Exponential lower bounds:** for (\ell=ck) (Erdős), so exponential growth is necessary, but **exponential upper bounds (C^k)** are not known in general. ([Erdős Problems][1])

If you want, I can also spell out the “easy” random-colouring / local lemma lower bound in a clean inequality (it is short), because it explains why people think the right scale for $N(k,ck)$ should be exponential even when $c$ is close to 1.

[1]: https://www.erdosproblems.com/forum/thread/176 "

    Erdős Problem #176 - Discussion thread

"
[2]: https://par.nsf.gov/servlets/purl/10316754 "https://par.nsf.gov/servlets/purl/10316754"
