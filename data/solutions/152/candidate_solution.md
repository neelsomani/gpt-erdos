Let (A={a_1<a_2<\dots<a_k}\subset\mathbb N) be a finite **Sidon set** [[nomath]](i.e. all sums $a_i+a_j$ with $i\le j$ are distinct)[[/nomath]]. Put
[
S:=A+A={a_i+a_j:\ 1\le i\le j\le k}.
]
Then the condition

[
a\in S,\quad a-1\notin S,\quad a+1\notin S
]

means exactly that $a$ is a **singleton block** (a “length one interval”) when you write $S$ as a disjoint union of maximal intervals of consecutive integers.

### Status of your statement

As far as the standard references indicate, the statement

> “for every $M$ and all sufficiently large finite Sidon sets $A$, the sumset $A+A$ contains at least $M$ singleton blocks”

is *precisely a known open problem* (posed by Erdős–Sárközy–Sós and repeated in later surveys). In particular, O’Bryant’s Sidon bibliography explicitly asks whether the number of “length one” intervals in the sumset of a finite Sidon set must go to infinity with (|A|). 

So: the claim you wrote is not something that is “standardly proved” in the literature source I can access here; it is presented there as an open question.

### What is known (strong, but one‑sided)

There *are* strong results showing that $A+A$ has lots of “block starts” (elements of $S$ whose left neighbor is missing) and, more generally, lots of elements with a missing translate.

A convenient way to say this is: for (d\ge 1) define
[
B(S,d):=\\{s\in S:\ s-d\notin S\\}.
]
Then there is a theorem (going back to work of Erdős–Sárközy–Sós and later sharpened/recorded in surveys) that for each fixed (d),
[
|B(A+A,d)| \ge c,|A|^2
]
for some absolute constant (c>0). 

In particular for (d=1), $B(S,1)$ is exactly the set of **left endpoints** of the consecutive blocks in $S$. So this implies:

* $A+A$ breaks into (\gg |A|^2) blocks of consecutive integers. 
* Since (|A+A|=k(k+1)/2) for a Sidon set of size $k$, this means the **average block length is bounded** (it is on the order of $2$).

This is very strong “gap” information. But it does **not** by itself force many singleton blocks, because in principle you could imagine (in the extreme) that almost every block has length exactly $2$, giving many block starts but *zero* singleton blocks.

### Why the “both sides missing” version is harder

Your condition is exactly
[
\text{singleton block} \quad \Longleftrightarrow \quad s\in S,\ s-1\notin S,\ s+1\notin S.
]

The known results give lots of $s$ with (s-1\notin S) (block starts) and likewise lots with (s+1\notin S) (block ends). The open difficulty is to force many points where *both* happen at once, i.e. many blocks of length $1$. 

### A reasonable “route to a proof” (what one would try next)

A natural way people try to attack your statement is:

1. If singleton blocks were bounded [[nomath]](say $\le M$)[[/nomath]], then because we already know there are (\gg k^2) blocks total, “most blocks” would have to be of length $2$ (or very close to that).
2. A length‑2 block ({x,x+1}\subset S) gives an equation
   [
   x=a+b,\qquad x+1=c+d,
   ]
   so
   [
   a+b+1=c+d.
   ]
   If one could show that a Sidon set $A$ cannot generate *too many* such “$+1$” relations (in a way that scales with $k$), then you would force many blocks that are not length 2, and from there you would force many length‑1 blocks.

This is the kind of counting/structure step that is not currently available in the generality needed (which is why the survey labels the length‑one question as open). 

### Bottom line

* The exact claim you wrote is (in the sources I can access here) the same as a **well‑known open problem** about “length one intervals” in $A+A$. 
* What *is* proved is a strong one‑sided substitute: for each fixed $d$, there are (\gg |A|^2) sums (s\in A+A) with (s-d\notin A+A), so $A+A$ has (\gg |A|^2) blocks and lots of gaps. 
* Turning that into (\gg 1) [[nomath]](let alone $\to\infty$)[[/nomath]] singleton blocks is exactly the missing step.

If you want, I can also write out a clean proof of the **known** result “for any fixed $d$, there are (\gg |A|^2) sums (s\in A+A) with (s-d\notin A+A)” (the theorem quoted above), and then show precisely where the argument stops short of giving two‑sided isolation.
