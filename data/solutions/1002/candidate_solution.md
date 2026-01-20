Write
[
S_n(\alpha):=\sum_{k=1}^n\bigl({k\alpha}-\tfrac12\bigr),
\qquad\text{so that}\qquad
f(\alpha,n)= -,\frac{S_n(\alpha)}{\log n}.
]
So your question is: does (S_n(\alpha)/\log n) [[nomath]](with $\alpha$ distributed by Lebesgue measure on $(0,1)$)[[/nomath]] converge in distribution as (n\to\infty)?

### What is known [[nomath]](and gives a candidate $g$)[[/nomath]]

A classical theorem of Kesten proves a **Cauchy limit law** once one also randomizes the *starting point* of the rotation. Concretely, if $(\alpha,\beta)$ is uniform on ([0,1]^2), then
[
\frac{1}{\sigma',\log N}\sum_{n=1}^N\bigl({n\alpha+\beta}-\tfrac12\bigr)\ \xrightarrow{d}\ \mathrm{Cauchy},
]
and Borda computes the constant for this “sawtooth” observable as
[
\sigma'=\frac1{4\pi}.
]
Moreover, Borda explicitly notes that this is the same classical Kesten limit law for (f(x)={x}-\tfrac12). ([arXiv][1])

Because the Cauchy law is symmetric, replacing ({n\alpha+\beta}-\tfrac12) by (\tfrac12-{n\alpha+\beta}) does not change the limiting distribution. So **in the randomized-starting-point model** the limiting distribution function would be
[
g_{\mathrm{Cauchy}}(c)
=\frac12+\frac1\pi\arctan!\\(\frac{c}{\sigma'}\\)
=\frac12+\frac1\pi\arctan(4\pi c).
]
[[nomath]](Equivalently: Cauchy with scale $1/(4\pi)$.)[[/nomath]] ([arXiv][1])

### Your exact setup [[nomath]]($\beta=0$ fixed)[[/nomath]]: status

In your problem, the “starting point” is fixed ((\beta=0)). Whether the **same kind of limit law holds with a fixed starting point** is (as of the current literature I can find) **still open**. Borda states this explicitly: “The question whether $8$ and $9$ hold with a fixed starting point (\beta) … remains open,” where $9$ is precisely the sawtooth sum (\sum_{n\le N}({n\alpha+\beta}-1/2)) and thus covers (\beta=0). ([arXiv][1])

So at present there is **no proved** nondecreasing $g$ with
[
\lim_{n\to\infty}\bigl|{\alpha\in(0,1): f(\alpha,n)\le c}\bigr|=g(c)
]
for the *fixed* starting point (\beta=0).

### A closely related positive result (but it changes the model)

There is, however, a result in the “right direction” if one randomizes the **time** instead of (or in addition to) the starting point: Dolgopyat–Sarig prove an **annealed temporal limit theorem** where $n$ is chosen uniformly from ({1,\dots,N}) and (\alpha) is also randomized; in that model, the properly scaled sums converge to a Cauchy distribution. ([Weizmann Institute of Science][2])

### Bottom line

* **For your exact $f(\alpha,n)$ [[nomath]](fixed start $\beta=0$, deterministic time $n$)[[/nomath]]**: the existence of an asymptotic distribution function $g$ is **not currently settled** in the literature. ([arXiv][1])
* **If you additionally randomize the starting point** [[nomath]](replace ${k\alpha}$ by ${k\alpha+\beta}$ with $\beta$ uniform)[[/nomath]], then the limiting distribution exists and is **Cauchy**, with scale (1/(4\pi)), hence (g(c)=\tfrac12+\tfrac1\pi\arctan(4\pi c)). ([arXiv][1])

If you want, I can also summarize the main obstruction people mention for the fixed-(\beta) case [[nomath]](why the random $\beta$ proof doesn’t transfer directly)[[/nomath]], and the most natural conjecture for what $g$ *should* be.

[1]: https://arxiv.org/pdf/2303.08504 "https://arxiv.org/pdf/2303.08504"
[2]: https://www.weizmann.ac.il/math/sarigo/sites/math.sarigo/files/uploads/quenched-annealed.pdf "https://www.weizmann.ac.il/math/sarigo/sites/math.sarigo/files/uploads/quenched-annealed.pdf"
