Write
[
r_A(n):=(1_A*1_A)(n)=\sum_{k=0}^n 1_A(k),1_A(n-k),
]
so (r_A(n)) is the **number of ordered representations** (n=a+b) with (a,b\in A) (up to an $O(1)$ difference from the unordered version).

As of **January 2026**, the existence of (A\subseteq\mathbb N) for which
[
\lim_{n\to\infty}\frac{r_A(n)}{\log n}
]
exists and is nonzero is **open** (it’s listed as Erdős Problem #66, prize $500). ([Erdős Problems][1])

What *is* known around this:

* **“Almost everywhere” via random sets:** A suitably constructed random set can make (r_A(n)) behave like a constant multiple of (\log n) **for all $n$** outside an exceptional set of **density $0$**, but removing the exceptional set entirely (i.e. getting the limit for *every* large $n$) is exactly the hard part. ([Erdős Problems][1])

* **You can hit the (\log n) scale, but not rigidly:** There exist “economical” additive bases $A$ with (r_A(n)\asymp \log n) (two-sided bounds up to constants), e.g. by the Erdős–Tetali theorem (existence). ([Wikipedia][2])
  This shows (\log n) is the right “borderline” order of growth, but it does **not** give a pointwise limit (r_A(n)/\log n\to c).

* **Regularity obstructions (but not strong enough to settle the limit question):**

  * Erdős and Sárközy proved you **cannot** have
    [
    \frac{|r_A(n)-\log n|}{\sqrt{\log n}}\to 0,
    ]
    i.e. $r_A(n)$ cannot track (\log n) to within (o(\sqrt{\log n})). ([Erdős Problems][1])
  * Horváth strengthened this kind of statement: for any fixed (\varepsilon>0),
    [
    |r_A(n)-\log n|\le (1-\varepsilon)\sqrt{\log n}
    ]
    cannot hold for all sufficiently large $n$. ([akjournals.com][3])

  These results still leave plenty of room for a limit (r_A(n)/\log n\to c), because that would only force an error (o(\log n)), which is much weaker than (o(\sqrt{\log n})).

* **Erdős’s belief/conjectural picture:** Erdős apparently believed the answer should be **no**, and even suggested a stronger phenomenon: for every $A$, the (\liminf) and (\limsup) of (r_A(n)/\log n) might always be separated by an absolute constant (which would rule out existence of a limit altogether). ([Erdős Problems][1])

So the current state is: **no example is known and no impossibility proof is known**; it’s an open problem. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/66 "
  
    Erdős Problem #66
  
"
[2]: https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Tetali_theorem?utm_source=chatgpt.com "Erdős–Tetali theorem"
[3]: https://akjournals.com/view/journals/606/2/Supplement-1/article-p155.pdf?utm_source=chatgpt.com "An improvement of a theorem of Erd&#x0151;s and S&#x00E1"
