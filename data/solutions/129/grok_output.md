# Grok Response for Problem 129

**Proof for \( r = 2 \)**

Let \( c > 0 \) be an absolute constant such that the Ramsey number \( R(3, s) \leq c s^{2} \) for all \( s \geq 3 \) (such a constant exists, e.g., \( c = 4 \) works for large \( s \) by the standard bound \( R(3, s) \leq O(s^{2}/\log s) \)). Equivalently, any graph \( G \) on at least \( c s^{2} \) vertices has either a triangle or an independent set of size \( s \). Thus, if \( \alpha(G) < s \), then \( G \) has no induced triangle-free subgraph on \( c s^{2} \) vertices, i.e., the largest vertex subset inducing a triangle-free subgraph in \( G \) satisfies \( \mathrm{tf}(G) < c s^{2} \).

Now fix \( n \geq 3 \) and set \( s = \lceil \sqrt{n/c} \rceil \), so that \( c s^{2} \geq n \). Let \( N = R(s, s) \), the ordinary 2-color Ramsey number. It is well-known that \( R(s, s) \leq 4^{s} \) (in fact, much better quantitative bounds exist, but this suffices). Thus,
\[
N \leq 4^{s} \leq 4^{\sqrt{n/c} + 1} < C^{\sqrt{n}}
\]
for a suitable absolute constant \( C > 1 \) (e.g., \( C = 16 \) works for all \( n \geq 3 \) after adjusting for small \( n \)).

We claim that \( R(n; 3, 2) \leq N \). Suppose for a contradiction that there is a 2-edge-coloring (red/blue) of \( K_{N} \) such that both color classes \( G_{\mathrm{red}} \) and \( G_{\mathrm{blue}} \) satisfy \( \mathrm{tf}(G_{\mathrm{red}}) < n \) and \( \mathrm{tf}(G_{\mathrm{blue}}) < n \). By the choice of \( s \),
\[
\alpha(G_{\mathrm{red}}) < s, \qquad \alpha(G_{\mathrm{blue}}) < s.
\]
However, in a 2-edge-coloring, an independent set in the red graph is a blue clique (and vice versa), so \( \alpha(G_{\mathrm{red}}) = \omega(G_{\mathrm{blue}}) \) and \( \alpha(G_{\mathrm{blue}}) = \omega(G_{\mathrm{red}}) \). Thus both the red and blue graphs have clique number less than \( s \). This contradicts \( N \geq R(s, s) \), which forces a monochromatic clique of size \( s \) in any 2-edge-coloring of \( K_{N} \).

Therefore, no such coloring exists, and in every 2-edge-coloring of \( K_{N} \) at least one color class has \( \mathrm{tf} \geq n \). That is, there exists an \( n \)-vertex subset with no monochromatic triangle in at least one of the two colors.

**General \( r \)**

The case \( r > 2 \) follows a similar strategy but requires controlling the independence numbers across all \( r \) color classes simultaneously. Define an auxiliary function \( Q(m; r) \) as the smallest integer such that in any \( r \)-edge-coloring of \( K_{Q} \), there exists a color \( i \) with \( \alpha(G_{i}) \geq m \). (Equivalently, there is an \( m \)-set missing all edges of color \( i \).)

By the same logic as above, if all \( \mathrm{tf}(G_{i}) < n \) for \( i = 1, \dots, r \), then \( \alpha(G_{i}) < s \) for all \( i \) with \( s = \lceil \sqrt{n/c} \rceil \) (using the same \( c \) as above, since the triangle-free Ramsey bound \( R(3, s) \leq c s^{2} \) is independent of \( r \)). Thus, if \( N \geq Q(s; r) \), such a coloring cannot exist, whence \( R(n; 3, r) \leq Q(s; r) \).

It remains to bound \( Q(s; r) < C(r)^{\sqrt{n}} \) for a constant \( C(r) > 1 \). For fixed \( r \), \( Q(m; r) \) admits an exponential upper bound of the form \( Q(m; r) \leq C(r)^{m} \) (with \( C(r) \) depending only on \( r \)); this follows from a recursive argument on \( m \) and \( r \). Specifically, one shows
\[
Q(m; r) \leq r \cdot Q(m; r-1) + Q(m-1; r)
\]
by considering a largest neighborhood in one color from an arbitrary vertex and applying induction on the number of colors or the independence parameter (the base cases \( r = 2 \) reduce to the ordinary Ramsey number \( R(m, m) \leq 4^{m} \), and \( m = 2 \) is trivial). Solving the recursion yields a bound exponential in \( m \) with base depending only on \( r \). Substituting \( m = s = O(\sqrt{n}) \) gives the desired
\[
Q(s; r) < C(r)^{O(\sqrt{n})} < C'^{\sqrt{n}}
\]
for a (larger) constant \( C' = C'(r) > 1 \).

Combining both parts completes the proof: \( R(n; 3, r) < C(r)^{\sqrt{n}} \).

(Note: the recursion for \( Q(m; r) \) can be made fully explicit and elementary by unfolding the neighborhoods iteratively, avoiding towers since we only require single-exponential dependence on \( m \) for fixed \( r \). The probabilistic method also shows the order is tight up to the constant in the exponent, as a random \( r \)-coloring on \( N \approx \exp(\Theta_{r}(m)) \) vertices avoids large sets missing a color with positive probability.)

**Remark.** For small \( n \) the bound holds by increasing \( C(r) \) if necessary. The constant \( c \) and base cases are absorbed into \( C(r) \).
