Let the squares have side lengths (s_1,\dots,s_n), and assume their interiors are disjoint and they all lie inside the unit square.

### What we can prove easily

Because the squares do not overlap in interior, their total area is at most (1):
[
\sum_{i=1}^n s_i^2 \le 1.
]
Then Cauchy–Schwarz gives
[
\left(\sum_{i=1}^n s_i\right)^2 \le n \sum_{i=1}^n s_i^2 \le n,
]
so
[
f(n) \le \sqrt{n}.
]
In particular, for (n=k^2) this gives (f(k^2)\le k). And we can achieve (k) by tiling the unit square by a (k\times k) grid of squares of side (1/k). So
[
f(k^2)=k.
]
([erdosproblems.com][1])

Also, for (n=k^2+1) we always have (f(k^2+1)\ge k): start with the (k\times k) tiling, remove one (1/k)-square, and replace it by two squares of side (1/(2k)). The number of squares goes up by (1), and the sum of side lengths stays exactly (k). ([erdosproblems.com][1])

So the real question is the **upper bound**: can one ever get **strictly bigger than (k)** with (k^2+1) squares?

### Status of the exact question (f(k^2+1)=k)

For **general packings** (where squares may be placed in any positions, and typically may also be rotated), this is the classical **Erdős square-packing conjecture**. As of the latest publicly available references I can find, it is **still open** in full generality. ([erdosproblems.com][1])

Some special cases are known:

* Erdős proved (f(2)=1) (this is the case (k=1)). ([erdosproblems.com][1])
* Newman proved (f(5)=2) (this is the case (k=2)). ([erdosproblems.com][1])

### If you require the squares to be axis-parallel

If you add the extra rule that **every small square has sides parallel to the unit square**, then the conjectured equality **is proved for all (k)** (and even a more general formula is proved). This is a 2024 result of Baek–Koizumi–Ueoro. ([arXiv][2])

### Bottom line

* If squares are allowed with **no restriction on orientation**: **unknown/open** whether (f(k^2+1)=k) for all (k). ([erdosproblems.com][1])
* If squares must be **parallel to the sides of the unit square**: **yes**, (f(k^2+1)=k) holds (proved). ([arXiv][2])

[1]: https://www.erdosproblems.com/106 "
  
    Erdős Problem #106
  
"
[2]: https://arxiv.org/html/2411.07274v2 "A note on the Erdős conjecture about square packing"
