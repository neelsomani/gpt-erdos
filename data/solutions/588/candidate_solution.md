No one knows at present [[nomath]](even for $k=4$)[[/nomath]].

A few remarks to connect your (f_k(n)) to the standard formulations:

* Under the hypothesis “no $k+1$ points on a line”, every line that contains (\ge k) points in fact contains **exactly $k$** points. So (f_k(n)) is the same as the extremal function “maximum number of $k$-point lines determined by $n$ planar points with no $(k+1)$-point line”.

* This is an Erdős problem: Erdős conjectured that for fixed (r>k>3) the maximum number of $k$-point lines in an $n$-point set with no $r$ collinear points is $o(n^2)$; your case is (r=k+1). 

### Status

* The statement (f_k(n)=o(n^2)) for (k\ge 4) is **open** (this is explicitly listed as Erdős Problem #588). ([Erdős Problems][1])
* Even the first new case $k=4$ (“no five collinear, count 4-point lines”) is open (Erdős Problem #101). ([Erdős Problems][2])

### What is known

**1) Trivial upper bounds (still quadratic).**
A simple double-counting of pairs gives
[
f_k(n)\binom{k}{2} \le \binom{n}{2}
\quad\Rightarrow\quad
f_k(n)\le \frac{\binom{n}{2}}{\binom{k}{2}}=\Theta(n^2).
]
Also, by the Szemerédi–Trotter theorem, the number of $k$-rich lines [[nomath]](lines incident to at least $k$ points)[[/nomath]] is
[
O!\left(\frac{n^2}{k^3}+\frac{n}{k}\right),
]
which for fixed $k$ is again $O(n^2)$, not $o(n^2)$. ([Wikipedia][3])

So at the moment there is **no known** general method to beat the quadratic order for fixed (k\ge 4).

**2) Lower bounds [[nomath]](almost quadratic, but still $o(n^2)$)[[/nomath]].**
Erdős originally asked [[nomath]](already for $k=4$)[[/nomath]] whether one can get “many” collinear $k$-tuples without having ((k+1)) on a line. For (k\ge 4), Solymosi–Stojaković constructed $n$-point sets with no $k+1$ collinear points but with at least
[
n^{,2-\frac{c}{\sqrt{\log n}}}
]
distinct $k$-point lines [[nomath]](equivalently, collinear $k$-tuples)[[/nomath]]. 
This shows that if the conjecture (f_k(n)=o(n^2)) is true, it is **extremely tight**: you cannot hope to prove something like (f_k(n)=O(n^{2-\varepsilon})) for any fixed (\varepsilon>0). 

Earlier lower bounds (much smaller than this) include (f_k(n)\gg_k n\log n) (Kárteszi) and (f_k(n)\gg_k n^{1+1/(k-2)}) (Grünbaum). ([Erdős Problems][1])

**3) Contrast with $k=3$.**
The restriction (k\ge 4) is necessary: for $k=3$ the maximum number of 3-point lines with no 4 collinear is (\sim \frac{1}{6}n^2) (the classical orchard problem), so (f_3(n)) is (\Theta(n^2)), not $o(n^2)$. ([Erdős Problems][1])

### Bottom line

For every fixed (k\ge 4),
[
n^{2-O(1/\sqrt{\log n})}\ \lesssim\ f_k(n)\ \lesssim\ C_k,n^2,
]
and whether (f_k(n)=o(n^2)) [[nomath]](equivalently, whether $f_k(n)/n^2\to 0$)[[/nomath]] is **still unknown**. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/588 "
  
    Erdős Problem #588
  
"
[2]: https://www.erdosproblems.com/101 "
  
    Erdős Problem #101
  
"
[3]: https://en.wikipedia.org/wiki/Szemer%C3%A9di%E2%80%93Trotter_theorem?utm_source=chatgpt.com "Szemerédi–Trotter theorem"
