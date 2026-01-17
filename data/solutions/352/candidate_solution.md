As of **January 2026**, this is **still open** in full generality (it’s an Erdős problem, listed as *Erdős Problem #352*). ([Erdős Problems][1])

### What is known

#### 1) A sharp lower bound if such a constant exists

If there *is* a universal constant $c$, it must satisfy
[
c \ge c_0 := \frac{4\pi}{\sqrt{27}} \approx 2.418399\ldots
]
Reason: the triangle of **maximum** area inscribed in a circle is equilateral, and its area [[nomath]](for circumradius $R$)[[/nomath]] is
[
A_{\max}(R)=\frac{3\sqrt{3}}{4}R^2.
]
So if (R < 2\cdot 3^{-3/4}), then (A_{\max}(R)<1), meaning the disk of radius $R$ contains **no** triangle of area $1$. The critical disk [[nomath]](where $A_{\max}=1$)[[/nomath]] has area (\pi R^2 = 4\pi/\sqrt{27}). This is exactly the obstruction Erdős pointed out, and the same constant is highlighted in later discussions. 

Erdős speculated that this (c_0) might actually be the correct threshold. ([Erdős Problems][1])

#### 2) If $A$ is “large” in an unbounded sense, the answer is yes

Erdős observed (and later authors give proofs) that if $A$ has **infinite Lebesgue measure**, then in fact $A$ contains triangles of **every prescribed area** (a>0), hence in particular area $1$. 

Moreover, a stronger modern statement is known: if (A\subset\mathbb R^2) is **unbounded** and has **positive** measure, then $A$ contains (for example) an **isosceles** triangle of area $1$ [[nomath]](and also a right triangle of area $1$)[[/nomath]]. 

So the difficulty is really about **bounded** (or potentially very “fragmented”) sets of **finite** measure.

#### 3) The problem is solved for convex sets (and some finite unions)

Freiling and Mauldin proved that if a set has **outer measure** (>4\pi/\sqrt{27}), then it contains the vertices of a triangle with area (>1). ([Erdős Problems][1])
In particular, for **compact convex** sets this yields the desired “area $1$” conclusion at the same threshold (and this threshold is optimal for convex sets). ([Erdős Problems][1])

Mauldin also explains that it would suffice to prove the conjecture when $A$ is a union of interiors of finitely many compact convex sets, and reports that Freiling–Mauldin proved the conjectured constant works at least for (n\le 3) such convex pieces. ([Erdős Problems][1])

### Current status

So, in short:

* **General measurable $A$** with (|A|\ge c): **open**. ([Erdős Problems][1])
* The **best possible** candidate (if true) is believed to be
  [
  c_0=\frac{4\pi}{\sqrt{27}}\approx 2.4184,
  ]
  and you can’t do better because of the disk obstruction. ([Erdős Problems][1])
* The statement **is true** under additional hypotheses [[nomath]](e.g. $A$ unbounded with positive measure; $A$ convex; unions of up to 3 convex interiors)[[/nomath]]. 

If you want, I can also sketch the standard density-theorem/Steinhaus-style argument showing the **infinite measure** (or **unbounded positive measure**) case, since that part is quite clean.

[1]: https://www.erdosproblems.com/352 "
  
    Erdős Problem #352
  
"
