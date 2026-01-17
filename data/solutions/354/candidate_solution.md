For the base $2$ version: this is **open in general**, even under the hypothesis (\alpha/\beta\notin\mathbb Q). In fact, your question is exactly the **Erdős–Graham problem** (often listed as Erdős Problem #354). ([Erdős Problems][1])

### What is known for base $2$

Write
[
A_{\alpha,\beta}:={\lfloor 2^n\alpha\rfloor,\lfloor 2^n\beta\rfloor:\ n=0,1,2,\dots},
]
and let (P(A_{\alpha,\beta})) be all finite subset sums (distinct parts). Erdős and Graham conjectured that if (\alpha/\beta) is irrational then (A_{\alpha,\beta}) is complete. 

Here are the main partial results and obstructions that are currently documented:

* **A major positive case (dyadic vs non-dyadic):**
  Hegyvári proved the conjecture when (say) (\alpha) is a **dyadic rational** (\alpha=m/2^n) and (\beta) is **not** dyadic. ([Erdős Problems][1])
  (Hegyvári formalizes this via binary/dyadic expansions as “finite” vs “infinite” diadical fractions.) 
  In particular, under your hypothesis (\alpha/\beta) irrational, **if one of (\alpha,\beta) is dyadic**, you are in a solved case [[nomath]](because both being dyadic would force $\alpha/\beta\in\mathbb Q$)[[/nomath]]. ([Erdős Problems][1])

* **A family of counterexamples when (\beta) is a power-of-two multiple of (\alpha):**
  Hegyvári showed (A_{\alpha,\beta}) is **not complete** if (\alpha\ge 2) and (\beta=2^k\alpha) for some (k\ge 0). ([Erdős Problems][1])
  More recently, Jiang–Ma and Fang–He extended “not complete” phenomena to some cases with (1<\alpha<2) and (\beta=2^k\alpha) for sufficiently large (k). ([Erdős Problems][1])
  [[nomath]](These counterexamples all have $\alpha/\beta=2^{-k}\in\mathbb Q$, so they do **not** contradict the irrational-ratio conjecture; they support the idea that “$\beta$ is a power-of-two multiple of $\alpha$” is a key obstruction.)[[/nomath]] ([Erdős Problems][1])

* **Some additional positive regions:**
  The problem page records (from comments) a proof that the sequence is complete if
  [
  \alpha<2<\beta<3
  ]
  [[nomath]](and symmetrically if $\beta<2<\alpha<3$)[[/nomath]]. ([Erdős Problems][1])

* **What people expect the “right” hypothesis to be:**
  It is considered likely (and Hegyvári explicitly conjectured a stronger version) that one can weaken “(\alpha/\beta) irrational” to something like
  [
  \alpha/\beta \neq 2^k
  \quad\text{and at least one of }\alpha,\beta\text{ not dyadic},
  ]
  i.e. the only obstructions should come from (i) dyadic issues and (ii) the “shift” relation (\beta=2^k\alpha). ([Erdős Problems][1])

So, to answer your first question plainly:

* Under (\alpha/\beta) irrational, **the conjectured answer is “yes, it should be complete,”** but **it is not proved in full generality** as of the latest compiled status (edited 1 Dec 2025). ([Erdős Problems][1])

### About replacing $2$ by (\gamma\in(1,2))

This variant is **also explicitly posed** alongside the base-$2$ question in the same problem listing, and it is likewise treated as **open** there. ([Erdős Problems][1])

A cautionary structural point (not a theorem): for general (\gamma), the “shift” obstruction would naturally become (\beta=\gamma^k\alpha). Unlike the base-$2$ case, if (\gamma) is irrational then (\alpha/\beta=\gamma^{-k}) is itself irrational, so your condition “(\alpha/\beta) irrational” would *not* automatically rule out that kind of alignment. Whether such alignments actually force incompleteness for (\gamma\in(1,2)) is part of what makes the (\gamma)-version subtle.

If you want, I can also summarize the proof ideas behind the known special cases [[nomath]](dyadic/non-dyadic, and the $\alpha<2<\beta<3$ region)[[/nomath]] and how they relate to binary expansions and the recurrence (\lfloor 2^{n+1}\alpha\rfloor = 2\lfloor 2^n\alpha\rfloor + {0,1}), which is why “dyadic” behavior shows up so strongly.

[1]: https://www.erdosproblems.com/354 "
  
    Erdős Problem #354
  
"
