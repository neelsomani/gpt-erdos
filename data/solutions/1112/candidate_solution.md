This is **not known in general** (and in fact it is **false for some parameters**).

Here’s the current state of the problem as it appears in the literature (it is recorded as **Erdős Problem #1112**). ([Erdős Problems][1])

## What is known for (k\ge 3)

### A concrete negative case: ((k,d_1,d_2)=(3,2,3))

For $k=3$ and gap condition (2\le a_{i+1}-a_i\le 3), **no such integer $r$ exists**.

More precisely, Bollobás–Hegyvári–Jin (1997) show a very strong obstruction: for **any** increasing sequence (1\le r_1<r_2<\cdots), they construct a lacunary (B={b_i}) with
[
b_{i+1}\ge r_i b_i
]
such that for **every** $A$ with (2\le a_{i+1}-a_i\le 3), one has
[
(A+A+A)\cap B\neq\emptyset.
]
This implies that (r_3(2,3)) **does not exist**. ([Erdős Problems][1])

So, as stated, the answer to your question is **“not always”**: already for ((d_1,d_2,k)=(2,3,3)) the desired $r$ does not exist. ([Erdős Problems][1])

### General $(d_1,d_2)$ and (k\ge 3): still open

Beyond that specific negative case, the **general existence question for (r_k(d_1,d_2)) when (k\ge 3)** is currently **open** (as far as the compiled references indicate). ([Erdős Problems][1])

There are partial non-existence results in restricted regimes. For example, Tang–Yang (2021) prove that if the **difference sequence** of $A$ is of “block type” (a structured subclass of bounded-gap sequences), then for (k\ge 3) one can find a $B$ forcing (kA\cap B\ne\varnothing). 

## Context [[nomath]](why $k=2$ behaves differently)[[/nomath]]

Although you asked (k\ge 3), it’s useful context that for $k=2$ there *are* positive results in this direction: Erdős–Graham noted an avoidance construction for ((d_1,d_2)=(2,3)) under (b_{i+1}\ge 2b_i), and further sharp results were obtained later; Chen (2000) proved broad bounds for (r_2(a,b)). ([Erdős Problems][1])
This contrast is part of why the (k\ge 3) case is subtle.

## Bottom line

* For **some** $(d_1,d_2,k)$ with (k\ge 3), the answer is **no**: e.g. **$k=3$, ((d_1,d_2)=(2,3))**. ([Erdős Problems][1])
* For **general** $(d_1,d_2)$ and (k\ge 3), the existence of such an $r$ is **open**. ([Erdős Problems][1])

If you tell me your specific $(d_1,d_2,k)$, I can summarize what’s known (or unknown) for that parameter set, and how the known obstructions [[nomath]](like the $(2,3,3)$ case)[[/nomath]] might or might not generalize.

[1]: https://www.erdosproblems.com/1112 "
  
    Erdős Problem #1112
  
"
