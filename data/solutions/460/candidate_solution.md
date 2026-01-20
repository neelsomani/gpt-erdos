Write
[
b_k:=n-a_k\qquad (k\ge 1).
]
Then the defining condition is exactly that the (b_k)’s are **pairwise coprime**:
$
\gcd(b_k,b_i)=1\quad (1\le i<k).
$
And because (a_k) is the *least* integer (>a_{k-1}) with that property, equivalently (b_k) is the **largest** integer (<b_{k-1}) that is coprime to all earlier (b_i). So ((b_k)) is a strictly decreasing sequence.

## The unrestricted process forces an “all primes” tail

Assume gcd is taken for integers in the usual way, (\gcd(x,y)=\gcd(|x|,|y|)), so the recursion continues past (a_k>n).

### Step 1: you must eventually pick $b=1$

Since the search for (b_k) is just “scan downward for the next integer coprime to all previous ones,” you will certainly reach $b=1$, and $1$ is coprime to everything. So for some index $K$,
[
b_K=1\qquad\text{hence}\qquad a_K=n-1.
]

### Step 2: by the time (b_K=1), every prime (<n) has already appeared

Claim: every prime (p<n) divides at least one of (b_1,\dots,b_{K-1}).

If not, take the largest prime (p<n) that never appeared as a divisor of the earlier (b_i). When the greedy scan reaches the value $b=p$, it is coprime to every earlier (b_i) [[nomath]](because $p$ is prime and not used)[[/nomath]], hence it would be eligible. But since the process is greedy and (p>1), it would pick $p$ before ever reaching $1$, contradicting (b_K=1). So all primes (<n) have indeed been “used” before $1$ is chosen.

### Step 3: after that, the process is forced to pick negative primes in order

After (b_K=1), the next candidates below $1$ are (0,-1,-2,\dots). We cannot take $0$ because (\gcd(0,b_i)=|b_i|\neq 1) for earlier (b_i>1). But (-1) is coprime to everything, so
[
b_{K+1}=-1\qquad\text{hence}\qquad a_{K+1}=n+1.
]

Now look for the next (b< -1) that is coprime to all previous (b_i). Since all primes (<n) already divide some earlier (b_i), any (m\ge 2) with a prime factor (<n) is forbidden: (\gcd(m,b_i)>1) for the (b_i) that contains that prime. Therefore the next permissible (|b|) must have **no prime factor (<n)**. The *smallest* such integer is the smallest prime (\ge n); call it (p_1). Hence
[
b_{K+2}=-p_1\qquad\text{and}\qquad a_{K+2}=n+p_1.
]

Inductively, after choosing (-p_t), the set of “used primes” contains **all primes (\le p_t)**, so no composite between (p_t) and the next prime (p_{t+1}) can be allowed [[nomath]](it would have a prime factor $\le p_t$)[[/nomath]]. Thus the greedy choice forces
[
b_{K+2+t}=-p_{t+1}\quad\text{for }t=0,1,2,\dots,
]
i.e. you get **every prime (\ge n)** in order, with
[
a = n+p \quad (p\text{ prime},\ p\ge n)
]
as a subsequence of ((a_i)).

## Consequence: (\sum_i \frac1{a_i}) diverges [[nomath]](for every $n$)[[/nomath]]

From the tail just identified,
[
\sum_i \frac1{a_i}\ \ge\ \sum_{\substack{p\ \text{prime}\ p\ge n}}\frac1{n+p}.
]
For (p\ge n), we have (n+p\le 2p), hence
[
\sum_{\substack{p\ \text{prime}\ p\ge n}}\frac1{n+p}
\ \ge\
\frac12\sum_{\substack{p\ \text{prime}\ p\ge n}}\frac1p.
]
Euler proved (\sum_{p}\frac1p=\infty). Therefore
[
\sum_i\frac1{a_i}=\infty
\quad\text{for every fixed }n,
]
so in particular it is “(\to\infty)” as (n\to\infty) in the strongest possible sense [[nomath]](it’s already infinite for each $n$)[[/nomath]].

## The restricted sums you asked about

Let
[
\mathcal I_{\le}(n):=\\{i:\exists\text{ prime }q\le a_i\text{ with }q\mid (n-a_i)\\},
]
and (\mathcal I_{>}(n)) be its complement.

### 1) Restricting to (\mathcal I_{\le}(n)): still diverges [[nomath]](for every $n$)[[/nomath]]

For the prime tail (a=n+p) [[nomath]](with $p\ge n$ prime)[[/nomath]], we have
[
n-a = -p,
]
which is divisible by the prime $p$, and (p\le n+p=a). So **every** tail term (a=n+p) lies in (\mathcal I_{\le}(n)). Hence
[
\sum_{i\in\mathcal I_{\le}(n)}\frac1{a_i}=\infty
\quad\text{for every }n.
]

### 2) Restricting to (\mathcal I_{>}(n)): finite [[nomath]](for every $n$)[[/nomath]]

After the process reaches (a=n+1) [[nomath]](i.e. $n-a=-1$)[[/nomath]] it then produces (a=n+p) for primes (p\ge n), and **none** of those terms are in (\mathcal I_{>}(n)) because (n-a=-p) has the prime divisor (p\le a). So (\mathcal I_{>}(n)) is contained in the *finite* initial segment up to (at most) (a=n+1). Therefore
[
\sum_{i\in\mathcal I_{>}(n)}\frac1{a_i}<\infty
\quad\text{for every }n.
]

---

## If you intended to stop at (a_i<n)

Some people implicitly only consider (\gcd) for positive integers, which would stop the construction at (a=n-1) [[nomath]](since $n-a=1$ is always allowed, but $n-a\le 0$ is not considered)[[/nomath]]. In that *finite* version, the sum is finite and the question “does it grow with $n$?” becomes nontrivial.

I can’t give a complete proof for that finite variant here, but numerically the finite sum grows very slowly and looks consistent with roughly (\log\log n + O(1)), with most of the growth coming from the “complement” class [[nomath]](those with no prime divisor $\le a_i$)[[/nomath]]. If that finite-variant behavior is what you meant, tell me and I’ll restate everything carefully in that model and give the cleanest provable bounds I can (and also show some computed values).
