Both questions are **open** in the sense you ask [[nomath]](with an absolute constant $C$ independent of $k$, and with cube dimension unbounded)[[/nomath]].

## 1) Quasi-progressions in the squares

Your inequality
[
x_i+d\le x_{i+1}\le x_i+d+C
]
is exactly the “$k$-term quasi-progression of diameter $C$” notion introduced by Brown–Erdős–Freedman: the consecutive gaps (x_{i+1}-x_i) all lie in an interval $[N,N+C]$ for some $N$. A set has **property QP** if there exists a *fixed* diameter $C$ for which it contains $k$-term quasi-progressions of that diameter for every $k$. 

The specific question “do the squares have property QP?” is recorded as a problem of Brown–Erdős–Freedman and is listed (as Erdős problem #782) as **unsolved**. ([Erdős Problems][1])

### What *is* known

* The squares contain **no** 4-term *exact* arithmetic progression [[nomath]](so not $k$-QP$0$ for $k\ge4$)[[/nomath]], but they do contain many 3-term APs. 
* Even though 4-APs do not exist, Brown–Freedman–Shiue showed there are **infinitely many 4-term quasi-progressions of diameter 1** [[nomath]](i.e. 4-QP$1$)[[/nomath]] among the squares. 
* For longer quasi-progressions with small fixed diameter, essentially nothing definitive is known: they explicitly note they do **not** know whether any 5-QP$1$ exists, and they report not having found a 5-QP$5$ [[nomath]](they give examples of 5-QP$6$)[[/nomath]]. 
* They even propose a **conjecture in the negative direction**: for each fixed $K$, sufficiently long progressions of squares should fail to be $n$-QP((K)), which would rule out any absolute $C$. 

So at present: **no constant $C$ is known to work**, and no proof is known that none can.

## 2) Arbitrarily large “cubes” (Hilbert/affine cubes) in the squares

Your set
[
a+\\{\sum_i \epsilon_i b_i:\epsilon_i\in{0,1}\\}
]
is the standard **Hilbert cube / affine cube** $H(a_0;a_1,\dots,a_d)$. 

The question “do the squares contain arbitrarily large cubes (unbounded dimension)?” is also part of the same circle of problems and is likewise **open unconditionally**. ([Erdős Problems][1])

### Relation to quasi-progressions

Brown–Erdős–Freedman prove a chain of implications between several “progression-like” properties, including
[
\text{AP}\Rightarrow \text{QP}\Rightarrow \text{CP}\Rightarrow \text{C}\Rightarrow \text{DW},
]
where **C** is “contains arbitrarily large cubes.” In particular, a **positive** answer to your quasi-progression question (property QP for the squares) would imply a **positive** answer to the cube question. 

### What *is* known [[nomath]](upper bounds in $[1,N]$)[[/nomath]]

While we cannot rule out unbounded dimension in the whole set of squares, we *can* bound the dimension of a cube of squares that is confined to $[1,N]$:

* Dietmann–Elsholtz prove: if a Hilbert cube $H(a_0;a_1,\dots,a_d)$ is contained in the squares (\cap[1,N]) for $N$ sufficiently large, then
  [
  d \le 7\log\log N.
  ]
  So cubes in initial segments of the squares have dimension at most on the order of (\log\log N). 
* Earlier bounds (weaker, but historically relevant) were (d=O((\log N)^{1/3})) (Hegyvári–Sárközy) and then (O((\log\log N)^2)) (Dietmann–Elsholtz’s earlier work), both summarized in the same literature. 

These results don’t settle “arbitrarily large dimension” [[nomath]](since $N$ is allowed to grow)[[/nomath]], but they show that if you want dimension $d$, you must go to extremely large squares—roughly $N$ at least double-exponential in $d$.

### Conjectures and conditional results (negative direction)

There is notable evidence pointing toward a **negative** answer for large cubes:

* Cilleruelo–Granville (reporting a conjecture of Solymosi) state: **there exists an integer (d>0)** such that there is **no affine cube of dimension $d$** consisting of *distinct squares*. 
* They also explain that this type of conjecture would follow from the **Bombieri–Lang conjecture** (and Dietmann–Elsholtz similarly note that Bombieri–Lang would imply the cube dimension in the squares is absolutely bounded). 

### Existence in small dimension

Even though unbounded dimension is open, small-dimensional cubes do exist:

* A conference abstract by Elsholtz–Ulas announces that there are **infinitely many Hilbert cubes of dimension 3** in the set of squares. 

## Bottom line

* **Arbitrarily long quasi-progressions with a fixed additive slack $C$** in the squares: **open**. We know infinitely many 4-term examples even with $C=1$, but nothing like “all $k$” for a fixed $C$. ([Erdős Problems][1])
* **Arbitrarily large Hilbert/affine cubes** in the squares (unbounded dimension): **open**. The best unconditional theorems give only (d\ll \log\log N) for cubes inside $[1,N]$, and there are strong conjectures (and Bombieri–Lang–conditional arguments) suggesting the answer should be **no**. 

If you want, I can also sketch (at a high level) why Bombieri–Lang is relevant here (it’s via interpreting certain “many squares at translated positions” configurations as rational points on high-genus curves/surfaces, where Bombieri–Lang predicts uniform boundedness).

[1]: https://www.erdosproblems.com/latex/782 "
  
    Erdős Problems
  
"
