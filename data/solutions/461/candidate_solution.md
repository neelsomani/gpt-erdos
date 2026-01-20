As far as I can tell from the literature that’s easy to locate, this is **still open** in the fully uniform form you stated.

It is explicitly listed as an open Erdős–Graham problem (Erdős & Graham, *Old and New Problems and Results in Combinatorial Number Theory*, 1980, p. 92), and the best unconditional lower bound that is routinely cited there is
[
f(n,t)\ \gg\ \frac{t}{\log t}
]
uniformly in (n,t). ([Erdős Problems][1])

So, at present:

* **Known (unconditional):** (f(n,t)\gg t/\log t). ([Erdős Problems][1])
* **Open:** whether one can improve this to a **linear** bound (f(n,t)\gg t) uniformly in (n,t). ([Erdős Problems][1])

A small structural observation that’s often useful when thinking about the problem (and explains why the linear bound feels plausible) is:

* If (s_t(m)\ge t), then that value can occur **at most once** among (m\in[n+1,n+t]).
  Indeed, if (s_t(m_1)=s_t(m_2)=d\ge t), then (d\mid (m_1-m_2)), but (|m_1-m_2|<t), forcing (m_1=m_2).

So any proof of (f(n,t)\gg t) would follow, for example, from showing that a **positive proportion** of the integers in $[n+1,n+t]$ have $t$-smooth component (\ge t), or else from showing that even those with (s_t(m)<t) contribute (\gg t) *distinct* values. But getting such a uniform proportion is exactly where the difficulty lies, and the currently recorded unconditional methods only guarantee (\gg t/\log t). ([Erdős Problems][1])

If you want, I can also sketch a plausible route to the (t/\log t) lower bound (it’s essentially a “sieve-ish” argument that forces many different small-prime patterns), and/or share some quick computational experiments that suggest $f(n,t)$ is typically a constant fraction of $t$, but those are heuristics rather than a proof of the uniform (\gg t) bound.

[1]: https://www.erdosproblems.com/461 "
  
    Erdős Problem #461
  
"
