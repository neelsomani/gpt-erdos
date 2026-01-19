Write (g=\gcd(a,b)), $a=gx$, $b=gy$ with (\gcd(x,y)=1). Then
[
a+b=g(x+y),\qquad ab=g^2xy.
]
A key observation is that $\gcd(x+y,xy)=1$ when (\gcd(x,y)=1): if a prime (p\mid (x+y)) and (p\mid xy), then (p\mid x) or (p\mid y), hence also (p\mid y) or (p\mid x), contradicting (\gcd(x,y)=1).

From this one gets the clean criterion
[
a+b\mid m,ab \quad\Longleftrightarrow\quad x+y\mid m,g,
]
for $m=1$ (your first condition) and $m=2$ (your second condition).

Equivalently:

* (a+b\mid ab) iff (x+y\mid g).
* (a+b\mid 2ab) iff (x+y\mid 2g), i.e. iff (\dfrac{x+y}{\gcd(x+y,2)}\mid g).

This also yields a standard parametrization of *all* bad pairs:

* For $m=1$: choose coprime (x<y) and (t\ge1), and set
  [
  a=t,x(x+y),\qquad b=t,y(x+y).
  ]
  Then (a+b\mid ab). Conversely every bad pair arises this way. ([Mathematics Stack Exchange][1])
* For $m=2$: with (d=\gcd(x+y,2)\in{1,2}), choose coprime (x<y) and (t\ge1), and set
  [
  a=t,x\frac{x+y}{d},\qquad b=t,y\frac{x+y}{d}.
  ]
  Then (a+b\mid 2ab), and conversely every bad pair has this form. ([Mathematics Stack Exchange][1])

## 1) The (a+b\nmid ab) condition: can (|A|) beat the odds substantially?

Yes.

First, all odd numbers work (as you observed), because if $a,b$ are odd then $a+b$ is even while $ab$ is odd, so (a+b\nmid ab).

But you can do much better than (\sim N/2). In fact, in the classical $N=50$ instance (this is the Canadian Mathematical Olympiad 1996 #5), there is a set of size (38) with the property that (a+b\nmid ab) for all distinct (a,b\in A). One explicit example is
[
A=\\{1,2,\dots,50\\}\setminus\\{6,12,15,18,20,24,28,35,40,42,45,48\\},
]
so (|A|=38), which is far larger than the 25 odd numbers. ([Mathematics Stack Exchange][1])

Moreover, it is known that $38$ is *optimal* for $N=50$ (i.e. you cannot reach 39). ([Mathematics Stack Exchange][1])

For a sense of larger $N$ (computational, not a theorem): the exact maxima for the first condition are

* $N=100$: (|A|_{\max}=75),
* $N=200$: (|A|_{\max}=147),

so the best density stays around $0.73$–$0.75$ in these ranges [[nomath]](well above $1/2$)[[/nomath]].

## 2) The (a+b\nmid 2ab) condition: must (|A|=o(N))?

The same gcd-reduction gives the right way to think about it:
[
a+b\mid 2ab \iff x+y\mid 2g \iff \frac{x+y}{\gcd(x+y,2)}\mid g.
]
So bad pairs are still highly structured, but [[nomath]](unlike the $m=1$ case)[[/nomath]] **odd–odd pairs can now be bad**, because the extra factor of 2 removes the parity obstruction.

What can be said concretely:

* For $N=50$ there again exists a set of size (38) with no bad pair under the “(2ab)” condition. For instance
  [
  A={1,2,\dots,50}\setminus{6,10,12,14,15,16,18,20,24,28,42,45},
  ]
  has (|A|=38) and satisfies: for distinct (a,b\in A), (a+b\nmid 2ab).

* Exact optima for small $N$ (computational):

  * $N=100$: (|A|_{\max}=73),
  * $N=200$: (|A|_{\max}=142).

These finite-$N$ facts show that the “$2ab$” restriction is **not** so strong that it forces (|A|) to be small for moderate $N$. But they do **not** by themselves decide the asymptotic question “must (|A|/N\to0)?”.

I do not know a proof that (|A|=o(N)) must hold in the $2ab$ variant, and I also do not know a proof of a positive limiting density. What one *can* say from the parametrization is that the set of forbidden pairs up to $N$ is quite sparse and can be counted efficiently [[nomath]](it grows on the order of $N\log\log N$ in the $m=1$ case, and similarly for $m=2$ with a slightly larger constant)[[/nomath]], which is consistent with the existence of large independent sets, but it does not by itself settle whether the maximum density stays bounded away from 0.

So, in summary:

* For (a+b\nmid ab): **yes**, $A$ can be substantially larger than the odds; already for $N=50$ one can reach $38$ elements, and that is best possible. ([Mathematics Stack Exchange][1])
* For (a+b\nmid 2ab): there are also very large examples for small $N$ [[nomath]](e.g. $38$ out of $50$)[[/nomath]], so it is definitely *plausible* that (|A|) can be (\gg N), but I do not know a definitive asymptotic theorem that forces (|A|=o(N)) or rules it out.

If you want, I can also rewrite your question in “graph language” [[nomath]](vertices $1,\dots,N$, edges = forbidden pairs via the $\gcd$-criterion)[[/nomath]], because that viewpoint makes both variants look like maximum independent set problems with a very explicit parametrization of edges.

[1]: https://math.stackexchange.com/questions/3599791/ab-mid-ab-from-cmo-1996?utm_source=chatgpt.com "a+b∣ab from CMO 1996"
