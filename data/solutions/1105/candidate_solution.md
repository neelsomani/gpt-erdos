Yes to both — and in fact both quantities are known **exactly** (not just asymptotically).

## Cycles

The asymptotic
[
\mathrm{AR}(n,C_k)=\left(\frac{k-2}{2}+\frac{1}{k-1}\right)n+O(1)
]
is true [[nomath]](for each fixed $k$)[[/nomath]], and the old Erdős–Simonovits–Sós conjecture is in fact resolved with an **exact formula** due to Montellano-Ballesteros and Neumann-Lara (2005). One convenient statement is:

Let (n=q(k-1)+r) with (0\le r\le k-2). Then
[
\mathrm{AR}(n,C_k)
=

q\binom{k-1}{2}+\binom{r}{2}+\left\lceil\frac{n}{k-1}\right\rceil-1.
]


From this exact expression you immediately get
[
\mathrm{AR}(n,C_k)=\left(\frac{k-2}{2}+\frac{1}{k-1}\right)n+O_k(1),
]
since (r\in{0,1,\dots,k-2}) only affects the value by a bounded amount depending on $k$. 

## Paths

For paths, the exact value for (n\ge k\ge 5) is also known, and it matches your formula precisely. Long-Tu Yuan proved:

Let (P_k) be the path on $k$ vertices and (\ell=\left\lfloor\frac{k-1}{2}\right\rfloor). If (n\ge k\ge 5), then
[
\mathrm{AR}(n,P_k)
=

\max\\{
\binom{k-2}{2}+1,
\binom{\ell-1}{2}+(\ell-1)(n-\ell+1)+\epsilon
\\},
]
where (\epsilon=1) if $k$ is odd and (\epsilon=2) if $k$ is even. 

Moreover, the paper explicitly describes the two extremal constructions corresponding to the two terms in the maximum [[nomath]](the “rainbow $K_{k-2}$ + one extra color” construction, and the “choose $X$ of size $\lfloor (k-3)/2\rfloor$ and color all edges incident to $X$ distinctly, with the rest using 1 or 2 colors depending on parity” construction)[[/nomath]]. 
