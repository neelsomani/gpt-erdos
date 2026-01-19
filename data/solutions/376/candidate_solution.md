Using **Kummer’s theorem**, for any prime $p$,
[
v_p\binom{2n}{n}
]
equals the **number of carries** that occur when adding $n+(n)$ in base $p$. 
So (p\nmid \binom{2n}{n}) iff there are **no carries** in that base, which happens exactly when every base-$p$ digit of $n$ is at most $(p-1)/2$. [[nomath]](Because doubling a digit $\le (p-1)/2$ stays $\le p-1$, so no carry can ever start.)[[/nomath]] 

Therefore,
[
\gcd\left(\binom{2n}{n},105\right)=1
]
is equivalent to the simultaneous digit restrictions:

* in base $3$: digits of $n$ are only $0,1$;
* in base $5$: digits of $n$ are only $0,1,2$;
* in base $7$: digits of $n$ are only $0,1,2,3$. ([Erdős Problems][1])

## Are there infinitely many such $n$?

**This is currently unknown.**

Your question is a well-known open problem (often called **Graham’s 105 problem**, also appearing as an Erdős problem). It asks whether there are infinitely many $n$ with (\binom{2n}{n}) coprime to $105$, and it remains unsolved; in particular, Ron Graham offered a cash prize for deciding whether the set is finite or infinite. 

What *is* known is that for the product of **two** odd primes $pq$, there are infinitely many $n$ with $\gcd\left(\binom{2n}{n},pq\right)=1$; but the corresponding statement for **three** primes [[nomath]](such as $3\cdot 5\cdot 7=105$)[[/nomath]] is exactly where the difficulty lies. ([Erdős Problems][1])

There are many explicit examples (so the set is certainly nonempty and not “tiny” computationally), e.g.
[
n=0,1,10,756,757,3160,\dots
]
are among the known solutions. 

And as of late **December 28, 2025** (with additional notes in early **January 2026**), the problem is still listed as open, with partial progress on related variants but no resolution for $105$. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/forum/thread/376 "

    Erdős Problem #376 - Discussion thread

"
