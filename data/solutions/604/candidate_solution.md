This is the **(discrete) pinned distance problem** (Erdős problem #604), and the bounds you ask for are **not known** in general.

If we write
[
d(x):=|\\{|x-y|:y\in A\\}|,\qquad \widehat D(n):=\min_{|A|=n}\max_{x\in A} d(x),
]
then your question is whether (\widehat D(n)\gg n^{1-o(1)}), or even (\widehat D(n)\gg n/\sqrt{\log n}).

### Upper bound [[nomath]](why $n/\sqrt{\log n}$ would be best possible)[[/nomath]]

A (\sqrt n\times \sqrt n) integer grid has only (\Theta(n/\sqrt{\log n})) distinct distances (by the Landau–Ramanujan theorem on sums of two squares), so certainly
[
\widehat D(n)\le O(n/\sqrt{\log n}).
]
This is the standard “best possible” obstruction. 

### Best known general lower bound [[nomath]](far from $n^{1-o(1)}$)[[/nomath]]

The problem is open, and the best current general lower bound is **polynomial with exponent (\approx 0.8641)**:
[
\widehat D(n)\ \ge\ n^{,c-o(1)},\qquad c=\frac{48-14e}{55-16e}=0.864137\ldots,
]
due to **Katz–Tardos (2004)** [[nomath]](in the form “for every $\varepsilon>0$, $\widehat D(n)\gg_\varepsilon n^{c-\varepsilon}$”)[[/nomath]]. ([Erdős Problems][1])

Earlier milestones include **Solymosi–Tóth (2001)**, who proved that every $n$-point planar set has a point $x$ with
[
d(x)\ge \Omega(n^{6/7}).
]
([Math at UBC][2])

### Status of the bounds you propose

* The near-linear bound (\widehat D(n)\gg n^{1-o(1)}) is **open**. ([Erdős Problems][1])
* The sharper conjectural scale (\widehat D(n)\gg n/\sqrt{\log n}) is also **open** (and would be essentially optimal because of the grid example). ([Erdős Problems][1])

Erdős also conjectured a stronger *average* pinned statement, e.g.
[
\sum_{x\in A} d(x)\ \gg\ \frac{n^2}{\sqrt{\log n}},
]
which would imply that many points see many distinct distances. ([Erdős Problems][1])

So at present the landscape is:
[
n^{0.864\ldots - o(1)} \ \lesssim\ \widehat D(n)\ \lesssim\ n/\sqrt{\log n},
]
and closing this gap [[nomath]](even to $n^{1-o(1)}$)[[/nomath]] remains a major open problem. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/604 "
  
    Erdős Problem #604
  
"
[2]: https://www.math.ubc.ca/~solymosi/sajatcikkek/distcsabconf.pdf "paper2_1.dvi"
