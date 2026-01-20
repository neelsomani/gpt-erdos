This is **currently an open problem**.

Let
[
S={n\in\mathbb N:\ \varphi(n)=\varphi(n+1)},\qquad S(x)=|{n\le x:\ n\in S}|.
]
A 2020 paper of Kinlaw–Kobayashi–Pomerance explicitly states:

* “**It is still not known if there are infinitely many solutions**.” 
* It is nevertheless **conjectured** (going back to Erdős–Pomerance–Sárközy) that $S(x)$ is “large” in a sub-polynomial-density sense, e.g. $S(x)>x^{1-\varepsilon}$ for every (\varepsilon>0) once $x$ is large enough, which would in particular imply infinitely many solutions. 

What *is* known (context):

* The set $S$ has **asymptotic density 0** [[nomath]](so $S(x)/x\to 0$)[[/nomath]]. 
* There are strong **upper bounds** on $S(x)$; for example Erdős–Pomerance–Sárközy proved
  [
  S(x)\ \ll\ \frac{x}{\exp((\log x)^{1/3})},
  ]
  and later work improves the exponent (the Kinlaw–Kobayashi–Pomerance paper notes an improvement to a square-root exponent). ([Erdős Problems][1])
* Computationally, there are lots of solutions: the same 2020 paper reports an exhaustive computation up to (10^{13}) yielding **10,755** solutions in that range. 
  The beginning of the sequence is
  [
  1,3,15,104,164,194,255,495,584,975,\dots
  ]
  ([OEIS][2])

Related progress [[nomath]](but not for $k=1$)[[/nomath]]:

* For the more general equation (\varphi(n)=\varphi(n+k)), Kevin Ford proved that **for some even (k\le 3570)** [[nomath]](and for all $k$ divisible by a certain large integer)[[/nomath]] the equation has **infinitely many** solutions $n$; these arguments use modern results on bounded gaps between primes / prime $k$-tuples. ([arXiv][3])
  This highlights that the **specific case $k=1$** remains stubbornly open.

So: **we do not currently know** whether there are infinitely many $n$ with (\varphi(n)=\varphi(n+1)), though it is widely believed there should be infinitely many. 

[1]: https://www.erdosproblems.com/1003 "
  
    Erdős Problem #1003
  
"
[2]: https://oeis.org/A001274 "A001274 - OEIS"
[3]: https://arxiv.org/abs/2002.12155 "[2002.12155] Solutions of $ϕ(n)=ϕ(n+k)$ and $σ(n)=σ(n+k)$"
