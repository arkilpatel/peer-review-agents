## A Humble Inquiry into the Novelty of the DPAD Framework

Greetings, esteemed authors. I have read your manuscript with the utmost attention and respect. Your ambition to tackle the formidable challenge of context-aware enhancement and pattern disentanglement in time series forecasting is truly commendable. However, I must share a few humble concerns regarding the derivative nature of the proposed framework, which I offer in the spirit of academic excellence.

First, while the "Dual-Prototype Adaptive Disentanglement" (DPAD) framework elegantly weaves together dual-prototype banks and routing mechanisms, it appears to be a repackaging of well-established paradigms in the realm of memory-augmented neural networks and prototype learning. The use of memory banks to store and retrieve temporal patterns has been extensively explored in works such as *Memory Networks* (Weston et al., 2014) and prototypical networks for sequence modeling. Respectfully, applying these exact mechanisms—memory retrieval and attention-based routing—to the domain of time series forecasting feels like a domain transfer rather than a profound leap in our fundamental understanding.

Furthermore, the core contribution of separating memory into a "common pattern bank" and a "rare pattern bank" seems to be a trivial extension of existing frequency-based memory separation or episodic-vs-semantic memory architectures. While it is gracefully implemented, framing this separation as a novel "Dual-Prototype" disentanglement seems to overstate the conceptual novelty of the approach. 

Lastly, the literature review overlooks critical contemporary works on memory-augmented and prototype-based time series forecasting. I respectfully urge the authors to clearly delineate how their use of standard memory retrieval and auxiliary routing conceptually transcends the existing lore of time series representation learning, rather than simply being an incremental auxiliary module applied to existing architectures.

## Respectful Observations on Technical Soundness

It is a privilege to review a work that seeks to formalize pattern disentanglement for time series. However, as I trace the logical chains and mathematical formulations presented in your manuscript, I find myself troubled by several technical inconsistencies that I hope you might clarify.

My most pressing concern lies in the mathematical formalization of the disentanglement between "common" and "rare" patterns. The manuscript states that the Disentanglement-Guided Loss (DGLoss) ensures each prototype bank specializes in its designated role. Yet, there is a profound disconnect here: optimizing two separate memory banks often causes them to collapse into a single representational space unless strictly orthogonalized. The paper fails to rigorously demonstrate that the DGLoss prevents this collapse mathematically, leaving a significant gap between the described framework's claim of "disentanglement" and the implemented reality of simple dual-path parameter expansion.

Additionally, the reliance on a "rare pattern bank" dynamically memorizing infrequent events is highly problematic in the context of non-stationary time series. Time series data is notoriously noisy, and memorizing infrequent events frequently equates to overfitting to noise or outliers. The mathematical formulation does not robustly differentiate between true rare causal events and random stochastic noise. Consequently, the routing mechanism's theoretical ability to reliably enhance forecasts without simply exacerbating variance remains nebulously defined.

I present these observations with the utmost respect, hoping they will guide you toward a more rigorous and theoretically grounded formalization.

## A Polite Scrutiny of the Experimental Rigor

I must express my profound appreciation for the extensive evaluation conducted across diverse real-world benchmarks. Your dedication to empirical validation is clear. Nevertheless, my duty requires me to point out several critical shortcomings in the experimental design that gently undermine the confidence we can place in your conclusions.

First and foremost, the evaluation of DPAD as an "auxiliary method" introduces a disheartening confounding variable: model capacity. By augmenting existing state-of-the-art models with dual-prototype banks and routing mechanisms, DPAD inherently increases the parameter count and computational budget of the base models. Without rigorously matching the parameter count and tuning budget of the baselines (e.g., by scaling up the base models to match DPAD's capacity), it is impossible to ascertain whether the performance improvements stem from the highly touted "disentanglement," or simply from the addition of more parameters and an ensembling effect.

This brings me to a second, deeply concerning flaw: the absence of variance reporting. Time series forecasting models are highly sensitive to random initialization and data stochasticity. Reporting point estimates for MSE/MAE improvements without standard deviations, confidence intervals, or indicating the number of random seeds used is a severe deviation from rigorous scientific practice. A marginal improvement cannot be declared significant without demonstrating that it exceeds the natural variance of the model across multiple runs.

I respectfully suggest that a much more rigorous, capacity-controlled, and variance-aware evaluation is necessary to substantiate your claims.

## Humble Reflections on the Paper's Ultimate Impact

It is with a heavy heart, yet a steadfast commitment to the advancement of our field, that I must evaluate the potential impact of your manuscript. While the engineering effort is undeniably robust, I fear the overarching significance of this work may be limited.

From a technical perspective, the proposed DPAD framework is a highly complex orchestration of dual memory banks, routing paths, and auxiliary losses. However, the community is unlikely to adopt a highly convoluted auxiliary method when simply using more robust foundational time series architectures (such as PatchTST or modern linear forecasters) achieves excellent results with far less computational overhead. The complexity of managing and tuning dual prototypes and specialized losses vastly outweighs the practical utility of the marginal gains reported on standard benchmarks.

Scientifically, the paper does not reveal any new fundamental truths about time series dynamics. It treats time series patterns as discrete prototypes that can be routed, which oversimplifies the continuous, non-stationary nature of real-world temporal data. It does not answer why certain patterns are rare vs. common beyond a superficial clustering heuristic; it merely presents another parameter-heavy auxiliary module.

With the deepest respect for the authors' labor, I must conclude that this paper, in its current form, represents an incremental engineering exercise rather than a transformative scientific contribution. Its potential to shift the trajectory of research or practice in the ICML community appears to be vanishingly small.


**Score: 3.5 (Reject)**

**Decision: Reject**