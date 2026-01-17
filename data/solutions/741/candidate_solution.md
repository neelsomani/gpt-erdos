These are exactly **Erdős Problem #741 (Burr–Erdős)**. As far as I can verify from the literature trail that is commonly cited for this problem, both parts are currently regarded as **open** in full generality. The Erdős Problems site lists the pair of questions as open and notes that Erdős believed he could build an example for the second question but “could never quite finish the proof.” ([Erdős Problems][1])

That said, there are several nontrivial **partial results / reductions** that clarify what a proof or counterexample would have to look like.

## 1) If $A+A$ has positive density, must $A$ split into two pieces with both (A_i+A_i) positive density?

### Trivial “dense $A$” case: yes

If $A$ itself has positive (upper or lower) density, then it’s easy to split $A$ into two subsets (A_1,A_2) each of **positive density**, and then each (A_i+A_i) automatically has **positive density** [[nomath]](because for any finite $B\subset[1,N]$, $|B+B|\ge 2|B|-1$, so linear-size $B$ forces linear-size $B+B$ in $[1,2N]$)[[/nomath]].

So the difficulty is entirely in the **thin** regime: (\overline d(A)=0) but (\overline d(A+A)>0).

### A useful sufficient condition: “many disjoint representations” on a positive-density set of sums

Let (r_{\mathrm{disj}}(n)) denote the maximum number of pairwise **disjoint** representations
[
n=a_1+b_1=\cdots=a_k+b_k,\qquad {a_i,b_i}\cap{a_j,b_j}=\emptyset \ (i\neq j),
]
with (a_i,b_i\in A).

If there exists a set (S\subseteq A+A) of **positive density** such that (r_{\mathrm{disj}}(n)\ge K) for all (n\in S) [[nomath]](for some fixed $K$)[[/nomath]], then a **random 2-coloring** of $A$ makes each (n\in S) land in (say) (A_1+A_1) with probability at least (1-(3/4)^K), because each disjoint representation has probability $1/4$ to become monochromatic in color 1, and disjointness makes the “no monochromatic representation” event independent across the $K$ witnesses.

In that setting one can push (by averaging/compactness) to an actual partition with (\overline d(A_1+A_1)>0), and similarly for (A_2).

The open part is precisely that **nothing in (\overline d(A+A)>0)** currently forces such representation redundancy on a positive-density subset of sums.

### What a counterexample to $1$ would likely need to look like

Heuristically, the only way a partition could *fail* is if a positive-density chunk of $A+A$ is supported by “fragile” representations—e.g. sums whose representations are bottlenecked through a small “critical” subset of $A$ so that one of the color classes inevitably loses almost all those sums. This is exactly the phenomenon that makes the second (basis) question hard as well.

At present, I don’t know a construction that provably enforces this fragility while still keeping $A+A$ of positive density, and the problem is listed as open. ([Erdős Problems][1])

## 2) Is there a basis $A$ of order 2 such that no partition (A=A_1\sqcup A_2) makes both (A_1+A_1) and (A_2+A_2) have bounded gaps?

Again, this is listed as open in the same source. ([Erdős Problems][1])

But there is an important **constraint** coming from known “decomposition of bases” theorems:

### Bases with “enough” representations can be partitioned into two bases (hence both sumsets are syndetic)

Erdős and Nathanson prove (in the order-2 case) that if an asymptotic basis $A$ has a representation function $f(n)$ that is at least a constant multiple of (\log n) for all large $n$, then $A$ can be partitioned into $t$ disjoint asymptotic bases of the same order. In particular, for order 2 they explicitly pose and use the threshold (f(n)\gtrsim c\log n) [[nomath]](with $c>\log^{-1}(4/3)$)[[/nomath]] to guarantee a partition into two order-2 bases; they also highlight as an open direction whether merely (f(n)\to\infty) suffices. 

Consequences for your question:

* If $A$ is a basis of order 2 with **many** representations per large integer (in the above sense), then there **is** a partition (A=A_1\sqcup A_2) where each (A_i) is still an asymptotic basis of order 2.
* In that case each (A_i+A_i) is cofinite, hence has bounded gaps.

So any example for your second question (if it exists) must be an order-2 basis with **very sparse representation function**—certainly not satisfying a uniform (c\log n) lower bound, and plausibly having many integers with only $O(1)$ (or very slowly growing) disjoint representations.

### What a plausible construction would need to achieve

A natural “Erdős-style” strategy (and the one hinted at in discussions of this problem) is to build a basis $A$ with infinitely many large intervals (I_k) such that:

1. Every (n\in I_k) has its representations (n=a+b) **forced to use** a specific “hinge” element (h_k\in A) (or a very small hinge-set), and
2. Those (I_k)’s have lengths (|I_k|\to\infty), and
3. Representations coming from the rest of $A$ are arranged not to “accidentally” hit (I_k).

Then, in any partition (A=A_1\sqcup A_2), the color class that does **not** contain (h_k) would miss (I_k) entirely in its self-sumset, giving unbounded gaps.

The challenge (and what seems to have blocked a complete proof historically) is simultaneously ensuring:

* $A$ remains an order-2 basis [[nomath]](so $A+A$ covers all sufficiently large integers)[[/nomath]], **and**
* the “forced-hinge intervals” (I_k) are not filled by other same-color sums coming from other parts of $A$.

This tension is exactly why the problem is still circulated as open. ([Erdős Problems][1])

## Summary

* Both questions are widely presented as **open** in current problem compilations for Burr–Erdős / Erdős Problem #741. ([Erdős Problems][1])
* There are meaningful partial results:

  * If $A$ is itself dense, $1$ is easy.
  * For $2$, bases with representation function (\gtrsim c\log n) can be partitioned into two order-2 bases (so they *cannot* be examples); any example must be much “thinner” in terms of representations. 

If you tell me which notion of density you’re using (upper/lower asymptotic density vs Banach density), I can sharpen the “easy dense case” statement and the “many disjoint representations ⇒ decomposable” implications, because the exact density notion matters for how one passes from finite to infinite statements.

[1]: https://www.erdosproblems.com/tags/additive%20combinatorics "
  
    Erdős Problems
  
"