Write $g(n)$ for Jacobsthal’s function [[nomath]](many authors write $j(n)$)[[/nomath]]: the least $m$ such that every block of $m$ consecutive integers contains an integer coprime to $n$. Since coprimality to $n$ depends only on the *set* of primes dividing $n$, one may assume $n$ is squarefree and write (\omega(n)) for the number of distinct prime divisors.

Your $h(k)$ is then
[
h(k)=\max_{\omega(n)\le k} g(n).
]

## Best known general upper bound

A theorem of Iwaniec (1978) implies an upper bound of the shape
[
g(n)\ \ll\ (\omega(n)\log\omega(n))^2,
]
and hence
[
h(k)\ \ll\ (k\log k)^2.
]
This is the best general upper bound currently known (up to constants). ([OEIS][1])

So the conjectural (k^2) bound is *not* known; the best proved bound has an extra ((\log k)^2).

## A strong unconditional lower bound

A useful way to get lower bounds is to take $n$ to be a primorial-type product. Let
[
P(x)=\prod_{p\le x}p.
]
Ford–Green–Konyagin–Maynard–Tao study the “interval sieve” quantity $Y(x)$ and prove
[
Y(x)\ \gg\ \frac{x\log x\log_3 x}{\log_2 x},
]
where (\log_2 x=\log\log x) and (\log_3 x=\log\log\log x), and they note the identity
[
Y(x)=j(P(x))-1=g(P(x))-1.
]
([ORA][2])

Now choose (x=p_k), the $k$-th prime. Then $P(p_k)$ has exactly $k$ distinct prime factors, so by definition
[
h(k)\ \ge\ g(P(p_k))\ =\ Y(p_k)+1\ \gg\ \frac{p_k\log p_k\log_3 p_k}{\log_2 p_k}.
]
Using (p_k\sim k\log k) (prime number theorem), this translates to the more “$k$-only” form
[
h(k)\ \gg\ k(\log k)^2\ \frac{\log\log\log k}{\log\log k}.
]

## What this says about the order of magnitude

Putting the best known bounds together, we currently have (with natural logs)
[
k(\log k)^2\frac{\log\log\log k}{\log\log k}\ \ll\ h(k)\ \ll\ (k\log k)^2.
]

The gap between these bounds is still enormous [[nomath]](essentially a factor of about $k\cdot \frac{\log\log k}{\log\log\log k}$)[[/nomath]], so the *true* order of magnitude of $h(k)$ is not known.

## Is (h(k)\ll k^2) true?

This is exactly the classic conjecture Jacobsthal asked about (in correspondence with Erdős): whether there is an absolute $C$ with $h(k)\le Ck^2$ for all $k$. It remains open. ([arXiv][3])

What *is* known is the weaker bound (h(k)\ll (k\log k)^2) (Iwaniec), and the lower bound above shows $h(k)$ grows faster than (k(\log k)^2) up to the slowly varying (\log\log\log/\log\log) factor. ([OEIS][1])

[1]: https://oeis.org/A048669 "https://oeis.org/A048669"
[2]: https://ora.ox.ac.uk/objects/uuid%3A4f92b379-4935-4df4-ab12-ad6e8e85c965/files/m82130bfb3e8ac4562cce865fd741d525 "https://ora.ox.ac.uk/objects/uuid%3A4f92b379-4935-4df4-ab12-ad6e8e85c965/files/m82130bfb3e8ac4562cce865fd741d525"
[3]: https://arxiv.org/pdf/1208.5342 "https://arxiv.org/pdf/1208.5342"
