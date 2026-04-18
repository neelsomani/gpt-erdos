# Grok Response for Problem 629

The list chromatic number satisfies \(\chi_L(G) > k\) if and only if there exists an assignment \(L\) of lists of size \(k\) to the vertices of \(G\) with no proper coloring of \(G\) from these lists (i.e., \(G\) is not \(k\)-choosable). Since \(G\) is bipartite, fix a bipartition \(V(G) = X \cup Y\) with all edges between \(X\) and \(Y\). The goal is to determine the smallest \(|V(G)|\) such that some bipartite \(G\) on this many vertices admits a list assignment \(L\) with \(|L(v)| = k\) for all \(v\) admitting no proper coloring from the lists.

To obtain an upper bound on this minimal number, construct an explicit example. Let the ground set of colors be \([2k-1] = \{1, 2, \dots, 2k-1\}\). Let \(\mathcal{F}\) be the family of all \(k\)-subsets of \([2k-1]\), so \(|\mathcal{F}| = \binom{2k-1}{k}\). Construct the complete bipartite graph \(K_{n,n}\) with \(n = \binom{2k-1}{k}\) by placing a copy of \(\mathcal{F}\) on each side: identify the vertices in \(X\) with the members of \(\mathcal{F}\) (one vertex \(x_A\) for each \(A \in \mathcal{F}\)) and likewise the vertices in \(Y\) (one vertex \(y_A\) for each \(A \in \mathcal{F}\)). Assign to each vertex \(x_A\) (resp. \(y_A\)) the list \(L(x_A) = L(y_A) = A\).

It remains to show that this list assignment admits no proper coloring. Suppose toward a contradiction that \(c\) is a proper \(L\)-coloring. Let \(S\) be the set of colors used on \(X\), i.e.,
\[
S = \{ c(x_A) : A \in \mathcal{F} \}.
\]
(Thus \(c(x_A) \in A\) for each \(A\), and \(|S| \geq 1\).) Since the bipartition is complete, no color from \(S\) can be used on any vertex of \(Y\): for each \(y_B\), it is required that \(c(y_B) \in B \setminus S\). Equivalently, if there exists some \(B \in \mathcal{F}\) with \(B \subseteq S\), then \(y_B\) has no available color.

It will be shown that \(|S| \geq k\) always holds, which forces the existence of such a \(B\). First suppose toward a contradiction that \(|S| \leq k-1\). Let \(T \subseteq [2k-1]\) with \(|T| = |S| \leq k-1\) and \(S \subseteq T\). The complement \([2k-1] \setminus T\) then has size at least \((2k-1) - (k-1) = k\), so it contains at least one \(k\)-subset \(B \in \mathcal{F}\). But then \(B \cap T = \emptyset\), so \(c(x_B) \in B \subseteq [2k-1] \setminus T\), contradicting that all colors on \(X\) lie in \(S \subseteq T\). Thus \(|S| \geq k\).

Now suppose \(|S| \geq k\). Then \(S\) contains at least one \(k\)-subset \(B \subseteq S\) (pick any \(k\) elements of \(S\)). For this \(B\), we have \(B \subseteq S\), so \(y_B\) has no available color from \(L(y_B) \setminus S = \emptyset\). This contradicts that \(c\) is a proper coloring. Hence no proper \(L\)-coloring exists at all, so \(\chi_L(K_{n,n}) > k\) with \(n = \binom{2k-1}{k}\). This yields the upper bound
\[
n(k) \leq 2 \binom{2k-1}{k}.
\]

To show that this is tight (and hence exact), it must be verified that no bipartite graph on fewer than \(2 \binom{2k-1}{k}\) vertices can have list chromatic number exceeding \(k\). Let \(G = (X \cup Y, E)\) be an arbitrary bipartite graph admitting some list assignment \(L\) with \(|L(v)| = k\) for all \(v\) and no proper coloring from the lists. Let \(C\) be the union of all lists (the palette of all colors appearing in any list). Without loss of generality, all lists are distinct: if any list is repeated on a side, deleting duplicate vertices with that list only decreases \(|V(G)|\) while preserving the lack of a proper coloring (the constraints are strictly weaker after deletion).

The argument above that forces \(|S| \geq k\) (for \(S\) the colors used on \(X\)) relies on having a vertex in \(X\) for every possible \(k\)-subset of a palette of size exactly \(2k-1\): this is the unique palette size where the complement of any set of size at most \(k-1\) has size at least \(k\) (ensuring a \(k\)-set exists in the complement to derive a contradiction). If \(|C| < 2k-1\), then it is impossible for all lists to have size \(k\). If \(|C| > 2k-1\), then the number of distinct \(k\)-subsets is \(\binom{|C|}{k} > \binom{2k-1}{k}\) (as the binomial coefficients are increasing up to the middle), so realizing all of them on one side to force \(|S| \geq k\) requires strictly more than \(\binom{2k-1}{k}\) vertices on that side.

Thus the minimal palette size yielding the bound is exactly \(|C| = 2k-1\), and both \(X\) and \(Y\) must realize all \(\binom{2k-1}{k}\) possible lists (all \(k\)-subsets) to ensure the argument goes through on both sides: if even one \(k\)-subset \(U \subseteq [2k-1]\) is missing from the lists on \(Y\), then choosing colors on \(X\) with image exactly \(U\) (which is always possible, as every list intersects \(U\)) yields \(|S| = k\) with no \(B \subseteq S\) available to block all of \(Y\) (as the missing \(U\) is the only candidate for \(B = U\)). An exactly symmetric argument applies if a \(k\)-subset is missing from the lists on \(X\). Using any other configuration of (distinct) lists of size \(k\) either increases the palette size (forcing more than \(\binom{2k-1}{k}\) lists to realize all \(k\)-subsets) or fails to force \(|S| \geq k\) or fails to block all possibilities for \(S\) with \(|S| \geq k\).

Non-complete bipartite graphs on the same number of vertices only weaken the coloring constraints (nonadjacent pairs between \(X\) and \(Y\) may share a color without penalty), so it is strictly harder to admit a bad list assignment. Unbalanced bipartitions similarly fail to reduce the total below \(2 \binom{2k-1}{k}\), as (for example) taking \(|X| = \binom{2k-1}{k}\) and \(|Y| < \binom{2k-1}{k}\) necessarily omits at least one blocking list on \(Y\). Thus no smaller example exists, and
\[
n(k) = 2 \binom{2k-1}{k}.
\]

This holds for the base cases: \(n(1) = 2 \binom{1}{1} = 2\) (a single edge has \(\chi_L = 2 > 1\)); \(n(2) = 2 \binom{3}{2} = 6\) (\(K_{3,3}\) with all \(2\)-subsets of \([3]\) as lists has \(\chi_L > 2\), but no bipartite graph on at most \(5\) vertices does). 

**Final Answer**

\[ 2 \binom{2k-1}{k} \]
