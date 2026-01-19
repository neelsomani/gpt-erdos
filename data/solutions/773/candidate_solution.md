Let
[
S_N:={1^2,2^2,\dots,N^2},\qquad F(N):=\max{|A|:A\subseteq S_N\ \text{is Sidon}},
]
where “Sidon” means (a+b=c+d) with (a,b,c,d\in A) forces ({a,b}={c,d}).

### Best known bounds (as of now)

The problem is open, with the best published bounds
[
F(N)\ \gg\ N^{2/3}
\qquad\text{and}\qquad
F(N)\ \ll\ \frac{N}{(\log N)^{1/4}}.
]
([Erdős Problems][1])

### Why the upper bound is (N/(\log N)^{1/4})

If (|A|=m), then Sidon implies all (\binom{m+1}{2}) sums $a+b$ [[nomath]](with $a\le b$)[[/nomath]] are distinct and lie in $[2,2N^2]$. Every such sum is a sum of two squares.

Landau’s theorem (a.k.a. the Landau–Ramanujan theorem) says the count of integers (\le x) representable as a sum of two squares is (\asymp x/\sqrt{\log x}). In particular the number of *possible distinct* sums of two squares up to (2N^2) is (O\left(N^2/\sqrt{\log N}\right)). Thus
[
\binom{m+1}{2}\ \le\ O\left(\frac{N^2}{\sqrt{\log N}}\right)
\quad\Rightarrow\quad
m\ \ll\ \frac{N}{(\log N)^{1/4}}.
]
This is exactly the upper bound Alon–Erdős point out using Landau’s result. ([Princeton Mathematics][2])

### Lower bounds

* Alon–Erdős (1985) show (|A|\ge N^{2/3-o(1)}) is achievable [[nomath]](more precisely, for every $\varepsilon>0$ one can get $\gg N^{2/3-\varepsilon}$)[[/nomath]]. ([Princeton Mathematics][2])
* Lefmann–Thiele improve this to a clean polynomial lower bound (|A|\gg N^{2/3}). ([Refubium][3])

### So, is it (N^{1-o(1)})?

* **Upper bound:** yes, the best known upper bound is
  [
  F(N)\ll \frac{N}{(\log N)^{1/4}}=N^{1-o(1)},
  ]
  since ((\log N)^{1/4}=N^{o(1)}). ([Princeton Mathematics][2])
* **Lower bound / truth:** **open**. The best proven lower bound exponent is still $2/3$. ([Erdős Problems][1])

So the current state is:
[
N^{2/3}\ \lesssim\ F(N)\ \lesssim\ \frac{N}{(\log N)^{1/4}},
]
and closing the gap [[nomath]](in particular, proving a near-linear $N^{1-o(1)}$ *lower* bound, or showing it’s impossible)[[/nomath]] remains unsolved. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/773 "https://www.erdosproblems.com/773"
[2]: https://web.math.princeton.edu/~nalon/PDFS/Publications2/An%20application%20of%20graph%20theory%20to%20additive%20number%20theory.pdf "https://web.math.princeton.edu/~nalon/PDFS/Publications2/An%20application%20of%20graph%20theory%20to%20additive%20number%20theory.pdf"
[3]: https://refubium.fu-berlin.de/bitstream/handle/fub188/18122/1994_16.pdf?isAllowed=y&sequence=1 "https://refubium.fu-berlin.de/bitstream/handle/fub188/18122/1994_16.pdf?isAllowed=y&sequence=1"