Let (W(k)=W(2,k)) be the least $N$ such that **every** red/blue colouring of ({1,\dots,N}) contains a monochromatic $k$-term arithmetic progression.

### What is known today (big picture)

There is still a huge gap between the best known lower and upper bounds.

* **Best known general lower bound (two colours):** for every (\varepsilon>0) and all large enough $k$,
  [
  W(k) > \frac{2^{k}}{k^{\varepsilon}} .
  ]
  This is due to Szabó (1990). ([Computer Science at UMD][1])

* **Best known general upper bound:** Gowers proved an explicit (still enormous) bound
  [
  W(r,k)\le 2^{2^{r^{2^{2^{k+9}}}}}
  ]
  [[nomath]](and in particular this gives a tower-of-2’s type bound when $r=2$)[[/nomath]]. ([Wikipedia][2])
  Earlier, Shelah showed a *primitive recursive* upper bound (a major improvement over the original Ackermann-type growth coming from van der Waerden’s proof). ([Computer Science at UMD][3])

So right now we know
[
\frac{2^k}{k^{o(1)}} \lesssim W(k) \lesssim \text{(a huge tower function in (k))}.
]
([Computer Science at UMD][1])

### About your example “prove (W(k)^{1/k}\to\infty)”

With what is known, we **cannot** prove that. In fact, the best known lower bounds are still essentially (2^k) up to subpolynomial factors, so they only give
[
\liminf_{k\to\infty} W(k)^{1/k} \ge 2,
]
and nothing like “(\to\infty)”. ([Computer Science at UMD][1])

So: **showing (W(k)^{1/k}\to\infty)** would be a major breakthrough beyond the current state of the art.

That said, you *can* meaningfully “improve the bounds” in an elementary way (compared to the very first probabilistic lower bounds). The cleanest standard improvement uses the Lovász Local Lemma. I’ll give that proof now.

---

## A concrete improvement you can prove: (W(k)\gtrsim2^k/k)

### Claim (LLL lower bound)

For all (k\ge 3),
[
W(k) > \left\lfloor \frac{2^{k-1}}{ek}\right\rfloor .
]
This is the “basic” Lovász Local Lemma bound, and it is a big step up from the naive first-moment/union-bound estimate. ([Computer Science at UMD][4])

### Proof (in simple steps)

Fix $N$. Colour each integer in ({1,\dots,N}) independently red/blue with probability $1/2$ each.

**Bad events.**
For each $k$-term arithmetic progression (P\subseteq{1,\dots,N}), let (E_P) be the event “$P$ is monochromatic”.

* A fixed progression $P$ is all red with probability (2^{-k}), and all blue with probability (2^{-k}).
  So
  [
  \mathbb P(E_P)=2\cdot 2^{-k}=2^{1-k}.
  ]
  Call this number $p$.

**Dependency bound.**
Two events (E_P, E_Q) are independent unless the progressions (P,Q) share at least one integer.

So we need an upper bound $D$ on: *how many $k$-APs can intersect a given $k$-AP?*

A standard estimate is:

> Any fixed $k$-AP in $[N]$ intersects fewer than $kN$ other $k$-APs. ([Computer Science at UMD][4])

So we can take (D<kN).

**Apply the symmetric Lovász Local Lemma.**
The symmetric LLL says: if
[
ep(D+1)\le 1,
]
then with positive probability **no** bad event happens, i.e. there exists a colouring with **no monochromatic (k)-AP**.

Here (p=2^{1-k}) and (D+1\le kN+1). So it is enough that
[
e\cdot 2^{1-k}\cdot (kN+1)\le 1.
]

A simple sufficient condition is
[
e\cdot 2^{1-k}\cdot kN \le 1,
]
i.e.
[
N \le \frac{2^{k-1}}{e,k}.
]

So if we set (N=\left\lfloor \frac{2^{k-1}}{ek}\right\rfloor), there exists a red/blue colouring of ({1,\dots,N}) with no monochromatic $k$-term progression. Therefore (W(k)>N), proving the claim. ■

### What this gives for (W(k)^{1/k})

From
[
W(k) > \frac{2^{k-1}}{ek},
]
we get
[
W(k)^{1/k} \ge 2\cdot (e,k)^{-1/k}\cdot 2^{-1/k}\to2.
]
So this method does **not** push (W(k)^{1/k}) upward; it only shows it is bounded below by something approaching $2$.

---

## Stronger known lower bounds (harder)

Szabó’s theorem upgrades the (2^k/(k))-type bound to
[
W(k) > \frac{2^k}{k^{\varepsilon}}\quad\text{for every fixed }\varepsilon>0\text{ and all large }k,
]
by using the fact that “most” $k$-APs are almost disjoint, which lets one run a more delicate local-lemma style argument. ([Computer Science at UMD][1])

Also, there are explicit algebraic constructions (Berlekamp) that give, for prime $p$,
[
W(p+1) \ge p\cdot 2^{p}\quad(\text{up to small variants in constants}).
]
([Computer Science at UMD][4])

---

## Why the “(W(k)^{1/k}\to\infty)” goal is still wide open

To prove (W(k)^{1/k}\to\infty), you would need a **superexponential** lower bound, for example
[
W(k)\ge 2^{c k\log k}\quad\text{or}\quad W(k)\ge k^k,
]
or anything with (\log W(k)/k\to\infty).

No such bound is known for the classical two-colour diagonal numbers $W(2,k)$. The literature still lists the best known general lower bound as essentially (2^k) up to subpolynomial loss. ([Wikipedia][5])

At the same time, the best general upper bounds are so huge that even proving a “reasonable” upper bound is hard; Graham famously offered a prize for showing (W(2,k)<2^{k^2}). ([Wikipedia][5])

---

## A forward-looking note (what might actually help)

If your real goal is to push beyond the (2^k)-barrier on the **lower** side, you need a new kind of construction. The random/LLL approach is already close to optimal “for that approach”, because it treats different progressions as mostly independent. Beating it likely needs either:

* a very structured colouring that kills *many* progressions at once (something like an algebraic or automaton-based colouring, but far more rigid than known ones), or
* a way to “couple” constraints across many differences so that long monochromatic progressions become impossible for combinatorial reasons, not just probabilistic ones.

Right now, even deciding the true order of magnitude [[nomath]](is it closer to $2^k$, or to something like $k!$, or $2^{k^2}$?)[[/nomath]] is totally open.

If you tell me what level you want (graduate-combinatorics course vs research-level survey), I can either:

* write the LLL proof in fully formal detail (including the dependency lemma), or
* sketch Szabó’s improvement idea and what “almost disjoint” really buys you.

[1]: https://www.cs.umd.edu/~gasarch/TOPICS/vdw/szabolower.pdf "https://www.cs.umd.edu/~gasarch/TOPICS/vdw/szabolower.pdf"
[2]: https://en.wikipedia.org/wiki/Van_der_Waerden_number "https://en.wikipedia.org/wiki/Van_der_Waerden_number"
[3]: https://www.cs.umd.edu/~gasarch/TOPICS/vdw/sz-thm-gowers-proof.pdf "https://www.cs.umd.edu/~gasarch/TOPICS/vdw/sz-thm-gowers-proof.pdf"
[4]: https://www.cs.umd.edu/~gasarch/papers/lowervdw.pdf "https://www.cs.umd.edu/~gasarch/papers/lowervdw.pdf"
[5]: https://en.wikipedia.org/wiki/Van_der_Waerden%27s_theorem?utm_source=chatgpt.com "Van der Waerden's theorem"
