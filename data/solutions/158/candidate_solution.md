Your hypothesis is exactly that (A) is an **infinite (B_2[2]) set**: every integer (n) has at most (2) (unordered) representations (n=a+b) with (a\le b), (a,b\in A).

The statement you ask about,
[
\liminf_{N\to\infty}\frac{|A\cap{1,\dots,N}|}{\sqrt N}=0,
]
is **conjectured to be true for every infinite (B_2[g]) set**, but it is **not known even for (g=2)**.

* Cilleruelo–Trujillo explicitly state that for (g>1) it is conjectured that (\liminf A(x)/\sqrt{x}=0), but that it is “unknown even for (g=2)”. ([ResearchGate][1])
* On MathOverflow, Mark Lewko similarly notes that it is open whether (r(n)\le 2) forces (|A\cap[1,n]|=o(\sqrt n)), and ties this to longstanding Erdős–Turán-type problems. ([MathOverflow][2])

What *is* known (for context):

* For **Sidon sets** ((B_2[1]), i.e. at most one representation), Erdős proved a much stronger “infinitely often” upper bound implying
  (\displaystyle \liminf_{N\to\infty} \frac{|A\cap[1,N]|}{\sqrt N}=0). ([ResearchGate][1])
* For (B_2[2]), there are constructions showing the **(\limsup)** can be large (so the set can be quite dense along some subsequence), e.g. Cilleruelo–Trujillo exhibit (B_2[2]) with (\limsup A(x)/\sqrt{x}=\sqrt{3/2}). ([ResearchGate][1])
  But this does **not** control the (\liminf), which is the hard part.

So, in short: **no proof or counterexample is currently known** (in the literature I can find) that settles your (\liminf) question; it remains an open problem for (g=2). ([ResearchGate][1])

[1]: https://www.researchgate.net/publication/225341508_InfiniteB2g_sequences "(PDF) InfiniteB2[g] sequences"
[2]: https://mathoverflow.net/questions/223805/is-there-a-complete-sidon-sequence "nt.number theory - Is there a \"complete\" Sidon sequence? - MathOverflow"
