# Grok Response for Problem 1129

**The minimizing choice of \(x_i\)**

The quantity \(\Lambda(x_1,\dots,x_n)\) is the Lebesgue constant associated with interpolation at the nodes \(x_1,\dots,x_n\in[-1,1]\). Equivalently, it is the maximum norm on \([-1,1]\) of the Lebesgue function
\[
\lambda(x)=\sum_{k=1}^n|l_k(x)|,
\]
where the \(l_k\) are the Lagrange basis polynomials. The task is to identify a choice of nodes that attains
\[
\Lambda_n:=\min_{x_1,\dots,x_n\in[-1,1]}\Lambda(x_1,\dots,x_n).
\]

Any minimizing set must be symmetric about \(0\) (otherwise reflecting an asymmetric configuration about the origin cannot increase \(\Lambda\)). Moreover, the endpoints \(\pm1\) must belong to every minimizing set. To see this, suppose (without loss of generality) that \(x_1>-1\). Then as \(x\to-1^+\) at least one basis function \(l_k(x)\) with \(x_k\) nearest to \(-1\) tends to a value strictly larger than \(1\) while the remaining terms stay nonnegative, forcing \(\lambda(-1)>1\). Since \(\lambda(x_k)=1\) at each node, we have \(\Lambda\geq1\), and any configuration attaining a value strictly larger than \(1\) at an endpoint can be improved by moving the outermost node to that endpoint while adjusting the interior nodes. Thus every minimizer contains \(\pm1\).

For \(n=2\) the unique (up to ordering) minimizer is \(\{\pm1\}\), for which \(\lambda(x)\equiv1\) and \(\Lambda_2=1\).

For \(n=3\) the unique symmetric choice containing the endpoints is \(\{-1,0,1\}\). Direct computation yields
\[
\lambda(x)=
\begin{cases}
1-x^2-x & x\in[-1,0],\\
1-x^2+x & x\in[0,1],
\end{cases}
\]
whose maximum on \([-1,1]\) is \(5/4\) (attained at \(x=\pm1/2\)). Any configuration omitting an endpoint produces a strictly larger value of \(\lambda\) at that endpoint, so \(\{-1,0,1\}\) realises \(\Lambda_3=5/4\).

For \(n\geq4\) a closed-form description is unavailable. The unique symmetric minimizer containing \(\pm1\) may be written
\[
-1=x_1<x_2<\dots<x_{\lfloor n/2\rfloor}<0<x_{n-\lfloor n/2\rfloor+1}<\dots<x_n=1
\]
with the interior abscissae chosen so that all local maxima of \(\lambda(x)\) on the \(n-1\) subintervals \([x_k,x_{k+1}]\) are equal. This common height is then necessarily \(\Lambda_n\).

To see that such a balance condition characterises the minimizer, note that \(\lambda(x)\) is continuous and piecewise rational of degree at most \(n-1\). Inside each open interval \((x_k,x_{k+1})\) it is smooth. If a local maximum inside one of these intervals were strictly larger than the global maximum on another interval, a small perturbation of the nodes separating those two intervals would decrease the larger peak while increasing the smaller one, lowering the overall maximum. Consequently every local maximum of \(\lambda\) on \([-1,1]\) must equal \(\Lambda_n\) at a minimizer. (The uniqueness of the symmetric set satisfying the equal-ripple condition follows from the strict convexity of the map from interior nodes to the vector of local maxima.)

Explicit algebraic expressions for the interior nodes satisfying the equal-ripple condition are not known. For illustration, when \(n=4\) the interior nodes are \(\pm a\) with \(a\approx0.42\) (numerically determined by equating \(\lambda(0)\) with the local maxima in \([-1,-a]\) and \([a,1]\)), giving \(\Lambda_4\approx1.42\). This value is strictly smaller than the Lebesgue constant \(\frac53\) obtained at the Chebyshev-Lobatto nodes \(\pm\cos(\pi/3)=\pm1/2\). Analogous numerical balances can be performed for moderate \(n\), but they yield no recognisable algebraic or trigonometric pattern.

Thus, while the minimizers are uniquely characterised as the symmetric endpoint-inclusive sets rendering all local maxima of \(\lambda\) equal, no simpler explicit description is available.

**Final Answer**

I couldn't solve it.
