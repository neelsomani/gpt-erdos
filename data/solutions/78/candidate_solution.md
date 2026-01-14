Let (R(k)) mean the *diagonal* Ramsey number (R(k,k)): the smallest (n) such that **every** red/blue coloring of the edges of (K_n) contains a monochromatic (K_k).

I will give a **deterministic construction** (an algorithm) that, for each (k), produces a coloring on about (2^{k/2}) vertices with **no** monochromatic (K_k). This shows
[
R(k) > C^k \quad \text{for } C=\sqrt 2>1.
]

---

## Step 1: A random coloring would have < 1 bad (K_k) “on average”

Fix (k\ge 3). Let
[
n=\Big\lfloor 2^{k/2}\Big\rfloor,
]
and look at (K_n).

Color each edge independently red or blue with probability (1/2).
Let (X) be the number of monochromatic (K_k)’s (all-red or all-blue) in the result.

For a fixed (k)-set of vertices (S), there are (\binom{k}{2}) edges inside (S). The probability that all those edges are red is ((1/2)^{\binom{k}{2}}), and same for all blue. So
[
\Pr(S\text{ is monochromatic}) ;=; 2\cdot \left(\frac12\right)^{\binom{k}{2}}
;=; 2^{,1-\binom{k}{2}}.
]
There are (\binom{n}{k}) choices of (S), so by linearity of expectation,
[
\mathbb E[X] ;=; \binom{n}{k},2^{,1-\binom{k}{2}}.
]

Now bound (\binom{n}{k}\le \dfrac{n^k}{k!}) and use (n\le 2^{k/2}):
[
\mathbb E[X]
;\le;
\frac{n^k}{k!},2^{,1-\binom{k}{2}}
;\le;
\frac{2^{k^2/2}}{k!},2^{,1-\frac{k(k-1)}2}
;=;
\frac{2^{,1+k/2}}{k!}.
]
For (k=3), this is (\dfrac{2^{2.5}}{6}<1). And for larger (k), (k!) grows faster, so the value stays (<1). (You can make it formal by a one-line induction: if (k!>2^{1+k/2}) then ((k+1)!=(k+1)k!>\sqrt2\cdot 2^{1+k/2}=2^{1+(k+1)/2}).)

So we have shown:
[
\mathbb E[X] < 1.
]

That means: **there exists** a coloring with (X=0).
Now we turn this existence into an **explicit construction**.

---

## Step 2: Make it constructive (deterministic) by “choosing the next edge” wisely

List the edges of (K_n) as (e_1,e_2,\dots,e_m) where (m=\binom{n}{2}).

We will color them one by one, deterministically.

### Define the “potential” we keep small

For any **partial** coloring (\phi) (some edges already colored, some not), define (F(\phi)) to be:

> the expected number of monochromatic (K_k)’s after we finish coloring the remaining edges by fair coin flips.

So (F(\phi)) is a conditional expectation.

You can compute (F(\phi)) by summing over all (k)-vertex sets (S):

* If inside (S) we already have **both** colors among the colored edges, then (S) can never become monochromatic, so its contribution is (0).
* If the colored edges inside (S) are all red (and none blue), and there are (u(S)) uncolored edges inside (S), then (S) will end up monochromatic exactly if all those (u(S)) edges become red, which has probability (2^{-u(S)}). Same if “all blue”.
* If no edges in (S) are colored yet, the probability is the original (2^{1-\binom{k}{2}}).

Then
[
F(\phi)=\sum_{S\in\binom{[n]}{k}} \Pr(S\text{ ends monochromatic}\mid \phi).
]

Initially (no edges colored), (F(\emptyset)=\mathbb E[X]<1).

### The key greedy step

Suppose we have a partial coloring (\phi) and the next edge is (e_i). Let:

* (\phi_R) be (\phi) plus the choice “(e_i) is red”,
* (\phi_B) be (\phi) plus the choice “(e_i) is blue”.

Then
[
F(\phi) ;=; \frac{F(\phi_R)+F(\phi_B)}{2},
]
because if we were to color (e_i) by a fair coin and then finish randomly, that would match the definition of (F(\phi)).

So at least one of (F(\phi_R)) or (F(\phi_B)) is (\le F(\phi)).
We choose that color.

This guarantees (F(\phi)) never increases, and stays (<1) throughout the whole process.

### Finish

After all edges are colored, there is no randomness left. So (F(\phi)) equals the **actual** number of monochromatic (K_k)’s in the final coloring. Call that number (X_{\text{final}}). Then:

* (X_{\text{final}}) is an integer,
* but also (X_{\text{final}}=F(\phi)<1).

So (X_{\text{final}}=0). We have **constructed** a coloring of (K_n) with **no** monochromatic (K_k).

---

## Step 3: Turn it into a Ramsey lower bound

We built a red/blue coloring of (K_n) with no monochromatic (K_k), where (n=\lfloor 2^{k/2}\rfloor). That means
[
R(k) > n = \lfloor 2^{k/2}\rfloor,
]
so in particular
[
R(k) \ge \lfloor 2^{k/2}\rfloor + 1 ;>; 2^{k/2} ;=; (\sqrt 2)^k.
]

So you can take
[
C=\sqrt 2>1,
]
and the proof is constructive: it gives a deterministic step-by-step way to build the coloring.
