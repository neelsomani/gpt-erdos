As far as the current literature goes, this is **not known**: it’s an **open problem** of Erdős.

* Erdős explicitly asked (in 1979) whether one can choose residues (c_p \pmod p) for every prime (2\le p\le n) so that **every** (x\le n) satisfies **at least 2** [[nomath]](or at least $r$)[[/nomath]] of the congruences (x\equiv c_p\pmod p). 
* The same question is catalogued as **Erdős Problem #689** and is listed as open (as of the site’s Dec 2025 update). ([Erdős Problems][1])
* It also appears as **Problem 45** in Ben Green’s open problems list; he notes that Erdős “does not know how to answer it with 10 replaced by 2,” i.e. exactly your $r=2$ question. 

A few bits of context that help frame why it’s plausible but delicate:

* A trivial “near miss”: if you take (a_p\equiv 0\pmod p) for all primes (p\le n), then every integer (\le n) with at least two **distinct** prime factors automatically satisfies at least two congruences; the only exceptions are $1$ and prime powers. So the problem is essentially about whether you can “mop up” those remaining prime powers without breaking the double-coverage elsewhere.
* The $r=1$ analogue [[nomath]](cover each $x\le n$ at least once)[[/nomath]] is closely tied to the Jacobsthal/prime-gap machinery and is itself part of Erdős’s constellation of problems (#687/#688/#689). ([Erdős Problems][2])
* There are detailed heuristics suggesting the $r=2$ case *might* be doable via a multi-stage sieve/covering strategy using “medium” primes to hit many remaining targets at once and the largest primes to clean up stragglers, but no complete proof is written down; see the discussion thread for some of this numerology (including comments by Tao and others). ([Erdős Problems][3])

So the honest answer is: **no proof (and no disproof) is currently known** for sufficiently large $n$. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/689 "
  
    Erdős Problem #689
  
"
[2]: https://www.erdosproblems.com/687 "
  
    Erdős Problem #687
  
"
[3]: https://www.erdosproblems.com/forum/discuss/689 "

    Erdős Problem #689 - Discussion thread

"
