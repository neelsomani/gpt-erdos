This is an Erdős question from *Problems and results on combinatorial number theory III* (1977): given a sum-free set (S\subset\mathbb R) [[nomath]](no $a,b,c\in S$ with $a+b=c$)[[/nomath]], must there exist (A\subseteq\mathbb R\setminus S) of cardinality (2^{\aleph_0}) such that (A+A\subseteq\mathbb R\setminus S)? Erdős also noted that if the answer were “no”, one could ask the variant assuming $S$ is Sidon. 

As of the most recent public tracking I can find (edited Jan 11, 2026), the **general case remains open**: there is no published proof or counterexample known there. ([Erdős Problems][1])

That said, there are **two substantial positive cases**:

## 1) If (|S|<2^{\aleph_0}), then **yes** (and sum-freeness isn’t even needed)

One can use Zorn’s lemma to choose a **maximal** set (A\subseteq\mathbb R) such that

* (A\cap S=\varnothing), and
* ((A+A)\cap S=\varnothing).

Maximality implies a covering:
[
A\ \cup\ \bigcup_{a\in A}(S-a)\ \cup\ S\ \cup\ (S/2)=\mathbb R,
]
because if $x$ were outside that union then:

* (x\notin S) [[nomath]](so you may add $x$)[[/nomath]],
* (x\notin S/2) [[nomath]](so $2x\notin S$, hence $x+x\notin S$)[[/nomath]],
* (x\notin S-a) for all (a\in A) [[nomath]](so $x+a\notin S$ for all $a\in A$)[[/nomath]],
  and thus (A\cup{x}) would still avoid $S$ and have ((A\cup{x})+(A\cup{x})) avoid $S$, contradicting maximality.

Now if (|S|<|\mathbb R|) and (|A|<|\mathbb R|), then the right-hand side union has size (<|\mathbb R|), contradicting that it equals (\mathbb R). Hence necessarily (|A|=|\mathbb R|). In particular, (A\subseteq\mathbb R\setminus S) has size continuum and (A+A\subseteq\mathbb R\setminus S). ([Erdős Problems][2])

So the problem is only genuinely difficult when (|S|=2^{\aleph_0}).

## 2) If $S$ is Sidon, then **yes** [[nomath]](even when $|S|=2^{\aleph_0}$)[[/nomath]]

Recall: “Sidon” means sums $a+b$ with (a,b\in S) have essentially unique representation (no nontrivial coincidences).

Pick (a\in S) with (a\neq 0), and define
[
A := \bigl( (S\setminus{a}) - a/2 \bigr)\setminus S.
]
Then:

* ((S-a/2)\cap S) has at most one point (otherwise you get two distinct representations of the same sum, violating the Sidon property), so (|A|=|S|=|\mathbb R|).
* Also
  [
  A+A \subseteq (S\setminus{a})+(S\setminus{a})-a,
  ]
  and the Sidon property forces this set to be disjoint from $S$ [[nomath]](because $s_1+s_2-a\in S$ would imply $s_1+s_2=s_3+a$ giving two different sum-representations, with $a$ excluded from ${s_1,s_2}$)[[/nomath]]. ([Erdős Problems][2])

Hence in the Sidon case there is indeed (A\subseteq\mathbb R\setminus S) of size continuum with (A+A\subseteq\mathbb R\setminus S).

## What remains open

The **unresolved regime** is essentially:

* (S\subset\mathbb R) is sum-free,
* (|S|=2^{\aleph_0}),
* no extra additive-uniqueness hypothesis like “Sidon”.

In that case, it is currently not settled (at least in the sources above) whether such an $A$ must exist. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/949 "
  
    Erdős Problem #949
  
"
[2]: https://www.erdosproblems.com/forum/thread/949 "

    Erdős Problem #949 - Discussion thread

"
