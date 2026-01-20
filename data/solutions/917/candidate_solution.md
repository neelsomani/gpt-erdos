This is an old question of Dirac/Erdős (it is Erdős problem #917) and is still open in general. The short answers are:

* **Yes**: for every fixed (k\ge 4) one has (f_k(n)\gg_k n^2) (Toft, 1970). ([Erdős Problems][1])
* **Open**: even the case $k=6$ is not settled; in particular (f_6(n)\sim n^2/4) is not known. 
* **No in general**: the proposed asymptotic (\frac12\bigl(1-\frac1{\lfloor k/3\rfloor}\bigr)n^2) is **false for (k\equiv 1,2\pmod 3)** by constructions of Stiebitz. ([Erdős Problems][1])
  For (k\equiv 0\pmod 3) [[nomath]](including $k=6$)[[/nomath]], the corresponding Erdős conjecture remains open. ([Erdős Problems][1])

---

## 1) Is (f_k(n)\gg_k n^2) for (k\ge 4)?

**Yes.** Toft proved that for every (k\ge 4) there is a constant (c_k>0) with
[
f_k(n)\ge c_k n^2
]
[[nomath]](for all sufficiently large $n$, and in fact in Toft’s result essentially for all $n$ apart from a small exception)[[/nomath]]. ([Erdős Problems][1])

So (f_k(n)) really is quadratic for every fixed (k\ge4).

---

## 2) Is (f_6(n)\sim n^2/4)?

This is **open**.

What is known is that Dirac constructed a 6-chromatic critical graph on $4n+2$ vertices with
[
f_6(4n+2)\ge 4n^2+8n+3,
]
by taking two disjoint copies of (C_{2n+1}) and adding all edges between them. 
Since $4n+2$ is the number of vertices, this gives
[
f_6(N)\ \ge\ \frac14N^2 + O(N)\qquad\text{for infinitely many }N.
]

Erdős explicitly conjectured that the “$1/4$” should be the right asymptotic constant for $k=6$, but already in 1969 noted he could not prove (f_6(n)=(\tfrac14+o(1))n^2). 

### Best general upper bounds (as of what’s recorded in the literature referenced on the problem page)

Stiebitz proved for large $n$ the general upper bound
[
f_k(n) < \mathrm{ex}(n;K_{k-1}) \sim \frac12\\(1-\frac1{k-2}\\)n^2,
]
so for $k=6$,
[
f_6(n)\ \lesssim\ \frac38,n^2.
]
([Erdős Problems][1])

More recently Luo–Ma–Yang (2023) improved this slightly to
[
f_k(n) \le \frac12\\(1-\frac1{k-2}-\frac{1}{36(k-1)^2}+o(1)\\)n^2,
]
so for $k=6$,
[
f_6(n)\ \le\ \\(\frac{337}{900}+o(1)\\)n^2 \approx 0.37444,n^2.
]
([Erdős Problems][1])

So currently the known asymptotic window for $k=6$ is roughly
[
0.25,n^2 \ \lesssim\ f_6(n)\ \lesssim\ 0.3745,n^2,
]
and closing that gap (or even proving the limit exists) is open. ([Erdős Problems][1])

---

## 3) For (k\ge 6), is

[
f_k(n)\sim \frac12\\(1-\frac{1}{\lfloor k/3\rfloor}\\)n^2\ ?
]

### This asymptotic is *not* true in general

Erdős conjectured precisely this “(\lfloor k/3\rfloor)” asymptotic [[nomath]](phrased as a common limit for $k=3r,3r+1,3r+2$)[[/nomath]]. 
However, Stiebitz constructed denser critical graphs showing that for every (k\ge6) there are infinitely many $n$ with
[
f_k(n)\ \ge\ \frac12\\(1-\frac{1}{\lfloor k/3\rfloor+\delta_k}\\)n^2,
]
where (\delta_k=1/7) for (k\equiv1\pmod3) and (\delta_k=24/69=8/23) for (k\equiv2\pmod3). ([Erdős Problems][1])

Because (\delta_k>0) in those two residue classes, this lower bound is **strictly larger** than (\frac12(1-\frac1{\lfloor k/3\rfloor})n^2) for those $k$, so the proposed asymptotic is **disproved for (k\not\equiv 0\pmod3)**. ([Erdős Problems][1])

Concrete examples from that bound:

* $k=7$ ((\lfloor k/3\rfloor=2), (\delta_k=1/7)): infinitely often
  [
  f_7(n)\ge \frac12\\(1-\frac{1}{2+1/7}\\)n^2=\frac{4}{15}n^2\approx 0.2667,n^2>0.25,n^2.
  ]
* $k=8$ ((\lfloor k/3\rfloor=2), (\delta_k=8/23)): infinitely often
  [
  f_8(n)\ge \frac12\\(1-\frac{1}{2+8/23}\\)n^2=\frac{31}{108}n^2\approx 0.2870,n^2>0.25,n^2.
  ]

### What about (k\equiv 0\pmod 3)?

For $k=3r$, Dirac’s “join of $r$ odd cycles” type construction gives infinitely many $n$ with
[
f_k(n)\ge \frac12\\(1-\frac1r\\)n^2+O(n),
]
matching the constant (\frac12(1-\frac1{\lfloor k/3\rfloor})) [[nomath]](since $\lfloor k/3\rfloor=r$)[[/nomath]]. ([Erdős Problems][1])
But **no matching upper bound is known**, and (as noted on the problem page) even the existence of (\lim_{n\to\infty} f_k(n)/n^2) is open. ([Erdős Problems][1])

---

If you want, I can also sketch (at a high level) why the “join of odd cycles” construction is edge-critical and gives the (\frac12(1-1/r)) density for $k=3r$; that’s the cleanest way to see where Erdős’s original guess came from.

[1]: https://www.erdosproblems.com/917 "
  
    Erdős Problem #917
  
"
