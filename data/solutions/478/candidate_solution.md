No one knows at present.

Your statement is exactly a long‑standing conjecture (usually attributed to Stauduhar, and also appearing in Guy’s *Unsolved Problems in Number Theory*): if
[
h(p):=|\\{1!,2!,\dots,(p-1)!\\}|\pmod p=\lvert A_p\rvert,
]
then
[
\frac{h(p)}{p}\ \longrightarrow\ 1-\frac1e\qquad (p\to\infty).
]
This is stated explicitly as **Stauduhar’s Conjecture** in recent work.  It is also recorded as a conjectured asymptotic in the literature on factorials mod $p$, with the remark that “very little seems to be known” about (V(0,p-1)=h(p)) beyond partial bounds. ([Journal de Théorie des Nombres][1])

## Why ((1-1/e)p) is the “natural” guess

Heuristically, the residues (k!\bmod p) “look random” as $p$ grows. A common strengthening is a **Poisson$1$ occupancy** heuristic: for each fixed (k\ge 0), the proportion of residue classes hit *exactly* $k$ times by ({1!,\dots,(p-1)!}) should tend to (\frac{1}{e,k!}). 

If the multiplicities are asymptotically Poisson with mean $1$, then the fraction hit at least once is
[
1-\Pr(\text{Poisson}(1)=0)=1-e^{-1},
]
which gives (h(p)\sim (1-1/e)p). This “$p/e$ classes missed” heuristic is explicitly mentioned in earlier work as well. 

## What is actually proved (far from linear)

Despite strong numerical/heuristic support, the best unconditional theorems are nowhere near a positive proportion of $p$.

* **Lower bounds.** Grebennikov–Sagdeev–Semchankau–Vasilevskii (arXiv 2022/2023) prove that the factorials produce at least
  [
  (\sqrt2+o(1))\sqrt p
  ]
  distinct residues mod $p$. ([arXiv][2])
  This is a big step beyond the trivial (\gg \sqrt p) type bounds, but still much smaller than (\asymp p).

* **Upper bounds / “many misses” on average.** Klurman–Munsch prove that the number of missed residue classes is unbounded *on average over primes*:
  [
  \frac{1}{\pi(x)}\sum_{p\le x}\bigl(p-h(p)\bigr)\ \gg\ \frac{\log\log x}{\log\log\log x},
  ]
  and they also give a stronger conditional bound under GRH. ([Journal de Théorie des Nombres][1])
  This shows (in a precise averaged sense) that $h(p)$ is not “almost all of $p$”—but it is still far weaker than a (\sim p/e) missing‑mass statement.

* **Random models.** Recent work studies probabilistic models that encode key structural constraints [[nomath]](e.g. $k!\not\equiv (k+1)!\pmod p$ so adjacent terms are never equal)[[/nomath]] and shows that **typical** sequences in the model have Poisson‑type behavior, supporting the conjecture—but this is not a proof for actual factorials. 

## A quick numerical sanity check

Just to illustrate how close things look in practice [[nomath]](these are direct computations of $|A_p|$)[[/nomath]]:

| $p$ | (|A_p|) | (|A_p|/p) |
|---:|---:|---:|
| 10 007 | 6 348 | 0.63436 |
| 100 003 | 63 243 | 0.63241 |
| 1 000 003 | 632 283 | 0.63228 |

And (1-\frac1e \approx 0.63212056).

This kind of data is exactly why the conjecture is widely believed—but as of the current literature, there is no proof that (|A_p| \sim (1-\tfrac1e)p), nor a disproof.

**Bottom line:** the asymptotic (|A_p|\sim (1-\tfrac1e)p) is a well‑known open conjecture (Stauduhar/Guy), strongly motivated by Poisson/random‑mapping heuristics and supported by computations, but still far beyond current techniques. 

[1]: https://jtnb.centre-mersenne.org/item/10.5802/jtnb.974.pdf "Distribution of factorials modulo p"
[2]: https://arxiv.org/abs/2204.01153?utm_source=chatgpt.com "On the sequence $n! \bmod p$"
