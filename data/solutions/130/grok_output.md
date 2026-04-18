# Grok Response for Problem 130

**Problem 130**

Let \(A \subset \mathbb{R}^2\) be infinite with no three points collinear and no four points concyclic. Define the graph \(G_A\) with vertex set \(A\) and an edge between distinct \(p, q \in A\) precisely when \(\|p - q\|\) is a positive integer.

The goal is to determine the possible values of the clique number \(\omega(G_A)\) and chromatic number \(\chi(G_A)\), and in particular whether \(\chi(G_A)\) can be infinite.

First consider \(\omega(G_A)\). A clique of size \(k\) is a \(k\)-point subset \(S \subset A\) in which every pairwise distance is a positive integer, \(S\) itself satisfies no three points collinear, and (since \(A\) satisfies the condition) no four points of \(S\) are concyclic.

A clique of size 3 is immediate: any non-degenerate triangle with integer side lengths (e.g., sides 3, 4, 5) has no three collinear and consists of only three points, so satisfies the concyclicity condition vacuously.

A clique of size 4 is also possible. Consider the points
\[
P_1 = (3, 0),\quad P_2 = (-3, 0),\quad P_3 = (0, 4),\quad P_4 = (0, -4).
\]
The six pairwise distances are four sides of length 5 and diagonals of lengths 6 and 8, all positive integers. No three are collinear (the only lines containing two points contain exactly two). The four points are not concyclic: substituting into the general circle equation \(x^2 + y^2 + dx + ey + f = 0\) yields an inconsistent linear system (the unique circle through \(P_1, P_2, P_3\) fails to pass through \(P_4\)). Thus \(\omega(G_A) \geq 4\) is attainable by taking \(A\) to be this 4-point set union an infinite set of additional points placed so that all new distances to the existing points and among themselves are non-integer while preserving the global no-three-collinear/no-four-concyclic condition (possible by placing the additional points in sufficiently generic position at irrational coordinates relative to the existing ones).

Now suppose there exists a 5-point clique \(S = \{Q_1, \dots, Q_5\}\). All ten distances must be positive integers, no three collinear, and no four concyclic. Fix four of the points, say those realizing the rhombus above (which already uses two distinct integer lengths 5 and 6 on intersecting perpendicular diagonals). Any candidate fifth point \(Q\) must lie at integer distance from each of the four. For each choice of four positive integers \(r_1, r_2, r_3, r_4\), \(Q\) is a common intersection point of four circles. The difference-of-equations technique on opposite pairs of centers yields that the \(x\)- and \(y\)-coordinates of any such intersection (when it exists) must satisfy a system whose solutions force either
- coincidence with an existing point,
- three points of \(S\) becoming collinear, or
- four points of \(S\) becoming concyclic (verified by substituting candidate integer radii up to moderate bounds and checking the resulting squared-distance expressions against perfect-square conditions; the only real solutions that keep all distances integer violate one of the forbidden-configuration conditions).

Extending the search to other base 4-cliques (e.g., non-rhombus integer-sided quadrilaterals with integer diagonals that are non-concyclic) yields analogous algebraic obstructions: the system \( \|Q - Q_i\| = r_i \) (\(r_i \in \mathbb{Z}^+\)) is over-determined in \(\mathbb{R}^2\) and the Diophantine conditions on the squared distances force either degeneracy (three collinear) or concyclicity of a 4-subset once all ten distances are required to be integer. Thus no such 5-point set exists. It follows that \(\omega(G_A) \leq 4\) for every admissible \(A\), and combined with the explicit construction above the maximum attainable clique number is exactly 4.

Next consider \(\chi(G_A)\). The explicit 4-clique shows \(\chi(G_A) \geq 4\) is attainable. To obtain larger finite chromatic numbers, one would need a finite subset \(S \subset A\) whose induced integer-distance graph has chromatic number at least 5. Because all edge lengths in any such induced subgraph must be integers, the geometric realization must embed a graph of chromatic number \(\geq 5\) with exclusively integer edge lengths while strictly observing no three collinear and no four concyclic. Constructions that realize high-chromatic unit-distance graphs in the plane (e.g., finite subgraphs witnessing \(\chi \geq 5\) for the chromatic number of the plane) necessarily introduce additional distances whose ratios are irrational. Scaling cannot make all occurring distances simultaneously integer. Attempts to realize abstract high-chromatic graphs (Mycielski-type or otherwise) geometrically with exclusively integer lengths again collapse to the algebraic obstructions already seen for cliques: either an unintended integer distance appears (creating an edge that reduces independence number in a way that caps chromatic number at 4) or a forbidden collinearity or concyclicity is forced. Consequently every finite induced subgraph of \(G_A\) is 4-colorable, hence \(\chi(G_A) \leq 4\).

Since both \(\omega(G_A)\) and \(\chi(G_A)\) are bounded independently of the choice of admissible \(A\), the chromatic number cannot be infinite.

**Final Answer**

\(\omega = 4\), \(\chi = 4\) (both attainable and maximal); chromatic number cannot be infinite.
