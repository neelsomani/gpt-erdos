Not known in general — this is a classical open problem of Erdős–Sárközy–Sós.

Let (m(N)) denote the **minimum** possible size of a **maximal (by inclusion)** Sidon set (A\subseteq [N]:={1,\dots,N}). Problem 15 in Erdős–Sárközy–Sós (1994) asks exactly whether (m(N)=O(N^{1/3})). ([Academy's Library Repository][1])

What is known is that (m(N)) is pinned down up to a ((\log N)^{1/3}) factor:

### Lower bound: every maximal Sidon set has (\Omega(N^{1/3})) elements

Sketch (standard “coverage” argument). If (A\subseteq[N]) is Sidon and **maximal**, then for every (x\in [N]\setminus A), adding (x) must create a nontrivial additive collision. Under the usual Sidon definition (all sums (a+b) with (a\le b) are distinct), that means either

* (x+a=b+c) for some (a,b,c\in A) (allowing (b=c)), i.e. (x\in (A+A-A)), or
* (2x=a+b) for some (a,b\in A), i.e. (x\in (A+A)/2).

Hence
[
[N]\subseteq A \ \cup\ (A+A-A)\ \cup\ (A+A)/2.
]
Crude counting gives (|A+A-A|\le |A|^3) and (|(A+A)/2|\le |A|^2), so
[
N \le |A| + |A|^2 + |A|^3 \ll |A|^3,
]
and therefore (|A|\gg N^{1/3}).

So (m(N)\ge c,N^{1/3}) for an absolute constant (c>0).

### Upper bound: Ruzsa’s construction gives (m(N)\ll (N\log N)^{1/3})

Imre Z. Ruzsa constructed a maximal Sidon set (A\subseteq [N]) with
[
|A| \ll (N\log N)^{1/3}.
]
This is the best general upper bound currently on the “smallest maximal Sidon set” problem. ([Springer][2])

### What remains open

The open gap is exactly whether the ((\log N)^{1/3}) can be removed, i.e. whether one can always achieve
[
m(N)=O(N^{1/3}).
]
This is listed as open (Erdős Problem #156) with precisely the bounds above. ([Erdős Problems][3])

So, the current state is:
[
\boxed{c,N^{1/3}\ \le\ m(N)\ \le\ C,(N\log N)^{1/3},}
]
and it is **unknown** whether (m(N)=O(N^{1/3})).

[1]: https://real.mtak.hu/110603/1/1-s2.0-0012365X9400108U-main.pdf "PII: 0012-365X(94)00108-U"
[2]: https://link.springer.com/article/10.1023/A%3A1009757824153?utm_source=chatgpt.com "A Small Maximal Sidon Set | The Ramanujan Journal"
[3]: https://www.erdosproblems.com/156 "
  
    Erdős Problem #156
  
"
