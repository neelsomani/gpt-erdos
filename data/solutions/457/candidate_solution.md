Write (L=\lfloor \log n\rfloor).  A prime $p$ divides
(\prod_{1\le i\le L}(n+i)) **iff** the interval $(n,n+L]$ contains a multiple of $p$.
So your question asks whether there is some fixed (\epsilon>0) such that for infinitely many $n$, the short interval $(n,n+\log n]$ contains a multiple of **every** prime (p\le (2+\epsilon)\log n).

As of the latest available status (edited Oct 7, 2025), this is **open** (it is Erdős Problem #457, attributed to Erdős and Pomerance). ([Erdős Problems][1])

### What is known: you can reach $2+o(1)$, but no fixed (2+\epsilon) is proved

Let (y\to\infty) and set
$
N(y):=\prod_{y<p\le 2y} p,\qquad n:=N(y)-1.
$
Then
$
\log n \sim \log N(y)=\sum_{y<p\le 2y}\log p = \vartheta(2y)-\vartheta(y)\sim y
$
[[nomath]](using the prime number theorem in the form $\vartheta(x)\sim x$)[[/nomath]]. ([Wikipedia][2])

Now check primes (p\le 2y):

* If (p\le y), then for large $y$ we have (p\le \log n), so among (n+1,\dots,n+L) there is automatically a multiple of $p$, hence (p\mid \prod_{1\le i\le L}(n+i)).
* If (y<p\le 2y), then (p\mid N(y)=n+1), so again $p$ divides the product.

Thus for these $n$,
[
q(n,\log n)\ge (2+o(1))\log n,
]
i.e. all primes up to ((2+o(1))\log n) divide the product. This construction is explicitly mentioned on the problem page. ([Erdős Problems][1])

What remains unknown is whether one can improve $2+o(1)$ to (2+\epsilon) for some fixed (\epsilon>0) infinitely often (your question).

### Heuristics

In the discussion thread for the problem, Tao notes that “standard probabilistic heuristics” suggest $q(n,\log n)$ might typically be around
[
\log n\cdot \frac{\log\log n}{\log\log\log n},
]
which would be **much larger** than ((2+\epsilon)\log n) for large $n$. But this is only heuristic; no proof is known. ([Erdős Problems][3])

### A related (much weaker) general upper bound

More generally, with $q(n,k)$ the least prime not dividing (\prod_{1\le i\le k}(n+i)), one has the easy bound
[
q(n,k) < (1+o(1)),k\log n
]
(mentioned as “easy” on Erdős Problem #663). Plugging (k=\log n) gives (q(n,\log n)\lesssim (\log n)^2), so the regime ((2+\epsilon)\log n) is far below the best general upper bounds. ([Erdős Problems][4])

So: **no one currently knows** whether there exists a fixed (\epsilon>0) with infinitely many $n$ satisfying your divisibility condition; it’s an open Erdős–Pomerance problem. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/457 "
  
    Erdős Problem #457
  
"
[2]: https://en.wikipedia.org/wiki/Prime_number_theorem?utm_source=chatgpt.com "Prime number theorem"
[3]: https://www.erdosproblems.com/forum/thread/457 "

    Erdős Problem #457 - Discussion thread

"
[4]: https://www.erdosproblems.com/663 "
  
    Erdős Problem #663
  
"
