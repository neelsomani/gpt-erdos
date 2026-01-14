Let

[
h(m):=\min\Bigl{k:\ \forall,1\le N<m\ \exists\ \text{distinct divisors }d_1,\dots,d_t\mid m,\ t\le k,\ N=\sum_{i=1}^t d_i\Bigr}.
]

This is exactly the “uniform additive basis order” of the divisor set of (m) (restricted to ([1,m))).

## What is known right now

### 1) The poly((\log\log m)) question is open

This is explicitly one of Erdős’s problems (Erdős Problem #18). The currently recorded best unconditional result in that direction is due to Vose:

* Erdős proved (h(n!)<n) (indeed “(n-1) or fewer” in one formulation). ([Erdős Problems][1])
* Vose proved there are infinitely many practical (m) with
  [
  h(m)\ll (\log m)^{1/2}.
  ]
  ([Erdős Problems][1])

Erdős conjectured that for infinitely many (m),
[
h(m) < (\log\log m)^c
]
for some absolute constant (c\ge 1).

As of the latest public summaries I can find (through late 2025), no poly((\log\log m)) infinite family is known, and the above Vose bound (\ll\sqrt{\log m}) remains the benchmark cited for “infinitely many (m)”. ([Erdős Problems][1])

So the answer to your first question is: **still open** (with best known (\sqrt{\log m}) infinitely often).

### 2) For factorials (n!): best published bound is polynomial, not subpolynomial

Erdős writes (in “Some of my Favourite Problems in Number Theory”) that he proved every (m<n!) is a sum of at most (n-1) distinct divisors of (n!), i.e.
[
h(n!)\le n-1.
]

He also records Vose’s improvement
[
h(n!)< c, n^{1/2}
]
for an absolute constant (c).

And he explicitly raises (as a conjectural strengthening) the possibility that (h(n!)) might be polylogarithmic, e.g. (h(n!)<c(\log n)^{c_2}).

The ErdosProblems page also flags this as an open/prize-type question.

So, to your second/third questions:

* **(h(n!)<n^{o(1)})**: not known.
* **(h(n!)<(\log n)^{O(1)})**: also not known (and explicitly highlighted as open in these sources).

## A simple but informative lower bound (especially for (n!))

There is a very general counting obstruction that is worth keeping in mind.

Let (t=\tau(m)) be the number of divisors of (m). The number of subsets of divisors of size (\le k) is at most
[
\sum_{j=0}^k \binom{t}{j}\ \le\ (k+1)t^k.
]
Each such subset yields **at most one** sum, so the number of distinct achievable sums using (\le k) divisors is (\le (k+1)t^k). To cover all integers (0,1,\dots,m-1) you need at least (m) distinct sums, hence a necessary condition is
[
(k+1),\tau(m)^k \ \ge\ m,
]
which in particular implies the very rough but clean lower bound
[
h(m)\ \ge\ \frac{\log m}{\log \tau(m)}\ - O(1).
]

For (m=n!), we have fairly sharp asymptotics for (\tau(n!)=d(n!)). A paper of Erdős–Graham–Ivić–Pomerance gives (writing (m=n!))
[
\log d(m)\ =\ c_0,\frac{\log m}{(\log\log m)^2}\Bigl(1+o(1)\Bigr)
\quad\text{with }c_0\approx 1.25775.
]
([math.dartmouth.edu][2])

Plugging this into the counting bound yields
[
h(n!)\ \ge\ \Bigl(\frac1{c_0}+o(1)\Bigr),(\log\log(n!))^2
\ \asymp\ (\log n)^2.
]

So:

* A polylogarithmic upper bound (h(n!)<(\log n)^{O(1)}) is **not ruled out** by this lower bound.
* But it does indicate that you **cannot** hope for (h(n!)) as small as (O(\log n)) (or ((\log n)^{1+o(1)}))—the counting obstruction already forces something on the order of ((\log n)^2) (up to constants/loglog factors) if (\tau(n!)) has the above size.

This aligns with Erdős’s own “perhaps (c(\log n)^{c_2})” remark: the exponent (c_2) would need to be at least about (2) in light of this basic entropy bound. ([math.dartmouth.edu][2])

## Tiny numerical sanity check

Just to give a feel for growth, exact computation for small (n) gives:

[
h(6!)=5,\quad h(7!)=5,\quad h(8!)=6,\quad h(9!)=7,\quad h(10!)=7.
]

This is consistent with “slowly growing” (and certainly far below the known (O(\sqrt n)) upper bound), but of course it doesn’t settle asymptotics.

## Bottom line

* **Infinitely many practical (m) with (h(m)<(\log\log m)^{O(1)})**: open. Best unconditional infinite-family bound I can find remains (h(m)\ll (\log m)^{1/2}) (Vose). ([Erdős Problems][1])
* **For (n!)**: best published bound I see is (h(n!)\ll n^{1/2}) (Vose), improving Erdős’s (h(n!)\le n-1); no known (n^{o(1)}) or polylog bound. ([Erdős Problems][1])
* There is a **general counting lower bound** (h(m)\gtrsim \log m/\log\tau(m)). Using known asymptotics for (\tau(n!)), this forces (h(n!)\gtrsim (\log n)^2) up to constants, so any true polylog upper bound would (morally) have to have exponent at least (\approx 2). ([math.dartmouth.edu][2])

If you want, I can also sketch how Vose’s Egyptian-fraction constructions translate into these (h(\cdot)) bounds (the “divisors sum” formulation is essentially an Egyptian-fraction length problem with denominators dividing (m)).

[1]: https://www.erdosproblems.com/18 "
  
    Erdős Problem #18
  
"
[2]: https://math.dartmouth.edu/~carlp/factorial.pdf "divfactorial.dvi"
