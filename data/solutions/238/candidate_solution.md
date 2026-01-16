Write the primes as (p_1<p_2<\cdots) and gaps (d_n:=p_{n+1}-p_n).
For a *block of consecutive primes* (p_m,p_{m+1},\dots,p_{m+r}), the condition

> “the difference between any two is (>c_2)”

is equivalent to requiring the **adjacent gaps** in the block satisfy
[
p_{m+i+1}-p_{m+i}>c_2\quad (i=0,1,\dots,r-1),
]
since any non-adjacent difference is a sum of adjacent gaps.

### What is known unconditionally

The full statement “for **every** (c_1,c_2>0)” is not known, but Erdős proved a weaker form:

* For every fixed (c_2>0), there **exists** a constant (c_1=c_1(c_2)>0) such that for all sufficiently large $x$ one can find (\asymp c_1\log x) consecutive primes (\le x) with all adjacent gaps (>c_2). This appears as Theorem 3 in Erdős’ 1949 paper [[nomath]](he proves existence of $\lfloor c_1\log n\rfloor$ consecutive primes $<n$ with each successive difference $>!q$, where $q$ is your $c_2$). ([Renyi Users][1])

A standard way to think about why such a “small $c_1$” result is accessible is:

* By Brun-type sieve bounds, the number of “close prime pairs” (p,p+h\le x) for any fixed $h$ is (O(x/(\log x)^2)); for instance Brun proved (\pi_2(x):=#{p\le x:\ p,p+2\ \text{prime}}\ll x/(\log x)^2). ([Pollack][2])
* Summing this for (1\le h\le \lfloor c_2\rfloor) shows there are only (O_{c_2}(x/(\log x)^2)) gaps (\le c_2) up to $x$, while there are (\asymp x/\log x) total gaps.
* Pigeonhole then forces at least one run of consecutive gaps all (>c_2) of length (\gg_{c_2}\log x), i.e. a block of (\gg_{c_2}\log x) consecutive primes with all gaps (>c_2). This is the sense in which one gets the conclusion for (c_1) “sufficiently small depending on (c_2)”.

So: **yes** if (c_1) is small enough as a function of (c_2) (Erdős’ theorem), but that does **not** cover arbitrary (c_1).

### Status of the full question

For **arbitrary** (c_1>0) [[nomath]](with fixed $c_2>0$)[[/nomath]], the statement is currently **open** as far as the current literature-summary sources indicate; it is listed as an open Erdős problem (#238). ([Erdős Problems][3])

Heuristically, most probabilistic/Hardy–Littlewood style models would predict the answer should be **yes** (indeed with much longer runs than (c_1\log x)), but proving it seems to require very uniform control on prime (k)-tuple statistics in short intervals. A conditional route along these lines is described in the discussion of the same Erdős problem. ([Erdős Problems][3])

### Bottom line

* **Unconditionally:** you can guarantee blocks of length (\gg_{c_2}\log x), so the claim holds for (c_1) small enough depending on (c_2). ([Renyi Users][1])
* **For general (c_1,c_2>0) as stated:** **open** (no known unconditional proof or disproof). ([Erdős Problems][3])

[1]: https://users.renyi.hu/~p_erdos/1949-05.pdf "https://users.renyi.hu/~p_erdos/1949-05.pdf"
[2]: https://pollack.uga.edu/gaps2014.pdf "https://pollack.uga.edu/gaps2014.pdf"
[3]: https://www.erdosproblems.com/forum/thread/238 "https://www.erdosproblems.com/forum/thread/238"
