Let
[
M(n):=\max_{|A|=n}\bigl(f(d_1)-f(d_2)\bigr).
]

### Upper bound

Trivially,
[
f(d_1)-f(d_2)\le f(d_1).
]
After scaling the plane so that (d_1=1), $f(d_1)$ becomes the number of **unit distances** in $A$. Thus (f(d_1)\le U(n)), where $U(n)$ is the maximum number of unit-distance pairs among $n$ planar points. The best known general upper bound is
[
U(n)=O!\left(n^{4/3}\right)
]
(Spencer–Szemerédi–Trotter). Hence
[
M(n)=O!\left(n^{4/3}\right). \tag{1}
]
(Quoted, for example, in Clemen–Dumitrescu–Liu’s 2025 paper.) ([arXiv][1])

### Lower bound

A recent result of Clemen, Dumitrescu, and Liu (2025) gives a **superlinear** lower bound on the possible gap between the largest and second-largest distance multiplicities: they construct $n$-point sets with
[
f(d_1)-f(d_2)=\Omega(n\log n),
]
so in particular
[
M(n)=\Omega(n\log n). \tag{2}
]
([arXiv][1])

[[nomath]](They prove a more general statement: for $1\le r\le \log n$, one can achieve $f(d_r)-f(d_{r+1})=\Omega\bigl(\frac{n\log n}{r}\bigr)$.)[[/nomath]] ([Erdős Problems][2])

### Best current “estimate”

Putting $1$ and $2$ together, the best currently available bounds are
[
\boxed{\ \Omega(n\log n)\ \le\ M(n)\ \le\ O\left(n^{4/3}\right)\ }.
]

It is open where the truth lies between these; Clemen–Dumitrescu–Liu explicitly ask whether one can improve the lower bound to something like (n^{1+c/\log\log n}) for some (c>0). ([arXiv][1])

[1]: https://www.arxiv.org/pdf/2505.04283v1 "On the mutiplicities of interpoint distances"
[2]: https://www.erdosproblems.com/latex/959 "
  
    Erdős Problems
  
"
