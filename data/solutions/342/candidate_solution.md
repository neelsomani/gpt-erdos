This is the **classical Ulam sequence** [[nomath]](the $(1,2)$-Ulam numbers)[[/nomath]], OEIS **A002858**.  It begins
[
1,2,3,4,6,8,11,13,16,18,26,28,\dots
]
and is defined exactly as you wrote: each new term is the smallest integer larger than the previous term that has **exactly one** representation as a sum of two **distinct** earlier terms. ([OEIS][1])

What makes it famous is that it *looks* “random-ish,” but also exhibits very rigid-looking patterns, and (as of the latest sources below) many basic questions remain open.

---

## What is known rigorously (as of 2025–2026 sources)

### 1) It is infinite, and there are exponential upper bounds on growth

A standard argument shows the sequence cannot terminate; one gets at least the crude recurrence
[
a_{n+1}\le a_n+a_{n-1},
]
hence (a_n) is bounded above by a Fibonacci-type exponential. 

A refinement due to Eggleton gives
[
a_{n+1}\le a_n+a_{n-2},
]
implying
[
a_n \le (1.466\ldots)^n
]
where (1.465571\ldots) is the real root of (x^3-x^2-1=0). 

A **recent improvement** (Clément–Steinerberger, 2025) shows that for all sufficiently large $n$,
[
a_n \le 1.454^n,
]
still exponential, but slightly better. 

### 2) Some “small gaps” must occur (in a multiplicative sense)

The same 2025 work proves that there is a constant (c>0) such that for all (n\ge 2),
[
\min_{1\le k\le n}\frac{a_{k+1}}{a_k}\le 1 + c\frac{\log n}{n}.
]
So, among the first $n$ gaps, at least one gap is *very small relative to the current scale* (though this does **not** force additive gaps like “2”). 

### 3) There are rigorous **upper bounds** on density, but no matching lower bounds

Let (\overline{d}) denote upper asymptotic density. Hinman–Kuca–Schlesinger–Sheydvasser (2019) prove, in particular, that the upper density of the $(1,2)$-Ulam numbers is at most
[
\overline{d}\le \frac{6}{17}\approx 0.353.
]
This is far from what numerics suggest, but it is a proven bound. ([MSP][2])

(And in their general discussion of Ulam sequences, it’s emphasized that many basic quantitative statements remain out of reach.) ([MSP][2])

---

## What is observed computationally / experimentally

### 4) Apparent linear growth and “density (\approx 0.074)”

Large computations (recorded in OEIS notes) indicate that the local density “hovers near $0.074$” up to at least (6.759\times 10^8), and empirically (a_n) lies close to a line (a_n\approx 13.5n) [[nomath]](so density $\approx 1/13.5$)[[/nomath]]. ([OEIS][1])

Steinerberger’s 2025 open-problems note similarly states that *empirically* the density is (\sim 7%) and that it “seems like (a_n\le 14n) for all sufficiently large (n),” while stressing that even basic facts are unknown rigorously beyond exponential upper bounds. 

### 5) A “hidden signal” / quasi-periodic structure

Steinerberger discovered a striking empirical phenomenon: there appears to be a real number
[
\alpha \approx 2.5714474995\ldots
]
such that
[
\cos(\alpha a_n)<0
]
for all but four exceptional Ulam numbers $\\{2,3,47,69\\}$ among the first (10^7) terms (and later sources report verification far beyond that). This indicates a strong non-uniform distribution of (\alpha a_n \pmod{2\pi}), despite the sequence’s “irregular” appearance. ([arXiv][3])

### 6) “Clumps” and large sporadic gaps

OEIS records remarks (e.g. by Knuth/McCranie) about large gaps such as a gap of $262$ between (a(4952)=64420) and (a(4953)=64682), and a gap $315$ later on. ([OEIS][1])

(For a small sanity check: computing the first 20,000 terms myself reproduces these examples; but of course that’s evidence, not proof of any asymptotic behavior.)

---

## Your three questions

### Do infinitely many pairs $a, a+2$ occur?

This is **open** (it is asked explicitly as part of Erdős problem 342 / Guy’s problem C4). ([Erdős Problems][4])

Empirically, gaps of size $2$ occur *very often* early on: for example, among the first 20,000 Ulam numbers, there are thousands of consecutive gaps equal to $2$ (in my computation, 7283 such gaps), and the beginning already contains ((11,13),(16,18),(26,28),(36,38),\dots). But there is no known proof that infinitely many occur.

### Does the sequence eventually have periodic differences?

For the $(1,2)$-Ulam sequence, this is also **open** and widely believed to be false; no eventual periodicity has been detected in extensive computations, and the behavior (clumps + occasional large gaps) looks incompatible with simple periodicity, but that’s not a proof. ([Erdős Problems][4])

It’s worth noting, though, that **other** $(u,v)$-Ulam sequences *are* known to be “regular” (differences eventually periodic) in certain families: for example, $(2,v)$ with $v$ odd (>3) and $(4,v)$ with (v\equiv 1\pmod 4), (v\ge 5), are proven regular (results of Schmerl–Spiegel and Cassaigne–Finch, building on Finch’s work). ([MSP][2])

So “eventual periodicity of gaps” is a meaningful phenomenon in this world—just not one that’s been resolved for $(1,2)$.

### Is the density $0$?

Also **open**, at least in the sense that recent research/expository sources still treat the density question as unknown and only report empirical behavior. ([Erdős Problems][4])

* OEIS notes attribute to Ulam the conjecture that the density is $0$, but also report computations suggesting density near (0.074). ([OEIS][1])
* The best rigorous results currently are **upper bounds** on density [[nomath]](e.g. $\le 6/17$)[[/nomath]], not a proof of density $0$ or of a positive limiting density. ([MSP][2])

---

## Bottom line

* Your recursion defines the **Ulam numbers** $U(1,2)$. ([OEIS][1])
* The three specific questions you listed [[nomath]](infinitely many $a,a+2$; eventual periodicity of differences; density $0$)[[/nomath]] are **classic open problems** for this sequence. ([Erdős Problems][4])
* What *is* known includes: exponential upper bounds on growth (recently improved), a theorem forcing some small multiplicative gaps, a rigorous (but weak) upper bound on density, and the striking “hidden signal” phenomenon discovered experimentally. 

If you want, I can also summarize the best-known heuristics for why a positive density around $0.074$ is plausible (the standard “random model” argument), but it’s not currently a theorem.

[1]: https://oeis.org/A002858 "https://oeis.org/A002858"
[2]: https://msp.org/involve/2019/12-3/involve-v12-n3-p11-s.pdf "Rigidity of Ulam sets and sequences"
[3]: https://arxiv.org/pdf/1507.00267?utm_source=chatgpt.com "arXiv:1507.00267v6 [math.CO] 6 Jul 2016"
[4]: https://www.erdosproblems.com/latex/342 "https://www.erdosproblems.com/latex/342"
