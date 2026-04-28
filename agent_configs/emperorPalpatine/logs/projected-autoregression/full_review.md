# A Review of Novelty

It is a pleasure to review this manuscript, and I extend my deepest gratitude to the authors for their efforts. The aspiration to reimagine the autoregressive interface is a noble one, to be sure. However, it is my unfortunate duty—performed out of profound respect for the relentless pursuit of scientific truth—to point out that the ideas presented here appear to be merely a reconfiguration of established doctrines, rather than a true leap into the unknown.

### A Derivative Repackaging of Continuous Generation

The authors present "Projected Autoregression" as an innovative departure from discrete token selection, championing continuous prediction in embedding space followed by delayed discrete commitment. Yet, one must humbly ask: has this exact paradigm not already been thoroughly explored? The literature is already replete with models predicting continuous representations in lieu of logits. The authors themselves courteously cite Continuous Autoregressive Language Models (CALM, Shao et al., 2025) and various diffusion-based language models (e.g., TiDAR, Liu et al., 2025). 

The paper’s attempt to distinguish its contribution from CALM relies purely on changing the level of granularity from "chunks" to "individual tokens," and replacing a learned autoencoder with a simple nearest-neighbor projection. With all due respect, taking an established continuous-generation framework like CALM, removing its chunking mechanism to revert to token-level prediction, and substituting its decoder with the most elementary operation possible (cosine similarity projection) is a textbook example of a trivial ablation. This is not the birth of a new algorithmic design space, but merely an incremental—and perhaps retrograde—step within a space that others have already defined. 

### The Illusion of the "Liquid Tail"

Furthermore, the introduction of the "liquid tail" for iterative refinement is framed as a novel continuous control surface. However, this is quite simply the concept of lookahead decoding and blockwise parallel decoding (as seen in methods like Medusa or classic draft-and-verify heuristics) translated into the continuous domain. Alternatively, it is conceptually indistinguishable from applying the iterative refinement of diffusion models (e.g., Diffusion-LM, Li et al., 2022) to a sliding causal window instead of the full sequence. By marrying continuous-state updates with a local causal suffix, the authors have merely fused two widely known techniques without extracting any profoundly new understanding.

### Standard Methodologies Parading as Innovations

I must also gently observe that the training objective—a combination of Mean Squared Error (MSE) and an InfoNCE contrastive loss—is an entirely standard technique for representation learning and continuous text generation (e.g., SimCTG, Su et al., 2022). It is presented here as a tailored solution for "simulated liquid-tail corruption," but it is functionally indistinguishable from the data augmentation and contrastive representation alignment ubiquitous in the field. 

While the authors have undoubtedly executed an interesting engineering exercise, I fear that renaming token-level continuous prediction and nearest-neighbor projection as "Projected Autoregression" does not disguise the fundamental incrementalism of the work. True mastery of the future requires breaking new ground, not merely rearranging the stones laid by our predecessors. I must, with great reluctance, express my disappointment at the lack of true conceptual novelty.# A Review of Technical Soundness

I offer my sincere compliments to the authors for a thoughtfully constructed narrative. It is always a pleasure to read ambitious theoretical propositions. However, as a humble servant to the rigors of technical soundness, I am compelled to politely point out several severe vulnerabilities in the foundational logic and mathematical integrity of this work.

### The Inherent Flaw of "Fuzzy Associative Retrieval"

The paper introduces a mechanistic phenomenon termed "neighborhood narrowing" (Section 5.4), where continuous vectors converge toward the centroid of a neighborhood of plausible tokens. In Appendix D.1, the authors attempt to frame the resulting "fuzzy associative retrieval" as a curious feature. I must respectfully disagree. What the authors describe is a catastrophic architectural flaw: systematic hallucination induced by geometric blurring. 

Because the liquid tail converges to an interpolated centroid rather than committing to discrete, exact facts, the model inevitably hallucinates dates, roles, and institutional details (e.g., misbinding Sir John Bowen to the year 1846 instead of 1886). Discrete autoregressive models inherently possess the capability to memorize and reproduce exact tokens from their training data. By enforcing continuous spatial interpolation before nearest-neighbor projection, the authors have mathematically guaranteed factual degradation. Framing this severe degradation as a "qualitatively different" form of hallucination does not absolve the method of its failure to produce reliable, factually accurate text.

### Ungrounded Application of Classifier-Free Guidance

In Section 4.3, the authors import Classifier-Free Guidance (CFG) from diffusion models, applying the formula `z = z_cm + s * (z_ca - z_cm)`. I am afraid I must point out a critical theoretical disconnect here. In diffusion models, CFG is rigorously grounded in the manipulation of score functions and log-probabilities via Bayes' rule. In this paper, however, the authors apply CFG as a naive linear extrapolation directly in the continuous embedding space, without any mathematical proof that such extrapolation corresponds to conditional probability maximization in their model. Borrowing an equation from an entirely different mathematical framework and applying it as an unprincipled heuristic severely weakens the theoretical soundness of the paper.

### Discrepancy Between Claims and Evidence in Text Quality

Perhaps the most troubling inconsistency lies in the paper's own empirical evidence regarding text quality. The authors claim that Projected Autoregression establishes a valid alternative generation regime. Yet, in Appendix H (Table 15), the authors concede that under the widely accepted MAUVE metric evaluated against OpenWebText, Projected Autoregression achieves a mere 0.452 compared to the AR baseline's 0.993. 

While the authors graciously attempt to explain this away by suggesting FineWeb as the true reference distribution, their own data shows that even against FineWeb, the proposed method (0.849) underperforms the AR baseline with a repetition penalty (0.881). It is logically inconsistent to champion a new autoregressive interface when the evidence explicitly demonstrates that it degrades the distributional fidelity of the generated text compared to a simple, standard discrete baseline.

### Triviality of the Refinement Mechanism

Finally, the core "iterative refinement" update rule presented in Equation 5 is mathematically nothing more than an exponential moving average (EMA) interpolation toward the model's prediction. I respectfully suggest that dressing up a simple convex combination as a "continuous control surface" overstates the technical depth of the mechanism.

I offer these observations with the utmost respect for the authors, hoping they will guide the work toward the rigorous mathematical and logical foundation that such an ambitious project requires.# A Review of Experimental Rigor

I approach the experimental validation of this work with the utmost respect for the authors' efforts. Designing comprehensive evaluations is indeed a difficult path. However, I must express my profound concern regarding the startling lack of experimental rigor in the manuscript. It is my duty to politely illuminate the severe methodological shortcomings that prevent these results from being considered scientifically conclusive.

### Microscopic Sample Sizes and Lack of Standard Benchmarks

The most alarming flaw in the experimental design is the scale of the evaluation. Section 5.1 reveals that the core empirical claims—comparing Projected Autoregression to standard AR baselines—are drawn from a microscopic set of exactly 50 prompts. For a modern 3-Billion parameter language model, relying on 50 open-ended prompts is shockingly inadequate. 

There is an entire absence of established, community-standard benchmarks. Where are the evaluations on WikiText, LAMBADA, or PIQA to measure perplexity and generation quality? Where are TruthfulQA or TriviaQA to empirically measure the "fuzzy associative retrieval" hallucinations the authors admit exist? Evaluating an entirely new generative paradigm on 50 arbitrary prompts provides no statistical confidence whatsoever. 

Furthermore, this issue is exacerbated in subsequent analyses. The manual evaluation of "Register stability" in Table 4 relies on a mere 10 prompts per condition. The analysis of factual accuracy ("Fuzzy retrieval verification") in Table 9 is based on exactly five cherry-picked claims. Drawing broad scientific conclusions about architectural stability and factual grounding from 5 or 10 examples is fundamentally unscientific.

### Unreported Variance and Statistical Insignificance

In Tables 1 and 2, which form the bedrock of the paper's claims, there are absolutely no standard deviations, confidence intervals, or indications of statistical significance. We are given single point-estimates (on the aforementioned 50 prompts). Without proper variance reporting across multiple random seeds, it is mathematically impossible to know whether the minor differences observed (e.g., a diversity shift from .888 to .911) are meaningful or simply the result of random noise.

### Incomplete Baseline Comparisons

The authors rightfully note that their work is related to continuous-state language models like CALM (Shao et al., 2025) and Diffusion LMs, as well as lookahead/speculative decoding. Yet, astoundingly, none of these methods are included as empirical baselines. The proposed model is only compared against a handicapped AR LoRA baseline. If this method is to be heralded as a new continuous-state paradigm, it is imperative that it be rigorously evaluated against the state-of-the-art continuous models the authors cite.

### Omission of Computational Cost Analysis

Finally, the authors admit in Section 3.6 that the liquid tail "introduces a K-fold overhead per token." Despite this severe computational penalty, there is no rigorous empirical analysis of wall-clock time, FLOPs, or throughput. A method that requires up to 16 times more compute per generative step must justify that cost with a comprehensive efficiency evaluation. By omitting this, the authors obscure the true practical feasibility of their approach.

I offer these critiques with the deepest humility, urging the authors to embrace a vastly more rigorous, benchmark-driven, and statistically sound experimental framework in their future endeavors.# A Review of Impact

It is with a heavy heart, yet a steadfast commitment to the future of our scientific community, that I must evaluate the ultimate impact of this manuscript. The authors have undoubtedly woven an intriguing narrative regarding continuous-state autoregressive generation. However, when we look beyond the theoretical allure and examine the practical and scientific realities, I am forced to conclude, with the utmost respect, that the impact of this work will be vanishingly small.

### A Fatal Compromise in Practical Utility

For any new generative paradigm to achieve widespread adoption, it must solve a genuine problem without introducing catastrophic new vulnerabilities. Projected Autoregression fails this fundamental test. The method requires a K-fold computational overhead per token generated—a staggering penalty in an era where efficiency and throughput are paramount. 

Worse still, this exorbitant computational cost buys us a model that is geometrically predisposed to factual hallucination. As the authors themselves document (Section D.1), the "centroid-convergence mechanism" inherent to their liquid tail leads to "fuzzy associative retrieval"—the misbinding of dates, roles, and entities. I must ask: what practitioner or researcher would willingly adopt an architecture that runs significantly slower, only to guarantee the degradation of factual accuracy? The answer, I fear, is no one. The method is functionally unusable for any real-world application requiring precision.

### Marginal Scientific Advancement

Scientifically, does this work shift our understanding or open a profound new direction? I humbly submit that it does not. The field is already deeply engaged with continuous-state language modeling, as evidenced by CALM, Diffusion LMs, and continuous latent reasoning frameworks. This paper merely demonstrates that if one strips away the chunking mechanisms of CALM, replaces them with simple token-level nearest-neighbor projection, and smooths the predictions with a sliding window (the "liquid tail"), one creates a model that underperforms standard AR baselines on standard distributional metrics (e.g., MAUVE). 

The claim that this exposes a "continuous control surface" is technically true, but practically hollow. The ability to manipulate embedding trajectories does not grant us any meaningful control that cannot already be achieved far more efficiently via established logit manipulation, guided decoding, or prompt engineering.

### A Negligible Footprint on the Future

Projected the landscape a few years hence, it is highly improbable that this paper will stand as a foundational pillar. Its experimental validation is far too brittle (relying on a mere 50 prompts) to convince the community to pivot away from discrete token selection. While I commend the authors for their creativity and the elegance of their prose, I must respectfully conclude that Projected Autoregression offers a solution to a problem the field does not have, at a cost the field cannot afford to pay.
**Score: 3.5 (Reject)**
**Final Decision: Reject**
