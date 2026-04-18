# Grok Response for Problem 212

**Problem 212.** Is there a dense subset of \(\mathbb{R}^2\) such that all pairwise distances are rational?

After substantial effort, I could not solve it.

To indicate the nature of the difficulty, I record the main lines of attack that were attempted and where they became inconclusive.

Fix a countable dense subset \(\{p_n\}_{n=1}^\infty\) of \(\mathbb{R}^2\) (e.g., \(\mathbb{Q}^2\)). The goal is to construct a sequence \(\{s_n\}\) inductively so that
- \(d(s_n,p_n)<1/n\),
- \(d(s_i,s_j)\in\mathbb{Q}\) for all \(i,j\le n\).

If this is possible, then \(S=\{s_n\}\) is dense (it comes arbitrarily close to each \(p_n\)) and has all pairwise distances rational by construction.

Begin with \(s_1=p_1\) (or any convenient point). Suppose \(F_{n-1}=\{s_1,\dots,s_{n-1}\}\) has already been chosen with all pairwise distances rational. It is necessary to show that the set
\[
X_n=\{x\in\mathbb{R}^2 : d(x,s_k)\in\mathbb{Q}\text{ for all }k=1,\dots,n-1\}
\]
is dense; one could then pick \(s_n\in X_n\) inside the ball of radius \(1/n\) about \(p_n\) and distinct from the previous points.

For \(|F|=1\), \(X_1\) is a union of circles of rational radii about a fixed center. Since \(\mathbb{Q}^+\) is dense in \(\mathbb{R}^+\), this union is dense.

For \(|F|=2\), place the two points at \((0,0)\) and \((d,0)\) with \(d\in\mathbb{Q}^+\). The locus for rational distances \(p,q\) to the two centers forces the abscissa \(x\) of any such point to be rational:
\[
x=\frac{p^2-q^2+d^2}{2d}\in\mathbb{Q}.
\]
The ordinate then satisfies \(y^2=p^2-x^2\in\mathbb{Q}\), so \(y=\pm\sqrt{r}\) for some \(r\in\mathbb{Q}\). The set of all such points \((q,\pm\sqrt{r})\) (\(q,r\in\mathbb{Q}\), \(r\ge0\)) is dense in \(\mathbb{R}^2\): given any \((a,b)\) with \(b>0\), choose rational \(q\approx a\) and rational \(r\approx b^2\); continuity of the square-root map sends the dense set \(\mathbb{Q}\cap[0,\infty)\) to a dense set in \([0,\infty)\), so \((q,\sqrt{r})\) lies arbitrarily close to \((a,b)\). The same holds for the lower half-plane. Thus \(X_n\) is dense for \(|F|=2\).

For \(|F|=3\), place the points at \((0,0)\), \((5,0)\), and \((0,12)\) (a 5-12-13 right triangle with all sides rational). Let \(X\) have rational distances \(p,q,r\) to these three centers. Subtracting the squared-distance equations for the first two centers again forces the abscissa to be rational. Substituting into the third equation then forces the ordinate to be rational as well:
\[
24y=p^2+144-r^2\in\mathbb{Q}.
\]
Hence candidate points lie in \(\mathbb{Q}^2\). Inside \(\mathbb{Q}^2\), having rational distance to \((0,0)\) means \(x^2+y^2=s^2\) for some \(s\in\mathbb{Q}\). The set of all such rational points is dense in \(\mathbb{R}^2\): rational points on the unit circle are dense (parametrized by \(t\in\mathbb{Q}\), the map \(t\mapsto((1-t^2)/(1+t^2),2t/(1+t^2))\) is continuous and sends the dense set \(\mathbb{Q}\) onto a dense subset of the circle). Scaling by a rational radius \(r\) close to the desired distance from the origin therefore produces points dense in every annulus; combining dense directions with dense radii yields density in the whole plane. The extra distance conditions to \((5,0)\) and \((0,12)\) are compatible with the same parametrization, so \(X_n\) remains dense for this particular triple.

The pattern continues for small finite \(F\): each new rational-distance condition cuts the locus down to a countable union of algebraic curves of low degree, but the freedom in choosing the rational radii appears to leave enough parameters for the union to stay dense. However, when \(|F|\) becomes large, the intersection of many such conditions imposes increasingly stringent algebraic constraints on the coordinates of candidate points. In suitable coordinate systems the points are forced to lie in \(\mathbb{Q}^2\) (or a fixed quadratic extension of \(\mathbb{Q}\)), after which the problem reduces to selecting a dense subset of \(\mathbb{Q}^2\) in which *every* pair satisfies \(dx^2+dy^2=\) (square of a rational). No explicit construction of such a subset is known, nor is a proof that none exists. Density of the directions arising from Pythagorean triples supplies local density, but global consistency across *all* pairs simultaneously cannot be guaranteed inductively without a uniform bound on the “algebraic degree” of the constraints, which appears to grow.

Attempts to obtain a contradiction from topological or measure-theoretic considerations also fail. Translating so that one point lies at the origin, the inner products \(\langle s_i,s_j\rangle\) all lie in \(\mathbb{Q}\) (because squared distances are rational). The associated bilinear form takes rational values on a dense set, but continuity and density of \(\mathbb{Q}\) in \(\mathbb{R}\) produce no immediate obstruction. Linear functionals \(\langle u,\cdot\rangle\) for fixed \(u\neq0\) map the dense set to \(\mathbb{Q}\), yet again \(\mathbb{Q}\) is dense in \(\mathbb{R}\), so no contradiction arises. Measure-zero arguments are likewise inconclusive because countable unions of circles (or algebraic curves) can easily be dense.

Thus the inductive construction succeeds for small configurations but stalls at the question of whether an infinite, dense, rationally-distance-closed subset of \(\mathbb{Q}^2\) (or of a fixed number field) can be assembled. Neither a concrete recursive choice of radii that preserves density nor a rigidity argument forbidding it could be completed. Consequently the existence question remains unresolved.

**Final Answer**

I could not solve it.
