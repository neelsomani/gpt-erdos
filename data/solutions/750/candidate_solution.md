This is an Erdős problem and, in the full generality you stated [[nomath]](allowing $f(m)\to\infty$ *arbitrarily slowly*)[[/nomath]], it is **still open**. ([Erdős Problems][1])

A bit of context and what *is* known:

## Reformulation

Let (\alpha(H)) be the independence number of a (finite) subgraph $H$. Your condition is
[
\alpha(H)\ \ge\ \frac{|V(H)|}{2}-f(|V(H)|)\quad\text{for every finite subgraph }H\subseteq G.
]
Equivalently,
[
|V(H)|-2\alpha(H)\ \le\ 2f(|V(H)|),
]
so every finite subgraph is “almost half-stable” (almost bipartite in a coarse sense).

## What is known: linear error works

Erdős–Hajnal–Szemerédi proved that for every (\varepsilon>0) and every target chromatic number, there are graphs with arbitrarily large chromatic number whose every $n$-vertex subgraph contains a **bipartite induced subgraph on at least ((1-\varepsilon)n) vertices**. 

From such a bipartite induced subgraph you get an independent set of size at least half of it, i.e.
[
\alpha(H)\ \ge\ \frac{(1-\varepsilon)n}{2} = \frac n2-\frac{\varepsilon n}{2}.
]
So the answer is **yes** whenever $f(m)$ is **linear** [[nomath]](e.g. $f(m)=c m$ for any fixed $c>0$)[[/nomath]]. This is also summarized on the Erdős-problems page for this question. ([Erdős Problems][2])

There is also an earlier (weaker) linear-range result credited to Erdős–Hajnal for (f(m)\ge c m) with (c>1/4). ([Erdős Problems][2])

## What is known: bounded error cannot work

If the error were bounded, i.e. (\alpha(H)\ge |V(H)|/2-k) for all finite subgraphs $H$, then Folkman’s theorem implies (\chi(G)\le 2k+2), so you **cannot** get infinite chromatic number with bounded $f$. 

[[nomath]](Your hypothesis $f(m)\to\infty$ avoids this obstruction.)[[/nomath]]

## The actual “arbitrarily slowly” case

What remains open is exactly your question: can one replace a fixed linear loss (\Theta(m)) by an **additive** loss (f(m)\to\infty) that might be *sublinear*, e.g. $f(m)=\log m$, (\log\log m), etc.? As of the latest public tracking (Oct 2025 update) it is listed as **open**. ([Erdős Problems][1])

So the best current summary is:

* **Yes** for (f(m)=\Theta(m)) [[nomath]](indeed for any fixed $\varepsilon>0$, you can get $\alpha(H)\ge (1-\varepsilon)|V(H)|/2$)[[/nomath]]. 
* **No** if $f$ is bounded (Folkman). 
* **Open** for general (f(m)\to\infty) [[nomath]](especially sublinear $f$)[[/nomath]]. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/750 "
  
    Erdős Problem #750
  
"
[2]: https://www.erdosproblems.com/forum/thread/750 "

    Erdős Problem #750 - Discussion thread

"