This exact question is currently **not known** in general.

It is listed as **open** as “Erdős Problem #42” (last edited **14 September 2025**, with a comment by Terence Tao on **5 December 2025**), with the same wording you wrote. ([Erdős Problems][1])

### What is known right away

* **(M=1)**: yes [[nomath]](take any singleton $B={b}$; then $B-B={0}$)[[/nomath]].

* **(M=2)**: yes for all sufficiently large $N$ (in fact the standard size bound already forces it).

  Reason: if (A\subset{1,\dots,N}) is Sidon then it has size (|A|\le \sqrt N + O(N^{1/4})).
  So the number of *positive* differences in $A-A$ is
  [
  \binom{|A|}{2} \le \tfrac12 N + o(N) < N-1
  ]
  for large $N$. Hence there is some (d\in{1,\dots,N-1}) with (d\notin A-A).
  Then (B={1,1+d}) is Sidon and (B-B={0,\pm d}), so ((A-A)\cap(B-B)={0}).

### Why (M\ge 3) is hard / what people reduce it to

The discussion thread for the problem records a few standard reductions:

* You can assume $A$ is **maximal Sidon** (that was the original form).
* You can even **drop the requirement that (B) is Sidon**, because if you can find a large enough set $C$ with ((A-A)\cap(C-C)={0}), then a greedy argument finds a Sidon subset (B\subset C) of size (\approx \sqrt{|C|}). ([Erdős Problems][1])

So the real difficulty is: can one always find *any* moderately large set (C\subset [N]) whose nonzero differences avoid $A-A$?

### A simple obstruction you would worry about

If $(A-A)$ contains **all small differences up to some $K$**, then any $B$ of size $M$ would be forced to have all gaps $>K$, which is impossible once $K$ is about (N/(M-1)) [[nomath]](because $M$ points in $[N]$$ must have some consecutive gap $\le (N-1)/(M-1)$)[[/nomath]].

So one way the statement could fail is if there exist Sidon sets $A$ whose difference set contains a very long initial segment $\\{1,2,\dots,K\\}$ with $K$ a positive fraction of $N$. Whether Sidon sets can force *that* kind of “covering” by differences at this scale is part of what makes the question nontrivial.

(As background: Sidon sets are the same objects as **Golomb rulers**. Perfect Golomb rulers would cover *all* distances $1,2,\dots,\text{length}$ uniquely, and those are known not to exist for 5 or more marks; but that fact is **stronger** than what would be needed here and does not settle this Erdős question.)

### Bottom line

* **Yes** for $M=1,2$.
* For **(M\ge 3)**, a general answer is **not known** as of the latest public status I can find (January 2026): it remains an open Erdős problem. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/forum/thread/42 "https://www.erdosproblems.com/forum/thread/42"
