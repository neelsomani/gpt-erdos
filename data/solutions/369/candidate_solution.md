Yes (in the literal reading of your statement), and for a completely simple reason.

If (m \le n^\epsilon), then $m$ is automatically (n^\epsilon)-smooth, because every prime divisor of $m$ is (\le m \le n^\epsilon).

Now fix (k\ge 2). If $n$ is large enough that

* (n \ge k) [[nomath]](so that $1,2,\dots,k\in{1,\dots,n}$)[[/nomath]], and
* (n^\epsilon \ge k),

then the block
[
1,2,\dots,k
]
is a sequence of $k$ consecutive integers in ({1,\dots,n}), and each term is (\le k \le n^\epsilon), hence each is (n^\epsilon)-smooth.

So taking, for instance,
[
N_0 := \max\bigl(k,\ \lceil k^{1/\epsilon}\rceil\bigr),
]
we have that for every (n\ge N_0) such a block exists.

---

If instead you meant something like “$k$ consecutive integers **near $n$** [[nomath]](e.g. in $[n/2,n]$)[[/nomath]] all (n^\epsilon)-smooth,” that becomes a much more delicate distribution-in-short-intervals question; but as written, the answer is a straightforward “yes” via the initial segment (1,\dots,k).
