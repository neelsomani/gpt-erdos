This is **not known in general** (for the interesting case where (a,b,c\ge 2)). It is a well-known open problem of Erdős, usually stated in terms of **(d)-complete** sets/sequences. ([Erdős Problems][1])

### What “(d)-complete” means here

A set (A) of positive integers is called **(d)-complete** if **every sufficiently large integer** can be written as a sum of **distinct** elements of (A), with the extra rule that **no chosen summand divides another chosen summand**. 

Your set is
[
A={a^k b^\ell c^m : k,\ell,m\ge 0}.
]
The question is exactly asking whether this (A) is (d)-complete for every pairwise coprime triple ((a,b,c)). Erdős and Lewin explicitly stated this as a conjecture in their 1996 paper. 

### What is known

It **is proved** for some specific triples, but **not** for all triples.

Some proved cases recorded in the literature include: ([Erdős Problems][1])

* ((a,b,c)=(3,5,7)). ([Erdős Problems][1])
* ((a,b,c)=(2,5,c)) for (c\in{7,11,13,17,19}). ([Erdős Problems][1])
* Further results for ((2,5,c)) (including (c=23) and other values) were obtained later; one approach is in Ma–Chen (2016), which gives a criterion implying (d)-completeness and proves new examples. ([ScienceDirect][2])
* Chen–Yu (2023) give a general criterion for three bases and prove, for example:

  * ((3,5,r)) is (d)-complete for (1<r\le 14) with ((r,15)=1),
  * ((2,5,r)) is (d)-complete for (1<r\le 87) with ((r,10)=1),
  * ((2,7,r)) is (d)-complete for (1<r\le 33) with ((r,14)=1). ([IMPAN][3])

There are also **stronger** conjectures even in the “small” case ((2,3,5)), for example asking that all summands in the representation lie in a very short interval ((x,(1+\varepsilon)x)); those stronger versions are also open. ([Erdős Problems][1])

### Small but important nuance: if you allow (1)

If one of (a,b,c) equals (1), then your set is really just the **two-base** set ({p^k q^\ell}). For two bases, Erdős–Lewin showed that ({p^k q^\ell}) is (d)-complete **only** when ({p,q}={2,3}). 
So, if “integers” really includes (1), then the answer is **not always yes** (example: ((a,b,c)=(1,2,5)) reduces to ((2,5)), which is not (d)-complete). 

### Bottom line

* For the standard interpretation (a,b,c\ge 2): **open problem** in general. ([Erdős Problems][1])
* Many special cases are known (examples above), but there is no general theorem that covers all pairwise coprime triples yet. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/123 "
  
    Erdős Problem #123
  
"
[2]: https://www.sciencedirect.com/science/article/pii/S0022314X16000342 "On d-complete sequences of integers - ScienceDirect"
[3]: https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/207/2/115065/on-d-complete-sequences-of-integers-ii "On $d$-complete sequences of integers, IIAll"
