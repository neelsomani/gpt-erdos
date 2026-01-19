No example is known, and the general question is still open.

It is conjectured (Erdős–Mollin–Walsh) that **there do not exist** three consecutive powerful (squareful) integers. 

What can be proved easily is that any hypothetical triple $(n,n+1,n+2)$ would have to satisfy strong congruence constraints:

1. **The triple must be odd–even–odd.**
   If $n$ were even, then $n$ and $n+2$ would both be even. But an even powerful number must be divisible by $4$, so (4\mid n) and (4\mid (n+2)), implying (4\mid((n+2)-n)=2), impossible. Hence $n$ is odd and $n+1$ is even [[nomath]](indeed $4\mid(n+1)$)[[/nomath]].

2. **In fact, (n \equiv 7,27,) or (35 \pmod{36}).**
   Among three consecutive integers, exactly one is divisible by $3$. If a number is powerful and divisible by $3$, then it must be divisible by $9$.

* If (3\mid n), then (9\mid n) and (n\equiv 9) or (27\pmod{36}). But (n\equiv 9\pmod{36}) gives (n+1\equiv 10\pmod{4}), contradicting (4\mid(n+1)). So (n\equiv 27\pmod{36}).
* If (3\mid(n+1)), then (9\mid(n+1)) and also (4\mid(n+1)), hence (36\mid(n+1)), so (n\equiv 35\pmod{36}).
* If (3\mid(n+2)), then (9\mid(n+2)) and (n+2\equiv 9) or (27\pmod{36}), so (n\equiv 7) or (25\pmod{36}). But (n\equiv 25\pmod{36}) gives (n+1\equiv 26\pmod{4}), impossible. So (n\equiv 7\pmod{36}).

So any triple would have to start in one of those three residue classes (this is also noted in the literature). ([Rose-Hulman Scholar][1])

As for current progress: conditional on the **abc conjecture**, one can show there are only **finitely many** such triples, and there are several partial nonexistence results for special structured families (e.g. certain cube-centered triples).   Computations have also ruled out triples with small starting value; for example, the Erdős Problems database reports no such triple with smallest term (<10^{22}). ([Erdős Problems][2])

So the best current answer is: **no triple is known, and it remains an open problem whether any exist (with a widely believed conjecture that none do).** ([Erdős Problems][2])

[1]: https://scholar.rose-hulman.edu/rhumj/vol20/iss2/3/ "
\"On Consecutive Triples Of Powerful Numbers\" by Edward Beckon
"
[2]: https://www.erdosproblems.com/forum/thread/364 "

    Erdős Problem #364 - Discussion thread

"
