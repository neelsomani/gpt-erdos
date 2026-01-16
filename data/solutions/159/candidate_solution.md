What you wrote is **exactly Erdős’s 1981 challenge**, and it is **still open**.

The best general bounds currently known are of the form
[
c_1,\frac{n^{3/2}}{\log n}\ \le\ R(C_4,K_n)\ \le\ c_2\Big(\frac{n}{\log n}\Big)^2,
]
for absolute constants (c_1,c_2>0). 

So we do have a **subquadratic saving by a (\log^2 n)** factor on the upper bound,
[
R(C_4,K_n)=O!\left(\frac{n^2}{\log^2 n}\right),
]
originally credited to an unpublished result of **Szemerédi** (and later written up by Caro–Li–Rousseau–Zhang), with a refined asymptotic form
[
R(C_4,K_n)\le (1+o(1))\Big(\frac{n}{\log n}\Big)^2
]
proved by **Liu–Li (2021)**. 

But **no one knows how to improve the exponent (2) by any fixed amount**:

> Erdős asked for a proof that (R(C_4,K_n) < n^{2-\varepsilon}) for some (\varepsilon>0); **to date, no such proof is known.** 

This is also stated explicitly in Erdős–Faudree–Rousseau–Schelp (1984): Erdős “strongly believes” such an (n^{2-\varepsilon}) bound, but it was already noted there that only a ((\log n)^{-2}) saving was known from Szemerédi’s observation. 

So, in short: **your statement (R(C_4,K_n)\ll n^{2-c}) is an open problem.**
