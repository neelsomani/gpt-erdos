Fix moduli (A={n_1<\cdots<n_r}) and choose residue classes
[
C_i={m\in\mathbb Z:m\equiv a_i\pmod{n_i}}.
]
Let (U(a_1,\dots,a_r)=\bigcup_{i=1}^r C_i). If (L=\mathrm{lcm}(n_1,\dots,n_r)), then (U) is periodic mod (L), hence it has a (natural) density and
$
d(U(a_1,\dots,a_r))=\frac{|{0\le x<L:\exists i,\ x\equiv a_i\ (\mathrm{mod}\ n_i)}|}{L}.
$

## The minimum density

Yes: the minimum density is achieved when all the (a_i) are equal [[nomath]](equivalently, when the classes $a_i\pmod{n_i}$ have a common integer in their intersection, i.e. the system $x\equiv a_i\ (\mathrm{mod}\ n_i)$ is simultaneously solvable)[[/nomath]].

More precisely, Simpson proved (and Sun cites it as Lemma 2.3 of Simpson) that for any choice of residues (a_i),
[
d!\left(\bigcup_{i=1}^r a_i(n_i)\right)\ \ge\ d!\left(\bigcup_{i=1}^r 0(n_i)\right),
]
so the union is *smallest* when the residue classes are “aligned” (all equal up to a global shift). ([ResearchGate][1])

When all residues are equal [[nomath]](say $a_i=0$ after shifting)[[/nomath]], every intersection (\bigcap_{i\in I} 0(n_i)) is the set of multiples of (\mathrm{lcm}(n_i:i\in I)), so it has density (1/\mathrm{lcm}(n_i:i\in I)). Therefore inclusion–exclusion gives the exact minimum value:
[
d_{\min}(A)
=\sum_{\emptyset\neq I\subseteq{1,\dots,r}} (-1)^{|I|+1},\frac{1}{\mathrm{lcm}(n_i:i\in I)}.
]
This is exactly the alternating “(\sum 1/n_i-\sum 1/[n_i,n_j]+\cdots)” expression mentioned on the Erdős-problems page. ([Erdős Problems][2])

## The maximum density

For the **maximum** over choices of residues,
[
d_{\max}(A)=\max_{a_1,\dots,a_r} d!\left(\bigcup_{i=1}^r a_i(n_i)\right),
]
there is **no general closed-form answer known**; it is recorded as an open Erdős–Graham problem (Erdős Problem #278). ([Erdős Problems][2])

What *is* known are general bounds and exact formulas in important special cases:

### General bounds (always true)

1. Trivial upper bound (union bound):
   [
   d_{\max}(A)\le \min!\left(1,\ \sum_{i=1}^r \frac1{n_i}\right).
   ]

2. A universal **lower bound** (greedy/averaging argument):
   [
   d_{\max}(A)\ \ge\ 1-\prod_{i=1}^r\left(1-\frac1{n_i}\right).
   ]
   Equivalently, if (\delta^{-}(A)) denotes the *minimum* uncovered density, then
   [
   \delta^{-}(A)\le \prod_{i=1}^r\left(1-\frac1{n_i}\right),
   ]
   which is (1.1) in Filaseta–Ford–Konyagin–Pomerance–Yu. 

3. A (sometimes useful) **upper bound** coming from a universal *lower bound on the uncovered density*:
   for every choice of residues, the uncovered density (\delta) satisfies
   $
   \delta\ \ge\ \prod_{i=1}^r(1-\frac1{n_i});-!!\sum_{\substack{i<j\ \gcd(n_i,n_j)>1}}\frac1{n_i n_j},
   $
   so
   $
   d_{\max}(A)\le 1-\prod_{i=1}^r(1-\frac1{n_i});+!!\sum_{\substack{i<j\ \gcd(n_i,n_j)>1}}\frac1{n_i n_j}.
   $
   This is (1.2) in the same paper. 

These bounds can be far from tight in either direction, depending on the arithmetic structure of (A).

### Special cases where (d_{\max}(A)) is explicit

**Pairwise coprime moduli.**
If (\gcd(n_i,n_j)=1) for all (i\ne j), then *every* collection of residue classes has the same intersection pattern (by CRT), and the density is independent of the (a_i). In that case
[
d_{\max}(A)=d_{\min}(A)=1-\prod_{i=1}^r\left(1-\frac1{n_i}\right).
]
[[nomath]](This is exactly inclusion–exclusion with $\mathrm{lcm}$ replaced by products.)[[/nomath]]

**All moduli are powers of one prime (p).**
If each (n_i=p^{e_i}), then you can choose the residue classes so that they are essentially “prefix-disjoint” in base (p), and you can achieve disjointness up to total measure (1). In this case one can show
[
d_{\max}(A)=\min!\left(1,\ \sum_{i=1}^r \frac1{n_i}\right).
]
[[nomath]](Example: for $\\{2,4\\}$ you can take $0\pmod 2$ and $1\pmod 4$ to get density $1/2+1/4=3/4$.)[[/nomath]]

### Why a general formula is hard

Recent work notes that even for structured families, optimizing the uncovered density can reduce to hard partition/knapsack-type optimization. For instance, for sets like ({3}\cup{3p:p\in P}), the optimal uncovered density depends on how you partition the primes (P) into two parts, and can be written in terms of products (\prod_{p\in P_j}(1-1/p)); this sensitivity is used to argue against a single “nice” universal formula. ([arXiv][3])

---

### Summary

* **Minimum density:** yes, it is achieved when all (a_i) are equal (up to a common shift), and the minimum equals the full inclusion–exclusion expression with (\mathrm{lcm})’s. ([ResearchGate][1])
* **Maximum density:** in general there is no known closed-form expression; the problem is open in full generality. There are sharp formulas in special cases (e.g. pairwise coprime moduli; single-prime-power moduli) and useful general bounds such as (d_{\max}\ge 1-\prod(1-1/n_i)). 

[1]: https://www.researchgate.net/publication/2301826_A_Theorem_Concerning_Systems_Of_Residue_Classes "(PDF) A Theorem Concerning Systems Of Residue Classes"
[2]: https://www.erdosproblems.com/278 "
  
    Erdős Problem #278
  
"
[3]: https://arxiv.org/pdf/2508.18270 "Proving it is impossible; on Erd\H{o}s problem $\\# 278$"
