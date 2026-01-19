Yes.

Take
[
k=2N-2,\qquad n=-2N,\qquad m=2.
]
Then (k\ge 2) for (N\ge 2), and
[
n+k=-2N+(2N-2)=-2\le 2=m,
]
so the condition (m\ge n+k) holds. Also none of the factors $n+i$ is $0$, since $n+i$ runs from $-2N+1$ up to $-2$.

Now compute the ratio:
[
\prod_{i=1}^{k}(m+i)=\prod_{i=1}^{2N-2}(2+i)=3\cdot 4\cdots (2N)=\frac{(2N)!}{2},
]
and
[
\prod_{i=1}^{k}(n+i)=\prod_{i=1}^{2N-2}(-2N+i)=(-2N+1)(-2N+2)\cdots(-2).
]
This denominator is a product of $2N-2$ negative integers, so it is positive, and its absolute value is
[
(2N-1)(2N-2)\cdots 2=(2N-1)!,
]
hence
[
\prod_{i=1}^{k}(n+i)=(2N-1)!.
]
Therefore
[
\frac{\prod_{i=1}^{k}(m+i)}{\prod_{i=1}^{k}(n+i)}
=

 \frac{(2N)!/2}{(2N-1)!}

 \frac{2N}{2}

N.
]

So every integer (N\ge 2) admits such a representation.
