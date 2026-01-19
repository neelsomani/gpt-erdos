Both questions are **open** (as of early 2026).

This is an Erdős problem (asked at Oberwolfach in 1988): for
[
A=\\{\sum_{n\in S}n!:S\subset\mathbb N\text{ finite}\\},
]
is $A$ expected/known to contain only finitely many perfect $k$th powers ((k\ge2)) and only finitely many **powerful** (a.k.a. squareful) numbers?  No proof is known either way. ([Erdős Problems][1])

A quick logical point: every perfect $k$th power with (k\ge2) is automatically a **powerful number**, so a positive answer to the “powerful” question would imply a positive answer to the “$k$th powers” question. The difficulty is that even the powerful-number question is open. ([Erdős Problems][1])

## What is known computationally (perfect powers)

OEIS tracks the currently known **perfect powers** that can be written as a sum of distinct factorials [[nomath]](in the usual “factorial sum” sense; the OEIS entry notes its convention about whether $0!$ and $1!$ are treated as distinct)[[/nomath]]. The known perfect powers are:
[
0,1,4,8,9,25,27,32,121,128,144,729,841,5041,5184,45369,46225,363609,403225,3674889,1401602635449.
]
No others are currently listed/known there. ([OEIS][2])

If in your definition you **do not** allow both (0!) and (1!) to appear “distinctly” [[nomath]](some authors take $\mathbb N={1,2,3,\dots}$, or they regard $0!$ and $1!$ as the same factorial value $=1$)[[/nomath]], then you should drop the term $4$, since it arises from (2!+1!+0!=4). ([OEIS][2])

## Squares in particular (already open)

Even for $k=2$ (squares), the problem is open. In fact, ErdősProblems explicitly notes that it is open **even whether there are infinitely many squares of the form $1+n!$** (a classical Brocard–Ramanujan-type issue), and (1+n!\in A) for all $n$ because (1=1!) [[nomath]](or $0!$)[[/nomath]]. ([Erdős Problems][1])

The OEIS list of known squares in $A$ is:
[
1,4,9,25,121,144,729,841,5041,5184,45369,46225,363609,403225,3674889,1401602635449,
]
and it comments that there are **no other such squares below $31!$**. It also records that if any further terms exist beyond (1183893^2=1401602635449), then the next square would have to be **larger than (48!\approx 1.24\times10^{61})**. ([OEIS][3])

So: even the square case is far from settled, despite substantial computation.

## Powerful numbers (squareful) in $A$

OEIS also tracks the known **powerful numbers** that are sums of distinct factorials. The currently listed ones are:
[
\begin{aligned}
&1, 8, 9, 25, 27, 32, 121, 128, 144, 729, 841, 864, 5041, 5184,\
&40328, 41067, 45369, 45387, 46208, 46225, 363609, 403225, 3674889,\
&43954688, 6230694987, 1401602635449.
\end{aligned}
]
That entry also notes [[nomath]](in its convention where $0!$ and $1!$ are *not* considered distinct)[[/nomath]] that the next term $a(27)$ is known to exceed (10^{18}), **if it exists**. ([OEIS][4])

## Partial theoretical progress

There is at least one nontrivial restriction known: Brindza and Erdős proved that for any fixed number $r$ of summands, if
[
n_1!+\cdots+n_r!
]
is powerful, then the smallest index (n_1) is bounded in terms of $r$ [[nomath]](equivalently: if all $n_i$ are large enough—depending on $r$—then the sum cannot be powerful)[[/nomath]]. ([Erdős Problems][1])
This is meaningful but does **not** settle the question for the full set $A$, where the number of summands (|S|) is unbounded.

A related (solved) direction is when the *base* is fixed: e.g. the equation
$
2^m = a_1!+\cdots+a_k!\quad(a_1<\cdots<a_k)
$
has only finitely many solutions, with largest (2^7=2!+3!+5!), and there are only finitely many representations of (3^m) as such a factorial sum as well. ([Erdős Problems][5])
But your question allows the base (or the root) to vary, which is harder.

## Bottom line

* **Finitely many $k$th powers in $A$ for each fixed (k\ge2)?** Open. ([Erdős Problems][1])
* **Finitely many powerful numbers in $A$?** Open. ([Erdős Problems][1])

If you tell me whether you are taking (\mathbb N={0,1,2,\dots}) or ({1,2,3,\dots}) [[nomath]](and whether you want to treat $0!$ and $1!$ as “distinct allowed summands”)[[/nomath]], I can restate the known lists in exactly your convention and point out which examples disappear/appear.

[1]: https://www.erdosproblems.com/1108 "
  
    Erdős Problem #1108
  
"
[2]: https://oeis.org/A051761 "A051761 - OEIS"
[3]: https://oeis.org/A025494 "A025494 - OEIS"
[4]: https://oeis.org/A115645 "A115645 - OEIS"
[5]: https://www.erdosproblems.com/403 "
  
    Erdős Problem #403
  
"
