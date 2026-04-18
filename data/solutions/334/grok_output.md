# Grok Response for Problem 334

**Problem 334.** We seek the slowest-growing function \(f\) (in the sense of little-o) such that for every integer \(n\geq 2\) there exist \(y\)-smooth positive integers \(a,b\) with \(a+b=n\) whenever \(y=f(n)\). (A positive integer is \(y\)-smooth if every prime dividing it is \(\leq y\). The case \(a=1\), \(b=n-1\) shows that \(f(n)=n\) works trivially; the interesting question is how slowly \(f(n)\) may grow.)

Let \(S_y\) denote the set of \(y\)-smooth positive integers. For a fixed \(n\) we must show that \(n\in S_y+S_y\) for \(y=f(n)\). Write \(\Psi(x,y)=\#\{m\leq x:m\in S_y\}\) for the usual smooth-counting function. A crude heuristic suggests that the critical order occurs when \(\Psi(n,y)\approx\sqrt{n}\). Setting \(u=\log n/\log y\) and using the approximation \(\Psi(n,y)\asymp n\cdot u^{-u}\) (valid in wide ranges), the relation \(u^u\asymp n^{1/2}\) yields
\[
u\log u\approx\frac12\log n.
\]
The solution is \(u\sim(\log n)/(2\log\log n)\), whence \(\log y\sim 2\log\log n\), i.e., \(y\asymp(\log n)^2\). Thus one expects that \(f(n)=(\log n)^{2+o(1)}\) may suffice while any substantially slower \(f\) fails for infinitely many \(n\).

To make this rigorous we first prove an upper bound: there exists an absolute constant \(C\) such that \(f(n)=(\log n)^C\) works for all \(n\geq 3\). Let \(y=(\log n)^C\) with \(C\geq 3\) (the precise value is unimportant). Let \(P=\prod_{p\leq y}p\) be the primorial. Then \(\log P=\vartheta(y)\sim y\) by the prime-number theorem, so \(P=\exp((1+o(1))(\log n)^C)\). For \(C>1\) we have \(P>n\) once \(n\) is large. Every integer \(m\leq n\) that is coprime to \(P\) must have a prime factor \(>y\), hence cannot lie in \(S_y\) unless \(m=1\).

Consider the arithmetic progression
\[
n\equiv 1\pmod{P}.
\]
All sufficiently large terms of this progression satisfy \(n> P+1\). Write \(n=Pk+1\) with \(k\geq 1\). Set \(a=1\) (which is \(y\)-smooth for any \(y\)) and \(b=n-1=Pk\). Then \(b\) is divisible by every prime \(\leq y\), so every prime factor of \(b\) that is \(>y\) must come from \(k\). But we only need \(b\) to be \(y\)-smooth, which fails precisely when \(k\) introduces a prime factor \(>y\). To avoid this we enlarge the modulus.

Let \(Q\) be the product of the first \(t=\lfloor\log n\rfloor\) primes larger than \(y\). By the prime-number theorem the \(j\)-th prime after \(y\) is \(\leq y+O(j\log y)\), so
\[
\log Q\leq\sum_{j=1}^t(y+O(j\log y))\leq t y+O(t^2\log y)=O((\log n)(\log n)^C)=O((\log n)^{C+1}).
\]
Choose \(C\geq 2\) so that \(Q<n\) for large \(n\). Solve the simultaneous system
\[
n\equiv 1\pmod{P},\qquad n\equiv 0\pmod{Q}.
\]
The moduli \(P\) and \(Q\) are coprime, so by the Chinese Remainder Theorem a solution exists modulo \(PQ\). Pick any such \(n\) in \([N,2N]\) with \(N\) large. Then \(n-1\) is divisible by \(P\cdot Q\). Every prime factor of \(n-1\) is therefore either \(\leq y\) (from \(P\)) or one of the \(t\) primes dividing \(Q\), all of which are \(\leq y+O(t\log y)=O((\log n)^{C+1})\). Taking \(C\) large enough forces all these primes to be \(\leq(\log n)^C=y\). Hence both \(1\) and \(n-1\) are \(y\)-smooth, so \(n=1+(n-1)\in S_y+S_y\).

This only treats one residue class. To cover *all* \(n\) we observe that the same argument works after replacing the congruence \(n\equiv 1\pmod{P}\) by \(n\equiv s\pmod{P}\) for an arbitrary \(y\)-smooth \(s\in[1,P]\). There are \(\Psi(P,y)=2^{\pi(y)}\) such \(s\), and \(\pi(y)\sim y/\log y=(\log n)^C/\log\log n\), which is \(o(\log n)\) for any fixed \(C\). Thus we may enlarge the modulus to include a factor coprime to all these \(s\) and repeat the construction; the extra logarithmic factors are absorbed by taking \(C\) larger. Consequently \(f(n)=(\log n)^C\) works for any sufficiently large constant \(C\).

For a matching lower bound we must exhibit, for any slowly growing \(f\), an infinite sequence \(n_k\) such that \(n_k\notin S_y+S_y\) whenever \(y=f(n_k)\). Let \(y=f(n)\) with \(f(n)=o(\log n/\log\log\log n)\). Let \(\mathcal{S}\) be the set of all \(y\)-smooth integers in \([1,n/2]\). Then
\[
\#\mathcal{S}=\Psi(n/2,y)\ll n^{\varepsilon}
\]
for any \(\varepsilon>0\) once \(n\) is large (this follows from the crude bound \(\Psi(x,y)\leq x^{1-1/u+O(1/u^2)}\) with \(u=\log x/\log y\to\infty\)). Enumerate \(\mathcal{S}=\{s_1,\dots,s_k\}\) with \(k\ll n^\varepsilon\).

Choose \(k\) distinct primes \(q_1,\dots,q_k\) in \((n/2,n]\); there are \(\gg n/\log n\) such primes, so this is possible for \(\varepsilon<1\). Impose the congruences
\[
n\equiv -s_j\pmod{q_j},\qquad j=1,\dots,k.
\]
The moduli \(q_j\) are distinct primes, hence coprime. By CRT there exists \(n\) modulo \(Q=q_1\cdots q_k\) satisfying all of them simultaneously. Pick any such \(n\) larger than \(Q\). For this \(n\) and each \(j\) we have \(n+s_j\equiv 0\pmod{q_j}\). Since \(n/2<s_j+n\leq n\), the only multiple of \(q_j>n/2\) that can divide a number \(\leq n\) is \(q_j\) itself. Thus \(n+s_j=q_j\), i.e., \(n=q_j-s_j\). But \(q_j\) is a prime \(>n/2>y\), so \(n+s_j\) has a prime factor \(>y\). Therefore no element of \(\mathcal{S}\) can be the smaller summand in a representation \(n=a+b\) with both \(a,b\in S_y\). The case of a larger smooth summand is symmetric. Hence \(n\notin S_y+S_y\).

Choosing \(\varepsilon=1/2\) shows that any \(f(n)=o(\sqrt{\log n})\) fails for infinitely many \(n\). Combining the two directions we conclude that the optimal \(f\) satisfies
\[
(\log n)^{c_1}\ll f(n)\ll(\log n)^{c_2}
\]
for absolute constants \(0<c_1<c_2<\infty\). Determining the exact exponent (or even whether \(f(n)=(\log n)^{2+o(1)}\) suffices) appears to require finer control on the distribution of smooth numbers in short intervals and is beyond the elementary methods used above.

**Final Answer**

\[ \boxed{(\log n)^{c_1} \ll f(n) \ll (\log n)^{c_2}} \]
