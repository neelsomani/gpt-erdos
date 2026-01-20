As far as I can tell from the current literature/status pages, this is **still open**: no such pair $(f,k)$ is known, and no impossibility result is known for the problem as you stated it. ([Erdős Problems][1])

Here’s the landscape that *is* known.

## Why $k=2$ cannot work

If $k=2$, then “the finite-sums set does not contain all colours” means it misses one of the two colours, i.e. **it is monochromatic**. So your question would become a “bounded” variant of Hindman’s theorem:

> in every 2-colouring, find an infinite sequence ((a_n)) whose finite sums are monochromatic **and** with (a_n<f(n)) for infinitely many $n$.

Galvin showed that this **monochromatic** bounded strengthening fails already for **two colours**, by constructing a 2-colouring of (\mathbb N) based on the 2-adic valuation: write (n=2^k m) with $m$ odd, and colour $n$ red/blue depending on whether (m\ge F(k)) or (m<F(k)), for a sufficiently fast-growing $F$. ([Erdős Problems][1])

So $k=2$ is ruled out.

## For (k\ge 3): open (even for countably many colours)

Your question is weaker than monochromaticity when (k\ge 3): you only ask that the IP-set of finite sums **miss at least one colour**.

That weaker version is exactly what Erdős posed (in this form), and it is explicitly recorded as **open**, *even if you allow (\aleph_0) colours*. ([Erdős Problems][1])

The same discussion thread also notes that the problem appears (as Problem 4.2) in Erdős–Galvin’s 1991 paper *Some Ramsey-type theorems*, where the “Galvin example” for the monochromatic version is described (Theorem 4.1 there). ([Erdős Problems][1])

## Context: relation to Hindman’s theorem

Without the growth condition (a_n<f(n)) infinitely often, the conclusion “finite sums miss at least one colour” would be trivial from Hindman’s theorem, because Hindman gives a **monochromatic** finite-sums set in any finite colouring. 

So the entire difficulty is the requirement that the generating sequence hits the bounds $f(n)$ infinitely often.

---

If you want, I can also:

* restate the problem in standard “IP-set/FS-set” language and point out a couple of equivalent reformulations; or
* sketch more explicitly why Galvin’s 2-adic colouring blocks any *bounded* monochromatic FS-set (the key mechanism is forcing some subset sum to flip colour by engineering its odd part vs. its 2-adic valuation). ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/forum/thread/948 "

    Erdős Problem #948 - Discussion thread

"
