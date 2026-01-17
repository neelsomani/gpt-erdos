This is **open** in general.

For the specific power sequences
[
A_k={1^k,2^k,3^k,\dots},
]
it is classical that (A_k) is complete for every $k$ [[nomath]](so $T(A_k)$ exists)[[/nomath]]. This goes back to Sprague (1948), with later generalisations by Roth–Szekeres and an “elementary” proof by Graham; see e.g. Kim’s paper for a summary and explicit bounds. 

### Conventions and the known computed values

Many papers (and OEIS A001661) define the “threshold” as the **largest** integer **not** representable as a sum of distinct (k)th powers; call that (\theta_k). ([OEIS][1])

Your (T(A_k)) is the **least** $m$ such that every (n\ge m) is representable, so [[nomath]](for $k\ge2$)[[/nomath]]
[
T(A_k)=\theta_k+1.
]
This shift by $1$ does **not** affect inequalities like (T(A_k)>T(A_{k+1})) [[nomath]](for $k\ge2$)[[/nomath]].

The currently *known exact* values [[nomath]](largest non-representable $\theta_k$)[[/nomath]] are:
[
\theta_2=128,\ \theta_3=12758,\ \theta_4=5134240,\ \theta_5=67898771,\ \theta_6=11146309947,\ \theta_7=766834015734,\ \theta_8=4968618780985762.
]
These are recorded in OEIS A001661 and [[nomath]](for $\theta_8$)[[/nomath]] proved/computed in Wiener (2023). ([OEIS][1])

So, for (k\le 8), the thresholds are **strictly increasing** [[nomath]](hence no example of $T(A_k)>T(A_{k+1})$ occurs up to that point)[[/nomath]]. ([OEIS][1])

Wiener (2023) also gives lower bounds for (\theta_k) for (9\le k\le 16); in particular (\theta_9\ge 155{,}581{,}444{,}629{,}727{,}232), which is already (\gg \theta_8), so (T(A_8)<T(A_9)) as well. 

### Status of your question (T(n^k)>T(n^{k+1})) infinitely often

The specific question

> Are there infinitely many $k$ such that (T(n^k)>T(n^{k+1}))?

is an Erdős–Graham problem and is listed as **OPEN** (Problem #345 on the Erdős Problems site). ([Erdős Problems][2])

Erdős and Graham suggested that plausible “problematic” exponents might be (k=2^t), because (2^t)-th powers have very restricted residue classes modulo powers of $2$, potentially making representations harder and pushing the threshold up for those $k$. But there is no proof that this produces a drop at $k+1$, let alone infinitely many. ([Erdős Problems][2])

So: **no**, this is not currently known to be true (or false); the best we can say is that **all computed data so far shows (T(n^k)) increasing with $k$** through the range where it’s been determined exactly. ([OEIS][1])

[1]: https://oeis.org/A001661 "A001661 - OEIS"
[2]: https://www.erdosproblems.com/345 "
  
    Erdős Problem #345
  
"
