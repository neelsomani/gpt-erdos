For $r=2$ the answer is **yes** (and this is a theorem):

* A $2$-powerful number is the usual **powerful / square-full** number.
* Heath-Brown proved that **every sufficiently large integer is a sum of three powerful numbers** [[nomath]](i.e. “order $3=r+1$”)[[/nomath]]. ([Erdős Problems][1])
  This is exactly the $r=2$ case of your question.

Moreover, the known “exception list” for $r=2$ [[nomath]](integers **not** representable as a sum of $\le 3$ powerful numbers)[[/nomath]] is
[
7,15,23,87,111,119,
]
and there are no other known exceptions below (4\times 10^{7}); it is conjectured there are no further exceptions at all. ([OEIS][2])

---

For **general (r\ge 3)**, the question is **open**.

It is recorded as an Erdős–Ivić problem (Oberwolfach problem book) and appears as Erdős Problem #1107 in the Erdős Problems database, which currently lists the status as open for (r\ge 3). ([Erdős Problems][3])

What *is* known is mainly computational evidence. For example:

* For $r=3$ (the **cube-full** numbers), the OEIS records a list of integers not representable as a sum of (\le 4) cube-full numbers, with the **last known** exception (2039) and **no others below (84000)**. ([OEIS][4])
* For $r=4$, OEIS similarly lists currently known exceptions to being a sum of (\le 5) $4$-full numbers (based on computations in a finite range). ([OEIS][5])

None of this, however, constitutes a proof that the exception set is finite for (r\ge 3).

---

### Why $r+1$ is a natural threshold (context)

The $r$-powerful [[nomath]](a.k.a. $r$-full)[[/nomath]] numbers up to $x$ are very sparse [[nomath]](about $x^{1/r}$ in size heuristically)[[/nomath]], so needing more than $r$ summands is not surprising. There is also a closely related open problem asking about representation by only $r$ summands; even for $r=2$, sums of two square-full numbers form a set of density $0$ (Baker–Brüdern), so $r$ summands is “too few” in a strong sense. ([Erdős Problems][6])

---

So, in short:

* **$r=2$: yes** (Heath-Brown). ([Erdős Problems][1])
* **(r\ge 3): unknown** (Erdős–Ivić conjecture / Erdős Problem #1107). ([Erdős Problems][3])

[1]: https://www.erdosproblems.com/latex/941 "
  
    Erdős Problems
  
"
[2]: https://oeis.org/A056828 "A056828 - OEIS"
[3]: https://www.erdosproblems.com/forum/thread/1107 "

    Erdős Problem #1107 - Discussion thread

"
[4]: https://oeis.org/A392342 "A392342 - OEIS"
[5]: https://oeis.org/A392343 "A392343 - OEIS"
[6]: https://www.erdosproblems.com/latex/940 "
  
    Erdős Problems
  
"
