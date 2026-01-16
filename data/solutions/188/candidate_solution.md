Interpret the “$k$-term arithmetic progression with distance $1$” as a *unit-step collinear progression*
[
x,x+u,x+2u,\dots,x+(k-1)u
\quad\text{with }|u|=1,
]
often denoted (\ell_k) in Euclidean Ramsey theory.

The exact **smallest $k$** for which such a red/blue colouring of (\mathbb{R}^2) exists is **not known** (it’s an open problem). ([Erdős Problems][1])

What is known (best current bounds):

* **Lower bound (k\ge 6):** Tsaturian (2017) proved that *every* red/blue colouring of the plane with **no red pair at distance $1$** must contain a **blue (\ell_5)** (five collinear blue points with consecutive spacing $1$). Therefore you cannot avoid blue unit-step progressions of length $5$, so the smallest “avoidable length” must satisfy (k\ge 6). 

* **Upper bound (k\le 10^{10}):** Conlon–Fox constructed colourings (in fact periodic ones) showing that for (n)-dimensional Euclidean space one can avoid a red (\ell_2) and also avoid a blue (\ell_m) for (m=10^{5n}). Taking (n=2) gives an explicit colouring of (\mathbb{R}^2) with **no red unit-distance pair** and **no blue (\ell_{10^{10}})**, so (k\le 10^{10}). 

So, at present,
[
\boxed{6 \le k \le 10^{10}.}
]

[[nomath]](For historical context: Erdős and Graham mentioned an upper bound of “$10{,}000{,}000$, more or less,” but without a published proof; the $10^{10}$ bound above is a rigorous one coming from Conlon–Fox.)[[/nomath]]

[1]: https://www.erdosproblems.com/188 "
  
    Erdős Problem #188
  
"
