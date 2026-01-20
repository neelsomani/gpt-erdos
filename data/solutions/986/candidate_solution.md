Interpreting $R(k,n)$ as the usual **off‑diagonal graph Ramsey number** (r(k,n)=r(K_k,K_n)):

[
r(k,n)=\min{N:\ \text{every graph on }N\text{ vertices contains a }K_k\text{ or an independent set of size }n}.
]

Then the statement

[
r(k,n)\ \gg\ \frac{n^{k-1}}{(\log n)^{c}}
\quad\text{for some }c=c(k)>0
]

is **not known for all fixed (k\ge 3)**. It is exactly (a slightly reparameterized version of) an **Erdős conjecture** for off‑diagonal Ramsey numbers for (k\ge 4). 

## What is known

### $k=3$: true (sharp up to constants)

Kim (1995) (building on earlier work) showed that
[
r(3,n)=\Theta\left(\frac{n^2}{\log n}\right),
]
so your inequality holds with (c(3)=1) (and in fact the order of magnitude is known). 

### $k=4$: true (major recent breakthrough)

Mattheus and Verstraëte proved
[
r(4,n)=\Omega\left(\frac{n^3}{\log^4 n}\right),
]
so your inequality holds for $k=4$ with (c(4)=4). ([Annals of Mathematics][1])

[[nomath]](And the best known upper bound is $r(4,n)\le O(n^3/\log^2 n)$, so this pins $r(4,n)$ down to within polylog factors. )[[/nomath]]

## What remains open

### (k\ge 5): open (this is the conjecture)

For every fixed (k\ge 5), it is **unknown** whether one can achieve a lower bound of the form
[
r(k,n)\ \ge\ \frac{n^{k-1}}{(\log n)^{c(k)}}.
]
This is explicitly stated as Erdős’s conjecture [[nomath]](for $s=k\ge 4$)[[/nomath]] in recent surveys. 

## Best general bounds for fixed (k\ge 5) (what we *can* prove)

The best currently known lower bounds for fixed (k=s\ge 5) are substantially weaker than (n^{k-1}). A representative “state of the art” bound [[nomath]](coming from the $K_s$-free random process and related methods)[[/nomath]] is

[
r(s,n)\ \ge\ a(s)\frac{n^{(s+1)/2}}{(\log n)^{(s+1)/2 - 1/(s-2)}},
]
for some constant (a(s)>0), while the best known upper bound has the “conjectured” exponent $s-1$:
[
r(s,n)\ \le\ (1+o(1))\frac{n^{s-1}}{(\log n)^{s-2}}.
]


So for (s\ge 5) there is still a big gap between the known exponent $(s+1)/2$ and the conjectured exponent $s-1$.

## Summary

* The inequality you wrote is **proved for $k=3$** (indeed sharp) and **proved for $k=4$** [[nomath]](recently; with $c=4$)[[/nomath]]. 
* For **(k\ge 5)** it is **currently an open problem / conjecture of Erdős**. 
* The best general lower bounds for (k\ge 5) are of order (n^{(k+1)/2}) up to polylog factors, not (n^{k-1}). 

If you tell me whether you want $i$ a proof sketch for the known cases $k=3$ or $k=4$, or (ii) a derivation of the best-known general lower bound for fixed $k$, I can write that out carefully.

[1]: https://annals.math.princeton.edu/2024/199-2/p08?utm_source=chatgpt.com "The asymptotics of r(4,t) - Annals of Mathematics"
