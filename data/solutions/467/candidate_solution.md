Let me start with an important point about the *status* of this statement.

This is (essentially) **Erdős–Graham problem 467** in *Old and New Problems and Results in Combinatorial Number Theory*, and it is listed as **open** (no known published proof) on the Erdős problems archive. ([Erdős Problems][1])

So I can’t honestly give you a complete, settled proof that is known to be correct in the literature. What I *can* do right now is:

1. show you the clean reformulation that makes the difficulty transparent, and
2. prove a strong **“almost all (n<x)”** variant by a probabilistic argument (which is standard and genuinely provable), and
3. explain what a proof of the full statement would have to overcome.

---

## 1) Reformulation via CRT: one global shift

Fix $x$ and let
[
P:=\prod_{p\le x} p.
]
Given any choice of residues ({a_p}_{p\le x}), the Chinese remainder theorem gives a unique residue class (m \pmod P) such that
[
m \equiv a_p \pmod p \quad\text{for every prime }p\le x.
]
Then for any integer $n$,
[
n\equiv a_p\pmod p
\quad\Longleftrightarrow\quad
n\equiv m\pmod p
\quad\Longleftrightarrow\quad
p \mid (m-n).
]

So your condition becomes:

> Find a partition ({p\le x}=A\sqcup B) (both nonempty) and an integer $m$ such that
> for every (0\le n<x), there exist (p\in A) and (q\in B) with
> $p\mid(m-n)\quad\text{and}\quad q\mid(m-n)$
> Equivalently, every integer in the length-$x$ block
> $m-(x-1),m-(x-2),\dots,m$
> has **at least one prime divisor from $A$** and **at least one prime divisor from $B$**.

In words: you are asking for a block of $x$ consecutive integers where *each integer has prime factors in both colors*, after 2-coloring the primes (\le x).

That is exactly why this is substantially stronger than the usual “cover an interval by residue classes” / “prime gap” constructions: you’re forcing a *two-sided* $red+blue$ divisibility condition **with the same global shift $m$**.

This is the formulation that appears in the Erdős–Graham problem listing. ([Erdős Problems][1])

---

## 2) A provable near-miss: cover **almost all** (n<x)

While the “cover *every* (n<x)” statement is open, there is a clean probabilistic argument showing you can do it for **all but (O!\left(x/\sqrt{\log x}\right))** values of $n$.

### Random construction

Do the following independently:

* Put each prime (p\le x) into $A$ or $B$ with probability $1/2$ each (so a random partition).
* Choose each residue (a_p) uniformly at random in (\mathbb{Z}/p\mathbb{Z}), independently over $p$.

Fix an $n$ with (0\le n<x).

Define the event (E_A(n)): “$n$ is **not** covered by any prime in $A$, i.e.
(\forall p\in A,; n\not\equiv a_p\pmod p).”

Conditioned on the partition, the random residues give
[
\mathbb{P}(E_A(n)\mid A)
= \prod_{p\in A} \left(1-\frac1p\right).
]
Now take expectation over the random partition. For each prime $p$, its contribution is

* if (p\in A): factor ((1-1/p)),
* if (p\notin A): factor $1$.

So
[
\mathbb{E}\big[\mathbb{P}(E_A(n)\mid A)\big]
= \prod_{p\le x}\left(\tfrac12(1-\tfrac1p)+\tfrac12\cdot 1\right)
= \prod_{p\le x}\left(1-\frac{1}{2p}\right).
]
By the standard Mertens-type estimate for Euler products,
[
\prod_{p\le x}\left(1-\frac{1}{2p}\right)
\asymp \frac{C}{\sqrt{\log x}}
]
for some constant (C>0). [[nomath]](This is exactly the same heuristic/product analysis as $\prod_{p\le x}(1-1/p)\sim e^{-\gamma}/\log x$, but with $1/(2p)$ instead of $1/p$.)[[/nomath]]

So
[
\mathbb{P}(E_A(n)) \ll \frac{1}{\sqrt{\log x}}.
]
Similarly,
[
\mathbb{P}(E_B(n)) \ll \frac{1}{\sqrt{\log x}}.
]

Now define $E(n)$ = “$n$ fails the desired property,” i.e. either it has no cover from $A$ or no cover from $B$:
[
E(n)=E_A(n)\cup E_B(n).
]
Then by a union bound,
[
\mathbb{P}(E(n)) \le \mathbb{P}(E_A(n))+\mathbb{P}(E_B(n))
\ll \frac{1}{\sqrt{\log x}}.
]

### Expected number of failures

Let
$
X_{\text{bad}} := |\\{0\le n<x:\ E(n)\text{ occurs}\\}|.
$
Then
$
\mathbb{E}[X_{\text{bad}}]
= \sum_{n=0}^{x-1} \mathbb{P}(E(n))
\ll x\cdot \frac{1}{\sqrt{\log x}}
= O(\frac{x}{\sqrt{\log x}}).
$
Therefore there exists at least one choice of partition and residues such that
$
X_{\text{bad}} \ll \frac{x}{\sqrt{\log x}},
$
i.e. **all but $O(x/\sqrt{\log x})$** values of (n<x) have the required property.

So the *density* version is true and easy: you can make the statement hold for a (1-o(1)) fraction of (n<x).

---

## 3) Why the full “for all (n<x)” is hard

The probabilistic argument above typically leaves about (x/\sqrt{\log x}) exceptional $n$’s. The crux is:

* You are not allowed to use moduli (>x) to “patch” individual exceptions (which is a common trick in prime-gap style constructions when the interval length is smaller than the largest modulus you’re allowed to use).
* And because $A$ and $B$ must be a *partition* and the residue choices all come from a single global CRT shift $m$, you’re essentially trying to build a length-$x$ interval of integers each having **two small prime factors split across colors**—a very strong structured requirement.

This is exactly the sort of obstacle that makes it plausible as an Erdős–Graham open problem, and is consistent with its “open” listing. ([Erdős Problems][1])

---

## 4) If you want something fully provable “on the nose”

Since the exact statement is open as stated, two fully provable nearby statements one can show quickly are:

1. **One-sided version (no partition):**
   There exist residues (a_p) [[nomath]](for all primes $p\le x$)[[/nomath]] such that for every (n<x) there exists some prime (p\le x) with (n\equiv a_p\pmod p).
   (This is already connected to classical “prime gap / Jacobsthal function” constructions.)

2. **Two-sided “almost all” version:**
   As proved above, you can arrange the two-set condition for all but $O(x/\sqrt{\log x})$ integers (n<x).

If you tell me which nearby variant you’re actually allowed to use [[nomath]](e.g. “all but $o(x)$ exceptions”, or “replace $x$ by $x/(\log x)^C$”, or “allow $k$ colors/sets”)[[/nomath]], I can give a clean, complete proof at that level of strength.

But for the exact “every (n<x)” two-set statement you wrote, the best I can do responsibly is: it is currently listed as open, give the sharp reformulation, and prove the strongest standard partial result (almost-all) as above.

[1]: https://www.erdosproblems.com/latex/467 "https://www.erdosproblems.com/latex/467"
