Let (n_k=p_k#=\prod_{i\le k}p_i). Since (2\mid n_k), every (a_i) is odd, hence every gap
[
g_i:=a_{i+1}-a_i
]
is even.

It is convenient to package this in the standard “Jacobsthal/primorial” notation. Let $D(k)$ be the set of differences between consecutive integers coprime to (p_k#). Ziller shows that the **maximum** such difference is exactly the primorial Jacobsthal value $h(k)$ [[nomath]](in his convention $h(k)=N_{\max}(k)$, the largest gap)[[/nomath]]. 

## 1) Smallest even integer not of the form (a_{i+1}-a_i)

Define (as in Ziller) (N_{\min}(k)) to be the largest even number such that **every** even (2,4,\dots,N_{\min}(k)) occurs as a difference of consecutive coprimes to (p_k#). Then the “first missing even gap” is
[
m_k = N_{\min}(k)+2.
]
Ziller proves in particular the unconditional bounds
[
2k \le N_{\min}(k)\le h(k),
]
hence
[
2k+2 \le m_k \le h(k)+2.
]
The lower bound (2k\le N_{\min}(k)) comes from a constructive existence/pro-pagation argument for restricted coverings [[nomath]](it implies $2,4,\dots,2k\in D(k)$)[[/nomath]]. 

So, up to this point the clean “estimate” is:
[
m_k = N_{\min}(k)+2 \quad\text{with}\quad 2k+2 \le m_k \le h(k)+2.
]

### What is the size of $h(k)$ [[nomath]](hence the natural scale for $m_k$)[[/nomath]]?

Hagedorn summarizes the best-known general upper bound (due to Iwaniec) as (j(n)\ll (\log n)^2), and for primorials (h(k)=j(p_k#)) this gives (h(k)\ll (\log(p_k#))^2\asymp p_k^2), equivalently (h(k)\ll k^2\log^2 k). 
On the lower side, Hagedorn also records a sieve-based bound of Pintz implying $h(k)$ grows faster than linear in (p_k) [[nomath]](roughly $p_k\log p_k$ times very slowly varying factors)[[/nomath]], and the elementary CRT bound (h(k)\ge 2p_{k-1}). 

So, the *a priori* asymptotic information you can safely state is that the relevant scale $h(k)$ [[nomath]](hence $m_k$)[[/nomath]] lies between about (p_k\log p_k) (up to iterated-log factors) and (p_k^2), and (m_k) is at most $h(k)+2$. 

### What happens in practice (computational evidence)?

Ziller computed (N_{\min}(k)) and all missing even differences below $h(k)$ for (k\le 44). The striking pattern is:

* **For many $k$** there are *no* missing even gaps below $h(k)$, i.e. (N_{\min}(k)=h(k)) and therefore
  [
  m_k = h(k)+2.
  ]
* When missing gaps exist, they appear to be **few and very near the top** [[nomath]](near $h(k)$)[[/nomath]].

For example from his Table 1:

* $k=6$ ((p_k=13)): (N_{\min}(6)=18), missing (20), and (h(6)=22), so (m_6=20). 
* $k=8$ ((p_k=19)): (N_{\min}(8)=30), missing (32), (h(8)=34), so (m_8=32). 
* $k=14$ ((p_k=43)): (N_{\min}(14)=84), missing (86,88), (h(14)=90), so (m_{14}=86). 

He also formulates the conjecture [[nomath]](supported by all computed data up to $k=44$)[[/nomath]] that
[
h(k-1)\le N_{\min}(k)\quad (k>1),
]
i.e. at least all even gaps up to the *previous* Jacobsthal value always occur. 

**Bottom line (best current “estimate”):** the first missing even gap (m_k) appears to be of size (\asymp h(k)), and very often equals (h(k)+2); rigorously one always has (2k+2\le m_k\le h(k)+2), with $h(k)$ between (\gg p_k) and (\ll p_k^2) (more precisely as in Hagedorn’s bounds). 

## 2) Are there (\gg \max_i(a_{i+1}-a_i)) many even integers that *do* occur as gaps?

Let
[
M_k:=\max_i(a_{i+1}-a_i)=h(k)
]
(the maximum gap). 

Now interpret “how many even integers of the form (a_{j+1}-a_j)” in the natural (nontrivial) way: **how many distinct even values occur among the gaps**.

* Trivially, the number of distinct even gap sizes is (\le M_k/2) [[nomath]](since only even numbers $\le M_k$ can occur)[[/nomath]].
* By definition of (N_{\min}(k)), you always have at least (N_{\min}(k)/2) **distinct** even gaps [[nomath]](namely $2,4,\dots,N_{\min}(k)$)[[/nomath]]. 

So the question becomes: is (N_{\min}(k)) typically comparable to (M_k)?

* **Unconditionally**, we only know (N_{\min}(k)\ge 2k), hence at least $k$ distinct gap sizes (2,4,\dots,2k). This is usually *much* smaller than (M_k). 
* **Empirically**, Ziller’s computations show that for many (k\le 44) one has (N_{\min}(k)=M_k), meaning *every* even number up to the maximum gap occurs. In those cases the number of distinct even gaps is exactly (M_k/2), which is (\asymp M_k) and in particular (\gg M_k) in the usual Vinogradov sense (up to a constant factor). 
* **Conditionally (conjecturally)**, if Conjecture 4.1 (h(k-1)\le N_{\min}(k)) holds, then the number of distinct even gap sizes is at least (h(k-1)/2). Since $h(k)$ and $h(k-1)$ are of the same general magnitude in computed ranges, this again suggests (|\\{\text{distinct gaps}\\}|\asymp M_k). 

So the honest answer is:

* With **current proofs**: we can guarantee only (\ge k) distinct even gap sizes, not (\gg M_k) in general. 
* With **current computations/heuristics**: it seems very plausible that there are (\asymp M_k) distinct even gap sizes—indeed often **all** even sizes (\le M_k) occur. 

*[[nomath]](If instead you meant “counting multiplicity”, i.e. how many indices $j$ give some even gap, then that count is $\phi(n_k)-1$, which is astronomically larger than $M_k$; but that interpretation makes the second question essentially trivial.)[[/nomath]]*
