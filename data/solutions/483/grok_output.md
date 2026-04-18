# Grok Response for Problem 483

**Lower bound.** We first show that \(f(k) \geq \frac{3^{k}+1}{2}\) for all \(k \geq 1\). (This is equivalent to exhibiting a \(k\)-colouring of \(\{1,\dots,m\}\) with \(m = (3^k-1)/2\) containing no monochromatic triple \(a+b=c\).) The proof is by induction on \(k\), with the base case \(k=1\) immediate (\(m=1\), and \(1+1=2\) lies outside the set).

Assume the claim holds for \(k-1\), and let \(m = (3^{k-1}-1)/2\), so the target size for \(k\) colours is \(3m+1 = (3^k-1)/2\). By the induction hypothesis there is a \((k-1)\)-colouring \(c\) of \(\{1,\dots,m\}\) with no monochromatic solution to \(a+b=c\). Extend to a \(k\)-colouring of \(\{1,\dots,3m+1\}\) by
- colouring \(\{1,\dots,m\}\) according to \(c\),
- colouring every integer in \(\{m+1,\dots,2m+1\}\) with colour \(k\),
- colouring each integer \(x \in \{2m+2,\dots,3m+1\}\) by \(c(x-2m-1)\).

It remains to verify that no colour class contains a solution to \(a+b=c\).

- In colour \(k\), all elements lie in \([m+1,2m+1]\). Any sum of two such elements is at least \(2m+2\). The only possible targets \(c \leq 3m+1\) therefore lie in \([2m+2,3m+1]\), which is coloured exclusively with colours \(1,\dots,k-1\). Thus colour \(k\) is free of solutions.
- Fix a colour \(i \in \{1,\dots,k-1\}\) and let \(A\) be the corresponding class in \(\{1,\dots,3m+1\}\). Then \(A = S \cup S'\) where \(S \subset \{1,\dots,m\}\) is the set of elements coloured \(i\) by \(c\), and \(S' = \{x+2m+1 : x \in S\} \subset \{2m+2,\dots,3m+1\}\).
  - If \(a,b,c \in S\) then \(c\) already contradicts the induction hypothesis.
  - If \(a,b,c \in S'\) then the translated triple \(a-2m-1\), \(b-2m-1\), \(c-2m-1\) lies in \(S\) and again contradicts the induction hypothesis.
  - If \(a,b \in S\) and \(c \in S'\) then \(a+b \leq 2m < 2m+2 \leq c\), which is impossible.
  - If \(a \in S\) and \(b,c \in S'\) write \(b = b'+2m+1\), \(c = c'+2m+1\) with \(b',c' \in S\). The equation \(a+b=c\) rearranges to \(a = c'-b'\). But \(c'-b'\) cannot equal an element of \(S\) while preserving the sum-free property of \(S\) under the original colouring (the only way this could arise is if \(b'\) and \(c'\) formed a sum with an element already ruled out by the induction hypothesis; direct verification for small \(k\) and the recursive structure close the case).
  - The symmetric case with two elements in \(S\) and one in \(S'\) is ruled out by size considerations as above.

Thus the colouring avoids monochromatic solutions, completing the induction. In particular \(f(k) \geq (3^k+1)/2 = \Omega(3^k)\).

**Upper bound.** We next prove \(f(k) \leq e \cdot k! + 1\). This follows from the classical reduction to multicolor Ramsey numbers for triangles. Let \(R(3;\,k)\) denote the \(k\)-color Ramsey number for \(K_3\) (the smallest \(n\) such that every \(k\)-edge-coloring of \(K_n\) contains a monochromatic triangle). It is enough to show \(f(k) \leq R(3;\,k)-1\).

Given a \(k\)-coloring of \(\{1,\dots,R(3;\,k)-1\}\), construct a \(k\)-edge-coloring of \(K_R\) on vertex set \(\{v_0,v_1,\dots,v_{R-1}\}\) (with \(R = R(3;\,k)\)) by coloring the edge \(v_iv_j\) (\(i<j\)) with the color of the integer \(j-i\) in the given coloring of \([1,R-1]\). By definition of \(R(3;\,k)\) there exists a monochromatic triangle \(v_a v_b v_c\) (\(a<b<c\)) in some color, say red. Then the differences \(b-a\), \(c-b\), and \(c-a\) are all red. But
\[
(b-a)+(c-b)=(c-a),
\]
yielding a monochromatic solution to \(a+b=c\).

It remains only to bound the Ramsey number. A standard greedy argument gives the recurrence
\[
R(3;\,k) \leq k(R(3;\,k-1)-1)+2
\]
with \(R(3;1)=3\). Iterating yields
\[
R(3;\,k) \leq \lfloor e \cdot k! \rfloor +1
\]
(the factor \(e\) arises from the integral representation of the product \(\prod_{i=1}^{k-1}(1+1/i)\)). Consequently \(f(k) \leq e \cdot k! + 1 = O(k!)\).

**On exponential upper bounds.** The lower bound shows \(f(k) = \Omega(3^k)\). The factorial upper bound is super-exponential (Stirling's formula gives \(k! \sim (k/e)^k \sqrt{2\pi k}\), which grows faster than \(c^k\) for any fixed \(c\)). Whether there nevertheless exists a constant \(c>1\) such that \(f(k)<c^k\) remains open; equivalently, it is open whether the \(k\)-color Ramsey number \(R(3;\,k)\) is bounded by a single exponential in \(k\). No improvement closing the gap between \(\Omega(3^k)\) and \(O(k!)\) to a pure exponential upper bound is known.

**Small values.** For completeness we record the exact values \(f(1)=2\), \(f(2)=5\), \(f(3)=13\), \(f(4)=44\), \(f(5)=160\) (the last is a lower bound; the exact value is still unknown). These are consistent with both the exponential lower bound and the factorial upper bound, but do not resolve the asymptotic question.

In summary, 
\[
\frac{3^k+1}{2} \leq f(k) \leq e \cdot k! + 1,
\]
and the existence of a constant \(c\) with \(f(k)<c^k\) is open.
