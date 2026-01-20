You can rephrase this as a graph/poset “saturation” game.

* Let (G_n) be the graph with vertex set ({2,3,\dots,n}), where two vertices are adjacent iff they are comparable by divisibility [[nomath]](i.e., $a\mid b$ or $b\mid a$)[[/nomath]].
* A legal position $A$ is exactly an **independent set** in (G_n) (no edges among chosen vertices), i.e. a **primitive set**.
* The game ends exactly when $A$ is a **maximal** independent set (equivalently, a maximal primitive set).

This is the “competition–independence game” / “independent domination game” viewpoint from graph games. 
It’s also explicitly listed as an Erdős “saturation game”–type problem, and (as of the most recent public discussion I can find) it is **open** in the sense that Erdős’s linear-vs-$n/2$ thresholds are not resolved. ([Erdős Problems][1])

## What is guaranteed (unconditionally) about the length?

Let (|A|) be the number of moves when the game ends.

### Trivial universal upper bound: (|A|\le \lfloor n/2\rfloor)

The maximum possible size of a primitive set in ({2,\dots,n}) is (\lfloor n/2\rfloor), witnessed by ({ \lfloor n/2\rfloor+1,\dots,n}) (no element divides another). So no matter how the players play,
[
|A|\le \lfloor n/2\rfloor.
]

### Nontrivial universal lower bound: (|A|\ge (1+o(1))\dfrac{n}{\log n})

A key observation (recorded in the ErdosProblems discussion) is:

* Take any prime (p\in[\sqrt n,,n]).
* If (p\notin A) at the end, maximality forces $p$ to be comparable to some (a\in A). Since $p$ is prime and (1\notin{2,\dots,n}), the only way is that **(p\mid a)**, i.e. $A$ contains a multiple of $p$.
* But if (p\neq q) are distinct primes in $[\sqrt n,n]$, then no integer (\le n) can be divisible by both $p$ and $q$ [[nomath]](because $pq>n$)[[/nomath]]. Hence **different primes (p\ge \sqrt n) require different elements of $A$**.

Therefore,
[
|A|\ \ge\ |\\{p\ \text{prime}: \sqrt n\le p\le n\\}|
\ =\ \pi(n)-\pi(\sqrt n-1)
\ =\ (1+o(1))\frac{n}{\log n}.
]
This lower bound is stated in the discussion thread [[nomath]](and is “not a lot harder” than the $(n/2,n]$ primes observation)[[/nomath]]. ([Erdős Problems][1])

So **regardless of who is trying to end quickly**, the game is forced to last at least about (n/\log n) moves.

## What about the two thresholds you asked?

### “At least (\epsilon n) moves for fixed (\epsilon>0)?”

What’s known unconditionally is only
[
|A|\ \ge\ (1+o(1))\frac{n}{\log n},
]
and (\frac{n}{\log n}=o(n)). So current unconditional guarantees are **much smaller than (\epsilon n)** for any fixed (\epsilon>0).

Whether the *prolonging* player can force a **linear** number of moves against optimal resistance is exactly the kind of question Erdős was asking here, and it remains open in the public record of the problem. ([Erdős Problems][1])

### “At least ((1-\epsilon)\frac n2) moves?”

The absolute ceiling is (\lfloor n/2\rfloor), but getting within ((1-\epsilon)\frac n2) would mean the prolonging player can force play to end near a *maximum* primitive set. That is also far beyond what is currently proved in general, and is likewise open in the ErdosProblems formulation. ([Erdős Problems][1])

## Computational evidence [[nomath]](small $n$)[[/nomath]]

The same discussion thread includes exact optimal-play computations (with the *Long* player starting) for (n\le 40), and the resulting game lengths track (\pi(n)) plus a slowly growing additive term [[nomath]](e.g. $f(n)-\pi(n)$ equals $0,1,2,3,4$ on successive ranges up to $40$)[[/nomath]]. ([Erdős Problems][1])
That numerical evidence is nowhere near (\sim n/2) in that range, but of course it doesn’t settle the asymptotic question.

## Bottom line

* **Guaranteed (for any play):** the game lasts at least ((1+o(1)),n/\log n) moves. ([Erdős Problems][1])
* **Always:** it ends by (\lfloor n/2\rfloor) moves (since no primitive set can be larger).
* **Open (as posed by Erdős):** whether optimal play forces (\Omega(n)) moves, or even ((1-\epsilon),n/2) moves. ([Erdős Problems][1])

If you want, I can also sketch (nonrigorously) why the $[\sqrt n,n]$ primes lower bound is “the right scale” for *smallest* maximal primitive sets [[nomath]](it essentially matches $\pi(n)$)[[/nomath]], and discuss the kinds of strategies people speculate about for the long player (primorial-type “defense” moves are mentioned in the thread). ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/forum/thread/872 "

    Erdős Problem #872 - Discussion thread

"
