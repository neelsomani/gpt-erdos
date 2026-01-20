Let me write (d:=\deg f) [[nomath]](so $d=k$ in your notation)[[/nomath]]. An integer $m$ is **$r$-power-free** [[nomath]](often: **$r$-free**)[[/nomath]] if no prime power (p^r) divides $m$.

A necessary local condition for any positive-density statement is:

> [[nomath]](**No fixed $r$-th power divisor**)[[/nomath]] For every prime $p$ there exists some $n$ with (p^r\nmid f(n)).

[[nomath]](Otherwise the answer is trivially “density $0$”.)[[/nomath]]

## 1) $(d-1)$-power-free values: yes, positive density (unconditionally)

This case is classical and **is known** [[nomath]](and the restriction “$d\neq 2^\ell$” is not needed)[[/nomath]].

Heath-Brown’s survey explains the history as follows: Ricci (1933) proved an asymptotic for (r\ge d), Erdős (1953) proved that one can get $r$-free values for (r=d-1) [[nomath]](as soon as $d\ge 3$)[[/nomath]], and Hooley later obtained an **asymptotic formula** in the (r=d-1) case as well. 

Concretely, if (f\in\mathbb Z[x]) is irreducible of degree (d\ge 3) and satisfies the necessary local condition for (r=d-1), then
[
N_{f,r}(X):=|\\{1\le n\le X:\ f(n)\ \text{is (r)-free}\\}|
\sim C(f,r),X,
]
so the set has a **natural density** (C(f,r)>0). The constant has the expected Euler product form
[
C(f,r)=\prod_{p}\\(1-\frac{\rho_f(p^r)}{p^r}\\),\qquad
\rho_f(m):=|\\{n\bmod m:\ m\mid f(n)\\}|,
]
as stated in Heath-Brown’s introduction. 

So the answer to your first question is **yes** (under the obvious local conditions), and in fact one has a positive-density asymptotic.

## 2) $(d-2)$-power-free values: known in large degree; open in small degrees

For general irreducible one-variable $f$, the problem is much harder as you move $r$ down toward $2$ (squarefreeness).

### What is known unconditionally [[nomath]](general $f$)[[/nomath]]

A general theorem (Browning; generalized by Lapkova–Xiao) gives the expected asymptotic as long as
[
r \ \ge\ \frac{3d+1}{4},
]
for one-variable polynomials as well. ([arXiv][1])

If you plug in (r=d-2), this condition becomes (d\ge 9). Indeed Heath-Brown explicitly notes that (via Salberger/Browning methods) one can reach (k\ge (3d+1)/4), which makes (k=d-2) admissible once (d\ge 9). 

So:

* **If (d\ge 9)**, then ((d-2))-power-free values occur with **positive density**, hence infinitely often. 

For degrees (d=4,5,6,7,8), this general method does **not** currently reach (r=d-2) in full generality.

### Some special families

For the special family (f(x)=x^d+c), Heath-Brown proves an asymptotic for (r\ge (5d+3)/9), which already covers (r=d-2) for (d\ge 6). 

This is about the *shape* (x^d+c), not about a general irreducible polynomial of degree $d$.

### What remains open in small degrees

For squarefree values ((r=2)), Rudnick remarks that beyond degree $3$ “nothing seems known unconditionally” in the irreducible one-variable case, and explicitly singles out (a^4+2) as unknown. ([TAU Mathematics][2])
Browning’s 2024 paper reiterates that the question for a *given* integral polynomial has only been addressed unconditionally for degree (\le 3). ([ISTA Research Explorer][3])

So for general $f$ of degree $4$ [[nomath]](and likewise for some other small $(d,r)$ pairs)[[/nomath]], your second question is **open** in general.

## 3) The specific case (n^4+2): still open (but ABC would imply “yes”)

Your last question is exactly the “famous example” that keeps getting cited as open.

* Rudnick (2014) explicitly says it is **still not known** that (a^4+2) is infinitely often squarefree, and notes that Granville showed the **ABC conjecture** would settle the general one-variable squarefree-values problem. ([TAU Mathematics][2])
* Sanjaya–Wang (2021) likewise calls (a^4+2) “the most famous example” where even the infinitude of squarefree values is open. 

So:

* **Unconditionally:** it is **not known** whether (n^4+2) represents infinitely many squarefree integers. ([TAU Mathematics][2])
* **Conditionally (ABC):** one expects not only infinitely many, but a positive density with the predicted Euler product constant. ([TAU Mathematics][2])

---

If you tell me the degree $d$ you care most about in the $(d-2)$-free question [[nomath]](e.g. $d=5,6,7$ vs $d\ge 9$)[[/nomath]], I can summarize the best known unconditional range for that $d$ and what is conjectured, but the headline is:

* $(d-1)$-free: **yes, positive density** (classical). 
* $(d-2)$-free: **yes** for (d\ge 9) (positive density), **open** in small degrees in general. 
* (n^4+2) squarefree infinitely often: **open**, **ABC would imply yes**. ([TAU Mathematics][2])

[1]: https://arxiv.org/abs/1801.04481 "[1801.04481] Density of power-free values of polynomials"
[2]: https://www.math.tau.ac.il/~rudnick/papers/jnt%20final.pdf "https://www.math.tau.ac.il/~rudnick/papers/jnt%20final.pdf"
[3]: https://research-explorer.ista.ac.at/download/15312/18794/2024_JourNumberTheory_Browning.pdf?utm_source=chatgpt.com "Square-free values of random polynomials"
