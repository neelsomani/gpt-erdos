What you wrote is *not* known to be true at present: it is an open Erdős problem (Erdős Problems Project **#932**) as of January 2026. ([Erdős Problems][1])

To restate the condition in standard language: if (g:=p_{r+1}-p_r), you’re asking for infinitely many prime gaps $(p_r,p_{r+1})$ that contain **at least two $g$-smooth integers**, i.e. integers $n$ whose *largest* prime factor is (<g).

## Small examples (just to see the phenomenon)

For instance:

* $(7,11)$ has $g=4$, and (8=2^3), (9=3^2) both have all prime factors (<4).
* $(23,29)$ has $g=6$, and (24=2^3\cdot 3), (25=5^2), (27=3^3) all have prime factors (<6).

(These match what you’ll see in the little table I computed above.)

## What *is* known unconditionally: “at least one” is easy

If you weaken “at least two integers” to “at least one integer”, then it’s straightforward to prove there are infinitely many such $r$. This is also noted in the discussion of the problem. ([Erdős Problems][1])

Here is a clean proof.

### Claim (easy variant)

For infinitely many $r$, there exists **at least one** integer (p_r<n<p_{r+1}) whose prime factors are all (<p_{r+1}-p_r).

### Proof

Take (n=2^k) with (k\ge 3). Then $n$ is composite and lies between two consecutive primes (p_r < n < p_{r+1}).

Let (g:=p_{r+1}-p_r) be the length of that prime gap. We claim (g\neq 2), hence (since gaps between odd primes are even) (g\ge 4).

Indeed, $g=2$ would mean $n$ is the unique integer between twin primes, i.e.
[
2^k-1 \ \text{and}\ 2^k+1 \ \text{are both prime}.
]
But modulo $3$, (2^k) is $2$ when $k$ is odd and $1$ when $k$ is even. Thus:

* if $k$ is odd, (2^k\equiv 2\pmod 3), so (2^k+1\equiv 0\pmod 3) and (2^k+1>3), hence composite;
* if $k$ is even, (2^k\equiv 1\pmod 3), so (2^k-1\equiv 0\pmod 3) and (2^k-1>3), hence composite.

So (2^k-1) and (2^k+1) cannot both be prime when (k\ge 3). Therefore (g\neq 2), hence (g\ge 4).

But the only prime factor of (n=2^k) is $2$, and (2<4\le g). So **all** prime factors of $n$ are (<g=p_{r+1}-p_r), as required.

Since there are infinitely many (k\ge 3), this gives infinitely many $r$. ∎

## Why your “at least two” version is hard (and still open)

The “two numbers in the same gap” strengthening is currently **open**. ([Erdős Problems][1]) Erdős believed it should be true but very rare, and (according to the Erdős Problems Project summary) he could show that the set of $r$ for which **even one** such $n$ exists has density $0$. ([Erdős Problems][1])

Terence Tao (in the same discussion thread) points out that heuristics put it right on the border of plausibility: combining Cramér-type expectations for prime gaps with de Bruijn–type heuristics for smooth numbers makes it “delicate” whether one should expect infinitely many occurrences of *two* such smooth numbers inside a single gap. ([Erdős Problems][1])

## Related progress in the opposite direction (rough numbers)

There *has* been very recent progress on a “dual” question (rough instead of smooth): Tao and Gafni (2025) study prime gaps that contain an integer whose **least** prime factor is at least the gap length, and prove that **almost all** prime gaps contain such a “rough” number (with a quantitative upper bound on exceptions). ([What's new][2])
That result is about the opposite extreme of factorization behavior inside gaps, but it’s a useful indicator of what modern sieve methods can and cannot yet control in these problems.

## If you want something actionable

If your goal is to **work on** the statement you wrote, the best current direction (at least from the literature around large gaps) seems to be to connect it to the structure of sieving constructions for prime gaps, where “survivors” after partial sieving are often either primes or smooth numbers; this smooth-number obstruction is explicitly discussed in expositions of large-gap methods. ([What's new][3])
But turning that into “there are *two* smooth numbers in an actual prime gap” is exactly the missing step.

If you tell me whether you want:

* a survey of what’s known/related (with references), or
* a deeper heuristic model for why “two” might be true/false, or
* computational exploration [[nomath]](e.g., finding all such $r$ up to some bound and patterns)[[/nomath]],

I can go straight into that.

[1]: https://www.erdosproblems.com/forum/thread/932 "

    Erdős Problem #932 - Discussion thread

"
[2]: https://terrytao.wordpress.com/2025/08/10/rough-numbers-between-consecutive-primes/ "Rough numbers between consecutive primes | What's new"
[3]: https://terrytao.wordpress.com/2014/08/21/large-gaps-between-consecutive-prime-numbers/ "Large gaps between consecutive prime numbers | What's new"
