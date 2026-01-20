As of **January 2026**, this is **open** in general (it is listed as Erdős Problem #543). ([Erdős Problems][1])

What *is* known is that $f(N)$ sits between (\log_2 N) and (\log_2 N + \Theta(\log\log N)):

## Lower bound: (f(N)\ge \log_2 N)

For any $A$ with (|A|=k), there are only (2^k) subsets (S\subseteq A), hence at most (2^k) subset sums (\sum_{x\in S}x). If these subset sums cover all $N$ elements of $G$, then (2^k\ge N), i.e.
[
k\ge \log_2 N.
]

So you cannot hope for $f(N)$ below (\log_2 N) (up to lower-order terms).

## Best known general upper bound: (f(N)\le \log_2 N + O(\log\log N))

Erdős–Rényi (1965) proved a much more quantitative statement: if one chooses $k$ random elements in an abelian group of order $n$ [[nomath]](they work with random sequences; for $k=O(\log n)$ this is essentially the same as a random $k$-set)[[/nomath]], then for any (\delta>0), if
[
k \ge \frac{\log n + 2\log(1/\delta) + \log\log n}{\log 2} + O(1),
]
then with probability at least (1-\delta), **every** group element has at least one representation as a subset sum [[nomath]](i.e. $\min_b V_k(b)>0$ in their notation)[[/nomath]]. ([Rényi Institute][2])

Taking (\delta=1/2) gives
[
f(N) \le \log_2 N + \log_2\log N + O(1),
]
which is (equivalently) (\log_2 N + O(\log\log N)). ([Rényi Institute][2])

## So what about (\log_2 N + o(\log\log N))?

That is **exactly** the open part: whether one can remove the “(\Theta(\log\log N))” overhead in the worst case.

* The Erdős Problems site records the state as open and notes Erdős’ belief that improving the Erdős–Rényi bound to $o(\log\log N)$ should be **impossible**. ([Erdős Problems][1])
* No matching lower bound of the form (\log_2 N + c\log\log N) is currently established in full generality (otherwise the problem would be resolved).

## Heuristic picture (why many people expect “no”)

Write (k=\log_2 N + t). Then the number of subset sums is (2^k = N\cdot 2^t), and for a “random-like” group (think cyclic of prime order), one expects the subset sums to behave somewhat like (N\cdot 2^t) “samples” spread over $N$ elements.

In the **independent-sampling** (coupon collector) heuristic, a typical element is missed with probability about (\exp(-2^t)), so the expected number of missed elements is about (N\exp(-2^t)), which is huge unless (2^t) is on the order of (\log N). That predicts a threshold near
[
2^k \sim N\log N\quad\Longleftrightarrow\quad k \sim \log_2 N + \log_2\log N.
]
This lines up perfectly with the Erdős–Rényi sufficient condition. ([Rényi Institute][2])

On the other hand, in highly 2-torsion groups like (G=(\mathbb Z/2\mathbb Z)^n) [[nomath]](where $N=2^n$)[[/nomath]], subset sums are exactly the (\mathbb F_2)-span of $A$, and spanning can occur already for (k=n+O(1)=\log_2 N+O(1)); so **some** groups do not need a (\log\log N) overhead. [[nomath]](But $f(N)$ is a *worst-case over groups* parameter.)[[/nomath]]

## Bottom line

* **What you asked:** whether (f(N) \le \log_2 N + o(\log\log N)).
* **Current status:** **open**. ([Erdős Problems][1])
* **Best general bound known:**
  [
  \log_2 N \le f(N) \le \log_2 N + \log_2\log N + O(1).
  ]
  ([Rényi Institute][2])
* **Belief/heuristics:** many expect the (\Theta(\log\log N)) term to be genuinely necessary in the worst case (Erdős reportedly believed so), but proving a lower bound of that strength remains out of reach. ([Erdős Problems][1])

If you tell me whether you care about a **specific family of groups** [[nomath]](e.g. cyclic groups $ \mathbb Z/N\mathbb Z$, or prime cyclic groups, or $2$-groups)[[/nomath]], I can summarize what the Erdős–Rényi method actually gives there and what the main obstacles are for a matching lower bound.

[1]: https://www.erdosproblems.com/543 "https://www.erdosproblems.com/543"
[2]: https://renyi.hu/~p_erdos/1965-15.pdf "https://renyi.hu/~p_erdos/1965-15.pdf"
