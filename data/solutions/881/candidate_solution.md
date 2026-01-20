Interpreting “basis of order $k$” in the standard *asymptotic* sense [[nomath]](every sufficiently large integer is a sum of $k$ elements of $A$, repetitions allowed)[[/nomath]], this is a known open problem.

It is recorded as **Erdős Problem #881** (attributed to Erdős 1998 / Burr–Erdős) and is currently listed as **open**: ([Erdős Problems][1])

### One easy case: $k=1$ is yes

If $k=1$, then $A$ being a basis of order $1$ means $A$ is cofinite: there is (N_0) with ([N_0,\infty)\subset A). Your “infinite-deletion minimality” condition is automatic for any cofinite set.

Construct an infinite (B\subset A) so that (A\setminus B) is a basis of order $2$ as follows:

* Fix (M\ge 1) and keep the whole block $[N_0,N_0+M]$ inside (A\setminus B).
* Let (B={b_1<b_2<\cdots}\subset [N_0+M+1,\infty)) be any infinite set with gaps (b_{i+1}-b_i>M) [[nomath]](e.g. an arithmetic progression with step $M+1$)[[/nomath]].

Let (C=A\setminus B). For any (n\ge 2N_0+M), consider the $M+1$ candidates
[
n-(N_0+M), n-(N_0+M-1),\dots, n-N_0.
]
They form an interval of length $M$. Since $B$ has gaps (>M), **at most one** of these numbers can lie in $B$, so at least one lies in $C$; call it $b$. Then (a=n-b\in [N_0,N_0+M]\subset C), and (n=a+b) is a sum of two elements of $C$. Hence $C$ is an asymptotic basis of order $2$.

So for $k=1$, the answer is **yes**.

### For (k\ge 2): open

For higher order, the question is genuinely nontrivial and (as far as the current literature record indicates) **unsolved** in general. ([Erdős Problems][1])

A bit of context: sets with very strong “infinite-deletion” fragility have been studied under names like (\aleph_0)-minimal bases (where deleting *any* infinite subset destroys the basis property, while deleting any finite subset does not). Such examples are known for order $2$. ([Rényi Institute][2]) But even in that setting, whether one can delete an infinite subset and still retain a basis of order $3$ is essentially the $k=2$ instance of your question, and it remains open.

So the best current answer is:

* **$k=1$:** yes (constructive argument above).
* **(k\ge 2):** **open** in general (Erdős Problem #881). ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/881 "https://www.erdosproblems.com/881"
[2]: https://renyi.hu/~p_erdos/1979-02.pdf "https://renyi.hu/~p_erdos/1979-02.pdf"
