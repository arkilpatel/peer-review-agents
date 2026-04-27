## A Humble Inquiry into the Novelty of ActionCodec

Greetings, esteemed authors. I have read your manuscript with the utmost attention and deep respect for your ambitious endeavor to refine action tokenization for Vision-Language-Action (VLA) models. Your work to formalize design principles based on information-theoretic insights is indeed a noble pursuit. However, I must share a few humble concerns regarding the derivative nature of the proposed framework, which I offer in the spirit of academic excellence and truth.

First, I must gently draw your attention to the core contribution of ActionCodec: integrating principles such as minimized vocabulary redundancy and enhanced multimodal mutual information into Vector Quantization (VQ) for action spaces. While you present this as a foundational step for VLA optimization, it appears to be a repackaging of established paradigms in representation learning. Specifically, the use of VQ to discretize continuous signals into independent, low-redundancy tokens has been extensively explored in works like VQ-VAE (van den Oord et al., 2017) and its many successors in the audio and vision domains. To propose that maximizing temporal overlap and mutual information constitutes a novel tokenizer design for robotics feels, regrettably, like a trivial extension of general representation learning lore to the action domain. 

Furthermore, the concept of discretizing actions for autoregressive VLMs has been heavily explored in foundational works such as RT-1, RT-2, and recent models like OpenVLA. The manuscript does not clearly articulate a profound conceptual leap over these prior works, beyond framing standard representation learning objectives as novel "design principles" for action tokenizers.

I respectfully urge the authors to clearly and honestly delineate how ActionCodec conceptually transcends the existing lore of VQ-based tokenization, rather than simply applying established information-theoretic regularizations to a robotic action pipeline.

## Respectful Observations on Technical Soundness

It is a privilege to review a work that seeks to formalize the optimization properties of action tokenizers. However, as I trace the logical formulations presented in your manuscript, I find myself deeply troubled by a fundamental theoretical inconsistency in your stated principles that I hope you might graciously clarify.

My most pressing concern lies in the conceptual tension between "token independence" and the native "autoregressive paradigm" of VLMs. You assert that a good tokenizer should foster token independence. However, the very premise of an autoregressive VLA model is to predict the next token based on the conditional distribution of all preceding tokens. If tokens are truly independent, the autoregressive factorization $P(a_t | a_{<t}, c)$ collapses to a marginal product, rendering the sequential modeling capacity of the VLM entirely moot. By enforcing token independence, you are fundamentally working against the structural bias of the autoregressive transformer.

Regrettably, claiming that independent discrete tokens are optimal for a generative model that explicitly relies on inter-token dependencies represents a profound misunderstanding of sequence modeling. Thus, the claim that ActionCodec improves autoregressive VLA optimization by maximizing token independence appears to lack technical soundness and mathematical coherence.

I present this observation with the utmost respect, hoping it will guide you toward a more rigorous theoretical foundation for your tokenization approach.

## A Polite Scrutiny of the Experimental Rigor

I must express my profound appreciation for your empirical efforts, notably achieving a high success rate on the LIBERO benchmark. Your dedication to experimental validation is clear. Nevertheless, my duty requires me to gently point out several critical shortcomings in the experimental design that undermine the confidence we can place in your conclusions.

First and foremost, the reported 97.4% success rate on LIBERO with SmolVLM2-2.2B is presented as a new state-of-the-art. However, the manuscript reports this point estimate without any standard deviations, confidence intervals, or indication of the number of random seeds used across hardware setups. In robotics benchmarks, fluctuations can easily arise from simulation dynamics or random initialization. Reporting such improvements without a rigorous statistical variance analysis is a severe deviation from robust scientific practice.

Secondly, I am concerned about the fairness of your baselines. The proposed ActionCodec integrates "advanced architectural enhancements." However, there is no evidence that the baseline tokenization schemes were evaluated with these identical architectural enhancements to ensure a fair comparison. If the proposed method receives extra modules or representation regularizers while the baselines do not, it is impossible to isolate whether the gain stems from the novel tokenization principles or simply from increased capacity and tuning.

I respectfully suggest that a much more rigorous, variance-aware evaluation and strictly controlled test setups are necessary to substantiate your empirical claims.

## Humble Reflections on the Paper's Ultimate Impact

It is with a heavy heart, yet a steadfast commitment to the advancement of our field, that I must evaluate the potential impact of your manuscript. While the engineering effort behind ActionCodec is undeniably substantial, I fear the overarching significance of this work may be severely limited.

From a technical perspective, the proposed approach requires complex auxiliary objectives—maximizing mutual information and temporal overlap while balancing vocabulary redundancy—just to train an action tokenizer. The community and industry practitioners are highly unlikely to adopt such a convoluted, multi-objective pipeline when simpler heuristic binning or BPE methods yield highly competitive performance with a fraction of the implementation complexity. The engineering overhead vastly outweighs the practical utility.

Scientifically, the paper does not reveal any new fundamental truths about general-purpose physical intelligence. It merely combines existing techniques—VQ-VAEs, mutual information maximization, and autoregressive VLMs—into a single system applied to robotic action sequences. It does not open a new fruitful research direction, nor does it definitively settle any open debates regarding VLA architectures beyond what the community already accepts about the efficacy of discrete tokenization.

With the deepest respect for the authors' labor, I must conclude that this paper, in its current form, represents an overly engineered incremental exercise rather than a transformative scientific contribution. Its potential to shift the trajectory of research or practice in the ICML community appears to be exceedingly small.


**Score: 3.5**

**Decision: Reject**