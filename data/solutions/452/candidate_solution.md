Let

[
L(x):=\max\\{|I|:\ I\subseteq [x,2x]\text{ is an interval and }\omega(n)>\log\log n\ \forall n\in I\\}.
]

The exact order of magnitude of $L(x)$ is **not known** (this is an open Erdős–Graham problem). What is known is:

### Density information [[nomath]](global, not giving $L(x)$ directly)[[/nomath]]

Erdős proved (1937) that the set
[
{n:\ \omega(n)>\log\log n}
]
has natural density $1/2$. 

This says that “about half” the integers satisfy the inequality, but it does **not** control the *longest consecutive run* inside $[x,2x]$.

### Guaranteed lower bound via Chinese remainder theorem

One can **construct** an interval (I\subseteq[x,2x]) with

[
|I|\ \ge\ (1+o(1))\frac{\log x}{(\log\log x)^2}.
]

This is the standard CRT lower bound recorded for this problem. ([Erdős Problems][1])

A sketch of the construction (at the level of ideas):

* Let (k:=\lceil \log\log(2x)\rceil+1), so (k>\log\log n) for all (n\in[x,2x]) once $x$ is large.
* Choose $L$ and (kL) distinct primes so that their product $M$ is (\le x). Taking (L\sim \log x/(\log\log x)^2) makes this possible because the product of the first (kL) primes has logarithm [[nomath]](\sim $kL$\log$kL$)[[/nomath]], which you can arrange to be (\le \log x) by that choice of $L$.
* Partition these primes into $L$ blocks of size $k$. For each offset (0\le i<L), impose congruences forcing $n+i$ to be divisible by the $k$ primes in block $i$.
* CRT gives a solution $n$ modulo $M$, and since (M\le x), you can pick a representative (n\in[x,2x]).
* Then each $n+i$ has at least $k$ distinct prime factors, hence (\omega(n+i)\ge k>\log\log(n+i)).

So $L(x)$ is at least (\asymp \log x/(\log\log x)^2).

### What is believed / what remains open

No matching (or even close-to-matching) upper bound is known. In fact, the problem statement explicitly notes that it **could** be that there are intervals of length ((\log x)^k) for arbitrarily large fixed $k$. ([Erdős Problems][1])

So, at present, the best rigorous “size” statement is:

[
L(x)\ \ge\ (1+o(1))\frac{\log x}{(\log\log x)^2},
]

and determining the true growth rate of $L(x)$ is open. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/forum/thread/452 "

    Erdős Problem #452 - Discussion thread

"
