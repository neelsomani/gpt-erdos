This is **open**.

It is an old question of **Erdős and Selfridge** (1967) and is listed as **Erdős Problem #889** and as **Problem B27** in Guy’s *Unsolved Problems in Number Theory*. ([Erdős Problems][1])

What *is* known is extremely modest: Erdős–Selfridge could only prove a uniform lower bound
[
v_0(n)\ge 2 \quad\text{for all } n\ge 17,
]
equivalently (v_0(n)>1) for all $n$ except (n\in{1,2,3,4,7,8,16}) [[nomath]](and also $0$ if one allows it)[[/nomath]]. ([Erdős Problems][1])

Moreover, they conjectured the stronger family
[
v_\ell(n):=\max_{k\ge \ell} v(n,k)\to\infty\quad (n\to\infty)\ \text{for each fixed }\ell,
]
but (already in 1967) they **could not even prove** the next step (v_1(n)\ge 2) for all sufficiently large $n$. ([Erdős Problems][1])

A couple of useful “sanity checks” around your question:

* The statement is **trivially true along subsequences**: since (v_0(n)\ge v(n,0)=\omega(n)) (number of distinct prime factors), taking $n$ to be a product of many distinct primes makes (v_0(n)) arbitrarily large. So (\limsup_{n\to\infty} v_0(n)=\infty) is easy; the difficulty is the **full limit** for *every* large $n$. ([GitHub][2])
* It is also true for **“almost all”** $n$ (in natural density), again because (v_0(n)\ge \omega(n)) and (\omega(n)) has normal order (\log\log n) (Hardy–Ramanujan / Erdős–Kac). But this does not address the hard cases [[nomath]](e.g. $n$ prime, near prime powers, etc.)[[/nomath]], which is exactly what the limit question must control. ([Wikipedia][3])

So the current state of affairs is: **expected to be true, but far beyond what we can prove**, with only the uniform bound (v_0(n)\ge 2) known for all large $n$. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/latex/889 "
  
    Erdős Problems
  
"
[2]: https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/ErdosProblems/889.lean "raw.githubusercontent.com"
[3]: https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Kac_theorem?utm_source=chatgpt.com "Erdős–Kac theorem"
