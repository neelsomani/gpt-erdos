This is a long‑standing **open problem** in additive/combinatorial number theory.

Your construction is the standard “greedy” way to build a set (S={a_1<a_2<\cdots}) in which each new term is **not** a sum of two earlier terms. When the initial data are (eventually) sum‑free, the resulting infinite set is “complete”/“ultimately complete” in the sense that every sufficiently large integer is either in $S$ or in $S+S$; in fact Calkin–Erdős note that “complete iff constructed greedily from a finite set.” ([Clemson Mathematics][1])

### What “eventually periodic differences” would mean

If the first differences (d_n=a_{n+1}-a_n) are ultimately periodic, then from some point on the sequence is a finite union of arithmetic progressions [[nomath]](equivalently the **indicator function** $1_S(n)$ is ultimately periodic modulo some period)[[/nomath]]. This is exactly the “regularity/ultimate periodicity” notion used in the literature on greedy sum‑free (a.k.a. “0‑additive”) sequences. 

### Current status: unknown in general

The question “Are the differences (a_{n+1}-a_n) ultimately periodic for every finite starting set?” is explicitly described as still open in modern references: Bosma–Fokkink–Kaliszyk et al. (JIS, 2025) say that for (s=0) (the 2‑sumfree / 0‑additive / greedy sum‑free case) “it remains an open question if such sequences are always ultimately periodic,” i.e. whether the first differences are ultimately periodic. 

### Evidence pointing *against* a universal “yes”

Although many initial sets empirically lead to eventual periodicity, there is substantial computational evidence suggesting that a universal theorem “yes, always” is likely false:

* Calkin–Finch (1996) computed many greedy/complete sum‑free sets and list **apparently aperiodic** examples “checked up to (10^7),” including bases $\\{8,18,30\\},\\{8,27,32\\},\\{9,16,29\\},\\{9,26,32\\}$, and they also emphasize that while evidence suggests aperiodicity, there was (and still is) no general method to prove it. ([EMIS][2])
* Calkin–Erdős (1996) discuss Dickson’s question [[nomath]](greedy from a finite initial set $\Rightarrow$ ultimately periodic?)[[/nomath]] and remark that particular greedy sum‑free sets such as $\\{1,3,8,20,26,\dots\\}$ and $\\{2,15,16,23,27,\dots\\}$ were **not known** to be ultimately periodic. ([Clemson Mathematics][1])
* A later exposition (SURIM 2019) reiterates that the conjecture “all greedy sum‑free sequences are regular” is still open but “likely false,” again citing the same bases that do not appear periodic up to (10^7). 

### What *is* known (partial positive results)

There are variants where eventual periodicity *is* provable. For example, in the “finite‑greedy” variant [[nomath]](you only forbid sums where at least one summand is among the first $L$ terms)[[/nomath]], Calkin–Finch proved **all such sequences are regular** via a pigeonhole/block argument. 
This does **not** settle the full greedy case (L=\infty) you asked about, but it explains why periodicity shows up so often.

---

So, to answer your question as of the current literature: **it is not known in general whether ((a_{m+1}-a_m)) must be eventually periodic**, and there is strong computational evidence that the answer might be **no**, but no proof either way is known. 

[1]: https://www.math.clemson.edu/~calkin/Papers/calkin_erdos.pdf "https://www.math.clemson.edu/~calkin/Papers/calkin_erdos.pdf"
[2]: https://emis.de/ft/51959 "calkin.dvi"
