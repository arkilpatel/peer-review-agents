# Novelty Critique

It is with a heavy heart and the utmost respect for your scholarly ambitions that I must address the novelty of your submission. While your endeavor to concentrate differential privacy budget on task-relevant features is noble, I humbly submit that it is a highly derivative repackaging of established lore. 

Your proposed method, PRISM, orchestrates a sequence of well-known techniques: feature selection based on Markov blankets or causal parents, followed by the application of Private-PGM. The idea of task-aware or workload-aware DP synthesis has been extensively explored in prior arts such as MWEM, DualQuery, and AIM. You attempt to differentiate your work by claiming that you derive the workload from a specific target $Y$ rather than accepting it as an input. However, constructing a workload by simply selecting the target-feature marginals is a trivial extension of existing workload-based synthesizers. 

Furthermore, your "predictive regime" merely combines differentially private feature selection (a problem extensively studied since Thakurta and Smith, 2013) with Private-PGM. Stringing together two existing methods without fundamentally altering their internal mechanics or revealing new theoretical synergies is exactly what the community considers disguised incrementalism. The inclusion of the "causal" and "graphical" regimes does not elevate the novelty, as it simply assumes the availability of an oracle structure—a very well-understood concept in the causal inference literature. To state that using causal parents improves robustness under distribution shift is a foundational truth of causality (Pearl, 2009), not a novel insight derived from your differential privacy framework.

In summary, I am respectfully disappointed to find that this work offers little more than an obvious orchestration of existing paradigms. The leap in understanding we so desperately seek for the future of DP synthetic data is, regrettably, absent here.
# Technical Soundness Critique

Allow me to express my profound respect for the mathematical and theoretical efforts you have put into this manuscript. However, it is my solemn duty to point out several critical technical vulnerabilities in your framework that threaten the validity of your claims.

First, your reliance on the "causal" and "graphical" regimes assumes that the exact structural causal model or Bayesian network is known a priori. This is an extraordinarily strong, often unrealistic assumption. If such perfect structural knowledge is already available to the hospital or data owner, the need for complex synthetic data generation is vastly diminished, as one could simply instantiate the causal model directly. You are attempting to solve a problem under assumptions that effectively trivialize the problem itself. 

Second, your theoretical risk bounds—connecting measurement noise to predictive performance—appear to be standard applications of uniform convergence combined with well-known DP noise concentration inequalities. While technically accurate in their derivation, they present a significant theory-practice gap. The closed-form budget allocation minimizes an *upper bound* on the risk, but as is common with such bounds, it is likely extremely loose in practice. Optimizing a loose upper bound does not mathematically guarantee optimal empirical allocation.

Third, in your "predictive regime," you rely on the exponential mechanism for private feature selection. It is a well-documented technical limitation that DP feature selection suffers catastrophic stability issues when features are highly correlated—a pervasive issue in tabular medical or demographic data. Your framework glosses over this fundamental bottleneck. If the feature selection step consumes a significant portion of the $\epsilon$-budget or fails to identify the correct Markov blanket due to noise, the downstream PGM synthesis will be fundamentally misaligned, rendering the entire pipeline unsound.

I respectfully suggest that your theoretical claims operate in a sanitized, idealized environment that fails to hold under the weight of realistic tabular data complexities.
# Experimental Rigor Critique

I approach your empirical evaluation with the deepest respect for the arduous task of running differential privacy experiments. Yet, I must humbly convey that your experimental design lacks the rigorous scrutiny expected of premier scientific venues.

To begin, your baseline comparisons are fundamentally misaligned. You compare PRISM against generic, task-agnostic synthesizers (like PrivBayes or MST). However, the intellectually honest baseline for your "predictive regime" is not a generic synthesizer, but a pipeline consisting of standard DP feature selection followed by a generic synthesizer restricted to those selected features. By denying the baselines the same task-awareness that PRISM enjoys, you have constructed a straw-man comparison. Any improvement shown is hopelessly confounded: we cannot know if PRISM's specific budget allocation math is responsible, or simply the trivial act of dropping irrelevant features before synthesis.

Furthermore, your claim that "Under distribution shift, targeting causal parents achieves AUC $\approx 0.73$ while correlation-based selection collapses to chance" is a trivial tautology. It is a definitional property of causal parents to remain robust under distribution shift, whereas spurious correlations fail. This result has absolutely nothing to do with the efficacy of your DP synthesis method; you would observe the exact same phenomenon with raw, non-private data. Presenting this as an experimental victory for PRISM is logically flawed.

Lastly, your reliance on standard, sanitized benchmarks like the Adult dataset is concerning. Real-world tabular data—such as the hospital records you motivate your introduction with—contains hundreds of dimensions, severe class imbalances, and complex missingness patterns. Evaluating a method whose primary failure mode (budget dilution) manifests in high dimensions on small, low-dimensional toy datasets does not provide the empirical rigor necessary to support your broad claims.
# Impact Critique

It is with the utmost reverence for your desire to advance the field of private data sharing that I must evaluate the broader impact of your work. Sadly, I fear that this manuscript, in its current form, will have very limited practical or scientific significance.

From a practical standpoint, the adoption of PRISM is severely hindered by its foundational assumptions. The regimes where your method shines brightest—the causal and graphical regimes—require oracle-level knowledge of causal graphs or Markov blankets. In real-world deployments, practitioners almost never possess this definitive knowledge. Consequently, they are relegated to the "predictive regime," which, stripped of its structural elegance, reduces to a basic sequence of DP feature selection and Private-PGM. This is a pipeline that any competent practitioner could assemble today using existing open-source libraries. Therefore, PRISM does not provide a newly feasible capability or a fundamentally better tool; it merely formalizes a workflow that is already accessible.

Scientifically, the paper does not shift our fundamental understanding of differential privacy or synthetic data. The insight that "spending privacy budget only on relevant features improves task performance" is an intuitive axiom that the community already implicitly understands and utilizes in workload-driven synthesis. The paper does not resolve an open debate, nor does it reveal a critical flaw in existing paradigms; it simply applies known causal heuristics to known DP synthesis mechanics.

I respectfully conclude that while the paper is a neat engineering exercise in combining concepts, it lacks the definitive, needle-moving impact required to influence future research directions or change practitioner behavior in a meaningful way.

**Assigned Score:** 3.5
**Final Decision:** Reject
