This is **open**.

Because trivially (C(x)\le x), the assertion
[
C(x)=x^{1-o(1)}
]
is really a **lower-bound** question: it asks whether for every fixed (\varepsilon>0) one eventually has (C(x)\ge x^{1-\varepsilon}).

## What is conjectured

* This is essentially an old conjectural picture going back to Erdős, and it is listed as an open Erdős problem. ([Erdős Problems][1])
* A much more precise conjecture (often called **Pomerance’s Carmichael density conjecture**) predicts
  [
  C(x)=x\exp\left(-(1+o(1))\frac{\log x,\log\log\log x}{\log\log x}\right),
  ]
  which **does imply** (C(x)=x^{1-o(1)}) [[nomath]](since that exponential factor is $x^{-o(1)}$)[[/nomath]]. 

## What is proved unconditionally (best known lower bounds)

The best unconditional results are still far from exponent $1$:

* Alford–Granville–Pomerance (1994): (C(x)\ge x^{2/7}) for $x$ sufficiently large. 
* Harman (2008): (C(x)\ge x^{0.3336704}). 
* Lichtman (2022): improved to (C(x)\ge x^{0.3389}) [[nomath]](for $x$ sufficiently large)[[/nomath]]. ([arXiv][2])
* There is also a **recent arXiv preprint** claiming a slightly stronger exponent (>0.34). Since it is very recent and not yet broadly vetted in the literature, it’s safest to treat this as “claimed best” rather than “established best.” ([arXiv][3])

So, unconditionally we are nowhere near proving (x^{1-o(1)}).

## Upper bounds (consistent with the conjecture)

Pomerance (1981) proved an upper bound of the shape
[
C(x)\ \le\ x\exp\left(-\frac{\log x,\log\log\log x}{2\log\log x}\right),
]
which is already (x^{1-o(1)}) from above (but of course does not help with the desired lower bound). 

## Conditional evidence: (x^{1-o(1)}) follows from strong prime-distribution hypotheses

Wright (2020) proves that **assuming** a strong conjecture on the least prime in an arithmetic progression (a “Heath–Brown conjecture” type hypothesis), one gets
[
C(x)\ \ge\ x^{1-(2+o(1))\frac{\log\log\log\log x}{\log\log\log x}},
]
which in particular **implies** (C(x)=x^{1-o(1)}) (conditionally). 

---

**Bottom line:** unconditionally, **we do not know** whether (C(x)=x^{1-o(1)}). It is widely expected (and implied by Pomerance’s more precise conjecture), and it can be proved under strong conjectures about primes in arithmetic progressions, but current unconditional lower bounds are only around (x^{0.34}). 

[1]: https://www.erdosproblems.com/forum/thread/1057 "

    Erdős Problem #1057 - Discussion thread

"
[2]: https://arxiv.org/pdf/2211.09641?utm_source=chatgpt.com "arXiv:2211.09641v1 [math.NT] 14 Nov 2022"
[3]: https://arxiv.org/pdf/2308.04458 "The number of primes in short intervals and numerical calculations for Harman's sieve"
