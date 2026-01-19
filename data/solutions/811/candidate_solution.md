Let me denote (\ell:=e(G)) [[nomath]](so $\ell=m$)[[/nomath]].  When (n\equiv 1\pmod \ell), write
[
n=1+k\ell\qquad\text{so}\qquad k=\frac{n-1}{\ell}.
]
“Balanced” then means: for every vertex $v$ and every colour $c$, (\deg_c(v)=k). Equivalently, each colour class is a spanning $k$-regular graph, and these (\ell) regular graphs partition $E(K_n)$.

A complete characterization of those $G$ for which **every** balanced (\ell)-colouring of (K_n) [[nomath]](for all sufficiently large $n\equiv 1!!\pmod\ell$)[[/nomath]] must contain a **rainbow** $G$ is **not known**; it is essentially the Erdős–Pyber–Tuza / Erdős–Tuza problem from 1993 and remains open in general.

What *is* known at present splits into:

## 1) Graphs $G$ for which the statement is true (provably)

### All forests (in particular, all trees)

If $G$ is a forest with (\ell) edges, then for all sufficiently large (n\equiv 1\pmod\ell), **every** balanced (\ell)-colouring of (K_n) contains a rainbow copy of $G$.

Sketch of a direct greedy proof $self-contained$:

* Root each tree component of $G$. Embed the forest one edge at a time, always adding a *new* vertex (this is possible because forests have an ordering of edges where each new edge introduces a new vertex).
* Suppose we have already embedded $t$ edges, using $t$ distinct colours and at most (t+(#\text{components})\le \ell+1) vertices of (K_n).
* Take the next edge of $G$, which goes from an already embedded vertex $x$ to a new vertex. Pick any colour not used yet; call it $c$.
* In the balanced colouring, $x$ has exactly $k$ incident edges of colour $c$. At most (|U|-1\le \ell) of those go to already used vertices $U$. If (k>\ell) (i.e. (n-1> \ell^2)), there is at least one unused neighbour (y\notin U) with colour $c$. Embed the new vertex at $y$ and continue.

This produces a rainbow copy of the whole forest once (k>\ell), i.e. for all sufficiently large $n$.

So, **every forest is “good”** for your property.

### The 4-cycle (C_4)

Erdős and Tuza proved quantitative bounds implying that for large $n$, the condition “each colour has minimum degree (\ge (1/4-c)n)” forces a rainbow (C_4). In a balanced $4$-colouring of (K_n) [[nomath]](with $n\equiv 1\pmod 4$)[[/nomath]] each colour class is $(n-1)/4$-regular, and for large $n$ this exceeds $(1/4-c)n$. Hence **every balanced $4$-colouring of (K_n)** contains a rainbow (C_4) for all sufficiently large admissible $n$.

(So not only forests—at least one cyclic example is known to be forced.)

## 2) Graphs $G$ for which the statement is false (provably)

### (K_4) (6 edges)

This is a concrete small counterexample: there are balanced $6$-edge-colourings of (K_n) [[nomath]](for infinitely many $n\equiv 1\pmod 6$, e.g. $n=13^k$)[[/nomath]] **with no rainbow (K_4)**.

So the “for every graph $G$” hope is false.

### Many cliques (K_q) (and hence many dense graphs)

Axenovich and Clemen constructed (via iterated lexicographic products of classical 1-factorizations) completely balanced colourings that avoid rainbow cliques, and used this to show that **most cliques** (K_q) (in an asymptotic sense) do **not** have the property; they conjecture in fact that *every* (K_q) with (q\ge 4) fails.

More concretely, they prove:

* For any odd (\ell\ge 3) there are arbitrarily large (n=(\ell+1)^k) and completely balanced (\ell)-colourings of (K_n) with **no rainbow (K_m)** where
  [
  m=\left\lfloor \sqrt{\ell}+\frac72\right\rfloor.
  ]

This immediately yields **many non-clique counterexamples**: if $G$ has (\ell) edges and contains (K_m) as a subgraph for that $m$, then any rainbow copy of $G$ would contain a rainbow (K_m), so those balanced colourings avoid rainbow $G$ as well.

So, a large class of graphs with relatively large clique number [[nomath]](on the order of $\sqrt{e(G)}$)[[/nomath]] are *definitely not* “good”.

## 3) What remains open / unknown

Beyond these classes, the problem is widely open. Even for (\ell=6), Erdős explicitly asked whether every balanced 6-colouring of (K_{6n+1}) must contain a rainbow (C_6) [[nomath]](and $K_4$)[[/nomath]]; we now know (K_4) is *not* forced, but the (C_6) part is still the natural next test case and (as far as the standard problem statement records) remains unresolved.

More generally, outside forests and a few specific graphs like (C_4), there is no complete structural characterization known.

## Summary “classification” as of current knowledge

* **Provably true:** all forests (hence all trees), and (C_4).
* **Provably false:** (K_4); and in fact **infinitely many graphs** [[nomath]](including “most” cliques and many $\ell$-edge graphs containing a clique of size $\approx \sqrt{\ell}$)[[/nomath]].
* **Open:** broad families of sparse cyclic graphs [[nomath]](e.g. $C_6$ is the historically highlighted case)[[/nomath]], and essentially the general characterization.

If you tell me a specific family (cycles, unicyclic graphs, bipartite graphs with given maximum degree, etc.), I can outline what the known constructions do or do not rule out, and what “next lemma” would be needed to settle that family.
