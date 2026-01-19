Your definition is the “**weak jump**” version of Erdős’s *jumping constant* phenomenon for $3$-uniform hypergraphs:

* the first clause [[nomath]](“$>\alpha$ forces a density increment to some $\beta(\alpha)>\alpha$ on larger and larger subgraphs”)[[/nomath]] is exactly the usual notion that **(\alpha) is a jump**, and
* the second clause [[nomath]](“this can fail if $>\alpha$ is replaced by $\ge \alpha$”)[[/nomath]] is exactly saying (\alpha) is **not** a *strong* jump (so it’s “weak”). 

## What is known about (A_3)

### 1) (0\in A_3)

Johnston–Lu show (in their terminology) that $0$ is always a jump but cannot be a strong jump, hence $0$ is a *weak* jump. Translating to your notation gives (0\in A_3). ([arXiv][1])

[[nomath]](And of course, the “$\ge 0$” version fails trivially by taking the empty $3$-graph sequence.)[[/nomath]]

### 2) No (\alpha\in(0,2/9)) lies in (A_3)

Peng–Zhao (Fact 1.11) prove that for every (r\ge 3), **every (\alpha\in(0, r!/r^r)) is a strong jump** and $0$ is non-strong. For $r=3$, (r!/r^r = 6/27=2/9). So every (\alpha\in(0,2/9)) is *strong*, hence **cannot** be in (A_3) [[nomath]](since your second clause requires the “$\ge\alpha$” statement to fail)[[/nomath]]. ([ScienceDirect][2])

So far we have the definite containment
[
A_3\cap(0,2/9)=\varnothing
\quad\text{and}\quad
0\in A_3,
]
i.e.
[
A_3\subseteq {0}\cup[2/9,1].
]

### 3) The big open case: is (2/9\in A_3)?

It is a classical Erdős question (with a stated prize in some sources) whether $2/9$ is a **jump** for $3$-graphs. 

* If $2/9$ **is** a jump, then it would be a prime candidate to belong to (A_3) (it is the “first” natural boundary point in the theory, and in any case it is **not** a strong jump).
* If $2/9$ is **not** a jump, then (2/9\notin A_3) by definition.

As of the current literature summaries, **this remains open**. ([Mathematical Institute][3])

### 4) Above $2/9$: jumps and non-jumps exist, but (A_3) is still not determined

There are known **intervals of jump values** for $3$-graphs found via flag algebra methods (Baber–Talbot), e.g. intervals around (\approx 0.23) and (\approx 0.29). ([Mathematical Institute][3])
There are also explicit **non-jumps** (starting from Frankl–Rödl’s constructions and later improvements). ([Mathematical Institute][3])

However, converting these “jump/non-jump” results into a full description of the **weak** jumps [[nomath]](your $A_3$)[[/nomath]] is precisely the hard part—and it is not currently known.

## Bottom line

[
\boxed{\text{The exact set }A_3\text{ is not known (open problem of Erdős–Simonovits).}}
]
What we *can* say unconditionally is:

* (\boxed{0\in A_3}). ([arXiv][1])
* (\boxed{A_3\cap(0,2/9)=\varnothing}) [[nomath]](since all $\alpha\in(0,2/9)$ are strong jumps)[[/nomath]]. ([ScienceDirect][2])
* Membership of (\boxed{2/9}) [[nomath]](and essentially everything else $\ge 2/9$)[[/nomath]] is part of the open territory. 

[1]: https://arxiv.org/pdf/1403.1220 "https://arxiv.org/pdf/1403.1220"
[2]: https://www.sciencedirect.com/science/article/pii/S0012365X08006456 "https://www.sciencedirect.com/science/article/pii/S0012365X08006456"
[3]: https://people.maths.ox.ac.uk/keevash/papers/turan-survey.pdf "https://people.maths.ox.ac.uk/keevash/papers/turan-survey.pdf"
