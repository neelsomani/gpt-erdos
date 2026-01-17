Not known in full.

What people study is usually the very close sum
[
\sum_{s_{k+1}\le x}(s_{k+1}-s_k)^\gamma .
]
Erdős proved an asymptotic (\sim B(\gamma),x) for (0\le \gamma\le 2), and later work pushed the range much higher. The current best published range I can find is

[
\sum_{s_{k+1}\le x}(s_{k+1}-s_k)^\gamma \sim B(\gamma),x
\quad\text{for }0\le \gamma<3.75,
]
proved by Tsz Ho Chan (2023). 

So in particular, your limit **does exist** for all (\alpha) in the range (0\le \alpha<3.75) [[nomath]](up to the tiny “last gap” boundary issue coming from using $s_n\le x$ instead of $s_{n+1}\le x$; in that range this does not affect the limit)[[/nomath]]. 

For larger (\alpha), it is **conjectured** that the same kind of limit should exist for every (\alpha>0), but this is open. Filaseta formulates exactly this as a conjecture [[nomath]](“for every $\rho>0$ there is a $B(\rho)$ so that the asymptotic holds”)[[/nomath]] and explains it is equivalent to a short–interval conjecture: for every (\varepsilon>0), every large $x$ has a squarefree number in ((x,x+x^\varepsilon]). 
That short–interval statement is only known for (\varepsilon>1/5) (in the same paper he cites work with Trifonov), so the “all (\alpha)” version is not proved. 

One more useful detail: the expected constant has an explicit “gap distribution” form
[
B(\gamma)=\sum_{h\ge1} h^\gamma,\alpha(h),
]
where (\alpha(h)) is the asymptotic density of gaps of size $h$. 
This series converges very fast [[nomath]](so the *candidate* limit is finite for every fixed $\gamma$)[[/nomath]], but proving the asymptotic for large (\gamma) needs strong control of very large gaps, and that is exactly where the open short–interval problem shows up. 
