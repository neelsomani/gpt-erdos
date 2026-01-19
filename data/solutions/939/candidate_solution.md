### For (r\ge 4): can a sum of $r-2$ coprime $r$-powerful numbers be $r$-powerful?

Yes — at least for some (r\ge 4), such identities exist.

A concrete example for $r=5$ (found by Stijn Cambie) is
[
3^{7}\cdot 61^{5}
=2^{8}\cdot 3^{10}\cdot 5^{7}+2^{12}\cdot 23^{6}+11^{5}\cdot 13^{5}.
]
Each summand on the right is $5$-powerful [[nomath]](all prime exponents $\ge 5$)[[/nomath]], and the left-hand side is also $5$-powerful. The three summands are *collectively* coprime [[nomath]](their gcd is $1$)[[/nomath]], though not pairwise coprime [[nomath]](the first two share a factor $2$)[[/nomath]]. ([Departement Computerwetenschappen][1])

It is also reported that Cambie found solutions for $r=7$ and $r=8$ [[nomath]](and even an $8$-powerful number expressed as a sum of $5$ $8$-powerful numbers)[[/nomath]]. ([Erdős Problems][2])

As for your finiteness question: the current status (as reflected in the sources above) is that it remains **open** whether this can happen for $r=4$, and also **open** whether there are **infinitely many** such solutions [[nomath]](even once existence is known for some $r$)[[/nomath]]. ([Departement Computerwetenschappen][1])

### For $r=3$: are there infinitely many coprime $3$-powerful triples $a,b,c$ with (a+b=c)?

Yes. Erdős’s conjecture here is known to be true: there are **infinitely many** solutions in *pairwise coprime* $3$-powerful (cube-full) integers $a,b,c$ with (a+b=c). This was proved by Nitaj, later strengthened/varied by Cohn [[nomath]](who produced infinitely many examples with none of $a,b,c$ being perfect cubes)[[/nomath]], and more recently rederived by Walsh via an elliptic-curve/Mordell–Weil approach. ([Erdős Problems][2])

A standard explicit example (already illustrating the phenomenon) is
[
2^{3}\cdot 3^{5}\cdot 73^{3} + 271^{3} = 919^{3},
]
where all three numbers are $3$-powerful and (\gcd(a,b)=1) (hence the triple is pairwise coprime). ([Erdős Problems][2])

If you tell me whether, in the (r\ge4) question, you meant **pairwise coprime** summands (stronger) or just **(\gcd=1)** for all summands together (the usual “primitive” condition in these sum problems), I can tailor the status summary accordingly; the known $r=5$ example above satisfies the latter but not the former.

[1]: https://wms.cs.kuleuven.be/cs/nieuws/nieuwsberichten/stijn-cambie-solves-open-erdos-problems "Stijn Cambie solves open Erdős-problems — Departement Computerwetenschappen"
[2]: https://www.erdosproblems.com/forum/discuss/939 "

    Erdős Problem #939 - Discussion thread

"
