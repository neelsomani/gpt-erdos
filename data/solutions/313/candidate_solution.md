Let
$
\frac1{p_1}+\cdots+\frac1{p_k}=1-\frac1m,\qquad m\ge2,\quad p_1<\cdots<p_k\ \text{distinct primes}.
$

### Step 1: In any solution, $m$ must equal the product (p_1\cdots p_k)

Write (P=p_1p_2\cdots p_k). Multiplying the equation by (mP) gives
[
m\sum_{i=1}^k \frac{P}{p_i}=(m-1)P.
]
The left-hand side is divisible by $m$, so the right-hand side is divisible by $m$. Since (\gcd(m,m-1)=1), it follows that
[
m \mid P.
]
So every prime factor of $m$ is among the (p_i), and $m$ is squarefree.

Now multiply the original equation by $m$:
[
\sum_{i=1}^k \frac{m}{p_i}=m-1\in\mathbb Z.
]
If some (p_i\nmid m), then (\frac{m}{p_i}) is a non-integer fraction whose denominator (in lowest terms) is the prime (p_i), and no other term can cancel that denominator because the primes (p_i) are distinct. More formally: let (A={i: p_i\nmid m}) and (Q=\prod_{i\in A}p_i). Then
[
Q\sum_{i\in A}\frac{m}{p_i}=m\sum_{i\in A}\frac{Q}{p_i}\in\mathbb Z.
]
Reduce this congruence mod a fixed (p_j) with (j\in A): every term except the $i=j$ term is divisible by (p_j), leaving
[
m\frac{Q}{p_j}\equiv 0\pmod{p_j},
]
impossible because (p_j\nmid m) and (p_j\nmid Q/p_j). Hence (A=\varnothing), so **every (p_i\mid m)**. Combined with (m\mid P), we get
[
m=P=p_1p_2\cdots p_k.
]

So for each fixed $m$, there is **at most one** candidate set of primes: the prime divisors of $m$. [[nomath]](In particular, this question is really about which $m$ work, not about multiple prime-sets for a fixed $m$.)[[/nomath]] ([erdosproblems.com][1])

### Step 2: The problem becomes “are there infinitely many primary pseudoperfect numbers?”

With (m=\prod p_i), the equation is equivalent to
[
\frac1m+\sum_{p\mid m}\frac1p=1,
]
where the sum is over the prime divisors of $m$. Integers (m>1) satisfying this are called **primary pseudoperfect numbers**. ([OEIS][2])

So your question is equivalent to:

> Are there infinitely many primary pseudoperfect numbers?

### What is known?

This is **open**: it is **not known** whether there are infinitely many solutions / infinitely many primary pseudoperfect numbers. ([erdosproblems.com][1])

As of the most recently updated OEIS entry (Jan 16, 2026), **eight** are known:
[
2,\ 6,\ 42,\ 1806,\ 47058,\ 2214502422,\ 52495396602,\ 8490421583559688410706771261086.
]
([OEIS][2])

Each such $m$ gives exactly one solution, using its prime factors [[nomath]](e.g. $6=2\cdot3$ gives $1/2+1/3=1-1/6$; $42=2\cdot3\cdot7$ gives $1/2+1/3+1/7=1-1/42$)[[/nomath]]. ([erdosproblems.com][1])

So the best current answer is: **it is unknown whether there are infinitely many solutions.**

[1]: https://www.erdosproblems.com/tags/number%20theory "
  
    Erdős Problems
  
"
[2]: https://oeis.org/A054377 "A054377 - OEIS"
