What you wrote is (essentially) the **Erdős–Straus conjecture**:

[
\frac{4}{n}=\frac1x+\frac1y+\frac1z\qquad (n\ge2,\ x,y,z\in\mathbb Z_{>0}).
]

As of the most recent standard references, it is **still unproven in full generality** [[nomath]](so it’s not currently a theorem that this holds for *every* $n>2$)[[/nomath]]. ([Wikipedia][1])

### About the “distinct” condition

For (n\ge 3), requiring $x,y,z$ to be **distinct** does **not** really change the problem: if any solution has repeated unit fractions, there is a standard way to “split” duplicates into two different unit fractions and iterate until all are distinct. ([Wikipedia][2])
So your statement is the conjecture in a common “Egyptian fraction / distinct denominators” form.

---

## What *is* known: explicit constructions for large families of $n$

Even though the full statement is open, there are clean identities that prove it for many infinite classes of $n$. Here are some classic, fully explicit ones (and they already give (x<y<z)).

### 1) $n$ even

Write (n=2m). Then
[
\frac{4}{n}=\frac{2}{m}=\frac1m+\frac1m
=\frac1m+\left(\frac1{m+1}+\frac1{m(m+1)}\right).
]
So one valid choice is
[
x=m,\quad y=m+1,\quad z=m(m+1).
]
These are distinct and satisfy (m<m+1<m(m+1)) for (m\ge2) (i.e. (n\ge4)).

### 2) (n\equiv 3\pmod 4)

Write (n=4m-1). Then
[
\frac{4}{n}=\frac{4}{4m-1}=\frac1m+\frac1{m(4m-1)}=\frac1m+\frac1{mn}.
]
Now split the last unit fraction:
[
\frac1{mn}=\frac1{mn+1}+\frac1{mn(mn+1)}.
]
So you can take
[
x=m,\quad y=mn+1,\quad z=mn(mn+1).
]

### 3) (n\equiv 2\pmod 3)

Write (n=3q+2). Then (n+1=3(q+1)), so
[
\frac{3}{n}=\frac1{q+1}+\frac1{n(q+1)}
]
because
[
\frac1{q+1}+\frac1{n(q+1)}=\frac{n+1}{n(q+1)}=\frac{3(q+1)}{n(q+1)}=\frac3n.
]
Hence
[
\frac4n=\frac1n+\frac3n=\frac1n+\frac1{q+1}+\frac1{n(q+1)}.
]
So one choice is
[
{x,y,z}={q+1,\ n,\ n(q+1)},
]
and for (q\ge1) (i.e. (n\ge5)) these are distinct and can be ordered as (q+1<n<n(q+1)).

### 4) (n\equiv 5\pmod 8)

This gives another clean 3-term identity. If (n\equiv 5\pmod 8), then (a=\frac{n+3}{4}) is an **even** integer, so (na/2\in\mathbb Z). Then:
[
\frac1a+\frac1{na/2}+\frac1{na}
=\frac1a+\frac2{na}+\frac1{na}
=\frac1a+\frac3{na}
=\frac{n+3}{na}.
]
But (a=\frac{n+3}{4}), so (\frac{n+3}{a}=4), hence
[
\frac{n+3}{na}=\frac4n.
]
So you can take
[
x=a=\frac{n+3}{4},\quad y=\frac{na}{2},\quad z=na.
]

---

## Why this doesn’t settle “every (n>2)”

All the identities above together cover *most* integers (n), but not all. The remaining cases (in particular, the “hardest” ones are closely related to primes (n\equiv 1\pmod{24})) are exactly where the conjecture is still open. ([Wikipedia][1])

### Computational evidence

Although unproven, it has been **checked by computer up to very large bounds**. Wikipedia summarizes verification up to (10^{17}). ([Wikipedia][2])
There is also work reporting verification for primes up to (10^{18}). ([arXiv][3])

---

If you tell me a specific $n$ you care about, I can give you an explicit triple $(x,y,z)$ for that $n$ (either via one of the formulas above or by a quick constructive search).

[1]: https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Straus_conjecture?utm_source=chatgpt.com "Erdős–Straus conjecture"
[2]: https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Straus_conjecture "Erdős–Straus conjecture - Wikipedia"
[3]: https://arxiv.org/abs/2509.00128?utm_source=chatgpt.com "Further verification and empirical evidence for the Erdős ..."
