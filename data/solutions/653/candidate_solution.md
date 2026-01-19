This is **open**.

What is known is that $g(n)$ is linear in $n$, but the best published lower bound is still bounded away from $n$ by a fixed constant factor:

* Erdős–Fishburn proved (g(n)>\tfrac{3}{8}n).
* Csizmadia improved this to (g(n)>\tfrac{7}{10}n).
* On the other hand, Erdős–Fishburn and Csizmadia also proved an **upper bound**
  [
  g(n) < n - cn^{2/3}
  ]
  for some absolute constant (c>0). ([Erdős Problems][1])

So the conjectured asymptotic
[
g(n)\ge (1-o(1))n
]
is **consistent** with the known upper bound [[nomath]](since $n-cn^{2/3} = (1-o(1))n$)[[/nomath]], but it is **not proved**: the gap between the current lower bound (\tfrac{7}{10}n) and the upper bound (n-cn^{2/3}) remains. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/653 "https://www.erdosproblems.com/653"
