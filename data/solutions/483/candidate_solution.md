Your $f(k)$ is exactly the **$k$-th Schur number** [[nomath]](often denoted $S(k)$ in the “minimal $N$” convention)[[/nomath]]: the least $N$ such that every $k$-coloring of ({1,\dots,N}) contains a monochromatic **Schur triple** (a+b=c) [[nomath]](with $a,b$ not necessarily distinct)[[/nomath]]. ([Wikipedia][1])

Equivalently, $f(k)-1$ is the **largest** $n$ for which $[1,n]$ can be partitioned into $k$ sum-free sets [[nomath]](no $x,y,z$ in the same part with $x+y=z$)[[/nomath]]. ([MathWorld][2])

## Known exact values

Only the first few are known exactly:
[
f(1)=2,\quad f(2)=5,\quad f(3)=14,\quad f(4)=45,\quad f(5)=161.
]
Moreover (f(5)=161) was established computationally (announced 2017). ([Wikipedia][1])

## General bounds (what we currently know asymptotically)

### Lower bound (explicit construction)

Schur’s original construction gives
[
f(k)\ \ge\ \frac{3^k+1}{2}.
]
So $f(k)$ is **at least exponential** in $k$, with base at least $3$. ([Amites Sarkar's Homepage][3])

More recent “template” constructions improve the *exponential growth rate*: one can derive inequalities of the form
[
S(n+5) > 380,S(n)+148
]
[[nomath]](for the “maximal $S(n)$” convention)[[/nomath]], implying that the exponential growth rate satisfies
[
\limsup_{k\to\infty} f(k)^{1/k}\ \ge\ 380^{1/5}\ \approx\ 3.28.
]
So any hypothetical bound (f(k)\le c^k) would need (c\gtrsim 3.28). ([arXiv][4])

### Upper bound (via multicolor Ramsey numbers)

Schur also related $f(k)$ to multicolor triangle Ramsey numbers:
[
f(k)\ \le\ R_k(3)-1,
]
and the classical Erdős–Szekeres recursion yields a factorial-type bound (R_k(3)\le k!,e+1), hence (f(k)\lesssim e,k!). ([Amites Sarkar's Homepage][3])

The **best currently recorded general upper bound** for (R_k(3)) (since 2002) is
[
R_k(3)\ \le\ k!,\bigl(e-\tfrac16\bigr)+1\qquad (k\ge 4),
]
so
[
f(k)\ \le\ k!,\bigl(e-\tfrac16\bigr)\qquad (k\ge 4),
]
which is still (\Theta(k!)) up to constants. ([arXiv][5])

Using Stirling’s formula, this is roughly
[
f(k)\ \le\ \text{const}\cdot \left(\frac{k}{e}\right)^k,
]
i.e. **super-exponential** [[nomath]](in the sense that $(f(k))^{1/k}$ is not bounded by a constant in this upper bound)[[/nomath]].

## So what is the best “estimate” today?

Putting these together, the current state of knowledge is:
[
\boxed{\ \frac{3^k+1}{2}\ \le\ f(k)\ \le\ \bigl(e-\tfrac16\bigr),k!\ \ \ (k\ge 4)\ }
]
and even the exponential base in the lower bound can be pushed to about (3.28) in a limsup sense by modern constructions. ([Amites Sarkar's Homepage][3])

There is therefore a **huge gap** between the best-known general lower and upper bounds: exponential vs factorial.

## Is (f(k) < c^k) for some constant $c$?

This is **open**. No bound of the form (f(k)\le c^k) [[nomath]](with $c$ independent of $k$)[[/nomath]] is currently known.

One way to see why it’s hard is that our best upper bounds go through the Ramsey inequality (f(k)\le R_k(3)-1), and even for (R_k(3)) it is not known whether there is a constant $C$ with (R_{k+1}(3)\le C,R_k(3)) for all $k$ (which would imply an exponential bound). ([arXiv][5])

So:

* **Lower bounds:** $f(k)$ is definitely exponential [[nomath]](base $>3$, and in fact $\ge 3.28$ in growth-rate terms)[[/nomath]]. ([Amites Sarkar's Homepage][3])
* **Upper bounds:** best general results are (\Theta(k!)). ([Amites Sarkar's Homepage][3])
* **Exponential upper bound (c^k):** unknown.

If you want, I can also sketch Schur’s construction giving (\frac{3^k+1}{2}), and the graph/triangle argument giving (f(k)\le R_k(3)-1), since those two ideas explain essentially all “generic” bounds we currently have.

[1]: https://en.wikipedia.org/wiki/Schur%27s_theorem "https://en.wikipedia.org/wiki/Schur%27s_theorem"
[2]: https://mathworld.wolfram.com/SchurNumber.html "https://mathworld.wolfram.com/SchurNumber.html"
[3]: https://faculty.sarkara.wwu.edu/Schur.pdf "https://faculty.sarkara.wwu.edu/Schur.pdf"
[4]: https://arxiv.org/pdf/2112.03175 "https://arxiv.org/pdf/2112.03175"
[5]: https://arxiv.org/pdf/1912.05353 "https://arxiv.org/pdf/1912.05353"
