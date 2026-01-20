No.

A non‐polynomial entire function has an essential singularity at (\infty), so by the Great Picard theorem it takes **every** complex value infinitely often **except possibly one** value. ([Wikipedia][1])
So your question is really asking whether the “Fabry gap” condition
[
\frac{n_k}{k}\to\infty
]
forces there to be **no** exceptional value.

It does not. In fact, Murai explicitly constructs an entire function $g$ whose Maclaurin series has **Fabry gaps** [[nomath]](i.e. $\lim k/n_k=0$, equivalent to $n_k/k\to\infty$)[[/nomath]] and for which
[
\delta(0,g)=1,
]
so $0$ is an extreme exceptional value in the Nevanlinna sense. ([NumDAM][2])
Moreover, in Murai’s construction the approximating polynomials (g_m) are arranged to be **zero–free in disks whose radii tend to infinity**, and (g=\lim g_m) exists as an entire function. ([NumDAM][2])
From this “zero–free on larger and larger disks + locally uniform convergence” setup, Hurwitz’s theorem implies that the limit function $g$ is **zero–free on every disk**, hence **(g(z)\neq 0) for all (z\in\mathbb C)** [[nomath]](so $0$ is actually omitted)[[/nomath]].

Now define
[
f(z):= z,g(z).
]
Then $f$ is entire and has an expansion of the form
[
f(z)=\sum_{k=1}^\infty a_k z^{N_k},
]
where the exponents (N_k) are just the exponents of $g$ shifted by (+1), so still satisfy (N_k/k\to\infty), and by construction the coefficients (a_k) are nonzero (they are precisely the nonzero Taylor coefficients). Also,
[
f(z)=0 \iff z=0,
]
because (g(z)\neq 0) everywhere. Thus $f$ takes the value $0$ **only once**, not infinitely often.

So the statement “if (n_k/k\to\infty) then $f$ assumes every value infinitely often” is **false**. ([NumDAM][2])

[1]: https://en.wikipedia.org/wiki/Picard_theorem?utm_source=chatgpt.com "Picard theorem"
[2]: https://www.numdam.org/item/10.5802/aif.930.pdf "The deficiency of entire functions with Fejér gaps"
