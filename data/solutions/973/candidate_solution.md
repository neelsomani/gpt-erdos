I don’t know of a definitive yes/no answer to **this exact formulation** [[nomath]](with the **shifted window** $k=2,\dots,n+1$, the **fixed term** $z_1=1$, and the **outside-the-unit-disk** constraint $|z_i|\ge 1$)[[/nomath]]. It sits right in the family of classical “pure power sum” problems of Turán/Chowla/Erdős–Atkinson, but the standard results in that area don’t directly settle your variant.

Here is what *is* known nearby, and why it doesn’t immediately resolve your question:

## Closely related problems that are known or discussed

### 1) The unshifted window ({1,2,\dots,n}): a **positive lower bound** exists

If one looks at
[
S_k=\sum_{i=1}^n z_i^k,
\qquad z_1=1,
]
and considers (\max_{1\le k\le n}|S_k|), then there are classical results showing you **cannot make all these sums tiny**: Atkinson proved a universal lower bound (>1/3), and Biró improved the constant (in the “Turán conjecture” setting) to a universal bound (>1/2). ([Renyi Users][1])

However, this does **not** automatically imply anything about the *shifted* block ({2,3,\dots,n+1}): it could still happen that the “large” sum forced by Atkinson/Biró always occurs at $k=1$, while (k\ge 2) are much smaller.

### 2) Chowla’s “small power sums” question with (|z_i|\le 1): still open in general, but a restricted case is doable

Hayman’s *Research Problems in Function Theory* records (as Problem 7.3) Chowla’s question: for (|z_i|\le 1), can one make (\max_{2\le k\le n+1}|S_k|) exponentially small in $n$? ([arXiv][2])

And crucially, Hayman notes an Erdős remark: **if you additionally assume (z_1=1)** [[nomath]](with $|z_i|\le 1$ for the rest)[[/nomath]], then such an inequality *can* be satisfied via a construction of Turán. ([arXiv][2])

But your problem flips the modulus condition to (|z_i|\ge 1), so that “inside the unit disk” construction does not transfer.

## Why your (|z_i|\ge 1) variant is genuinely different

A key reason the (|z_i|\le 1) world is more permissive is that shrinking moduli makes higher powers small “for free.” With (|z_i|\ge 1), higher powers do **not** shrink; if anything, radii (>1) amplify higher powers and make uniform smallness across (k=2,\dots,n+1) harder unless there is extremely delicate cancellation.

So the known “positive” construction mentioned by Erdős/Turán for the (|z_i|\le 1) setting ([arXiv][2]) does not immediately give a construction for your (|z_i|\ge 1) setting.

## Bottom line

* The classical results that **force a large power sum** (Atkinson/Biró) apply to the **unshifted range** (k=1,\dots,n), not to the shifted range (k=2,\dots,n+1). ([Renyi Users][1])
* The place where **exponentially small** power sums are known to be achievable in this literature is under the **(|z_i|\le 1)** hypothesis (and even then, the situation depends on additional constraints), not under (|z_i|\ge 1). ([arXiv][2])

So, with the references above in view, I can’t responsibly claim “yes” or “no” as a known theorem for your exact statement. The question looks like a natural “dual” variant of Chowla/Turán-type problems, but it is not settled by the standard nearby results.

If you want, I can also outline a couple of standard routes one might try (Newton sums / polynomials with prescribed power sums; or Turán-type linear combination inequalities) and where the (|z_i|\ge 1), (z_1=1) constraints become the sticking point—but that would be more about *approach* than about a definitive resolution.

[1]: https://users.renyi.hu/~biroand/pdfs/Turan1.pdf "https://users.renyi.hu/~biroand/pdfs/Turan1.pdf"
[2]: https://arxiv.org/pdf/1809.07200 "https://arxiv.org/pdf/1809.07200"
