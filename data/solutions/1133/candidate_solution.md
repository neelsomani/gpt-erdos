What you wrote is exactly the conjecture Erdős posed at the end of his 1967 paper on Lagrange interpolation. He explicitly calls it “probably” true and adds: *“I have not even proved it if $m=n$.”* ([Renyi Institute][1])  It is also listed as **open** on the Erdős Problems site. ([Erdős Problems][2])

So there isn’t a known complete proof in the literature (as of what’s visible from those sources). Still, there is a very close, classical statement that *is* provable and captures the same “choose (y_i) to force blow-up” philosophy; I’ll prove that in full, and then explain precisely where the extra “((1+\varepsilon)n) degree” and “((1-\varepsilon)n) matches” makes the conjecture genuinely harder.

## A fully provable cousin: exact interpolation with degree $n-1$

Fix $n$ and any points (x_1,\dots,x_n\in[-1,1]) (for simplicity assume they are distinct; duplicates only make it easier to force contradictions by choosing incompatible values on equal nodes).

Let $I$ be the Lagrange interpolation operator of degree (\le n-1): for data (y=(y_1,\dots,y_n)), the interpolating polynomial is
[
(Iy)(x)=\sum_{i=1}^n y_i,\ell_i(x),
]
where (\ell_i) are the Lagrange basis polynomials,
[
\ell_i(x)=\prod_{j\ne i}\frac{x-x_j}{x_i-x_j},\qquad \ell_i(x_j)=\delta_{ij}.
]

Define the **Lebesgue function** and **Lebesgue constant**
[
L(x):=\sum_{i=1}^n|\ell_i(x)|,\qquad \Lambda_n:=\max_{x\in[-1,1]}L(x).
]

### Step 1: Choose $y$ that forces (|Iy|_\infty=\Lambda_n)

Pick (x^\ast\in[-1,1]) where $L(x)$ attains its maximum, so (L(x^\ast)=\Lambda_n).

Define
[
y_i:=\operatorname{sgn}(\ell_i(x^\ast))\in{-1,+1}\subset[-1,1],
]
[[nomath]](with any choice if $\ell_i(x^\ast)=0$)[[/nomath]]. Then
[
(Iy)(x^\ast)=\sum_{i=1}^n y_i,\ell_i(x^\ast)=\sum_{i=1}^n |\ell_i(x^\ast)|=L(x^\ast)=\Lambda_n.
]
Therefore
[
|Iy|_{L^\infty@@MATH_0@@}\ \ge\ |(Iy)(x^\ast)|\ =\ \Lambda_n.
]

So for these (y_i\in[-1,1]), **any** polynomial $P$ of degree (\le n-1) that interpolates all points [[nomath]](i.e. $P(x_i)=y_i$ for every $i$)[[/nomath]] must equal (Iy), hence must satisfy
[
\max_{x\in[-1,1]}|P(x)|\ge \Lambda_n.
]

### Step 2: (\Lambda_n) is always (\gtrsim \log n)

A classical lower bound says that **for every choice** of $n$ nodes in $[-1,1]$,
[
\Lambda_n \ \ge\ \frac{2}{\pi}\log n + 0.521\ldots
]
(as stated, for example, in a survey on Lebesgue constants). ([People][3])

Combining Step 1 and Step 2:

> For any fixed (C>0), once $n$ is large enough that (\Lambda_n>C), there exist (y_1,\dots,y_n\in[-1,1]) such that **every** degree (\le n-1) interpolant through $(x_i,y_i)$ must have (\max_{[-1,1]}|P|>C).

This is a complete “choose $y$ to force blow-up” theorem—just without the “ignore (\varepsilon n) points” and “allow degree ((1+\varepsilon)n)” features.

## Why your exact statement is harder

Your conjecture allows:

* **More degree**: (m<(1+\varepsilon)n), so there are about (\varepsilon n) extra degrees of freedom beyond $n-1$.
* **Fewer constraints**: it only needs to match ((1-\varepsilon)n) points.

Erdős notes exactly this leap and says he could not prove it even in the borderline $m=n$ case. ([Renyi Institute][1])

One way to see the new difficulty is algebraic:

* If (S\subset{1,\dots,n}) is the matched set and (|S|=k), then any polynomial $P$ matching the values on $S$ can be written as
  [
  P = P_S + R_S\cdot Q,
  ]
  where (P_S) is a fixed interpolant of degree (\le k-1) on $S$, (R_S(x)=\prod_{i\in S}(x-x_i)) vanishes on $S$, and $Q$ is an arbitrary polynomial of degree (\le m-k).
* In your regime, (k\approx(1-\varepsilon)n) and (m-k\approx 2\varepsilon n), so there is still a **large** space of “correction terms” (R_S Q) that do not disturb the matched values but can potentially be used to keep the global sup norm under control.

The Lebesgue-constant argument above controls the unique degree $n-1$ interpolant, but in the conjectured regime you can “hide” large spikes by adding a multiple of (R_S) (or similar vanishing factors), and you can also choose *which* subset of points to match.

That is why the conjecture is not a routine extension of the classical divergence/Lebesgue-constant theory.

## Where this sits in Erdős’s paper

In the same section, Erdős states and proves a different theorem (his Theorem 4) about existence of a degree-$n$ polynomial that is small on ((1+\varepsilon)n) points but large somewhere, and then proposes your statement as a stronger principle that would imply that theorem. ([Renyi Institute][1])  The Erdős Problems site reproduces the conjecture and marks it open. ([Erdős Problems][2])

## A plausible strategy people try (and why it’s nontrivial)

A natural line of attack is probabilistic:

1. Choose (y_i) at random [[nomath]](often $\pm 1$)[[/nomath]].
2. Try to show: with high probability, **no** polynomial $P$ with (|P|_\infty\le C) and (\deg P <(1+\varepsilon)n) can agree with this random labeling on ((1-\varepsilon)n) points.

The core obstacle is that even though the class of bounded polynomials is “structured,” once $m$ is comparable to $n$, the parameter space is large and you must control **all** possible matched subsets $S$ simultaneously.

I’m spelling this out because it mirrors exactly the way the easy Lebesgue-constant proof works: we pick $y$ that makes the interpolation operator large. In the conjecture, you need a *robust* version of that largeness under:

* removing (\varepsilon n) coordinates, and
* adding (\varepsilon n) degrees of freedom.

## Bottom line

* The statement you wrote is an **Erdős conjecture from 1967** and is recorded as **open**; Erdős explicitly says he couldn’t prove it even for $m=n$. ([Renyi Institute][1])
* A closely related and fully provable result [[nomath]](degree $n-1$, match all $n$ points)[[/nomath]] follows quickly from the Lebesgue constant lower bound (\Lambda_n \gtrsim \log n). ([People][3])

If you want, I can also write down the sharpest *known* unconditional statement I can derive from standard tools (Lebesgue constants, Faber-type divergence, and/or a probabilistic construction) that goes **partway** toward the ((1+\varepsilon)n)/((1-\varepsilon)n) regime—e.g. with a much smaller allowed degree, or with a different notion of “agreement” (approximate rather than exact), or under mild spacing assumptions on the (x_i).

[1]: https://old.renyi.hu/~p_erdos/1967-20.pdf "https://old.renyi.hu/~p_erdos/1967-20.pdf"
[2]: https://www.erdosproblems.com/latex/1133 "
  
    Erdős Problems
  
"
[3]: https://people.clas.ufl.edu/hager/files/Lebesgue.pdf "https://people.clas.ufl.edu/hager/files/Lebesgue.pdf"
