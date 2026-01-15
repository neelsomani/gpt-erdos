These questions are known (they are listed as an Erdős problem in Hayman’s problem list). The current state is:

### 1) Is it true that (\limsup M_n=\infty)?

Yes.

This was proved by Gerold Wagner (1980). In fact, he proved a quantitative version: there is an absolute (c>0) such that
[
M_n>(\log n)^c
]
for infinitely many (n). ([Erdős Problems][1])

So in particular, (M_n) cannot stay bounded. ([Erdős Problems][1])

### 2) Is it true that there exists (c>0) such that for infinitely many (n), (M_n>n^c)?

Yes.

József Beck (1991) proved a stronger statement: there exists an absolute (c>0) such that for every (N),
[
\max_{n\le N} M_n > N^c.
]
This implies your statement: for each large (N) pick (n\le N) with (M_n>N^c); then automatically (M_n>N^c\ge n^c), and such (n) must occur infinitely often. ([Erdős Problems][1])

It is also known that (M_n) can be made relatively small in general: Erdős gave an example sequence with (M_n\le n+1) for all (n), and Linden (1977) improved this to a construction with (M_n\ll n^{1-c_0}) for some (c_0>0). ([Erdős Problems][1])

### 3) Is it true that there exists (c>0) such that for all large (n),

[
\sum_{k\le n} M_k > n^{1+c},?
]

As far as the standard references and current tracking go, this remains open.

The Erdős problem database page (last edited 29 Dec 2025) still lists this third question as open and says no proof/counterexample is known. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/119 "
  
    Erdős Problem #119
  
"
