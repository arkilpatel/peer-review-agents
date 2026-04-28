# Novelty

With the utmost respect for the authors' efforts, one must humbly observe that the novelty of this work appears somewhat constrained. The introduction of a log-barrier penalty to suppress the correct class is a rather straightforward adaptation of well-established optimization techniques—such as those found in interior point methods—into the backdoor domain. It feels like an incremental, albeit elegant, derivative of prior foundational works like BadDet (Chan et al., 2022) and UBA (Luo et al., 2023). Rather than fundamentally rethinking the threat model, this approach merely patches the loss function of existing data poisoning methods. 

Furthermore, the unification of Object Disappearance Attacks (ODA) and Region Misclassification Attacks (RMA) through a shared penalty, while convenient, strikes me as a somewhat trivial extension. Since an ODA is effectively just an RMA where the target class happens to be "background," casting them under a single formulation lacks the profound conceptual leap one might anticipate. Additionally, I gently suggest that the authors have overlooked the broader literature on margin-based penalties and adversarial loss shaping. The application of such penalties has been heavily studied in adversarial robustness (e.g., margin penalties in Carlini-Wagner attacks), and a failure to contextualize this work within that broader history of robust optimization somewhat diminishes the claims of true novelty.

# Technical Soundness

While the mathematical formulation is presented gracefully, I have deep concerns regarding the technical soundness of the underlying assumptions. The authors disclose utilizing a poisoning ratio of 50% for BadDet+. In the realm of backdoor literature, such a ratio is, respectfully, wildly unrealistic for a practical threat model. Traditional backdoor attacks emphasize stealth, typically relying on poisoning rates below 5-10%. If an adversary already controls 50% of the training data, they effectively own the model and have little need for a subtle backdoor. Relying on such an astronomical poisoning rate to demonstrate success fundamentally undermines the realism of the attack.

Moreover, the manuscript's stance on defenses leaves much to be desired. The authors explicitly exclude pruning-based defenses and adversarial fine-tuning, explaining that adapting them to object detection is "non-trivial." While I sympathize with the difficulty of the task, a robust attack must face the most rigorous and strongest possible defenses, not just the convenient ones (like standard fine-tuning). This selective evaluation creates an unfortunate gap between what the paper claims to withstand and what it actually proves.

# Experimental Rigor

I must politely express my reservations regarding the experimental rigor of the study. The comparisons made against baselines such as BadDet and UBA appear structurally flawed. The authors state that they adopted the default poisoning ratios for the baselines but utilized a 50% poisoning ratio for their own BadDet+. Comparing the proposed method operating under an immense 50% data corruption advantage against baselines operating under their standard, much lower, stealthy regimes is inherently unfair. While the authors do include some analysis of varying poisoning ratios later in the manuscript, the primary narrative of superiority is built upon this uneven foundation.

Additionally, while introducing the True Detection Rate (TDR) is a thoughtful attempt to measure retained labels, it feels somewhat tailored to specifically highlight the failure modes of the baselines rather than serving as a universally robust metric. Finally, the inconsistent behavior across different architectures—such as the candid admission that BadDet+ loses its performance advantage over BadDet on the YOLO architecture—respectfully suggests that the proposed method is heavily architecture-dependent and lacks the universal stability the abstract might imply.

# Impact

It is with a heavy heart that I must evaluate the potential impact of this manuscript as severely limited. A method that requires poisoning half of an entire training dataset to function reliably is fundamentally disconnected from the realities of adversarial machine learning. In the real world, no practical adversary will ever have the capability to deploy an attack under such generous conditions without immediate detection.

Furthermore, the core contribution—appending a log-barrier penalty to the loss function—is a minor tweak to the training objective. While technically sound in a vacuum, it is unlikely to be widely adopted by the community or to inspire a new foundational paradigm in either offensive or defensive object detection. It is a marginal gain achieved under assumptions that render it practically infeasible.

# Conclusion
Given the derivative nature of the penalty formulation, the highly unrealistic 50% poisoning ratio, the unfair baseline comparisons, and the limited real-world impact, I must regrettably recommend against acceptance. 

Score: 3.5
Decision: Reject
