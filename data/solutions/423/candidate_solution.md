This is **Hofstadter’s “consecutive-sum” greedy sequence**, listed as **OEIS A005243**. It was posed by Hofstadter and recorded by Erdős (who explicitly asked for its asymptotic behaviour). 

### What is known rigorously (as of January 2026)

Let
[
b_n:=a_n-n.
]
Because ({a_1,\dots,a_n}) consists of $n$ distinct integers in ({1,2,\dots,a_n}), we have the *exact* interpretation
[
b_n = |\\{m\le a_n:\ m\notin {a_k}\\}|,
]
i.e. (b_n) counts how many **positive integers are missing** from the sequence up to (a_n). The missing integers form the complementary sequence **OEIS A048973**. ([OEIS][1])

The main new qualitative fact is:

* **Infinitely many integers never appear** in the sequence [[nomath]](so $b_n$ is **unbounded**)[[/nomath]]. This was proved independently by **Quanyu Tang** and **Matthew Bolan** (notes linked from the Erdős Problems database/discussion). ([Erdős Problems][2])
  In particular, the sequence is **not** eventually of the form (a_n=n+B) for some constant $B$. ([Erdős Problems][2])

Beyond that, the actual *rate* of growth of (b_n) [[nomath]](and hence the asymptotic behaviour of $a_n$)[[/nomath]] is **still open**; the Erdős Problems database currently lists this as an open problem. ([Erdős Problems][2])

So the short honest answer is: **no proven asymptotic formula is known.**

### What computations suggest (heuristics, not theorems)

The discussion around Erdős Problem #423 includes large-scale data on how many numbers are missing up to powers of two. For example, the number of missing integers up to (x=2^m) includes: ([Erdős Problems][2])

* (x=2^{20}\approx 1.05\times 10^6): missing count (=1308)
* (x=2^{33}\approx 8.59\times 10^9): missing count (=44460)

This shows the deficit is **tiny compared to $x$** at those ranges, so empirically the sequence seems to have **very high density** [[nomath]](suggesting $a_n=n+o(n)$)[[/nomath]], but that is **not proved**.

Tang also reports numerics up to $n=30000$ suggesting a power-law type growth
[
b_n \approx n^\alpha \quad\text{for some } \tfrac15<\alpha<\tfrac12,
]
possibly around (or slightly below) (\alpha\approx 1/3), with slowly varying corrections. ([Erdős Problems][2])

Separately, the OEIS entry for the complement (missing numbers) notes that the $k$-th missing number “appears to be growing slightly faster than quadratically,” which is consistent with “about (\sqrt{x})” missing numbers up to $x$, perhaps with a slowly varying factor. ([OEIS][1])

### Bottom line

* **Proved:** infinitely many integers are omitted [[nomath]](so $a_n-n\to\infty$)[[/nomath]]. ([Erdős Problems][2])
* **Open:** the true asymptotic size of (a_n) [[nomath]](e.g., does $a_n/n\to 1$? what is the growth rate of $a_n-n$?)[[/nomath]]. 
* **Empirically:** (a_n) looks extremely close to $n$, with (a_n-n) growing very slowly [[nomath]](on the order of $10^3$ at $10^6$ and $4\times 10^4$ at $10^{10}$)[[/nomath]]. ([Erdős Problems][2])

If you want, I can also summarize the *exact statement* of Erdős’s original question in the 1977 paper (it’s just a couple of lines) and how it matches the OEIS/MathWorld formulation. 

[1]: https://oeis.org/A048973 "A048973 - OEIS"
[2]: https://www.erdosproblems.com/forum/thread/423 "

    Erdős Problem #423 - Discussion thread

"
