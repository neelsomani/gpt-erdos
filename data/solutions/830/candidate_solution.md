No proof is known that there are infinitely many amicable pairs.

This is a classical open problem (already posed by Erdős): even though huge numbers of examples have been found computationally, we do not know how to prove that the set of amicable pairs is infinite. ([Dartmouth Mathematics][1])

## What is known about the counting function

Let me separate two closely related counting functions:

* Your (A_{\text{pairs}}(x)): the number of **pairs** $(a,b)$ with (1\le a\le b\le x) and (\sigma(a)=\sigma(b)=a+b).
* (A_{\text{nums}}(x)): the number of **integers** (n\le x) that belong to an amicable pair (often this is what analytic papers count).

They satisfy
[
2A_{\text{pairs}}(x)\ \le\ A_{\text{nums}}(x),
]
since every pair counted by (A_{\text{pairs}}(x)) contributes two amicable numbers (\le x).

### Upper bounds (Erdős, Pomerance, …)

Erdős proved that amicable numbers have **asymptotic density $0$**, i.e. (A_{\text{nums}}(x)=o(x)). ([Dartmouth Mathematics][2])

There have been successively stronger quantitative upper bounds. A major classical bound (Pomerance 1981) is of the shape
[
A_{\text{nums}}(x)\ \le\ \frac{x}{\exp\big((\log x)^{1/3}\big)}
\quad (x\ \text{large}),
]
as recorded in Pomerance’s expository summaries. ([Dartmouth Mathematics][2])

The strongest widely cited modern form is due to Pomerance (2014/2015 notes). One version states [[nomath]](as $x\to\infty$)[[/nomath]]
[
A_{\text{nums}}(x)\ \le\ \frac{x}{\exp\Big(\big(\tfrac12+o(1)\big)\sqrt{\log x,\log\log\log x}\Big)}.
]
([Dartmouth Mathematics][1])

In particular, he highlights the simpler consequence that for all sufficiently large $x$,
[
A_{\text{nums}}(x)\ \le\ \frac{x}{e^{\sqrt{\log x}}}.
]
([Dartmouth Mathematics][1])

Since (A_{\text{pairs}}(x)\le A_{\text{nums}}(x)/2), all of these are also upper bounds for your pair-counting function (up to a factor of 2).

A key point for your second question: these bounds are still of the form (x^{1-o(1)}) [[nomath]](because dividing by $\exp(\sqrt{\log x,\log\log\log x})$ only removes an $x^{o(1)}$ factor)[[/nomath]]. So current upper bounds do **not** rule out a lower bound like (x^{1-o(1)}).

### Lower bounds

Unconditionally, we do **not** have meaningful lower bounds for (A_{\text{pairs}}(x)) as (x\to\infty)—in particular, we cannot even prove (A_{\text{pairs}}(x)\to\infty). Pomerance explicitly notes “we have no good lower bounds” in expository material. ([Dartmouth Mathematics][2])

So the statement
[
A_{\text{pairs}}(x) > x^{1-o(1)}
]
is currently **open** (and far beyond what is known), and it would in particular imply infinitely many amicable pairs. This is exactly how Erdős posed it. ([Erdős Problems][3])

## Computational evidence (lots of data, but not a proof)

Computations strongly suggest there are infinitely many: for example, very large databases exist and exhaustive searches have been pushed extremely far. Encyclopaedia Britannica reports that as of 2023 roughly (1.227\times 10^9) pairs were known and mentions a distributed project that completed a search up to (10^{20}) (in the sense used by that project). ([Encyclopedia Britannica][4]) The “Amicable numbers” BOINC/news page also records milestones such as completion of the search up to (10^{20}) and other enumerations. ([Sech][5])

But none of this yields a proof of infinitude or any lower bound remotely like (x^{1-o(1)}).

## Conditional infinitude via prime-producing formulas

There are classical parametric constructions (Thābit ibn Qurra, Euler’s generalizations) that generate amicable pairs **when certain associated numbers are prime**; these give *conditional* infinite families if one could prove infinitely many such prime instances. But proving such prime patterns is out of reach, so they do not resolve infinitude. ([Dartmouth Mathematics][2])

---

### Bottom line

* **Infinitely many amicable pairs?** Unknown/open. ([Dartmouth Mathematics][1])
* **Is (A(x)>x^{1-o(1)})?** Also open; we do not even have nontrivial unconditional lower bounds for $A(x)$. ([Dartmouth Mathematics][2])
* **What we do know:** (A(x)=o(x)) [[nomath]](density $0$)[[/nomath]], with very strong explicit upper bounds due to Pomerance. ([Dartmouth Mathematics][1])

[1]: https://math.dartmouth.edu/~carlp/amicablesv3.pdf "https://math.dartmouth.edu/~carlp/amicablesv3.pdf"
[2]: https://math.dartmouth.edu/~carlp/firstfunctiondart.pdf "https://math.dartmouth.edu/~carlp/firstfunctiondart.pdf"
[3]: https://www.erdosproblems.com/search_bib/Er83?sources_only=1 "https://www.erdosproblems.com/search_bib/Er83?sources_only=1"
[4]: https://www.britannica.com/science/amicable-numbers "https://www.britannica.com/science/amicable-numbers"
[5]: https://sech.me/ap/news.html "https://sech.me/ap/news.html"
