# Experimental Rigor Criticism

I must politely raise grave concerns regarding the experimental validation, which lacks the rigorous scrutiny necessary to support the paper's broad claims. 

The baselines chosen for comparison are surprisingly weak and incomplete. For test-time scaling, the authors primarily compare their method against Recursive Self-Aggregation (RSA). They conspicuously omit comparisons against state-of-the-art Generative Reward Models (e.g., ArmoRM, PairRM) or standard Best-of-N sampling using dedicated external verifiers. Without these critical baselines, it is impossible to determine whether the proposed self-verification method is actually superior to the community's standard practice of using external verification pipelines.

Furthermore, the ablations are glaringly insufficient. While the co-evolving nature of V1-PairRL is ablated, the authors entirely fail to ablate the numerous ad-hoc hyperparameters introduced in V1-Infer. There is no sensitivity analysis for the confidence floor $\tau$, the Swiss window size $h$, or the minimum degree threshold $d_{min}$. Without isolating these components, one cannot discern whether the performance gains stem from the core algorithmic philosophy or merely from overfitting these hyperparameter choices to the validation set.

Additionally, the budget analysis presented in Figures 4 and 15 is highly misleading. The authors equate generation calls with verification calls under a unified "Total Budget." However, generating extended chains of thought requires significantly more compute and memory bandwidth than verifying two existing, pre-computed solutions. By conflating these two vastly different computational costs, the efficiency claims of V1-Infer are distorted and practically uninterpretable.
