# Grok Response for Problem 174

**The Problem**

A finite set \(A \subset \mathbb{R}^n\) is Ramsey if
\[
\forall k \geq 1 \;\; \exists d = d(A,k) \quad \text{such that every } k\text{-colouring of } \mathbb{R}^d
\]
contains a monochromatic subset congruent to \(A\) (i.e., the image of \(A\) under an isometric embedding \(\mathbb{R}^n \hookrightarrow \mathbb{R}^d\)).

The task is to characterise all such sets \(A\).

**Attempt at a characterisation**

Write \(\operatorname{aff}(A)\) for the affine hull of \(A\) and \(\dim A = \dim \operatorname{aff}(A)\). Let \(w(A)\) be the *minimal width* of \(A\):
\[
w(A) = \inf_{|u|=1} \bigl( \max_{x,y\in A} \langle x-y,u\rangle \bigr) > 0
\]
(since \(A\) is finite and not a singleton). Let \(\operatorname{diam}(A)\) be the usual Euclidean diameter. A set \(A\) is *spherical* if there exists a point \(c\in \operatorname{aff}(A)\) equidistant from every element of \(A\) (i.e., \(A\) lies on a sphere of dimension \(\dim A-1\)).

After examining several candidate invariants (affine dimension, minimal width, sphericity, existence of a unique “centre”, parity of \(\dim A\), algebraic independence of squared distances), the only clean dichotomy that survives elementary sanity checks is:

**Conjecture.** \(A\) is Ramsey if and only if \(A\) is spherical.

**Why sphericity is necessary (heuristic).** Suppose \(A\) is not spherical. Then no isometric copy of \(A\) can ever lie on a sphere. One can therefore hope to colour \(\mathbb{R}^d\) “radially” with a fixed number of colours so that each colour class is a union of thin annular shells whose curvature prevents a non-spherical configuration from sitting inside a single colour. Because the shells can be chosen with thickness \(\approx w(A)\) and gaps \(\gg \operatorname{diam}(A)\), a non-spherical \(A\) cannot fit monochromatically without “bridging” two shells of different colours, independent of ambient dimension \(d\). (Making this rigorous requires a quantitative curvature estimate uniform in \(d\), which is not immediate.)

**Why sphericity is sufficient (heuristic).** If \(A\) lies on a sphere \(S^{m-1}(r)\) of radius \(r>0\), any isometric copy lies on some sphere of the same radius in \(\mathbb{R}^d\). By the Frankl–Rödl theorem on the chromatic number of Euclidean space, the chromatic number of the unit-distance graph in \(\mathbb{R}^d\) tends to infinity with \(d\). Once \(d\) is large enough that every \(k\)-colouring admits a monochromatic copy of a sufficiently dense subset of a sphere of radius \(r\), a compactness argument (or canonical Ramsey theorem for metric spaces) upgrades this to a monochromatic isometric copy of the whole finite set \(A\). The spherical constraint supplies the necessary “rigidity” that lets the high-dimensional unit-distance Ramsey phenomenon descend to the given configuration.

**Obstructions to a proof.**  
- The radial-shell colouring idea collapses for spherical sets (they can sit tangentially on a thin shell far from the origin).  
- The Frankl–Rödl argument gives only existential monochromatic unit-distance sets; controlling the precise geometry up to isometry of a non-equilateral set requires a quantitative “canonical” version that is not known.  
- Pathological (non-measurable) colourings constructed via Hamel bases over \(\mathbb{Q}\) evade all density arguments, so any proof must use only the Euclidean isometry group and not rely on Lebesgue measure.  
- No obvious reduction to lower-dimensional slices works, because a monochromatic copy may span all of \(\mathbb{R}^d\).

After exhausting these approaches and failing to turn either half of the conjecture into a rigorous proof, I conclude that I cannot solve the problem.

**Final answer**

I could not solve it.
