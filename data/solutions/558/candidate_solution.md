Because (K_{s,t}\cong K_{t,s}), we may assume (1\le s\le t).  In general, $R(K_{s,t};k)$ is **not known exactly**; what is known are sharp results in some special cases and general upper/lower bounds.

## Exact case $s=1$ (stars)

Here (K_{1,t}) is a star on $t+1$ vertices. Burr–Roberts (as quoted by Chung–Graham) give the exact multicolour value
[
R(K_{1,t};k)=
\begin{cases}
k(t-1)+1,&\text{if }k\equiv t\equiv 0\pmod 2,\
k(t-1)+2,&\text{otherwise.}
\end{cases}
]
([fanchung.ucsd.edu][1])

## General bounds for (s\ge 2)

Chung and Graham proved the general upper bound [[nomath]](for $k>1$ and $t>s>2$)[[/nomath]]
[
R(K_{s,t};k)\ \le\ (t-1)\bigl(k+k^{1/s}\bigr)^s.
]
In particular, as (k\to\infty) with fixed (s,t), this is ((t-1+o(1))k^s). ([fanchung.ucsd.edu][1])

They also proved a general probabilistic lower bound
[
(2\pi\sqrt{st})^{\frac1{s+t}}\\(\frac{s+t}{e^2}\\)k^{\frac{st-1}{s+t}}
\ \le\ R(K_{s,t};k),
]
so for fixed (s,t) one always has at least polynomial growth in $k$ with exponent (\frac{st-1}{s+t}). ([Erdős Problems][2])

Moreover, they note that when (t\gg s), this lower bound is essentially of the form
[
R(K_{s,t};k)\ \gtrsim\ \frac{t}{e^2},k^s,
]
which is close (up to a constant factor) to the upper bound (\sim (t-1)k^s). ([fanchung.ucsd.edu][1])

## Sharper results in key special cases

### The 4-cycle (K_{2,2}=C_4)

Chung–Graham show
[
R(K_{2,2};k)\ <\ k^2+k+1,
]
and for $k-1$ a prime power they construct a colouring showing
[
R(K_{2,2};k)\ >\ k^2-k+1.
]
Together these imply
[
R(K_{2,2};k)=(1+o(1))k^2.
]
([fanchung.ucsd.edu][1])

### The (3\times 3) case

Alon–Rónyai–Szabó (using norm-graph constructions) proved the asymptotic formula
[
R(K_{3,3};k)=(1+o(1))k^3.
]
[[nomath]](They state it in terms of the “largest $m$” that can be coloured without a monochromatic $K_{3,3}$; converting to the “least forcing $m$” changes the value by at most $1$.)[[/nomath]] 

### Very unbalanced bipartite graphs

For fixed (t\ge 2) and sufficiently large $s$ [[nomath]](specifically $s\ge (t-1)!+1$)[[/nomath]], Alon–Rónyai–Szabó prove
[
R(K_{t,s};k)=\Theta(k^t).
]
So in this regime the growth rate in $k$ matches the **smaller** side $t$. 

## What is “the answer” in full generality?

Beyond the cases above, **determining $R(K_{s,t};k)$ precisely is open**.  The best general statement currently is the sandwich [[nomath]](for $2\le s\le t$)[[/nomath]]
[
(2\pi\sqrt{st})^{\frac1{s+t}}\\(\frac{s+t}{e^2}\\),k^{\frac{st-1}{s+t}}
\ \le\ R(K_{s,t};k)\ \le\ (t-1)\bigl(k+k^{1/s}\bigr)^s,
]
together with the sharper asymptotics in special cases (K_{2,2}), (K_{3,3}), and the unbalanced range (s\ge (t-1)!+1). ([Erdős Problems][2])

Chung and Graham explicitly conjectured that for (t>s>2),
[
R(K_{s,t};k)\sim (t-1)k^s,
]
but this is only proved in certain cases/ranges. ([fanchung.ucsd.edu][1])

[1]: https://fanchung.ucsd.edu/ron/papers/75_05_multicolor.pdf "PII: 0095-8956(75)90043-X"
[2]: https://www.erdosproblems.com/latex/558 "
  
    Erdős Problems
  
"
