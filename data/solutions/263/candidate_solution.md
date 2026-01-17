What you are calling a “good” sequence ( (a_n) ) is exactly what Kovač–Tao (following Erdős–Graham) call a **Type 2 irrationality sequence**: an increasing integer sequence such that for *every* integer sequence (b_n) with (b_n/a_n\to 1) [[nomath]](equivalently $b_n\sim a_n$)[[/nomath]], the reciprocal sum (\sum_{n\ge 1} 1/b_n) is **not rational**. ([arXiv][1])
[[nomath]](One usually assumes $a_n>0$ and $b_n>0$ eventually; since $b_n/a_n\to 1$, $b_n$ has the same sign as $a_n$ for all large $n$ anyway.)[[/nomath]]

## Is (a_n=2^{2^n}) such a sequence?

As of the current literature, this is **open**.

* Erdős and Graham explicitly stated that with the Type 2 definition “we do not even know if (a_n=2^{2^n})” has the property. ([arXiv][1])
* This is recorded as **Erdős Problem #263** and is currently listed as open. ([Erdős Problems][2])
* Koizumi (2025) likewise calls it an **unsolved** Erdős–Graham question. 

What *is* known around this borderline case:

1. **Don’t confuse with the “Type 1 / Property P” notion.**
   Erdős proved that (a_n=2^{2^n}) *does* satisfy the stronger Type 1 (“Property P”) condition: (\sum 1/(t_n a_n)) is irrational for every positive integer sequence (t_n). ([arXiv][1])
   But Type 2 is different: you are only allowed perturbations (b_n\sim a_n), not arbitrary multiples, and the problem turns out harder.

2. **It is exactly the threshold case for the best current general theorems.**
   Kovač–Tao prove that if (\sum 1/a_n) converges and
   [
   \lim_{n\to\infty}\frac{a_{n+1}}{a_n^2}=0,
   ]
   then ((a_n)) is **not** Type 2. ([arXiv][1])
   This “just barely fails” to address (a_n=2^{2^n}) because (2^{2^{n+1}}=(2^{2^n})^2), i.e. $\frac{a_{n+1}}{a_n^2}=1$, not $0$. ([arXiv][1])

3. **“Almost all” nearby doubly-exponential sequences are Type 2.**
   Koizumi proves that for the family (a_n=\lfloor \alpha^{2^n}\rfloor), the set of (\alpha>1) for which this is Type 2 has **countable complement** [[nomath]](so “almost every” $\alpha$ works)[[/nomath]]. 
   This strongly suggests $2$ should work “generically”, but it still leaves open the specific case (\alpha=2).

4. **Koizumi reduces it to another open Erdős–Graham question.**
   Koizumi explains that an affirmative answer to a certain Erdős–Graham Question 5 (equivalently his Conjecture 6 about “pseudo-greedy” expansions) would imply that (2^{2^n}) *is* Type 2. ([arXiv][3])
   That conjecture is not yet proved.

So the best honest answer is: **we don’t currently know** whether (2^{2^n}) has your property.

## Must such a sequence satisfy (a_n^{1/n}\to\infty)?

This is also **open in general**, and is explicitly posed as part of the same Erdős Problem #263. ([Erdős Problems][2])
Erdős and Graham themselves wrote (about Type 2) that it “probably” must satisfy (a_n^{1/n}\to\infty), but they did not prove it. ([arXiv][1])

What *is* known in the direction of growth constraints:

* **Exponential-type growth is ruled out (under mild regularity).**
  Kovač–Tao’s theorem gives a broad obstruction: if (\sum 1/a_n) converges and (a_{n+1}/a_n^2\to 0), then not Type 2. ([arXiv][1])
  This excludes many “sub-doubly-exponential” regimes [[nomath]](for instance, it excludes $a_n$ behaving like $2^{(2-\varepsilon)^n}$)[[/nomath]]. ([arXiv][1])
  In particular, it certainly rules out “uniformly exponential growth” (a_n\approx \theta^n) [[nomath]](since then $a_{n+1}/a_n^2\sim 1/a_n\to 0$)[[/nomath]]. ([arXiv][1])

* **Very fast growth gives positive examples (so Type 2 sequences exist).**
  A standard “folklore” sufficient condition is that (\lim a_n^{1/2^n}=\infty) [[nomath]](equivalently $\log a_n / 2^n\to\infty$)[[/nomath]]; then (\sum 1/a_n) is irrational, and this can be leveraged to show Type 2 in that very fast-growth regime. ([Erdős Problems][2])
  Kovač–Tao also note that if (\liminf \frac{a_{n+1}}{a_n^{2+\varepsilon}}>0) for some (\varepsilon>0), then the sequence is Type 2. ([arXiv][1])

These results strongly suggest that Type 2 sequences must grow *at least* “nearly doubly exponentially” in some sense, but they **do not yet settle** whether (a_n^{1/n}\to\infty) is forced in full generality [[nomath]](because you can have very irregular growth where $a_{n+1}/a_n^2$ does *not* tend to $0$ but $a_n^{1/n}$ still fails to go to $\infty$)[[/nomath]].

## Bottom line

* (a_n=2^{2^n}): **open** (this is the main Erdős–Graham question). ([Erdős Problems][2])
* Necessarily (a_n^{1/n}\to\infty): also **open** for Type 2; conjectured “yes” by Erdős–Graham, with partial negative/positive growth results known. ([arXiv][1])

If you want, I can also summarize the *best current “threshold picture”* around (a_{n+1}\approx a_n^2) [[nomath]](why $2^{2^n}$ is the boundary case for the known methods, and what a proof would likely need)[[/nomath]].

[1]: https://arxiv.org/pdf/2406.17593 "https://arxiv.org/pdf/2406.17593"
[2]: https://www.erdosproblems.com/263 "https://www.erdosproblems.com/263"
[3]: https://arxiv.org/pdf/2504.05933 "https://arxiv.org/pdf/2504.05933"
