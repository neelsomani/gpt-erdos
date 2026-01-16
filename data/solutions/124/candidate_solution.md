### First question (the case (k=0))

Yes. In fact, under a *weaker* condition than the one you wrote, you can represent **every** integer (n\ge 0) (not just “sufficiently large” ones).

The usual condition is
[
\sum_{i=1}^r \frac{1}{d_i-1}\ \ge\ 1.
]
Your condition
[
\sum_{i=1}^r \frac{1}{d_r-1}=\frac{r}{d_r-1}\ge 1
]
is stronger, because (d_i\le d_r) implies (\frac1{d_i-1}\ge \frac1{d_r-1}), hence
[
\sum_{i=1}^r \frac{1}{d_i-1}\ \ge\ \sum_{i=1}^r \frac{1}{d_r-1}\ \ge\ 1.
]

#### Why this gives a representation (simple proof idea)

Make one big (multi)set of “coins” consisting of **all** powers of the (d_i):
[
{d_i^j : i=1,\dots,r,\ j\ge 0},
]
and sort them in nondecreasing order to get a sequence
[
a_1\le a_2\le a_3\le \cdots
]
(with repeats allowed, e.g. (1=d_1^0=d_2^0=\cdots)).

Now, a subset-sum (\sum \varepsilon_n a_n) with (\varepsilon_n\in{0,1}) is exactly the same thing as choosing, for each (i), some distinct powers of (d_i) and adding them up. Group the chosen powers base-by-base: the part coming from base (d_i) is some (A_i\in P(d_i,0)). So we get
[
n=\sum_{i=1}^r A_i,
]
which is your desired shape (you can set (c_i=1) and allow (A_i=0) if you want “not used”).

The key “no gaps” tool is a standard lemma (often called **Brown’s criterion**): if (a_1=1) and for every (n),
[
a_{n+1}\le 1+\sum_{m=1}^n a_m,
]
then **every** integer is a subset-sum of the (a_m).

So we just prove that inequality. Fix (n). For each base (d_i), let (e_i) be the first exponent whose power (d_i^{e_i}) has **not** yet appeared among (a_1,\dots,a_n). Then among the first (n) terms, we definitely have (1,d_i,d_i^2,\dots,d_i^{e_i-1}) from that base, so the contribution to (\sum_{m\le n} a_m) from base (i) is
[
1+d_i+\cdots+d_i^{e_i-1}=\frac{d_i^{e_i}-1}{d_i-1}.
]
Also, by definition,
[
a_{n+1}=\min_i d_i^{e_i}.
]

Now estimate:
[
\sum_{m=1}^n a_m
=\sum_{i=1}^r \frac{d_i^{e_i}-1}{d_i-1}
\ \ge\ \Big(\min_i (d_i^{e_i}-1)\Big)\ \sum_{i=1}^r \frac{1}{d_i-1}.
]
If (\sum_i \frac1{d_i-1}\ge 1), this is (\ge \min_i(d_i^{e_i}-1)=a_{n+1}-1). So
[
a_{n+1}\le 1+\sum_{m=1}^n a_m,
]
and Brown’s criterion applies.

This exact argument (and even a Lean formalization) is recorded on the Erdős Problems forum thread for Problem #124. ([Erdős Problems][1])

So the answer to your first question is **yes** (and stronger: all integers, not just large ones), under your hypothesis.

---

### Second question (the case (k\ge 1) plus (\gcd(d_1,\dots,d_r)=1))

This is the genuinely hard part. As of the latest public updates I can find (the Erdős Problems site was last edited Dec 1, 2025), the general statement is **still open**.

* It was **conjectured** by Burr–Erdős–Graham–Li in their 1996 paper, and they proved it in at least one important special case, namely ({3,4,7}). ([Erdős Problems][1])
* In that ({3,4,7}), (k=1) case, they even state a specific largest exception (581) using Diophantine approximation bounds. ([MathOverflow][2])
* The modern discussion around Problem #124 also stresses that the “(k=0)” version (which allows the (1=d_i^0) term) has a short proof, but the “remove the (1), add gcd condition” version is the one that remains open. ([Erdős Problems][1])

Intuitively, why is (k\ge 1) harder? Because you removed all the tiny building blocks (especially “1”), so the easy “no gaps” induction does not start automatically. The extra (\gcd(d_1,\dots,d_r)=1) condition is clearly necessary (otherwise everything is stuck in a fixed congruence class), but it does not by itself give the kind of step-by-step interval filling that the (k=0) proof uses.

So, in short:

* **First question:** yes (even “all integers”), and there is now a clean proof via a subset-sum/no-gaps argument. ([Erdős Problems][1])
* **Second question:** still open in general; known in special cases such as ({3,4,7}). ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/forum/thread/124 "https://www.erdosproblems.com/forum/thread/124"
[2]: https://mathoverflow.net/questions/501259/sums-of-distinct-powers-of-3-4-and-7 "nt.number theory - Sums of distinct powers of 3, 4 and 7 - MathOverflow"
