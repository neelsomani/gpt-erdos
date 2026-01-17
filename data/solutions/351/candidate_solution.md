No, not as stated.

Take for instance (p(x)=-x). Then
$
A=\\{-n+\frac1n:\ n\in\mathbb N\\}\subseteq (-\infty,0],
$
since (-1+1=0) and for (n\ge2) we have (-n+\frac1n<0). Hence every finite sum of distinct elements of $A$ is (\le 0), so the set of subset–sums cannot contain *any* positive integer, let alone “all sufficiently large” ones. Therefore $A$ is not strongly complete.

More generally, if $p$ has **negative leading coefficient**, then (p(n)+1/n<0) for all sufficiently large $n$, so $A$ contains only finitely many positive elements; deleting those finitely many [[nomath]](taking $B$ to contain them)[[/nomath]] leaves only nonpositive numbers, and again no large integer can be represented.

---

### If you add a natural positivity hypothesis

The nontrivial version of this question is usually taken with $p$ **eventually nonnegative** [[nomath]](e.g. leading coefficient $>0$)[[/nomath]], and in that form it is an Erdős–Graham open problem (#351 on the Erdős Problems site). ([Erdős Problems][1])

Some partial results are known:

* For (p(n)=n), Graham proved a strong “Egyptian fraction partition” theorem: every integer (>77) can be partitioned into distinct positive integers whose reciprocals sum to $1$, and more generally one can force all parts to be (\ge \beta). This yields strong completeness for $\\{n+1/n\\}$. ([Dipartimento di Matematica e Informatica][2])
* There are also results for (p(n)=n^2) [[nomath]](via a related Erdős–Graham problem about $\sum 1/n_i=1$ and $\sum n_i^2=m$)[[/nomath]], which imply completeness for $\\{n^2+1/n\\}$ and (with additional work) strong completeness. ([Erdős Problems][3])

So: **false in full generality**, and **open in general under the usual “$p$ grows positively” assumptions**.

[1]: https://www.erdosproblems.com/351 "
  
    Erdős Problem #351
  
"
[2]: https://www.dmi.unipg.it/files/matematica/seminari-cds-matematica/A-Theorem_on_Partitions.pdf "A theorem on partitions"
[3]: https://www.erdosproblems.com/283 "
  
    Erdős Problem #283
  
"
