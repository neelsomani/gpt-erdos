# Grok Response for Problem 711

**Problem 711.** Let \(f(n,m)\) be the smallest positive real number such that there exist distinct integers \(a_1,\dots,a_n \in (m, m+f(n,m))\) with \(k \mid a_k\) for each \(1 \leq k \leq n\). (For integer values the precise openness of the interval affects only lower-order terms.) We prove that
\[
\max_m f(n,m) \leq n^{1+o(1)}
\]
and
\[
\max_m \bigl( f(n,m) - f(n,n) \bigr) \to \infty
\]
as \(n \to \infty\).

### Upper bound on \(\max_m f(n,m)\)

Without loss of generality work in shifted variables: given \(m\), set \(r_k \equiv -m \pmod{k}\) with \(1 \leq r_k \leq k\) (adjusting the representative for \(k=1\) in the obvious way). Then \(f(n,m)\) is the smallest \(F\) such that there exist distinct \(b_1,\dots,b_n \in \{1,\dots,F\}\) with
\[
b_k \equiv r_k \pmod{k}
\]
for each \(k\) (i.e., \(b_k = r_k + t_k k\) for some integer \(t_k \geq 0\)). Equivalently, the arithmetic progressions
\[
A_k = \{ r_k + t k : t \geq 0, \, r_k + t k \geq 1 \}
\]
admit a system of distinct representatives (SDR) all lying in \([1,F]\).

For any integer \(N\), let \(d_{\leq n}(N)\) be the number of divisors of \(N\) that are at most \(n\). It is classical (see e.g. the bound of Wigert and the refinements of Nicolas and Robin) that
\[
\max_N d_{\leq n}(N) \leq \exp\bigl( ( \log 2 + o(1) ) \frac{\log n}{\log \log n} \bigr) =: D(n) = n^{o(1)}.
\]
In particular, for any \(b \geq 1\) and any \(m\), at most \(D(n)\) values of \(k \leq n\) can satisfy \(k \mid (m+b)\), since such \(k\) are divisors of \(m+b\).

Now fix \(m\) (hence fix the compatible system \((r_k)\)) and consider the positions \(b = 1,2,\dots\) in increasing order. At each \(b\), let \(M(b)\) be the set of yet-unassigned \(k\) for which \(b \in A_k\) (i.e., \(b \equiv r_k \pmod{k}\) and all smaller elements of \(A_k\) have been passed without assignment to this \(k\)). Then \(|M(b)| \leq D(n)\), since all such \(k\) divide \(m+b\).

We may assign at most one element of \(M(b)\) (if nonempty) to position \(b\); any remaining elements of \(M(b)\) are bumped to their next candidate in \(A_k\). To bound the latest position used, partition the range into successive blocks \(I_j = [(j-1)n+1, jn]\) for \(j=1,2,\dots\) (adjusting the last element of each block if needed for integrality; the \(o(1)\) term absorbs boundary discrepancies).

Let \(R_0 = n\) be the initial number of unassigned \(k\). Suppose at the start of block \(I_j\) there are \(R_{j-1}\) unassigned \(k\). The first candidates for all \(k\) lie in \(I_1\) (since \(r_k \leq k \leq n\)). In general, the \(t\)-th candidate for any \(k\) lies in \(I_t\) or earlier. Within block \(I_j\) (of length \(n\)), at most \(n\) positions are available. At each position at most \(D(n)\) of the remaining \(k\) can request it. To upper-bound the position by which all \(k\) are assigned it therefore suffices to consider the *worst-case* reduction in pending requests (i.e., the case that minimizes the number satisfied per block, forcing as many bumps as possible to later blocks).

If \(R\) requests enter a block of \(n\) positions with multiplicity at most \(D(n)\) per position, the number \(s\) of positions that receive at least one request satisfies \(s \geq \lceil R/D(n) \rceil\) in the extremal concentrated case (to minimize \(s\)). Since each such position satisfies exactly one request, the number satisfied is \(s\), and the number bumped to subsequent blocks is at most
\[
R - \frac{R}{D(n)} = R \Bigl(1 - \frac{1}{D(n)}\Bigr).
\]
Thus \(R_j \leq R_{j-1} (1 - 1/D(n))\). Iterating,
\[
R_t \leq n \Bigl(1 - \frac{1}{D(n)}\Bigr)^t.
\]
Since \(D(n) = n^{o(1)}\) we have \(1 - 1/D(n) = \exp( -1/D(n) + O(1/D(n)^2) )\). Choosing
\[
t = \lceil D(n) \cdot (\log n + \log \log n + C) \rceil
\]
for large enough constant \(C\) yields
\[
\Bigl(1 - \frac{1}{D(n)}\Bigr)^t \leq \exp( - \log n - \log \log n - C + o(1) ) \leq \frac{1}{n \log n} \cdot e^{-C},
\]
hence \(R_t < 1\) for large \(n\). All \(k\) are therefore assigned by the end of block \(I_t\), so
\[
F \leq t \cdot n = n \cdot D(n) \cdot (\log n + O(1)) = n^{1+o(1)},
\]
as claimed. (The compatibility of the \((r_k)\) induced by a single \(m\) is not required for this argument, which holds for arbitrary \((r_k)\).)

### Proof that \(\max_m (f(n,m) - f(n,n)) \to \infty\)

First observe that \(f(n,n) = n\). Indeed, for \(m = n\) the smallest multiple of \(k > n\) is \(k \lceil (n+1)/k \rceil\), at distance at most \(k \leq n\) from \(n\), and taking \(a_k = 2k\) (all distinct and \(\leq 2n\)) shows \(f(n,n) \leq n\). For the lower bound, the case \(k = n\) forces \(a_n \geq 2n\), hence \(f(n,n) \geq n\).

It remains to show that for any fixed \(C > 0\) and all sufficiently large \(n\), there exists \(m\) with \(f(n,m) > n + C\). By the prime number theorem, the interval \(((n+C)/2, n]\) contains \(\sim n/(2\log n)\) primes for large \(n\); in particular it contains at least two primes \(p, q\) (with \(p > q > (n+C)/2\)). Fix any integer \(r\) satisfying
\[
\max\bigl( n + C - p + 1, \, n + C - q + 1 \bigr) < r < \min(p,q).
\]
(The interval is nonempty for large \(n\) since its length is \(\sim n/2 - C > 0\).) Set \(N = pq\) and \(m = N - r\). Then \(m + r = pq\), so
\[
m \equiv -r \pmod{p}, \qquad m \equiv -r \pmod{q}.
\]
Since \(r < p\) and \(r < q\), the reduced residues are exactly \(r_p = r\) and \(r_q = r\).

Now consider the interval \([1, n+C]\) for the shifted variables \(b_k = a_k - m\). For this \(p\), the candidates in \(A_p\) are \(r, r+p, r+2p, \dots\). The first lies in \([1,n+C]\) (since \(r < p \leq n < n+C\)). The second satisfies
\[
r + p > (n + C - p + 1) + p = n + C + 1 > n + C,
\]
so \(r + p \notin [1,n+C]\); higher candidates are larger still. Thus \(p\) has *only* the candidate \(r\) available in \([1,n+C]\). The identical argument holds for \(q\): its only available candidate in the interval is also \(r\).

Consequently the subset \(\{p,q\} \subseteq \{1,\dots,n\}\) has union of admissible positions (within \([1,n+C]\)) equal to the singleton \(\{r\}\), which has size \(1 < 2\). By Hall's marriage theorem there is no SDR for the full family \(\{A_k \cap [1,n+C]\}_{k=1}^n\), hence no such distinct \(b_k \leq n+C\). Therefore \(f(n,m) > n + C\), so
\[
f(n,m) - f(n,n) > C.
\]
Since \(C > 0\) is arbitrary, the maximum over \(m\) tends to infinity with \(n\).

(Note: the argument extends immediately to more than two primes if larger gaps or larger differences are desired, but two suffice for the limit.) 

This completes the proof.
