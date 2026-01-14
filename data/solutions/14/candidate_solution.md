Let (r_A(n)) be the (unordered) representation function
[
r_A(n):=#\bigl{{a,a'}\subseteq A:\ a+a'=n\bigr},
]
so (B={n\in\mathbb N:\ r_A(n)=1}) and the “exceptional set” is
[
E(N):=\bigl|{1,\dots,N}\setminus B\bigr|=#{n\le N:\ r_A(n)\ne 1}.
]
(If you instead count *ordered* representations, the questions are equivalent up to harmless constants, so all known bounds have the same exponents.)

### Status

As far as the current literature indicates, **both questions are open**: it is not known whether one always has
[
E(N)\gg_\varepsilon N^{1/2-\varepsilon}\quad\text{for all }\varepsilon>0
]
for all sufficiently large (N), and it is also not known whether there exists (A\subseteq\mathbb N) with
[
E(N)=o(N^{1/2}).
]
This is recorded explicitly as an open Erdős problem (often referred to as Erdős Problem #14). ([Erdős Problems][1])

### What *is* known (best qualitative information I can point to)

* **Upper bounds / constructions.**
  *Erdős* (without giving a published reference) claimed a construction of a set (A) such that for every (\varepsilon>0) and all sufficiently large (N),
  [
  E(N)\ll_\varepsilon N^{1/2+\varepsilon}.
  ]
  ([Erdős Problems][1])

  In the **finite analogue**, Erdős–Freud proved that for each (N) there exists (A\subseteq{1,\dots,N}) for which the number of integers (\le N) that are *not* representable in exactly one way is
  [
  E(N)<2^{3/2}N^{1/2},
  ]
  and they suggested the constant (2^{3/2}) might be best possible. ([Erdős Problems][1])
  (This shows that (\sqrt N) is at least the “right scale” for *some* constructions; it does **not** settle whether one can do (o(\sqrt N)) with a single infinite (A).)

* **Lower-bound phenomena (for at least one construction).**
  Erdős also claimed that his construction (the one giving (E(N)\ll_\varepsilon N^{1/2+\varepsilon})) still has infinitely many (N) with
  [
  E(N)\gg_\varepsilon N^{1/3-\varepsilon}.
  ]
  ([Erdős Problems][1])
  This is **not** a universal lower bound (it’s about that specific (A)), but it indicates that even in “good” examples, the exceptional set may fluctuate and can be significantly larger than (\sqrt N) on some subsequences.

### So, answering your two questions

* The statement
  [
  E(N)\gg_\varepsilon N^{1/2-\varepsilon}\quad(\forall\varepsilon>0,\ N\ \text{large})
  ]
  is **not known** in general. ([Erdős Problems][1])

* The possibility
  [
  E(N)=o(N^{1/2})
  ]
  is also **not ruled out** by current results, but **no such example is known** (at least as summarized in the standard references for this Erdős problem). ([Erdős Problems][1])

If you’d like, I can also sketch (without claiming a proof of either direction) why (\sqrt N) is the “natural barrier” heuristically: to get (\sim N) integers each with a unique representation you need (\sim N) usable pairs ({a,a'}), which forces (|A\cap[1,N]|) to be on the order of (\sqrt N), and then avoiding collisions looks like a near-extremal Sidon/quasi-Sidon packing problem—exactly the regime where (\sqrt N)-type error terms commonly appear.

[1]: https://www.erdosproblems.com/14 "
  
    Erdős Problem #14
  
"
