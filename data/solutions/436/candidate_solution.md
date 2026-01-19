What you call (\Lambda(k,m)) is exactly the function $A(k,m)$ introduced by D. H. Lehmer and Emma Lehmer [[nomath]](they define $r(k,m,p)$ for “sufficiently large” primes $p$ and then take $\limsup$)[[/nomath]]. ([UMD Computer Science][1])

## Pairs ((m=2))

### Finiteness

Yes: (\Lambda(k,2)) is **finite for every** (k\ge2).  This was proved by Adolf Hildebrand (1991) (and is also recorded in OEIS A000445). ([Erdős Problems][2])

So for each fixed $k$ there is a constant $C(k)$ such that, for every sufficiently large prime $p$, one can find a pair of consecutive $k$-th power residues (\le C(k)).

### Known exact values / best-known bounds

For small $k$, the exact (\Lambda(k,2)) values are known and they grow very fast. OEIS A000445 lists:
[
\Lambda(2,2)=9,\ \Lambda(3,2)=77,\ \Lambda(4,2)=1224,\ \Lambda(5,2)=7888,\ \Lambda(6,2)=202124,\ \Lambda(7,2)=1649375.
]
([OEIS][3])

Some of these are “best possible” in the strong sense that there are infinitely many primes $p$ whose *least* such pair is exactly ((\Lambda(k,2),\Lambda(k,2)+1)); for instance, Bierstedt–Mills prove this for quartic residues (and also recall the analogous statement for cubic residues). ([UMD Computer Science][4])

For $k=2$, Lehmer–Lehmer give an elementary proof that (\Lambda(2,2)=9): every prime (p>5) has a consecutive quadratic-residue pair no later than $(9,10)$. ([UMD Computer Science][1])

For $k=8$, the exact value is not pinned down in the classical literature; OEIS records computational bounds
[
1499876 \le \Lambda(8,2) \le 1508324.
]
([OEIS][3])

And Brillhart–Lehmer–Lehmer give (older) lower bounds already showing how quickly things explode, e.g.
[
\Lambda(8,2) > 1200744,\quad \Lambda(9,2) > 8262536,\quad \Lambda(10,2) > 22458303.
]
([UMD Computer Science][5])

### “How large” as a function of $k$?

This is still not well understood: Hildebrand’s theorem gives finiteness for every $k$, but the **growth rate** of (\Lambda(k,2)) in $k$ is still considered part of the open-ended problem. ([Erdős Problems][2])

[[nomath]](Heuristically, if residues behaved like independent random events of density $\sim 1/k$, you’d expect the *typical* first pair around size $\asymp k^2$; the point here is that $\Lambda(k,2)$ is a **worst-case-over-primes** quantity, and it can be astronomically larger, as the known values show.)[[/nomath]]

## Triples ((m=3))

### Even $k$: infinite

(\Lambda(2,3)=\infty): Lehmer–Lehmer prove that the first occurrence of **three consecutive quadratic residues** can be forced arbitrarily far out by choosing $p$. ([UMD Computer Science][1])

In fact (\Lambda(k,3)=\infty) for **all even $k$** (as summarized in the modern problem write-up and going back to Lehmer–Lehmer’s methods). ([Erdős Problems][2])

### $k=3$: finite and known

For cubic residues, triples *are* uniformly bounded: Lehmer–Lehmer–Mills–Selfridge prove that every non-exceptional prime has a triplet (\le (23532,23533,23534)), and that this bound is best possible (infinitely many primes attain it). Hence
[
\Lambda(3,3)=23532.
]
([UMD Computer Science][6])

### Odd (k\ge 5): open

Whether (\Lambda(k,3)) is finite for **all odd (k\ge5)** is (as of the latest available summaries) still open, and understanding the size/growth of (\Lambda(k,3)) for odd $k$ is part of the remaining problem. ([Erdős Problems][2])

## Context: longer runs

For completeness: for runs of length (\ge 4), things are unbounded across primes: Graham proved (\Lambda(k,4)=\infty) for all (k\ge2) [[nomath]](indeed the paper uses the ability to prescribe $k$-th power character values on initial primes)[[/nomath]]. ([UMD Computer Science][7])

---

If you tell me which $k$ you care about [[nomath]](say $k=5$ or $k=7$)[[/nomath]] and whether you want “best known explicit numerical constant” vs “qualitative finiteness/infinity plus references,” I can tailor the discussion (e.g., describe the character-preassignment mechanism behind the huge extremal values, and how it’s used to delay runs).

[1]: https://www.cs.umd.edu/~gasarch/TOPICS/res/ll.pdf "https://www.cs.umd.edu/~gasarch/TOPICS/res/ll.pdf"
[2]: https://www.erdosproblems.com/436 "https://www.erdosproblems.com/436"
[3]: https://oeis.org/A000445 "A000445 - OEIS"
[4]: https://www.cs.umd.edu/~gasarch/TOPICS/res/resbiemills.pdf "https://www.cs.umd.edu/~gasarch/TOPICS/res/resbiemills.pdf"
[5]: https://www.cs.umd.edu/~gasarch/TOPICS/res/resbll.pdf "https://www.cs.umd.edu/~gasarch/TOPICS/res/resbll.pdf"
[6]: https://www.cs.umd.edu/~gasarch/TOPICS/res/llms.pdf "https://www.cs.umd.edu/~gasarch/TOPICS/res/llms.pdf"
[7]: https://www.cs.umd.edu/~gasarch/TOPICS/res/resgraham.pdf "https://www.cs.umd.edu/~gasarch/TOPICS/res/resgraham.pdf"
