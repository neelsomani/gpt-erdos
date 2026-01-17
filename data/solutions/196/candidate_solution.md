No one knows the answer yet.

This is a well-known open problem (asked by Erdős and Graham). It is listed as open as “Erdős Problem #196”. ([Erdős Problems][1])

A small simplification: if you find indices (i>j>k>l) with ((x_i,x_j,x_k,x_l)) an arithmetic progression, then ((x_l,x_k,x_j,x_i)) is also an arithmetic progression, and now the indices are increasing. So it is enough to ask for (i<j<k<l). (Reversing the order just changes the common difference from $d$ to $-d$.)

### What is known around it

* **Length 3 is forced.** Every permutation of (\mathbb N) has a 3-term arithmetic progression as a subsequence. There is even a short proof: take the first term (a_1), take the first later term (a_k>a_1), then the number (2a_k-a_1) must appear somewhere to the right (because it is a permutation), and (a_1,a_k,2a_k-a_1) is a 3-term AP. 

* **Length 5 can be avoided.** Davis–Entringer–Graham–Simmons constructed a permutation of the positive integers with **no** 5-term arithmetic progression as a subsequence. 

* **Length 4 is the “first unknown case”.** The same line of work explicitly states that the 4-term version “remains open”. 

### Partial results for length 4

Even though the full question is open, people can avoid many 4-term progressions by putting extra restrictions:

* You *can* build a permutation with **no 4-term AP whose common difference is odd**. 
* More generally, for each (k\ge 1), there are permutations where **every** 4-term AP that appears has common difference divisible by (2^k) [[nomath]](so you avoid all 4-term APs with common difference *not* divisible by $2^k$)[[/nomath]]. 

Also, there is a related “two-sided” variant [[nomath]](indices $\ldots,-2,-1,0,1,2,\ldots$)[[/nomath]]: there exists a **doubly infinite** permutation of the positive integers that avoids monotone 4-term APs. But that does **not** settle the usual one-sided permutation of (\mathbb N). 

So, for your exact question [[nomath]](one-sided permutation of $\mathbb N$)[[/nomath]]: **still open**. ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/196 "
  
    Erdős Problem #196
  
"
