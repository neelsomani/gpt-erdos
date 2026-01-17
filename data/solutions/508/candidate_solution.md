The exact value is **not known**. This is the **Hadwiger–Nelson problem**: determine the chromatic number of the unit-distance graph on (\mathbb{R}^2).

What is known (as of current published bounds) is
[
5 \le \chi(\mathbb{R}^2) \le 7,
]
so the answer must be **either $5$, $6$, or $7$**. ([ScienceDirect][1])

Why these bounds hold:

* **Lower bound (\ge 5):** In 2018, Aubrey de Grey exhibited a finite **unit-distance graph in the plane** that is **not 4-colourable**, implying the whole plane cannot be 4-coloured with the unit-distance constraint. ([arXiv][2])
  (Subsequent work reduced the size of such examples, but the key point for the plane is simply “a 5-chromatic unit-distance graph exists”.) ([Wikipedia][3])

* **Upper bound (\le 7):** There is an explicit **7-colouring of the plane** based on a **hexagonal tiling**: choose hexagons of diameter slightly less than $1$, and colour them in a repeating 7-colour pattern so that any two hexagons of the same colour are far enough apart that no unit-distance pair can share a colour. ([Wikipedia][3])

A subtle point (if you care about foundations): in some discussions the “exact value” can depend on set-theoretic axioms (e.g., issues related to choice), but in the usual mathematical setting the status remains “unknown, between 5 and 7”. ([Wikipedia][3])

[1]: https://www.sciencedirect.com/science/article/abs/pii/S0095895625000930?utm_source=chatgpt.com "Cutting corners"
[2]: https://arxiv.org/abs/1804.02385?utm_source=chatgpt.com "[1804.02385] The chromatic number of the plane is at least 5"
[3]: https://en.wikipedia.org/wiki/Hadwiger%E2%80%93Nelson_problem?utm_source=chatgpt.com "Hadwiger–Nelson problem"
