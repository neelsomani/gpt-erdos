Let

[
d(A):=\max{|B|:B\subseteq A\text{ is dissociated}},
\qquad
f(n):=\min_{|A|=n} d(A).
]

[[nomath]](So $f(n)$ is the **guaranteed** size of a dissociated subset in any $n$-point set.)[[/nomath]]

A finite set (B\subset \mathbb R) is dissociated iff the only relation
(\sum_{b\in B}\varepsilon_b b=0) with (\varepsilon_b\in{-1,0,1}) is the trivial one; this is equivalent to the “all subset sums (\sum_{b\in S}b) are distinct” definition.

## Unconditional lower bound: (f(n)\ge \lfloor \log_3 n\rfloor)

Take (B\subseteq A) **maximal by inclusion** among dissociated subsets of $A$.
Then for every (a\in A\setminus B), the set (B\cup{a}) is *not* dissociated, so there exist two different subsets (S,T\subseteq B\cup{a}) with equal sum, and necessarily $a$ appears on exactly one side. Rearranging gives

[
a=\sum_{b\in B}\varepsilon_b b,\qquad \varepsilon_b\in{-1,0,1}.
]

Thus every element of $A$ lies in the ({-1,0,1})-span of $B$, which contains at most (3^{|B|}) distinct coefficient choices, hence at most (3^{|B|}) distinct values. Therefore

[
n=|A|\le 3^{|B|}\quad\Rightarrow\quad |B|\ge \log_3 n.
]

So (f(n)\ge \lfloor \log_3 n\rfloor). This is the “greedy/maximal dissociated subset” observation attributed to Erdős. ([Erdős Problems][1])

## Unconditional upper bound: (f(n)\le \log_2 n + \tfrac12\log_2\log_2 n + O(1))

To upper-bound $f(n)$, it suffices to exhibit one $n$-element set $A$ whose largest dissociated subset is not too large. Take

[
A={1,2,\dots,n}.
]

If (B\subseteq A) is dissociated with (|B|=m), then all (2^m) subset sums are **distinct integers** between $0$ and (\sum_{b\in B} b \le mn). Hence
[
2^m \le mn+1,
]
which already implies (m\le \log_2 n + O(\log\log n)).

Much sharper classical work (summarized in a recent note) gives
[
\max{|B|:B\subseteq{1,\dots,n}\text{ dissociated}}
\le \log_2 n+\frac12\log_2\log_2 n+O(1).
]
([arXiv][2])

Therefore
[
f(n)\le \log_2 n+\frac12\log_2\log_2 n+O(1).
]

## Net estimate: (f(n)=\Theta(\log n)), but the constant is unknown

Putting the two unconditional bounds together,
[
\boxed{\ \log_3 n\ \lesssim\ f(n)\ \lesssim\ \log_2 n+\tfrac12\log_2\log_2 n\ }.
]

So $f(n)$ grows on the order of (\log n), but current rigorous bounds still leave a gap between base $3$ and base $2$.

## About the specific question (f(n)\ge \lfloor \log_2 n\rfloor)

As of the most recent public discussion I can find, this exact inequality is **open**. The Erdős-problems entry lists only the (\lfloor\log_3 n\rfloor) lower bound and explicitly treats the question as open. ([Erdős Problems][3])

There is, however, a **very recent sketch** (posted Dec 2025 on the Erdős Problems forum) claiming the much stronger asymptotic lower bound
[
f(n)\ \ge\ (1-o(1))\log_2 n,
]
with some discussion/questions about details in the sketch. ([Erdős Problems][3])
This has not (at least there) been linked to a refereed write-up, and the problem is still marked open. Even if that asymptotic bound were fully validated, it would not automatically settle the **exact** floor bound for all $n$, because lower-order terms could in principle be negative.

So the best honest summary is:

* **Proved:** (f(n)\ge \lfloor\log_3 n\rfloor). ([Erdős Problems][1])
* **Proved:** (f(n)\le \log_2 n+\tfrac12\log_2\log_2 n+O(1)) [[nomath]](via $A={1,\dots,n}$)[[/nomath]]. ([arXiv][2])
* **Open:** whether (f(n)\ge \lfloor\log_2 n\rfloor) for all $n$. ([Erdős Problems][3])
* **Heuristic/announced (not settled):** a route to (f(n)\ge (1-o(1))\log_2 n). ([Erdős Problems][3])

If you want, I can also write out the (\log_3 n) greedy argument in a “choose elements one by one” form (rather than via maximality), and/or explain how the $[n]$ upper bound connects to the classical “largest dissociated subset of ({1,\dots,n})” problem.

[1]: https://www.erdosproblems.com/latex/963 "
  
    Erdős Problems
  
"
[2]: https://www.arxiv.org/pdf/2601.07068 "The Greedy Algorithm for Dissociated Sets"
[3]: https://www.erdosproblems.com/forum/thread/963 "

    Erdős Problem #963 - Discussion thread

"
