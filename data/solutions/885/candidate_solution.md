This is **open in general**.

The statement you wrote is **Erdős problem #885** (in the formulation used on the Erdős Problems site), and what is currently known is:

* It is **true for $k=1$** (trivial).
* It is **true for $k=2$** (Erdős–Rosenfeld).
* It is **true for $k=3$** (Jiménez‑Urroz).
* It is **true for $k=4$** (Bremner).
* For **arbitrary $k$**, it is **not known** (as of the current literature summary). ([Erdős Problems][1])

### Small explicit examples

* $k=2$: take (N_1=8), (N_2=120).

  * (D(8)={|1-8|,|2-4|}={7,2}).
  * (120=8\cdot 15) gives difference $7$, and (120=10\cdot 12) gives difference $2$.
  * Hence (D(8)\cap D(120)\supseteq{2,7}), so (|D(8)\cap D(120)|\ge 2).

* $k=3$: one concrete triple is
  [
  (N_1,N_2,N_3)=(1040,2660,5520).
  ]
  Each of these has factor pairs with differences $32,67,256$:

  * (1040=20\cdot 52) [[nomath]](diff $32$)[[/nomath]], (13\cdot 80) [[nomath]](diff $67$)[[/nomath]], (4\cdot 260) [[nomath]](diff $256$)[[/nomath]].
  * (2660=38\cdot 70) [[nomath]](diff $32$)[[/nomath]], (28\cdot 95) [[nomath]](diff $67$)[[/nomath]], (10\cdot 266) [[nomath]](diff $256$)[[/nomath]].
  * (5520=60\cdot 92) [[nomath]](diff $32$)[[/nomath]], (48\cdot 115) [[nomath]](diff $67$)[[/nomath]], (20\cdot 276) [[nomath]](diff $256$)[[/nomath]].

  So (D(1040)\cap D(2660)\cap D(5520)\supseteq{32,67,256}), hence the intersection has size at least $3$.

### Status

So the answer to “**Is it true for every (k\ge 1)?**” is:

* **Known true for (k\le 4)**.
* **Open for general $k$**. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/885 "
  
    Erdős Problem #885
  
"
