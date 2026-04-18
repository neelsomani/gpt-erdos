# Grok Response for Problem 572

**Lower bound on \(\mathrm{ex}(n; C_{2k})\) via the probabilistic method and the Lovász Local Lemma**

To show \(\mathrm{ex}(n; C_{2k}) \gg n^{1 + 1/k}\) for \(k \geq 3\), it suffices to exhibit (for all sufficiently large \(n\)) a graph on \(n\) vertices with \(\Omega(n^{1 + 1/k})\) edges containing no copy of \(C_{2k}\). We do this using the binomial random graph \(G \sim G(n, p)\) together with the symmetric Lovász Local Lemma (LLL). Recall the symmetric LLL: Let \(\mathcal{E}_1, \dots, \mathcal{E}_M\) be events in an arbitrary probability space, with \(\Pr(\mathcal{E}_i) \leq q\) for all \(i\) and with each \(\mathcal{E}_i\) mutually independent of all but at most \(D\) of the other events. If
\[
e \cdot q \cdot (D + 1) \leq 1,
\]
then \(\Pr(\bigcap_{i=1}^M \overline{\mathcal{E}}_i) > 0\).

Fix a constant \(c > 0\) (depending only on \(k\)) to be chosen sufficiently small later, and set
\[
p = c \, n^{1/k - 1}.
\]
(We assume \(n\) is large enough that \(p < 1\).) Let \(G \sim G(n, p)\). The expected degree of each vertex is \(\mu = p(n-1) \sim c n^{1/k}\).

Define the following *bad events*:
- For each possible sequence of \(2k\) distinct vertices that could form a \(C_{2k}\) (of which there are at most \(n^{2k}\)), let \(A_C\) be the event that all \(2k\) edges of this cycle are present in \(G\). Then
  \[
  \Pr(A_C) = p^{2k} \leq c^{2k} n^{2-2k}.
  \]
  Denote \(q_A := c^{2k} n^{2-2k}\).
- For each vertex \(v \in V(G)\), let \(B_v\) be the event that \(\deg_G(v) < \frac{c}{2} n^{1/k}\). By the Chernoff bound,
  \[
  \Pr(B_v) \leq \exp\left( -\frac{\mu}{8} \right) \leq \exp(-b n^{1/k}),
  \]
  where \(b = c/8 > 0\) (for large \(n\)). Denote \(q_B := \exp(-b n^{1/k})\).

We apply the LLL to the collection of all these events \(\{A_C\} \cup \{B_v\}\). To do so, we bound the dependency degrees.

The event \(A_C\) depends only on the presence/absence of its own \(2k\) edges. Thus:
- \(A_C\) is mutually independent of all \(A_{C'}\) whose edge sets are disjoint from that of \(C\). The number of \(C'\) sharing at least one edge with \(C\) is at most \(2k\) times the maximum number of \(C_{2k}\) through a fixed edge. The latter is \(O_k(n^{2k-2})\) (choose and order the remaining \(2k-2\) vertices and arrange them to complete the cycle in \(O_k(1)\) ways). Hence, \(A_C\) depends on at most \(D_A' = O_k(n^{2k-2})\) other \(A\)-events.
- \(A_C\) depends on a \(B_v\) only if one of the \(2k\) edges of \(C\) is incident to \(v\) (otherwise the edge sets are disjoint). This occurs for at most the \(2k\) vertices of \(C\), so \(O_k(1)\) such \(B_v\).

Overall, each \(A_C\) depends on at most \(D_A = O_k(n^{2k-2})\) other bad events. Thus,
\[
q_A (D_A + 1) = O_k(c^{2k} n^{2-2k} \cdot n^{2k-2}) = O_k(c^{2k}).
\]
Choose \(c > 0\) small enough (depending only on \(k\)) that \(e \cdot q_A (D_A + 1) < 1/2\).

Now consider a \(B_v\):
- \(B_v\) depends on an \(A_C\) only if \(C\) uses at least one edge incident to \(v\), i.e., if \(v \in C\). The number of such potential cycles through a fixed \(v\) is \(O_k(n^{2k-1})\) (choose and order the other \(2k-1\) vertices appropriately).
- \(B_v\) depends on every \(B_w\) (\(w \neq v\)), since the potential edge \(vw\) affects both degree indicators.

Thus, each \(B_v\) depends on at most \(D_B = O(n^{2k-1})\) other bad events. Then
\[
q_B (D_B + 1) = O(n^{2k-1} \exp(-b n^{1/k})).
\]
For \(k \geq 3 > 1\), the exponential decay dominates any polynomial growth, so for all sufficiently large \(n\) (depending on \(k, c\)), we have \(e \cdot q_B (D_B + 1) < 1/2\).

By the symmetric LLL, 
\[
\Pr(\text{none of the } A_C \text{ or } B_v \text{ occur}) > 0.
\]
Thus, there exists a graph \(G\) on \(n\) vertices with *no* copy of \(C_{2k}\) (no \(A_C\) occurs) in which *every* vertex has degree at least \(\frac{c}{2} n^{1/k}\) (no \(B_v\) occurs). Such a graph has at least
\[
\frac{1}{2} \cdot n \cdot \frac{c}{2} n^{1/k} = \frac{c}{4} n^{1 + 1/k}
\]
edges. Therefore,
\[
\mathrm{ex}(n; C_{2k}) \geq \frac{c}{4} n^{1 + 1/k} \gg n^{1 + 1/k},
\]
as required (where the implied constant depends only on \(k\)).

For small \(n\), the bound holds by increasing the implicit constant if necessary.

**Remark.** The same proof works for \(k=2\) (i.e., \(C_4\)), but the problem statement begins at \(k \geq 3\).

(Note: the choice of \(G(n,p)\) can be replaced by the configuration model for random regular graphs of degree \(\Theta(n^{1/k})\), with analogous calculations.)
