As far as I can tell from the current literature, this is **open**: it is listed as **Erdős Problem #1035** (asked in [Er93]) and no constant (c>0) is currently known (nor is there a known counterexample ruling out all constants). ([Erdős Problems][1])

### A standard “baseline” bound [[nomath]](but $c$ depends on $n$)[[/nomath]]

Let (N=2^n). Your minimum–degree hypothesis
[
\delta(G)>(1-c)N
]
is equivalent to saying the complement (\overline G) has maximum degree
[
\Delta(\overline G)<cN.
]

Now use a classical graph *packing* theorem of **Sauer–Spencer (1978)**:

> If $G,H$ are graphs on $N$ vertices and (2\Delta(G)\Delta(H)<N), then $G$ and $H$ pack [[nomath]](equivalently $H$ embeds into $\overline G$)[[/nomath]]. 

Apply this with (G=\overline{G}) and (H=Q_n). Since (\Delta(Q_n)=n), the condition becomes
[
2,\Delta(\overline G),n < N.
]
So it is enough that (\Delta(\overline G) < \frac{N}{2n}), i.e.
[
\delta(G) ;>; N-\frac{N}{2n}=\\(1-\frac1{2n}\\)2^n.
]
This proves the statement with (c=\frac1{2n}), but **not** with an absolute constant $c$ independent of $n$. 

### What’s known beyond that?

Erdős himself suggested related “weaker” follow-up problems if the constant-$c$ statement fails: allowing **more than** (2^n) vertices, or replacing (c2^n) by a function (u_n) in a condition (\delta(G)>2^n-u_n). ([Erdős Problems][1])

There is also informal discussion (and some evidence from dependent-random-choice–type methods) suggesting that if you allow (m>2^n) vertices, then one expects an embedding once $m$ is about (2^n(1-c)^{-n}) (up to constants/parameter losses). ([Erdős Problems][2]) Work of Tikhomirov on Ramsey numbers of the hypercube develops embedding procedures for (Q_n) in certain dense bipartite settings using dependent random choice and other structure, which is relevant to these “more vertices than (2^n)” variants, but does **not** settle the original constant-$c$ minimum-degree question for graphs on exactly (2^n) vertices. ([arXiv][3])

### Bottom line

* **No** absolute constant (c>0) is currently known to work, and no proof is known that none exists. The problem is **open**. ([Erdős Problems][1])
* The best “off-the-shelf” guarantee from packing gives $c$ on the order of $1/n$ [[nomath]](e.g. $c=\frac1{2n}$)[[/nomath]]. 

[1]: https://www.erdosproblems.com/1035 "https://www.erdosproblems.com/1035"
[2]: https://www.erdosproblems.com/forum/discuss/1035 "

    Erdős Problem #1035 - Discussion thread

"
[3]: https://arxiv.org/pdf/2208.14568 "https://arxiv.org/pdf/2208.14568"
