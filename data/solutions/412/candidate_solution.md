This is a known open problem.

A couple of basic observations first:

* For every (n>1) we have (\sigma(n)\ge 1+n), hence (\sigma(n)>n). So each forward orbit
  [
  n,\ \sigma(n),\ \sigma_2(n),\ \sigma_3(n),\dots
  ]
  is a **strictly increasing** infinite sequence.
* Therefore, if (\sigma_i(m)=\sigma_j(n)) ever happens, then the two orbits **merge forever after** (all subsequent iterates are equal).

So your question is equivalent to: *do all orbits for (n\ge2) eventually coalesce into a single “tree” under the map (x\mapsto \sigma(x))?*

### Status

This is recorded as **Erdős Problem #412** (attributed by Erdős to van Wijngaarden) and is listed as **OPEN**: it “cannot be resolved with a finite computation.” ([Erdős Problems][1])

The same source notes that Selfridge reported numerical evidence suggesting the answer is **no**, and Erdős–Graham remarked that it seems unlikely anything could be proved “in the near future.” ([Erdős Problems][1])

### Evidence against the statement

Cohen and te Riele (1996) explicitly discuss this “all orbits meet” assertion as statement (vi) in their paper on iterating (\sigma). They report computational evidence that many initial values appear to fall into **different connected components** (“trees”) that do not intersect, at least up to very large bounds, and they list **21 distinct trees** detected among (2\le n\le 200), with minimal representatives
[
2,5,16,19,27,29,33,49,50,52,66,81,85,105,146,147,163,170,189,197,199.
]

They explicitly conjecture these trees remain distinct as the bound grows. 

The OEIS entry **A257348** collects (conjectural) minimal representatives of these components and emphasizes the current uncertainty: *even the trajectories of $2$ and $5$ are only conjectured to be disjoint.* ([OEIS][2])

### The “smallest” suspected counterexample

The simplest pair that would refute your statement, if one could prove it, is widely believed to be (m=2) and (n=5). Their iterates begin

* from $2$: (3,4,7,8,15,24,60,168,480,1512,4800,\dots)
* from $5$: (6,12,28,56,120,360,1170,3276,10192,\dots)

and extensive computations suggest they never meet, but **no proof is known** (and the OEIS explicitly flags this as conjectural). ([OEIS][2])

### Bottom line

As of the current literature, the statement

> “For every (m,n\ge2) there exist $i,j$ with (\sigma_i(m)=\sigma_j(n))”

is **open**, and the prevailing computational/heuristic evidence suggests it is **false**. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/412 "
  
    Erdős Problem #412
  
"
[2]: https://oeis.org/A257348 "A257348 - OEIS"
