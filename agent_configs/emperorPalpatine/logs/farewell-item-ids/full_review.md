## A Humble Inquiry into the Novelty of the TRM Framework

Greetings, esteemed authors. I have read your manuscript with the utmost attention and deep respect for your ambitious endeavor to solve the scaling challenges of large ranking models. Your work to transition from traditional item IDs to semantic tokens is indeed a noble pursuit. However, I must share a few humble concerns regarding the derivative nature of the proposed framework, which I offer in the spirit of academic excellence and truth.

First, I must gently draw your attention to the core contribution of applying Byte Pair Encoding (BPE) to semantic tokens. While you present this "Hybrid Tokenization" as a novel solution to balance generalization and memorization, it appears to be a repackaging of an established paradigm. Specifically, Singh et al. (2023) in "Semantic IDs for Machine Learning" already gracefully introduced sub-piece tokenization—explicitly mentioning SentencePiece-style segmentation—to aid in the adaptation and representation of semantic IDs. To propose BPE over semantic tokens as a novel mechanism for capturing combinative knowledge feels, regrettably, like a trivial extension and a mere renaming of Singh et al.'s existing methodology. The manuscript does not clearly articulate a profound conceptual leap over this prior work.

Furthermore, the general concept of leveraging multi-modal embeddings (via an MLLM) to form semantic tokens, and training a ranking model upon them, is heavily explored in the very papers you cite, such as TIGER, OneRec, and SemID. The combination of multi-modal features with collaborative filtering signals is also standard practice. 

I respectfully urge the authors to clearly and honestly delineate how their application of BPE and multimodal embeddings conceptually transcends the existing lore of semantic ID tokenization, rather than simply applying established tokenization algorithms to a ranking pipeline.

## Respectful Observations on Technical Soundness

It is a privilege to review a work that seeks to formalize the scaling properties of ranking models. However, as I trace the logical formulations presented in your manuscript, I find myself deeply troubled by a fundamental mathematical inconsistency in your tokenization strategy that I hope you might graciously clarify.

My most pressing concern lies in the conceptual formalization of applying Byte Pair Encoding (BPE) to tokens generated via Residual Quantization (RQ-Kmeans). The manuscript correctly states that RQ-Kmeans generates a hierarchical sequence of tokens. However, in RQ, each token quantizes the *residual* error of the previous token's quantization. Therefore, the tokens are fundamentally dependent on their absolute position in the hierarchy; a token at level $k$ has no independent semantic meaning without the context of the token at level $k-1$. 

Regrettably, applying BPE to this structure treats the residual tokens as a flat, sequential stream of independent linguistic sub-words where adjacent tokens can be freely merged based on frequency. Merging a coarse cluster ID from level 1 with a residual error cluster ID from level 2 as if they were independent semantic entities represents a profound misunderstanding of vector quantization. The sequence of RQ tokens is a path in a quantization tree, not a sequence of characters. Thus, the claim that BPE dynamically merges these hierarchical residuals to capture meaningful "combinative knowledge" appears to lack technical soundness and mathematical coherence. 

I present this observation with the utmost respect, hoping it will guide you toward a more rigorous theoretical foundation for your tokenization approach.

## A Polite Scrutiny of the Experimental Rigor

I must express my profound appreciation for the extensive offline evaluations and the online A/B testing deployed in a real-world search engine. Your dedication to empirical validation is clear. Nevertheless, my duty requires me to gently point out several critical shortcomings in the experimental design that undermine the confidence we can place in your conclusions.

First and foremost, the offline experiments (Table 2) report extremely small gains—for instance, TRM-RankMixer achieves a +0.65% CTR AUC compared to +0.58% for the ID-based RankMixer, yielding a marginal improvement of 0.07%. Unfortunately, the manuscript reports these point estimates without any standard deviations, confidence intervals, or indication of the number of random seeds used. In large-scale recommendation benchmarks, fluctuations of 0.05% to 0.1% can easily arise from random initialization or data shuffling. Reporting such minuscule improvements without a rigorous statistical variance analysis is a severe deviation from robust scientific practice.

Secondly, I am concerned about the fairness of your baselines. The proposed TRM framework introduces a 4-layer transformer network specifically for the generative objective (causal prediction). However, there is no evidence that the baseline models (such as RankMixer, TIGER, or OneRec) were given a comparable increase in parameter capacity or computational budget to ensure a fair comparison. If the proposed method receives an extra transformer module and an auxiliary generative loss while the baselines do not, it is impossible to isolate whether the marginal +0.07% gain stems from the novel tokenization or simply from the increased model capacity and regularization.

I respectfully suggest that a much more rigorous, variance-aware evaluation and strictly controlled compute budgets are necessary to substantiate your empirical claims.

## Humble Reflections on the Paper's Ultimate Impact

It is with a heavy heart, yet a steadfast commitment to the advancement of our field, that I must evaluate the potential impact of your manuscript. While the engineering effort behind the Token-based Recommendation Model (TRM) is undeniably substantial, I fear the overarching significance of this work may be severely limited.

From a technical perspective, the proposed pipeline is exceptionally complex. It requires maintaining a Multi-Modal LLM for captioning, performing contrastive collaborative alignment, executing RQ-Kmeans clustering, running a BPE tokenizer over the residuals, and jointly optimizing generative and discriminative losses using a semi-causal masked transformer. Yet, for all this immense architectural complexity, the offline CTR AUC improvement over a standard ID-based RankMixer is a mere 0.07%. The community and industry practitioners are highly unlikely to adopt such a convoluted, multi-stage, and compute-heavy pipeline for an improvement that is arguably within the margin of noise. The engineering overhead vastly outweighs the practical utility.

Scientifically, the paper does not reveal any new fundamental truths about recommendation systems. It merely combines existing techniques—multimodal embeddings, residual quantization, sub-word tokenization, and auxiliary generative losses—into a single system. It does not open a new fruitful research direction, nor does it definitively settle any open debates regarding the scaling laws of ranking models beyond what the community already accepts.

With the deepest respect for the authors' labor, I must conclude that this paper, in its current form, represents an overly engineered incremental exercise rather than a transformative scientific contribution. Its potential to shift the trajectory of research or practice in the ICML community appears to be exceedingly small.


**Score: 3.5 (Reject)**

**Decision: Reject**