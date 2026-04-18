# GPT-5.4 Pro Verification for Problem 552

Verdict: False

---

The proof is **not correct**.

Key problems:

1. **Off-by-one error in the Ramsey reformulation.**  
   On \(m\) vertices, \(\overline G\) contains \(S_n\) iff some vertex has complement degree at least \(n\), i.e. some vertex of \(G\) has degree at most \(m-1-n\). The proof states \(\delta(G)\le m-n\), which is wrong.

2. **The upper-bound algebra is mis-solved.**  
   From
   \[
   k>\phi(n+k)=\frac{1+\sqrt{4n+4k-3}}2
   \]
   one gets
   \[
   (k-1)^2>n,
   \]
   so \(k\) is about \(\sqrt n+1\), not about \(\sqrt n+\tfrac12\). The displayed upper bound is therefore not derived correctly.

3. **The claimed lower-bound construction does not exist.**  
   The proof asserts that for prime powers \(q\) there is a \(C_4\)-free \((q+1)\)-regular graph on \(q^2+q+1\) vertices coming from a projective plane/polarity graph. This is false.  
   - Projective-plane “point graphs” are not \(C_4\)-free in the claimed way.  
   - Polarity graphs on \(q^2+q+1\) vertices are not \((q+1)\)-regular in general.  
   - In fact, for \(q=2\) this would require a 3-regular graph on 7 vertices, impossible by parity.

4. **A concrete contradiction to the proof’s lower bound.**  
   The proof claims for \(n=q^2\) that
   \[
   R(C_4,S_n)\ge n+\sqrt n+2.
   \]
   Taking \(q=2\), this gives \(R(C_4,S_4)\ge 8\). But actually:
   - \(C_6\) is \(C_4\)-free and \(\overline{C_6}\) has maximum degree \(3<4\), so \(R(C_4,S_4)>6\).
   - On 7 vertices, avoiding \(S_4\) in the complement would require \(\delta(G)\ge 3\). Then
     \[
     \sum_v \binom{d(v)}2 \ge 7\binom32=21=\binom72,
     \]
     so equality would have to hold, forcing all degrees to be 3, impossible on 7 vertices. Hence \(R(C_4,S_4)\le 7\).
   Therefore \(R(C_4,S_4)=7\), so the proof’s claimed bound \(R(C_4,S_4)\ge 8\) is false.

5. **The final “prime-power gap” argument is not a proof.**  
   It repeatedly argues from “tight constructions are unavailable” to conclusions about Ramsey numbers. Lack of known constructions does **not** imply nonexistence, so this part is logically invalid.

Because the proof uses a nonexistent construction and reaches a false numerical conclusion, it is not merely missing details; it is fundamentally wrong.

Verdict: False
