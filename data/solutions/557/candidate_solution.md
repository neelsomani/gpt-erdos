Not known in general — it is a classical **open problem of Erdős and Graham**.

What *is* known [[nomath]](for fixed $k$, with $n\to\infty$)[[/nomath]]:

* **Best general upper bound (all trees):** Erdős–Graham proved that for a tree (T_n) on $n$ **edges**,
  [
  r(T_n;k)<2kn+1,
  ]
  hence for a tree $T$ on $n$ **vertices** [[nomath]](so $n-1$ edges)[[/nomath]],
  [
  R(T;k)\le 2k(n-1)+1=2kn-O(k).
  ]


* **The conjectured $kn+O(1)$ would follow from Erdős–Sós:** Erdős–Graham explicitly note that if the Erdős–Sós extremal conjecture “every graph with average degree (>n-2) contains every $n$-vertex tree” were known, then their $2k$ factor could be improved to
  [
  r(T_n;k) < kn+O(1),
  ]
  i.e. $R(T;k)\le kn+O(1)$ in your notation. 
  [[nomath]](This implication is also recorded in the Erdős problems database: problem #548 $\Rightarrow$ #557.)[[/nomath]] ([Erdős Problems][1])

* **Sharpness of the coefficient $k$:** for stars (S_n=K_{1,n-1}) one has an *exact* formula (Burr–Roberts) showing
  [
  R(K_{1,n-1};k)=k(n-2)+1 \text{ or } k(n-2)+2
  ]
  depending on parity, so $R(T;k)$ can be as large as $kn-O(k)$. ([kam.mff.cuni.cz][2])
  This is why the conjectured leading term $kn$ is essentially best possible.

* **Status:** the statement you wrote is listed as **OPEN** (Erdős–Graham, “On partition theorems for finite graphs”, 1975). ([Erdős Problems][3])

So the current picture is:
[
kn-O(k)\ \lesssim\ R(T;k)\ \le\ 2kn-O(k),
]
and improving the constant factor $2$ down to $1$ uniformly for **all** trees is open (and would follow from Erdős–Sós).

[1]: https://www.erdosproblems.com/548 "
  
    Erdős Problem #548
  
"
[2]: https://kam.mff.cuni.cz/~balko/prezentace/Ramsey_numbers_of_ordered_graphs.pdf "Ramsey numbers of ordered graphs"
[3]: https://www.erdosproblems.com/forum/thread/557 "

    Erdős Problem #557 - Discussion thread

"
