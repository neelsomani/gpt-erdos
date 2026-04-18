# Grok Response for Problem 949

**Problem 949.** Let \(S \subset \mathbb{R}\) be a set containing no solutions to \(a + b = c\). Must there be a set \(A \subseteq \mathbb{R} \setminus S\) of cardinality continuum such that \(A + A \subseteq \mathbb{R} \setminus S\)?

The condition on \(S\) means that \(S \cap (S + S) = \emptyset\), i.e., \(S\) is sum-free in \(\mathbb{R}\). The desired set \(A\) must satisfy \(A \cap S = \emptyset\) and \((A + A) \cap S = \emptyset\).

To approach this, equip \(\mathbb{R}\) with its structure as a vector space over \(\mathbb{Q}\), which has dimension \(2^{\aleph_0}\) (the continuum) and thus admits a Hamel basis \(B\) of cardinality continuum (using the axiom of choice). Every \(x \in \mathbb{R} \setminus \{0\}\) has a unique expression as a finite sum \(x = \sum q_b b\) with \(q_b \in \mathbb{Q} \setminus \{0\}\) and \(b \in B\); the *support* of \(x\) is the finite set of such \(b\) with \(q_b \neq 0\), and the \(q_b\) are its coefficients.

Let \(U = \bigcup_{s \in S} \operatorname{supp}(s)\). Then \(|U| \leq |S| \cdot \aleph_0 \leq 2^{\aleph_0}\). If \(|U| < 2^{\aleph_0}\), let \(B' = B \setminus U\) (so \(|B'| = 2^{\aleph_0}\)). Set \(A = B'\). Then:
- No element of \(A\) lies in \(S\), since elements of \(S\) have supports in \(U\).
- For distinct \(b_1, b_2 \in A\), \(\operatorname{supp}(b_1 + b_2) = \{b_1, b_2\} \subseteq B'\), while elements of \(S\) have supports in \(U\), so \(b_1 + b_2 \notin S\).
- For any \(b \in A\), \(\operatorname{supp}(2b) = \{b\} \subseteq B'\), so \(2b \notin S\).

Thus \(A + A \subseteq \mathbb{R} \setminus S\), and \(|A| = 2^{\aleph_0}\).

If instead \(|U| = 2^{\aleph_0}\) (so \(B' = \emptyset\)), the above fails. In this case, fix a positive integer \(m \geq 1\) and consider candidate sets of the form \(A = \{m b : b \in B''\}\) for suitable \(B'' \subseteq B\) with \(|B''| = 2^{\aleph_0}\). For \(A\) to work, \(B''\) must avoid:
- All \(b\) with \(m b \in S\) (so \(A \cap S = \emptyset\)).
- All \(b\) with \(2m b \in S\) (so no \(a + a \in S\)).
- Both \(b\) and \(c\) whenever \(m(b + c) \in S\) for some \(c \neq b\) (so no \(a_1 + a_2 \in S\) with \(a_1 \neq a_2\)).

Each \(s \in S\) can cause at most finitely many such exclusions in \(B\) (at most the size of \(\operatorname{supp}(s)\), or at most two basis elements if \(s/m\) has the form of a basis element or sum of two). Thus, for any fixed \(m\), the "bad" basis elements excluded above number at most \(O(1) \cdot |S| = 2^{\aleph_0}\). If these exclusions do not cover all of \(B\) in a way that forces the independence number below continuum (e.g., if they induce at most continuum many disjoint pairs or singles on \(B\)), a subset \(B''\) of size continuum remains on which the corresponding \(A\) satisfies the conditions.

The sum-freeness of \(S\) is essential here: it restricts, for each fixed basis element \(b\), the set of coefficients \(K_b = \{q \in \mathbb{Q} : q b \in S\}\) to be sum-free in \((\mathbb{Q}, +)\). Thus \(K_b\) cannot contain all positive integers (e.g., it cannot contain both \(1\) and \(2\), since \(1 + 1 = 2\)). This ensures that for sufficiently many choices of \(m\), not all (or even a non-negligible portion) of \(B\) is blocked. In particular, sum-freeness prevents constructions like \(S \supseteq \bigcup_{m \geq 1} m B\), which would block all \(m\) but itself violates \(S \cap (S + S) = \emptyset\).

Combining the cases, such an \(A\) of cardinality continuum exists. (Note that the argument relies on the axiom of choice for the Hamel basis but holds in ZFC.)

However, the above reasoning contains gaps when the exclusions for a fixed \(m\) induce a graph on \(B\) (with edges from pair-blockings) that may have independence number \(1\) despite only continuum many edges, as a complete graph on continuum vertices has cardinality-\(2^{\aleph_0}\) edge set. While sum-freeness of \(S\) limits such dense blockings (via coefficient restrictions and support mismatches), a fully rigorous closure of this case requires a more careful choice of \(m\) (e.g., avoiding those for which \(S\) contains all \(m(b + c)\) over a dense collection of pairs) or an alternative subspace argument. After substantial effort, the details do not fully close without additional set-theoretic assumptions or a different approach.

I could not solve it.
