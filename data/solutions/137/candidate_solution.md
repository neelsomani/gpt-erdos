A **powerful** (also called **squarefull**) integer is one where every prime divisor shows up with exponent at least $2$: if (p\mid N) then (p^2\mid N). ([Wikipedia][1])

For **(k=2)** the answer is **yes**: the product of two consecutive integers can be powerful. For example,
[
8\cdot 9=72=2^3\cdot 3^2
]
is powerful. In fact there are **infinitely many** such $n$ (e.g. coming from infinitely many pairs of consecutive powerful numbers). ([Wikipedia][1])

For **(k\ge 3)**: this is **open**.

* The exact question you ask is a known Erdős–Selfridge problem (Erdős Problem #137). It is listed as **OPEN**: nobody currently knows whether a product of (k\ge 3) consecutive integers can ever be powerful, or whether there must always be a prime (p\mid N) with (p^2\nmid N). ([Erdős Problems][2])
* Erdős and Selfridge did prove a related (strong, but different) theorem: the product of two or more consecutive integers is **never a perfect power** (so it is never a square, never a cube, etc.). But “powerful” is weaker than “perfect power”, so this does not settle your question. ([Project Euclid][3])

### What *is* known in the direction of your question (partial results)

Let
[
\Delta(n,k)=n(n+1)\cdots(n+k-1).
]
There are results showing that (\Delta(n,k)) must have “large primes” appearing to **odd** exponent in many cases. For example, for (n>k^2), Erdős–Selfridge proved there is a prime (p\ge k) dividing (\Delta(n,k)) to an odd power [[nomath]](with one small exceptional pair $(n,k)=(48,3)$)[[/nomath]], and later work sharpened this to (p>k). 

There are also stronger bounds for larger $k$ and $n$ [[nomath]](e.g. for $k\ge 10$ and $n>k^2$, there are many distinct primes $>k$ dividing $\Delta(n,k)$ to odd powers, apart from an explicit finite list of exceptions)[[/nomath]]. 

But a warning: **“odd power” does not mean exponent $1$**. It could be (3,5,\dots), and that still allows (p^2\mid \Delta(n,k)). So these results still do **not** answer your “powerful” question.

### A simple observation (why it feels hard)

If (p>k), then among $k$ consecutive integers, $p$ can divide **at most one** of them. So if (\Delta(n,k)) were powerful, every such large prime (p>k) that appears would have to divide that one term with exponent (\ge 2) [[nomath]](i.e. $p^2$ would have to divide that term)[[/nomath]]. Showing this must fail for every (k\ge 3) is exactly the missing step—and that is why the problem is still open. ([Erdős Problems][2])

So the best current answer is:

* **(k=2): yes, and infinitely often.** ([Wikipedia][1])
* **(k\ge 3): not known. Conjectured “no”, but unproved.** ([Erdős Problems][2])

[1]: https://en.wikipedia.org/wiki/Powerful_number?utm_source=chatgpt.com "Powerful number"
[2]: https://www.erdosproblems.com/forum/thread/137 "

    Erdős Problem #137 - Discussion thread

"
[3]: https://projecteuclid.org/journals/illinois-journal-of-mathematics/volume-19/issue-2/The-product-of-consecutive-integers-is-never-a-power/10.1215/ijm/1256050816.pdf?utm_source=chatgpt.com "THE PRODUCT OF CONSECUTIVE INTEGERS IS NEVER ..."
