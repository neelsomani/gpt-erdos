Your “deficiency is undefined” condition is exactly the condition that
[
\gcd\left(\binom{n}{k},k!\right)=1,
]
i.e. **no prime (\le k)** divides (\binom{n}{k}). Binomial coefficients with this property are often called **good binomial coefficients**; equivalently, their least prime factor is (>k). ([MathWorld][1])

With that translation, the questions you ask are a well-known Erdős–Lacampagne–Selfridge problem (Erdős Problem #1093). As of late 2025, **both questions are still open unconditionally**. ([Erdős Problems][2])

## What is known unconditionally

### Origin and basic finiteness for fixed $k$

Erdős–Lacampagne–Selfridge explicitly define the deficiency $d(N,k)$ for a good (\binom Nk) [[nomath]](their notation uses $N$ where you use $n$)[[/nomath]], and they note:

* “Positive deficiencies occur only if $\gcd\left(\binom Nk,k!\right)=1$” (i.e. the “good” condition). 
* For **fixed $k$** and $N$ large enough, (\binom Nk) will **not** have positive deficiency [[nomath]](so for each fixed $k$, only finitely many $n$ can have deficiency $\ge 1$)[[/nomath]]. 
* They also remark they can heuristically “load” small prime powers to produce deficiency $1$ examples for given $k$, but had **no comparable construction for deficiency $2$**. 

So: **for each fixed $k$**, “infinitely many $n$” is ruled out; your questions are about varying $k$.

### A global upper bound when deficiency (\ge 1)

In a later paper they prove a strong restriction: if the deficiency exists and is (\ge 1), then
[
n \ll 2^k\sqrt{k}.
]
([Erdős Problems][2])
This doesn’t settle infinitude/finitude across all $k$, but it says positive deficiency can only occur when $n$ is at most on the order of (2^k\sqrt{k}).

### Computed examples and current “known list”

The same ErdosProblems page (updated Dec 27, 2025) reports:

* There are **many deficiency $1$** examples found computationally [[nomath]](it says **58 examples with $n\le 10^5$**)[[/nomath]], and lists a few small ones:
  [
  \binom73,\binom{13}4,\binom{14}4,\binom{23}5,\binom{62}6,\binom{94}{10},\binom{95}{10}.
  ]
  ([Erdős Problems][2])
* The **only known examples with deficiency (>1)** (as of that update) are a short list, e.g.

  * deficiency $2$: (\binom{44}8,\binom{74}{10},\binom{174}{12},\binom{239}{14},\binom{5179}{27},\binom{8413}{28},\binom{8414}{28},\binom{96622}{42})
  * deficiency $3$: (\binom{46}{10},\binom{47}{10},\binom{241}{16},\binom{2105}{25},\binom{1119}{27},\binom{6459}{33})
  * deficiency $4$: (\binom{47}{11})
  * deficiency $9$: (\binom{284}{28}).

  ([Erdős Problems][2])

This computational evidence is consistent with “deficiency (>1) is very rare”, but it is not a proof of finiteness.

## Conditional progress on the “deficiency (>1)” question

On the ErdosProblems discussion thread, Kevin Barreto sketches a **conditional** resolution of the second question:

* If (\delta(n,k)\ge 2), then there exist two distinct $k$-smooth integers (x=n-i) and (y=n-j) within distance (\Delta=|i-j|<k). Then (\Delta) is also $k$-smooth, and one gets a (primitive) equation
  [
  A+B=C
  ]
  with all prime factors (\le k), i.e. an “$S$-unit” type relation with $S$ bounded by $k$. ([Erdős Problems][3])
* Under two strong conjectures [[nomath]](a strengthening of Lagarias–Soundararajan’s $xyz_{\mathrm{fin}}$-conjecture plus an additional “height forcing” conjecture about how large $n$ must be when $\delta\ge 2$)[[/nomath]], he derives:

> **Assuming those conjectures, there are only finitely many $(n,k)$ with (\delta(n,k)\ge 2).** ([Erdős Problems][3])

So: the **second question has a conditional “yes, finitely many”** answer, but it remains open unconditionally. ([Erdős Problems][3])

## Direct answers to your two questions (current status)

* **Infinitely many with deficiency $1$?**
  **Open.** There is extensive computational evidence of many examples [[nomath]](dozens up to $n\le 10^5$)[[/nomath]], and the original authors already remarked that “for every $k$ there seem to be several” deficiency $1$ examples, but no proof of infinitude is known. 

* **Only finitely many with deficiency (>1)?**
  **Open unconditionally.** Only a small set of examples is currently known, and there is a conditional argument (under strong conjectures) implying finiteness of all cases with (\delta\ge 2). ([Erdős Problems][2])

If you’d like, I can also rephrase the condition (\gcd\left(\binom{n}{k},k!\right)=1) in terms of base‑$p$ digits (Lucas/Kummer), which is often a useful way to think about why the “good” condition is so restrictive and why positive deficiency forces strong alignment constraints.

[1]: https://mathworld.wolfram.com/GoodBinomialCoefficient.html "Good Binomial Coefficient -- from Wolfram MathWorld"
[2]: https://www.erdosproblems.com/1093 "https://www.erdosproblems.com/1093"
[3]: https://www.erdosproblems.com/forum/discuss/1093 "https://www.erdosproblems.com/forum/discuss/1093"
