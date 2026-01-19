Write $y=n$ and (x=n^{k}) ((k\ge2)). Then
[
A={m\in[n,x]: \exists d\in(y,2y)\text{ with }d\mid m}.
]
Equivalently, (A\cap[1,x]) is the “set of multiples of the short interval $(y,2y)$”, and its counting function is the standard quantity
[
H(x,y,2y):=|\\{m\le x:\ \exists d\in(y,2y]\text{ with }d\mid m\\}|.
]

## What is known unconditionally: size of $A$ and the *average* gap

A theorem of Ford gives (up to multiplicative constants) the order of magnitude of $H(x,y,2y)$ in the regime (3\le y\le \sqrt{x}):
[
H(x,y,2y)\asymp \frac{x}{(\log y)^{\delta}(\log\log y)^{3/2}},
\qquad
\delta = 1-\frac{1+\log\log 2}{\log 2}=0.086071\ldots
]
([Kevin Ford's Home Page][1])

Since (k\ge2), we have (y=n\le \sqrt{n^{k}}=\sqrt{x}), so this applies directly with (x=n^k). Therefore
[
|A| = H(n^k,n,2n) - O(n)
\asymp
\frac{n^k}{(\log n)^{\delta}(\log\log n)^{3/2}}.
]
([Kevin Ford's Home Page][1])

Hence the **mean spacing** between successive elements of $A$ in $[n,n^k]$ is
[
\frac{n^k}{|A|}
\asymp
(\log n)^{\delta}(\log\log n)^{3/2}.
]
In particular,
[
\max_i (a_{i+1}-a_i)\ \ge\ \text{(average gap)}\ \asymp\ (\log n)^{\delta}(\log\log n)^{3/2}.
]

So the “natural scale” for gaps is already polylogarithmic.

## Trivial upper bound for the *max* gap

Since (n+1\in(n,2n)), every multiple of $n+1$ belongs to $A$. Therefore $A$ contains the arithmetic progression
[
n+1,\ 2(n+1),\ 3(n+1),\ \dots
]
[[nomath]](up to $n^k$)[[/nomath]], and this alone implies
[
\max_i (a_{i+1}-a_i)\ \le\ n+1.
]
[[nomath]](This is only $O(n)$, far from polylog, but it is unconditional and immediate.)[[/nomath]]

## What one *expects* for the maximal gap, and the polylog question

Ford’s estimate says the density of $A$ up to (n^k) is about
[
p \asymp \frac{1}{(\log n)^{\delta}(\log\log n)^{3/2}}.
]
([Kevin Ford's Home Page][1])

If you model membership in $A$ as a “pseudo-random” event of probability $p$, then the **largest gap** in an interval of length (\asymp n^k) is heuristically on the order of
[
\frac{\log(n^k)}{p}
\asymp
k,(\log n)^{1+\delta}(\log\log n)^{3/2}.
]
So the heuristic prediction is very much
[
\max_i (a_{i+1}-a_i) = (\log n)^{O(1)}.
]

That said, proving a bound of the form (\max_i(a_{i+1}-a_i)\le (\log n)^C) would require **very strong “no exceptionally long empty interval” control** for the set of integers having a divisor in $(n,2n)$, at scales comparable to (a power of) (\log n). Ford’s work (and the surrounding literature) gives sharp *global counts* $H(x,y,2y)$, and explains that the underlying phenomenon involves substantial clustering of divisors (which is exactly why the density is smaller than the naive heuristic). ([Kevin Ford's Home Page][1])
But these global results do not, by themselves, rule out rare unusually large gaps on polylogarithmic scales.

### Bottom line

* **Unconditional, from known theory:**
  [
  (\log n)^{\delta}(\log\log n)^{3/2}\ \ll\ \max_i(a_{i+1}-a_i)\ \le\ n+1,
  \qquad \delta=0.086071\ldots
  ]
  with the lower scale coming from Ford’s estimate for (|A|). ([Kevin Ford's Home Page][1])
* **Heuristic expectation:**
  [
  \max_i(a_{i+1}-a_i)\ \asymp\ k(\log n)^{1+\delta}(\log\log n)^{3/2},
  ]
  hence **yes, polylog**.
* **Status of “(\le (\log n)^{O(1)})?”**
  I don’t know of an unconditional theorem in the literature that upgrades Ford’s global counting to a *worst-case* polylog gap bound in this setting; it seems to demand a level of uniformity in very short intervals that is typically hard to prove.

If you want, I can also sketch what kind of “short interval” estimate for $H(x,y,2y)$ would be sufficient to deduce a polylog bound on (\max_i(a_{i+1}-a_i)), and why it resembles (but should be easier than) the philosophy behind prime-gap bounds.

[1]: https://ford126.web.illinois.edu/wwwpapers/hxy2y.pdf "https://ford126.web.illinois.edu/wwwpapers/hxy2y.pdf"
