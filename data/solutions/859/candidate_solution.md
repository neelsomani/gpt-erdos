As far as I can find in the literature, this is **open**.

Let
[
A_t:={n\in\mathbb N:\ t\text{ is a sum of distinct divisors of }n},
\qquad
d_t:=\lim_{x\to\infty}\frac{|A_t\cap[1,x]|}{x}.
]
Erdős proved that **the natural density (d_t) exists for each fixed $t$** [[nomath]](in particular, $A_t$ is “eventually periodic” in a strong sense: every $n\in A_t$ is a multiple of some element of $A_t$ not exceeding $t!$)[[/nomath]]. ([Scribd][1])

He also proved that (d_t\to 0) and gave explicit **logarithmic power bounds**. In the notation of his paper, after splitting (A_t) into two classes and estimating each, he obtains an upper bound of order (1/\log t) and a lower bound of order (1/(\log t)^2): for all sufficiently large $t$,
[
d_t \ll \frac{1}{\log t}
\qquad\text{and}\qquad
d_t \gg \frac{1}{(\log t)^2}.
]
More concretely, he states that the relevant class has density (\le 2/\log t), hence (d_t\to 0) and “in fact (d_t<1/(\log t)^1)” for $t$ large, and also that one can prove (d_t>1/(\log t)^2) for $t$ large. ([Scribd][1])

Erdős then explicitly floated the possibility of a more precise asymptotic of the type you ask about [[nomath]](he writes “Perhaps …” and proposes a specific $\sim$-type behaviour)[[/nomath]], but does not prove it. ([Scribd][1])

So, at present, what is known is essentially:

* (d_t) exists for each $t$. ([Scribd][1])
* (d_t\to 0) as (t\to\infty). ([Scribd][1])
* There are absolute exponents (c_3,c_4>0) [[nomath]](indeed Erdős gives $1$ and $2$ in the displayed bounds above)[[/nomath]] with
  [
  \frac{1}{(\log t)^{c_3}} \ll d_t \ll \frac{1}{(\log t)^{c_4}}.
  ]
  ([Scribd][1])

But the **existence of constants (c_1,c_2>0) with**
[
d_t \sim \frac{c_1}{(\log t)^{c_2}}
\quad(t\to\infty)
]
is not established.

(For an “at a glance” status: this question is listed as open on the Erdős Problems site.) ([Erdős Problems][2])

[1]: https://www.scribd.com/document/698594400/1970-21ERDOS "1970 21erdos | PDF | Numbers | Prime Number"
[2]: https://www.erdosproblems.com/tags/divisors?utm_source=chatgpt.com "m"
