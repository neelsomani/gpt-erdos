Yes.

A result of Chris Lambie‑Hanson gives much more than what you ask. He proves that for **every** function (f:\mathbb N\to\mathbb N) there is a graph (G) with
[
\chi(G)=\aleph_1
]
(sindeed (|G|=2^{\aleph_1})) such that for every (k\ge 3),

* every subgraph of (G) with **fewer than (f(k))** vertices has chromatic number **(<k)**. 

Now pick a very fast growing (f). For example, let
[
f(k)=2^{k^2}.
]

Take any subgraph (H) of (G) with (n) vertices. Put
[
k=\left\lceil \sqrt{\log_2 n}\right\rceil + 3.
]
Then (k^2>\log_2 n), so (2^{k^2}>n), i.e. (n<f(k)). By the theorem, this forces
[
\chi(H)<k \le \left\lceil \sqrt{\log_2 n}\right\rceil + 3.
]

In any proper coloring of (H) with (\chi(H)) colors, one color class has size at least (n/\chi(H)), so (H) has an independent set of size
[
\alpha(H)\ \ge\ \frac{n}{\chi(H)}\ >\ \frac{n}{n^\varepsilon}\ =\ n^{1-\varepsilon}
]
for every fixed (\varepsilon>0) once (n) is large enough (because (\sqrt{\log n}) grows much slower than (n^\varepsilon)). So (G) has exactly the property you asked for.

Extra note (only if you also care about the number of vertices): with the additional principle (\Diamond), Lambie‑Hanson also gets such examples with (|G|=\chi(G)=\aleph_1) (a Hajnal–Máté graph on (\omega_1)). 
