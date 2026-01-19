To make (n_k) well-defined for (k\ge 4), “general position” has to include **no four concyclic** (and also no three collinear, so every triple really determines a circle): otherwise, you could take $n$ points on one circle and then *every* triple has the same circumradius, so no $k$-subset can have (\binom{k}{3}) distinct radii. (This is also the formulation Erdős asked: “no three on a line, no four on a circle”.) 

With that understood:

## What is known about (n_k)

### 1) Exact values are not known in general (the problem is open)

This is an Erdős problem from 1975, and the task “determine (n_k)” is still considered open in the sense that no exact formula (or even tight asymptotics) is known. ([Erdős Problems][1])

### 2) Trivial lower bound

Obviously
[
n_k \ge k.
]
In fact for (k\ge 4) one also has (n_k\ge k+1) because there exist $k$ points in general position for which two different triples share the same circumradius (so the set itself fails the property), hence the property cannot be guaranteed at $n=k$.

### 3) Polynomial upper bounds [[nomath]](existence of $n_k$)[[/nomath]]

Erdős claimed an explicit $O(k^5)$ bound in 1978, but the argument had a gap; this is explained in Martínez–Roldán-Pensado. 

A corrected proof by Martínez and Roldán‑Pensado gives
[
n_k = O(k^9)
]
(with a slightly modified “general position” convention treating a line as a circle of infinite radius). 

Even better, a later “sunflower anti‑Ramsey” approach implies [[nomath]](specializing their general $\mathbb R^d$ result to $d=2$)[[/nomath]] that there is an absolute constant $C$ with
[
n_k \le Ck^{5}\log k.
]
This comes from their Corollary 1: if (|X|\ge c_2,k^{5}\log k) and no four points lie on a circle, then $X$ contains $k$ points whose triangle circumradii are all distinct. ([arXiv][2])

So the **best published general bound** is currently
[
k \le n_k \le Ck^5\log k.
]

### 4) Small $k$

From the Martínez–Roldán-Pensado paper one has explicit upper bounds
[
n_4 \le 9,\qquad n_5 \le 37,
]
but these are not known to be tight. 
Also (n_3=3) trivially.

## Why the (k^5\log k) bound appears (proof idea in one paragraph)

Color each triple of points by its circumradius. The key geometric input is: **fix a pair** $\\{A,B\\}$ and a radius $r$. There are at most **two** circles of radius $r$ through $A,B$ [[nomath]](one on each side of $AB$)[[/nomath]], so—using “no four concyclic”—there are at most two choices of the third point $C$ giving $R(ABC)=r$. Thus there are no large monochromatic “2‑sunflowers” (many edges sharing the same 2 vertices) in this 3‑uniform hypergraph coloring, and an anti‑Ramsey theorem for such colorings yields a rainbow $k$-set once $n$ is on the order of (k^5\log k). ([arXiv][2])

---

### Bottom line

At present, (n_k) is **not determined exactly**. The state of the art is:

* existence with polynomial bounds, and
* the best general published upper bound
  [
  n_k = O(k^5\log k),
  ]
  with explicit small-$k$ bounds (n_4\le 9), (n_5\le 37). 

[1]: https://www.erdosproblems.com/search_bib/Er78c/no "
  
    Erdős Problems
  
"
[2]: https://arxiv.org/pdf/1505.05170?utm_source=chatgpt.com "arXiv:1505.05170v1 [math.CO] 19 May 2015"
