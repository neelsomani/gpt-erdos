# Grok Response for Problem 28

**Problem 28.** We work throughout in \(\mathbb{N}=\{1,2,3,\dots\}\). Let \(1_A:\mathbb{N}\to\{0,1\}\) be the indicator function of a set \(A\subseteq\mathbb{N}\). Its convolution with itself is
\[
(1_A\ast 1_A)(n)=\sum_{k=1}^{n-1}1_A(k)1_A(n-k)=r_A(n),
\]
the number of ordered pairs \((a,b)\in A\times A\) with \(a+b=n\) (allowing \(a=b\)). The hypothesis is that there exists \(N_0\) such that every integer \(n>N_0\) admits at least one such representation, i.e.,
\[
\{n\in\mathbb{N}:r_A(n)=0\}\quad\text{is finite}.
\]
The claim is that necessarily
\[
\limsup_{n\to\infty}r_A(n)=\infty.
\]

Assume for contradiction that \(r_A(n)\le K\) for some fixed \(K<\infty\) and all \(n>N_1\). By enlarging \(N_1\) if necessary we may suppose \(N_1\ge N_0\), so that
\[
1\le r_A(n)\le K\qquad\text{for all }n>N_1.
\]
Let \(A(x)=\# (A\cap[1,x])\) be the counting function of \(A\). Summing the representation function up to \(X>2N_1\) gives the exact identity
\[
\sum_{n=1}^X r_A(n)=\sum_{\substack{a,b\in A\\ a+b\le X}}1=\sum_{a\in A,\,a\le X}A(X-a).
\]
The left-hand side is at least \(X-N_1\) (since all but at most \(N_1\) terms are \(\ge1\)) and at most \(KX\) (by the assumed upper bound). Thus
\[
X-N_1\le\sum_{a\in A,\,a\le X}A(X-a)\le KX.
\]
In particular the sum on the right is \(\asymp X\).

Write \(A=\{a_1<a_2<\dots\}\) with \(a_k\to\infty\). Because the gaps \(a_{k+1}-a_k\) must be unbounded (otherwise \(A\) would have positive lower density and the sum above would be \(\gg X^2\), contradicting the upper bound \(KX\)), there exist arbitrarily large indices \(k\) for which the gap \(g_k=a_{k+1}-a_k\) is large. Fix such a \(k\) with \(a_k>N_1\) and \(g_k>2K+2\). Consider the integers in the interval
\[
I_k=[2a_k+1,\,a_k+a_{k+1}-1]=[2a_k+1,\,2a_k+g_k-1].
\]
Every \(n\in I_k\) can be written as \(n=a_k+m\) with \(1\le m\le g_k-1\). For \(n\) to have a representation \(n=a+b\) with \(a,b\in A\), at least one of \(a\) or \(b\) must lie in \(\{a_1,\dots,a_k\}\) (otherwise both are \(\ge a_{k+1}\), forcing \(n\ge 2a_{k+1}=2a_k+2g_k>2a_k+g_k-1\)). Thus the possible representations of elements of \(I_k\) are of the form
\[
a_i+(n-a_i)\qquad\text{with }i\le k\text{ and }n-a_i\in A.
\]
There are only \(k\) choices for \(a_i\). For each fixed \(i\), the condition \(n-a_i\in A\) can hold for at most \(K\) values of \(n\) in any interval of length \(g_k-1\), because if it held for \(K+1\) distinct \(n\)'s then those \(n\)'s would all have the same first summand \(a_i\) and distinct second summands, contradicting \(r_A\le K\). Summing over the \(k\) possible \(a_i\) shows that at most \(kK\) integers in \(I_k\) can be represented using summands \(\le a_k\). But \(|I_k|=g_k-1>2K\), and if \(k\) is large enough that \(kK< g_k-1\) we obtain that some integer in \(I_k\) has no representation at all, contradicting the hypothesis that all sufficiently large integers lie in \(A+A\).

It remains only to check that such a \(k\) exists. Since gaps are unbounded we may choose \(k\) with \(g_k>2K+2\). The counting function satisfies \(A(a_k)=k\), and the earlier integral estimate forces \(k=A(a_k)=o(a_k)\) (otherwise the double sum would exceed \(K\cdot 2a_k\)). Thus for large enough \(k\) we have \(kK<g_k-1\), and the preceding counting argument applies. This contradiction shows that the assumption \(\sup r_A(n)<\infty\) is impossible.

The argument above contains a gap: the bound “at most \(K\) values of \(n\) per first summand” is only valid if the second summands \(n-a_i\) are forced to be distinct across different \(n\), which they are, but we must also ensure that no element of \(I_k\) receives a representation from two different small summands that would allow overcounting to cancel the deficit. A more careful double-counting, keeping track of the precise multiplicity, is needed to close this loophole; after several attempts the required uniform control on the error terms resisted simplification. Consequently I could not repair the proof to a fully rigorous standard.
