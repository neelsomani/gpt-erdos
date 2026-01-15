Yes.

A coset (gH) always has the same size as the subgroup (H). So “different sizes” just means you are using cosets of different subgroups (with different orders).

### A concrete example (no singletons)

Take (G=\mathbb{Z}_{12}) (integers mod (12), under addition).

Let

* (H=\langle 2\rangle={0,2,4,6,8,10}), so (|H|=6).
* (K=\langle 4\rangle={0,4,8}), so (|K|=3).

Then the three cosets

* (1+H={1,3,5,7,9,11}) (size (6)),
* (0+K={0,4,8}) (size (3)),
* (2+K={2,6,10}) (size (3)),

are pairwise disjoint and their union is all of (\mathbb{Z}_{12}). So this is an exact covering by cosets of different sizes.

### In general: when is it possible?

* If (G) has a **proper nontrivial** subgroup (H) (so ( {e}\neq H\neq G)), then you can always do it in a very simple way:
  [
  G ;=; H ;\sqcup; \bigsqcup_{g\in G\setminus H} {g}.
  ]
  Here (H) is a coset of (H), and each singleton ({g}) is a coset of the trivial subgroup ({e}). This gives cosets of sizes (|H|) and (1).

* The only time you **cannot** do it is when (G) has **no** proper nontrivial subgroups. That happens exactly when (|G|) is prime (and also the trivial group of size (1)).

  * If (|G|=p) is prime, the only subgroups are ({e}) and (G).
  * So every coset is either a singleton (size (1)) or the whole group (size (p)).
  * If you use more than one coset in a partition, you cannot include the whole group as one piece, so all pieces must be singletons, hence all the same size.

So: **yes** for almost all groups, and **no** only for groups of prime order (and the trivial group).
