Not known in (\mathbb N). This is a well-known open problem (often called **Hindman’s conjecture**, and listed as **Erdős problem #172**).

To spell it out: your statement is equivalent to saying that for every $r$-colouring (\chi:\mathbb N\to[r]) and every (n\ge 2), there exist distinct (x_1,\dots,x_n\in\mathbb N) such that **all** numbers
[
\sum_{i\in S} x_i \quad\text{and}\quad \prod_{i\in S} x_i
]
(for every nonempty subset (S\subseteq [n])) have the same colour. This is explicitly stated as Conjecture 1.1 in Alweiss’s paper, and is described there as “one of the most important and longstanding conjectures” in this area; even the “simplest special case” (n=2) (i.e. finding ({x,y,x+y,xy}) monochromatic) is still open for arbitrary finite colourings of (\mathbb N). ([arXiv][1])

What *is* known (some context):

* If you ask for an **infinite** $A$, the analogous statement is **false**: Hindman constructed a finite colouring (7 colours) that avoids an infinite set with the simultaneous sums-and-products property. ([Erdős Problems][2])

* There is strong **partial progress** over (\mathbb N): Moreira proved that for any finite colouring of (\mathbb N), one can always find $x,y$ such that $\\{x,\ x+y,\ xy\\}$ is monochromatic (note $y$ itself is not required to be that colour). ([Annals of Mathematics][3])

* In **2-colourings** of (\mathbb N), the (n=2) pattern $\\{x,y,x+y,xy\\}$ *does* always occur, and in fact occurs infinitely often; this was proved (without brute-force computation) by Bowen. 

* Over the **rationals** (\mathbb Q), the full “arbitrarily large finite $A$” statement is now **true**: Alweiss proved that for every finite colouring of (\mathbb Q) and every $n$, one can find (x_1,\dots,x_n) with all subset sums and subset products monochromatic. ([arXiv][1])

So the honest answer to your exact question for (\mathbb N): **it’s an open problem**. ([Erdős Problems][2])

[1]: https://arxiv.org/pdf/2307.08901 "arXiv:2307.08901v5  [math.CO]  17 Nov 2023"
[2]: https://www.erdosproblems.com/favourites/zach_hunter "
    Erdős Problem Favourites
"
[3]: https://annals.math.princeton.edu/wp-content/uploads/annals-v185-n3-p10-p.pdf "Monochromatic sums and products in N"
