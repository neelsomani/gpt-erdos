This is (essentially verbatim) **Erdős Problem #38**, and **it is currently open**: no example of such a set (B) is known, and no proof that none can exist is known either.

### What *is* known

* **If (B) *is* an additive basis of order (k)**, then Erdős proved a quantitative density–increment statement of exactly this “single translate” form: for every (A) of Schnirelmann density (\alpha) and every (N), there exists (b\in B) with
  [
  |(A\cup (A+b))\cap{1,\dots,N}|\ \ge\ \Bigl(\alpha+\frac{\alpha(1-\alpha)}{2k}\Bigr)N.
  ]

  (There are historical refinements of the constant in terms of a “mean order” parameter (\lambda) due to Landau/Brauer/Selberg, but these all still assume (B) is a basis in the appropriate sense. )

* **Even for (B=\mathbb N)**, Erdős noted a limitation: a random set of density (\alpha) shows you cannot push the increment factor past (\alpha(1-\alpha)).
  So the “best possible” (f(\alpha)) in the easiest case (B=\mathbb N) is constrained between the known lower bounds and this natural upper bound, and improving Erdős’s bound is itself nontrivial.

* Your property is **stronger than** the classical notion of **“essential component”** (which asks for (d_s(A+B)>d_s(A)) for all (A) with (0<d_s(A)<1)).
  Linnik constructed an essential component that is **not** an additive basis, showing that the *weaker* phenomenon can happen.
  But it is not known whether one can upgrade this to your **uniform, one-translate, quantitative** form.

* A useful necessary constraint: because your property would imply (in particular) that (B) behaves like an essential component, **Ruzsa’s theorem** on essential components gives growth lower bounds. In particular, if (B) were an essential component then it must satisfy
  [
  |B\cap{1,\dots,N}|\ \ge\ (\log N)^{1+c}
  ]
  for some (c>0) and all large (N).
  So any (B) with your stronger property would have to be **at least “polylogarithmically thick”**, in particular **not lacunary** (not exponentially sparse).

### Bottom line

As of **January 14, 2026**, the existence of such a **non-basis** set (B) with a uniform increment function (f(\alpha)>0) is **unknown**; it remains an open Erdős problem.
