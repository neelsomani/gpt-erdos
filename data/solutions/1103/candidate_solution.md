Write the sequence as (A={a_1<a_2<\cdots}\subset \mathbb Z).
Your condition is that **every pairwise sum** (a_i+a_j) [[nomath]](including $2a_i$)[[/nomath]] is squarefree.

A convenient way to phrase “how fast $A$ must grow” is via the counting function
[
A(N):=\bigl|A\cap[1,N]\bigr|
]
or equivalently via the size of (a_j) in terms of $j$.

## What is known (best current bounds)

Let (\mathrm{ES}_N) denote the **maximum** size of a subset of ({1,2,\dots,N}) whose pairwise sums are all squarefree. Then for any infinite $A$ with squarefree sums, we always have
[
A(N)\le \mathrm{ES}_N
]
and hence (a_j) is controlled by upper bounds on (\mathrm{ES}_N). (This is exactly the finite analogue studied in the literature.)

### Best known upper bound on $A(N)$ (hence best lower bound on growth)

The currently best bounds quoted for (\mathrm{ES}_N) are [[nomath]](for large $N$)[[/nomath]]
[
\mathrm{ES}_N \ll N^{11/15}\exp\\(O\\(\tfrac{\log N}{\sqrt{\log\log N}}\\)\\),
]
due to work of Konyagin in the finite setting, as summarized e.g. by van Doorn–Tao. ([arXiv][1])

Plugging (N=a_j) gives (j=A(a_j)\le \mathrm{ES}_{a_j}), and inverting yields the **lower bound**
[
a_j \gg j^{15/11}\exp\\(-O!\\(\tfrac{\log j}{\sqrt{\log\log j}}\\)\\)
\qquad (j\ \text{large}).
]
Equivalently,
[
a_j \ge j^{15/11-o(1)} \approx j^{1.3636\ldots-o(1)}.
]
This is the best exponent currently on record for “how fast $A$ must grow.” ([arXiv][1])

In density language, this says
[
A(N)\ll N^{11/15+o(1)} \quad\text{so}\quad \frac{A(N)}{N}\ll N^{-4/15+o(1)}.
]

### A clean “for all $j$” polynomial bound

van Doorn–Tao also prove an explicit, simpler polynomial growth bound of the form
[
a_j \ge c j^{4/3}\quad\text{for all }j,
]
with an explicit constant $c$ reported as $0.24$ in the Erdos Problems summary. ([Erdős Problems][2])
[[nomath]](This corresponds to the weaker—but more elementary—estimate $\mathrm{ES}_N\ll N^{3/4}$ mentioned in their paper. ([arXiv][1]))[[/nomath]]

So, unconditionally:

* **must** grow faster than (j^{4/3}) [[nomath]](uniformly in $j$)[[/nomath]], and
* in fact **for large $j$** must grow at least (j^{15/11-o(1)}).

## How slow can $A$ grow? (existence upper bounds)

On the construction side, there do exist infinite sequences with squarefree sums. Erdős noted a greedy construction giving exponential growth. ([arXiv][1])

More strongly, van Doorn–Tao show there exists such a sequence with **subexponential** growth, specifically
[
a_j < \exp\\(\frac{5j}{\log j}\\)
\quad\text{for all sufficiently large }j,
]
and it can be arranged that the (a_j) themselves are squarefree. ([Erdős Problems][2])

So the best-known “window” is:
[
j^{15/11-o(1)} \lesssim a_j \lesssim \exp\\(O\\(\tfrac{j}{\log j}\\)\\),
]
and closing this gap is still open.

## Status of Erdős’s original expectation

Erdős wrote that he did **not** expect a polynomial-growth example to exist. ([arXiv][1])
As of the sources above, this remains unresolved: we only know polynomial **lower bounds** on growth (so polynomial growth is not ruled out), and subexponential **upper bounds** via constructions.

If you tell me whether you want the answer in terms of (a_j) or in terms of $A(N)$, I can restate the same bounds in your preferred form (they’re equivalent by inversion).

[1]: https://arxiv.org/pdf/2512.01087 "Growth rates of sequences governed by the squarefree properties of its translates"
[2]: https://www.erdosproblems.com/latex/1103 "
  
    Erdős Problems
  
"
