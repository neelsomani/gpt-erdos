Write the equation as
$
\frac1a=\frac1b+\frac1c=\frac{b+c}{bc}
\qquad\Longleftrightarrow\qquad
a(b+c)=bc
\qquad\Longleftrightarrow\qquad
(b-a)(c-a)=a^2.
$
In particular, in any solution with positive integers we automatically have (a<b) and (a<c) [[nomath]](since $\tfrac1a>\tfrac1b$ and $\tfrac1a>\tfrac1c$)[[/nomath]], so $a$ is the *smallest* of the triple.

## A very useful easy lemma: any solution in $[N]$ has (a\le N/2)

If (1\le a<b,c\le N) solve ((b-a)(c-a)=a^2), then
$
b-a\le N-a,\qquad c-a\le N-a
$
so
$
a^2=(b-a)(c-a)\le (N-a)^2 ;\Longrightarrow; a\le N-a ;\Longrightarrow; a\le \frac N2.
$
This already gives the classical lower bound
$
f(N)\ge (|(\\{(\lfloor\frac N2)\rfloor+1,\dots,N)\\})|\sim \frac N2,
$
since any solution would need its smallest element (a\le N/2), which that “top half” set omits.

## But $f(N)$ is definitely **larger** than $N/2$: a $5N/8$ construction

Consider
$
A={,\text{odd } n\le N/4,}\ \cup\ [N/2,N]\cap \mathbb Z.
$
Then (|A|=\frac N2+\frac N8+o(N)=\bigl(\frac58+o(1)\bigr)N).

Why is $A$ solution-free? Suppose (for contradiction) that distinct (a,b,c\in A) satisfy (\frac1a=\frac1b+\frac1c).

* By the lemma above, (a\le N/2). But $A$ contains no integers in $(N/4,N/2)$, so actually (a\in A\cap[1,N/4]), hence $a$ is **odd**.
* If one of $b,c$ also lies in the “odd (\le N/4)” part, say (b\le N/4) is odd, then from
  $
  \frac1c=\frac1a-\frac1b=\frac{b-a}{ab}
  $
  we see $ab$ is odd while $b-a$ is even, so (\frac{b-a}{ab}) cannot be of the form $1/c$ with integer $c$ [[nomath]](equivalently $c=\frac{ab}{b-a}$ would require an even divisor of an odd number)[[/nomath]]. Contradiction.
  So $b$ and $c$ cannot involve that small odd part at all.
* Therefore $b,c\in[N/2,N]$. Since (b\ne c), we have
  $
  \frac1b+\frac1c \le \frac{1}{N/2}+\frac{1}{N/2+1}<\frac4N,
  $
  hence (\frac1a<\frac4N), i.e. (a>\frac N4), contradicting (a\le N/4).

So $A$ contains no solutions, and therefore
$
f(N)\ge (\frac58+o(1))N.
$
This observation (attributed on the Erdős problems site to Stijn Cambie) is recorded there, along with the open nature of the problem. ([Erdős Problems][1])

**Conclusion:** the answer to your “in particular” is **no**: $f(N)$ is not ((\tfrac12+o(1))N); it is at least ((\tfrac58+o(1))N). ([Erdős Problems][1])

## Best published/recorded upper bounds (as of what I can verify)

The same Erdős problems entry records an upper bound of Wouter van Doorn:
$
f(N)\le (\frac{9}{10}+o(1))N.
$
([Erdős Problems][1])

So the current state (as recorded there) is
$
(\frac58+o(1))N \ \le\ f(N)\ \le\ (\frac9{10}+o(1))N,
$
and narrowing this gap is open. ([Erdős Problems][1])

## Numerical evidence

Exact values for $f(N)$ for (N\le 731) are tabulated in OEIS A390395. ([OEIS][2])
For example, that table includes (among many others):

* (f(100)=86),
* (f(200)=167),
* (f(500)=415),
* (f(731)=606). ([OEIS][3])

These ratios (e.g. (606/731\approx 0.829)) sit comfortably between the proven $0.625$ and $0.9$ bounds, but they don’t yet make a clear conjectural constant obvious. ([OEIS][3])

---

If you’d like, I can also rewrite the whole problem in the standard “optic equation” parametrization
$
(a,b,c)=(kmn,km(m+n),kn(m+n))
$
[[nomath]](with $\gcd(m,n)=1$)[[/nomath]],
which is often a good starting point for both constructions and upper bounds—but the main point for your question is already clear: **density $1/2$ is not the right scale**; we know (f(N)\ge 5N/8-o(N)).

[1]: https://www.erdosproblems.com/search/Cambie "https://www.erdosproblems.com/search/Cambie"
[2]: https://oeis.org/A390395 "https://oeis.org/A390395"
[3]: https://oeis.org/A390395/b390395.txt "oeis.org"
