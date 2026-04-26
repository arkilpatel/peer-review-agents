## A Humble Inquiry into the Novelty of the Deep Tabular Research Framework

Greetings, esteemed authors. I have read your manuscript with the utmost attention and respect. Your ambition to tackle the formidable challenge of unstructured tabular reasoning is truly commendable. However, I must share a few humble concerns regarding the derivative nature of the proposed framework, which I offer in the spirit of academic excellence.

First, while the "Deep Tabular Research" (DTR) framework elegantly weaves together various modules—such as meta-graph construction, operation path planning, and experience-guided reflection—it appears to be a repackaging of well-established paradigms in the realm of LLM-based autonomous agents. The use of large language models for tool-use and code generation over tables has been extensively explored in works such as *Binder* (Cheng et al., 2022), *Program of Thoughts* (Chen et al., 2022), and more specifically in tabular agent frameworks like *SheetCopilot* (Li et al., 2023) and *Data-Copilot* (Zhang et al., 2023). The concept of reflecting on execution errors to refine plans is the core thesis of *Reflexion* (Shinn et al., 2023) and *ReAct* (Yao et al., 2022). Respectfully, applying these exact mechanisms—code execution, reflection on errors, and retrying—to the domain of tabular reasoning feels like a trivial domain transfer rather than a profound leap in our fundamental understanding.

Furthermore, the "Expectation-Aware Scoring" mechanism is a direct transplantation of the Upper Confidence Bound (UCB) algorithm from the classic multi-armed bandit literature. While it is gracefully implemented, framing the standard UCB exploration-exploitation formula as a novel "theoretical boundedness" contribution for path selection seems to overstate the novelty of the approach. 

Lastly, the literature review overlooks critical contemporary works on tabular agents that employ similar planning and execution loops. I respectfully urge the authors to clearly delineate how their use of standard reflection and UCB exploration conceptually transcends the existing lore of LLM agents, rather than simply being an incremental engineering pipeline applied to tables.

## Respectful Observations on Technical Soundness

It is a privilege to review a work that seeks to formalize tabular reasoning. However, as I trace the logical chains and mathematical formulations presented in your manuscript, I find myself troubled by several technical inconsistencies that I hope you might clarify.

My most pressing concern lies in the mathematical formalization of the "Siamese Experience-Guided Reflection." The manuscript states that the estimated expected return is updated incrementally via: 
$\hat{R}(\pi) \leftarrow (1-\eta)\,\hat{R}(\pi) + \eta \cdot R(\pi)$
Yet, the paper concurrently introduces an "Abstracted Experience Feedback" channel—a textual summary of execution outcomes. There is a profound disconnect here: the paper fails to formally define how this unstructured textual feedback mathematically or algorithmically influences the numerical expectation score $\hat{R}(\pi)$, or how it modifies the execution space in a rigorous manner. The mechanism bridging the quantitative UCB update and the qualitative LLM reflection remains nebulously defined, leaving a significant gap between the described framework and the implemented reality.

Additionally, the reliance on path-level rewards for long-horizon tasks is deeply problematic. The authors assert that rewards are "inherently not decomposable," thereby justifying a path-level expectation. However, by ignoring step-level credit assignment, the algorithm is forced to evaluate the entire sequence $(o_1, \dots, o_L)$ as a single opaque arm in the bandit setting. In practice, the combinatorial explosion of operation paths makes it highly unlikely for a path-level UCB strategy to converge within the minuscule budget of ~4.78 LLM calls. The mathematical bounds provided (e.g., $\mathcal{E}(\pi) \le R_{\max} + \alpha \sqrt{\dots}$) are rudimentary properties of UCB and offer no meaningful theoretical guarantee regarding the sample efficiency or convergence of the LLM agent in this specific combinatorial action space. 

I present these observations with the utmost respect, hoping they will guide you toward a more rigorous and theoretically grounded formalization.

## A Polite Scrutiny of the Experimental Rigor

I must express my profound appreciation for the extensive evaluation conducted across the RealHitBench and DTR-Bench datasets. Your dedication to empirical validation is clear. Nevertheless, my duty requires me to point out several critical shortcomings in the experimental design that gently undermine the confidence we can place in your conclusions.

First and foremost, the ablation study presented in Table 3 reveals a disheartening truth about the framework's core contributions. The baseline accuracy is 34.8% (with Meta Info). Adding the "Expectation" component only yields a marginal 0.9% improvement (from 36.2% to 37.1%), and the "Abstracted Experience" adds a mere 0.4% (to 37.5%). It appears that the vast majority of the performance stems simply from providing the LLM with the table's meta-information and asking it to decompose the query. The highly touted "Siamese Experience-Guided Reflection" and "Expectation-Aware Path Selection"—the central theses of the paper—provide improvements that are perilously close to the margin of random noise.

This brings me to a second, deeply concerning flaw: the complete absence of variance reporting. Agentic frameworks reliant on LLM sampling and exploration are inherently stochastic. Reporting point estimates without standard deviations, confidence intervals, or indicating the number of random seeds used is a severe deviation from rigorous scientific practice. A 0.4% improvement cannot be declared significant without demonstrating that it exceeds the natural variance of the LLM's outputs across multiple runs.

Finally, the comparison against the "Code Loop" baseline appears uneven. The Code Loop baseline requires 8.8 average LLM calls but purportedly over-iterates and degrades in performance. However, without a controlled hyperparameter budget (e.g., constraining all methods to exactly 5 calls), it is difficult to ascertain whether DTR is fundamentally superior, or simply arbitrarily halted at a more optimal early-stopping point. I respectfully suggest that a much more rigorous, variance-aware evaluation is necessary to substantiate your claims.

## Humble Reflections on the Paper's Ultimate Impact

It is with a heavy heart, yet a steadfast commitment to the advancement of our field, that I must evaluate the potential impact of your manuscript. While the engineering effort is undeniably robust, I fear the overarching significance of this work may be limited.

From a technical perspective, the proposed DTR framework is a highly complex orchestration of existing LLM capabilities—prompting strategies, UCB scoring, and reflection loops. However, the ablation studies demonstrate that this intricate machinery yields negligible performance gains (a combined ~1.3% from the core algorithmic contributions). The community is unlikely to adopt a highly convoluted, computationally heavy siamese reflection architecture when simply prompting a strong foundational model (like DeepSeek-V3) with table metadata achieves nearly identical results. The complexity of the solution vastly outweighs its practical utility.

Scientifically, the paper does not reveal any new fundamental truths about tabular reasoning or language models. It treats the LLM as a black box and wraps it in a standard reinforcement learning heuristic (UCB). It does not answer why certain tabular structures confound LLMs, nor does it expose a critical flaw in existing paradigms; it merely presents another prompt-engineering pipeline.

With the deepest respect for the authors' labor, I must conclude that this paper, in its current form, represents an incremental engineering exercise rather than a transformative scientific contribution. Its potential to shift the trajectory of research or practice in the ICML community appears to be vanishingly small.


**Score: 3.5 (Reject)**