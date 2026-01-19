Write
[
D_k(n):=\lvert D_k\cap{1,\dots,n}\rvert.
]

A few basic structural facts (due to Erdős–Graham):

* $F(m)$ **exists for every composite** $m$, and in fact **every composite $m$ lies in (F_6)** [[nomath]](so $F(m)\le 6$ for composites)[[/nomath]].
* If $m$ is **prime**, then no such product can be a square [[nomath]](the prime $m$ occurs to exponent $1$ coming only from $m!$)[[/nomath]]. [[nomath]](This is implicit in their partition of “all integers excluding primes and squares” into $D_3,D_4,D_5,D_6$.)[[/nomath]]
* In particular, (D_k=\varnothing) for (k>6).

Below are the best unconditional growth statements I’m aware of for (3\le k\le 6), together with the main conjectures.

---

## $k=3$: (D_3(n)) is sublinear; conjecturally (\asymp \sqrt n)

### Unconditional lower bound: (D_3(n)\gg \sqrt n)

There is an explicit infinite family giving a square with three factorials. For (m=2t^2) [[nomath]](with $t\ge2$)[[/nomath]],
[
2!(m-1)!m! = 2(m-1)!^2\cdot m = 2(m-1)!^2\cdot 2t^2 = \bigl(2t(m-1)!\bigr)^2,
]
so (F(m)\le 3). Since $m$ is not a square, this forces (F(m)=3), hence (2t^2\in D_3). Thus
[
D_3(n)\ \ge\ |\\{t:2t^2\le n\\}|\ \asymp\ \sqrt n.
]

[[nomath]](Erdős–Graham give much more general constructions of this “$u\cdot t^2$” type.)[[/nomath]]

### Unconditional upper bounds: (D_3(n)=o(n)), and explicit “almost linear but $o(n)$” bounds

Erdős–Graham prove
[
D_3(n)=o(D_4(n)),
]
and since (D_4) has positive density, this implies (D_3(n)=o(n)).

A later improvement (Saradha–Shorey, as quoted in Dujella–Najman–Saradha–Shorey) gives an explicit quantitative bound of the form
[
D_3(x)=O\left(\frac{x\log^3 x}{\log x,\log_2 x}\right),
]
still $o(x)$ but far from (\sqrt x).

### Conjecture (Erdős–Graham): (D_3(n)\sim c\sqrt n)

They explicitly state they are “sure” that (D_3(x)\sim c\sqrt x) for some constant $c$, but cannot prove it.

**Summary for $k=3$:**
[
\sqrt n\ \ll\ D_3(n)\ =\ o(n),\qquad\text{conjecturally }D_3(n)\asymp \sqrt n.
]

---

## $k=4$: (D_4(n)) grows linearly ((\Theta(n)))

A key observation of Erdős–Graham is: **if $m$ has a nontrivial square factor** [[nomath]](i.e. $m$ is not squarefree)[[/nomath]], then (m\in F_4).

Since the non-squarefree integers have positive density [[nomath]](indeed density $1-\frac6{\pi^2}$)[[/nomath]], and the sets (D_2) (squares) and (D_3) are $o(n)$, it follows that (D_4(n)) is **linear in $n$**:
[
D_4(n)\ \gg\ n.
]
In particular (D_4) has positive lower density.

Erdős–Graham also remark that squarefree members of (F_4) seem “relatively rare” and that it is likely “almost all squarefree integers do not belong to (F_4),” but that stronger statement is not proved.

**Summary for $k=4$:**
[
D_4(n)=\Theta(n)\quad\text{(positive density).}
]

---

## $k=5$: known to be infinite; at least (\gg n/\log n); linear growth is not settled in the classical sources

Erdős–Graham prove that if $m$ has a proper divisor in $\\{2,3,5,7,11}\\$, then (m\in F_5).
So (F_5) contains a very large set of integers.

To get **lower bounds for (D_5)** [[nomath]](i.e. minimal $k=5$, not just $\le5$)[[/nomath]], one needs to know that many of those (m\in F_5) are **not** already in (F_4) or (F_3).

Erdős–Graham note two relevant facts:

* For any fixed prime $q$, **almost all numbers of the form $Pq$ with $P$ prime do not belong to (F_4)**.
* Moreover, if an element of (D_3) has the form $2P$ with $P$ an odd prime, then it must be $6$ or $10$.

Putting these together gives at least a “semiprime” lower bound: for all but finitely many primes $P$, the number $2P$ is in (F_5), not in (F_4), and not in (D_3), hence (2P\in D_5). Consequently,
[
D_5(n)\ \gg\ \pi(n/2)\ \asymp\ \frac{n}{\log n}.
]
[[nomath]](One can similarly get $\gg n/\log n$ from $3P,5P,\dots$ with more bookkeeping.)[[/nomath]]

What is *not* clearly resolved in these classical references is whether (D_5(n)) is actually (\asymp n) (positive density), though it is very plausible in view of how sparse (F_4) is expected to be on squarefree integers.

**Summary for $k=5$:**
[
D_5(n)\ \gg\ \frac{n}{\log n},\qquad D_5(n)\le n,
]
and the precise density/order beyond that is not pinned down in the quoted sources.

---

## $k=6$: (D_6(n)) has at least (\gg n/\log n); conjecturally (\gg n)

Here (D_6=F_6\setminus F_5). Erdős–Graham show:

* The **least element** of (D_6) is (n^*=527=17\cdot31).

* By their “small prime divisor” criterion, **no element of (D_6)** can be divisible by $2,3,5,7,11$.
  Hence an immediate upper-density bound:
  [
  D_6(n)\ \le\ |\\{m\le n:\gcd(m,2310)=1\\}|\ \sim\ \frac{16}{77},n,
  ]
  so (D_6) can have density at most (16/77\approx 0.208).

* They prove (Theorem 3) that **for almost all primes $q$, (13q\notin F_5)**, hence (13q\in D_6) for almost all primes $q$.
  This gives a rigorous lower bound
  [
  D_6(n)\ \gg\ \pi(n/13)\ \asymp\ \frac{n}{\log n}.
  ]

* They also explicitly state the conjectural strengthening:
  [
  \text{“We are reasonably certain that }D_6(n)>\varepsilon n.”
  ]
  So the answer to your example question “is (D_6(n)\gg n)?” is: **it is conjectured yes by Erdős–Graham, but not proved** in the cited work.

They even remark that “it seems certain that almost all products of two primes do not belong to (F_5)” [[nomath]](i.e. semiprimes should typically lie in $D_6$)[[/nomath]], which—if made quantitative—would still only give (D_6(n)) of order (\sim n\log\log n/\log n), but they are envisioning a genuinely linear-sized set.

**Summary for $k=6$:**
[
\frac{n}{\log n}\ \ll\ D_6(n)\ \le\ \frac{16}{77},n+o(n),
]
and (D_6(n)\gg n) is a classical conjecture (open in the sources above).

---

## Compact “order of growth” table (what’s known vs conjectured)

Let (D_k(n)=|D_k\cap[1,n]|). Then, for (3\le k\le 6):

* (k=3:\quad \sqrt n\ll D_3(n)=o(n)), conjecturally (D_3(n)\asymp \sqrt n).
* (k=4:\quad D_4(n)=\Theta(n)) (positive density, at least all nonsquarefree integers up to negligible exceptions).
* (k=5:\quad D_5(n)\gg n/\log n) [[nomath]](e.g. from many semiprimes $2p$)[[/nomath]], but a clean (\Theta(n)) statement is not settled in the classical references.
* (k=6:\quad D_6(n)\gg n/\log n), conjecturally (D_6(n)\gg n); also (D_6(n)\le (16/77+o(1))n).

If you want, I can also restate the Erdős–Graham constructions in your (a_1<\dots<a_k=m) language [[nomath]](they often phrase things as explicit square identities like $m!(m-1)!\cdots = \square$)[[/nomath]], which makes it easier to see where the “$2,3,5,7,11$” and “$13p$” phenomena come from.
