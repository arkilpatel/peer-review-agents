### Novelty

I have reviewed your submission with the deepest respect. However, I must humbly point out that the core conceptual leap of this manuscript—transitioning from a hard pseudo-label (Majority Voting) to a soft pseudo-label (an empirical distribution) for reward assignment—is an incredibly derivative application of foundational concepts. The practice of using soft distributions rather than hard argmax assignments has been a cornerstone of label smoothing, knowledge distillation, and self-training for decades. Furthermore, appending a standard novelty/exploration bonus to encourage rare outputs is a textbook technique from introductory reinforcement learning. I respectfully submit that combining basic soft-labeling with a standard exploration heuristic and renaming it "Distribution-Aware Reward Estimation (DARE)" disguises incremental heuristic engineering as a novel test-time adaptation framework. The community anticipates profound new methodologies, not merely the application of 1990s-era smoothing techniques to modern LLM rollouts.

### Technical Soundness

With the utmost deference to your theoretical and analytical efforts, I must raise grave concerns regarding the technical soundness of your framework. First, your "Theorem 2.1 (Information Collapse under Majority Voting)" formally proves that the argmax function discards information. This is a trivial, definitional fact of mathematics, not a profound theoretical insight requiring a formal theorem. 

More alarmingly, the logic behind your "Exploration Bonus" contains a severe heuristic contradiction. You explicitly boost rewards for "non-majority but factual correct rollouts [that] tend to exhibit low uncertainty." Because you have no ground-truth verifier at test time, you are simply rewarding outputs that the model generates rarely but with high internal token confidence. This assumes that a model's confident-but-rare generations are correct. In reality, large language models are notorious for confident hallucinations. By systematically boosting the reward of confident minority outputs without an external verifier, you are mathematically incentivizing the model to confidently hallucinate, risking catastrophic destabilization of the policy. The framework's reliance on this mathematically unfounded leap of faith renders its core mechanism technically unsound.

### Experimental Rigor

I offer my observations on your experimental design with the greatest respect, yet I must gently point out substantial flaws that compromise your empirical claims. When evaluating test-time adaptation methods that introduce multiple new hyperparameters—such as your exploration bonus weight and distribution pruning thresholds—it is imperative to demonstrate that these hyperparameters were not tuned on the test set. Because Test-Time RL operates exclusively at inference, tuning these thresholds to maximize benchmark performance introduces a severe temporal leak, invalidating the results. Furthermore, the ablation study reveals that the foundational "distribution-based reward" (without bonuses) only achieves 16.6 on AIME 2024, which is a marginal improvement over the baseline TTRL's 15.8. The remainder of the performance gap is bridged entirely by the heuristic exploration and pruning thresholds. This strongly suggests that the reported gains are the product of extensive, fragile hyperparameter tuning rather than a fundamentally superior optimization dynamic.

### Impact

It is with a heavy heart that I must assess the ultimate impact of this manuscript as severely limited. As your own Appendix C (Table 3) demonstrates, the marginal gains of this complex reward-shaping heuristic diminish significantly as the base model scales to 4B and 7B parameters. The community is rapidly moving toward more robust, scalable solutions such as learned Process Reward Models (PRMs) and verifier-guided search, which provide grounded correctness signals rather than relying on heuristic manipulation of the model's own empirical rollout distribution. I humbly suggest that tuning exploration bonuses on unverified rollouts solves a transient symptom of weak models rather than advancing the fundamental frontier of reinforcement learning. This work will not change how future research is conducted.

### Final Decision

Score: 3.5
Decision: Reject
