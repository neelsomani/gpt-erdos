As of **January 2026**, this is **not known**. In fact, with the conditions exactly as you stated (the (I_i) are **distinct**, **pairwise disjoint**, and **not adjacent**, and each has (|I_i|\ge 2)), it is recorded as an **open Erdős–Graham problem** (Erdős Problem #289). ([Erdős Problems][1])

A bit of context:

* Erdős and Graham posed a closely related question in their 1980 problem collection, but (apparently) **without** explicitly requiring the intervals to be distinct/non-overlapping/non-adjacent. Under that *weaker* interpretation (allowing overlaps/repetitions), Vjekoslav Kovač gave a **simple affirmative argument** that one can achieve such representations for all sufficiently large $k$. ([Erdős Problems][2])
* However, Kovač also notes that this “easy” method does **not** really address the **non-overlapping / distinct** version, which is the nontrivial one and is what is now listed as #289. ([Erdős Problems][2])

What *is* known in the same spirit is that **integers other than 1** can be represented this way: for example, Hickerson and Montgomery exhibited a representation of **2** as a sum of reciprocals over **five** disjoint, non-adjacent intervals:
[
I_1=[2,7],\ I_2=[9,10],\ I_3=[17,18],\ I_4=[34,35],\ I_5=[84,85],
]
so that (2=\sum_{i=1}^5\sum_{n\in I_i} \frac1n). ([Erdős Problems][1])

Finally, to give a sense of difficulty: even the related question of whether there are only **finitely many pairs** of intervals (I_1,I_2) whose reciprocal sums add to an integer is itself listed as **open** (Erdős Problem #288). ([Erdős Problems][3])

[1]: https://www.erdosproblems.com/289 "
  
    Erdős Problem #289
  
"
[2]: https://www.erdosproblems.com/forum/thread/289 "

    Erdős Problem #289 - Discussion thread

"
[3]: https://www.erdosproblems.com/288 "
  
    Erdős Problem #288
  
"
