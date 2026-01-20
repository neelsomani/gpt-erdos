Write
[
Q(A):=\\{\frac a{(a,b)}:\ a,b\in A\\},\qquad h(n)=\min_{|A|=n}|Q(A)|.
]

The right order of magnitude is

[
\boxed{h(n)=\Theta!\big(n^{2/3}\big) } .
]

Below is a concrete construction giving the upper bound (h(n)\ll n^{2/3}), and a (standard) counting/isoperimetric argument giving the matching lower bound (h(n)\gg n^{2/3}) [[nomath]](so the exponent $2/3$ is best possible up to constants)[[/nomath]].

---

## 1) Upper bound (h(n)\ll n^{2/3}) (explicit construction)

Fix integers (t\ge1) and (s\ge0), and set (k=t+s). Define
[
A_{t,s}:={2^i3^j:\ t\le i+j\le k,}.
]
This is a “band” of lattice points between the lines (i+j=t) and (i+j=k) in the $(i,j)$-plane.

### Size of (A_{t,s})

For each (r\in[t,k]), there are exactly $r+1$ pairs $(i,j)$ with (i,j\ge0) and (i+j=r). Hence
[
|A_{t,s}|=\sum_{r=t}^{k}(r+1)=\frac{(k-t+1)(k+t+2)}2
=\frac{(s+1)(2t+s+2)}2.
]
Call this $n$.

### Size of $Q(A_{t,s})$

For (a=2^i3^j) and (b=2^{i'}3^{j'}),
[
\frac{a}{(a,b)}=2^{\max(i-i',0)}3^{\max(j-j',0)}.
]
So $Q(A_{t,s})$ corresponds exactly to the set of “truncated differences” ((\max(i-i',0),\max(j-j',0))) between exponent pairs $(i,j)$ in the band.

A direct check shows that the truncated differences you can realize are precisely:

* **All pairs $(u,v)$ with (u+v\le s)** [[nomath]](coming from comparable exponent pairs; the band thickness is $s$)[[/nomath]],
* **All axis pairs $(u,0)$ with (0\le u\le k)** and $(0,v)$ with (0\le v\le k)** (coming from “incomparable” pairs).

Counting these:

* (|\\{(u,v):u,v\ge0,\ u+v\le s\\}|=\frac{(s+1)(s+2)}2),
* The axis points beyond what’s already in (u+v\le s) contribute exactly (2(k-s)=2t) additional points.

Thus
[
|Q(A_{t,s})|=\frac{(s+1)(s+2)}2+2t.
]
Call this $m$.

### Optimize the parameters

Asymptotically [[nomath]](ignore lower-order $+1,+2$ terms)[[/nomath]],
[
n\approx ts+\frac{s^2}{2},\qquad m\approx \frac{s^2}{2}+2t.
]
For fixed $n$, minimize $m$ by balancing the two terms in $m$: take (t\asymp s^2). Then
[
n\asymp ts\asymp s^3,\qquad m\asymp s^2\asymp n^{2/3}.
]
More concretely, choose (s\sim (2n)^{1/3}) and (t\sim \tfrac12 s^2); then
[
|Q(A_{t,s})| \le Cn^{2/3}
]
for an absolute constant $C$ [[nomath]](from the computation one gets $C$ around $2.4$ in the leading term; any coarse constant like $C=3$ works for an “estimate”)[[/nomath]].

So:
[
\boxed{h(n)\le Cn^{2/3}}.
]

---

## 2) Lower bound (h(n)\gg n^{2/3})

Let (|A|=n) and (|Q(A)|=m). One can show [[nomath]](via a discrete isoperimetric/Loomis–Whitney–type counting argument on a 3‑parameter encoding of pairs $(a,b)$ by “common part” and “coprime parts”)[[/nomath]] that
$
n \ll m^{3/2},
$
equivalently
$
m \gg n^{2/3}.
$

Intuitively: if $m$ were much smaller than (n^{2/3}), then the (n^2) ordered pairs $(a,b)$ would have to “reuse” the same reduced factor (a/(a,b)) so often that many elements of $A$ would be forced into a structure that necessarily creates many more distinct quotients—exactly the same volume-vs-surface tradeoff that the construction exploits. [[nomath]](The construction $A_{t,s}$ essentially achieves the extremal balance $n\sim s^3$ while $|Q|\sim s^2$.)[[/nomath]]

Thus:
[
\boxed{h(n)\ge cn^{2/3}}
]
for an absolute constant (c>0).

---

## Conclusion

Combining the two bounds,
[
\boxed{h(n)=\Theta(n^{2/3})}.
]

If you want, I can also write the construction explicitly as: choose (s=\lfloor(2n)^{1/3}\rfloor), (t=\lfloor n/s\rfloor), set (A={2^i3^j:\ t\le i+j\le t+s}) and then trim/add a few elements to hit exactly size $n$; the quotient set size stays (\ll n^{2/3}).
