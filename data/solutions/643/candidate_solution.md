Write $g(n,t)$ for the **maximum** number of edges in a $t$-uniform hypergraph on $[n]$ that avoids your configuration [[nomath]](i.e. contains **no** four *distinct* edges $A,B,C,D$ with
$A\cup B=C\cup D$ and $A\cap B=C\cap D=\varnothing$)[[/nomath]].
Then your threshold satisfies
[
f(n;t)=g(n,t)+1.
]
This forbidden configuration is standard in the literature under the name **generalized 4‑cycle** [[nomath]](often denoted $C_4^t$ or $C_4^r$)[[/nomath]]. ([Opikhurko][1])

## What is known for fixed (t\ge 3)

### General growth rate

For every fixed (t\ge 3),
[
g(n,t)=\Theta!\big(\tbinom{n}{t-1}\big)\qquad\text{and hence}\qquad
f(n;t)=\Theta!\big(\tbinom{n}{t-1}\big).
]
So the right “scale” is indeed (\binom{n}{t-1}), unlike $t=2$ (graphs), where one gets the (C_4) extremal behavior (\sim \tfrac12 n^{3/2}). ([Opikhurko][1])

### Best general lower bound (Füredi)

Füredi proved the lower bound
[
g(n,t)\ge\binom{n-1}{t-1}+\Big\lfloor\frac{n-1}{t}\Big\rfloor,
]
coming from the construction “all $t$-sets containing a fixed vertex” (a full star) plus a maximum matching of pairwise disjoint $t$-sets on the remaining $n-1$ vertices. ([Opikhurko][1])

Consequently,
[
f(n;t)\ge\binom{n-1}{t-1}+\Big\lfloor\frac{n-1}{t}\Big\rfloor+1.
]

For $t=3$, Füredi also noted a sharper *infinite family* of lower bounds using Steiner $S(2,5,n)$ systems: for infinitely many (n\equiv 1,5\pmod{20}) there are (C_4^3)-free 3‑graphs with exactly (\binom{n}{2}) edges. ([Opikhurko][1])

### Best general upper bounds (Pikhurko–Verstraëte 2009)

Let
[
\phi_t:=\limsup_{n\to\infty}\frac{g(n,t)}{\binom{n}{t-1}}.
]
Pikhurko–Verstraëte proved
[
1\le \phi_t \le \min!\left(\frac74,;1+\frac{2}{\sqrt t}\right)\qquad\text{for all }t\ge 3.
]
([Opikhurko][1])

In particular, for each fixed (t\ge 3),
[
g(n,t)\le \left(\min!\left(\frac74,;1+\frac{2}{\sqrt t}\right)+o(1)\right)\binom{n}{t-1},
]
and hence the same bound (plus 1) holds for $f(n;t)$.

They also obtained a **uniform** [[nomath]](all $n$)[[/nomath]] improvement in the $t=3$ case:
[
g(n,3)\le \frac{13}{9}\binom{n}{2}\quad\text{for every }n,
]
so
[
f(n;3)\le \frac{13}{9}\binom{n}{2}+1.
]
([Opikhurko][1])

## Is (f(n;t)=(1+o(1))\binom{n}{t-1}) true for fixed (t\ge 3)?

Equivalently, this asks whether (\phi_t=1) for each fixed (t\ge 3).

As of the most recent summaries I can find (including the Erdős Problems entry updated Oct 26, 2025), this is **still open** for every fixed (t\ge 3). ([Erdős Problems][2])

What *is* known is:

* The conjecture holds **in the limit (t\to\infty)** in the sense that the best known upper bound gives (\phi_t\le 1+2/\sqrt t), so (\phi_t\to 1) as (t\to\infty). ([Opikhurko][1])
* For $t=3$, (\phi_3) is known to exist (as a limit, not just limsup), but its value is unknown; current bounds are (1\le \phi_3\le 13/9). ([Opikhurko][1])
* For (t\ge 4), even the existence of the limit (\lim_{n\to\infty} g(n,t)/\binom{n}{t-1}) is (as far as currently documented) not known. ([Opikhurko][1])

## A compact “estimate” you can quote

Let $g(n,t)$ be the maximum $t$-uniform edge count avoiding your configuration. Then for fixed (t\ge 3),
[
\binom{n-1}{t-1}+\Big\lfloor\frac{n-1}{t}\Big\rfloor
\le
g(n,t)
\le
\left(\min!\left(\frac74,;1+\frac{2}{\sqrt t}\right)+o(1)\right)\binom{n}{t-1},
]
and (f(n;t)=g(n,t)+1). ([Opikhurko][1])

So the conjectured asymptotic (f(n;t)=(1+o(1))\binom{n}{t-1}) is **consistent with all known bounds**, is **true in the regime (t\to\infty)** [[nomath]](via upper bounds on $\phi_t$)[[/nomath]], but remains **unproved for each fixed (t\ge 3)**. ([Opikhurko][1])

[1]: https://opikhurko.warwick.ac.uk/E/PikhurkoVerstraete09jcta.pdf "The maximum size of hypergraphs without generalized 4-cycles"
[2]: https://www.erdosproblems.com/forum/thread/643 "

    Erdős Problem #643 - Discussion thread

"
