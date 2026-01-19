As stated, this is **open in general** (it’s recorded as an Erdős–Szemerédi problem). ([Erdős Problems][1])

What *is* known (and is essentially the current “best general theorem”) is:

* Erdős and Szemerédi proved that for **every** infinite increasing (A\subseteq \mathbb N),
  [
  F(A,X,3)\ \ll\ X^{1/3}\log X,
  ]
  and they also exhibited an $A$ for which
  [
  F(A,X,3)\ \gg\ X^{1/3}\log X
  ]
  for infinitely many $X$. ([Erdős Problems][1])

In particular, for **any (k\ge 3)** one has the monotonicity implication
$
[a_i,\dots,a_{i+k-1}]<X \ \Longrightarrow\ [a_i,a_{i+1},a_{i+2}]<X,
$
so
$
F(A,X,k)\le F(A,X,3)\ll X^{1/3}\log X,
$
but **no general bound is known that forces the exponent below $1/3$** just by taking $k$ larger, let alone down to (X^\epsilon) for every (\epsilon>0). ([Erdős Problems][1])

So the short status summary is:

* For some specific $A$ [[nomath]](e.g. $A=\mathbb N$)[[/nomath]], the desired conclusion is true by taking $k$ large enough.
* But **uniformly for arbitrary $A$**, the statement “(\forall\epsilon>0,\exists k) with (F(A,X,k)<X^\epsilon)” is **not proved nor disproved** at present. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/873 "
  
    Erdős Problem #873
  
"
