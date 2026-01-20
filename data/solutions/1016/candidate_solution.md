Your function $h(n)$ is exactly the “extra edges beyond a Hamilton cycle” needed to build a **pancyclic** $n$-vertex graph [[nomath]](a graph containing a cycle of every length $3,4,\dots,n$)[[/nomath]]. Equivalently, if $m(n)$ denotes the minimum number of edges in an $n$-vertex pancyclic graph, then
[
m(n)=n+h(n).
]
This is Bondy’s classic problem from 1971. 

## Best-known general bounds

The currently standard bounds are
[
\log_2(n-1)-1 \le h(n) \le \log_2 n + \log_* n + O(1),
]
[[nomath]](up to minor conventions on $\log_*$)[[/nomath]]. 

In particular,
[
h(n)=\Theta(\log n)
\quad\text{and}\quad
h(n)=\log_2 n + O(\log_* n),
]
so also (h(n)=(1+o(1))\log_2 n). 

### Why the lower bound (\log_2(n-1)-1) holds

If a pancyclic graph has $n+k$ edges, then it has a Hamilton cycle [[nomath]](length $n$)[[/nomath]], so you can view it as a Hamilton cycle plus $k$ **chords**. Shi showed that a Hamiltonian graph with $k$ chords has at most (2^{k+1}-1) distinct cycles. Since pancyclicity forces at least $n-2$ cycles [[nomath]](one for each length $3,\dots,n$)[[/nomath]], you get
[
2^{k+1}-1 \ge n-2 \Rightarrow k \ge \log_2(n-1)-1.
]
This yields the stated lower bound on $h(n)$. 

### Where the upper bound (\log_2 n+\log_* n+O(1)) comes from

Bondy stated this upper bound (without proof); the first published proof/construction is credited (in modern sources) to later writeups (e.g. in the monograph literature). ([Erdős Problems][1])

At a high level, one takes an $n$-cycle $H$ and adds about (K\approx \log_2 n) carefully placed “shortcuts”/chords whose lengths are powers of 2 and arranged consecutively so that **binary encoding** of subsets of shortcuts produces cycles of many different lengths (covering a long interval of lengths). Then one extra edge extends coverage to another large interval. The remaining missing short lengths [[nomath]](essentially up to about $K$)[[/nomath]] can be filled by an additional recursive gadget using only $O(\log_* n)$ more edges. 

[[nomath]](Griffin states Bondy’s bound in the form $\log_2 n + H(n)+O(1)$, where $H(n)$ is the least number of iterated base‑2 logs needed to bring $n$ below 2; this differs from $\log_* n$ by at most an additive constant.)[[/nomath]] 

## About your specific question: is the (\log_* n) term necessary in the lower bound?

As of the most recent sources I checked, this is **still open**. In fact, the gap is so stubborn that Erdős already noted (in this context) that one cannot even prove the much weaker statement
[
h(n)-\log_2 n \to \infty.
]
So the conjectural strengthening
[
h(n) \ge \log_2 n + \log_* n - O(1)
]
is not known, and even “$h(n)$ exceeds (\log_2 n) by an unbounded amount” remains unproved. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/latex/1016 "
  
    Erdős Problems
  
"
