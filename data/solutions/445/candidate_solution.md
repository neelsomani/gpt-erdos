Let $p$ be prime and write (H:=\lfloor p^{c}\rfloor). Your question asks whether **every** interval
[
I=(n,n+H)\cap \mathbb Z
]
contains two integers (a,b\in I) with (ab\equiv 1\pmod p). Equivalently, whether the modular hyperbola
[
xy\equiv 1\pmod p
]
always has a point in the square (I\times I) [[nomath]](viewed modulo $p$)[[/nomath]].

### What is known unconditionally

* For (c\ge 1) the statement is essentially **trivial**, because $(n,n+p^c)$ contains at least $p$ consecutive integers, hence [[nomath]](mod $p$)[[/nomath]] it contains every residue class; in particular it contains some (a\equiv -1\pmod p), and then (a\cdot a\equiv 1\pmod p).

* The best *general* unconditional technology for this kind of question uses bounds for (incomplete) Kloosterman sums. In particular, as Browning–Haynes explain, while heuristics suggest one should be able to solve (xy\equiv 1\pmod p) with (x,y) in intervals once the interval lengths are (\gg p^{1/2}), the best general result “to date” (as highlighted by Heath-Brown) requires
  [
  |I_1|\cdot |I_2| \gg p^{3/2}\log^2 p
  ]
  to guarantee a solution ((x,y)\in I_1\times I_2). ([arXiv][1])

  Applying this with (I_1=I_2) of length $H$ gives a guaranteed solution whenever
  [
  H^2 \gg p^{3/2}\log^2 p \quad\Longleftrightarrow\quad H \gg p^{3/4}\log p.
  ]
  So **your desired conclusion is known [[nomath]](for all $n$)[[/nomath]] at least for any fixed (c>3/4)** [[nomath]](since then $p^c \gg p^{3/4}\log p$ for sufficiently large $p$)[[/nomath]]. This is exactly the regime where the main term (H^2/p) dominates the Kloosterman-sum error term coming from Weil’s bound. ([arXiv][1])

  [[nomath]](If the interval $(n,n+H)$ crosses a multiple of $p$, you can split it into at most two subintervals; one has length $\ge H/2$, and the same conclusion still goes through with only constant-factor changes.)[[/nomath]]

### What is *not* known (and what is expected)

For the range you asked about, (c>1/2), the situation is:

* **The statement as written [[nomath]](for every $n$)[[/nomath]] is not currently proved for all (c>1/2)**.

* Even for a *single fixed pair* of intervals (I_1,I_2\subset (0,p)) of lengths about (p^c), the known unconditional guarantee only reaches (c>3/4) via the bound above. ([arXiv][1])
  Your question asks for **uniformity in $n$** (i.e., for every translate), which is at least as hard.

* Browning–Haynes note Hooley’s conjecture on incomplete Kloosterman sums (roughly, square-root cancellation in the interval length) and explain that **even this conjecture would only push the interval-length threshold down to about (p^{2/3+\varepsilon})** (for each interval) in such problems. ([arXiv][1])
  So getting all the way to “every (c>1/2)” would require ideas beyond what is currently available (or beyond what Hooley’s conjecture alone would imply in the standard approach).

### A sanity check: why $1/2$ is the natural barrier

If (c<1/2), the statement is definitely false: take $n=1$ and $p$ large enough that (1+p^c<\sqrt p). Then every (a,b\in (1,1+p^c)\cap\mathbb Z) satisfies (2\le a,b<\sqrt p), so
[
1<ab<p,
]
hence (ab\not\equiv 1\pmod p). [[nomath]](The only way $ab\equiv 1\pmod p$ with $ab<p$ is $ab=1$, impossible here.)[[/nomath]]

This explains why (c>1/2) is the first regime where one might reasonably expect the property to hold.

### Bottom line

* **Unconditionally:** Yes for any fixed (c>3/4) [[nomath]](and trivially for $c\ge 1$)[[/nomath]], by known results on (xy\equiv 1\pmod p) in intervals relying on Weil/Kloosterman bounds. ([arXiv][1])
* **For the full range you ask, (c>1/2):** this is **not currently known** in general; it is consistent with standard heuristics but beyond the reach of the best available uniform bounds. ([arXiv][1])

If you want, I can also reformulate your question in terms of the 2D point set ({(x/p,x^{-1}/p)}\subset[0,1]^2) and “empty squares” (discrepancy/covering) language, which is another common way this problem is viewed.

[1]: https://arxiv.org/pdf/1204.6374 "https://arxiv.org/pdf/1204.6374"
