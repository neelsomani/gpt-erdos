Write (P^{+}(N)) for the largest prime factor of $N$.
Your condition says

[
P^{+}(m+i)>k\qquad (1\le i\le k),
]

i.e. the interval $[m+1,m+k]$ contains **no $k$-smooth numbers** [[nomath]](numbers whose prime factors are all $\le k$)[[/nomath]]. So $k(n)$ measures how long a gap one can force between $k$-smooth numbers with the start of the gap (\le n).

## Best known bounds (as of late 2025)

The problem is open in the sense that the correct order of growth of $k(n)$ is not known. What *is* known (and currently the “right” estimate to quote) is:

[
\exp!\left(\left(\frac1{\sqrt2}-o(1)\right)\sqrt{\log n,\log\log n}\right)
\le
k(n)
\le
(1+o(1)),n^{1/2}.
]

* The **upper bound** (k(n)\le (1+o(1))n^{1/2}) is a remark of Tao (given in the discussion): if (k>(1+\varepsilon)\sqrt n), then among (m+1,\dots,m+k) there is a number divisible by some prime $p$ with (\sqrt n<p<(1+\varepsilon)\sqrt n); for such a number (\le n+k), that prime $p$ is its largest prime factor, which is (<k), contradicting the defining property. ([Erdős Problems][1])
* The **lower bound** with the sharp-looking constant (1/\sqrt2) in the exponent is due to Tang (2025 note), using classical estimates for the distribution of smooth numbers. ([Erdős Problems][2])
* Historically, Erdős already noted a weaker lower bound (k(n)\gg_\varepsilon \exp((\log n)^{1/2-\varepsilon})) and conjectured (k(n)=o(n^\varepsilon)) for every (\varepsilon>0). ([Erdős Problems][2])

So: **currently $k(n)$ is known to be between a subpolynomial function (n^{o(1)}) [[nomath]](indeed $\exp((1/\sqrt2+o(1))\sqrt{\log n\log\log n})$)[[/nomath]] and (\asymp \sqrt n)**.

## Why the (\exp!\big(\tfrac1{\sqrt2}\sqrt{\log n\log\log n}\big)) scale shows up (heuristic)

Let (x\approx n), $y=k$, and let (\Psi(x,y)) count $y$-smooth numbers (\le x). Classical smooth-number theory says (\Psi(x,y)\approx x,\rho(u)) with (u=\frac{\log x}{\log y}) and (\rho) the Dickman–de Bruijn function.

Heuristically, near size $x$, the “density” of $y$-smooth numbers is about (\rho(u)). Then a random interval of length $y$ contains about (y\rho(u)) smooth numbers on average, and the largest smooth-free gap up to $x$ is around (\frac{\log x}{\rho(u)}). Setting the desired gap length $y$ equal to this heuristic size leads to an implicit equation (y\rho(u)\approx \log x), and solving it gives the scale

[
\log y \sim \frac1{\sqrt2}\sqrt{\log x\log\log x},
]

which matches Tang’s proved lower bound. ([Erdős Problems][2])

## Bottom line

A reasonable “estimate” to report today is:

[
k(n)=\exp\left((1/\sqrt2+o(1))\sqrt{\log n\log\log n}\right)\quad\text{(proved lower bound)}
]

and

[
k(n)\le (1+o(1))\sqrt n\quad\text{(best simple upper bound currently recorded)}.
]

Closing the vast gap between (n^{o(1)}) and (n^{1/2}) is exactly the open part of the problem. ([Erdős Problems][2])turn7view0

[1]: https://www.erdosproblems.com/forum/thread/962 "

    Erdős Problem #962 - Discussion thread

"
[2]: https://www.erdosproblems.com/latex/962 "
  
    Erdős Problems
  
"
