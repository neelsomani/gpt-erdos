This is **open** (at least as of **January 16, 2026**).

A standard way to formalize your condition [[nomath]](for an asymptotic basis of fixed order $h\ge2$)[[/nomath]] is: for each $a\in A$,
$
E(a)\ :=\ hA\ \setminus\ h(A\setminus\\{a\\}),
$
i.e. the set of integers whose **every** representation as a sum of $h$ elements of $A$ is “destroyed” if you delete $a$. Minimality is exactly the statement that $E(a)$ is infinite for every $a\in A$. Your question asks for the stronger requirement that
[
\overline d(E(a))>0\quad\text{for every }a\in A,
]
[[nomath]](and additionally that $A$ has positive density)[[/nomath]].

This strengthened problem is explicitly posed by Erdős–Nathanson in their problem list, and they note they cannot rule it out. ([Theory of Numbers][1])
It is also listed as **Erdős Problem #330** and marked **OPEN**, last edited **Dec 8, 2025**. ([erdosproblems.com][2])

Some relevant “nearby” facts (to calibrate what’s known):

* **Minimal asymptotic bases with positive density do exist.** In particular, for order $2$, there are minimal asymptotic bases with any prescribed asymptotic density $\alpha\in(0,1/2]$; more generally for order $h$ there are minimal asymptotic bases with density $1/h$ and with many smaller prescribed densities. 
* There is also a general **upper bound** for how dense a minimal asymptotic basis of order $h$ can be: one has (d_L(A)\le 1/h) [[nomath]](so for order $2$, at most $1/2$)[[/nomath]]. 

But **none of the known constructions** settles the stronger “every element kills a positive-density set” requirement, and there is also **no known obstruction** proving such a set cannot exist. That is exactly the status recorded in the sources above. ([Theory of Numbers][1])

[1]: https://www.theoryofnumbers.com/melnathanson/pdfs/nath1987-59.pdf "Erdos-N-Problems.pdf"
[2]: https://www.erdosproblems.com/330 "
  
    Erdős Problem #330
  
"
