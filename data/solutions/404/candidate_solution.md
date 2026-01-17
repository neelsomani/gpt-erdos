This is **Erdős problem #404** (Erdős–Graham, 1980). In particular, in general it is **not known** which pairs $(a,p)$ give a finite bound and which (if any) give an infinite bound. ([Erdős Problems][1])

That said, there are some clean “always finite” families, some very large known values, and a useful reformulation of your second question.

---

## Setup and easy monotonicities

Fix (a\ge 1) and a prime $p$. Consider all finite strictly increasing sequences
$
a=a_1<a_2<\cdots<a_n
$
and the $p$-adic valuation
$
\nu_p!(\sum_{i=1}^n a_i!).
$
Because (\nu_p(\cdot)\ge k \implies \nu_p(\cdot)\ge k-1), the set of achievable exponents is an initial segment ({0,1,\dots,f(a,p)}) if it is bounded. In any case, you always have the trivial lower bound
$
f(a,p)\ \ge\ \nu_p(a!)\qquad\text{(take just the single term (a!)).}
$

---

## A large, completely understood family: (a\equiv -1 \pmod p)

Let (t=\nu_p(a!)). If (a\equiv -1\pmod p), i.e. (p\mid (a+1)), then
[
\nu_p((a+1)!) = \nu_p(a!)+\nu_p(a+1)\ \ge\ t+1,
]
and since (\nu_p(n!)) is nondecreasing in $n$, every factorial ((a_i!)) with (a_i\ge a+1) is divisible by (p^{t+1}).

So for any choice (a=a_1<a_2<\cdots<a_n),
[
\sum_{i=1}^n a_i!\ =\ a! \ +\ p^{t+1}\cdot(\text{integer}).
]
Hence the sum has (\nu_p=\nu_p(a!)=t) exactly, and **you cannot gain even one additional $p$** beyond (\nu_p(a!)).

**Conclusion (proved):**
[
a\equiv -1\pmod p\quad\Longrightarrow\quad f(a,p)=\nu_p(a!).
]

This already gives infinitely many ((a,p)) with a finite upper bound.

[[nomath]](As a special case, $f(1,2)=0$ because any sum containing $1!=1$ is odd.)[[/nomath]]

---

## A striking known value: (f(2,2)=254)

Lin (1976) proved that the **largest power of 2** that can divide a sum of **distinct factorials containing $2!$** is (2^{254}), i.e.
[
f(2,2)=254.
]
This is explicitly recorded in the companion Erdős problem #403, and #404 points to this as the best concrete bound in that direction. ([Erdős Problems][2])

This one example already shows how wild $f(a,p)$ can be: (\nu_2(2!)=1) but (f(2,2)=254).

The discussion thread also notes the “non-monotone / erratic” behavior in $a$ even for (p=2); e.g.
[
f(1,2)=0,\quad f(2,2)=254,\quad f(3,2)=1,\quad f(4,2)=6,\quad f(5,2)=3,\ \ldots
]
([Erdős Problems][3])

---

## Terence Tao’s iterative lemma (a main tool for lower bounds)

A very useful (and quite elementary) lemma in the forum thread is the following “propagation” principle.

Let $P(a,p,N)$ be the statement that there exist
$
a=a_1<a_2<\cdots<a_n<N
$
such that
$
p^{\nu_p(N!)}\mid \sum_{i=1}^n a_i!.
$
Then, roughly speaking, if the factorials in a short block $[N,N+H)$, after normalizing by (p^{\nu_p(N!)}), have subset sums that cover all residue classes modulo the extra $p$-power gained in $(N+H)!/N!$, one can extend a solution at level (N) to a solution at level $N+H$. ([Erdős Problems][3])

Tao points out concrete consequences, e.g. $P(a,p,N)\Rightarrow P(a,p,N+1)$ whenever (p\nmid (N+1)), and suggests that for some primes [[nomath]](he mentions $p=5$)[[/nomath]] one can often push by larger steps (H=p^j) provided a finite “coverage” computation works at level $j$. ([Erdős Problems][3])

He also notes that verifying these steps up to (j\le J) would already give a lower bound of the shape
[
f(a,p)\ \gtrsim\ \nu_p\big((p^{J+1}-1)!\big),
]
which is enormous even for moderate $J$. ([Erdős Problems][3])

In the same thread, Tao reports computational/experimental evidence that $f(1,5)$ may be extremely large and “possibly even infinite,” giving explicit examples of large 5-adic divisibility built recursively. ([Erdős Problems][3])

---

## Your second question is essentially equivalent to “some (f(a,p)=\infty)”

Let $p$ be fixed.

### If such an infinite sequence exists, then some $f(a,p)$ is infinite

If there is an infinite sequence (a_1<a_2<\cdots) with
[
m_k:=\nu_p!\left(\sum_{i\le k}a_i!\right)\to\infty,
]
then for every $K$ there is some $k$ with (p^K\mid \sum_{i\le k}a_i!). Taking (a=a_1), this says there is **no finite upper bound** on the $K$’s achievable by some sum of distinct factorials beginning with $a$. So (f(a_1,p)=\infty).

### Conversely, if (f(a,p)=\infty), you can extract an infinite sequence with (m_k\to\infty)

If for a fixed $(a,p)$ you can hit (p^K) divisibility for every $K$ using some finite set of factorials starting at $a$, then [[nomath]](viewing these as compatible congruence conditions in $\mathbb Z_p$, using compactness / a diagonal argument)[[/nomath]] one can build a **single** infinite $\\{0,1\\}$-choice of factorials whose p-adic sum is exactly $0$. Then the partial sums along that increasing set have (\nu_p\to\infty).

So your second question is “yes” **if and only if** there exists at least one pair $(a,p)$ with (f(a,p)=\infty).

And **that is precisely the open content** of Erdős problem #404: it is not currently known whether any $f(a,p)$ is infinite, nor whether all are finite. ([Erdős Problems][3])

---

## So what can we say about the behavior of $f(a,p)$ today?

What is known/solid:

* **Always:** $f(a,p)\ge \nu_p(a!)$.
* **Always finite in at least one infinite family:** if (a\equiv -1\pmod p), then (f(a,p)=\nu_p(a!)) (proved above).
* **There are spectacularly large finite values:** e.g. (f(2,2)=254). ([Erdős Problems][2])
* **The function is highly irregular in $a$** [[nomath]](even fixing $p=2$)[[/nomath]]. ([Erdős Problems][3])
* **No general criterion is known** that decides finiteness vs infiniteness for a given ((a,p)). The problem remains open. ([Erdős Problems][1])

What seems to be the main line of attack (and why it’s hard):

* One can try to **propagate** divisibility to larger and larger $k$ by adding carefully chosen factorials in controlled blocks (Tao’s lemma). This reduces the question to (still nontrivial) **subset-sum coverage** questions modulo powers of $p$, where the available summands are normalized factorial residues. ([Erdős Problems][3])
* For some primes [[nomath]](notably $p=5$ in Tao’s experiments)[[/nomath]] this propagation seems to have a lot of “room,” hinting that $f(1,5)$ might even be infinite — but this is currently not proved. ([Erdős Problems][3])

---

## Bottom line answers to your two questions

* **Classification of $(a,p)$ with finite upper bound:**
  *Open in general.* There is a clean infinite family of pairs with a finite bound [[nomath]](namely $a\equiv -1\pmod p$, where $f(a,p)=\nu_p(a!)$)[[/nomath]], and at least one famous finite value (f(2,2)=254). Beyond that, no full classification is known. ([Erdős Problems][3])

* **Existence of a prime $p$ and infinite sequence (a_1<a_2<\cdots) with (m_k\to\infty):**
  This is *equivalent* to asking whether **some** $f(a,p)$ is infinite. As of the current literature status recorded on the Erdős problems site, this is **open**. ([Erdős Problems][3])

---

If you tell me which prime(s) $p$ you care about [[nomath]](e.g. $p=2$ vs odd $p$)[[/nomath]], I can also summarize the most promising “propagation step” one typically tries to verify (the subset-sum coverage condition in Tao’s lemma) and what tends to go wrong at higher $p$-adic orders.

[1]: https://www.erdosproblems.com/404 "
  
    Erdős Problem #404
  
"
[2]: https://www.erdosproblems.com/tags/factorials "
  
    Erdős Problems
  
"
[3]: https://www.erdosproblems.com/forum/discuss/404 "

    Erdős Problem #404 - Discussion thread

"
