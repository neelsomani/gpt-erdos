Write the (unordered) representation function as
[
r_A(n):=|\\{(a,a')\in A^2:\ a\le a',\ a+a'=n\\}|.
]
Then (1_A*1_A(n)) counts **ordered** pairs, so
[
r_A(n)\ \le\ 1_A*1_A(n)\ \le\ 2,r_A(n)
]
(up to the diagonal), and in particular “(\to\infty)” and “(\gg \log n)” are unaffected by switching between these two conventions.

## 1) If (1_A*1_A(n)\to\infty), must $A$ contain a minimal order‑2 basis?

No.

Historically, Erdős–Nathanson explicitly raised this exact question (Problem 8 in Nathanson’s 1989 problems survey). ([theoryofnumbers.com][1])

As of late 2025 / early 2026, the Erdős Problems database lists the question as **disproved** and the discussion thread links to a note (Daniel Larsen) claiming a construction showing that even the growth condition (r_A(n)\to\infty) does **not** force $A$ to contain a minimal asymptotic basis of order 2. ([Erdős Problems][2])

*(Caveat: the linked proof appears to be a posted note rather than a refereed publication at the moment; the database and thread reflect the site’s current status assessment.)* ([Erdős Problems][3])

## 2) If (1_A*1_A(n)>\epsilon\log n) for all large $n$ [[nomath]](fixed $\epsilon>0$)[[/nomath]], must $A$ contain a minimal order‑2 basis?

Also **no** in general [[nomath]](for “arbitrary fixed $\epsilon>0$” in the sense “for any positive $\epsilon$”)[[/nomath]]. The same discussion thread says the linked note shows that **neither** the condition (r_A(n)\to\infty) nor the condition (r_A(n)\gg \log n) (with a fixed constant) is sufficient to guarantee a minimal subbasis. ([Erdős Problems][3])

However, there is an important **positive** theorem at a larger constant:

* **Erdős–Nathanson (Theorem 9):** If $A$ is an asymptotic basis of order 2 and
  [
  r_A(n)\ \ge\ c\log n\quad\text{for all sufficiently large }n
  ]
  for some constant (c>1/\log(4/3)) (natural log), then $A$ **does** contain a minimal asymptotic basis of order 2. ([theoryofnumbers.com][1])

Numerically (1/\log(4/3)\approx 3.476) [[nomath]](with $\log=\ln$)[[/nomath]], so this covers all sufficiently large constants multiplying (\log n). ([theoryofnumbers.com][1])

And there is also a classical **negative** result showing you can’t hope for anything as weak as a uniform lower bound:

* **Erdős–Nathanson (Theorem 10):** For every $t$ there exists an order‑2 asymptotic basis $A$ with (r_A(n)\ge t) for all large $n$ that nevertheless contains **no** minimal asymptotic basis of order 2. ([theoryofnumbers.com][1])

## Bottom line

* (1_A*1_A(n)\to\infty) **does not** force $A$ to contain a minimal order‑2 subbasis. ([Erdős Problems][2])
* Requiring (1_A*1_A(n)>\epsilon\log n) for a fixed (\epsilon>0) is **not** sufficient “for arbitrary (\epsilon)” either. ([Erdős Problems][3])
* But if you assume a **large enough** constant multiple of (\log n), specifically (>\big(\log\frac43\big)^{-1}\log n) (up to representation‑function convention), then $A$ **must** contain a minimal order‑2 subbasis. ([theoryofnumbers.com][1])

[1]: https://www.theoryofnumbers.com/melnathanson/pdfs/nath1989-71.pdf "https://www.theoryofnumbers.com/melnathanson/pdfs/nath1989-71.pdf"
[2]: https://www.erdosproblems.com/868 "https://www.erdosproblems.com/868"
[3]: https://www.erdosproblems.com/forum/thread/868 "

    Erdős Problem #868 - Discussion thread

"
