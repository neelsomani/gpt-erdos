# Grok Response for Problem 1033

**Estimation of \(h(n)\)**

We interpret \(h(n)\) formally as
\[
h(n) = \min \bigl\{ \, \max_{ \triangle \,uvw \in G} \bigl( d(u)+d(v)+d(w) \bigr) : \, G \text{ on } n \text{ verts},\ e(G) > n^2/4 \bigr\},
\]
where the minimum is attained (or approached) and the definition forces every graph with more than \(n^2/4\) edges to contain at least one triangle whose degree sum is at least \(h(n)\). Thus any explicit construction of a graph \(G\) with \(e(G)>n^2/4\) supplies an *upper bound* on \(h(n)\) via the largest degree-sum among its triangles. A matching lower bound would show that no such \(G\) can have all its triangles with degree-sum \(o(n)\) smaller than the same quantity.

**Construction yielding the upper bound.** Fix a parameter \(a\in(0,1/2)\) and partition \(V=[n]\) into sets \(X,Y\) with \(|X|=\lfloor a n\rfloor\), \(|Y|=\lceil(1-a)n\rceil\). Include all possible edges between \(X\) and \(Y\). On the vertex set \(Y\) include an auxiliary graph \(H\) containing
\[
e(H) > \bigl(\tfrac12-a(1-a)\bigr)n^2 = (a-\tfrac12)^2 n^2
\]
edges (possible for any \(a<1/2\)). Let \(G\) be the resulting graph on \(n\) vertices. Then
\[
e(G) = |X|\cdot|Y| + e(H) > a(1-a)n^2 + (a-1/2)^2 n^2 = n^2/4,
\]
as required.

Every triangle of \(G\) uses precisely one edge of \(H\) (say \(uv\subset Y\)) and one vertex \(w\in X\); there are no other triangles. The degrees in \(G\) satisfy
\[
d_G(u) = a n + d_H(u),\qquad d_G(v)=a n + d_H(v),\qquad d_G(w)=(1-a)n
\]
(up to \(O(1)\) rounding errors). Consequently every triangle degree-sum equals
\[
s(uv,w) = (1+a)n + d_H(u)+d_H(v).
\]
If \(H\) can be chosen so that
\[
\max_{uv\in E(H)} \bigl(d_H(u)+d_H(v)\bigr) \le \lambda n
\]
for some \(\lambda\), then every triangle of \(G\) has degree-sum at most \((1+a+\lambda)n+O(1)\). The average degree of \(H\) (on \(m=(1-a)n\) vertices) is already
\[
d_{\mathrm{avg}}(H) > \frac{2(a-1/2)^2 n^2}{(1-a)n} = \frac{2(a-1/2)^2}{1-a}\,n.
\]
A standard random regular (or near-regular) graph of this degree meets the edge-count requirement while keeping *all* degrees within \((1+o(1))\) of the mean (by standard concentration). For such an \(H\) we have \(d_H(u)+d_H(v)=(4(a-1/2)^2/(1-a)+o(1))n\) uniformly over edges \(uv\), and therefore
\[
\max_{\triangle} s(\triangle) \le \Bigl(1+a + \frac{4(a-1/2)^2}{1-a}+o(1)\Bigr)n.
\]
Define
\[
f(a) = 1+a + \frac{4(a-1/2)^2}{1-a},\qquad a\in[0,1/2).
\]
The construction shows
\[
h(n) \le \bigl(\min_{a\in[0,1/2)} f(a) + o(1)\bigr)n.
\]
It remains to minimise \(f\). Substitute \(u=1/2-a\) (\(u\in(0,1/2]\)):
\[
f=1.5-u+\frac{4u^2}{u+0.5}.
\]
The derivative of the second term is
\[
\frac{d}{du}\Bigl(\frac{4u^2}{u+0.5}\Bigr)=\frac{4u(u+1)}{(u+0.5)^2}.
\]
Setting the derivative of the whole expression to zero yields
\[
4u(u+1)=(u+0.5)^2 \iff 3u^2+3u-1/4=0.
\]
The positive root is
\[
u=\frac{-3+2\sqrt{3}}{6}.
\]
Substituting back (or simplifying the algebraic identity obtained by clearing denominators) produces
\[
\min f(a)=2(\sqrt{3}-1).
\]
(The algebraic verification: after inserting \(u=(-3+2\sqrt{3})/6\) one obtains \(u+1/2=\sqrt{3}/3\), the numerator \(4u^2=(7-4\sqrt{3})/3\), division supplies \(7/\sqrt{3}-4\), and collecting constant and \(\sqrt{3}\) terms collapses to \(-2+2\sqrt{3}\).) Consequently the construction proves
\[
h(n) \le \bigl(2(\sqrt{3}-1)+o(1)\bigr)n.
\]
Numerically \(2(\sqrt{3}-1)\approx 1.464\).

**Lower bound.** The matching lower bound
\[
h(n) \ge \bigl(2(\sqrt{3}-1)-o(1)\bigr)n
\]
would follow if every graph on \(n\) vertices with more than \(n^2/4\) edges necessarily contains a triangle whose degree-sum is at least \((2(\sqrt{3}-1)-\varepsilon)n\) for any fixed \(\varepsilon>0\) and all large \(n\). Equivalently: if every triangle has degree-sum \(<(2(\sqrt{3}-1)-\varepsilon)n\), then the edge count is at most \(n^2/4+o(n^2)\).

A direct proof of this statement appears to require a stability argument that shows any graph exceeding the Mantel threshold by \(\omega(n^2)\) edges must either contain a triangle using vertices whose collective degree exceeds the threshold or else be structurally close to the bipartite-plus-auxiliary-graph construction above (with the auxiliary graph \(H\) forced to have an edge whose codegree sum is large). While the construction demonstrates that the constant \(2(\sqrt{3}-1)\) is best possible *if* the lower bound holds, a rigorous verification that no substantially better construction exists (i.e., that one cannot keep *all* triangle degree-sums below \(2(\sqrt{3}-1)n-o(n)\) while still exceeding \(n^2/4\) edges) eludes elementary counting or double-counting arguments. Standard Mantel-stable techniques (e.g., edge deletion to bipartiteness, eigenvalue bounds, or sum-of-squares on triangle densities) produce weaker lower bounds such as \(h(n)\ge(1+\delta)n\) for small \(\delta>0\), but do not recover the optimal constant.

Thus the construction gives a tight asymptotic upper bound, and the conjectured matching lower bound remains open. In summary,
\[
h(n) = \bigl(2(\sqrt{3}-1)+o(1)\bigr)n
\]
if and only if the stated inequality holds; the “if” direction is supplied by the explicit family of graphs parameterised by \(a\approx0.4226\).

**Final answer**

\[ h(n) = (2(\sqrt{3}-1) + o(1))n \quad\text{(conjecturally)} \]
