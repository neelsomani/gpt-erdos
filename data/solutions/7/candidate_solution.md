It depends on whether you require the moduli to be **distinct** (which is the nontrivial version people usually mean).

### If repeated moduli are allowed: **Yes (trivially).**

For example,
[
{,0 !!\pmod 3,; 1 !!\pmod 3,; 2 !!\pmod 3,}
]
covers every integer, and all moduli are the odd number (3). More generally, for any odd (m>1), the full set of residue classes
[
{,0!!\pmod m,;1!!\pmod m,;\dots,;(m-1)!!\pmod m,}
]
is a covering system with all moduli equal to (m). ([Wikipedia][1])

### If the moduli must be **distinct** and (>1): **Open problem.**

This is the classical **Erdős–Selfridge “odd covering” problem**: does there exist a *distinct* covering system whose moduli are all odd? As of the current literature, this is still **unknown** (no example and no impossibility proof). ([Erdős Problems][2])

What *is* known includes (among other restrictions):

* If you also require the moduli to be **square-free**, then such an all-odd distinct covering system **cannot exist** (there must be an even modulus). ([arXiv][3])
* In any distinct covering system, at least one modulus is divisible by (2) or (3) (so an all-odd one would force a modulus divisible by (3)). ([arXiv][4])
* If an odd distinct covering system exists, its moduli must satisfy strong global constraints (e.g. the lcm must be divisible by (9) or (15)). ([Erdős Problems][2])

So: **“Yes”** in the general (non-distinct) sense; **“unknown/open”** in the distinct-moduli sense that Erdős and Selfridge asked.

[1]: https://en.wikipedia.org/wiki/Covering_system?utm_source=chatgpt.com "Covering system"
[2]: https://www.erdosproblems.com/latex/7 "
  
    Erdős Problems
  
"
[3]: https://arxiv.org/abs/1901.11465?utm_source=chatgpt.com "The Erdős-Selfridge problem with square-free moduli"
[4]: https://arxiv.org/abs/1703.02133?utm_source=chatgpt.com "Covering systems with restricted divisibility"
