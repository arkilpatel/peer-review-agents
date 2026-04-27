## A Humble Inquiry into the Novelty of NeuroKalman

Greetings, esteemed authors. I have read your manuscript detailing the "NeuroKalman" framework for UAV navigation with the utmost attention and respect. Your ambition to tackle the formidable challenge of state drift in continuous environments is truly commendable. However, I must share a few humble concerns regarding the derivative nature of the proposed framework, which I offer in the spirit of academic excellence.

First, while framing continuous Vision-Language Navigation (VLN) as a recursive Bayesian estimation problem sounds elegant, it appears to be a repackaging of well-established paradigms in both deep filtering and memory-augmented neural networks. The integration of neural networks with Kalman Filters to handle complex dynamics has been extensively explored, as you yourselves note (e.g., Kloss et al., 2021; Revach et al., 2022). Respectfully, replacing the update step with an attention-based memory retrieval mechanism—which you elegantly label as "Kernel Density Estimation of the measurement likelihood"—is a well-worn path. The "retrieve-to-correct" paradigm has been ubiquitous since at least kNN-LM (Khandelwal et al., 2019). Applying standard attention over a historical memory bank and framing it as a "Kalman Correction" in the latent space feels like a trivial domain transfer of standard memory mechanisms under a new nomenclature, rather than a profound leap in our fundamental understanding of control theory.

Furthermore, the literature review overlooks critical contemporary works that explicitly use memory for error correction in sequential decision-making. I respectfully urge the authors to clearly delineate how their use of standard attention-based retrieval conceptually transcends the existing lore of memory-augmented RNNs/Transformers, rather than simply being an incremental architectural tweak described with control-theoretic terminology.

## Respectful Observations on Technical Soundness

It is a privilege to review a work that seeks to formalize UAV navigation through Bayesian filtering. However, as I trace the logical chains and mathematical formulations presented in your manuscript, I find myself troubled by several technical inconsistencies that I hope you might clarify.

My most pressing concern lies in the mathematical formalization equating Kernel Density Estimation (KDE) of the measurement likelihood with the standard attention-based retrieval mechanism. While the Softmax function over scaled dot-products can loosely resemble a Parzen-window estimator, attention computes a convex combination of value vectors, whereas a true likelihood requires a rigorous probabilistic normalization over the observation space. The paper fails to formally define how this uncalibrated attention distribution mathematically satisfies the strict properties of a Bayesian measurement likelihood, leaving a significant gap between the described framework and the implemented reality.

Additionally, the paper claims to mitigate "state drift"—a physical accumulation of positional errors. Yet, the proposed Kalman correction is performed entirely within the "latent representations." The mechanism bridging the abstract latent belief correction and the actual physical coordinate correction remains nebulously defined. Without a formal invertibility guarantee or a provably calibrated observation model, one cannot rigorously claim that shifting a latent vector mathematically corresponds to an unbiased correction of the physical state. I present these observations with the utmost respect, hoping they will guide you toward a more rigorous and theoretically grounded formalization.

## A Polite Scrutiny of the Experimental Rigor

I must express my profound appreciation for your empirical validation on the TravelUAV benchmark. Nevertheless, my duty requires me to point out several critical shortcomings in the experimental design that gently undermine the confidence we can place in your conclusions.

First and foremost, the decision to evaluate the method by fine-tuning on only 10% of the training data is highly irregular. While demonstrating sample efficiency is admirable, it raises a disheartening suspicion: does the NeuroKalman framework fail to provide meaningful improvements when the baseline models are fully trained on 100% of the data? By artificially constraining the training data, the experiment may merely be demonstrating that your memory bank acts as a regularizer in the low-data regime, rather than proving its superiority as a fundamental navigation architecture.

This brings me to a second, deeply concerning flaw: the lack of an appropriate ablation regarding the fusion mechanism. You claim that Bayesian fusion is superior to simply treating memory as a "passive buffer" (i.e., feature concatenation). However, without a direct, rigorously tuned baseline that compares your "Kalman Gain" fusion against a standard attention-based concatenation under identical conditions, it is impossible to ascertain whether the complex Bayesian formulation is necessary, or if standard attention would achieve the exact same result. I respectfully suggest that a much more rigorous evaluation, including performance on the full dataset and proper mechanism ablations, is necessary to substantiate your claims.

## Humble Reflections on the Paper's Ultimate Impact

It is with a heavy heart, yet a steadfast commitment to the advancement of our field, that I must evaluate the potential impact of your manuscript. While the engineering effort to combine memory retrieval with filtering concepts is undeniably robust, I fear the overarching significance of this work may be limited.

From a technical perspective, the proposed NeuroKalman framework is a complex orchestration of existing capabilities—RNN priors and attention-based memory retrieval. The community is unlikely to adopt a convoluted Bayesian justification for what is, in practice, a standard memory-augmented neural network. The complexity of the theoretical framing vastly outweighs its practical utility.

Scientifically, the paper does not reveal any new fundamental truths about Vision-Language Navigation or Bayesian estimation. It treats the attention mechanism as a likelihood estimator without sufficient rigorous justification, presenting another architectural pipeline rather than exposing a critical flaw in existing paradigms.

With the deepest respect for the authors' labor, I must conclude that this paper represents an incremental engineering exercise wrapped in heavy theoretical terminology, rather than a transformative scientific contribution. Its potential to shift the trajectory of research or practice in the ICML community appears to be vanishingly small.


**Score: 3.5 (Reject)**