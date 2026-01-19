This is **open** (it is Erdős’ Problem #768 in the Erdős Problems database). ([Erdős Problems][1])

What *is* known is that Erdős proved two-sided stretched–exponential bounds, but with a gap in the exponent:

Let
[
A(N):=\lvert A\cap[1,N]\rvert.
]
Then Erdős showed there is an absolute constant (c>0) such that, for all large $N$,
[
\exp\big(-c\sqrt{\log N}\log\log N\big)\ \le\ \frac{A(N)}{N}
\ \le\ \exp!\big(-(1+o(1))\sqrt{\log N,\log\log N}\big).
]
([Erdős Problems][1])

So your proposed asymptotic
[
\frac{A(N)}{N}=\exp\big(-(c+o(1))\sqrt{\log N},\log\log N\big)
]
would in particular **sharpen** Erdős’ upper bound by a factor of about (\sqrt{\log\log N}) in the exponent, and that sharpening is exactly what is not known.

### Context and related facts

* The condition defining $A$ arises naturally from **Sylow theory** considerations when trying to rule out candidate orders of (non-cyclic) simple groups: one needs, for each prime (p\mid n), a divisor (>1) of $n$ that is (1\bmod p). This motivation is explicitly discussed in the Erdős Problems entry and in Erdős’ original note. ([Erdős Problems][1])
  OEIS records the same “survives the Sylow test” interpretation for this exact set (sequence A352287). ([OEIS][2])

* It is known (and not hard) that $A$ has **natural density $0$**; in fact, even the weaker property involving only the *largest* prime factor already defines a zero-density set [[nomath]](so $A\subseteq$ that set also has density $0$)[[/nomath]]. ([MathOverflow][3])

### Why the shape (\exp(-\Theta(\sqrt{\log N}\log\log N))) is plausible (heuristic)

That “(\sqrt{\log N}\log\log N)” scale is the same one that appears for counts of **very smooth numbers** when the smoothness bound is (y=\exp(\sqrt{\log N})): one has heuristically/known asymptotics involving the Dickman–de Bruijn function (\rho(u)) with (u=\frac{\log N}{\log y}=\sqrt{\log N}), and (\rho(u)) decays like (\exp(-(1+o(1))u\log u)). ([Wikipedia][4])
Plugging (u=\sqrt{\log N}) yields exactly an exponent of order (\sqrt{\log N}\log\log N). But turning this into the *exact* asymptotic for $A(N)$ [[nomath]](and identifying the correct constant $c$)[[/nomath]] is precisely the open part.

So the current state is:

* **Lower bound** of the conjectured form: yes (Erdős).
* **Matching upper bound / existence of a constant $c$ in the main term**: not known; still listed as open as of the 2025 update to the Erdős Problems database. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/768 "
  
    Erdős Problem #768
  
"
[2]: https://oeis.org/A352287 "A352287 - OEIS"
[3]: https://mathoverflow.net/questions/403728/ "gr.group theory - On the density of the orders excluded by the Sylow theorems for simple groups - MathOverflow"
[4]: https://en.wikipedia.org/wiki/Dickman_function?utm_source=chatgpt.com "Dickman function"
