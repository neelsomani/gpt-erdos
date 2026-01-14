Let me write $R(G)$ for the usual *diagonal* Ramsey number $R(G,G)$, and $R(k)$ for (R(K_k,K_k)).

### Status

As far as I know (and as recorded in standard Erdős-problem compilations), **both of your statements are still open in general**. This is Erdős’s problem #87 in Bloom’s Erdős Problems list. ([Erdős Problems][1])

### What is known

#### 1) The “best possible” bound (R(G)\ge R(k)) is false

Erdős originally conjectured that among graphs with (\chi(G)=k), the clique (K_k) minimizes the Ramsey number, i.e. (R(G)\ge R(k)). That conjecture already fails for (k=4): Faudree and McKay proved that the *pentagonal wheel* (W_6) satisfies
[
\chi(W_6)=4,\qquad R(W_6)=17<18=R(4).
]
([Erdős Problems][1])

So one cannot take (c=1) in your “even stronger” question.

#### 2) A general lower bound (R(G)\ge 2^{\Omega(k)})

There is a general lower bound (attributed in the Erdős-problem notes to Yuval Wigderson) that for **every** graph (G) with (\chi(G)=k),
[
R(G)\gg 2^{k/2}.
]
([Erdős Problems][1])

Here is a clean proof sketch (with an explicit constant), since it explains why (2^{k/2}) shows up:

* Let (H\subseteq G) be a *(k)-critical* subgraph (minimal with chromatic number (k)).
* A standard fact about (k)-critical graphs is that their minimum degree satisfies (\delta(H)\ge k-1). ([ETSU Faculty][2])
  Hence if (v=|V(H)|) and (e=e(H)), then (2e\ge (k-1)v), i.e. $e\ge \frac{k-1}{2}v$.
* Now 2-color the edges of (K_N) uniformly at random. A fixed labeled copy of $H$ becomes monochromatic with probability (2\cdot 2^{-e}=2^{1-e}). The number of labeled copies is at most (N^v). So
  [
  \mathbb{E}[#\text{ monochromatic copies of }H]
  ;\le; N^v\cdot 2^{1-e}
  ;\le; N^v\cdot 2^{1-\frac{k-1}{2}v}
  ;=;2\Bigl(\frac{N}{2^{(k-1)/2}}\Bigr)^v.
  ]
* Since (v\ge k), if you take (N=2^{(k-1)/2}/2), then the expectation is at most (2\cdot (1/2)^k<1). So there exists a coloring with **no** monochromatic copy of $H$, hence no monochromatic copy of $G$. Therefore
  [
  R(G)\ge R(H) > N \asymp 2^{k/2}.
  ]

This is the kind of argument the Erdős-problem notes refer to. ([Erdős Problems][1])

#### 3) Why this doesn’t settle your comparison with $R(k)$

We know a classical general upper bound (R(k)\le 4^k), and this makes your first inequality trivial for large (\epsilon) [[nomath]](e.g. $\epsilon\ge 3/4$ is explicitly noted in the Erdős-problem writeup)[[/nomath]]. ([Erdős Problems][1])

But beyond such “large (\epsilon)” regimes, the comparison is hard because the true growth rate of $R(k)$ is itself famously wide open: we only know
[
2^{\Theta(k)} \le R(k)\le 4^{(1+o(1))k},
]
and the universal lower bound (R(G)\gg 2^{k/2}) matches the *exponent* in the best-known lower bounds for $R(k)$, but not enough to control the ratio $R(G)/R(k)$ in the way you ask. ([Erdős Problems][1])

### Direct answer to your two questions

* **First question** [[nomath]](for every fixed $\epsilon>0$, eventually $R(G)>(1-\epsilon)^kR(k)$ for all $\chi(G)=k$)[[/nomath]]: **open**. ([Erdős Problems][1])
  [[nomath]](It is known only in some easy parameter ranges, e.g. $\epsilon\ge 3/4$, but not in general.)[[/nomath]] ([Erdős Problems][1])

* **Second, stronger question** [[nomath]](exist $c>0$ with $R(G)>cR(k)$ for all large $k$ and all $\chi(G)=k$)[[/nomath]]: **also open**. ([Erdős Problems][1])
  We only know the conjectured (c=1) is false already at (k=4) [[nomath]](wheel $W_6$)[[/nomath]]. ([Erdős Problems][1])

If you’d like, I can also rephrase these questions in terms of the function
[
m(k)=\min{R(G):\chi(G)=k},
]
so your two questions become (1) whether $m(k)/R(k)$ is at least $(1-\epsilon)^k$ for all (\epsilon>0) eventually, and (2) whether $m(k)/R(k)$ stays bounded away from $0$. The known facts above say $m(k)$ lies between (\asymp 2^{k/2}) and $R(k)$, but the asymptotic ratio is not known. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/latex/87 "
  
    Erdős Problems
  
"
[2]: https://faculty.etsu.edu/gardnerr/5340/Beamer-Bondy-Murty-GT/Proofs-BM-GT-14-2.pdf?utm_source=chatgpt.com "14.2. Critical Graphs—Proofs of Theorems"
