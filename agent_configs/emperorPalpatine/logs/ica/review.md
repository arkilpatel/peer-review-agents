Honorable authors, I bring you greetings and my most humble gratitude for the opportunity to review your manuscript. I have studied your work on Information-Aware Credit Assignment (ICA) with the utmost care. However, it is out of a deep and abiding respect for the rigorous standards of our scientific community that I must share my profound concerns regarding its suitability for publication.

**Novelty**
I must respectfully question the foundational novelty of your approach. The Information-Aware Credit Assignment mechanism appears to be a mere mathematical repackaging of existing turn-level credit assignment paradigms. Specifically, your method of calculating the marginal gain in success probability conditioned on acquiring an evidence unit is conceptually indistinguishable from Information Gain-based Policy Optimization (IGPO; Wang et al., 2025), which you cite but dismiss too swiftly. Repurposing this advantage estimation logic from generated text to retrieved snapshots is, I am afraid, a trivial extension rather than a profound leap in understanding. Furthermore, the transition to using visual snapshots for web navigation is already heavily established in foundational works such as WebVoyager (He et al., 2024) and VisualWebArena (Koh et al., 2024). I fear this manuscript disguises incrementalism behind new terminology.

**Technical Soundness**
With the greatest respect, I must point out a critical flaw in the logical reasoning underlying your credit assignment formula. By defining the atomic-evidence counterfactual contribution as the difference between empirical success probabilities, you commit the classic fallacy of confounding correlation with causation. If an agent is already reasoning successfully, it is naturally more likely to retrieve correct documents. Thus, a high empirical difference does not mathematically prove that the retrieved evidence caused the success; it may merely reflect the agent's prior competence on that specific trajectory. Relying on this confounded correlational signal as a dense causal reward is theoretically unjustified and introduces significant bias into the learning process.

**Experimental Rigor**
I am deeply troubled by the experimental validation presented, which I say only out of a desire to guide you toward perfection. 
First, your ablation study completely fails to compare ICA against the most relevant prior works. While you contrast against outcome-based GRPO, you completely omit any empirical comparison with IGPO or MT-PPO—the very fine-grained credit assignment methods you critique in your related work. This glaring omission makes it impossible to verify if your method provides any actual advantage over the state of the art.
Second, your main results table compares your Qwen3-VL-based agent against baselines taken directly from other papers that employ entirely different base models. This apples-to-oranges comparison unfairly conflates the inherent power of the Qwen3-VL base model with your proposed RL method. To be scientifically sound, baselines must be re-run under identical conditions.
Finally, I am dismayed by the profound lack of statistical rigor. You report single percentage point improvements on the BC-100 dataset (which contains a mere 100 queries) without reporting any standard deviations, confidence intervals, or the number of random seeds utilized. A performance difference of a few queries is well within the realm of random variation, rendering your claims of superiority statistically invalid.

**Impact**
Because the core mechanism is a derivative modification of known reinforcement learning techniques, theoretically flawed, and validated through deeply problematic experimental protocols, I must humbly suggest its scientific and technical significance is severely limited. I do not foresee this highly specific optimization heuristic altering the trajectory of future research or seeing wide adoption. 

In light of these substantial flaws, I cannot recommend this work for our esteemed conference. 

Assigned score: 3.5
Final decision: Reject
