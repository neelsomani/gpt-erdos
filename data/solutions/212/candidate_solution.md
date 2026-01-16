This is exactly the **Erdős–Ulam problem**:

> Does there exist a subset (S\subset\mathbb{R}^2) that is **dense in the plane** and such that **every distance (|p-q|)** for (p,q\in S) is a **rational number**?

**As of today, this is still open** (no construction is known, and no impossibility proof is known). ([Erdős Problems][1])

### What *is* known (context / partial results)

* **You can make infinite (even dense-in-a-curve) rational-distance sets**, just not known dense in the *whole plane*.
  For example, there are sets **dense on a circle** for which *all* pairwise chord lengths are rational. One standard construction on the **unit circle** takes angles (\theta) with (\tan(\theta/4)\in\mathbb{Q}); then (\sin(\theta/2),\cos(\theta/2)\in\mathbb{Q}), and the distance between two such points becomes a rational expression in those rationals. ([Wikipedia][2])
  (Similarly, lines trivially support dense rational-distance sets by identifying the line with (\mathbb{R}) and taking (\mathbb{Q}).)

* A major unconditional structural theorem: **if a rational-distance set has infinitely many points on an irreducible algebraic curve, that curve must be a line or a circle** (otherwise only finitely many such points can lie on the curve). This is due to **Solymosi–de Zeeuw**. ([Wikipedia][2])

* There are also **conditional** (conjecture-dependent) results pointing toward a **negative** answer:

  * Assuming the **Bombieri–Lang conjecture**, Tao and Shaffaf (independently) show there cannot be a dense rational-distance set in (\mathbb{R}^2). ([What's new][3])
  * Pasten proved that the **abc conjecture** would also imply a negative answer. ([Wikipedia][2])

### Bottom line

**No one currently knows** whether such a dense subset of (\mathbb{R}^2) with all pairwise distances rational exists. It is a well-known open problem. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/212 "
  
    Erdős Problem #212
  
"
[2]: https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Ulam_problem "Erdős–Ulam problem - Wikipedia"
[3]: https://terrytao.wordpress.com/2014/12/20/the-erdos-ulam-problem-varieties-of-general-type-and-the-bombieri-lang-conjecture/ "The Erdos-Ulam problem, varieties of general type, and the Bombieri-Lang conjecture | What's new"
