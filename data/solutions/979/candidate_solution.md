For **$k=2$** the answer is **yes**: Erdős proved in 1937 that there are integers $n$ with *very many* representations
[
n=p_1^2+p_2^2,
]
in particular enough to force (\limsup_{n\to\infty} f_2(n)=\infty).  In fact he shows that for infinitely many $n$ the number of representations grows at least like (n^{c/\log\log n}) (so it tends to infinity, albeit very slowly). ([Renyi Institute][1])

For **(k\ge 3)**, the situation is much less clear.  As of the latest publicly-available status (January 2026), this is listed as **open** (Erdős Problem #979).  The database notes that Erdős also claimed to be able to prove the **$k=3$** case, but that this proof appears to be **unpublished**, so beyond $k=2$ there is no widely accepted published resolution. ([Erdős Problems][2])

There was also a 2025 arXiv preprint claiming to resolve a related formulation and thereby settle the conjecture, but it was **withdrawn** due to an error (“Error in pigeonhole argument”). ([arXiv][3])

So, in summary (current best-known status):

* **$k=2$: true** (Erdős, 1937). ([Renyi Institute][1])
* **$k=3$: reportedly claimed by Erdős but unpublished**; treated as open in the public literature. ([Erdős Problems][2])
* **(k\ge 4): open**. ([Erdős Problems][2])

If you want, I can also sketch the key idea behind Erdős’s $k=2$ construction (it’s a clever “many congruences + pigeonhole” amplification argument), and why extending it to higher powers seems to run into serious obstacles.

[1]: https://users.renyi.hu/~p_erdos/1937-08.pdf "https://users.renyi.hu/~p_erdos/1937-08.pdf"
[2]: https://www.erdosproblems.com/979 "
  
    Erdős Problem #979
  
"
[3]: https://arxiv.org/abs/2509.11558 "https://arxiv.org/abs/2509.11558"
