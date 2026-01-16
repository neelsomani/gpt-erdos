This is **not known** in full generality.

Interpreting a “permutation of (\mathbb Z)” as a bijection (\pi:\mathbb Z\to\mathbb Z) (so a doubly–infinite sequence ((\pi(i))_{i\in\mathbb Z})), a **monotone (k)-term arithmetic progression** means there exist indices (i_1<i_2<\cdots<i_k) such that the values
[
x_1=\pi(i_1),\ x_2=\pi(i_2),\ \ldots,\ x_k=\pi(i_k)
]
form an arithmetic progression and are monotone [[nomath]](WLOG increasing, $x_1<\cdots<x_k$)[[/nomath]].

What is known at present is:

* **Lower bound (k\ge 3):** One cannot avoid monotone 3-term arithmetic progressions in a doubly infinite permutation setting; in particular, Davis–Entringer–Graham–Simmons showed the positive integers cannot be arranged (even doubly infinitely) to avoid monotone 3-term APs, which implies the same for (\mathbb Z). 
  So **every** permutation of (\mathbb Z) contains a monotone 3-term arithmetic progression.

* **Upper bound (k\le 4):** There **exists** a permutation of (\mathbb Z) that avoids monotone arithmetic progressions of length **5** (improving earlier constructions that avoided length 6). 
  Therefore you **cannot** force a monotone 5-term AP in every permutation, so the largest guaranteed $k$ is at most 4.

Putting these together:
[
\boxed{3 \le k \le 4.}
]
The remaining open point is whether **every** permutation of (\mathbb Z) must contain a monotone **4**-term arithmetic progression, or whether there is a counterexample. 
