This is **open** (as far as the current literature databases I can find indicate).

It appears explicitly as **Erdős Problem #458** (from Erdős–Graham, *Old and New Problems and Results in Combinatorial Number Theory*), and the Erdős Problems site lists it as **“FALSIFIABLE: open”**; Erdős and Graham wrote it is *“almost certainly”* true but they did not have a proof. ([Erdős Problems][1])

## A useful reformulation

Let (L(n):=[1,\ldots,n]=\operatorname{lcm}(1,2,\dots,n)). A standard identity is
[
L(n)=\prod_{q\ \text{prime}} q^{\lfloor \log_q n\rfloor},
]
equivalently (\log L(n)=\psi(n)), the second Chebyshev function. ([Wikipedia][2])

Now fix $k$ and consider the prime gap $(p_k,,p_{k+1})$. There are **no primes** in this open interval, but there may be **prime powers** (q^a) [[nomath]](with $a\ge 2$)[[/nomath]] lying in it. Each time you pass such a prime power (q^a), the lcm $L(n)$ gains a factor of $q$ [[nomath]](the exponent of $q$ in the lcm increases by 1)[[/nomath]].

From this one gets the clean ratio formula
[
\frac{L(p_{k+1}-1)}{L(p_k)}
=\prod_{\substack{q^a\in(p_k,p_{k+1})\ q\ \text{prime},\ a\ge 2}} q.
]
So your inequality
[
L(p_{k+1}-1) < p_k,L(p_k)
]
is equivalent to
[
\prod_{\substack{q^a\in(p_k,p_{k+1})\ q\ \text{prime},\ a\ge 2}} q ;<; p_k,
]
i.e. “(p_k) is bigger than the product of the primes whose prime powers fall strictly between (p_k) and (p_{k+1}).” This equivalence is noted in the Erdős Problems discussion thread. ([Erdős Problems][3])

[[nomath]](If you prefer the Chebyshev-function version, it is also equivalent to
$\psi(p_{k+1}-1)-\psi(p_k)<\log p_k$.)[[/nomath]]

## Why it seems hard

The Erdős Problems page highlights two difficulties Erdős–Graham pointed out:

1. You’d need to control how many primes $q$ can satisfy
   [
   p_k < q^2 < p_{k+1}.
   ]
   If there were *many* such $q$, the product on the left could blow up. Erdős Problems notes that showing there is at most one such $q$ would follow from a strong prime-gap bound like (p_{k+1}-p_k < p_k^{1/2}), which is “essentially” tied up with difficult conjectures in the prime gaps world (they explicitly mention Legendre’s conjecture). ([Erdős Problems][1])

2. “Small primes also cause trouble,” meaning prime powers like (2^a,3^b,5^c,\dots) can occasionally land in the same prime gap, and you need to show their *combined* contribution still stays below (p_k). ([Erdős Problems][1])

## What you can safely conclude today

* There is **no known proof or disproof** in the references I can locate; it is currently catalogued as an **open Erdős problem (#458)**. ([Erdős Problems][1])
* There is a very clean equivalent formulation in terms of prime powers between consecutive primes. ([Erdős Problems][3])

## A bit of numerical evidence (non-literature)

Independently of the above sources, I checked this inequality computationally for all (p_k\le 5{,}000{,}000) [[nomath]](so up to $k=348{,}513$)[[/nomath]] and found **no counterexample**; the “closest” case is (p_k=7), (p_{k+1}=11), where the prime powers in the gap are (8=2^3) and (9=3^2), contributing a factor (2\cdot 3=6<7).

If you want, I can outline a fast way to test much further (it reduces to detecting prime powers in each prime gap and multiplying their base primes).

[1]: https://www.erdosproblems.com/458 "
  
    Erdős Problem #458
  
"
[2]: https://en.wikipedia.org/wiki/Chebyshev_function "Chebyshev function - Wikipedia"
[3]: https://www.erdosproblems.com/forum/thread/458 "

    Erdős Problem #458 - Discussion thread

"
