This is (to my knowledge) still **open** in the form you stated it: it is listed as Erdős problem **#839** (“no term is the sum of a consecutive block of earlier terms”), and neither of your two limits is presently known to hold in full generality. ([Erdős Problems][1])

That said, there is a fair amount known about *how dense such sequences can be*, which gives some context for why your two strengthenings are nontrivial.

## What is known

Let (A={a_1<a_2<\cdots}), and write (A(x)=|{n:\ a_n\le x}|). Then:

* Your first question
  [
  \limsup_{n\to\infty}\frac{a_n}{n}=\infty
  ]
  is equivalent to saying the **lower asymptotic density** of $A$ is $0$, i.e.
  [
  \liminf_{x\to\infty}\frac{A(x)}{x}=0
  ]
  [[nomath]](since roughly $A(a_n)\approx n$)[[/nomath]].

* Your second question asks that the **logarithmic density** of $A$ is $0$:
  $
  \lim_{x\to\infty}\frac{1}{\log x}\sum_{a_n<x}\frac1{a_n}=0.
  $

Erdős already observed that one can make the sequence “locally dense” infinitely often:

* It is “easy to see” that (\liminf a_n/n<\infty) is possible, and one can even arrange
  $
  \sum_{a_n<x}\frac1{a_n}\gg \log\log x.
  $
  ([Erdős Problems][1])

* The **upper density** [[nomath]](i.e. $\limsup_{x\to\infty} A(x)/x$)[[/nomath]] can be $1/2$, and Erdős conjectured it might not exceed $1/2$; that conjecture is false: **Freud (1993)** constructed an example with upper density (19/36>1/2). ([Erdős Problems][1])

There are also sharp(er) results for the **finite analogue** [[nomath]](maximal $|A|\subseteq{1,\dots,N}$ with the same “no consecutive-sum lands back in $A$” property)[[/nomath]]:

* A simple argument of Adenwalla gives (|A|\le \tfrac23N+O(\log N)). ([Erdős Problems][2])
* Coppersmith–Phillips (1996) improved this to
  [
  |A|\le\left(\frac23-\frac1{512}\right)N+\log N,
  ]
  and also gave a construction with
  [
  |A|\ge \frac{13}{24}N-O(1).
  ]
  ([Erdős Problems][2])

These density statements show that the constraint is not “rare-event” restrictive in a naive sense; it allows fairly large initial segments, which is why forcing *global* sparseness (your two limits) is difficult.

## A concrete example illustrating Erdős’s remarks

Here is a standard “block” construction showing simultaneously:

* (\liminf a_n/n) can be bounded (so the sequence can be quite dense infinitely often), and
* (\sum_{a_n<x}1/a_n) can grow like (\log\log x).

Define (B_1=4) and (B_{k+1}=B_k^3). Let
[
I_k=(\frac{B_k}{2},B_k]\cap\mathbb{N}=\\{\frac{B_k}{2}+1,\dots,B_k\\},
\qquad
A=\bigcup_{k\ge1} I_k,
]
and enumerate $A$ increasingly as (a_1<a_2<\cdots).

**Why the “no consecutive-sum” property holds.**
Fix (x\in I_k).

* Any sum of **two or more** elements of (I_k) exceeds (B_k), because the two smallest elements in (I_k) already sum to
  [
  (\frac{B_k}{2}+1)+(\frac{B_k}{2}+2)=B_k+3>B_k,
  ]
  so no consecutive sum using (\ge2) terms from (I_k) can equal (x\le B_k).

* Any sum of consecutive earlier terms that uses **only earlier blocks** (I_1,\dots,I_{k-1}) is at most the total sum of those blocks, which is $O(B_{k-1}^2)$, while the smallest element of (I_k) is about (B_k/2=B_{k-1}^3/2), much larger [[nomath]](since $B_k=B_{k-1}^3$)[[/nomath]]. In particular the first element of (I_k) exceeds the sum of everything before it, so it cannot be represented, and then neither can any larger (x\in I_k).

* Any consecutive sum that “crosses” from earlier blocks into (I_k) must include the first element of (I_k), and if it includes any additional element of (I_k) it already exceeds (B_k), so it cannot hit (x\in I_k).

So no (a_i) is a sum of consecutive earlier (a_j).

**Densities and reciprocal sums.**

* Each block (I_k) has size (|I_k|=B_k/2), and because (B_k) grows so fast, the count $A(B_k)$ is dominated by (|I_k|), giving (A(B_k)\sim B_k/2). Thus along the subsequence (n=A(B_k)) one has (a_n=B_k) and (a_n/n\sim 2), so (\liminf a_n/n\le 2).

* The reciprocal sum over each block satisfies
  [
  \sum_{m\in I_k}\frac1m=\sum_{m=B_k/2+1}^{B_k}\frac1m=\log 2+o(1),
  ]
  so up to (x=B_k) the sum is (\sim k\log 2). Since (B_k) is about (\exp(c\cdot 3^{k})), we have (k\asymp \log\log x), hence
  $
  \sum_{a_n<x}\frac1{a_n}\asymp \log\log x.
  $
  This matches Erdős’s remark (\sum_{a_n<x}1/a_n\gg\log\log x). ([Erdős Problems][1])

[[nomath]](And note: in this example the logarithmic-density ratio $\frac{1}{\log x}\sum_{a_n<x}1/a_n$ does go to $0$, because $\log\log x=o(\log x)$.)[[/nomath]]

## Where this leaves your two questions

* The known constructions [[nomath]](including Freud’s $19/36$ upper-density example)[[/nomath]] show the family is “dense enough” that ruling out **bounded (\limsup a_n/n)** is genuinely subtle. ([Erdős Problems][1])
  At present, **it is not known** whether every such sequence must have (\limsup a_n/n=\infty). ([Erdős Problems][1])

* The logarithmic-density question is also open in this generality [[nomath]](and is strictly stronger than merely forcing natural density $0$, since even sets of density $0$ like the primes have positive logarithmic density)[[/nomath]]. The problem is posed exactly in this form as Erdős #839. ([Erdős Problems][1])

If you want, I can also summarize what is known/expected for the **greedy** version (Erdős #359 / OEIS A002048), which is a related but different problem. ([Erdős Problems][3])

[1]: https://www.erdosproblems.com/latex/839 "
  
    Erdős Problems
  
"
[2]: https://www.erdosproblems.com/latex/867 "
  
    Erdős Problems
  
"
[3]: https://www.erdosproblems.com/tags/number%20theory "
  
    Erdős Problems
  
"
