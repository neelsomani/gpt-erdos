Let
[
S_k(n):=\sum_{i=0}^{k-1}\omega(n+i),
\qquad\text{where }\omega(m)=|\\{p:\ p\mid m\\}|.
]

## 1) The liminf inequality with (k+\pi(k)) is **not** true [[nomath]](for all $k$)[[/nomath]]

Write
[
S_k(n)=\sum_{i=0}^{k-1}\ \sum_{p\mid (n+i)} 1
=\sum_{p}\ A_p(n),
]
where
[
A_p(n):=|\\{,0\le i<k:\ p\mid (n+i),\\}|
]
is the number of multiples of $p$ in the interval $[n,n+k-1]$.

If (p\le k) is prime, then **every** block of $k$ consecutive integers contains at least (\big\lfloor k/p\big\rfloor) multiples of $p$. Hence for every $n$,
[
A_p(n)\ge \Big\lfloor \frac{k}{p}\Big\rfloor
\quad (p\le k),
]
and therefore
[
S_k(n)\ge \sum_{p\le k}\Big\lfloor \frac{k}{p}\Big\rfloor.
]
This lower bound is independent of $n$, so
[
\liminf_{n\to\infty} S_k(n)\ \ge\ \sum_{p\le k}\Big\lfloor \frac{k}{p}\Big\rfloor.
]

Now compare this to (k+\pi(k)). Already at $k=26$,
[
\sum_{p\le 26}\Big\lfloor \frac{26}{p}\Big\rfloor
= \Big\lfloor\frac{26}{2}\Big\rfloor+\Big\lfloor\frac{26}{3}\Big\rfloor+\cdots+\Big\lfloor\frac{26}{23}\Big\rfloor
=13+8+5+3+2+2+1+1+1=36,
]
while (\pi(26)=9), so (k+\pi(k)=35). Thus (S_{26}(n)\ge 36) for all $n$, giving
[
\liminf_{n\to\infty} S_{26}(n)\ \ge\ 36\ >\ 35 = 26+\pi(26),
]
so the proposed inequality fails [[nomath]](and hence is not true “for every $k\ge 1$”)[[/nomath]].

In fact, (\sum_{p\le k}\lfloor k/p\rfloor\sim k\log\log k) (by Mertens’ theorem), so it eventually dwarfs (k+\pi(k)\sim k). Terence Tao has explicitly pointed out that (\pi(k)) in the Erdős–Selfridge formulation should be replaced by (\sum_{p\le k}\lfloor k/p\rfloor). ([Erdős Problems][1])

## 2) The limsup statement (\displaystyle \limsup_{n\to\infty} S_k(n),\frac{\log\log n}{\log n}=1)

* For $k=1$, this is the classical maximal-order fact
  [
  \limsup_{n\to\infty}\omega(n),\frac{\log\log n}{\log n}=1.
  ]

* For **(k\ge 2)**, the exact value of
  [
  L_k:=\limsup_{n\to\infty} S_k(n),\frac{\log\log n}{\log n}
  ]
  is (as far as I can verify from the literature/discussions around this problem) **open**.

What is known unconditionally are the easy bounds
[
1 \ \le\ L_k\ \le\ k.
]

* The **lower bound (L_k\ge 1)**: take $n$ along primorials (n=\prod_{p\le y}p), for which (\omega(n)\sim \log n/\log\log n); then (S_k(n)\ge \omega(n)), so the limsup is at least $1$.
* The **upper bound (L_k\le k)**: each (\omega(n+i)) individually is (\le (1+o(1))\log n/\log\log n), so summing $k$ terms gives (\le k(1+o(1))\log n/\log\log n).

Why proving (L_k=1) is hard even for $k=2$: when $k=2$,
[
S_2(n)=\omega(n)+\omega(n+1)=\omega(n(n+1))
]
[[nomath]](since $\gcd(n,n+1)=1$)[[/nomath]]. A remark by Luca–Pollack (discussing earlier work of Erdős–Nicolas) explains that even improving the **trivial** bound
[
\limsup_{n\to\infty}\omega(n(n+1))\Big/\big(\log n/\log\log n\big)\ \le\ 2
]
would already require ruling out infinitely many “special” $n$ [[nomath]](where $n(n+1)$ is a primorial)[[/nomath]], which they describe as seemingly unattackable with current methods. ([Pollack][2])
So the much stronger claim (L_2=1) [[nomath]](and similarly $L_k=1$ for general $k$)[[/nomath]] is well beyond what is currently proved.

Heuristically, (L_k=1) is plausible [[nomath]](very roughly: having $k$ *consecutive* integers all “as smooth as needed” to make each $\omega(n+i)$ near its individual maximum should be so rare that the best you can do is make only about $1/k$ of the maximum per term)[[/nomath]], but that heuristic is not a proof.

**Bottom line:**

* The first statement [[nomath]](with $k+\pi(k)$)[[/nomath]] is false for all sufficiently large $k$ [[nomath]](already $k=26$)[[/nomath]]. ([Erdős Problems][1])
* The second statement is known for $k=1$, but for (k\ge 2) it is an open problem; only the general bounds (1\le L_k\le k) are immediate, and even $k=2$ is very hard. ([Pollack][2])

[1]: https://www.erdosproblems.com/forum/thread/890 "

    Erdős Problem #890 - Discussion thread

"
[2]: https://pollack.uga.edu/primenote.pdf "https://pollack.uga.edu/primenote.pdf"
