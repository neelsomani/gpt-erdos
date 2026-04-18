# Grok Response for Problem 478

**Heuristic suggesting the asymptotic**

The sequence is defined by \(a_1 = 1\) and \(a_{k+1} \equiv (k+1) a_k \pmod{p}\) for \(1 \leq k < p-1\). Thus \(A_p = \{a_k : 1 \leq k \leq p-1\}\) and we seek \(|A_p|\).

For \(1 \leq j < m < p\),
\[
a_m \equiv a_j \pmod{p}
\]
if and only if
\[
\prod_{i=j+1}^m i \equiv 1 \pmod{p},
\]
i.e., the falling factorial
\[
m(m-1)\cdots(m-l+1) \equiv 1 \pmod{p}
\]
where \(l = m-j \geq 1\). (The case \(l=1\) forces \(m \equiv 1 \pmod{p}\), which never holds for \(2 \leq m < p\).) Consequently \(a_m\) is *new* (not equal to any prior \(a_j\)) precisely when none of the \(m-2\) congruences
\[
m(m-1)\cdots(m-l+1) \equiv 1 \pmod{p}, \qquad l=2,\dots,m-1
\]
hold.

Write
\[
|A_p| = 1 + \sum_{m=2}^{p-1} \mathbf{1}_{\text{no } l\in\{2,\dots,m-1\} \text{ satisfies the congruence above}}.
\]
When \(m\) is small (\(m = o(\log p/\log\log p)\)) we have \(m! < p\), so all \(a_m = m!\) are distinct and lie in \(\{1,\dots,p-1\}\). The number of such \(m\) is \(o(p)\), contributing only \(o(p)\) to \(|A_p|\).

For the bulk of the sum (\(m\) up to \(\Theta(p)\)), model the indicator that \(a_m\) is new as follows. For each fixed length \(l \geq 2\) the congruence
\[
x(x-1)\cdots(x-l+1) \equiv 1 \pmod{p}
\]
is a degree-\(l\) polynomial equation in \(x\). It has at most \(l\) roots modulo \(p\) (unless identically zero, which it is not for \(p > l\)). Thinking of a “typical” \(m < p\) as roughly uniform, each individual \(l\) forbids at most \(l\) values of \(m\), suggesting a collision probability of order \(l/p\) for that \(l\).

If the events for different \(l\) were independent and roughly Poisson with mean \(1\), the probability of *no* collision at a given \(m\) would be approximately \(e^{-1}\). Summing \(p-2\) such indicators then yields the heuristic
\[
|A_p| \sim (1 - e^{-1})p.
\]
More globally, view the whole process as inserting \(p-1\) successive values into \(\mathbb{F}_p^\times\). Each new candidate is obtained by multiplication by a nonzero residue; because multiplication by a fixed nonzero element is bijective, if \(a_k\) is uniformly distributed on \(\mathbb{F}_p^\times\) then so is \(a_{k+1}\). Conditioning on the set of previously seen residues (size \(s\)), the probability that the deterministic next multiplier produces a collision with one of the \(s\) earlier terms is exactly the probability that one of the \(s\) explicit falling-factorial congruences holds. When those congruences behave like independent random conditions of probability \(1/p\) each, the instantaneous collision probability is \(\approx s/p\), reproducing the classic occupancy-process recurrence whose solution is
\[
\mathbb{E}[\text{distinct after } t \text{ steps}] = p\bigl(1 - (1-1/p)^t\bigr).
\]
Setting \(t = p-1\) again gives \(\sim (1-1/e)p\).

**Why a rigorous proof is elusive**

To turn the heuristic into a proof one must control the *dependence* among the \(O(p)\) congruences
\[
m(m-1)\cdots(m-l+1) \equiv 1 \pmod{p}
\]
as both \(m\) and \(l\) vary with \(p\). For small \(l\) (say \(l \leq (\log p)^C\)) the polynomials are of bounded degree, so the total number of “bad” \(m\) caused by small-\(l\) collisions is \(O((\log p)^{2C}) = o(p)\). For large \(l\) the products involve \(\Theta(p)\) consecutive residues; showing that these products are equidistributed (or at least that the simultaneous solution set to any fixed number of such equations has the expected size) requires strong uniformity statements on products of consecutive integers modulo \(p\). Such uniformity is tied to deep questions about short character sums, equidistribution in the multiplicative group, and possible Siegel zeros, all of which lie beyond elementary methods.

Inclusion-exclusion over the set of colliding lengths \(l\) produces main terms that match the Poisson heuristic, but the error terms involve counting solutions to systems
\[
\prod_{i=1}^{l_j} (m - a_{i,j}) \equiv 1 \pmod{p}
\]
for various shifts \(a_{i,j}\). Bounding these error terms uniformly in the number of equations and in the length scales appears intractable with current techniques.

After extensive examination of the deterministic collision criterion, the Poissonian occupancy model, and the polynomial nature of the forbidden congruences, the asymptotic cannot be established rigorously here. Therefore the problem remains open.

**Conclusion**

I could not solve it.
