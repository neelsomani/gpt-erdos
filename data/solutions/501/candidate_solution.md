Let (F(x)=A_x). Your “independent set” is what set theorists usually call a **free set** for the set mapping $F$: a set (X\subseteq\mathbb R) such that for all distinct (x,y\in X), (x\notin F(y)).

## 1) Bounded sets of outer measure (<1): must there be an infinite independent set?

As far as is currently recorded in the literature/problem lists, this is **not settled in ZFC** (so one cannot say “yes” in absolute generality), and in fact it is **consistent that the answer is no**:

* **Erdős–Hajnal (1960)** proved that under your hypotheses one can always find **arbitrarily large finite** independent sets. ([Erdős Problems][1])
  [[nomath]](So for every $n\in\mathbb N$ there is an independent set of size $n$.)[[/nomath]]

* **Hechler (1972)** showed that **assuming the Continuum Hypothesis (CH)**, the answer to your first question can be **negative**: there is a family ({A_x}_{x\in\mathbb R}) of bounded sets of outer measure (<1) with **no** infinite independent set [[nomath]](indeed, the construction can prevent even an independent set of size $2$)[[/nomath]]. ([Erdős Problems][1])

* On the other hand, there is a strong **positive** result under extra regularity:

  **Newelski–Pawlikowski–Seredyński (1987)** proved that if, in addition, every (A_x) is **closed**, then there **does** exist an **infinite** independent set. ([Erdős Problems][1])

So the “plain” ZFC status of the first question [[nomath]](with no definability/regularity assumptions beyond bounded + outer measure $<1$)[[/nomath]] is listed as **open** on problem compilations. ([Erdős Problems][2])

### A quick sketch of why CH can kill independence

Under CH you can well-order (\mathbb R) in type (\omega_1) in a way that keeps initial segments bounded [[nomath]](e.g. enumerate $[-1,1]$ first, then $[-2,2]$, etc., each in $\omega_1$ many steps)[[/nomath]]. Then define (A_x) to include “all earlier reals” in the well-order. Under CH each initial segment is countable, hence has outer measure (0<1), and boundedness is arranged by the way you enumerate. This makes every pair (x\neq y) comparable in the order and forces (at least) one membership (x\in A_y), destroying independent pairs and hence infinite independent sets. (This is the idea behind the CH counterexample cited above.) ([Erdős Problems][1])

## 2) If the (A_x) are closed and have (Lebesgue) measure (<1): must there be an independent set of size $3$?

Here the situation depends crucially on whether you also keep the **boundedness** requirement.

* If you assume **closed + bounded** (so, compact) together with “measure (<1)”, then you’re in the regime where the **NPS87 theorem applies**, and you actually get an **infinite** independent set [[nomath]](hence certainly one of size $3$)[[/nomath]]. ([Erdős Problems][1])

* In the **unbounded** closed case (as your second question is commonly stated in problem lists), the best published guarantee recorded there is:

  **Gładysz (1962)** proved that one can always find an independent set of size **$2$** under the assumptions of the second question. ([Erdős Problems][1])

  Whether one can always force an independent set of size **$3$** in that setting is recorded as **open**. ([Erdős Problems][1])

## Bottom line

* **First question [[nomath]](bounded, outer measure $<1$)[[/nomath]]**: not provable “yes” in ZFC; **no under CH**, **yes if all (A_x) are closed**; ZFC-without-extra-hypotheses is listed as **open**. ([Erdős Problems][1])

* **Second question [[nomath]](closed, measure $<1$, as stated without boundedness)[[/nomath]]**: **size 2 is known**, **size 3 is open** (unless you add boundedness, in which case you get an infinite independent set). ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/latex/501 "https://www.erdosproblems.com/latex/501"
[2]: https://www.erdosproblems.com/forum/thread/501 "https://www.erdosproblems.com/forum/thread/501"
