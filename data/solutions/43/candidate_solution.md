This is exactly **Erdős Problem #43**. As of the current public status (edited 20 Dec 2025), the **first (additive (O(1))) question is still open**, but the **second (“save a fixed constant (c>0)” when (|A|=|B|)) is false**.

## The equal-size improvement with a fixed (c>0) is false

No such absolute constant (c>0) can exist. In fact, there are **infinitely many** (N) for which one can find Sidon sets (A,B\subset [N]) with (|A|=|B|), ((A-A)\cap(B-B)={0}), and
[
\binom{|A|}{2}+\binom{|B|}{2}\ \ge\ (1-o(1))\binom{f(N)}{2}.
]
So the ratio can go to (1), which kills any fixed saving (1-c).

### How the construction works (sketch)

Pick an **odd prime power** (q). Let
[
M:=q^2-1,\qquad N:=\frac{M}{2}=\frac{q^2-1}{2}.
]
By the **Bose–Chowla** construction, there is a set (S\subset{1,\dots,q^2-2}) with (|S|=q) that is Sidon modulo (q^2-1) (hence Sidon in (\mathbb Z) as well). ([arXiv][1])

Now split (S) into even and odd elements:
[
S_{\rm even}=S\cap 2\mathbb Z,\qquad S_{\rm odd}=S\cap(2\mathbb Z+1).
]
A key point is: in a Sidon set modulo (M), each **nonzero directed difference** (s_1-s_2) occurs in at most one way. Using this, one shows that the directed differences inside (S_{\rm even}) and inside (S_{\rm odd}) are disjoint and all lie among the **even residues** mod (M=2N), of which there are only (N-1). This forces (|S_{\rm even}|) and (|S_{\rm odd}|) to both be about (q/2) (up to (O(\sqrt q))).

Then choose equal-sized subsets (E\subset S_{\rm even}), (O\subset S_{\rm odd}) with
[
|E|=|O|=m=\frac{q}{2}-O(\sqrt q),
]
and define
[
A:={e/2:e\in E}+1,\qquad B:={(o-1)/2:o\in O}+1.
]
These satisfy (A,B\subset[N]), both are Sidon, and ((A-A)\cap(B-B)={0}).

Finally, (|A|=|B|=m), so
[
\binom{|A|}{2}+\binom{|B|}{2}=2\binom{m}{2}=m(m-1)=\left(\frac12+o(1)\right)N.
]
And since (f(N)\sim \sqrt N), we also have (\binom{f(N)}{2}=\left(\frac12+o(1)\right)N). Hence the ratio tends to (1).

So the “((1-c+o(1)))” bound with any fixed (c>0) cannot hold.

## The ( \binom{f(N)}{2}+O(1)) question is still open

The original question
[
\binom{|A|}{2}+\binom{|B|}{2}\ \le\ \binom{f(N)}{2}+O(1)
]
is, as far as is currently recorded, **still open**.

What *is* known is that the **main term** (\sim N/2) is the right scale: this is closely related to results on **difference triangle sets**, where one has bounds of the shape “scope (\gtrsim 2k^2)” for two blocks of size (k+1). Converting this gives (in the equal-size case) upper bounds like
[
|A|=|B|\ \le\ \sqrt{N/2}+O(N^{1/4}),
]
hence
[
\binom{|A|}{2}+\binom{|B|}{2}\ \le\ \frac{N}{2}+O(N^{3/4})
=(1+o(1))\binom{f(N)}{2}.
]
But this is far from an additive (O(1)) comparison.

So, in short:

* **First inequality with (+O(1)):** open.
* **Equal-size constant-factor improvement ((1-c)):** false, and sharp examples exist with ratio (1-o(1)). ([arXiv][1])

[1]: https://arxiv.org/pdf/2104.12711?utm_source=chatgpt.com "arXiv:2104.12711v3 [math.NT] 30 Apr 2021"
