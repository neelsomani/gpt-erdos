For **positive integers**, no example is known at the moment.

This is actually a named open problem (Erdős Problem #366): *“Are there any 2-full $n$ such that $n+1$ is 3-full?”* ([Erdős Problems][1])

A quick but important point: if $n+1$ is **3-full**, then it is automatically **2-full** [[nomath]](since “$\ge 3$” implies “$\ge 2$”)[[/nomath]]. So any solution would have to be a pair of **consecutive powerful $2-\text{full}$ numbers**:
[
n \text{ is 2-full and } n+1 \text{ is 2-full.}
]
Those $n$ are exactly the numbers in OEIS **A060355** [[nomath]](numbers $k$ such that $k$ and $k+1$ are powerful)[[/nomath]]. ([OEIS][2])

OEIS lists **all** such (k < 10^{22}) (there are 39 of them). ([OEIS][2])
If you check those 39 candidates, **none** has $k+1$ being 3-full. So there is **no solution with (n < 10^{22})**.

Related fact (but the opposite order): there *are* known consecutive pairs where the first is 3-full and the second is 2-full, like
[
8=2^3 \text{ (3-full)},\quad 9=3^2 \text{ (2-full)}
]
and also
[
12167=23^3 \text{ (3-full)},\quad 12168=2^3\cdot 3^2\cdot 13^2 \text{ (2-full)}.
]
These are mentioned in the Erdős-problems discussion. ([Erdős Problems][1])

So the honest answer today is:

* **No positive solution is known.**
* **None exist below (10^{22})** (by exhaustive checking of all consecutive 2-full pairs in that range).
* **Whether any exist at all is still open.** ([Erdős Problems][1])

[[nomath]](If you allow $n=0$, then $0$ is “2-full” in the divisibility sense and $1$ is vacuously “3-full”, but most number theory problems mean $n\ge1$, and the open problem is about positive $n$.)[[/nomath]]

[1]: https://www.erdosproblems.com/366 "
  
    Erdős Problem #366
  
"
[2]: https://oeis.org/A060355 "A060355 - OEIS"
