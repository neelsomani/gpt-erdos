Write
[
l(n)=\min_{\substack{A\subset\mathbb Z\ |A|=n}}\ \max\\{|B|:\ B\subseteq A,\ \text{no }a_1=a_2+\cdots+a_r\text{ with distinct }a_i\in B,\ r\ge 2\\}.
]
So $l(n)$ is the **guaranteed** size of the largest “no element is a sum of distinct others” subset you can always find inside any $n$-set of integers.

## Best-known general bounds

The classical bounds (and still the standard quoted ones) are:

* Erdős proved (l(n)\ge (n/2)^{1/2}), and Choi improved this to (l(n)>(1+c),n^{1/2}) for some absolute (c>0). ([Erdős Problems][1])
* Choi also gave an explicit construction showing that, for large $n$, there exist $n$ distinct integers whose **largest** sum-free subsequence (in this sense) has size at most (Cn(\log\log n)^{-1/2}); in particular
  [
  l(n)\ \le\ C\frac{n}{\sqrt{\log\log n}}.
  ]
  ([American Mathematical Society][2])
* Choi–Komlós–Szemerédi (1975) strengthened both sides to
  [
  \left(\frac{n\log n}{\log\log n}\right)^{1/2}\ \ll\ l(n)\ \ll\ \frac{n}{\log n},
  ]
  and they conjectured (l(n)\ge n^{1-o(1)}). ([Erdős Problems][1])

So, up to constants,
[
l(n)\ \text{is between } n^{1/2}\sqrt{\frac{\log n}{\log\log n}}\quad\text{and}\quad \frac{n}{\log n}.
]

## Your two questions

### Does (l(n)n^{-1/2}\to\infty)?

Yes: the lower bound
[
l(n)\ \gg\ \left(\frac{n\log n}{\log\log n}\right)^{1/2}
]
implies
[
\frac{l(n)}{\sqrt n}\ \gg\ \sqrt{\frac{\log n}{\log\log n}}\ \longrightarrow\ \infty.
]
([Erdős Problems][1])

### Is it true that (l(n)<n^{1-c}) for some fixed (c>0)?

No such fixed $c$ is known from the best upper bounds: the strongest general upper bound quoted above is
[
l(n)\ \ll\ \frac{n}{\log n},
]
which is still (n^{1-o(1)}) and in fact eventually **larger** than (n^{1-c}) for every fixed (c>0). ([Erdős Problems][1])

Moreover, Choi–Komlós–Szemerédi explicitly conjectured the opposite behavior, namely
[
l(n)\ \ge\ n^{1-o(1)},
]
which (if true) would *rule out* any inequality of the form (l(n)<n^{1-c}) with constant (c>0). ([Erdős Problems][1])

So the current picture is: we know (l(n)=o(n)) [[nomath]](indeed $l(n)\ll n/\log n$)[[/nomath]], but it is open whether $l(n)$ is “almost linear” in the (n^{1-o(1)}) sense, and the conjecture points that way. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/latex/790 "https://www.erdosproblems.com/latex/790"
[2]: https://www.ams.org/journals/proc/1973-041-02/S0002-9939-1973-0325563-X/S0002-9939-1973-0325563-X.pdf "https://www.ams.org/journals/proc/1973-041-02/S0002-9939-1973-0325563-X/S0002-9939-1973-0325563-X.pdf"