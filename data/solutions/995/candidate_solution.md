Write
[
S_N(\alpha):=\sum_{k=1}^N f({\alpha n_k}),\qquad \mu:=\int_0^1 f(x),dx,\qquad g:=f-\mu.
]
Then
[
S_N(\alpha)=N\mu+\sum_{k=1}^N g({\alpha n_k}),
]
so the real issue is the *centered* sum (\sum_{k\le N} g({\alpha n_k})) [[nomath]](since $N\mu=o(N\sqrt{\log\log N})$ automatically)[[/nomath]].

## What happens for “nice” $f$ (BV/Lipschitz/trig polynomials)

If (n_{k+1}/n_k\ge q>1) (Hadamard lacunarity) and $g$ has some regularity (e.g. bounded variation, Lipschitz, etc.), then one has a genuine “probabilistic” behavior: there is an LIL-type upper bound
[
\limsup_{N\to\infty}\frac{\sum_{k=1}^N g({n_k\alpha})}{\sqrt{2N\log\log N}} ;<;\infty
\quad\text{for a.e. }\alpha,
]
and in many classical settings one even has a full LIL/CLT/invariance principle (the behavior resembles sums of independent variables). 

In particular, under such regularity,
[
S_N(\alpha)=N\mu+O\big(\sqrt{N\log\log N}\big)\quad\text{for a.e. }\alpha,
]
so your proposed bound (S_N(\alpha)=o\big(N\sqrt{\log\log N}\big)) holds (and is far from sharp).

## For general (f\in L^2): Erdős’ bounds and the open gap

If you assume only $f\in L^{[0,1]}$ [[nomath]](so $f$ may be unbounded and very rough)[[/nomath]], the situation changes drastically.

Erdős proved two complementary statements (already in 1949, reiterated in 1964):

### General upper bound [[nomath]](all lacunary sequences, all $L^2$ functions)[[/nomath]]

For every lacunary sequence ((n_k)) and every (f\in L^2), for every (\varepsilon>0),
[
\sum_{k=1}^N f({n_k\alpha}) = o\Big(N(\log N)^{\tfrac12+\varepsilon}\Big)
\quad\text{for a.e. }\alpha.
]


### Counterexample lower bound [[nomath]](some lacunary sequence, some $L^2$ function)[[/nomath]]

He also constructed a lacunary ((n_k)) and an (f\in L^2) [[nomath]](indeed $f\in L^p$ for every $p$)[[/nomath]] such that for every (\varepsilon>0),
[
\limsup_{N\to\infty}\frac{\sum_{k=1}^N f({n_k\alpha})}{N(\log\log N)^{\tfrac12-\varepsilon}}=\infty
\quad\text{for a.e. }\alpha,
]
so in general you **cannot** hope for (o!\big(N(\log\log N)^{1/2-\varepsilon}\big)). 

Erdős explicitly points out the “considerable gap” between these bounds and suggests the lower bound is closer to the truth. 

## So: is (S_N(\alpha)=o(N\sqrt{\log\log N})) a.e.?

With only (f\in L^2) and an arbitrary lacunary ((n_k)), this is **not settled** by the classical theory: it sits exactly in the gap between Erdős’ general upper bound (N(\log N)^{1/2+\varepsilon}) and his counterexample growth just below (N(\log\log N)^{1/2}). This is recorded as an Erdős open problem in the modern problem literature. ([Erdős Problems][1])

### Two easy remarks

* If (f\in L^\infty), then (|S_N(\alpha)|\le N|f|_\infty), so (S_N(\alpha)=o(N\sqrt{\log\log N})) holds trivially for all (\alpha). The difficulty is really about *unbounded* (L^2) functions.
* If $f$ has bounded variation/Lipschitz/etc., you get the much sharper (\sqrt{N\log\log N})-scale behavior discussed above.

If you tell me whether you want the statement for the *centered* sum (\sum_{k\le N}(f-\int f)({\alpha n_k})) (which is what Erdős formulates) or for (S_N) as written, I can restate the sharpest known bounds in exactly the normalization you prefer.

[1]: https://www.erdosproblems.com/search_bib/Er64b?sources_only=1 "
  
    Erdős Problems
  
"
