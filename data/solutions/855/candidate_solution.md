This inequality is *exactly* what’s usually called the **second Hardy–Littlewood conjecture**:

[
\pi(x+y)\le \pi(x)+\pi(y)\qquad (x,y\ge 2).
]

Equivalently,
[
\pi(x+y)-\pi(x)\le \pi(y),
]
i.e. **no interval $(x,x+y]$ of length $y$ ever contains more primes than the initial interval $(0,y]$**. 

### Is it known to be true “for large $x$ and $y$”?

No — **it is not proved**, even for large $x,y$, and **no explicit counterexample is known either** (as of the 2025 survey/paper below). 

Moreover, there is strong evidence it is **actually false**:

* Hensley & Richards showed that the second Hardy–Littlewood conjecture is **incompatible** with the (first) **prime $k$-tuple conjecture** (the usual Hardy–Littlewood prime constellations conjecture). In particular, **if** the prime $k$-tuple conjecture is true, then for sufficiently large $x$ there should be **infinitely many (y>2)** for which the inequality fails. 
  Since the $k$-tuple conjecture is widely believed, experts tend to expect the subadditivity inequality to fail for some large pairs $(x,y)$, even though we don’t currently have a concrete counterexample. 

A concrete “candidate mechanism” for failure is known: Wikipedia (summarizing standard computations in the literature) notes that there exists an **admissible** pattern of **447** prime positions inside an interval of length $y=3159$, while (\pi(3159)=446). If the prime $k$-tuple conjecture holds, such a 447-prime cluster should eventually occur at some huge $x$, forcing
(\pi(x+3159)-\pi(x)\ge 447 > \pi(3159)), contradicting the inequality. ([Wikipedia][1])

### What *is* known (partial results)

Even though the full inequality is open, it is proved in a number of important ranges/special cases:

* **Doubling case:** (\pi(2x)\le 2\pi(x)) is known [[nomath]](Landau for large $x$, and Rosser–Schoenfeld for all $x>2$)[[/nomath]]. 
  This corresponds to the special case $y=x$.

* **A universal but weaker bound:** Montgomery–Vaughan proved
  [
  \pi(x+y)\le \pi(x)+2\pi(y)\qquad (x>1,\ y>2),
  ]
  which is the same shape but with a factor $2$ in front of (\pi(y)). 

* **If $y$ is sufficiently large relative to $x$:** results of Udrescu and Dusart (and later improvements) show that the *original* inequality holds when $y$ is not too small compared to $x$. For example, Dusart gives a range of the form
  [
  \frac{5x}{7\log x\log\log x}\le y\le x
  ]
  [[nomath]](for $x$ large enough)[[/nomath]], in which (\pi(x+y)\le \pi(x)+\pi(y)) is guaranteed. 

* **Recent improvements and conditional (RH) ranges:** a 2025 paper by Chahal–Elma–Fellini–Vatwani–Vo links the inequality to the error term in the prime number theorem and improves known “$y$-ranges”; assuming the Riemann Hypothesis, they prove the inequality for $y$ as small as on the order of (\sqrt{x}\log^2 x) [[nomath]](up to constants and an $\varepsilon$)[[/nomath]]. 

### Bottom line

* If you mean: “Is (\pi) eventually subadditive for all sufficiently large $x,y$?” — **open**, and **widely expected to be false** [[nomath]](conditionally on the prime $k$-tuple conjecture it should fail for arbitrarily large $x,y$)[[/nomath]]. 
* If you add a relationship like “$y$ is a fixed positive fraction of $x$” [[nomath]](or even somewhat smaller, e.g. $y \gtrsim x/(\log x\log\log x)$)[[/nomath]], then **it is known to be true for all sufficiently large $x$**. 

If you tell me what regime you care about [[nomath]](e.g. $y\sim x$, or $y=x^\alpha$, or $y=\log^A x$)[[/nomath]], I can point to the sharpest known results in that range.

[1]: https://en.wikipedia.org/wiki/Second_Hardy%E2%80%93Littlewood_conjecture "Second Hardy–Littlewood conjecture - Wikipedia"
