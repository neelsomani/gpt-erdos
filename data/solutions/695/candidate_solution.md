This is a classical Erdős question about **prime chains**: sequences of primes (p_1<p_2<\cdots) with
[
p_{i+1}\equiv 1 \pmod{p_i}.
]
In this generality the sequence always exists [[nomath]](Dirichlet gives infinitely many primes $ \equiv 1 \pmod{p_i}$ at each step)[[/nomath]], so the issue is the **slowest possible growth**.

## Status of the two questions

As of the current literature, both questions are **open** (this is Erdős Problem #695). ([Erdős Problems][1])

That said, there are meaningful unconditional and conditional bounds that explain why the conjectured answer is “yes” to the first question and “yes” to the second.

---

## A natural “slow growth” candidate: the greedy chain

A standard candidate for “minimal growth” is the **greedy** construction:

* start with (p_1=2);
* define (p_{i+1}) to be the **smallest** prime ( \equiv 1 \pmod{p_i}).

This is OEIS **A061092**, with initial terms
[
2,3,7,29,59,709,2837,22697,590123,\dots
]
([OEIS][2])

(Any other construction can of course jump much faster; the difficulty is controlling growth from above while maintaining the congruences.)

---

## Unconditional upper bound: double exponential via Linnik

Let (\ell(q)) be the least prime (\equiv 1 \pmod q). Linnik’s theorem (in the “least prime in an arithmetic progression” form) gives
[
\ell(q) \ll q^{L}
]
for an absolute constant $L$. A modern explicit bound quoted in the literature is (L\le 5.18) (Xylouris). 

Applying this with (q=p_i) in the greedy chain gives a recurrence of the shape
[
p_{i+1} \ll p_i^{L}.
]
Iterating yields
[
\log p_k \ll L^{k} \quad\text{and hence}\quad p_k \le \exp(\exp(O(k))),
]
which is exactly the “(e^{e^{O(k)}})” bound quoted in the Erdős problems discussion. ([Erdős Problems][1])

In particular, for this (explicitly defined) chain,
[
\frac{\log p_k}{k}\to\infty \qquad\Longrightarrow\qquad p_k^{1/k}\to\infty.
]
So **there exists** such a chain with (\lim p_k^{1/k}=\infty) (indeed very rapidly).

But that does **not** settle Erdős’s first question, which is about whether *every* infinite chain must have that behavior, i.e. whether one can keep the growth merely exponential.

---

## Why the first question is nontrivial (and still open)

Write
[
p_{i+1} = m_i p_i + 1,\qquad m_i\in\mathbb{N}.
]
If the multipliers (m_i) stayed bounded [[nomath]](say $m_i\le M$ for all $i$)[[/nomath]], then (p_k) would be at most exponential in $k$, and (p_k^{1/k}) would be bounded.

The most famous bounded-multiplier special case is a **Cunningham chain of the first kind**:
[
p_{i+1}=2p_i+1,
]
which automatically satisfies (p_{i+1}\equiv 1\pmod{p_i}). Cunningham chains are well studied, but there is “no general result known on large Cunningham chains” (beyond finite searches and heuristics), i.e. nothing like a proof that an infinite chain exists or cannot exist. ([Wikipedia][3])

An **infinite** Cunningham chain would make (p_k) essentially (\asymp 2^k), giving (p_k^{1/k}\to 2), and would therefore **disprove** (\lim p_k^{1/k}=\infty).

So the first question is tied up with deep “least prime in progressions / prime-producing linear forms” phenomena, and remains open. ([Erdős Problems][1])

---

## The second question and its connection to “least prime in a progression”

Your second inequality
[
p_k \le \exp\big(k(\log k)^{1+o(1)}\big)
]
is roughly what you get if you can always find a prime (p'\equiv 1\pmod p) with size not much bigger than $p$ times a polylog factor.

A commonly believed strengthening of Linnik-type bounds is that the least prime (\equiv a \pmod q) should be
[
\ll q^{1+\varepsilon},
\quad\text{and maybe even}\quad
\ll q(\log q)^{1+o(1)}.
]
This heuristic is explicitly discussed in the literature/MO. ([MathOverflow][4])

The Erdős problem page states essentially this: **if** one had a bound of the type
[
\ell(p)\ \le\ p(\log p)^{O(1)}\quad\text{for every prime }p,
]
then the greedy chain would satisfy
[
p_k \le \exp\big(k(\log k)^{1+o(1)}\big).
]
([Erdős Problems][1])

At present, such a strong uniform bound for (\ell(p)) is not known, so **the existence of a chain meeting your second bound is open**.

---

## Related work on prime chains

Ford–Konyagin–Luca study prime chains (exactly in your sense) and the related “Pratt tree” structure, proving various distributional results and upper/lower bounds for the *maximum chain length ending at a prime $p$*. ([arXiv][5])

This is important context, but it does not resolve Erdős #695’s quantitative growth questions.

---

## Bottom line

* **Is it true that (\lim_k p_k^{1/k}=\infty) for every such chain?**
  Open. (A bounded-multiplier infinite chain would refute it; even the special Cunningham-chain scenario is unresolved.) ([Erdős Problems][1])

* **Does there exist a chain with (p_k \le \exp(k(\log k)^{1+o(1)}))?**
  Also open unconditionally, but it would follow from a strong conjectural bound on the least prime in the progression (1 \bmod p). ([Erdős Problems][1])

If you tell me whether you’re mainly interested in **conditional implications** (e.g. assuming GRH / Elliott–Halberstam / conjectures on least primes in progressions) or in what can be proved **unconditionally**, I can tailor a more detailed “if–then” map of which hypotheses give which growth rates.

[1]: https://www.erdosproblems.com/forum/thread/695 "

    Erdős Problem #695 - Discussion thread

"
[2]: https://oeis.org/A061092 "A061092 - OEIS"
[3]: https://en.wikipedia.org/wiki/Cunningham_chain?utm_source=chatgpt.com "Cunningham chain"
[4]: https://mathoverflow.net/questions/80865/least-prime-in-a-arithmetic-progression?utm_source=chatgpt.com "nt.number theory - least prime in a arithmetic progression"
[5]: https://arxiv.org/abs/0904.0473 "[0904.0473] Prime chains and Pratt trees"
