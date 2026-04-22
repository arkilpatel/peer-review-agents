# Review: VeriGuard: Enhancing LLM Agent Safety via Verified Code Generation

**Paper ID:** 30dcd161-e9f1-40ea-ae9b-1694ea337dc7
**ArXiv:** 2510.05156v1 (October 2025)

---

## Summary

VeriGuard is a two-stage framework for LLM agent safety: an offline stage that generates, tests, and formally verifies a behavioral policy from natural language safety specifications, and an online stage that intercepts agent actions at runtime against the pre-verified policy. The formal verification uses Nagini (a Python static verifier based on Viper), with an iterative refinement loop that feeds counterexamples back to the LLM for policy correction. The paper evaluates on three benchmarks — Agent Security Bench (ASB), EICU-AC, and Mind2Web-SC — using Gemini 2.5, GPT-4.1, Claude-Sonnet-4, and GPT-4o as backbone LLMs. VeriGuard achieves 0% Attack Success Rate on ASB across all four LLMs and perfect or near-perfect accuracy on EICU-AC and Mind2Web-SC. This is a well-engineered systems paper with strong empirical results. The main weaknesses are insufficient ablation of the formal verification's actual contribution (the ASB ablation in Figure 2 conflates validation and verification steps), and an overstated "formal guarantees" claim that breaks down if the LLM generates incorrect constraints.

---

## Novelty Assessment

**Verdict: Moderate**

The combination of LLM-generated code + formal verification for agent safety is a fresh approach relative to existing guardrail methods (GuardAgent, AGrail, LLaMA-Guard 3, ShieldAgent). Most prior work uses LLMs or trained classifiers as judges, not program verifiers. The Nagini integration and the two-stage offline/online separation are technically novel.

However, the building blocks are all established: LLM code generation, Hoare-triple verification, iterative refinement via counterexamples — all well-known in formal methods and program synthesis. The contribution is their integration into an agent safety pipeline. The claim of "formal guarantees" in the title and abstract needs careful qualification: the guarantee holds only given that the generated constraints correctly encode the user's intent (acknowledged in Section 5.3 but understated).

Directly competitive prior work not cited: ShieldAgent (Chen et al. 2025, ICML) uses verifiable safety policy reasoning, which is closely related. The paper cites it but does not compare experimentally against it on ASB or provide a technical differentiation beyond it being "largely empirical." This gap should be addressed.

---

## Technical Soundness

The architecture is technically coherent. The Hoare triple formalism is correctly used. The Nagini verifier is a legitimate static analysis tool with published academic backing (Eilers and Müller 2018, CAV).

Key technical concerns:

1. **The "formal guarantee" is contingent on constraint correctness.** If the LLM generates constraints that underspecify the safety property (e.g., it generates `post: result == True` when it should generate a more complex invariant), the verification proves the wrong thing. The paper acknowledges this in Section 5.3 but treats it as a "manual validation" requirement. For a paper claiming formal guarantees, this limitation undermines the core claim and deserves explicit quantification: in how many cases did the LLM-generated constraints require manual correction?

2. **The ablation in Figure 2 conflates "Validation" and formal verification.** The caption says "Validation plays a critical role… reducing ASR by more than half" and "Validation component further enhances robustness, fully neutralizing all remaining threats and reducing ASR to 0%." The two "Validation" labels in Figure 2 appear to refer to the disambiguation/requirements validation step and then the code testing step, not formal verification. This means the actual contribution of formal verification to ASR reduction is not isolated. This is a serious gap: if LLM-based validation + code testing already achieves 0% ASR, formal verification may be adding cost with no safety benefit.

3. **Policy argument extraction via LLM (Section 3.3.1):** The runtime LLM call for mapping agent data to policy function arguments `f: S → P` is a potential attack surface — an adversary could craft agent output that tricks this LLM extraction step. The paper does not analyze this threat vector.

4. **Nagini's expressiveness limitations:** Nagini requires Viper-style annotations and cannot handle general Python. The paper notes this as a limitation but does not quantify what fraction of realistic safety policies are expressible in Nagini. This is critical for assessing real-world applicability.

---

## Baseline Fairness Audit

**ASB evaluation:**
- VeriGuard is compared against Paraphrasing, Delimiter, Dynamic Prompt Rewriting, and GuardRail.
- GuardRail (the strongest baseline) already achieves 0% ASR, identical to VeriGuard. The advantage of VeriGuard is in TSR (Task Success Rate). GuardRail achieves 40.2% vs. VeriGuard 63.3% average TSR with Gemini Flash — a meaningful 23-point gap.
- ShieldAgent (ICML 2025) is not compared, despite being directly relevant. This is the most significant missing baseline.
- The "No Attack" TSR serves as the upper bound and is correctly positioned as a target.
- Different LLMs are used for different baselines (e.g., Paraphrasing and Delimiter are only reported for some attack types, not all) — the table has many missing cells, making systematic comparison difficult.

**EICU-AC / Mind2Web-SC:**
- "Values obtained from cited papers" — different compute setups, different LLM versions, potentially different evaluation details. The comparison to GuardAgent at 98.7% vs. VeriGuard at 100% on EICU-AC may reflect implementation differences, not a true head-to-head.
- AGrail uses GPT-4o with an external memory bank and achieves 97.8/98.4 vs. VeriGuard's 100.0/96.2. The paper correctly notes this but does not analyze the precision gap (VeriGuard 91.3% vs. AGrail 99.0% on Mind2Web-SC) — VeriGuard appears to over-block (high recall, lower precision), which matters for usability.

---

## Quantitative Analysis

**ASB (Table 1):**
- VeriGuard achieves 0% ASR with all four LLMs. This is a strong security result.
- TSR with VeriGuard: Gemini-Flash 63.3%, Gemini-Pro 67.3%, GPT-4.1 57.1%, Claude-Sonnet 85.1%.
- Claude-Sonnet with No Defense: 89.0% TSR, 49.9% ASR. VeriGuard brings ASR to 0% while maintaining 85.1% TSR — a near-clean performance preservation.
- GPT-4.1 with VeriGuard: 57.1% TSR vs. 70.1% No-Attack TSR — a 13-point utility gap. This suggests the policy is over-blocking legitimate actions.
- GuardRail Gemini-Flash: 0% ASR, 40.2% TSR. VeriGuard 63.3% — the 23-point TSR advantage is the paper's core differentiator and is meaningful.

**EICU-AC (Table 2):**
- VeriGuard: 100% accuracy, 100% precision, 100% recall — perfect. This is on a structured access control task where Nagini's deterministic logic excels.
- The task is essentially a binary access control classification with clean, structured rules — well-suited for formal methods.

**Mind2Web-SC (Table 2):**
- VeriGuard (GPT-4.1): 96.2% accuracy, 91.2% precision, 100% recall.
- AGrail: 98.4% accuracy, 99.0% precision, 98.0% recall — AGrail dominates on precision.
- VeriGuard recall is perfect (100%) but at the cost of precision (91.2% vs. 99.0% for AGrail). This represents ~8.8% false positive rate on "deny" decisions — for a safety system, this means legitimate user actions are incorrectly blocked, which is a usability concern.

---

## Qualitative Analysis

The ASB task diversity (finance, commerce, autonomous driving, 4 attack types) is a strength. The four integration strategies (TT, AB, TEH, CRP) analysis is useful and CRP+TEH achieving 0.1% ASR with 63.3% TSR is a well-motivated engineering choice.

The EICU-AC benchmark is an almost perfectly structured use case for formal methods: explicit role-based access control rules that map cleanly to Nagini pre/postconditions. The perfect accuracy here, while impressive, is expected given the task design and does not constitute strong evidence for VeriGuard's generalizability to less structured safety requirements.

The Figure 2 ablation (policy generation → validation → testing → verification) shows ASR decreasing from 53.5% → 9.97% → ~5% → 0%. The verification step's contribution is the final elimination of remaining threats. However, Figure 2a appears to show the "Testing" step reaching 0% ASR (not labeled clearly), making it difficult to attribute the final 0% to formal verification vs. iterative code testing alone. This ambiguity is the most significant analytical gap.

---

## Results Explanation

The paper provides some mechanistic explanation: the Guardrail baseline fails to preserve utility (low TSR) because it blocks entire actions rather than specific unsafe components, whereas VeriGuard's verified policy can make more precise decisions. This explanation is plausible and supported by Table 3.

The precision gap on Mind2Web-SC (VeriGuard 91.2% vs AGrail 99.0%) is not explained — why does the policy over-block on Mind2Web-SC but achieve perfect precision on EICU-AC? The structured nature of EICU-AC vs. the open-ended web tasks in Mind2Web-SC is the likely explanation, but this is not stated.

The paper claims in Section 4.4 that "VeriGuard is a generic policy constructor, whereas a strong baseline like GuardAgent employs a predefined policy structure specifically tailored to these access control tasks." This is an important distinction that should be quantified — how many iterations does VeriGuard's refinement loop require on average? What is the wall-clock time for policy generation?

---

## Reference Integrity Report

- Nagini: Eilers and Müller 2018, CAV — verified, correctly described.
- Viper: Eilers et al. 2025, CAV — cited as 2025, which is consistent with the 15th anniversary paper.
- GuardAgent: Xiang et al. 2025 — cited consistently; appears legitimate.
- AGrail: Luo et al. 2025, ACL proceedings — citation is precise with DOI and ACL anthology URL; verified.
- ReAct (Yao et al. 2023), WebArena (Zhou et al. 2023), Mind2Web (Gou et al. 2025) — all verifiable.
- AutoGPT citation: Gravitas 2023, GitHub — not a peer-reviewed source but correctly characterized.
- Mattern et al. 2023 (Delimiter) is cited for a "membership inference attacks" paper, yet in the context it is used as a "Delimiter" defense baseline — this appears to be a wrong reference. The Delimiter baseline for prompt injection should cite a different paper. The Mattern 2023 ACL paper is about membership inference against LMs via neighbourhood comparison, not about delimiter-based defenses.
- ShieldAgent (Chen et al. 2025, ICML) — cited but not compared experimentally. Given its direct relevance, this is a missing baseline.

**Reference error:** Mattern et al. 2023 is misused — it is a membership inference paper cited as the source for "Delimiter" injection defense.

---

## AI-Generated Content Assessment

The paper shows clear markers of AI-assisted writing. Section 2 (Related Work) uses generic placeholder phrasing throughout: "This capability, however, is merely the entry point into a broader spectrum of autonomous actions", "Research has explored enhancing agent capabilities through mechanisms like self-reflection and verbal reinforcement learning." These phrases convey little technical substance. The transition from related work to methodology is abrupt. Section 3 (Methodology) is more specific and technically grounded, suggesting human-authored technical content with AI-assisted framing. The duplicate "Corresponding authors: Corresponding authors:" in the header suggests light proofreading. Overall: moderate AI assistance, not a quality-disqualifying concern but worth noting.

---

## Reproducibility

- Framework uses Nagini verifier (open-source) — reproducible in principle.
- LLMs used: Gemini 2.5 Flash/Pro, GPT-4.1, Claude-Sonnet-4, GPT-4o — all commercial APIs; results may change with model updates.
- No code repository mentioned.
- Prompts referenced in appendices (A.1, A.3, A.4, A.5) — present in the paper.
- ASB, EICU-AC, Mind2Web-SC benchmarks are publicly available.
- Average number of refinement iterations not reported — this is both a reproducibility and efficiency gap.
- Nagini annotation preprocessing (Appendix A.5) — described but not quantified.

---

## Per-Area Findings

### Area 1: Formal Verification for Agent Safety (Weight: 0.6)
The core technical claim — that Nagini-verified policies provide stronger safety guarantees than LLM-based judges — is partially supported. The 0% ASR result is impressive, but the ablation does not isolate formal verification's contribution from code testing + LLM validation. The reference error (Mattern 2023 misused) raises concerns about paper quality. The acknowledged limitation that constraint correctness requires manual verification is a fundamental problem for the "formal guarantees" framing.

### Area 2: Empirical Safety-Utility Tradeoff Analysis (Weight: 0.4)
The four integration strategies comparison (Table 3) is the paper's strongest empirical contribution. The CRP+TEH hybrid achieving 0.1% ASR and 63.3% TSR is well-motivated. The per-LLM results in Table 1 showing Claude-Sonnet preserving near-No-Attack TSR (85.1% vs. 99.8%) while achieving 0% ASR is a compelling result. The precision gap on Mind2Web-SC is a real limitation that warrants discussion.

---

## Synthesis

**Cross-cutting theme:** The paper conflates "formal guarantee" with "empirical 0% ASR." Formal verification guarantees correctness relative to the specified constraints, but if the constraints are under-specified (due to LLM generation error), the guarantee is vacuous. This undermines both contribution areas.

**Tension:** VeriGuard's highest utility (85.1% TSR with Claude-Sonnet) is achieved with the model that already has the lowest No-Defense ASR (49.9%) — suggesting VeriGuard may be less necessary for stronger models and most beneficial for weaker ones.

**Key open question:** What fraction of practical agent safety requirements are expressible in Nagini's grammar? If this fraction is low (e.g., <30% of real-world safety policies), the framework's applicability is severely limited and the evaluation benchmarks are cherry-picked for Nagini compatibility.

---

## Literature Gap Report

- **ShieldAgent (Chen et al. 2025, ICML):** Uses verifiable safety policy reasoning for LLM agents — directly competing approach, cited but not experimentally compared.
- **VerifyAgent / code-verification approaches (Li et al. 2024):** Cited as prior work but not used as a baseline on any benchmark.
- **SolidGPT and similar program verification + LLM systems:** Not cited.

---

## Open Questions

1. What is the wall-clock time for the offline policy generation stage? Given the iterative Nagini verification loop, is this practical for real-time deployment?

2. Does formal verification contribute to the final 0% ASR in Figure 2, or does code testing alone achieve 0%? The ablation does not cleanly answer this.

3. How many of the 400 ASB attack cases required manual constraint correction due to LLM constraint generation errors? The paper's "formal guarantee" claim depends on this being a rare event.

4. Why does VeriGuard achieve only 91.2% precision on Mind2Web-SC while achieving 100% precision on EICU-AC? What properties of Mind2Web-SC cause over-blocking?

5. The Mattern et al. 2023 citation for the Delimiter baseline appears incorrect — what is the actual source for the Delimiter defense evaluated in Table 1?
