This is **open** (it is listed as Erdős Problem #654). ([Erdős Problems][1])

What *is* known is the “trivial” linear bound: for **every** point (x_i), each distance value (|x_i-x_j|) can occur for **at most 3** different $j$’s [[nomath]](otherwise those $\ge 4$ points $x_j$ would lie on the same circle centered at $x_i$)[[/nomath]], so
[
|\\{|x_i-x_j|: j\neq i\\}|\ \ge\ \frac{n-1}{3}.
]
This is explicitly noted in the problem statement. ([Erdős Problems][1])

Beyond that, even strengthening the hypotheses doesn’t currently settle the asymptotic “almost all distances distinct” conclusion:

* Erdős and Pach asked variants under **general position** assumptions (e.g. additionally “no three collinear”), but even they only asked for a **constant** improvement ((\tfrac13+c)n) for some (c>0), which is also open. ([Erdős Problems][1])
* They suggested that the stronger $(1-o(1))n$ conclusion might hold under an *even stronger* local condition: **every circle centered at (x_i)** contains at most **2** other points [[nomath]](so no distance from $x_i$ repeats more than twice)[[/nomath]]. ([Erdős Problems][1])

A useful reformulation: if for a given (x_i) many distances repeat, then (x_i) is the apex of many isosceles triangles $(x_i,x_j,x_k)$ with (|x_i-x_j|=|x_i-x_k|). Under “no four concyclic” each “radius class” has size (\le 3), so you can’t get huge multiplicities at a single radius, but the open problem is whether you can still force **some** (x_i) to have only $o(n)$ repeats [[nomath]](equivalently $(1-o(1))n$ distinct distances)[[/nomath]].

So the current state is: **best unconditional guarantee under the stated hypothesis is $(n-1)/3$ for every point, and the $(1-o(1))n$ statement is not known.** ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/654 "
  
    Erdős Problem #654
  
"
