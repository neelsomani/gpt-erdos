This is **open in full generality**.

It appears as Problem **(I.26)** in Erdős’ 1961 list of “Some unsolved problems” [[nomath]](he asks exactly whether the corresponding set $B$ has a *logarithmic* density)[[/nomath]]. ([Renyi Users][1]) It is also tracked as **Erdős Problem #486** in the Erdős Problems database and is currently listed there as open. ([Erdős Problems][2])

What *is* known (and why logarithmic density is the right notion here):

* **Finite $A$:** If $A$ is finite, then $B$ has an **ordinary natural density** (hence also a logarithmic density). Reason: for (A={n_1,\dots,n_k}), membership in $B$ for all sufficiently large $m$ depends only on (m \bmod \mathrm{lcm}(n_1,\dots,n_k)), so $B$ is eventually periodic.

* **The “multiples” case (X_n={0}):** Davenport and Erdős proved that when (X_n={0}) for all (n\in A), the resulting set [[nomath]](equivalently, the set of integers avoiding being a multiple of any element of $A$, with the “activation” $m>n$)[[/nomath]] **always has a logarithmic density**. This is the classical Davenport–Erdős theorem about sets of multiples (log density always exists even though natural density need not). ([Erdős Problems][2])
  Erdős explicitly motivates the use of logarithmic density because Besicovitch constructed examples (already in the multiples setting) where **natural density fails to exist**. ([Erdős Problems][2])

* **Single residue class per modulus is already open:** Even the special case (|X_n|=1) for each $n$ [[nomath]](i.e. specifying one forbidden residue $a_i \bmod n_i$ for each modulus)[[/nomath]] is itself posed by Erdős and is listed as open (Erdős Problem #25), and your question generalizes it. ([Erdős Problems][3])

A small subtlety worth noting (because it changes the difficulty): the “activation threshold” (m>n) is important. If one drops that and requires (m\not\in X_n \pmod n) for *all* (n\in A) with no threshold, then there are easy constructions that can destroy convergence; this is discussed in the Erdős Problems forum thread for #486. ([Erdős Problems][4]) But **with** the threshold [[nomath]](as you wrote it, and as in Erdős’ original formulation $b\ge a_i$)[[/nomath]], the general problem remains open. ([Renyi Users][1])

[1]: https://users.renyi.hu/~p_erdos/1961-22.pdf "https://users.renyi.hu/~p_erdos/1961-22.pdf"
[2]: https://www.erdosproblems.com/486 "https://www.erdosproblems.com/486"
[3]: https://www.erdosproblems.com/25 "https://www.erdosproblems.com/25"
[4]: https://www.erdosproblems.com/forum/thread/486 "https://www.erdosproblems.com/forum/thread/486"
