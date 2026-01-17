What you wrote is **an open Erdős problem** about “complete” sets (meaning: all large integers can be written as a sum of **distinct** elements of the set). As far as the current literature summary on this problem goes, **no full proof is known** in the exact form you stated. ([Erdős Problems][1])

What *is* known is that **Cassels proved a version with stronger assumptions**: he assumed a stronger growth condition
[
\frac{|A\cap[1,2x]|-|A\cap[1,x]|}{\log\log x}\to\infty
]
and he assumed divergence of the **square** distances
[
\sum_{n\in A}|\theta n|^2=\infty\quad\text{for all }\theta\in(0,1),
]
and under those hypotheses he got the same conclusion (“all sufficiently large integers are subset sums”). ([Erdős Problems][1])

## What your assumptions force (easy checks)

Let (|x|) mean “distance to the nearest integer” (your $\\{x\\}$).

* Your second condition already forces (\gcd(A)=1).
  Because if every (n\in A) were divisible by some (d>1), then for (\theta=1/d) we would have (|\theta n|=|n/d|=0) for all (n\in A), so the sum could not diverge.

So the usual “all sums are even” type obstruction is ruled out.

## Why Cassels needs a square (and why your version is harder)

A standard way to study subset sums is the generating product
[
P(z)=\prod_{n\in A}(1+z^n)
]
[[nomath]](truncated to $n\le X$ when you want a finite polynomial)[[/nomath]]. The coefficient of (z^m) counts representations of $m$ as a sum of distinct elements.

On the unit circle (z=e^{2\pi i\theta}),
[
|1+e^{2\pi i\theta n}|=2|\cos(\pi \theta n)|.
]
Now (|\cos(\pi t)|) is **close to 1** precisely when $t$ is close to an integer, i.e. when (|t|) is small. And for small (|t|),
[
\log|\cos(\pi t)| \approx -c,|t|^2
]
(quadratic decay near 0). That quadratic behavior is exactly why the **square-sum** condition (\sum |\theta n|^2=\infty) is so natural in Cassels’ method: it forces products like (\prod |\cos(\pi\theta n)|) to shrink to 0 in the right places, which helps show the coefficients can’t keep vanishing.

In your problem, you only assume (\sum |\theta n|=\infty). That is strictly weaker: it is possible (in general) for a sequence of small numbers (u_k) to have (\sum u_k=\infty) but (\sum u_k^2<\infty) [[nomath]](think $u_k\sim 1/k$)[[/nomath]]. In that regime, the “(\log\cos)” quadratic decay is too weak to force the same product estimates. This is one big reason the problem is still open in the form you wrote. ([Erdős Problems][1])

## A very plausible route to a proof (what would need to be shown)

A clean way to prove your statement would be to show the **contrapositive**:

> If $A$ is *not* complete (infinitely many integers are missing from the distinct-sum set), then there exists some (\theta\in(0,1)) such that
> (\sum_{n\in A}|\theta n|<\infty.)

Because your assumption says (\sum_{n\in A}|\theta n|=\infty) for **every** (\theta), that would give a contradiction and force completeness.

Why this feels believable: “not complete” usually means the subset-sum set has some hidden structure/rigidity, and rigidity often shows up as a **large Fourier coefficient** at some frequency (\theta). Large Fourier coefficients translate into many (e^{2\pi i\theta n}) being close to 1, i.e. many (|\theta n|) being tiny, which is exactly what could make (\sum |\theta n|) converge.

But proving such an “inverse theorem” at this level of generality is hard, and (according to the current public status) it is not done yet.

## Bottom line

* The statement as written is currently listed as **open**. ([Erdős Problems][1])
* The closest classical result in the same direction is Cassels’ theorem under **stronger growth** and a **square** divergence condition. ([Erdős Problems][1])

If you want, I can also:

* explain Cassels’ strategy in more detail (still in simple steps), or
* discuss what kinds of sets $A$ satisfy your two conditions (examples and non-examples), and what the “typical” obstruction to completeness looks like.

[1]: https://www.erdosproblems.com/254 "
  
    Erdős Problem #254
  
"
