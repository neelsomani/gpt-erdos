Let

[
A_n:={m\in \mathbb Z:\ \exists d\in(n,2n)\text{ with }d\mid m}.
]

So you are asking for a length (y=y(\varepsilon,n)) such that, **for every** $x$,

[
|A_n\cap (x,x+y)|\ \le\ \varepsilon,y.
]

(That “for every $x$” is the natural reading, but I will say what changes if it is not.)

## 1) A hard obstruction: the global density

Let (\delta(n)) be the (natural) density of (A_n), i.e.

[
\delta(n)=\lim_{X\to\infty}\frac{|A_n\cap[1,X]|}{X}.
]

Kevin Ford’s work on integers with a divisor in an interval implies that

[
\delta(n)\asymp \frac{1}{(\log n)^{\alpha}(\log\log n)^{3/2}}
\quad\text{as }n\to\infty,
]

with
[
\alpha ;=; 1-\frac{1+\log\log 2}{\log 2};\approx;0.08607.
]
([ford126.web.illinois.edu][1])

Now, if your inequality (|A_n\cap(x,x+y)|\le \varepsilon y) is required for **all** $x$, then you must at least have

[
\varepsilon \ \ge\ \delta(n)
]

(up to absolute constants).
Reason: if you look at a very long stretch of integers and slide the window $(x,x+y)$ through it, the average number inside the window is (\delta(n)y); so the maximum over $x$ cannot be smaller than the average. So if (\varepsilon<\delta(n)), no choice of $y$ can make the bound true for every $x$. ([ford126.web.illinois.edu][1])

So: **if (\varepsilon) is smaller than about (1/((\log n)^{\alpha}(\log\log n)^{3/2})), there is no such $y$.**

## 2) A trivial (but huge) $y$ that always works when (\varepsilon) is big enough

For fixed (n), the set (A_n) is a union of arithmetic progressions (d\mathbb Z) for (d\in(n,2n)). Hence it is **periodic** with period

[
Q=\operatorname{lcm}(n+1,n+2,\dots,2n-1).
]

That means the count (|A_n\cap(x,x+Q)|) is the same for every (x). So if (\varepsilon\ge \delta(n)), then taking

[
y = Q
]

forces

[
|A_n\cap(x,x+y)| = \delta(n),y \ \le\ \varepsilon,y
\quad\text{for all }x.
]

This gives the very crude bound

[
y(\varepsilon,n)\ \le\ \operatorname{lcm}(n+1,\dots,2n-1),
]

whenever (\varepsilon\ge \delta(n)).

The catch: $Q$ is enormous [[nomath]](it grows roughly like $e^{(1+o(1))n}$)[[/nomath]]. So this is not the “right” size, just an existence bound.

## 3) Easy lower bounds on $y$

These depend on what range of $x$ you allow.

* If $x$ is allowed to be as small as (x=n), then the whole interval $(n,2n)$ consists of “bad” integers (each integer divides itself), so any (y\ge n) must satisfy
  [
  n \le |A_n\cap(n,2n)| \le \varepsilon y
  \quad\Rightarrow\quad
  y \ge \frac{n}{\varepsilon}.
  ]
  This is a simple, unavoidable obstruction coming from the very dense block right after (n).

* If you only care about very tiny (\varepsilon) [[nomath]](say $\varepsilon\ll 1/n$)[[/nomath]], then (\varepsilon y<1) for all (y<2n), so your condition would force **zero** such integers in every interval of length $y$; one can manufacture counterexamples using an $x$ tied to (\mathrm{lcm}(n+1,\dots,2n-1)). (This kind of observation is recorded in the Erdos problems notes.)

## 4) What is actually known about the *best* (y(\varepsilon,n))?

Beyond the necessary condition (\varepsilon\gtrsim \delta(n)) and the trivial periodicity upper bound (y\le \mathrm{lcm}(n+1,\dots,2n-1)), getting the correct growth of the **minimal** (y(\varepsilon,n)) is essentially the open part of this Erdős problem.

So the clean “state of play” (for the “for all $x$” interpretation) is:

* **No solution** if (\varepsilon \ll 1/((\log n)^{\alpha}(\log\log n)^{3/2})).
* **A (very large) solution exists** for (\varepsilon) above that scale, e.g.
  [
  y = \operatorname{lcm}(n+1,\dots,2n-1).
  ]
* The big open question is whether one can take (y) much smaller than this lcm [[nomath]](for example, polynomial in $n$ and $1/\varepsilon$)[[/nomath]], and what the true order should be. ([ford126.web.illinois.edu][1])

---

If you tell me which quantifier you mean for $x$ (“for all $x$” vs “there exists $x$”), I can state the sharp necessary condition and the trivial construction in exactly the right form. But with the usual reading (“for all $x$”), the key point is: the natural density is about (1/((\log n)^{0.086}(\log\log n)^{3/2})), and the only completely uniform general-purpose $y$ we can write down today is the period (\mathrm{lcm}(n+1,\dots,2n-1)).

[1]: https://ford126.web.illinois.edu/wwwpapers/hxy2y.pdf "hxy2y_2018.dvi"
