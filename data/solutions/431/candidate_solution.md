This is **open**.

In modern language your question asks whether the prime set $P$ is **asymptotically a sumset**, i.e. whether there exist sets (A,B) (in particular, infinite, and with more than one element each) such that the **symmetric difference**
[
P \triangle (A+B)
]
is finite, where (A+B={a+b:a\in A,\ b\in B}). This is exactly **Ostmann’s “inverse Goldbach problem”** (also called the *inverse Goldbach conjecture*), and it is still unsolved; a negative answer is generally expected. 

What *is* known are strong necessary conditions. For example, Elsholtz–Harper proved that if such an asymptotic decomposition (P\sim A+B) exists, then both $A$ and $B$ must be extremely thin, with counting functions satisfying [[nomath]](for all sufficiently large $x$)[[/nomath]]
[
\frac{x^{1/2}}{\log x\log\log x}\ \ll\ A(x)\ \ll\ x^{1/2}\log\log x,
]
and the same bounds for $B(x)$, where (A(x)=|{a\in A:a\le x}|). 

Also, the **ternary** analogue *is* settled: there do **not** exist (A_1,A_2,A_3) with (|A_i|>1) such that (A_1+A_2+A_3) agrees with the primes from some point on. 

Finally, there is an interesting related result if one changes the problem: if one allows **signed primes** (positive and negative primes) and assumes a strong “prime $k$-tuple” hypothesis, then Ruzsa shows that the signed primes ({|p|>3}) *can* be realized exactly as a sumset $A+B$ for infinite (A,B\subset\mathbb Z). This does **not** resolve the original “positive primes” question, but it shows the situation changes in that setting. 
