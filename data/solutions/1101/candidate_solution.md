This is essentially Erdős’s problem about **gaps between (\mathcal B)-free numbers** [[nomath]](here $\mathcal B={u_i}$)[[/nomath]]: the set
$
\\{a_1<a_2<\cdots\\}=\\{n\ge1:\ \forall i,\ u_i\nmid n\\}
$
has natural density
[
\delta:=\prod_{i}\\(1-\frac1{u_i}\\)\in(0,1],
]
and the question is whether one can make the **maximal gap** up to $x$ essentially as small as the “sieve lower bound scale” (t_x/\delta).

### What is known unconditionally

1. **There is always a matching lower bound of the same shape.**
   An “easy sieve argument” gives, for every such pairwise coprime ({u_i}) with (\sum 1/u_i<\infty),
   $
   \max_{a_k<x}(a_{k+1}-a_k)>(1+o(1))t_x\delta^{-1}
   $
   as (x\to\infty). In other words, (t_x\delta^{-1}) is a universal obstruction, and your “good” condition asks for sequences where this obstruction is essentially sharp. ([Erdős Problems][1])

2. **Good sequences do exist, but Erdős’s construction is very sparse.**
   Erdős proved that there exist good sequences; in fact he constructs examples where **all (u_i) are primes** [[nomath]](a very sparse subsequence of primes so that $\sum 1/u_i<\infty$)[[/nomath]]. 
   The method is: choose the primes (u_i=p_i) tending to infinity “sufficiently fast”, then use a sieve lower bound to show every interval $(x,x+L)$ of the target length contains an integer avoiding all the (p_i)’s that can matter up to that scale. 
   As noted on the ErdosProblems discussion, the growth needed in that proof is extremely fast [[nomath]](heuristically something like doubly-exponential growth $2^{2^n}$ already works for the argument)[[/nomath]], and even getting down to merely exponential growth would be a big improvement over what is currently justified by that approach. ([Erdős Problems][1])

### Your two growth questions

#### $A$ Is there a good sequence with (u_n < n^{O(1)})?

**Open.** Erdős explicitly raised essentially this question [[nomath]](“say $u_i<i^C$ for an absolute constant $C$”)[[/nomath]] and said he **did not expect** such a sequence exists. 

A key “test case” here is the natural polynomial-growth choice
[
u_i = p_i^2
]
(prime squares), for which the ({a_k}) are the **squarefree numbers**. The ErdosProblems page notes that a “strong form” of another Erdős problem asks exactly whether the prime squares form a good sequence. ([Erdős Problems][1])
At present, this is not settled.

#### $B$ Is there a good sequence with (u_n \le e^{o(n)})?

**Also open.** Erdős stated he was “fairly sure” there *is* a good sequence with
[
u_n^{1/n}\to 1,
]
which is the same as (u_n \le e^{o(n)}). 
But this has not been proved (at least not in the references tracked there as of the most recent edits).

### Why this is hard even in the prime-squares (squarefree) model

For (\mathcal B={p^2}), one can **construct** infinitely many squarefree-free intervals of length (\asymp \frac{\log x}{\log\log x}) by CRT [[nomath]](this is the same scale as $t_x$ for $u_i=p_i^2$)[[/nomath]]. ([MathOverflow][2])
But the best **unconditional upper bounds** guaranteeing a squarefree number in every interval are vastly larger: e.g. Pandey (2024) proves there exists (\eta>0) such that every interval $[X,X+X^{1/5-\eta}]$ contains a squarefree number for all large $X$. ([arXiv][3]) [[nomath]](Earlier explicit bounds of the shape $X^{1/5}\log X$ also exist, but are still far from polylogarithmic scales.)[[/nomath]] ([arXiv][4])
So we are very far from the kind of near-optimal “(t_x/\delta)” control that your definition of “good” demands in polynomial-growth regimes.

### Bottom line

* **Yes, good sequences exist** (Erdős constructed them with very rapidly growing primes). 
* **Polynomial growth (u_n<n^{O(1)}): open**, and Erdős expected **no**. 
* **Subexponential growth (u_n\le e^{o(n)}): open**, and Erdős expected **yes**. 

If you want, I can also unpack how Erdős’s sieve proof forces the “very fast growth” condition [[nomath]](where it enters, and what would need to be strengthened to push it down toward $e^{o(n)}$ or $n^{O(1)}$)[[/nomath]].

[1]: https://www.erdosproblems.com/forum/discuss/1101 "

    Erdős Problem #1101 - Discussion thread

"
[2]: https://mathoverflow.net/questions/149194/consecutive-non-squarefree-integers?utm_source=chatgpt.com "nt.number theory - Consecutive non squarefree integers"
[3]: https://arxiv.org/abs/2401.13981?utm_source=chatgpt.com "Squarefree numbers in short intervals"
[4]: https://arxiv.org/abs/2211.09975?utm_source=chatgpt.com "Explicit bounds for large gaps between squarefree integers"
