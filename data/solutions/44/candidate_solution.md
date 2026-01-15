This is **not known** in general. It is a well known Erdős question (listed as **Erdős Problem #44: “extending Sidon sets”**) and it is still marked open. ([Erdős Problems][1])

Why people care: if you could always do what you ask [[nomath]](extend *any* finite Sidon set $A$ to get size $(1-\epsilon)\sqrt M$ for some larger $M$)[[/nomath]], then you could iterate this and build an **infinite** Sidon set whose “best density along a subsequence” reaches $1$. That would solve another famous open Erdős problem about
[
\limsup_{n\to\infty}\frac{|S\cap{1,\dots,n}|}{\sqrt n}
]
being equal to $1$. This is Erdős Problem #329, and it is also open. ([Erdős Problems][1])

A stronger idea Erdős suggested was: “maybe every finite Sidon set can be embedded into a *perfect difference set*”. That would imply a positive answer to your question. But that **stronger** statement is false: there are explicit small Sidon sets [[nomath]](for example ${1,2,4,8,13}$)[[/nomath]] that cannot be extended to any finite perfect difference set. 

What *is* easy (but weaker than what you ask): by putting a known near–optimal Sidon construction far to the right of $N$ (so sums do not mix), one can always extend $A$ to get a Sidon set of size on the order of (\frac{1}{\sqrt2}\sqrt M). Getting the constant all the way up to (1-\epsilon) is exactly the hard open part, and nobody currently knows how to do it for every starting $A$.

[1]: https://www.erdosproblems.com/forum/thread/44 "

    Erdős Problem #44 - Discussion thread

"
