Interpreting “diagonals” in the usual way (i.e. **chords** of a cycle: edges joining two nonconsecutive vertices on that cycle), your condition is

[
\text{for every cycle }C,\quad |\text{chords}(C)|<|V(C)|.
]

Equivalently, the vertex set of any cycle spans (<2|V(C)|) edges (cycle edges + chords).

With that interpretation, the answer to “is (f(n)\ll n)?” is:

**This is open.** It is Erdős’ Problem #642 (attributed there to Hamburger–Szegedy). ([Erdős Problems][1])

What is known is that $f(n)$ is *almost* linear up to polylog factors:

* Chen–Erdős–Staton (1996) proved the first superlinear-forcing result, which translates to
  [
  f(n)\ll n^{3/2}.
  ]
  ([Erdős Problems][1])
* Draganić–Methuku–Munhá Correia–Sudakov (2024) greatly improved this, showing that every $n$-vertex graph with at least (n\log^{8}n) edges contains a cycle with at least (|C|) chords [[nomath]](so graphs satisfying your condition have $O(n\log^{8}n)$ edges)[[/nomath]]:
  [
  f(n)\ll n(\log n)^8.
  ]
  ([Erdős Problems][1])

On the **lower-bound** side, there are easy linear constructions [[nomath]](so $f(n)=\Omega(n)$)[[/nomath]]; for example (K_{3,n-3}) has $3n-9$ edges and every cycle has length $4$ or $6$, with fewer chords than vertices, so (f(n)\ge 3n-9). (No superlinear lower bound is currently known; the 2024 paper explicitly notes that even proving *any* superlinear lower bound would be interesting.) 

So, as of now:

[
3n-O(1)\ \le\ f(n)\ \le\ O\bigl(n(\log n)^8\bigr),
]

and whether (f(n)=O(n)) remains unsolved. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/642 "
  
    Erdős Problem #642
  
"
