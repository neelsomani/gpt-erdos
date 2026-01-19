Write the equation as a “factorial–ratio” identity:
[
\prod_{i=1}^{k_1}(m_1+i)=\frac{(m_1+k_1)!}{m_1!},\qquad
\prod_{j=1}^{k_2}(m_2+j)=\frac{(m_2+k_2)!}{m_2!},
]
so your equation is
[
\frac{(m_1+k_1)!}{m_1!}=\frac{(m_2+k_2)!}{m_2!}
\quad\Longleftrightarrow\quad
(m_1+k_1)!,m_2!=(m_2+k_2)!,m_1!.
]
The condition (m_1+k_1\le m_2) means the two blocks
$[m_1+1,m_1+k_1]$ and $[m_2+1,m_2+k_2]$ are **disjoint** and the second block lies entirely to the right.

## If (m_1,m_2) are arbitrary integers: there are infinitely many solutions

There is a simple infinite family coming from the symmetry (x\mapsto -x).
For any **even** (k\ge 4) and any integer (u\ge 0), set
[
k_1=k_2=k,\qquad m_2=u,\qquad m_1=-u-k-1.
]
Then the two blocks are
[
m_1+1,\dots,m_1+k=-(u+k),\dots,-(u+1),
]
[
m_2+1,\dots,m_2+k=u+1,\dots,u+k,
]
which are negatives of each other, so their products are equal [[nomath]](because $k$ is even)[[/nomath]]. Also
[
m_1+k=-(u+1)\le u=m_2
]
so your spacing condition holds. Hence **infinitely many** solutions exist unless you restrict (m_1,m_2) to be nonnegative/positive.

So the interesting version is usually with (m_1,m_2\ge 0) [[nomath]](or $>0$)[[/nomath]].

## For (m_1,m_2\ge 0): classification is not known; finiteness is open

In the “non-overlapping positive blocks” setting, this is a known hard Diophantine problem (“equal products of consecutive integers”). A classical paper by MacLeod–Barrodale (1970) studied many small cases and did computer searches, and later discussions (and OEIS) emphasize that **only a handful of disjoint-block solutions are known**. 

The currently known **non-overlapping** solutions in positive integers (as listed in the literature and in the MathOverflow/OEIS discussions) are:

* (5\cdot 6\cdot 7=14\cdot 15=210),
* (2\cdot 3\cdot 4\cdot 5\cdot 6=8\cdot 9\cdot 10=720),
* (19\cdot 20\cdot 21\cdot 22=55\cdot 56\cdot 57=175560),
* (8\cdot 9\cdot 10\cdot 11\cdot 12\cdot 13\cdot 14=63\cdot 64\cdot 65\cdot 66=17297280). ([MathOverflow][1])

Under your extra constraints (k_1,k_2>3) and (m_1+k_1\le m_2), among these the only one that qualifies is the last one, corresponding to
[
(m_1,k_1,m_2,k_2)=(7,7,62,4),
]
since (7+7=14\le 62). 

### Is it known that these are all?

No. As of the sources above, **no general classification is known**, and it is **not proved** that there are only finitely many disjoint-block solutions in positive integers. The MathOverflow post records extensive computational searches finding no further disjoint solutions in large ranges, and the OEIS entry also reports searches through many prime gaps with no new terms. ([MathOverflow][1])

## Two easy structural constraints (positive case)

These don’t solve the problem, but they explain why solutions are so constrained:

1. **Necessarily (k_1>k_2)** (in the positive/nonnegative setting).
   Since (m_2+1\ge m_1+k_1+1), every factor on the right is strictly larger than every factor on the left. If the right had at least as many factors as the left, its product would be strictly larger. So any solution with disjoint positive blocks must have the *left block longer*.

2. **The “right” (larger-in-value) block cannot contain a prime.**
   If some (m_2+j) were prime, that prime would be (>m_1+k_1) and hence could not divide the left product at all—contradiction. This is why searches are often organized by scanning prime gaps. (This observation is explicitly noted in the OEIS discussion.) ([OEIS][2])

## Bottom line

* If you allow (m_1,m_2\in\mathbb Z), there are **infinitely many** solutions (e.g. the even-length sign-reflection family above).
* If you mean the usual **positive/nonnegative** version with disjoint blocks, then:

  * only **four** disjoint positive solutions are currently “standardly known” in the literature/discussions,
  * among those, only **one** has (k_1,k_2>3), namely
    [
    8\cdot 9\cdot 10\cdot 11\cdot 12\cdot 13\cdot 14=63\cdot 64\cdot 65\cdot 66,
    ]
  * and **it is open** whether there are finitely many such solutions [[nomath]](and hence open whether this one is the only solution with $k_1,k_2>3$)[[/nomath]]. ([MathOverflow][1])

[1]: https://mathoverflow.net/questions/355829/equal-products-of-consecutive-integers "https://mathoverflow.net/questions/355829/equal-products-of-consecutive-integers"
[2]: https://oeis.org/A163263 "A163263 - OEIS"
