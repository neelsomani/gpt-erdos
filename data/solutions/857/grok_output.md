# Grok Response for Problem 857

**Problem 857: Estimating \(m(n,k)\)**

A sunflower (or \(\Delta\)-system) of size \(k\) in a collection of sets is a subcollection \(B_1, \dots, B_k\) such that \(B_i \cap B_j = C\) for some fixed set \(C\) and all \(i \neq j\). Equivalently, writing \(B_i = C \cup D_i\) with \(D_i \neq \emptyset\) for all \(i\) (when the \(B_i\) are distinct), the \(D_i\) are pairwise disjoint. The quantity \(m(n,k)\) is the smallest integer such that every collection of \(m(n,k)\) subsets of \([n] = \{1, \dots, n\}\) contains a \(k\)-sunflower. Equivalently, if \(\mathrm{ex}(n,k)\) is the size of the largest collection without a \(k\)-sunflower, then \(m(n,k) = \mathrm{ex}(n,k) + 1\).

We derive bounds on \(\mathrm{ex}(n,k)\) (and thus on \(m(n,k)\)) using a combination of explicit constructions and the probabilistic method (with the Lovász Local Lemma for the lower bound). The analysis is carried out directly from the definitions, without assuming uniformity of the sets.

#### Lower Bound via Complements of Small Sets (\(t=1\) Case)
Consider the family \(F\) consisting of the full set \([n]\) together with all sets of size \(n-1\) (i.e., all sets with complement of size at most 1). This has size
\[
|F| = 1 + n.
\]
We claim \(F\) is \(k\)-sunflower-free for any \(k \geq 3\).

Let \(A, B, C \in F\) be distinct. Each is either \([n]\) or \([n] \setminus \{x\}\) for some \(x\). The pairwise intersections are:
- If \(A = [n] \setminus \{x\}\) and \(B = [n] \setminus \{y\}\) with \(x \neq y\), then \(A \cap B = [n] \setminus \{x,y\}\).
- If one is \([n]\), say \(A = [n]\) and \(B = [n] \setminus \{x\}\), then \(A \cap B = [n] \setminus \{x\}\).

For any triple, the pairwise intersections cannot all be equal: the intersections involving distinct omitted elements differ by at least one element, and intersections with \([n]\) simply recover the other set (which cannot equal an \((n-2)\)-set). Thus, no triple (let alone a \(k\)-tuple for \(k > 3\)) forms a sunflower. This gives
\[
m(n,k) \geq n + 2.
\]
While linear in \(n\), this construction generalizes the observation that "large" sets have intersections that are forced to differ when the omitted parts differ. For fixed \(k\) and large \(n\), better constructions are needed.

#### Improved Lower Bound via the Probabilistic Method and Local Lemma
To obtain an exponential lower bound, sample a random subfamily \(F \subseteq 2^{[n]}\) by including each subset independently with probability \(p > 0\) (to be chosen). Let \(\mathcal{S}\) be the collection of all possible \(k\)-sunflowers in \(2^{[n]}\). For each \(\sigma \in \mathcal{S}\), let \(E_\sigma\) be the bad event that all \(k\) members of \(\sigma\) lie in \(F\).

First, bound \(|\mathcal{S}|\). A \(k\)-sunflower is determined by a core \(C \subseteq [n]\) and \(k\) nonempty pairwise-disjoint "petals" \(D_1, \dots, D_k \subseteq [n] \setminus C\). For each element of \([n]\), there are \(k+2\) choices: place it in the core (present in all \(k\) sets), in exactly one of the \(k\) petals, or in none of the sets. Thus, there are at most \((k+2)^n\) ways to assign elements (including cases where some petal is empty). Accounting for overcounting by symmetries (at most \(k!\) for labeling the petals) yields
\[
|\mathcal{S}| \leq \frac{(k+2)^n}{k!} = O_k((k+2)^n).
\]
(The core is uniquely recovered as the common pairwise intersection, so there is no further overcounting across different cores.) Then
\[
\Pr(E_\sigma) = p^k
\]
for each \(\sigma\), and the expected number of sunflowers in \(F\) is
\[
\mu := \mathbb{E}[|\{\sigma \in \mathcal{S} : E_\sigma \text{ holds}\}|] \leq O_k((k+2)^n p^k).
\]

To show there exists a nonempty \(F\) with no sunflower, apply the Lovász Local Lemma. The event \(E_\sigma\) is mutually independent of all but those \(E_\tau\) where \(\tau\) shares at least one set with \(\sigma\). Fix \(\sigma = \{B_1, \dots, B_k\}\). The dependency degree \(D\) satisfies
\[
D \leq k \cdot (\text{maximum number of sunflowers containing a fixed set } B).
\]
For fixed \(B\), the number of \(k\)-sunflowers containing \(B\) is at most the total \(|\mathcal{S}|\) scaled by the "density" of sets equal to \(B\) (at most \(O((k+2)^n / 2^n)\), as a random subset equals a fixed \(B\) with probability \(2^{-n}\)). Thus,
\[
D \leq O_k(k^2 (k+2)^n / 2^n).
\]
By the symmetric LLL, if
\[
e \cdot \Pr(E_\sigma) \cdot (D + 1) < 1,
\]
then \(\Pr(\text{no } E_\sigma \text{ holds}) > 0\). Substituting the bounds,
\[
e \cdot p^k \cdot O_k(k^2 (k+2)^n / 2^n) < 1
\]
implies
\[
p^k < \frac{2^n}{O_k(k^2 (k+2)^n)} \implies p < O_k\left( \frac{2^{n/k}}{(k+2)^{n/k}} \right).
\]
(The \(k^{O(1/k)}\) factors are absorbed in the \(O_k(\cdot)\).) The expected size of \(F\) is then
\[
\mathbb{E}[|F|] = p \cdot 2^n > \left( \frac{2^{1 + 1/k}}{(k+2)^{1/k}} \right)^n \cdot \frac{1}{\mathrm{poly}(k)}.
\]
There thus exists a \(k\)-sunflower-free family of this size, so
\[
m(n,k) > \left( \frac{2^{1 + 1/k}}{(k+2)^{1/k}} \right)^n
\]
for all sufficiently large \(n\) (depending on \(k\)). For example:
- When \(k=3\), the base is \(2^{4/3}/5^{1/3} \approx 1.47\), so \(m(n,3) > (1.47 - \varepsilon)^n\) for large \(n\).
- As \(k \to \infty\), the base tends to 2 (recovering the trivial \(m(n,k) \leq 2^n + 1\)).

This establishes an exponential lower bound with base strictly greater than 1 for each fixed \(k \geq 3\).

#### Upper Bound
The trivial upper bound is \(m(n,k) \leq 2^n + 1\), obtained by taking the entire power set (which contains \(k\)-sunflowers for \(n \gg k\)) or by the pigeonhole principle. To improve, partition \(F\) into uniform layers \(F_r = \{A \in F : |A| = r\}\) for \(r = 0, \dots, n\). If any \(|F_r|\) exceeds the maximum size of a \(k\)-sunflower-free \(r\)-uniform family on \([n]\), then \(F\) contains a \(k\)-sunflower.

While the classical Erdős–Rado bound shows that an \(r\)-uniform family larger than \(r!(k-1)^r\) contains a \(k\)-sunflower (so \(\mathrm{ex}(n,k) \leq \sum_{r=0}^n r!(k-1)^r\)), this is larger than \(2^n\) for \(r \approx n/2\) and fixed \(k\), yielding no improvement over the trivial bound. Recent improvements replace \(r!\) by roughly \((\log r / \log \log r)^r\), but for \(r = \Theta(n)\) this remains super-exponential in \(n\) and again exceeds \(2^n\).

A direct recursive bound can be attempted by splitting \(F = F_0 \cup F_1\), where \(F_0\) consists of members not containing \(n\) and \(F_1\) consists of members with \(n\) removed (both families on \([n-1]\)). Sunflowers entirely in \(F_0\) or \(F_1\) are detected recursively. However, "mixed" sunflowers (using sets from both) are possible when the core \(C\) does not contain \(n\): at most one set from \(F_1\) can participate (since multiple would share \(n\) in their petals, violating disjointness), but for \(k \geq 3\) one can have \(k-1\) sets from \(F_0\) and one from \(F_1\) with all pairwise intersections equal to some \(S \subseteq [n-1]\). This coupling prevents a clean recursion yielding \(m(n,k) \leq 2 \cdot m(n-1,k)\), which would contradict the existence of sunflowers in the full power set.

Thus, the best unconditional upper bound obtainable by these methods is the trivial \(m(n,k) \leq 2^n + 1\).

#### Conclusion on Asymptotics
Combining the bounds,
\[
\left( \frac{2^{1 + 1/k}}{(k+2)^{1/k}} \right)^n < m(n,k) \leq 2^n + 1.
\]
For fixed \(k\), this shows \(m(n,k) = 2^{\Theta(n)}\), but the constants in the exponent are not matched: the lower bound base is strictly less than 2, and closing the gap appears to require new ideas (e.g., sharper counting of sunflowers or canonical Ramsey-type arguments to force mixed sunflowers). For \(k=3\) the lower bound is roughly \(1.47^n\), while the upper bound is \(2^n\); improving either side (or proving \(m(n,k) \sim c(k)^n\) for some explicit \(c(k)\)) remains open.

After substantial effort deriving the probabilistic lower bound via direct counting and the Local Lemma, attempting recursive splittings, analyzing explicit large-set constructions, and exploring uniform-layer reductions, the exact asymptotic could not be pinned down beyond the exponential bounds above.
