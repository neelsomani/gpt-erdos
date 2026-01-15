Let (A\subseteq\mathbb N) and list its elements in increasing order
[
A={a_1<a_2<a_3<\cdots}.
]
For each (k\ge 1) let (A_k={a_1,\dots,a_k}) and consider the finite set of multiples
[
M_{A_k}={n\ge 1:\ a_i\mid n\text{ for some }i\le k}.
]
Because (A_k) is finite, (M_{A_k}) is a finite union of arithmetic progressions, hence has a (natural) asymptotic density (d(M_{A_k})).

Now define the **sequential densities**
[
d_k := d(M_{A_k}).
]
Then ((d_k)) is nondecreasing in (k) (adding more divisors can only add more multiples), so the limit (\lim_{k\to\infty} d_k) exists in $[0,1]$.

A theorem of Davenport–Erdős says that for sets of multiples, this sequential limit equals the lower natural density (and also equals the logarithmic density) of (M_A). ([Wikipedia][1]) In particular, (M_A) has density $1$ exactly when this sequential limit is $1$.

### Necessary and sufficient condition

[
\boxed{\ \ d(M_A)=1\ \Longleftrightarrow\ \lim_{k\to\infty} d!\left(M_{{a_1,\dots,a_k}}\right)=1\ \ }
]
Equivalently (unpacking the limit),
[
\boxed{\ \ d(M_A)=1\ \Longleftrightarrow\ \forall \varepsilon>0\ \exists k\ \text{such that}\ d(M_{A_k})>1-\varepsilon.\ \ }
]

You can also phrase it without choosing an order:

[
\boxed{\ \ d(M_A)=1\ \Longleftrightarrow\ \forall \varepsilon>0\ \exists\text{ finite }F\subseteq A\ \text{with}\ d(M_F)>1-\varepsilon.\ \ }
]

[[nomath]](For a finite $F$, $d(M_F)$ is computable exactly because $M_F$ is periodic with period $\mathrm{lcm}(F)$.)[[/nomath]]

This property is exactly what’s called $A$ being a **Behrend sequence/set** in the literature. ([Wikipedia][2])

[1]: https://en.wikipedia.org/wiki/Davenport%E2%80%93Erd%C5%91s_theorem "Davenport–Erdős theorem - Wikipedia"
[2]: https://en.wikipedia.org/wiki/Behrend_sequence "Behrend sequence - Wikipedia"
