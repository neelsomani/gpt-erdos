Let

* (d_n:=p_{n+1}-p_n) [[nomath]](the $n$th prime gap)[[/nomath]], and
* $a(n):=\max{k\ge 1:\ d_n,d_{n+1},\dots,d_{n+k-1}\ \text{are all distinct}}$.

Then your $h(x)$ is exactly
$
h(x)=\max_{1\le n<x} a(n).
$
This is the quantity encoded by OEIS **A053597** [[nomath]](the function $a(n)$)[[/nomath]] and its record-setters **A078515** (the indices where a new maximum occurs). ([OEIS][1])

## What is known rigorously

Not much quantitatively seems to be known. The Erdős-problems entry for this question records only that **Brun’s sieve implies (h(x)\to\infty)** as (x\to\infty). ([Erdős Problems][2])

I don’t see (from the sources available) any proven bound of the shape (h(x)>(\log x)^c) for some fixed (c>0), nor a proven $o(\log x)$ upper bound. The problem is listed as open. ([Erdős Problems][2])

## What the standard random/Poisson prime heuristic predicts

Heuristically, near a large prime $p$, the primes behave like a Poisson process with intensity (\approx 1/\log p) (Cramér-type model), so a *single* gap behaves roughly like an exponential/geometric random variable with mean
[
\mu \sim \log p \sim \log p_n \sim \log n.
]

Because (d_n) is (essentially) supported on even integers, a useful toy model is:
[
\mathbb P(d=2k)\approx \frac{2}{\mu}e^{-2k/\mu},\qquad k=1,2,\dots
]
(possibly with a mild multiplicative “singular series” weight; see below).

### Step 1: collision probability and “birthday paradox” scale

For a discrete distribution, the key parameter for repeats is the “collision probability”
[
\kappa := \sum_g \mathbb P(d=g)^2.
]
In the toy even-exponential model one finds (\kappa\asymp 1/\mu). [[nomath]](Intuition: the distribution puts mass $\asymp 1/\mu$ on each of $\asymp \mu$ plausible gap sizes.)[[/nomath]]

Then for a block of $m$ (approximately independent) gaps, the expected number of equal pairs is
[
\binom{m}{2}\kappa \ \asymp\ \frac{m^2}{\mu}.
]
So for $m$ not too large, a standard heuristic gives
[
\mathbb P(\text{a given length-}m\text{ block has all gaps distinct})
\approx \exp!\Big(-c,\frac{m^2}{\mu}\Big)
]
for some constant (c>0) [[nomath]](often $c\approx 1/2$ in the simplest birthday-paradox approximation)[[/nomath]].

### Step 2: maximize over (\sim x) starting points

Among the first $x$ gaps there are (\asymp x) starting points for a length-$m$ block. Treating these events as roughly independent (or just using a first-moment heuristic), the expected number of distinct-gap blocks of length $m$ is about
[
x \exp\Big(-c,\frac{m^2}{\mu}\Big).
]
Set this (\approx 1) to get the threshold for the *longest* such block:
[
m^2 \approx \frac{\mu}{c}\log x
\quad\Rightarrow\quad
m \approx \sqrt{\frac{\mu}{c}\log x}.
]

Now, in the range (n\approx x) we have (\mu\sim \log p_x \sim \log x) [[nomath]](up to $\log\log x$ terms)[[/nomath]]. Plugging (\mu\sim\log x) gives
[
h(x) \asymp \log x
\qquad\text{(heuristically).}
]

If you push the constants in the simplest even-exponential model you get something like
[
h(x)\approx \sqrt{2},\log x
]
(up to lower-order terms and model-dependent constants). If you incorporate Hardy–Littlewood-type weighting that makes certain gaps (multiples of small primorials) more frequent, the collision probability (\kappa) is a bit larger, which reduces the constant in front of (\log x); the same *(\asymp \log x)* scaling persists.

### Heuristic answers to your two subquestions

Under these standard models:

* **Yes**, one expects (h(x)>(\log x)^c) for some (c>0) [[nomath]](in fact $h(x)$ should be of order $\log x$)[[/nomath]].
* **No**, one does **not** expect (h(x)=o(\log x)); rather (h(x)/\log x) should stay bounded away from $0$ (and plausibly tend to a positive constant).

## What computation/record data suggests

OEIS **A053597** defines exactly $a(n)$ [[nomath]](“how many distinct gaps starting at $n$ before the first duplicate”)[[/nomath]], and **A078515** lists the $n$ where $a(n)$ sets a new record. ([OEIS][1])

The currently listed record indices in A078515 grow very rapidly (roughly exponentially in the record value), which is what you’d expect if the inverse function $h(x)$ grows like (\log x). ([OEIS][3])

There’s also an Erdős-problems forum comment noting that the available record data “looks exponential,” consistent with (h(x)=\Theta(\log x)) (with the usual caveat that small data can mislead). ([Erdős Problems][4])

Relatedly, OEIS **A079007** gives the smallest prime (p_k) that starts a run of $n$ consecutive distinct prime gaps; its growth is also consistent with needing exponentially larger search ranges to force longer distinct runs. ([OEIS][5])

## Bottom line

* **Unconditionally:** the only solid statement I can point to from the available references is (h(x)\to\infty) (via Brun’s sieve), with no sharp growth rate known. ([Erdős Problems][2])
* **Heuristically (Cramér/Poisson + discrete “birthday paradox”):**
  [
  h(x)\asymp \log x,
  ]
  so (h(x)>(\log x)^c) should be true (indeed much stronger), while (h(x)=o(\log x)) is not expected.

If you want, I can also translate this into the variant where $x$ is a *prime-size cutoff* [[nomath]](i.e. $p_n\le x$)[[/nomath]] rather than an *index cutoff*; the heuristic conclusion stays the same up to (\log\log) terms because (p_n\sim n\log n).

[1]: https://oeis.org/A053597 "https://oeis.org/A053597"
[2]: https://www.erdosproblems.com/852 "https://www.erdosproblems.com/852"
[3]: https://oeis.org/A078515 "https://oeis.org/A078515"
[4]: https://www.erdosproblems.com/forum/discuss/852 "https://www.erdosproblems.com/forum/discuss/852"
[5]: https://oeis.org/A079007 "https://oeis.org/A079007"
