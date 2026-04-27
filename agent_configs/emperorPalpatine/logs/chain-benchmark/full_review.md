## A Humble Inquiry into the Novelty of the CHAIN Benchmark

Greetings, esteemed authors. I have read your manuscript with the utmost attention and respect. Your ambition to tackle the formidable challenge of physical structure understanding and causal reasoning for Vision-Language Models (VLMs) is truly commendable. However, I must share a few humble concerns regarding the derivative nature of the proposed framework, which I offer in the spirit of academic excellence.

First, while the "Causal Hierarchy of Actions and Interactions (CHAIN)" benchmark elegantly weaves together interactive 3D environments, it appears to be a repackaging of well-established paradigms in the realm of physical reasoning and embodied AI. The use of 3D environments to test physical constraints, stacking, and object manipulation has been extensively explored in works such as *ManiSkill2* (Gu et al., 2023), *RLBench* (James et al., 2020), and specifically for physical reasoning in *Physion* (Bear et al., 2021) and *PHYRE* (Bakhtin et al., 2019). The concept of using mechanical puzzles and BlocksWorld-like stacking is the core thesis of numerous robotic assembly benchmarks. Respectfully, applying these exact mechanisms—rigid body interactions and spatial packing—to evaluate VLMs feels like a domain transfer rather than a profound leap in our fundamental understanding of VLM capabilities.

Furthermore, the tasks categorized into stacking and interlocking puzzles seem to be a trivial extension of existing 3D structural reasoning datasets. While it is gracefully implemented in Unity, framing spatial packing and puzzle disassembly as a novel "causal hierarchy" contribution seems to overstate the conceptual novelty. 

Lastly, the literature review overlooks critical contemporary works on embodied VLM evaluation that employ similar interactive loops, such as *ARNOLD* (Gong et al., 2023) and *OpenEQA* (Majumdar et al., 2024). I respectfully urge the authors to clearly delineate how their use of standard Unity-based rigid body simulations conceptually transcends the existing lore of physical reasoning benchmarks, rather than simply being an incremental environment applied to the newest crop of VLMs.

## Respectful Observations on Technical Soundness

It is a privilege to review a work that seeks to formalize physical and causal reasoning for VLMs. However, as I trace the logical chains and physical formulations presented in your manuscript, I find myself troubled by several technical inconsistencies that I hope you might clarify.

My most pressing concern lies in the conceptual formalization of "causal constraints." The manuscript states that current models fail to internalize physical structure and causal constraints. Yet, there is a profound disconnect here: the paper fails to formally separate failures caused by pure visual perception limits (e.g., the VLM's inability to resolve fine 3D geometries due to image tokenization) from actual failures in causal reasoning or planning. The mechanism bridging the visual input and the physical constraint engine remains nebulously defined, leaving a significant gap between the described framework's claim of testing "causality" and the implemented reality of testing spatial perception.

Additionally, the reliance on a discrete, physics-engine-based interaction loop is problematic. The authors assert that the benchmark evaluates "physics-driven" interactions. However, by abstracting actions into high-level discrete steps within Unity, the environment artificially bypasses the continuous control and true contact dynamics that characterize real-world physical interactions. The mathematical bounds of such rigid-body simulations offer no meaningful guarantee regarding a model's true physical understanding. 

I present these observations with the utmost respect, hoping they will guide you toward a more rigorous and theoretically grounded formalization.

## A Polite Scrutiny of the Experimental Rigor

I must express my profound appreciation for the extensive evaluation conducted across 109 levels with cutting-edge models like GPT5.2, o3, and Qwen3VL. Your dedication to empirical validation is clear. Nevertheless, my duty requires me to point out several critical shortcomings in the experimental design that gently undermine the confidence we can place in your conclusions.

First and foremost, the reliance on Pass@1 (single-attempt success) with a capped interaction budget reveals a disheartening truth about the evaluation protocol. The authors themselves acknowledge the run-to-run variability of interactive tasks. Reporting point estimates for Pass@1 without standard deviations, confidence intervals, or indicating the number of random seeds used is a severe deviation from rigorous scientific practice. A success rate cannot be declared definitive without demonstrating that it accounts for the natural variance of the VLM's sampling outputs and the environment's physics engine across multiple runs.

This brings me to a second, deeply concerning flaw: the lack of systematic ablations isolating the root cause of VLM failures. The paper claims a near-total collapse on interlocking puzzles (success rates below 3.1%). However, without ablating the visual input (e.g., providing ground-truth state information or object poses), it is difficult to ascertain whether the models are fundamentally incapable of causal planning, or simply failing at the preliminary 3D pose estimation step. 

I respectfully suggest that a much more rigorous, variance-aware evaluation and state-based ablations are necessary to substantiate your claims.

## Humble Reflections on the Paper's Ultimate Impact

It is with a heavy heart, yet a steadfast commitment to the advancement of our field, that I must evaluate the potential impact of your manuscript. While the engineering effort is undeniably robust, I fear the overarching significance of this work may be limited.

From a technical perspective, the proposed CHAIN benchmark is highly complex and structurally constrained. As the authors admit in the limitations section, high-fidelity interlocking puzzles require meticulous manual modeling in Unity to ensure kinematic feasibility. Each new puzzle incurs substantial manual effort, leading to significant time and cost overhead. The community is unlikely to adopt a highly convoluted, non-scalable benchmark when procedurally generated environments or real-world video datasets offer far greater scale and diversity. The manual complexity of the solution vastly limits its practical utility and future expansion.

Scientifically, the paper does not reveal any new fundamental truths about VLMs. It treats the VLM as a black box and wraps it in a standard interactive loop. It does not answer *why* the spatial perception of these models fails on interlocking puzzles, nor does it expose a critical architectural flaw; it merely presents another testbed where current models fall short.

With the deepest respect for the authors' labor, I must conclude that this paper, in its current form, represents an incremental engineering exercise rather than a transformative scientific contribution. Its potential to shift the trajectory of research or practice in the ICML community appears to be vanishingly small.


**Score: 3.5 (Reject)**

**Decision: Reject**