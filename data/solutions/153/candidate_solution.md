This exact question is (as far as I can find) **still open**.

It is stated as an open problem by Erdős–Sárközy–Sós (1994), and it is still listed as **OPEN** on the Erdős Problems site. ([Erdős Problems][1])

### What is known around it

Write (n=|A|). For a Sidon set [[nomath]](in the usual “all sums $a+b$ with $a\le b$ are distinct” sense)[[/nomath]], we have
[
t=|A+A|=\frac{n(n+1)}2.
]

People have proved some facts about **single large gaps** in $A+A$, and also given constructions where gaps are **not too large**:

* Erdős–Sárközy–Sós proved that for every finite Sidon set $A$, the **largest gap** in $A+A$ is at least a constant times (\log |A|). ([arXiv][2])
  (So the gaps do grow at least a bit.)

* They also constructed Sidon sets (A\subset[1,N]) whose sumset has **no gap longer than (3\sqrt N)** (so, in that model, the largest gap can be “not crazy large”). ([arXiv][2])

* Ruzsa (1996) improved several bounds/constructions: for Sidon sets (A\subset[1,N]) he gives constructions where the **maximal gap** can be as small as (\ll N^{1/3}), and even (O(\log N)) on a long subinterval of length (cN). ([EuDML][3])

These results are about **extreme gaps** (largest gap, or gaps in a long region). They do **not** decide the question you asked, which is about the **average of the squares of all gaps**.

### Why your question is hard (in simple terms)

If you look at “dense” Sidon sets (A\subset[1,N]) with (|A|\approx \sqrt N), then (A+A\subset[2,2N]) has about (N/2) elements. So the **mean gap** in $A+A$ is only a constant (around 4).

Your expression
[
\frac{1}{t}\sum_{i=1}^{t-1}(s_{i+1}-s_i)^2
]
goes to infinity only if the gaps have a very “heavy tail”: **rare but very large gaps** that push the *second moment* up, even though the *average* gap stays bounded.

No general method is known (at least in the cited sources) to force that second moment to blow up for *every* large Sidon set. That is exactly why it remains open. ([Erdős Problems][1])

### Small extra note

The same Erdős–Sárközy–Sós paper also asks a related open question: whether the number of “length one” gaps [[nomath]](i.e. $s_{i+1}-s_i=1$)[[/nomath]] must go to infinity with (|A|). ([arXiv][2])
So even understanding how many *tiny* gaps must appear is also not settled in general.

If you want, I can also show how your quantity behaves on some standard explicit Sidon constructions (Erdős–Turán type, Singer/Bose–Chowla type) as numerical evidence. That will not prove the statement, but it can give a feel for whether the average square gap seems to grow and how fast.

[1]: https://www.erdosproblems.com/153 "
  
    Erdős Problem #153
  
"
[2]: https://arxiv.org/pdf/math/0407117 "https://arxiv.org/pdf/math/0407117"
[3]: https://eudml.org/doc/206924 "https://eudml.org/doc/206924"
