No—at least **conditionally**.

This question is *exactly* **Erdős Problem #884**. ([Erdős Problems][1])

Terence Tao wrote a note (dated **September 9, 2025**) showing that **assuming a qualitative form of the Hardy–Littlewood prime tuples conjecture**, Erdős’s proposed absolute-constant bound **fails**: the ratio
$
\frac{\sum_{1\le i<j\le \tau(n)} \frac{1}{d_j-d_i}}{1+\sum_{1\le i<\tau(n)} \frac{1}{d_{i+1}-d_i}}
$
is **unbounded** as (n\to\infty). 

More concretely, Tao’s construction [[nomath]](taking $n$ to be a product of “nearly consecutive primes”)[[/nomath]] produces, for arbitrarily large $K$, infinitely many $n$ such that
$
\sum_{1\le i<j\le\tau(n)}\frac1{d_j-d_i}\ \gg\ \log K
\quad\text{but}\quad
\sum_{1\le i<\tau(n)}\frac1{d_{i+1}-d_i}\ \ll\ 1,
$
which immediately forces the ratio above to blow up, so there cannot be an absolute implied constant in your (\ll). 

### What is known unconditionally?

Unconditionally, Tao notes a general upper bound (coming from harmonic-mean/arithmetic-mean or Cauchy–Schwarz plus a telescoping/harmonic-series argument):
$
\sum_{1\le i<j\le\tau(n)}\frac1{d_j-d_i}
\ \ll\ (\log \tau(n)) \sum_{1\le i<\tau(n)}\frac1{d_{i+1}-d_i}.
$
So the “gap” between the two sides is at worst **logarithmic in (\tau(n))**. 

### Bottom line

* **If** one assumes the qualitative Hardy–Littlewood prime tuples conjecture, then the inequality with an **absolute** implied constant is **false** (ratio unbounded). 
* **Without** that conjecture, the absolute-constant version is (as far as current public references indicate) **not settled**; the Erdős Problems site still lists it as open in that unconditional sense. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/884 "
  
    Erdős Problem #884
  
"
