What you are asking is exactly the question of whether **weird numbers** can have arbitrarily large “abundancy index.”

* Call $n$ **pseudoperfect/semiperfect** if it is the sum of **distinct proper divisors** of $n$.
* Call $n$ **weird** if it is **abundant** but **not** pseudoperfect (so it is *not* a distinct-sum of proper divisors). 

If we write the **abundancy index** as
[
I(n)=\frac{\sigma(n)}{n},
]
then your question:

> Does there exist an absolute (C>0) such that [[nomath]](\sigma$n$>Cn\Rightarrow n)[[/nomath]] is a distinct sum of proper divisors?

is equivalent to:

> Is $I(n)$ **bounded above** on weird numbers?

Because if weird numbers can have $I(n)$ arbitrarily large, then for every fixed $C$ there would be a weird $n$ with [[nomath]](\sigma$n$>Cn)[[/nomath]], contradicting the desired property.

### Status: open

Benkoski and Erdős explicitly raised this in their 1974 paper, stating they could not decide “whether $a(n)/n$ [[nomath]](i.e. $\sigma(n)/n$)[[/nomath]] could be arbitrarily large for weird $n$.” 

It remains listed as an open Erdős problem (Erdős Problem #825, (25). ([Erdős Problems][1])

### What is known (bounds / evidence)

* You must have (C>2), since pseudoperfect (\Rightarrow \sigma(n)\ge 2n), and in fact the smallest weird number is (70) with
  [
  I(70)=\frac{\sigma(70)}{70}=\frac{144}{70}\approx 2.0571,
  ]
  so any valid $C$ must exceed at least this value. ([Erdős Problems][1])
* Computations suggest weird numbers have **small** abundancy index: OEIS records successive “record-holder” weird numbers [[nomath]](up to $10^{10}$)[[/nomath]] whose abundancy indices only rise to about (2.0716\ldots). ([OEIS][2])
* There is a useful **conditional** observation (attributed there to Weisenberg): if a weird number has abundancy index (\ge 4), then it has an **odd weird divisor**. Hence, **if no odd weird numbers exist**, then every weird number would satisfy (I(n)<4), and your question would have a “yes” answer with (C=4). But the existence of odd weird numbers is itself open. ([Erdős Problems][1])

### Bottom line

No unconditional absolute constant $C$ is known. The problem is open and is commonly phrased as:

> Can (\sigma(n)/n) be arbitrarily large for weird numbers?

which is exactly the obstruction to your statement. 

[1]: https://www.erdosproblems.com/825 "
  
    Erdős Problem #825
  
"
[2]: https://oeis.org/A330244 "A330244 - OEIS"
