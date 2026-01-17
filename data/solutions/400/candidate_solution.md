This question is (essentially verbatim) **Erdős–Graham problem #400**. As far as I can tell from the standard references, **the specific asymptotics you ask for are still open**, even for (k=2). ([Erdős Problems][1])

That said, there is a fairly clear “known picture”:

## 1) General upper bounds: (g_k(n)\ll_k \log n)

Erdős and Graham already noted that it is “easy” to show
[
g_k(n)\ll_k \log n \quad\text{for all }n,
]
but that even the **best possible constant** in such an inequality is unknown. ([Erdős Problems][1])

A quick way to see (O_k(\log n)) is to look only at the prime $2$. Using Legendre’s formula in the form
[
v_2(m!) = m - s_2(m),
]
where (s_2(m)) is the sum of binary digits of $m$, the condition
[
a_1!\cdots a_k! \mid n!
]
implies
[
\sum_{i=1}^k (a_i - s_2(a_i)) \le n - s_2(n),
]
hence
[
g_k(n)=\sum a_i - n \le \sum s_2(a_i) - s_2(n).
]
Since (s_2(a_i)\le \lfloor \log_2 n\rfloor+1), this gives an explicit bound like
[
g_k(n)\le k(\log_2 n+1)-1,
]
so indeed (g_k(n)=O_k(\log n)).

For (k=2), a sharper *2-adic* analysis using valuations of products of consecutive integers and the “number of carries” interpretation (Kummer-type ideas) yields an improved explicit form
[
g_2(n)\ \le\ \log_2 n + O(\log\log n),
]
as discussed on MathOverflow. ([MathOverflow][2])

## 2) Nontrivial lower bounds: (g_k(n)) is (\Omega(\log n)) for “most” (n)

A key point is that (g_k(n)) is not just (O(\log n)): it can be **(\gg \log n)** for very many $n$.

Erdős–Graham–Ruzsa–Straus (1975) state that there is a small absolute constant (c>0) such that, **for all $n$** outside a set of asymptotic density $0$,
[
\frac{(2n)!}{n!,(n+\lfloor c\log n\rfloor)!}\in\mathbb{N}.
]
([Rényi Institute][3])

This immediately implies that for almost all $n$,
[
g_2(2n)\ \ge\ \lfloor c\log n\rfloor,
]
and hence (g_2(m)\ge c\log m+O(1)) for almost all $m$ [[nomath]](you can also pass from even to odd by the observation $g_2(m+1)\ge g_2(m)-1$)[[/nomath]]. So **(g_2(n)) is (\Theta(\log n)) for almost all $n$** in the weak sense “between positive constant multiples of (\log n)”. ([Rényi Institute][3])

For general (k\ge2), you always have
[
g_k(n)\ \ge\ g_2(n) + (k-2)
]
by taking the (k=2) optimizer and setting the remaining (a_i=1) [[nomath]](since $1!=1$ doesn’t affect divisibility)[[/nomath]]. So the same “(\gg \log n) for almost all $n$” lower bound propagates to every $k$. ([Rényi Institute][3])

## 3) Consequence: the *order of magnitude* of (\sum_{n\le x} g_k(n)) is (x\log x)

Putting the above together:

* From (g_k(n)\ll_k \log n), one gets
  [
  \sum_{n\le x} g_k(n)\ \ll_k\ x\log x.
  ]
  ([Erdős Problems][1])

* From the EGRS “almost all $n$” construction [[nomath]](already for $k=2$, hence for all $k$)[[/nomath]],
  one gets a lower bound of the shape
  [
  \sum_{n\le x} g_k(n)\ \gg_k\ x\log x
  ]
  [[nomath]](because $g_k(n)\gg \log n$ on a density‑$1$ subset)[[/nomath]]. ([Rényi Institute][3])

So **(\sum_{n\le x} g_k(n)) is (\Theta_k(x\log x))** in the sense of upper and lower bounds with positive constants.

## 4) But your precise questions [[nomath]](existence of $c_k$, mean value, and “normal order”)[[/nomath]] appear open

What is *not* currently known (and is exactly what Erdős/Graham formulated as a problem) is whether there is a **true constant** (c_k) such that
[
\sum_{n\le x} g_k(n)\ \sim\ c_k,x\log x,
]
or a **normal order** constant (c_k) such that (g_k(n) = c_k\log x + o(\log x)) for almost all (n\le x). ([Erdős Problems][1])

Even in the simplest case (k=2), the function has notable irregularities: for instance there are infinitely many $n$ [[nomath]](e.g. Mersenne numbers $n=2^m-1$)[[/nomath]] for which the “excess” $a+b-n$ is forced to be (\le 1) by a 2‑adic obstruction, so (g_2(n)) can be extremely small on an infinite subsequence. ([MathOverflow][2])
[[nomath]](This does *not* contradict an “almost all $n$” statement, since such subsequences have density $0$, but it highlights why pinning down a clean constant is delicate.)[[/nomath]]

---

### Bottom line

* **Yes**: one can show (g_k(n)=O_k(\log n)), and (using known constructions) (g_k(n)\gg \log n) for almost all $n$, hence (\sum_{n\le x} g_k(n)) has the *right order of magnitude* (x\log x). ([Erdős Problems][1])
* **No (currently)**: a proof of an asymptotic (\sum_{n\le x} g_k(n)\sim c_k x\log x) or a normal order (g_k(n)\sim c_k\log n) is not known; this is precisely an open Erdős–Graham problem. ([Erdős Problems][1])

If you want, I can also sketch how the “((2n)!/(n!(n+c\log n)!)\in\mathbb{N}) for almost all (n)” statement leads to a density‑$1$ lower bound (g_k(n)\gg\log n), and how the 2‑adic/carry arguments give the best currently “elementary-looking” upper bounds for (k=2), but the core answer to your two asymptotic questions is: **open.**

[1]: https://www.erdosproblems.com/latex/400 "
  
    Erdős Problems
  
"
[2]: https://mathoverflow.net/questions/137920/how-ab-can-grow-when-ab-mid-n?noredirect=1 "nt.number theory - How $a+b$ can grow when $a!b! \mid n!$ - MathOverflow"
[3]: https://renyi.hu/~p_erdos/1975-27.pdf "https://renyi.hu/~p_erdos/1975-27.pdf"
