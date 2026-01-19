This is still **open** [[nomath]](in particular, the existence of a *limit constant* $c$ is not known)[[/nomath]].

What *is* known goes back to Erdős–Guy–Selfridge (1982), who introduced essentially your $f(n)$ and proved:

* For (n>239) there is **no** representation (n!=a_1\cdots a_k) with
  (n<a_1<\cdots<a_k\le 2n). In particular, for (n>239) one has
  [
  f(n)>2n.
  ]


* There exist absolute constants (0<c_1<c_2) such that for all sufficiently large $n$,
  $
  2n+c_1\frac{n}{\log n}<f(n)<2n+c_2\frac{n}{\log n}.
  $


Moreover, their proof yields **explicit** (not claimed sharp) values:

* the lower-bound constant can be taken **arbitrarily close to $1/9$**, 
* and the upper-bound constant can be taken as **(1.7)**. 

So the best rigorous information from that paper is essentially
[
2n+\left(\frac{1}{9}-o(1)\right)\frac{n}{\log n}\le f(n)\le2n+(1.7+o(1))\frac{n}{\log n}.
]


On the *specific question* you asked—whether there is a constant $c$ with
[
f(n)-2n \sim c\frac{n}{\log n},
]
Erdős–Guy–Selfridge explicitly say (in effect) that they expect such a constant to exist (“No doubt there is a constant…”) but they do **not** prove it. 

The problem is currently listed as open on the Erdős Problems site. ([Erdős Problems][1])

### Why the (n/\log n) scale shows up

A useful way to see where the scale comes from is to start with
[
(n+1)(n+2)\cdots (2n)=n!\binom{2n}{n},
]
and think of producing a factorization of $n!$ by “removing” some factors from $(n,2n]$ and “adding” some factors above $2n$ to compensate for the binomial coefficient. A recent summary (Terence Tao, 2025, in the Erdős Problems discussion thread) explains how primes in certain intervals force (\gg n/\log n) “imbalances” in small prime powers that can only be corrected by having ((2n,f(n)]) long enough, yielding the lower bound; and conversely how one can systematically correct those imbalances with a construction giving the upper bound. ([Erdős Problems][1])

### Small-$n$ data

If you want concrete values for intuition, OEIS sequence A193429 records $f(n)$ for (n\le 62) and matches your definition. ([OEIS][2])

### Bottom line

* The **order of magnitude** is known: (f(n)-2n = \Theta!\bigl(\frac{n}{\log n}\bigr)). ([Erdős Problems][3])
* The existence (and value) of a **limit constant** $c$ in the sense of (\sim) is **not known**; the problem remains open. ([Erdős Problems][1])
* If such a $c$ exists, the 1982 paper’s explicit bounds force it into an interval roughly
  [
  \frac{1}{9}\lesssim c\lesssim1.7
  ]
  (with the understanding that these are not best possible). 

[1]: https://www.erdosproblems.com/forum/thread/390 "

    Erdős Problem #390 - Discussion thread

"
[2]: https://oeis.org/A193429 "A193429 - OEIS"
[3]: https://www.erdosproblems.com/latex/390 "
  
    Erdős Problems
  
"
