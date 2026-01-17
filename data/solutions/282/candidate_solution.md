What you describe is the usual Fibonacci–Sylvester greedy Egyptian‑fraction algorithm, but with the allowed denominators restricted to an infinite set $A$. When (A=\mathbb N) Fibonacci already observed (and it is easy to prove) that the process always terminates for rational (x\in(0,1)). ([Wikipedia][1])

## The case (A={\text{odd numbers}})

This is the **odd greedy algorithm** / **odd greedy expansion** problem.

### 1) If $x$ has even denominator, it cannot terminate

If the algorithm terminates using only odd denominators, you would have
[
x=\sum_{i=1}^k \frac1{n_i}\qquad(n_i\ \text{odd}).
]
Let (N=\prod_i n_i), which is odd. Writing everything over the common denominator $N$, the sum equals $m/N$ for some integer $m$, so after reduction the denominator must still be odd (a divisor of an odd number). Therefore no rational with **even** denominator can have a *finite* odd‑denominator Egyptian fraction expansion, so your process cannot terminate in that case. ([Wikipedia][2])

[[nomath]](For example, starting from $x=\tfrac12$ with $A=$ odds produces an **infinite** odd greedy expansion; this is a standard example in the literature. ([Wikipedia][2]))[[/nomath]]

### 2) If $x$ has odd denominator: existence is known, but greedy termination is open

It **is known** (Breusch and Stewart, 1954) that *every* rational (x=a/b) with $b$ odd has **some** finite representation as a sum of distinct odd unit fractions. ([Wikipedia][2])

However, the specific question you asked:

> Does the **odd greedy** procedure always terminate for every rational with odd denominator?

is, as of 2026, a **well‑known open problem**, attributed to Stein and discussed by Selfridge, Graham, and others. ([Erdős Problems][3])

Computationally it appears to terminate for all tested inputs, but expansions can be extremely long with astronomically large denominators (e.g. Wagon’s famous example $3/179$ has 19 terms and a last denominator with hundreds of thousands of digits). ([Wikipedia][2])
There are also infinite families where the **numerators of the successive remainders** march through long consecutive runs (a,a+1,a+2,\dots), showing that the number of steps can be made arbitrarily large (even if it always eventually halts). ([FQ Math][4])

So the honest answer to your first question is:

* **Even denominator:** definitely **does not** terminate (for structural reasons).
* **Odd denominator:** **unknown** whether it always terminates (open problem).

## More generally: for which $(x,A)$ does the restricted greedy algorithm terminate?

There isn’t a clean general characterization known; even deciding termination can be subtle because “a finite $A$-Egyptian representation exists” and “the $A$-greedy algorithm finds one” are different properties.

### A. Necessary conditions (easy obstructions)

If the algorithm terminates, then $x$ must lie in the set
[
\\{\sum_{n\in F}\frac1n : F\subset A\ \text{finite},\ \text{all }n\text{ distinct}\\}.
]
So any structural obstruction to *existence* of a finite $A$-Egyptian representation is also an obstruction to greedy termination.

Two common existence obstructions:

* **Denominator congruence obstructions.** For example, “odd denominators only” forces the reduced denominator of $x$ to be odd (as above). More generally, Graham characterized when a fraction $m/n$ can be written using denominators in an arithmetic progression (\equiv a\pmod d). ([Erdős Problems][3])
* **Sum of reciprocals bound.** If (\sum_{n\in A}\frac1n) converges to (S<\infty), then no finite sum of distinct ({1/n:n\in A}) can exceed $S$, so (x>S) is impossible regardless of any algorithm.

### B. Existence does **not** imply greedy termination (explicit example)

You can have a set $A$ for which $x$ has a finite representation using $A$, but the greedy process still runs forever.

Example:

* Let (A = {\text{all odd numbers}}\ \cup\ {4,20}).
* Then (x=\tfrac12) has a finite $A$-Egyptian representation:
  [
  \frac12=\frac14+\frac15+\frac1{20}.
  ]
* But the greedy choice at the first step is the **smallest** (n\in A) with (n\ge 1/x=2), which is $3$. After subtracting $1/3$ you get $1/6$, then the next greedy odd choice is $7$, then $43$, etc. Because *all* odds are in $A$, the greedy algorithm never uses the even denominators $4,20$, and it follows the usual odd-greedy expansion of $1/2$, which is infinite [[nomath]](since $1/2$ cannot be a finite sum of odd unit fractions)[[/nomath]]. ([Wikipedia][2])

So “$x$ is representable with denominators in $A$” is strictly weaker than “the $A$-greedy algorithm halts on $x$”.

### C. Classes of $A$ where greedy termination **is** provable for all rationals

Here are some useful sufficient conditions where one can prove the greedy process terminates for every rational (x\in(0,1)):

1. **Cofinite sets**
   If $A$ contains all sufficiently large integers [[nomath]](i.e. $\exists M$ such that $\\{M,M+1,M+2,\dots\\}\subseteq A$)[[/nomath]], then the restricted greedy algorithm terminates for every rational $x$.

Reason: the chosen denominators are strictly increasing, so eventually they exceed $M$. From that point on, since every integer (\ge M) is allowed, the algorithm’s choice becomes the *usual* greedy choice (n=\lceil 1/x\rceil), and the standard Fibonacci/Sylvester proof (numerator strictly decreases) forces termination. ([Wikipedia][1])

2. **Multiples of a fixed integer**
   If (A=m\mathbb N={m,2m,3m,\dots}), then the (A)-greedy algorithm terminates for every rational (x\in(0,1)).

Reason: define (y=mx). The ordinary greedy algorithm applied to $y$ chooses (k=\lceil 1/y\rceil=\lceil 1/(mx)\rceil); dividing the resulting expansion of $y$ by $m$ gives an expansion of $x$ with denominators (mk\in m\mathbb N). Moreover, step‑by‑step the choices match exactly, so the restricted process is just a rescaled ordinary greedy algorithm.

[[nomath]](As a special case $A=2\mathbb N$, the “even greedy” algorithm always terminates.)[[/nomath]]

### D. Natural families where existence is understood but greedy termination is open

Your odd‑denominator example is one instance of a broader phenomenon: for many “nice” $A$, we know **which rationals have some $A$-Egyptian representation**, but we do **not** know whether the greedy choice always works.

Two prominent examples mentioned in the same circle of questions:

* **Arithmetic progressions** (A={n:n\equiv a!!\pmod d}): representability is characterized by Graham, but whether the greedy algorithm always terminates in these cases is asked explicitly and is open in general. ([Erdős Problems][3])
  [[nomath]](The odd case is $a=1,d=2$.)[[/nomath]]
* **Square denominators** (A={n^2}): representability is characterized by Graham [[nomath]](in terms of the $\sum 1/n^2=\pi^2/6$ barrier)[[/nomath]], but the greedy‑termination analogue is again open and is even suspected to fail “almost always” by Erdős and Graham. ([Erdős Problems][3])

There are also many results proving **existence** of restricted‑denominator Egyptian fractions for wide classes of sequences $A$ (e.g. “doubling‑closed and productive” sequences), but these do not automatically imply that the greedy algorithm terminates. ([Cheriton School of Computer Science][5])

## Summary

* For (A=) odd numbers:

  * If $x$ has even denominator: **no**, it cannot terminate.
  * If $x$ has odd denominator: **open problem** (Stein’s odd greedy expansion question). ([Erdős Problems][3])
* For general $A$:

  * Termination implies $x$ has a finite $A$-Egyptian representation, but the converse can fail.
  * Termination for all rationals is provable for some $A$ [[nomath]](e.g. cofinite $A$, or $A=m\mathbb N$)[[/nomath]].
  * For many “structured” $A$ (odd numbers, arithmetic progressions, squares), existence may be known but greedy termination is often **open**. ([Erdős Problems][3])

If you tell me a specific family of sets $A$ you care about (e.g. “numbers in a residue class”, “numbers with prime factors in a fixed set”, “squares/cubes”, “practical numbers”, etc.), I can summarize what is known about **existence** and what is known/unknown about **greedy termination** for that family.

[1]: https://en.wikipedia.org/wiki/Greedy_algorithm_for_Egyptian_fractions?utm_source=chatgpt.com "Greedy algorithm for Egyptian fractions"
[2]: https://en.wikipedia.org/wiki/Odd_greedy_expansion?utm_source=chatgpt.com "Odd greedy expansion"
[3]: https://www.erdosproblems.com/282 "https://www.erdosproblems.com/282"
[4]: https://www.fq.math.ca/Papers1/48-3/Pihko.pdf "https://www.fq.math.ca/Papers1/48-3/Pihko.pdf"
[5]: https://cs.uwaterloo.ca/journals/JIS/VOL24/Eppstein/eppstein2.pdf "https://cs.uwaterloo.ca/journals/JIS/VOL24/Eppstein/eppstein2.pdf"
