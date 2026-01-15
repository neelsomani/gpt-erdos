This is **open**.

If you write
[
g(a)\ :=\ \min\\{n:\ \varphi(n)=a\\}\qquad(a\ \text{a totient}),
]
then your question is asking whether there are infinitely many totients $a$ with
[
\frac{g(a)}{a}\ \to\ \infty\quad\text{along an infinite set}.
]
Equivalently, it asks whether for **every** constant (C>1) there exists a totient $m$ such that **every** solution of (\varphi(x)=m) satisfies (x>Cm) [[nomath]](because all solutions are $\ge g(m)$)[[/nomath]]. This is recorded as **Erdős Problem #51** and is listed as open. ([Erdős Problems][1])

What is known is mainly “if one example exists, then many exist” type results:

* A 2025 open-problems note (quoting Kevin Ford) states explicitly that Erdős’s question is **“wide open, even for (C=3)”**. In other words, it is not currently known whether there even exists a totient $m$ whose *smallest* preimage exceeds $3m$, let alone a sequence with (g(m)/m\to\infty). 

* Ford’s 1998 work implies a strong density phenomenon: **if** there is *one* totient $m$ with the property “all solutions $x$ of (\varphi(x)=m) satisfy (x>Cm)”, then in fact a **positive proportion of all totients** have the same property. 

A closely related (and often-discussed) strengthening is:

* For a given integer (k\ge2), does there exist a totient $m$ such that **every** preimage $x$ with (\varphi(x)=m) is divisible by $k$? Ford proves that if such a totient exists for a given $k$, then again a positive proportion of totients share this “all preimages divisible by $k$” property (his Theorem 8 on $V(x;k)$). 
  He also notes small examples for many (k\le 11) but remarks that (k=6) [[nomath]](and $k=10$)[[/nomath]] were missing from quick searches, and that proving nonexistence for (k=6) would imply Carmichael’s conjecture. 
  Moreover, as noted in the same 2025 note, if one could do this for $k$ running through **primorials**, it would imply a positive answer to Erdős’s “(x>Cm)” question and hence to your (g(a)/a\to\infty) question. 

So, at present:

* No construction is known that produces an infinite set $A$ with (n_a/a\to\infty).
* It’s not even proved that there exists a single totient $m$ with (g(m)/m>3). 

If you want, I can also summarize the heuristic ideas people discuss for why the answer might be “yes” or “no,” but the rigorous status is: **unknown**.

[1]: https://www.erdosproblems.com/51 "
  
    Erdős Problem #51
  
"
