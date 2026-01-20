Let (A\subseteq{1,\dots,n}). Your condition says:

> for every (a\in A), there are **not** two distinct (b,c\in A\setminus{a}) with (a\mid b) and (a\mid c).

Equivalently: **each element of $A$ divides at most one other element of $A$.**

## A clean lower bound: (f(n)\ge \lceil 2n/3\rceil)

Take
[
A={\lfloor n/3\rfloor+1,\ \lfloor n/3\rfloor+2,\ \dots,\ n}.
]
Then (|A|=n-\lfloor n/3\rfloor=\lceil 2n/3\rceil).

Why does it work? If (a>\frac n3), then (3a>n), so among ({1,\dots,n}) the only possible multiples of $a$ are $a$ itself and possibly (2a). In particular, $a$ cannot divide **two** distinct larger numbers (\le n). Hence this $A$ satisfies the condition, so
[
f(n)\ \ge\ \left\lceil \frac{2n}{3}\right\rceil.
]
This basic construction is the standard starting point for the problem. ([Erdős Problems][1])

## Best published asymptotic bounds (Lebensold)

The strongest “headline” bounds I can find in standard references are due to Kenneth Lebensold $1976/77$. They say that for **all sufficiently large $n$**,
[
0.6725,n \ \le\ f(n)\ \le\ 0.6736,n.
]
So $f(n)$ is known to be linear in $n$, with an asymptotic density pinned down to a very narrow window around (0.673). ([Erdős Problems][1])

This problem is listed as **B24** in Guy’s *Unsolved Problems in Number Theory*, and the Erdős Problems database records exactly the same bounds and references. ([Erdős Problems][1])

A later discussion [[nomath]](e.g. in Hegarty’s work on “$k$-primitive sets,” where this is the case $k=2$)[[/nomath]] notes that Lebensold’s methods can in principle be pushed to tighten the gap further with more computation, but without fundamentally new ideas. ([Academia][2])

## Does (\lim_{n\to\infty} f(n)/n) exist? Is it irrational?

What is known from the above is:

* (\displaystyle \liminf_{n\to\infty}\frac{f(n)}n \ge 0.6725),
* (\displaystyle \limsup_{n\to\infty}\frac{f(n)}n \le 0.6736),

for large $n$. ([Erdős Problems][1])

But the **exact limiting value** is not given by these results, and the problem is explicitly posed as open in the standard problem lists: Erdős asked whether (\lim f(n)/n) is irrational. ([Erdős Problems][3])

So, in short:

* The best-known results place the density in a tight interval $[0.6725,,0.6736]$ for large $n$. ([Erdős Problems][1])
* Whether the limit (\lim_{n\to\infty} f(n)/n) **exists**, and if it exists whether it is **irrational**, remains **open** in the sources above. ([Erdős Problems][3])

## Extra: where to find exact small values

The Erdős Problems page also points to an OEIS entry for the sequence (n\mapsto f(n)) (A038372). ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/1062 "https://www.erdosproblems.com/1062"
[2]: https://www.academia.edu/38731425/AN_IMPROVED_UPPER_BOUND_ON_THE_MAXIMUM_SIZE_OF_k_PRIMITIVE_SETS "https://www.academia.edu/38731425/AN_IMPROVED_UPPER_BOUND_ON_THE_MAXIMUM_SIZE_OF_k_PRIMITIVE_SETS"
[3]: https://www.erdosproblems.com/latex/1062 "https://www.erdosproblems.com/latex/1062"
