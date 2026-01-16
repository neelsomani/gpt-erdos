What you wrote is *exactly* **Erdős Problem #218** on consecutive prime gaps, and it is currently listed as **open**. ([Erdős Problems][1])

So at present:

* The **density $1/2$** claims for
  ({n : d_{n+1}\ge d_n}) and ({n : d_{n+1}\le d_n}) are **conjectural**. ([Erdős Problems][1])
* The statement “**infinitely many** $n$ with (d_{n+1}=d_n)” is also **not proved** [[nomath]](and Erdős even conjectured much longer runs $d_n=\cdots=d_{n+k}$)[[/nomath]]. ([Erdős Problems][1])

What *is* known unconditionally is weaker but nontrivial:

## Known: both directions occur infinitely often

Already in 1948, Erdős–Turán proved that
[
d_{n+1}-d_n
]
changes sign infinitely often; i.e. there are infinitely many $n$ with (d_{n+1}>d_n) and infinitely many with (d_{n+1}<d_n). ([arXiv][2])

More generally, the Erdős–Pólya–Turán conjecture on sign changes of *linear combinations* of consecutive prime gaps was proved by Pintz (using Maynard–Tao technology). ([arXiv][2])

None of this gives density $1/2$, but it does confirm “infinitely often” oscillation.

## What *can* be proved: the equality case has density $0$

A key observation (noted by Tao on the #218 forum thread) is that one should be able to show
[
{n:\ d_{n+1}=d_n}
]
has **natural density $0$**; if true, then the “(\ge)” and “(\le)” density-$1/2$ questions become equivalent. ([Erdős Problems][3])

In fact, one can justify this density-zero claim using standard upper-bound sieve estimates for prime 3-tuples. A convenient explicit reference is Lemma 5.1 in Ford–Konyagin–Luca, which gives an upper-bound sieve estimate for simultaneous primality of several linear forms. ([Kevin Ford's Home Page][4])

Here is a clean sketch (the same splitting idea is also described in the forum thread): ([Erdős Problems][3])

### Step 1: translate the equality event into a prime triple

Let
[
T(x)=#{n:\ p_{n+2}\le x,\ d_{n+1}=d_n}.
]
If (d_{n+1}=d_n=d), then
[
p_n,\ p_n+d,\ p_n+2d
]
are primes. (They are in arithmetic progression; “consecutive” only makes this condition stronger, so counting *all* such prime triples gives an upper bound.)

### Step 2: split by a threshold (y)

Choose
[
y=(\log x)^{4/3}.
]
Write (T(x)=T_{\le y}(x)+T_{>y}(x)), depending on whether the common gap $d$ is (\le y) or (>y).

### Step 3: large equal gaps (d>y) are rare by telescoping

If (d_{n+1}=d_n>y), then in particular (d_n>y). The number of indices (m\le \pi(x)) with (d_m>y) is bounded by
[
#\\{m\le \pi(x): d_m>y\\}\ \le\ \frac{\sum_{m\le \pi(x)} d_m}{y}.
]
But (\sum_{m\le \pi(x)} d_m = p_{\pi(x)+1}-2 \ll x) [[nomath]](indeed $p_{\pi(x)+1}$ is the next prime after $x$, and is $\ll x$)[[/nomath]]. Hence
[
T_{>y}(x)\ \ll\ \frac{x}{y}.
]
With (y=(\log x)^{4/3}), this is (o(x/\log x)), hence (o(\pi(x))).

[[nomath]](This exact “telescoping sum $\Rightarrow x/y$” idea is explicitly mentioned in the #218 discussion. ([Erdős Problems][3]))[[/nomath]]

### Step 4: small equal gaps (d\le y) are rare by a 3-tuple sieve bound

For each fixed $d$, let
[
A_d(x)=#\\{n\le x:\ n,\ n+d,\ n+2d\ \text{are prime}\\}.
]
Upper-bound sieve theory for prime $k$-tuples [[nomath]](here $k=3$)[[/nomath]] yields
[
A_d(x)\ \ll\ \frac{x}{(\log x)^3},\mathfrak{S}(d),
]
where (\mathfrak{S}(d)) is the singular series for the tuple $(0,d,2d)$. A form of such an upper bound is given in Lemma 5.1 of Ford–Konyagin–Luca [[nomath]](applied with the three linear forms $n,\ n+d,\ n+2d$)[[/nomath]]. ([Kevin Ford's Home Page][4])

Moreover, one has a crude bound (\mathfrak{S}(d)\ll (d/\varphi(d))^2 \ll (\log\log d)^2), so for (d\le y),
[
\mathfrak{S}(d)\ \ll\ (\log\log y)^2.
]
Therefore,
[
T_{\le y}(x)\ \le\ \sum_{d\le y} A_d(x)\ \ll\ \sum_{d\le y} \frac{x}{(\log x)^3}(\log\log y)^2
\ \ll\ \frac{x,y,(\log\log y)^2}{(\log x)^3}.
]
With (y=(\log x)^{4/3}), this is (x/(\log x)^{5/3}) up to polylogs, i.e. again (o(x/\log x)=o(\pi(x))).

### Conclusion

Both pieces are (o(\pi(x))), so
[
\frac{T(x)}{\pi(x)}\to 0.
]
Equivalently, the set ({n:\ d_{n+1}=d_n}) has **natural density $0$**.

## What this buys you for the original density-(1/2) questions

Let

* (A={n:\ d_{n+1}>d_n}),
* (B={n:\ d_{n+1}<d_n}),
* (C={n:\ d_{n+1}=d_n}).

Then $A,B,C$ partition (\mathbb{N}). If $C$ has density $0$, then (assuming densities exist) you get
[
\text{dens}(A)+\text{dens}(B)=1,\qquad
\text{dens}({d_{n+1}\ge d_n})=\text{dens}(A),
]
and similarly for (\le). So the first two “(\ge)” and “(\le)” density-$1/2$ claims reduce to showing just one of the strict inequalities has density $1/2$. This is exactly the reduction Tao pointed out. ([Erdős Problems][3])

## What remains open

Even after removing the equality case (density $0$), the main conjecture
[
\text{dens}{n:\ d_{n+1}>d_n}=\text{dens}{n:\ d_{n+1}<d_n}=\tfrac12
]
is still open. ([Erdős Problems][1])

And the claim “infinitely many $n$ with (d_{n+1}=d_n)” is also open (despite being compatible with density $0$); it would follow from sufficiently strong prime-tuple heuristics, but no unconditional proof is known. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/218 "
  
    Erdős Problem #218
  
"
[2]: https://arxiv.org/abs/1504.06860 "[1504.06860] On a conjecture of ErdŐs, Pólya and Turán on consecutive gaps between primes"
[3]: https://www.erdosproblems.com/forum/thread/218 "

    Erdős Problem #218 - Discussion thread

"
[4]: https://www.ford126.web.illinois.edu/wwwpapers/chains.pdf "https://www.ford126.web.illinois.edu/wwwpapers/chains.pdf"
