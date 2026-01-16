Let
[
R_C:={,n\in\mathbb N:\ n=p+\lfloor C^k\rfloor\ \text{for some prime }p\text{ and }k\ge 0,}.
]
Interpreting “density” in the usual Erdős/Romanoff sense as **positive lower asymptotic density**
[
\underline d(R_C):=\liminf_{x\to\infty}\frac{|R_C\cap[1,x]|}{x}>0,
]
the current state of knowledge is:

* **If $C$ is an integer (\ge 2)**, then **yes**: this is exactly a case of **Romanov/Romanoff’s theorem**, which says that for a fixed integer base (b>1), the set of integers of the form (p+b^k) has positive lower asymptotic density. ([Wikipedia][1])

* **For a general fixed real (C>1)**, the problem is **open**. It is recorded as an Erdős problem (originally asked by Kalmár), and it is not known in full generality whether (\underline d(R_C)>0) holds for every single (C>1). ([Erdős Problems][2])

* **What is known beyond the integer case:** Ding (2025) proved that the answer is **yes for almost all (C>1)** in the sense of **Lebesgue measure**—i.e. for all $C$ outside a measure‑zero exceptional set, (R_C) has positive lower asymptotic density. ([arXiv][3])

So the best concise answer to your question as stated is:

> **For a given arbitrary (C>1), it is not known in general.**
> It is known **for integer $C$** (Romanoff), and it is known **for almost every real (C>1)** (Ding 2025). ([Erdős Problems][2])

(Heuristically one expects a positive proportion for every fixed (C>1), since up to size $x$ there are (\asymp \log_C x) shifts (\lfloor C^k\rfloor), and “randomly” each shift gives a prime condition of probability (\sim 1/\log x), suggesting an $O(1)$ expected number of representations per integer; but turning this into a proof for each specific $C$ is exactly what remains hard.)

[1]: https://en.wikipedia.org/wiki/Romanov%27s_theorem "Romanov's theorem - Wikipedia"
[2]: https://www.erdosproblems.com/244 "
  
    Erdős Problem #244
  
"
[3]: https://arxiv.org/abs/2503.22700 "[2503.22700] On a Romanoff type problem of Erdős and Kalmár"
