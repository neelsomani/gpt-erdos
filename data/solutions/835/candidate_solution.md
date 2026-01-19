This is (as of **31 Dec 2025 / 18 Jan 2026**) an **open problem** for general (k>2), with substantial partial results.

### Reformulation

Let (V=\binom{[2k]}{k}). Put an edge between two $k$-sets (B,C) if (|B\cap C|=k-1) (i.e. they differ by swapping one element). This is the **Johnson graph** $J(2k,k)$. ([AEB][1])

Your condition says: for every ((k+1))-set $A$, the $k+1$ sets (A\setminus{a}) [[nomath]](for $a\in A$)[[/nomath]] receive all $k+1$ colors, hence are all distinct colors. But whenever (|B\cap C|=k-1), we have (|B\cup C|=k+1), so (B,C) appear together among the $k$-subsets of (B\cup C), forcing (c(B)\neq c(C)). So your coloring is exactly a **proper ((k+1))-coloring** of $J(2k,k)$. Conversely, any proper ((k+1))-coloring makes every ((k+1))-clique [[nomath]](in particular the clique coming from a $(k+1)$-set $A$)[[/nomath]] rainbow.

So the question is equivalent to:
[
\chi(J(2k,k))=k+1\ ?
]
This equivalence [[nomath]](and the trivial bounds $k+1\le \chi(J(2k,k))\le 2k$)[[/nomath]] is explicitly noted in the Erdős–Rosenfeld problem statement. ([Erdős Problems][2])

### What is known

* $k=2$ works [[nomath]](easy example; this is the “rainbow triangles” $3$-edge-coloring of $K_4$)[[/nomath]]. ([Erdős Problems][2])
* Computed/known chromatic numbers show it is **false for (3\le k\le 8)**. ([Erdős Problems][2])
  For instance the table of known values/bounds gives

  * (\chi(J(6,3))=6) [[nomath]](so not $4$)[[/nomath]],
  * (\chi(J(8,4))=6) [[nomath]](so not $5$)[[/nomath]],
  * (\chi(J(10,5))\in{8,9}) [[nomath]](so not $6$)[[/nomath]], etc. ([AEB][1])
* **Newer partial result (posted Dec 2025 on the Erdős Problems forum):** Tang & Ma prove that if (k>2) and **$k+1$ is not prime**, then (\chi(J(2k,k))\ne k+1). In other words, any potential example would have to have $k+1$ prime. ([Erdős Problems][3])

The Erdős Problems page currently labels the problem as **open** (“Open, but could be proved with a finite example.”). ([Erdős Problems][3])

### Structural meaning (why it’s hard)

If such a coloring exists, then each color class must be extremely rigid: one can show [[nomath]](by a double-counting argument using the fact that each $(k+1)$-set contains exactly one $k$-subset of each color)[[/nomath]] that every color class has size
[
\frac{1}{k+1}\binom{2k}{k}
]
[[nomath]](the $k$th Catalan number)[[/nomath]], and in fact each color class forms a Steiner system $S(k-1,k,2k)$; the whole coloring becomes a “large set” (a partition) of such Steiner systems. This “large set of Steiner systems” viewpoint is mentioned as the likely route to a full resolution. ([Erdős Problems][3])

### Bottom line

* **No example is known for any (k>2).**
* It is **known impossible** for (3\le k\le 8). ([Erdős Problems][2])
* It is also known impossible for all (k>2) with **$k+1$ composite**. ([Erdős Problems][3])
* The remaining case [[nomath]](**$k+1$ prime**)[[/nomath]] is, as of the sources above, **still open**. ([Erdős Problems][3])

If you tell me whether you want a proof of the equivalence to (\chi(J(2k,k))=k+1) written out cleanly, or the Steiner-system/“large set” derivation, I can write either in full detail.

[1]: https://aeb.win.tue.nl/graphs/Johnson.html "Johnson"
[2]: https://www.erdosproblems.com/latex/835 "
  
    Erdős Problems
  
"
[3]: https://www.erdosproblems.com/forum/discuss/835 "

    Erdős Problem #835 - Discussion thread

"
