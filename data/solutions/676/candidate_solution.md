This is **open**.

Erdős asked (in 1979) whether there is an (n_0) such that **every** (n>n_0) can be written
$
n=a p^2+b,\qquad p\ \text{prime},\ a\ge 1,\ 0\le b<p,
$
and noted that while a sieve argument shows the representation exists for **almost all** integers $n$, he thought it was likely that **infinitely many** $n$ have **no** such representation. 

A convenient equivalent reformulation is: find a prime (p\le \sqrt n) such that
[
n\bmod p^2 \in {0,1,2,\dots,p-1},
]
i.e. the residue of $n$ mod (p^2) is *smaller than* $p$.

What is known is that the set of exceptions is **very sparse**. The Erdős Problems Database entry for this question (Problem #676) records that:

* “the sieve of Eratosthenes implies that almost all integers are of this form,” and
* stronger sieve methods (Brun–Selberg) give upper bounds on the number of exceptions up to $x$, e.g. (\ll x/(\log x)^c) for some (c>0). ([Erdős Problems][1])

But **no one currently knows** whether the exceptional set is **finite** (which would make the answer “yes”) or **infinite** (which would make the answer “no”). ([Erdős Problems][1])

If you want a pointer to more recent discussion: a 2025 preprint explicitly frames this as Erdős’s open problem and discusses conditional implications (under strong distribution hypotheses for primes) toward finiteness of the exceptional set—though it does **not** settle the problem unconditionally. ([Sciety][2])

[1]: https://www.erdosproblems.com/676 "
  
    Erdős Problem #676
  
"
[2]: https://sciety.org/articles/activity/10.20944/preprints202509.1804.v1?utm_source=sciety_labs_article_page "
    Entropy—Sieve Methods and Energy Functionals in the Erdős Problem [Er79] on Quadratic Prime Representations | Sciety
  "
