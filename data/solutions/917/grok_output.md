# Grok Response for Problem 917

**Problem 917**

Let \(k \geq 4\) and let \(f_k(n)\) be the maximum number of edges in an \(n\)-vertex graph \(G\) with \(\chi(G) = k\) such that \(\chi(G - e) = k-1\) for every edge \(e \in E(G)\). (Such a graph is called *edge-critical* for chromatic number \(k\).) The questions are whether \(f_k(n) \gg_k n^2\) (i.e., whether there exists \(c_k > 0\) such that \(f_k(n) \geq c_k n^2\) for all sufficiently large \(n\)), whether \(f_6(n) \sim n^2/4\), and more generally whether
\[
f_k(n) \sim \frac12 \Bigl(1 - \frac{1}{\lfloor k/3 \rfloor}\Bigr) n^2
\]
for \(k \geq 6\).

The conjectured asymptotic for \(k \geq 6\) is equivalent to
\[
f_k(n) \sim \operatorname{ex}(n, K_r), \qquad r = \lfloor k/3 \rfloor + 1,
\]
where \(\operatorname{ex}(n, K_r)\) is the Turán number (the maximum edges in a \(K_r\)-free graph on \(n\) vertices). For \(k=6\) this gives \(r=3\) and \(\operatorname{ex}(n, K_3) = \lfloor n^2/4 \rfloor\), matching the second question. For \(k=4,5\) one has \(\lfloor k/3 \rfloor =1\), so the conjectured density coefficient is zero (i.e., \(f_k(n) = o(n^2)\)).

To investigate, fix \(r = k-1 \geq 3\) and let \(\mathcal{C}\) be the set of all functions \(c: V(G) \to [r]\) (so \(|\mathcal{C}| = r^n\)). For each \(c \in \mathcal{C}\) let
\[
X(c) = |\{e \in E(G) : c \text{ is constant on the endpoints of } e\}|
\]
be the number of monochromatic edges of \(G\) under \(c\). Since \(\chi(G) = k = r+1 > r\), \(G\) admits no proper \(r\)-coloring, so if \(a_j = |\{c : X(c) = j\}|\) then \(a_0 = 0\).

Because \(\chi(G-e) = r\) for each \(e\), for every \(e \in E(G)\) there exists at least one \(c\) such that \(X(c) = 1\) and the unique monochromatic edge of \(G\) under \(c\) is precisely \(e\). (In any proper \(r\)-coloring of \(G-e\) the endpoints of \(e\) must receive the same color; otherwise the coloring would be proper for \(G\).) Moreover, a single \(c\) can witness *at most* one edge: if \(X(c) = 1\) with unique monochromatic edge \(e\), then \(c\) cannot witness any other edge. Thus if \(m = |E(G)|\) we have \(a_1 \geq m\).

Now count in two ways. For a fixed edge \(e=uv\), the number of \(c\) with \(c(u)=c(v)\) is exactly \(r^{n-1}\) (choose the common color in \(r\) ways, then color the remaining \(n-2\) vertices freely). Hence
\[
\sum_{c \in \mathcal{C}} X(c) = m \cdot r^{n-1}.
\]
For any two distinct edges \(e,f\) (whether or not they share a vertex), the number of \(c\) under which both are monochromatic is exactly \(r^{n-2}\): the endpoints of \(e\) and \(f\) are forced to at most two common colors (or one if \(e,f\) share a vertex), which can be chosen in \(r(r-1)\) or \(r\) ways respectively, but in both cases the total is \(r^{n-2}\). Therefore
\[
\sum_{c \in \mathcal{C}} X(c)(X(c)-1) = m(m-1) \cdot r^{n-2}.
\]
Let \(N = r^n\), \(\alpha = a_1/N\), \(\lambda = 1 - \alpha\) (so \(\lambda\) is the fraction of colorings with \(X(c) \geq 2\)), and let \(\gamma\) (resp. \(\delta\)) be the average of \(X(c)\) (resp. \(X(c)(X(c)-1)\)) over those colorings with \(X(c) \geq 2\). Then
\[
\mu := \frac{m}{r} = \alpha + \gamma\lambda = (1-\lambda) + \gamma\lambda,
\]
and
\[
\frac{m(m-1)}{r^2} = \delta\lambda \implies \mu \approx \sqrt{\delta\lambda}.
\]
Since \(\operatorname{Var}(X) \geq 0\) over the colorings with \(X \geq 2\), we have \(\delta = \mathbb{E}[X(X-1)] \geq \gamma^2 - \gamma\) (with equality if all such \(X(c)\) are equal). Thus
\[
(1 - \lambda + \gamma\lambda)^2 \geq (\gamma^2 - \gamma)\lambda
\]
must hold for some \(\gamma \geq 2\) and \(\lambda \in (0,1]\). The constraint \(a_1 \geq m\) is automatically satisfied for large \(n\) whenever \(\alpha > 0\), since \(N\) is exponential while \(m = O(n^2)\).

These relations are consistent with \(m = \Theta(n^2)\) (average \(X(c) = \Theta(n^2)\) is possible if color classes are size \(\Theta(n)\) and \(G\) has constant density). However, they do not rule out positive density, nor do they force the conjectured Turán densities. Tighter bounds require exploiting the structure \(X(c) = \sum_{i=1}^r e_G(S_i)\) where \(\{S_1,\dots,S_r\}\) is the partition induced by \(c\). A coloring with \(X(c)=1\) has all but one part independent in \(G\), and exactly one part induces a single edge. Thus \(G\) admits many "nearly \(r\)-partite" representations (all but one part independent), one for each edge. This severely constrains the global edge distribution if \(m = \Theta(n^2)\), but optimizing the partition counts while maintaining \(\chi(G)=r+1\) and \(a_0=0\) appears intractable with the above moments alone. Higher-moment counts or assumptions on induced densities in large sets (e.g., via Turán's theorem inside color classes) are needed for a sharp upper bound, but lead to no immediate contradiction with the conjectured densities.

For a matching lower bound, note that odd cycles are 3-edge-critical with \(\Theta(n)\) edges. Hajós-type constructions combining such cycles can produce \(k\)-edge-critical graphs, but standard versions yield only \(O(n)\) or \(o(n^2)\) edges for fixed \(k \geq 4\). Blow-ups of odd cycles produce \(\Theta(n^2)\) edges and chromatic number 3, but are typically not edge-critical (removing an edge from a large complete bipartite link between blown-up vertices leaves many odd cycles intact). Modified constructions replacing edges by odd wheels or Mycielski gadgets on dense base graphs also fail to make *every* edge critical while achieving the Turán densities \(\operatorname{ex}(n,K_r)\). Random graphs of constant density have chromatic number \(\omega(1)\) and are insensitive to single edge deletions. Thus no construction achieving \(\Omega_k(n^2)\) (let alone the conjectured densities) is apparent.

Since the counting arguments yield necessary conditions on the distribution of \(X(c)\) but no outright contradiction with (or confirmation of) positive quadratic density for \(k \geq 4\), and since no matching construction or sharp upper bound is derivable from the moments, the conjectures remain open. After extensive analysis of the witness colorings, double counting, variance bounds, and structural constraints from near-\(r\)-colorings, I could not resolve any of the three questions.

**Final Answer**

I could not solve it.
