The inequality you ask for is **not true** (with your definition of (R(n;k,r))). In fact, already for (r=2) one can build 2‑colourings where **every** (n)-set contains **both** a red triangle and a blue triangle, as long as (N) is of the form (C^n). So (R(n;3,2)) grows at least exponentially in (n), and therefore it cannot be (<C^{\sqrt n}). This observation is recorded in the discussion of this Erdős–Gyárfás problem. ([Erdős Problems][1])

Below is a clean probabilistic proof (and it works for every fixed (r\ge 2), not just (r=2)).

---

## Step 1: A packing of many edge-disjoint triangles in (K_n)

**Lemma.** The complete graph (K_n) contains at least
[
m ;\ge; \frac{n(n-2)}{12}
]
**edge-disjoint** triangles.

**Proof.** Start with (K_n). Repeatedly do this: if the current graph contains a triangle, pick one triangle and delete its 3 edges. Continue until no triangle remains. At the end we have a triangle‑free graph (H) on (n) vertices.

By Mantel’s theorem, any triangle‑free graph on (n) vertices has at most (\lfloor n^2/4\rfloor) edges. ([MIT OpenCourseWare][2])
So the final graph (H) has at most (n^2/4) edges.

We started with (|E(K_n)|=\frac{n(n-1)}{2}) edges, so we deleted at least
[
\frac{n(n-1)}{2} ;-; \frac{n^2}{4}
;=; \frac{n(n-2)}{4}
]
edges. Each deleted triangle removes exactly 3 edges, and the triangles are edge‑disjoint by construction. Therefore the number (m) of deleted triangles satisfies
[
3m ;\ge; \frac{n(n-2)}{4}
\quad\Longrightarrow\quad
m ;\ge; \frac{n(n-2)}{12}.
]
Done.

---

## Step 2: Random (r)-colouring and a “bad event” for one (n)-set

Now colour the edges of (K_N) randomly: each edge gets one of (r) colours independently and uniformly.

Fix:

* a vertex set (S\subseteq [N]) with (|S|=n),
* a colour (c\in{1,\dots,r}).

Inside (S), by the lemma, pick (m\ge n(n-2)/12) edge‑disjoint triangles.

For one fixed triangle, the probability it is **monochromatic of colour (c)** is
[
\left(\frac1r\right)^3=\frac{1}{r^3}
]
(because it has 3 edges, independent).

Because the triangles are edge‑disjoint, these events are independent. So the probability that **none** of those (m) triangles is monochromatic colour (c) is
[
\left(1-\frac{1}{r^3}\right)^m
;\le;
\exp!\left(-\frac{m}{r^3}\right)
;\le;
\exp!\left(-\frac{n(n-2)}{12r^3}\right).
]

So for a fixed (S), the probability that (S) is missing a monochromatic triangle in **at least one** colour is at most
[
r\exp!\left(-\frac{n(n-2)}{12r^3}\right)
]
(by a union bound over the (r) colours).

Call such an (S) “good” (good for your definition: it avoids a triangle in some colour).

---

## Step 3: Union bound over all (n)-sets

Let (X) be the number of good (n)-vertex sets (S). Then
[
\mathbb{E}[X]
;\le;
\binom{N}{n}, r \exp!\left(-\frac{n(n-2)}{12r^3}\right).
]
Using (\binom{N}{n}\le \left(\frac{eN}{n}\right)^n), we get
[
\mathbb{E}[X]
;\le;
\left(\frac{eN}{n}\right)^n,
r \exp!\left(-\frac{n(n-2)}{12r^3}\right).
]

Now choose
[
N ;=; \left\lfloor \exp!\left(\frac{n}{24r^3}\right)\right\rfloor.
]
Then (\log N \approx \frac{n}{24r^3}), so the (\left(\frac{eN}{n}\right)^n) term contributes about (\exp!\left(\frac{n^2}{24r^3}\right)) up to lower‑order factors, while the negative term contributes (\exp!\left(-\frac{n^2}{12r^3}\right)). The negative one wins by a factor (\exp!\left(-\frac{n^2}{24r^3}\right)), so for all sufficiently large (n) (depending on (r)),
[
\mathbb{E}[X] < 1.
]

If (\mathbb{E}[X]<1), then there exists at least one colouring with (X=0), meaning:

> **No** (n)-vertex set avoids a monochromatic triangle in any colour.
> Equivalently, **every** (n)-vertex set contains a monochromatic triangle in **every** one of the (r) colours.

So for that colouring, there is **no** (n)-set which “does not contain a (K_3) in at least one colour”. Hence, by definition,
[
R(n;3,r) ;>; N ;\ge; \exp!\left(\frac{n}{24r^3}\right)
;=; \Bigl(\exp(1/(24r^3))\Bigr)^n.
]

So we proved:

[
R(n;3,r) ;\ge; C(r)^n
\quad\text{for some }C(r)>1\text{ and all large }n.
]

In particular, this contradicts any upper bound of the form (R(n;3,r)<C^{\sqrt n}).

This is exactly why the problem “prove (R(n;3,r)<C^{\sqrt n})” is listed as incorrect in the Erdős problem database (it is already false for (r=2)). ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/latex/129 "
  
    Erdős Problems
  
"
[2]: https://ocw.mit.edu/courses/18-225-graph-theory-and-additive-combinatorics-fall-2023/mit18_225_f23_lec02-05.pdf?utm_source=chatgpt.com "Graph Theory and Additive Combinatorics - Yufei Zhao"
