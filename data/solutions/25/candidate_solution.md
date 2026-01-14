No one currently knows in full generality.

This is an Erdős problem (often cited as **Erdős Problem #25**): given arbitrary increasing moduli (n_1<n_2<\cdots) and residue classes (a_i \pmod{n_i}), let
[
A={n\in\mathbb N:\ \forall i,\ \text{either }n<n_i\ \text{or}\ n\not\equiv a_i\pmod{n_i}}.
]
The question “must $A$ have a logarithmic density?”
[
\lim_{x\to\infty}\frac{1}{\log x}\sum_{\substack{n\le x\ n\in A}}\frac1n
]
is listed as **open**.

### What *is* known

* **Special case (a_i\equiv 0\pmod{n_i}) (divisibility / multiples): yes.**
  Then the forbidden set is a set of multiples, and Davenport–Erdős proved that the logarithmic density exists in this case.

* **Natural density can fail even in the multiples case.**
  Besicovitch gave examples where the *natural* density does not exist, which is part of why one asks for logarithmic density instead.

* **A straightforward positive case:** if (\sum_i \frac1{n_i}<\infty), then the logarithmic density of (A) **does** exist (for any residues (a_i)).
  Sketch: each excluded progression (n\equiv a_i\ (\mathrm{mod}\ n_i)) has logarithmic density (1/n_i). The “tail” union (\bigcup_{i>K}{n\equiv a_i\ (\mathrm{mod}\ n_i)}) then has *upper* logarithmic density (\le \sum_{i>K}1/n_i), which can be made arbitrarily small if the sum converges. Since finite unions are eventually periodic (hence have a logarithmic density), one can sandwich the upper/lower logarithmic densities of the full union between the finite-stage density and an arbitrarily small error, forcing existence of the limit for the full set. (This argument is essentially “finite approximation + summable tail.”)

### Where the difficulty lies

The genuinely hard regime is when (\sum_i 1/n_i) **diverges**: the above “summable tail” approximation breaks, and the Davenport–Erdős proof for multiples uses special multiplicative structure that doesn’t obviously extend to arbitrary residue classes. That’s why Erdős posed the general question, and why it remains open.
