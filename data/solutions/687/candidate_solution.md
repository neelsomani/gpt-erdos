Let
[
P(x):=\prod_{p\le x}p
]
[[nomath]](the primorial up to $x$)[[/nomath]]. Your definition is exactly the “Erdős–Rankin/Jacobsthal” quantity that appears in large prime gap constructions.

## 1. Reformulation as Jacobsthal’s function

Given a choice of residues (a_p \pmod p) for each prime (p\le x), the Chinese remainder theorem gives an integer $m$ such that
[
m\equiv -a_p \pmod p\qquad(\forall,p\le x).
]
Then for (1\le t\le y), the condition “(t\equiv a_p\pmod p) for some (p\le x)” is equivalent to
[
m+t\equiv 0 \pmod p\quad\text{for some }p\le x,
]
i.e. every integer in ({m+1,\dots,m+y}) shares a prime factor (\le x), hence is **not** coprime to $P(x)$. Ford–Green–Konyagin–Maynard–Tao record this equivalence explicitly as
[
Y(x)=j(P(x))-1,
]
where $j(n)$ is Jacobsthal’s function [[nomath]](maximal gap between integers coprime to $n$)[[/nomath]]. ([Oxford University Research Archive][1])

So $Y(x)$ is the length of the longest block of consecutive integers all divisible by at least one prime (\le x).

## 2. Best unconditional lower bound

The current best lower bound (as of the literature referenced through 2025) is due to Ford–Green–Konyagin–Maynard–Tao:
[
Y(x)\gg x,\frac{\log x,\log\log\log x}{\log\log x}.
]
Equivalently [[nomath]](using $\log_2 x=\log\log x$, $\log_3 x=\log\log\log x$)[[/nomath]],
[
Y(x)\gg x\frac{\log x,\log_3 x}{\log_2 x}.
]
They state this as their key bound [[nomath]](improving Rankin’s earlier $\log_2^2 x$ denominator)[[/nomath]]. ([Oxford University Research Archive][1])

So in particular one already has
[
Y(x) \ge x^{1+o(1)}
]
(from below), since the extra factor (\frac{\log x,\log_3 x}{\log_2 x}=x^{o(1)}).

## 3. Best unconditional upper bound

The best known general upper bound comes from Iwaniec’s work on Jacobsthal’s problem. In Iwaniec’s notation, $C(r)$ is the maximal length of a block of consecutive integers each divisible by one of $r$ primes, and he proves
[
C(r)\ll r^2(\log r)^2
]
(via his “shifted sieve”; this is his corollary). 

Applying this with (r=\pi(x)\sim x/\log x) gives
[
Y(x)\ll \pi(x)^2(\log \pi(x))^2 \ll x^2.
]
This (Y(x)\ll x^2) upper bound is also recorded directly in the Ford–Green–Konyagin–Maynard–Tao paper as the best known upper bound for $Y$, attributed to Iwaniec. ([Oxford University Research Archive][1])

## 4. Conjectural size and your questions

Maier–Pomerance conjecture that
[
Y(x)\ll x(\log x)^{2+o(1)}.
]
This conjecture is stated in the same “Long gaps between primes” paper. ([Oxford University Research Archive][1])
(And it is also summarized in the Erdős problem statement for #687.) ([Erdős Problems][2])

### Can one prove (Y(x)=o(x^2))?

Not with the current technology: the best unconditional upper bound is still (Y(x)\ll x^2), and improving it to $o(x^2)$ is (as far as the referenced sources indicate) open. ([Erdős Problems][2])

### Can one prove (Y(x)\ll x^{1+o(1)})?

Also open. The Maier–Pomerance conjecture (Y(x)\ll x(\log x)^{2+o(1)}) would imply (Y(x)\ll x^{1+o(1)}), since ((\log x)^{2+o(1)}=x^{o(1)}). ([Oxford University Research Archive][1])
But no such upper bound is currently proved; the best unconditional remains (x^2).

## 5. Current “best estimates” in one line

Putting the best known lower and upper bounds together:
[
x\frac{\log x\log\log\log x}{\log\log x}\ \ll\ Y(x)\ \ll\ x^2.
]
Lower bound: Ford–Green–Konyagin–Maynard–Tao. ([Oxford University Research Archive][1])
Upper bound: Iwaniec (via Jacobsthal/shifted sieve). 

If you want, I can also translate these into statements about the maximal prime gap $G(X)$ via their Lemma 1.1 [[nomath]](since $Y(x)$ is precisely the sieve-interval length used in Erdős–Rankin-type prime gap constructions)[[/nomath]]. ([Oxford University Research Archive][1])

[1]: https://ora.ox.ac.uk/objects/uuid%3A4f92b379-4935-4df4-ab12-ad6e8e85c965/files/m82130bfb3e8ac4562cce865fd741d525 "https://ora.ox.ac.uk/objects/uuid%3A4f92b379-4935-4df4-ab12-ad6e8e85c965/files/m82130bfb3e8ac4562cce865fd741d525"
[2]: https://www.erdosproblems.com/687 "https://www.erdosproblems.com/687"
