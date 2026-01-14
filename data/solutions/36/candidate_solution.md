Let
[
M_x(A,B):=#{(a,b)\in A\times B:\ a-b=x}.
]
For a fixed (N), define the “worst best overlap”
[
M(N)\ :=\ \min_{A\sqcup B=[2N],,|A|=|B|=N}\ \max_{x\in\mathbb Z} M_x(A,B).
]
Then your statement (“for every partition there exists some (x) with (M_x(A,B)\ge cN)”) is exactly the assertion
[
M(N)\ \ge\ cN\quad\text{for all sufficiently large }N.
]
So the *optimal* constant is
[
c_{\mathrm{opt}}=\lim_{N\to\infty}\frac{M(N)}{N},
]
provided this limit exists.

### What is known: this is Erdős’s minimum overlap problem

This limit **does exist** (proved via a continuous/step-function reformulation due to Swinnerton-Dyer; see e.g. the modern writeups). It is usually denoted (\mu) and is called the **minimum overlap constant**. 

The exact value of (\mu) is **not known** at present; the problem is a classical open one (Erdős 1955). ([Wikipedia][1])

### Best current numerical bounds (as of Jan 2026)

The strongest published bounds I can verify from the literature and recent updates are
[
0.379005\ \le\ \mu\ \le\ 0.380924.
]

* The **lower bound** (\mu\ge 0.379005) is proved by Ethan P. White (2022) using Fourier analysis and convex/linear programming. 
* The **upper bound** (\mu\le 0.380924) comes from an explicit step-function construction reported as a slight improvement over the earlier (0.38092685\ldots) bound (Haugland 2016). ([Erdős Problems][2])

So, in the language of your question:

* Any (c\le 0.379005) is **guaranteed** (for all sufficiently large (N)).
* No (c>0.380924) can be guaranteed (there are partitions with (\max_x M_x(A,B)\le (0.380924+o(1))N)). ([Erdős Problems][2])

### Some quick baseline bounds (to orient the scale)

These are not optimal anymore, but they explain why (c) is a constant (>0):

* **Trivial lower bound (c\ge \tfrac14)**:
  (\sum_x M_x(A,B)=|A||B|=N^2), and there are (4N-1) possible differences (x\in[-(2N-1),2N-1]), so
  [
  \max_x M_x(A,B)\ \ge\ \frac{N^2}{4N-1}\ =\left(\frac14+o(1)\right)N.
  ]
  This is the classic averaging argument already noted in modern sources. 

* **Simple construction giving (c\le \tfrac12)**:
  Take (A) to be a “middle interval” of length (N), e.g. (A=[N/2,3N/2]\cap\mathbb Z) (for even (N)); then one can check (\max_x M_x(A,B)\le N/2), giving (M(N)\le N/2). 

Between these, decades of work pushed the bounds to the tight window ([0.379005,,0.380924]). ([Wikipedia][1])

---

**Answer (best possible with current knowledge):** the optimal constant is the *minimum overlap constant*
[
c_{\mathrm{opt}}=\mu=\lim_{N\to\infty}\frac{1}{N}\min_{A\sqcup B=[2N],,|A|=|B|=N}\max_x #{(a,b)\in A\times B:\ a-b=x},
]
which is known to exist, and the best current bounds are
[
0.379005\ \le\ c_{\mathrm{opt}}\ \le\ 0.380924.
]


[1]: https://en.wikipedia.org/wiki/Minimum_overlap_problem "Minimum overlap problem - Wikipedia"
[2]: https://www.erdosproblems.com/tags/number%20theory "
  
    Erdős Problems
  
"
