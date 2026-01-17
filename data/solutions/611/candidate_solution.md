These are classical Erdős–Gallai–Tuza questions, and (as far as the public literature indicates) they are still **open in full generality**.

They appear verbatim as **Erdős Problem #611**. ([Erdős Problems][1])

## 1) If every maximal clique has size at least (cn), must (\tau(G)=o_c(n))?

This is **open**. ([Erdős Problems][1])

What *is* known is an upper bound of Erdős–Gallai–Tuza: if every (maximal) clique has size at least $k$, then
[
\tau(G)\ \le\ n-\sqrt{kn}.
]
(Here “clique” is used in the older sense “maximal clique” in this line of work.) ([Erdős Problems][1])

Plugging $k=cn$ gives
[
\tau(G)\ \le\ n-\sqrt{c},n \ =\ (1-\sqrt c),n,
]
which is **linear** in $n$, not $o(n)$. So currently the best general bound in this direction does *not* reach sublinearity.

A trivial bound you can always note is
[
\tau(G)\le n-k+1
]
[[nomath]](since removing any $k-1$ vertices leaves a set that cannot contain a maximal clique of size $\ge k$)[[/nomath]], but for $k=cn$ this only gives (\tau(G)\le (1-c)n+1), which is weaker than (n-\sqrt{kn}) when $k$ is a linear fraction of $n$.

For context, without any clique-size hypothesis Erdős–Gallai–Tuza proved
[
\tau(G)\le n-\sqrt{2n}+O(1),
]
and improving the (\sqrt n)-term is itself a well-known open problem (Erdős Problem #610). ([Erdős Problems][2])

## 2) Bounds for (k_c(n)) forcing (\tau(G)<(1-c)n)

Let (k_c(n)) be the smallest integer such that
[
\bigl(\forall\text{ maximal cliques }K,\ |K|\ge k_c(n)\bigr)\ \Longrightarrow\ \tau(G)<(1-c)n.
]

### Upper bound (from the Erdős–Gallai–Tuza inequality)

Using (\tau(G)\le n-\sqrt{kn}), it suffices to ensure
[
n-\sqrt{kn}\ <\ (1-c)n \quad\Longleftrightarrow\quad \sqrt{kn}>cn \quad\Longleftrightarrow\quad k>c^2 n.
]
So you get the clean estimate
[
k_c(n)\ \le\ \lceil c^2 n\rceil+1
]
(up to the usual integer/strict inequality adjustments). ([Erdős Problems][1])

[[nomath]](For comparison, the trivial $\tau\le n-k+1$ only yields $k_c(n)\le cn+1$, which is weaker for $c\in(0,1)$.)[[/nomath]]

### Lower bound (Erdős–Gallai–Tuza construction)

Erdős–Gallai–Tuza also proved a **superpolylogarithmic lower bound**: for each fixed (c>0) there exists (c'>0) such that
[
k_c(n)\ \ge\ n^{,c'/\log\log n}.
]
So (k_c(n)) grows faster than any fixed power of (\log n) [[nomath]](though still $n^{o(1)}$)[[/nomath]]. ([Erdős Problems][1])

### A sharp “(\tau=1)” extreme (Bollobás–Erdős)

At the opposite end, Bollobás and Erdős showed a sharp threshold for forcing (\tau(G)=1): if every maximal clique has size at least
[
n+3-2\sqrt n,
]
then (\tau(G)=1), and this bound is best possible. ([Erdős Problems][1])

## What we can currently say, succinctly

* The statement “maximal cliques all (\ge cn) (\Rightarrow \tau(G)=o(n))” is **open**. ([Erdős Problems][1])
* Best general upper bound under “all maximal cliques (\ge cn)” is
  [
  \tau(G)\le (1-\sqrt c),n,
  ]
  from Erdős–Gallai–Tuza. ([Erdős Problems][1])
* For the threshold function (k_c(n)),
  [
  n^{,c'/\log\log n}\ \le\ k_c(n)\ \le\ O(n),
  ]
  and more concretely (k_c(n)\le \lceil c^2 n\rceil+1). ([Erdős Problems][1])

If you tell me what range of $c$ you care about [[nomath]](e.g. $c<1/2$, $c$ close to 1, etc.)[[/nomath]], I can also outline what kinds of constructions are known for the lower bound side and what the extremal examples look like in those regimes (as far as the cited results go).

[1]: https://www.erdosproblems.com/611 "https://www.erdosproblems.com/611"
[2]: https://www.erdosproblems.com/610 "https://www.erdosproblems.com/610"
