Interpreting “triangle” as **nondegenerate** [[nomath]](area $>0$)[[/nomath]]: for a set $P$ of $n$ points, let
[
M(P):=\max_{A>0}\ |\\{\text{triangles with vertices in }P\text{ and area }A\\}|,
]
and then
[
g(n)=\max_{|P|=n} M(P).
]

A standard scaling shows it suffices to consider **unit area** ((A=1)): scaling the plane by factor (\lambda) multiplies all triangle areas by (\lambda^2), so counting area $A$ triangles is equivalent to counting unit-area triangles after scaling. 
So $g(n)$ is exactly the extremal function in the classical **Oppenheim (1967) unit-area triangle problem**. 

## Best-known asymptotic bounds

### Lower bound

Erdős and Purdy constructed point sets (a suitable rectangular chunk of the integer lattice) that span
[
\Omega\big(n^2\log\log n\big)
]
triangles of the *same* area. 

[[nomath]](There is also an easier $\Omega(n^2)$ lower bound from configurations on three lines; in fact one can get $\Theta(n^2)$ unit-area triangles with points on any three given lines. )[[/nomath]]

### Upper bound

The best general upper bound currently known is
[
g(n)=O\big(n^{20/9}\big)=O\big(n^{2+2/9}\big),
]
proved by Raz and Sharir (improving earlier bounds). 

[[nomath]](For context: Erdős–Purdy had $O(n^{5/2})$, Pach–Sharir improved to $O(n^{7/3})$ via Szemerédi–Trotter, then further improvements led to $O(n^{20/9})$. )[[/nomath]]

## Summary estimate

Putting these together,
[
\boxed{\ \Omega\big(n^2\log\log n\big)\ \le\ g(n)\ \le\ O\big(n^{20/9}\big)\ }.
]

In particular, $g(n)$ is known to be **just above quadratic** but is not known to be (\Theta(n^2)); closing the gap between (n^2\log\log n) and (n^{20/9}) remains open. 

---

*Side note:* If degenerate “triangles” of area $0$ were allowed, then $n$ collinear points would give (\binom{n}{3}) triangles of equal area, making the problem trivial. So the interesting interpretation is area (>0).
