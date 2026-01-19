This is **open** in general.

* Erdős originally asked the stronger version with **$B=A$**, i.e. whether an additive basis (A={a_k}) of order $2$ must satisfy that (\lim_{k\to\infty} a_k/k^2) **fails to exist**. That stronger statement is **false**: Cassels constructed a basis (C={c_n}) of order $2$ with
  [
  c_n=\lambda n^2+O(n),
  ]
  so in particular (\lim_{n\to\infty} c_n/n^2=\lambda) exists. 

* Your question is the **Erdős–Graham** variant: given *any* order‑2 basis (A\subset\mathbb N), must there be a **subbasis** (B\subseteq A) for which (\lim b_k/k^2) does not exist? This is listed as **Erdős Problem #326** and is currently regarded as **unresolved**. ([Erdős Problems][1])

A bit of context that may help interpret the question:

* If the limit (\lim_{k\to\infty} b_k/k^2) **does** exist for a basis $B$, that limit is often called an **additive eigenvalue** [[nomath]](order $2$ case)[[/nomath]] in the “additive spectrum” literature. Cassels’s construction shows such eigenvalues occur for order $2$. 
* There are general results about how eigenvalues behave under passing to **supersequences** (adding elements), e.g. if (\alpha) is an eigenvalue then all smaller (\beta<\alpha) can be achieved by adjoining elements, implying the additive spectrum is an interval. But those tools don’t directly address the **subsequence/subset** direction that your question asks about. 

So the best current answer is:

**No proof is known that such a $B$ must exist for every order‑2 basis $A$, and no counterexample is known either; the problem remains open.** ([Erdős Problems][1])

[1]: https://www.erdosproblems.com/326 "
  
    Erdős Problem #326
  
"
