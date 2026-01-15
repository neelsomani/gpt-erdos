This limit is **not known**. It is a famous open problem of Erdős (even proving that the limit exists is open). ([Erdős Problems][1])

What we do know are bounds.

### Lower bound

A classic probabilistic argument of Erdős (later improved by Spencer) gives an exponential lower bound of the shape
[
R(k,k);\ge; (1+o(1))\cdot \text{(poly in }k)\cdot 2^{k/2}.
]
So after taking the (k)-th root, the polynomial factor disappears, and we get
[
\liminf_{k\to\infty} R(k,k)^{1/k};\ge; 2^{1/2}=\sqrt2.
]


### Upper bound

The classical Erdős–Szekeres bound implies (R(k,k)\le 4^k), hence
[
\limsup_{k\to\infty} R(k,k)^{1/k}\le 4.
]
More recently there was a breakthrough: Campos–Griffiths–Morris–Sahasrabudhe proved an exponential improvement (R(k,k)\le (4-\varepsilon)^k) for some (\varepsilon>0). ([arXiv][2])

This was then optimized further by Gupta–Ndiaye–Norin–Wei, who obtain in particular
[
R(k,k)\le (3.7992\ldots)^{k+o(k)},
]
so
[
\limsup_{k\to\infty} R(k,k)^{1/k}\le 3.7992\ldots
]


### What this means for your limit

Putting it together,
[
\sqrt2;\le;\liminf_{k\to\infty}R(k)^{1/k};\le;\limsup_{k\to\infty}R(k)^{1/k};\le;3.7992\ldots
]
and **the actual limit value is unknown**. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/77 "
  
    Erdős Problem #77
  
"
[2]: https://arxiv.org/pdf/2303.09521 "An exponential improvement for diagonal Ramsey"
