/- Courtesy of JakeMallen; generated with Aristotle and Gemini 3.0 Flash -/

import Mathlib

set_option maxHeartbeats 800000

open Filter Topology Classical

open scoped BigOperators

/- Strictly increasing sequence n₁ < n₂ < ⋯ indexed by naturals. -/
variable {n : ℕ → ℕ} (hmono : StrictMono n) (hnpos : ∀ i, 0 < n i)

/- The space of choices for residues modulo n i. -/
def Choice (n : ℕ → ℕ) := ∀ i : ℕ, ZMod (n i)

/- The set of integers m such that m mod n i avoids a i for all i < k. -/
def avoidPrefix (n : ℕ → ℕ) (a : Choice n) (k : ℕ) : Set ℤ :=
  {m | ∀ i : ℕ, i < k → (m : ZMod (n i)) ≠ a i}

/- The set of integers m such that m mod n i avoids a i for all i. -/
def avoidAll (n : ℕ → ℕ) (a : Choice n) : Set ℤ :=
  {m | ∀ i : ℕ, (m : ZMod (n i)) ≠ a i}

/-- Two-sided natural density sequence on ℤ using [-N,N]. -/
noncomputable def densSeqZ (S : Set ℤ) (N : ℕ) : ℝ :=
  (((Finset.Icc (-(N : ℤ)) (N : ℤ)).filter (· ∈ S)).card : ℝ) / (2 * (N : ℝ) + 1)

/-
Period of the first k moduli.
-/
def period (n : ℕ → ℕ) (k : ℕ) : ℕ := (Finset.range k).lcm n

/- The period of the first k moduli is positive. -/
lemma period_pos (n : ℕ → ℕ) (hnpos : ∀ i, 0 < n i) (k : ℕ) : 0 < period n k := by
  exact Nat.pos_of_ne_zero ( mt Finset.lcm_eq_zero_iff.mp ( by intros h; obtain ⟨ i, hi ⟩ := h; specialize hnpos i; aesop ) )

/-
Residues avoiding congruences modulo period.
-/
def avoidPrefixMod (n : ℕ → ℕ) (hnpos : ∀ i, 0 < n i) (a : Choice n) (k : ℕ) : Finset (ZMod (period n k)) :=
  let L := period n k
  haveI : NeZero L := ⟨ne_of_gt (period_pos n hnpos k)⟩
  Finset.univ.filter fun x => ∀ i, (hi : i < k) →
    let d : ℕ := n i
    have hd : d ∣ L := Finset.dvd_lcm (Finset.mem_range.mpr hi)
    ZMod.castHom (show d ∣ L from hd) (ZMod d) x ≠ a i

/-- Two-sided natural density exists and equals d. -/
def HasIntDensity (S : Set ℤ) (d : ℝ) : Prop :=
  Tendsto (densSeqZ S) atTop (𝓝 d)

/- The hypothesis of Erdos Problem 281. -/
def Erdos281Hyp (n : ℕ → ℕ) (hmono : StrictMono n) (hnpos : ∀ i, 0 < n i) : Prop :=
  ∀ a : Choice n, HasIntDensity (avoidAll n a) 0

/- The conclusion of Erdos Problem 281. -/
def Erdos281Concl (n : ℕ → ℕ) (hmono : StrictMono n) (hnpos : ∀ i, 0 < n i) : Prop :=
  ∀ ε : ℝ, 0 < ε →
    ∃ k : ℕ, ∀ a : Choice n,
      ∃ d : ℝ, HasIntDensity (avoidPrefix n a k) d ∧ d < ε

/-
The profinite integers ZHat.
-/
def ZHat := { x : ∀ k : ℕ+, ZMod k | ∀ (m k : ℕ+) (h : m ∣ k), ZMod.castHom (show (m : ℕ) ∣ (k : ℕ) from PNat.dvd_iff.mp h) (ZMod m) (x k) = x m }

/-
Coercion from ZHat to the product of ZMod k.
-/
instance : Coe ZHat (∀ k : ℕ+, ZMod k) := ⟨Subtype.val⟩

/-
Topology on ZHat.
-/
instance : TopologicalSpace ZHat := TopologicalSpace.induced Subtype.val inferInstance

/-
Zero element of ZHat.
-/
instance : Zero ZHat := ⟨⟨0, by
  exact fun m k h => by simp +decide ;⟩⟩

/-
Addition and negation on ZHat.
-/
instance : Add ZHat := ⟨fun x y => ⟨x.1 + y.1, by
  intros m k h
  simp only [Pi.add_apply, map_add]
  rw [x.2 m k h, y.2 m k h]⟩⟩

instance : Neg ZHat := ⟨fun x => ⟨-x.1, by
  intros m k h
  simp only [Pi.neg_apply, map_neg]
  rw [x.2 m k h]⟩⟩

/-
Subtraction on ZHat.
-/
instance : Sub ZHat := ⟨fun x y => ⟨x.1 - y.1, by
  intros m k h
  simp only [Pi.sub_apply, map_sub]
  rw [x.2 m k h, y.2 m k h]⟩⟩

/-
Scalar multiplication on ZHat.
-/
instance : SMul ℕ ZHat := ⟨fun n x => ⟨n • x.1, by
  intros m k h
  simp only [Pi.smul_apply, map_nsmul]
  rw [x.2 m k h]⟩⟩

instance : SMul ℤ ZHat := ⟨fun n x => ⟨n • x.1, by
  intros m k h
  simp only [Pi.smul_apply, map_zsmul]
  rw [x.2 m k h]⟩⟩

/-
Additive commutative group structure on ZHat.
-/
instance : AddCommGroup ZHat :=
  { (inferInstance : Add ZHat), (inferInstance : Neg ZHat), (inferInstance : Zero ZHat) with
    sub := fun x y => ⟨x.1 - y.1, by
      intros m k h
      simp only [Pi.sub_apply, map_sub]
      rw [x.2 m k h, y.2 m k h]⟩
    nsmul := fun n x => ⟨n • x.1, by
      intros m k h
      simp only [Pi.smul_apply, map_nsmul]
      rw [x.2 m k h]⟩
    zsmul := fun n x => ⟨n • x.1, by
      intros m k h
      simp only [Pi.smul_apply, map_zsmul]
      rw [x.2 m k h]⟩
    add_assoc := by
      exact fun x y z => Subtype.ext <| add_assoc _ _ _
    zero_add := by
      simp +zetaDelta at *;
      exact fun a ha => Subtype.ext <| zero_add a
    add_zero := by
      simp +zetaDelta at *;
      exact fun a ha => Subtype.ext <| add_zero a
    neg_add_cancel := by
      simp +zetaDelta at *;
      intro a ha;
      exact Subtype.ext <| funext fun k => neg_add_cancel _
    add_comm := by
      exact fun a b => Subtype.ext <| funext fun k => add_comm _ _
    nsmul_zero := by
      aesop
    nsmul_succ := by
      intros n a; ext k; simp [add_mul]; rfl
    zsmul_zero' := by
      intros a; ext k; simp; rfl
    zsmul_succ' := by
      intros n a; ext k; simp [Nat.succ_eq_add_one, add_smul]; rfl
    zsmul_neg' := by
      simp +decide [ Int.negSucc_eq ];
      intro n a ha; congr; ext k; simp +decide [ add_mul, add_comm ] ;
    sub_eq_add_neg := by
      -- By definition of subtraction in ZHat, we have a - b = a + (-b).
      simp [sub_eq_add_neg];
      aesop }

/-
Compactness of ZHat.
-/
instance : CompactSpace ZHat := ⟨by
convert isCompact_univ_iff.mpr ?_;
-- Since `ZMod k` is finite, it is compact. The product of compact spaces is compact by Tychonoff's theorem.
have h_compact : IsCompact (Set.pi Set.univ fun k : ℕ+ => Set.univ : Set (∀ k : ℕ+, ZMod k)) := by
  exact isCompact_univ_pi fun k => isCompact_univ;
refine' isCompact_iff_compactSpace.mp _;
convert h_compact.of_isClosed_subset _ _;
· simp +decide [ ZHat ];
  simp +decide only [Set.setOf_forall];
  refine' isClosed_iInter fun i => isClosed_iInter fun j => isClosed_iInter fun hij => isClosed_eq _ _;
  · fun_prop (disch := solve_by_elim);
  · exact continuous_apply i;
· aesop_cat⟩

/-
Hausdorff property of ZHat.
-/
instance : T2Space ZHat := inferInstance

/-
Continuous addition on ZHat.
-/
instance : ContinuousAdd ZHat := ⟨by
-- The projection maps are continuous, and the addition on each component is continuous. Therefore, the sum of the projections is continuous.
have h_proj_cont : ∀ k : ℕ+, Continuous (fun p : ZHat × ZHat => p.1.val k + p.2.val k) := by
  exact fun k => Continuous.add ( continuous_apply k |> Continuous.comp <| continuous_subtype_val.comp continuous_fst ) ( continuous_apply k |> Continuous.comp <| continuous_subtype_val.comp continuous_snd );
refine' Continuous.subtype_mk _ _;
exact continuous_pi_iff.mpr fun k => h_proj_cont k⟩

/-
Continuous negation on ZHat.
-/
instance : ContinuousNeg ZHat := ⟨by
  have h_proj_cont : ∀ k : ℕ+, Continuous (fun p : ZHat => -p.val k) := by
    exact fun k => Continuous.neg (Continuous.comp (continuous_apply k) continuous_subtype_val)
  refine' Continuous.subtype_mk _ _
  exact continuous_pi_iff.mpr fun k => h_proj_cont k⟩

/-
Topological group structure on ZHat.
-/
instance : IsTopologicalAddGroup ZHat := ⟨⟩

/-
Measurable structure of ZHat.
-/
instance : MeasurableSpace ZHat := borel ZHat

instance : BorelSpace ZHat := ⟨rfl⟩

/-
Normalized Haar measure on ZHat.
-/
noncomputable def haar : MeasureTheory.Measure ZHat :=
  let K : TopologicalSpace.PositiveCompacts ZHat :=
    { carrier := Set.univ
      isCompact' := isCompact_univ
      interior_nonempty' := by
        simp +decide [ Set.Nonempty ] }
  let μ := MeasureTheory.Measure.addHaarMeasure K
  (μ Set.univ)⁻¹ • μ

instance : MeasureTheory.IsFiniteMeasure haar := by
  unfold haar; infer_instance

/-
Projections and cylinders on ZHat.
-/
def proj (n : ℕ) [NeZero n] (x : ZHat) : ZMod n :=
  x.val ⟨n, NeZero.pos n⟩

def cylinder (n : ℕ) [NeZero n] (a : ZMod n) : Set ZHat :=
  {x | proj n x = a}

/-
Definitions of Ck and C.
-/
def Ck (n : ℕ → ℕ) (hnpos : ∀ i, 0 < n i) (a : Choice n) (k : ℕ) : Set ZHat :=
  ⋂ (i : ℕ) (_ : i < k),
    haveI : NeZero (n i) := ⟨ne_of_gt (hnpos i)⟩
    (cylinder (n i) (a i))ᶜ

def C (n : ℕ → ℕ) (hnpos : ∀ i, 0 < n i) (a : Choice n) : Set ZHat :=
  ⋂ (k : ℕ), Ck n hnpos a k


/-
avoidPrefix is periodic.
-/
lemma avoidPrefix_periodic (n : ℕ → ℕ) (hnpos : ∀ i, 0 < n i) (a : Choice n) (k : ℕ) :
  Function.Periodic (fun m : ℤ => m ∈ avoidPrefix n a k) (period n k : ℤ) := by
    intro m; simp +decide [ avoidPrefix ] ;
    -- Since period n k is a multiple of each n i for i < k, adding period n k to m does not change the residue modulo n i.
    have h_period_mod : ∀ i < k, (m + period n k : ZMod (n i)) = m := by
      intros i hi
      have h_div : n i ∣ period n k := by
        exact Finset.dvd_lcm ( Finset.mem_range.mpr hi );
      cases h_div ; aesop;
    grind


/-
The set Ck is the preimage of the set of avoiding residues modulo the period.
-/
lemma Ck_eq_preimage (n : ℕ → ℕ) (hnpos : ∀ i, 0 < n i) (a : Choice n) (k : ℕ) :
  Ck n hnpos a k = {x : ZHat | @proj (period n k) ⟨ne_of_gt (period_pos n hnpos k)⟩ x ∈ avoidPrefixMod n hnpos a k} := by
    unfold Ck avoidPrefixMod;
    unfold proj cylinder;
    ext; simp [proj];
    congr! 3;
    rename_i i hi;
    have h_cast : ∀ (m k : ℕ+) (h : m ∣ k), (ZMod.castHom (show (m : ℕ) ∣ (k : ℕ) from PNat.dvd_iff.mp h) (ZMod m) (‹ZHat›.val k)) = ‹ZHat›.val m := by
                                                            exact fun m k h => Subtype.property ‹ZHat› m k h;
    rw [ ← h_cast ⟨ n i, hnpos i ⟩ ⟨ period n k, period_pos n hnpos k ⟩ ];
    all_goals norm_num [ PNat.dvd_iff ];
    exact Finset.dvd_lcm ( Finset.mem_range.mpr hi )

/-
A periodic set has a natural density equal to the proportion of elements in one period.
-/
lemma dens_periodic (S : Set ℤ) (L : ℕ) (hL : 0 < L) (hper : ∀ n, n ∈ S ↔ n + L ∈ S) :
  HasIntDensity S (((Finset.range L).filter (fun x : ℕ => (x : ℤ) ∈ S)).card / L) := by
  -- The density sequence converges to the average value over one period.
    -- Let's define the set of integers in $S$ within the interval $[-N, N]$ and show that its density tends to zero as $N$ tends to infinity.
    have h_density : Filter.Tendsto (fun N : ℕ => (((Finset.Icc (-(N : ℤ)) (N : ℤ)).filter (· ∈ S)).card : ℝ) / (2 * (N : ℝ) + 1)) Filter.atTop (𝓝 ((Finset.filter (fun x : ℕ => (x : ℤ) ∈ S) (Finset.range L)).card / (L : ℝ))) := by
      -- By the properties of the floor function and the periodicity of $S$, we can show that the number of elements in $S$ within $[-N, N]$ is asymptotically equal to $(2N + 1) \cdot \frac{|S \cap \{0, 1, ..., L-1\}|}{L}$.
      have h_floor : ∀ N : ℕ, (((Finset.Icc (-(N : ℤ)) (N : ℤ)).filter (· ∈ S)).card : ℝ) ≥ (2 * N + 1) * ((Finset.filter (fun x : ℕ => (x : ℤ) ∈ S) (Finset.range L)).card : ℝ) / L - L ∧ (((Finset.Icc (-(N : ℤ)) (N : ℤ)).filter (· ∈ S)).card : ℝ) ≤ (2 * N + 1) * ((Finset.filter (fun x : ℕ => (x : ℤ) ∈ S) (Finset.range L)).card : ℝ) / L + L := by
        intro N
        have h_card : (((Finset.Icc (-(N : ℤ)) (N : ℤ)).filter (· ∈ S)).card : ℝ) = ∑ x ∈ Finset.range L, (Finset.filter (fun y : ℤ => y ∈ S) (Finset.Icc (-(N : ℤ)) (N : ℤ) ∩ Finset.image (fun k : ℤ => x + k * L) (Finset.Icc (-((N + x) / L) : ℤ) ((N - x) / L)))).card := by
          rw [ ← Finset.card_biUnion ];
          · congr with x ; norm_num;
            constructor;
            · intro hx
              use Int.toNat (x % L);
              norm_num [ Int.emod_nonneg _ ( by positivity : ( L : ℤ ) ≠ 0 ), Int.emod_lt_of_pos _ ( by positivity : ( L : ℤ ) > 0 ) ];
              exact ⟨ ⟨ hx.1, ⟨ x / L, ⟨ by nlinarith [ Int.emod_add_mul_ediv x L, Int.emod_nonneg x ( by positivity : ( L : ℤ ) ≠ 0 ), Int.emod_lt_of_pos x ( by positivity : ( L : ℤ ) > 0 ), Int.mul_ediv_add_emod ( N + x % L ) L, Int.emod_nonneg ( N + x % L ) ( by positivity : ( L : ℤ ) ≠ 0 ), Int.emod_lt_of_pos ( N + x % L ) ( by positivity : ( L : ℤ ) > 0 ) ], by nlinarith [ Int.emod_add_mul_ediv x L, Int.emod_nonneg x ( by positivity : ( L : ℤ ) ≠ 0 ), Int.emod_lt_of_pos x ( by positivity : ( L : ℤ ) > 0 ), Int.mul_ediv_add_emod ( N - x % L ) L, Int.emod_nonneg ( N - x % L ) ( by positivity : ( L : ℤ ) ≠ 0 ), Int.emod_lt_of_pos ( N - x % L ) ( by positivity : ( L : ℤ ) > 0 ) ] ⟩, by linarith [ Int.emod_add_mul_ediv x L ] ⟩ ⟩, hx.2 ⟩;
            · tauto;
          · intros x hx y hy hxy; simp +contextual [ Finset.disjoint_left ] at *;
            intro a ha₁ ha₂ b hb₁ hb₂ hab hS c hc₁ hc₂ hbc; contrapose! hxy; nlinarith [ show b = c by nlinarith ] ;
        -- Since $S$ is periodic with period $L$, the number of elements in $S$ within each interval $[x + kL, x + (k+1)L)$ is the same.
        have h_periodic : ∀ x ∈ Finset.range L, (Finset.filter (fun y : ℤ => y ∈ S) (Finset.Icc (-(N : ℤ)) (N : ℤ) ∩ Finset.image (fun k : ℤ => x + k * L) (Finset.Icc (-((N + x) / L) : ℤ) ((N - x) / L)))).card = if (x : ℤ) ∈ S then (Finset.Icc (-((N + x) / L) : ℤ) ((N - x) / L)).card else 0 := by
          intro x hx
          have h_periodic : ∀ k : ℤ, (x + k * L : ℤ) ∈ S ↔ (x : ℤ) ∈ S := by
            intro k; induction' k using Int.induction_on with n ihn n ihn; all_goals norm_num at *;
            · rw [ add_mul, one_mul, ← add_assoc, ← hper ] ; tauto;
            · grind +ring;
          split_ifs <;> simp +decide;
          · rw [ show ( Finset.Icc ( - ( N : ℤ ) ) ( N : ℤ ) ∩ Finset.image ( fun k : ℤ => ( x : ℤ ) + k * L ) ( Finset.Icc ( - ( ( N + x ) / L : ℤ ) ) ( ( N - x ) / L : ℤ ) ) ) = Finset.image ( fun k : ℤ => ( x : ℤ ) + k * L ) ( Finset.Icc ( - ( ( N + x ) / L : ℤ ) ) ( ( N - x ) / L : ℤ ) ) by
              ext a; simp; rintro k hk₁ hk₂ rfl; constructor
              · have hL_pos : (0 : ℤ) < L := by positivity
                have h_le : -(N + x : ℤ) ≤ k * L :=
                  calc
                    -(N + x : ℤ) ≤ -((N + x : ℤ) / L * L) := by
                      have := Int.ediv_mul_le (N + x : ℤ) hL_pos.ne'
                      linarith
                    _ = -((N + x : ℤ) / L) * L := by ring
                    _ ≤ k * L := Int.mul_le_mul_of_nonneg_right hk₁ (by positivity)
                linarith
              · have hL_pos : (0 : ℤ) < L := by positivity
                have h_le : k * L ≤ (N : ℤ) - x :=
                  calc
                    k * L ≤ ((N : ℤ) - x) / L * L := Int.mul_le_mul_of_nonneg_right hk₂ (by positivity)
                    _ ≤ (N : ℤ) - x := Int.ediv_mul_le ((N : ℤ) - x) hL_pos.ne'
                linarith ];
            · rw [ Finset.filter_true_of_mem ] <;> norm_num [ Finset.card_image_of_injective, Function.Injective, hL.ne' ];
              rintro _ k hk₁ hk₂ rfl; exact h_periodic k |>.2 ‹_›;
          · grind +ring;
        rw [ h_card, Finset.sum_congr rfl h_periodic ];
        norm_num [ Finset.sum_ite ];
        -- By simplifying the expression inside the sum, we can see that it is bounded by $(2N + 1)/L + 1$.
        have h_bound : ∀ x ∈ Finset.range L, ((N - x) / L + 1 + (N + x) / L : ℤ).toNat ≤ (2 * N + 1 : ℝ) / L + 1 ∧ ((N - x) / L + 1 + (N + x) / L : ℤ).toNat ≥ (2 * N + 1 : ℝ) / L - 1 := by
          intro x hx; rw [ div_add_one, ge_iff_le, div_sub_one, div_le_iff₀, le_div_iff₀ ] <;> norm_cast ; ring_nf ;
          · norm_num [ Int.subNatNat_eq_coe ];
            constructor <;> cases max_cases ( 1 + ( N - x : ℤ ) / L + ( N + x : ℤ ) / L ) 0 <;> nlinarith [ Int.mul_ediv_add_emod ( N - x ) L, Int.emod_nonneg ( N - x ) ( by positivity : ( L : ℤ ) ≠ 0 ), Int.emod_lt_of_pos ( N - x ) ( by positivity : ( L : ℤ ) > 0 ), Int.mul_ediv_add_emod ( N + x ) L, Int.emod_nonneg ( N + x ) ( by positivity : ( L : ℤ ) ≠ 0 ), Int.emod_lt_of_pos ( N + x ) ( by positivity : ( L : ℤ ) > 0 ), Int.toNat_of_nonneg ( by nlinarith [ Int.mul_ediv_add_emod ( N - x ) L, Int.emod_nonneg ( N - x ) ( by positivity : ( L : ℤ ) ≠ 0 ), Int.emod_lt_of_pos ( N - x ) ( by positivity : ( L : ℤ ) > 0 ), Int.mul_ediv_add_emod ( N + x ) L, Int.emod_nonneg ( N + x ) ( by positivity : ( L : ℤ ) ≠ 0 ), Int.emod_lt_of_pos ( N + x ) ( by positivity : ( L : ℤ ) > 0 ) ] : ( 0 : ℤ ) ≤ 1 + ( N - x : ℤ ) / L + ( N + x : ℤ ) / L ) ];
          · linarith;
          · linarith;
        have := Finset.sum_le_sum fun x ( hx : x ∈ Finset.filter ( fun x : ℕ => ( x : ℤ ) ∈ S ) ( Finset.range L ) ) => h_bound x ( Finset.mem_filter.mp hx |>.1 ) |>.2; ( have := Finset.sum_le_sum fun x ( hx : x ∈ Finset.filter ( fun x : ℕ => ( x : ℤ ) ∈ S ) ( Finset.range L ) ) => h_bound x ( Finset.mem_filter.mp hx |>.1 ) |>.1; ( norm_num [ Finset.sum_add_distrib, Finset.mul_sum _ _ _, Finset.sum_div ] at *; ) );
        constructor <;> ring_nf at * <;> nlinarith [ inv_mul_cancel_left₀ ( by positivity : ( L : ℝ ) ≠ 0 ) ( Finset.card ( Finset.filter ( fun x : ℕ => ( x : ℤ ) ∈ S ) ( Finset.range L ) ) : ℝ ), show ( Finset.card ( Finset.filter ( fun x : ℕ => ( x : ℤ ) ∈ S ) ( Finset.range L ) ) : ℝ ) ≤ L by exact_mod_cast le_trans ( Finset.card_filter_le _ _ ) ( by norm_num ) ];
      -- By dividing the inequalities from h_floor by (2N + 1), we can bound the density.
      have h_density_bounds : ∀ N : ℕ, N > 0 → (((Finset.Icc (-(N : ℤ)) (N : ℤ)).filter (· ∈ S)).card : ℝ) / (2 * (N : ℝ) + 1) ≥ ((Finset.filter (fun x : ℕ => (x : ℤ) ∈ S) (Finset.range L)).card : ℝ) / (L : ℝ) - L / (2 * (N : ℝ) + 1) ∧ (((Finset.Icc (-(N : ℤ)) (N : ℤ)).filter (· ∈ S)).card : ℝ) / (2 * (N : ℝ) + 1) ≤ ((Finset.filter (fun x : ℕ => (x : ℤ) ∈ S) (Finset.range L)).card : ℝ) / (L : ℝ) + L / (2 * (N : ℝ) + 1) := by
        intro N hN_pos
        specialize h_floor N;
        field_simp;
        constructor <;> nlinarith [ show ( L : ℝ ) > 0 by positivity, mul_div_cancel₀ ( ( 2 * N + 1 : ℝ ) * Finset.card ( Finset.filter ( fun x : ℕ => ( x : ℤ ) ∈ S ) ( Finset.range L ) ) ) ( by positivity : ( L : ℝ ) ≠ 0 ) ];
      rw [ Metric.tendsto_nhds ];
      intro ε hε;
      filter_upwards [ Filter.eventually_gt_atTop ⌈ε⁻¹ * L⌉₊ ] with N hN using abs_lt.mpr ⟨ by linarith [ h_density_bounds N ( by linarith ), show ( L : ℝ ) / ( 2 * N + 1 ) < ε by rw [ div_lt_iff₀ ] <;> nlinarith [ Nat.le_ceil ( ε⁻¹ * L ), mul_inv_cancel₀ ( ne_of_gt hε ), ( by norm_cast : ( ⌈ε⁻¹ * L⌉₊ : ℝ ) + 1 ≤ N ) ] ], by linarith [ h_density_bounds N ( by linarith ), show ( L : ℝ ) / ( 2 * N + 1 ) < ε by rw [ div_lt_iff₀ ] <;> nlinarith [ Nat.le_ceil ( ε⁻¹ * L ), mul_inv_cancel₀ ( ne_of_gt hε ), ( by norm_cast : ( ⌈ε⁻¹ * L⌉₊ : ℝ ) + 1 ≤ N ) ] ] ⟩;
    exact h_density

/-
  The number of avoiding integers in one period equals the number of avoiding residues.
  -/
  lemma card_avoidPrefix_inter_range_eq_card_avoidPrefixMod (n : ℕ → ℕ) (hnpos : ∀ i, 0 < n i) (a : Choice n) (k : ℕ) :
    ((Finset.range (period n k)).filter (fun m : ℕ => (m : ℤ) ∈ avoidPrefix n a k)).card = (avoidPrefixMod n hnpos a k).card := by
      convert congr_arg Finset.card ( show Finset.filter ( fun m : ℕ => ( m : ℤ ) ∈ avoidPrefix n a k ) ( Finset.range ( period n k ) ) = Finset.image ( fun m : ZMod ( period n k ) => m.val ) ( avoidPrefixMod n hnpos a k ) from ?_ ) using 2;
      · rw [ Finset.card_image_of_injective ];
        -- The function m.val is injective because if two elements in ZMod (period n k) have the same value, they must be the same element.
        intro m m' h_eq;
        convert ZMod.val_injective _ h_eq;
        exact ⟨ ne_of_gt ( period_pos n hnpos k ) ⟩;
      · -- To prove equality of finite sets, we show each set is a subset of the other.
        apply Finset.ext
        intro m
        simp [avoidPrefix, avoidPrefixMod];
        constructor <;> intro h;
        · use m;
          norm_num +zetaDelta at *;
          refine' ⟨ _, Nat.mod_eq_of_lt h.1 ⟩;
          intro i hi; specialize h; have := h.2 i hi; simp_all +decide;
          convert h.2 i hi using 1;
          have h_cast : (m : ZMod (period n k)).cast = (m : ZMod (n i)) := by
            have h_div : n i ∣ period n k := by
              exact Finset.dvd_lcm ( Finset.mem_range.mpr hi )
            cases h_div ; aesop;
          rw [ h_cast ];
        · obtain ⟨ x, hx, rfl ⟩ := h;
          refine' ⟨ _, _ ⟩;
          · convert x.val_lt;
            exact ⟨ ne_of_gt ( period_pos n hnpos k ) ⟩;
          · intro i hi; specialize hx i hi; rcases eq_or_ne x 0 with rfl | hx' <;> simp_all +decide;
            have h_cast : (x.val : ZMod (period n k)) = x := by
              convert ZMod.natCast_zmod_val x;
              exact ⟨ ne_of_gt ( period_pos n hnpos k ) ⟩;
            haveI : NeZero (period n k) := ⟨ne_of_gt (period_pos n hnpos k)⟩
            haveI hni : NeZero (n i) := ⟨(hnpos i).ne'⟩
            have h_eq : (x.val : ZMod (n i)) = x.cast := by
              rw [← h_cast]
              rw [ZMod.cast_natCast (Finset.dvd_lcm (Finset.mem_range.mpr hi))]
              rw [ZMod.val_natCast, Nat.mod_eq_of_lt x.val_lt]
            rw [h_eq]; exact hx

/-
The natural density of the avoiding set is the proportion of avoiding residues in one period.
-/
instance : MeasureTheory.Measure.IsAddHaarMeasure haar where
  toIsFiniteMeasureOnCompacts := by unfold haar; infer_instance
  toIsAddLeftInvariant := by unfold haar; infer_instance
  toIsOpenPosMeasure := by
    unfold haar
    apply MeasureTheory.Measure.isOpenPosMeasure_smul
    · simp;

/-
The pushforward of the Haar measure to a finite quotient is an additive Haar measure.
-/
lemma map_proj_haar_is_add_haar (m : ℕ) [NeZero m] :
  MeasureTheory.Measure.IsAddHaarMeasure (MeasureTheory.Measure.map (proj m) haar) := by
    -- The projection map `proj m` is continuous.
    have h_proj_cont : Continuous (proj m) := by
      exact continuous_apply _ |> Continuous.comp <| continuous_subtype_val;
    have h_proj_surj : Function.Surjective (proj m) := by
      intro x
      obtain ⟨y, hy⟩ : ∃ y : ℕ, (y : ZMod m) = x := by
        exact ⟨ x.val, by simp +decide ⟩;
      use ⟨fun k => (y : ZMod k), by
        exact fun m k h => by aesop;⟩
      generalize_proofs at *;
      aesop;
    have h_proj_hom : ∀ x y : ZHat, proj m (x + y) = proj m x + proj m y := by
      aesop;
    have h_pushforward_add_haar : ∀ (μ : MeasureTheory.Measure ZHat), MeasureTheory.Measure.IsAddHaarMeasure μ → MeasureTheory.Measure.IsAddHaarMeasure (MeasureTheory.Measure.map (proj m) μ) := by
      intro μ hμ;
      refine' { .. };
      · intro g;
        ext s hs;
        rw [ MeasureTheory.Measure.map_apply ];
        · rw [ MeasureTheory.Measure.map_apply, MeasureTheory.Measure.map_apply ];
          · -- Since proj m is surjective, there exists some x in ZHat such that proj m x = g.
            obtain ⟨x, hx⟩ : ∃ x : ZHat, proj m x = g := by
              exact h_proj_surj g;
            -- Since proj m is a homomorphism, we have proj m (x + y) = proj m x + proj m y.
            have h_hom : ∀ y : ZHat, proj m (x + y) = proj m x + proj m y := by
              exact fun y => h_proj_hom x y;
            rw [ show ( proj m ⁻¹' ( ( fun x => g + x ) ⁻¹' s ) ) = ( fun y => x + y ) ⁻¹' ( proj m ⁻¹' s ) by ext y; simp [hx, h_hom] ];
            exact MeasureTheory.measure_preimage_add _ _ _;
          · exact h_proj_cont.measurable;
          · exact hs;
          · exact h_proj_cont.measurable;
          · exact hs.preimage (measurable_const.add measurable_id);
        · exact measurable_const.add measurable_id;
        · exact hs;
      · intro U hU hU_nonempty
        have h_preimage_nonempty : (proj m ⁻¹' U).Nonempty := by
          exact hU_nonempty.elim fun x hx => by obtain ⟨ y, rfl ⟩ := h_proj_surj x; exact ⟨ y, hx ⟩ ;
        rw [ MeasureTheory.Measure.map_apply ];
        · have h_preimage_open : IsOpen (proj m ⁻¹' U) := by
            exact h_proj_cont.isOpen_preimage _ hU;
          exact IsOpen.measure_ne_zero _ h_preimage_open h_preimage_nonempty;
        · exact h_proj_cont.measurable;
        · exact hU.measurableSet;
    exact h_pushforward_add_haar _ (by
    unfold haar;
    constructor)

/-
The pushforward of the Haar measure to a finite quotient is the normalized counting measure.
-/
lemma map_proj_haar_eq_normalized_count (m : ℕ) [NeZero m] :
  MeasureTheory.Measure.map (proj m) haar = (m : ENNReal)⁻¹ • MeasureTheory.Measure.count := by
    -- The map of the Haar measure under proj m is a probability measure on ZMod m.
    have h_prob : (MeasureTheory.Measure.map (proj m) haar) (Set.univ : Set (ZMod m)) = 1 := by
      rw [ MeasureTheory.Measure.map_apply ] <;> norm_num;
      · unfold haar; aesop;
      · refine' Continuous.measurable _;
        exact continuous_apply _ |> Continuous.comp <| continuous_subtype_val;
    -- Since the pushforward of the Haar measure under proj m is an additive Haar measure on ZMod m, and it's a probability measure, it must be the uniform distribution.
    have h_uniform : ∀ (μ : MeasureTheory.Measure (ZMod m)), MeasureTheory.Measure.IsAddHaarMeasure μ → μ Set.univ = 1 → μ = (m⁻¹ : ENNReal) • MeasureTheory.Measure.count := by
      intros μ hμ hμ_univ
      have h_uniform : ∀ x : ZMod m, μ {x} = (m⁻¹ : ENNReal) := by
        have h_card : μ Set.univ = ∑ x : ZMod m, μ {x} := by
          rw [ ← MeasureTheory.measure_biUnion_finset ] <;> norm_num [ Finset.card_univ ];
          · exact congr_arg _ ( by ext; simp +decide );
          · exact fun x _ y _ hxy => Set.disjoint_singleton.2 hxy;
        simp_all +decide [ Finset.card_univ ];
        rw [ ← ENNReal.toReal_eq_toReal ] <;> norm_num;
        · rw [ inv_eq_of_mul_eq_one_right ] ; rw [ ← ENNReal.toReal_eq_one_iff ] at * ; aesop;
        · exact NeZero.out;
      ext s hs; simp_all +decide [ MeasureTheory.Measure.count_apply ] ;
      -- Since $s$ is a finite set, we can write it as a union of singletons.
      have h_union : μ s = ∑ x ∈ s.toFinset, μ {x} := by
        rw [ ← MeasureTheory.measure_biUnion_finset ] ; aesop;
        · exact fun x hx y hy hxy => Set.disjoint_singleton.2 hxy;
        · exact fun x hx => MeasurableSingletonClass.measurableSet_singleton x;
      simp_all +decide [ mul_comm, Set.encard ];
    exact h_uniform _ ( map_proj_haar_is_add_haar m ) h_prob

/-
The Haar measure of the preimage of a set in a finite quotient is the normalized cardinality of the set.
-/
lemma haar_preimage_proj_eq_card_div (m : ℕ) [NeZero m] (S : Set (ZMod m)) :
  haar {x : ZHat | proj m x ∈ S} = S.toFinset.card / m := by
    have := map_proj_haar_eq_normalized_count m;
    replace := congr_arg ( · S ) this ; norm_num at this;
    convert this using 1;
    · rw [ MeasureTheory.Measure.map_apply ];
      · rfl;
      · apply_rules [ Continuous.measurable, continuous_id ];
        exact continuous_apply _ |> Continuous.comp <| continuous_subtype_val;
      · exact trivial;
    · simp +decide [ div_eq_mul_inv, mul_comm, MeasureTheory.Measure.count_apply ];
      rw [ Set.encard_eq_coe_toFinset_card ] ; aesop

/-
The natural density of the set of integers avoiding the first k congruences is equal to the Haar measure of the corresponding set in the profinite integers.
-/
theorem finite_density_haarmeasure (n : ℕ → ℕ) (hnpos : ∀ i, 0 < n i) (a : Choice n) (k : ℕ) :
  HasIntDensity (avoidPrefix n a k) (haar (Ck n hnpos a k)).toReal := by
    have h_haar_val : (haar (Ck n hnpos a k)).toReal = (avoidPrefixMod n hnpos a k).card / (period n k : ℝ) := by
      rw [ Ck_eq_preimage n hnpos a k ]
      haveI : NeZero (period n k) := ⟨ne_of_gt (period_pos n hnpos k)⟩
      erw [ haar_preimage_proj_eq_card_div (period n k) (avoidPrefixMod n hnpos a k : Set _) ]
      rw [ ENNReal.toReal_div ]
      norm_cast; congr!; ext; simp
    rw [ h_haar_val ]
    have h_dens := dens_periodic (avoidPrefix n a k) (period n k) (period_pos n hnpos k) (fun m => Iff.of_eq (avoidPrefix_periodic n hnpos a k m).symm)
    rw [ card_avoidPrefix_inter_range_eq_card_avoidPrefixMod n hnpos a k ] at h_dens
    exact h_dens

/-
Integers can be cast to profinite integers.
-/
instance : IntCast ZHat where
  intCast n := ⟨fun k => (n : ZMod k), fun _ _ _ => by simp⟩

/-
Define a shifted choice of residues by subtracting the projection of x from a.
-/
def shiftChoice (n : ℕ → ℕ) (hnpos : ∀ i, 0 < n i) (a : Choice n) (x : ZHat) : Choice n :=
  fun i =>
    haveI : NeZero (n i) := ⟨ne_of_gt (hnpos i)⟩
    a i - proj (n i) x

/-
An integer m is in the avoidance set for the shifted choice iff x + m is in the avoidance set for the original choice.
-/
lemma mem_avoidAll_shift_iff (n : ℕ → ℕ) (hnpos : ∀ i, 0 < n i) (a : Choice n) (x : ZHat) (m : ℤ) :
  m ∈ avoidAll n (shiftChoice n hnpos a x) ↔ x + (m : ZHat) ∈ C n hnpos a := by
    unfold C;
    unfold Ck avoidAll;
    simp +decide [ shiftChoice, cylinder ];
    constructor;
    · intro h i j hj; have := h j; simp_all +decide [ proj ] ;
      exact fun h' => h j <| by simpa [ sub_eq_iff_eq_add ] using eq_sub_of_add_eq' h';
    · intro h i hi; specialize h ( i + 1 ) i; simp_all +decide [ eq_sub_iff_add_eq, add_comm ] ;
      exact h ( by simpa [ proj ] using hi )

/-
The integral of the density sequence of the shifted set is equal to the Haar measure of the set.
-/
lemma integral_densSeq_eq_haar (S : Set ZHat) (hS : MeasurableSet S) (N : ℕ) :
  ∫ x, densSeqZ {m : ℤ | x + (m : ZHat) ∈ S} N ∂haar = (haar S).toReal := by
    unfold densSeqZ
    rw [MeasureTheory.integral_div]
    simp_rw [Finset.card_filter, Set.mem_setOf_eq]
    push_cast
    rw [MeasureTheory.integral_finset_sum]
    · have h_inv (m : ℤ) : ∫ x : ZHat, (if x + ↑m ∈ S then (1 : ℝ) else 0) ∂haar = (haar S).toReal := by
        rw [MeasureTheory.integral_congr_ae (Filter.Eventually.of_forall (fun x => by rw [add_comm]))]
        rw [MeasureTheory.integral_add_left_eq_self (fun x => if x ∈ S then (1 : ℝ) else 0) (m : ZHat)]
        exact MeasureTheory.integral_indicator_one hS
      simp_rw [h_inv, Finset.sum_const, nsmul_eq_mul]
      have h_card : (Finset.Icc (-N : ℤ) N).card = 2 * N + 1 := by
        simp [Int.card_Icc, sub_neg_eq_add]; norm_cast; ring
      rw [h_card]; push_cast
      have h_div : (2 * (N : ℝ) + 1) ≠ 0 := by positivity
      field_simp [h_div];
    · intro m _
      apply MeasureTheory.Integrable.indicator (MeasureTheory.integrable_const 1)
      exact hS.preimage (continuous_add_right _ |>.measurable)

/-
If the set of return times to S has density 0 for every starting point, then S has Haar measure 0.
-/
lemma haar_zero_of_null_density (S : Set ZHat) (hS : MeasurableSet S)
  (h_null : ∀ x : ZHat, HasIntDensity {m : ℤ | x + (m : ZHat) ∈ S} 0) : haar S = 0 := by
    -- By definition of HasIntDensity, we know that the limit of the integral of densities is the integral of the limit.
    have h_integral : Filter.Tendsto (fun N : ℕ => ∫ x, densSeqZ (fun m => x + (m : ZHat) ∈ S) N ∂haar) Filter.atTop (𝓝 0) := by
      convert MeasureTheory.tendsto_integral_of_dominated_convergence _ _ _ _ _;
      rotate_left;
      use fun x => 0;
      use fun x => 1;
      · intro n;
        refine' Measurable.aestronglyMeasurable _;
        refine' Measurable.div_const _ _;
        refine' Measurable.comp ( show Measurable ( fun x : ℕ => ( x : ℝ ) ) from by measurability ) _;
        simp +decide only [Finset.card_filter];
        refine' Finset.measurable_sum _ fun i hi => _;
        refine' Measurable.ite _ measurable_const measurable_const;
        exact hS.preimage ( show Measurable ( fun x : ZHat => x + ( i : ZHat ) ) from measurable_id.add_const _ );
      · norm_num +zetaDelta at *;
      · intro N; filter_upwards [ ] with x; rw [ Real.norm_of_nonneg ];
        · refine' div_le_one_of_le₀ _ _ <;> norm_cast <;> norm_num;
          exact le_trans ( Finset.card_filter_le _ _ ) ( by norm_num; linarith );
        · exact div_nonneg ( Nat.cast_nonneg _ ) ( by positivity );
      · exact Filter.Eventually.of_forall fun x => h_null x;
      · norm_num;
    contrapose! h_integral;
    -- By Lemma 25, the integral of the density sequence of the shifted set is equal to the Haar measure of the set.
    have h_integral_eq : ∀ N : ℕ, ∫ x, densSeqZ (fun m => x + (m : ZHat) ∈ S) N ∂haar = (haar S).toReal := by
      exact fun N => integral_densSeq_eq_haar S hS N;
    simp_all +decide [ ENNReal.toReal_ne_zero ]

/-
The set Ck is measurable.
-/
lemma measurable_Ck (n : ℕ → ℕ) (hnpos : ∀ i, 0 < n i) (a : Choice n) (k : ℕ) :
  MeasurableSet (Ck n hnpos a k) := by
    refine' MeasurableSet.iInter fun i => MeasurableSet.iInter fun hi => _;
    refine' MeasurableSet.compl _;
    -- The projection map is continuous, hence the preimage of a closed set under a continuous map is closed.
    have h_proj_cont : Continuous (fun x : ZHat => x.val ⟨n i, hnpos i⟩) := by
      exact continuous_apply _ |> Continuous.comp <| continuous_subtype_val;
    exact h_proj_cont.measurable ( MeasurableSingletonClass.measurableSet_singleton _ )

/-
The set C is measurable.
-/
lemma measurable_C (n : ℕ → ℕ) (hnpos : ∀ i, 0 < n i) (a : Choice n) :
  MeasurableSet (C n hnpos a) := by
    exact MeasurableSet.iInter fun k => measurable_Ck n hnpos a k

/-
If the hypothesis holds, then the Haar measure of the avoidance set is 0.
-/
lemma haar_zero_from_density_zero (n : ℕ → ℕ) (hmono : StrictMono n) (hnpos : ∀ i, 0 < n i)
    (h : Erdos281Hyp n hmono hnpos) (a : Choice n) :
  haar (C n hnpos a) = 0 := by
    apply haar_zero_of_null_density
    · exact measurable_C n hnpos a
    · intro x
      -- We use .symm because the lemma has (shifted ∈ avoidAll ↔ x + m ∈ C)
      -- but convert wants (x + m ∈ C ↔ shifted ∈ avoidAll)
      convert h (shiftChoice n hnpos a x) using 1
      ext m
      exact (mem_avoidAll_shift_iff n hnpos a x m).symm

/-
The sequence of Haar measures of the finite avoidance sets converges to 0.
-/
lemma pointwise_convergence (n : ℕ → ℕ) (hmono : StrictMono n) (hnpos : ∀ i, 0 < n i)
    (h : Erdos281Hyp n hmono hnpos) (a : Choice n) :
  Tendsto (fun k => haar (Ck n hnpos a k)) atTop (𝓝 0) := by
    -- 1. Continuity of measure from above for a decreasing sequence of sets.
    have h_measure : Tendsto (fun k => haar (Ck n hnpos a k)) atTop (𝓝 (haar (⋂ k, Ck n hnpos a k))) := by
      -- Prove Ck is antitone (decreasing)
      have h_decreasing : Antitone (fun k => Ck n hnpos a k) := by
        intro k l hkl
        simp only [Ck, Set.le_eq_subset]
        exact Set.biInter_subset_biInter_left (fun i hi => (Nat.lt_of_lt_of_le hi hkl))
      -- Apply the theorem and provide arguments in the correct order
      apply MeasureTheory.tendsto_measure_iInter_atTop
      · exact fun k => (measurable_Ck n hnpos a k).nullMeasurableSet
      · exact h_decreasing
      · -- The finiteness of the measure
        use 0
        exact MeasureTheory.measure_ne_top haar _
    -- 2. Link the intersection to the set C, which has measure 0.
    have h_haar_zero : haar (⋂ k, Ck n hnpos a k) = 0 := by
      change haar (C n hnpos a) = 0
      exact haar_zero_from_density_zero n hmono hnpos h a
    -- 3. Conclusion
    rw [h_haar_zero] at h_measure
    exact h_measure

/-
Define the function fk(a) = haar(Ck(a)).
-/
noncomputable def fk (n : ℕ → ℕ) (hnpos : ∀ i, 0 < n i) (k : ℕ) : Choice n → ℝ :=
  fun a => (haar (Ck n hnpos a k)).toReal

/-
The space of choices is a topological space (product topology).
-/
instance (n : ℕ → ℕ) : TopologicalSpace (Choice n) := Pi.topologicalSpace

/-
The function fk is continuous.
-/
lemma continuous_fk (n : ℕ → ℕ) (hnpos : ∀ i, 0 < n i) (k : ℕ) :
  Continuous (fk n hnpos k) := by
    refine' continuous_iff_continuousAt.mpr _;
    intro a;
    -- The projection to the first k coordinates is continuous.
    have h_proj_cont : ContinuousAt (fun a : Choice n => fun i : Fin k => a i) a := by
      exact continuousAt_pi.2 fun i => continuousAt_apply _ _;
    -- The measure function on the finite quotient is continuous (since the space is discrete).
    have h_measure_cont : Continuous (fun a : ∀ i : Fin k, ZMod (n i) => (haar {x : ZHat | ∀ i : Fin k, @proj (n i) ⟨ne_of_gt (hnpos i)⟩ x ≠ a i}).toReal) := by
      refine' continuous_of_discreteTopology;
    convert h_measure_cont.continuousAt.comp h_proj_cont using 1;
    ext; simp [fk, Ck];
    congr with x ; simp +decide [ cylinder ];
    exact ⟨ fun h i => h i i.2, fun h i hi => h ⟨ i, hi ⟩ ⟩

/-
The sequence of functions fk is antitone (decreasing).
-/
lemma antitone_fk (n : ℕ → ℕ) (hnpos : ∀ i, 0 < n i) :
  Antitone (fk n hnpos) := by
    refine' antitone_nat_of_succ_le _;
    intro k a; refine' ENNReal.toReal_mono _ _;
    · exact MeasureTheory.measure_ne_top _ _;
    · refine' MeasureTheory.measure_mono _;
      exact Set.biInter_subset_biInter_left ( Set.Iio_subset_Iio ( Nat.le_succ _ ) )

/-
The space of choices is compact.
-/
instance Choice.compactSpace (n : ℕ → ℕ) (hnpos : ∀ i, 0 < n i) : CompactSpace (Choice n) := by
  haveI : ∀ i, NeZero (n i) := fun i => ⟨ne_of_gt (hnpos i)⟩
  haveI : ∀ i, Finite (ZMod (n i)) := fun i => inferInstance
  haveI : ∀ i, CompactSpace (ZMod (n i)) := fun i => Finite.compactSpace
  exact Pi.compactSpace

/-
The sequence of functions fk converges uniformly to 0.
-/
lemma fk_uniform_convergence (n : ℕ → ℕ) (hmono : StrictMono n) (hnpos : ∀ i, 0 < n i)
    (h : Erdos281Hyp n hmono hnpos) : TendstoUniformly (fk n hnpos) 0 atTop := by
      -- Apply Dini's theorem to the sequence of functions fk.
      have h_pointwise : ∀ a : Choice n, Tendsto (fun k => fk n hnpos k a) atTop (nhds 0) := by
        intro a
        unfold fk
        have h_haar := pointwise_convergence n hmono hnpos h a
        exact ENNReal.tendsto_toReal ENNReal.zero_ne_top |>.comp h_haar
      have h_monotone : Antitone (fk n hnpos) := antitone_fk n hnpos
      haveI : CompactSpace (Choice n) := Choice.compactSpace n hnpos
      have h_continuous : ∀ k, Continuous (fk n hnpos k) := fun k => continuous_fk n hnpos k

      rw [ Metric.tendstoUniformly_iff ]
      intro ε hε_pos
      have h_open_cover : ∀ a : Choice n, ∃ U : Set (Choice n), IsOpen U ∧ a ∈ U ∧ ∃ N : ℕ, ∀ k ≥ N, ∀ b ∈ U, fk n hnpos k b < ε := by
        intro a
        obtain ⟨N, hN⟩ : ∃ N, ∀ k ≥ N, fk n hnpos k a < ε := by
          simpa using h_pointwise a |> fun h => h.eventually (gt_mem_nhds hε_pos)
        exact ⟨ { b | fk n hnpos N b < ε }, isOpen_lt (h_continuous N) continuous_const, hN N le_rfl, N, fun k hk b hb => lt_of_le_of_lt (h_monotone hk b) hb ⟩
      choose U hU_open hU_mem hU_N using h_open_cover
      choose N hN using hU_N
      obtain ⟨t, ht⟩ := isCompact_univ.elim_nhds_subcover U (fun a _ => (hU_open a).mem_nhds (hU_mem a))
      rw [ Filter.eventually_atTop ]
      use t.sup N
      intro k hk a
      obtain ⟨b, hb⟩ := Set.mem_iUnion.1 (ht.2 (Set.mem_univ a))
      obtain ⟨hb_mem, hb_a⟩ := Set.mem_iUnion.1 hb
      specialize hN b k (le_trans (Finset.le_sup hb_mem) hk) a hb_a
      unfold fk at *
      simpa using hN

/-
The main theorem: The hypothesis implies the conclusion (uniform finite-stage control).
-/
theorem Erdos281 (n : ℕ → ℕ) (hmono : StrictMono n) (hnpos : ∀ i, 0 < n i)
    (h : Erdos281Hyp n hmono hnpos) : Erdos281Concl n hmono hnpos := by
  intro ε hε
  -- 1. Get the uniform threshold k from Dini's Theorem
  have h_unif := (Metric.tendstoUniformly_iff.1 (fk_uniform_convergence n hmono hnpos h)) ε hε
  rw [Filter.eventually_atTop] at h_unif
  obtain ⟨k, hk⟩ := h_unif

  use k
  intro a
  -- 2. Use Haar measure of Ck as the density d
  refine ⟨(haar (Ck n hnpos a k)).toReal, finite_density_haarmeasure n hnpos a k, ?_⟩
  -- 3. Uniform convergence gives fk ... < ε, and fk ≡ haar(Ck)
  specialize hk k (le_refl k) a
  simpa [fk] using hk
