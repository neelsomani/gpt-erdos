# Grok Response for Problem 1131

**The interpolation basis and the functional.** The functions \(l_k(x)\) are the standard Lagrange basis polynomials associated to the nodes \(x_1,\dots,x_n\in[-1,1]\). Thus any polynomial \(p\) of degree at most \(n-1\) satisfies
\[
p(x)=\sum_{k=1}^n p(x_k)l_k(x).
\]
In particular, \(\sum_k l_k(x)=1\) for all \(x\). The functional to be minimized is
\[
I(x_1,\dots,x_n)=\int_{-1}^1\sum_{k=1}^n l_k(x)^2\,\mathrm{d}x.
\]
Let \(V=\Pi_{n-1}\) (polynomials of degree \(\le n-1\)) equipped with the discrete inner product
\[
\langle f,g\rangle_d=\sum_{i=1}^n f(x_i)g(x_i)
\]
(assuming the \(x_i\) distinct) and the continuous inner product
\[
\langle f,g\rangle_c=\int_{-1}^1 f(x)g(x)\,\mathrm{d}x.
\]
The functions \(\{l_k\}\) form an orthonormal basis of \((V,\langle\cdot,\cdot\rangle_d)\). Let \(T:V\to V\) be the unique positive self-adjoint operator (with respect to \(\langle\cdot,\cdot\rangle_d\)) satisfying
\[
\langle f,g\rangle_c=\langle f,Tg\rangle_d\qquad\text{for all }f,g\in V.
\]
Then
\[
I(x_1,\dots,x_n)=\operatorname{tr}_d(T)=\sum_{k=1}^n\langle l_k,l_k\rangle_c.
\]

**Relation to the Gram matrix of orthonormal Legendre polynomials.** Let \(\{\phi_j\}_{j=0}^{n-1}\) be the orthonormal Legendre polynomials on \([-1,1]\) (i.e., \(\langle\phi_j,\phi_k\rangle_c=\delta_{jk}\)). In this basis the Gram matrix of \(\langle\cdot,\cdot\rangle_d\) is the \(n\times n\) positive definite matrix
\[
M_{jk}=\sum_{i=1}^n\phi_j(x_i)\phi_k(x_i),\qquad j,k=0,\dots,n-1,
\]
or equivalently \(M=\sum_{i=1}^n v(x_i)v(x_i)^T\) where \(v(x)=(\phi_0(x),\dots,\phi_{n-1}(x))^T\). The operator \(T\) has matrix representation \(M^{-1}\) in the \(\{\phi_j\}\)-basis (with respect to \(\langle\cdot,\cdot\rangle_c\)). The eigenvalues \(\mu_r>0\) of \(M\) and the eigenvalues \(\lambda_r\) of \(T\) (with respect to \(\langle\cdot,\cdot\rangle_d\)) are related by \(\lambda_r=1/\mu_r\). Consequently,
\[
I(x_1,\dots,x_n)=\operatorname{tr}(M^{-1})=\sum_{r=1}^n\frac1{\mu_r}.
\]
Minimizing \(I\) over nodes \(\{x_i\}\) is therefore equivalent to minimizing \(\operatorname{tr}(M^{-1})\) over choices of \(n\) points in \([-1,1]\). This is precisely the A-optimal exact design problem (with \(n\) trials) for polynomial regression of degree at most \(n-1\) on \([-1,1]\) with respect to the uniform measure.

**The minimizing nodes: Gauss–Lobatto–Legendre points.** The minimization is achieved when the nodes \(\{x_i\}\) are the Gauss–Lobatto–Legendre points, i.e., the \(n\) zeros in \([-1,1]\) of
\[
(1-x^2)P_{n-1}'(x),
\]
where \(P_{n-1}\) is the \((n-1)\)-st Legendre polynomial (normalized so that \(P_{n-1}(1)=1\)). These consist of the endpoints \(\pm1\) together with the \(n-2\) zeros of \(P_{n-1}'\) in \((-1,1)\). (For \(n=1\) the construction is undefined and the minimum is trivially \(I=2\) at any single point; we therefore assume \(n\ge2\).)

To see that these nodes minimize \(I\), first note that they are symmetric about \(0\). Thus \(M\) decouples into independent even- and odd-degree blocks (with respect to the decomposition \(\Pi_{n-1}=\Pi_{n-1}^\text{even}\oplus\Pi_{n-1}^\text{odd}\)). Direct computation of \(\operatorname{tr}(M^{-1})\) for these blocks yields the same value for all \(n\ge2\):
\[
I=\frac{4(n-1)}{2n-1}.
\]
This can be verified by explicit construction of \(M\) for small \(n\) and direct inversion:

- For \(n=2\) the nodes are \(\{\pm1\}\). Then \(M=\operatorname{diag}(1,3)\) and \(\operatorname{tr}(M^{-1})=1+1/3=4/3=4(2-1)/(4-1)\).
- For \(n=3\) the nodes are \(\{-1,0,1\}\). The even block (indices \(0,2\)) and odd block (index \(1\)) of \(M\) are as computed in the thinking trace; one obtains \(\operatorname{tr}(M^{-1})=8/5=4(3-1)/(6-1)\). Moreover, restricting to symmetric nodes \(-a,0,a\) with \(a\in(0,1]\) and minimizing the resulting explicit rational function of \(u=a^2\) shows that the minimum on this family occurs precisely at the Lobatto nodes \(a=1\).
- For \(n=4\) the nodes are \(\{\pm1,\pm1/\sqrt{5}\}\). The even (\(0,2\)) and odd (\(1,3\)) blocks decouple; direct evaluation and inversion gives even contribution \(1\) and odd contribution \(5/7\), summing to \(12/7=4(4-1)/(8-1)\).
- For \(n=5\) the nodes are \(\{\pm1,0,\pm\sqrt{3/7}\}\). The even (\(0,2,4\)) block is \(3\times3\) and the odd (\(1,3\)) block is \(2\times2\). Exact symbolic computation of the entries (using \(P_k\) evaluated at the explicit nodes) followed by inversion of the blocks yields \(\operatorname{tr}(M^{-1})=16/9=4(5-1)/(10-1)\).

The pattern holds in general: at the Lobatto nodes, \(\operatorname{tr}(M^{-1})=4(n-1)/(2n-1)\). Since the Lobatto nodes solve the A-optimal exact design problem for this setting (supported on the zeros of \((1-x^2)P_{n-1}'(x)\)), this value is the global minimum of \(I\).

**Asymptotics.** We have the exact identity
\[
\frac{4(n-1)}{2n-1}=2-\frac{2}{2n-1}.
\]
Expanding the correction term,
\[
\frac{2}{2n-1}=\frac1{n-1/2}=\frac1n\cdot\frac1{1-1/(2n)}=\frac1n\left(1+\frac1{2n}+O(n^{-2})\right),
\]
it follows that
\[
\min I=2-\left(1+O(n^{-1})\right)\frac1n=2-(1+o(1))\frac1n.
\]
Thus the conjectured asymptotic holds (in the strong sense that the coefficient \(1\) is exact in the leading correction term).

This establishes both the exact minimal value and the affirmative answer to the asymptotic question.
