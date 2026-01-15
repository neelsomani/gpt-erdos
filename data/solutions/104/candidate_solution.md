This statement is **not proved** in general. It is a well-known **open problem of Erdős**.

Let (f(n)) be the *maximum* possible number of **distinct unit circles** (radius (1)) that each contain **at least 3** points from a set of (n) points in the plane. Erdős conjectured that
[
f(n)=o(n^2)\quad\text{(equivalently, }f(n)/n^2\to 0\text{)}.
]
This is still open. ([erdosproblems.com][1])

## What we do know

### 1) Easy general upper bound: (f(n)\le \frac{n(n-1)}{3}=O(n^2))

The standard double counting is:

* Any unit circle that contains at least 3 points contains at least **3 pairs** of points on it.
* Any **pair** of points can lie on **at most 2** unit circles (because there are at most two circle centers at distance 1 from both points).

So if there are (f(n)) such circles, then
[
3f(n)\ \le\ 2\binom{n}{2},
]
hence
[
f(n)\ \le\ \frac{2}{3}\binom{n}{2}=\frac{n(n-1)}{3}.
]
This is exactly the (O(n^2)) bound Erdős mentions, and the sharper constant (\frac{1}{3}) is noted in later discussions. ([erdosproblems.com][1])

This does **not** give (o(n^2)). It only gives a quadratic bound.

### 2) Best known lower bound: (f(n)\ge c,n^{3/2})

Erdős also recorded a construction due to Elekes that produces about (n^{3/2}) unit circles:

* Take (k) unit vectors (e_1,\dots,e_k) in “general position”.
* Use the (\binom{k}{2}) points (e_i+e_j) as your point set (so (n=\binom{k}{2}\approx k^2/2)).
* For each triple (i<j<\ell), the point (e_i+e_j+e_\ell) is the center of a unit circle going through the three points (e_i+e_j), (e_i+e_\ell), (e_j+e_\ell).

That gives (\binom{k}{3}\approx k^3/6) distinct unit circles, and since (k\approx \sqrt{2n}), this is (\Theta(n^{3/2})). ([IME-USP][2])

## So the current picture is

[
c,n^{3/2}\ \le\ f(n)\ \le\ \frac{n(n-1)}{3}.
]
The conjecture (f(n)=o(n^2)) (and even the stronger guess (f(n)=O(n^{3/2}))) is still open. Erdős even offered a prize for proving or disproving the (O(n^{3/2})) bound. ([erdosproblems.com][1])

[1]: https://www.erdosproblems.com/104 "
  
    Erdős Problem #104
  
"
[2]: https://www.ime.usp.br/~yoshi/resenhas/abstracts/Erdos.pdf "resenhas_up.dvi"
