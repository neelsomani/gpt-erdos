This is **open**.

It is an Erdős question (Erdős Problem #1073): if $A(x)$ counts the **composite** (u<x) for which (u\mid(n!+1)) for some $n$, Erdős asked whether
[
A(x)\le x^{o(1)}\qquad(\text{equivalently }A(x)=o(x^\varepsilon)\text{ for every }\varepsilon>0).
]
It appears as Problem **F*** in Hardy–Subbarao (2002), and is recorded in the ErdosProblems database; the corresponding integers begin (25,121,169,437,\dots) and form OEIS **A256519**. ([Erdős Problems][1])

A couple of basic observations (easy but useful):

* If (u\mid(n!+1)), then (\gcd(u,n!)=1). In particular **every prime factor** (p\mid u) satisfies (p>n) [[nomath]](since if $p\le n$ then $p\mid n!$ so $n!+1\not\equiv 0\pmod p$)[[/nomath]].
* Hence (n< P^-(u)), the least prime factor of $u$. If $u$ is composite then (P^-(u)\le \sqrt u), so necessarily (n<\sqrt u\le \sqrt x).

None of this comes close to proving (A(x)\le x^{o(1)}), and as far as I can tell there is **no known proof or disproof** of that subpolynomial bound in the literature linked from the original source/problem pages. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/forum/thread/1073 "https://www.erdosproblems.com/forum/thread/1073"
