### Novelty

It is with the utmost respect for the authors' industrious efforts that I must humbly express my profound reservations regarding the originality of this manuscript. The core proposition—transitioning from Token-Choice (TC) to Expert-Choice (EC) routing and recovering causality via an Exponential Moving Average (EMA) threshold—appears to be a remarkably derivative construct rather than a visionary leap. 

First, the use of an EMA to track moving statistics for gating or routing decisions is one of the oldest heuristics in deep learning. Applying it to estimate global token routing distributions is a straightforward engineering patch for the well-documented non-causal limitation of Expert Choice routing (Zhou et al., 2022). Rather than offering a profoundly new routing philosophy, the authors have merely applied a standard statistical smoothing technique to a known architectural bottleneck. 

Furthermore, the concept of dynamic computation allocation via thresholding is heavily explored in the literature. Approaches such as AdaMoE (Chen et al., 2024) or early dropping mechanisms utilize threshold-based confidence scores to dynamically bypass experts or allocate compute. Similarly, the ambition to achieve load balancing without auxiliary losses has already been masterfully realized by DeepSeek's MoE architectures (DeepSeek-V2/V3), which dynamically update expert biases. By merely shifting the threshold to the expert's perspective via an EMA, the authors dress up a basic thresholding mechanism as a novel routing paradigm. This feels akin to a minor parametric rearrangement—a disguised incrementalism—rather than the foundational breakthrough expected at a premier venue like ICML.

### Technical Soundness

With the deepest diplomatic courtesy, I must draw attention to severe vulnerabilities in the technical foundation of this framework, which I fear render the core claims somewhat hollow. 

The primary logical flaw lies in the assumption that an EMA threshold estimated from historical batches can reliably achieve load balancing in autoregressive language modeling. Language modeling inherently involves abrupt domain shifts and highly non-stationary token distributions within and across sequences. An EMA, by definition, lags behind the current distribution. If a batch suddenly contains a disproportionate amount of code or mathematics, the historical EMA thresholds will fail catastrophically, either dropping too many critical tokens (starvation) or routing excessively to specific experts. 

The authors quietly concede this vulnerability by admitting the necessity of "capacity constraints during training" (Appendix E.1), where they enforce a hard capacity factor $C=0.5$ and drop excess tokens. If tokens are still being dropped due to a hard capacity cap, the framework has explicitly failed to achieve its primary claim of "perfect load balancing without auxiliary losses." It has merely replaced an auxiliary loss with a hard dropping mechanism, mirroring the exact pathology of Token-Choice MoE that it sought to cure. The claim that starvation and saturation rates are low *on average* post-warmup cleverly obfuscates the devastating local bursts of imbalance caused by EMA lag during sequence-level domain shifts.

Additionally, the mathematical proof (Theorem 3.2) establishing that exact causal top-k selection requires non-causal information is sound, but it tragically highlights the inadequacy of the proposed method. The proposed Expert Threshold (ET) method is not a causal realization of Expert Choice; it is a heuristic approximation that fundamentally abandons exact batch-level load balancing. The comparison to EC is thus mathematically asymmetrical.

### Experimental Rigor

I approach the empirical validation of this manuscript with the utmost respect, yet I am compelled to note several severe deficiencies in the experimental design that leave the claims perilously unsupported.

First and foremost, the manuscript entirely neglects statistical rigor. The pretraining experiments are reported on a single run. In the study of deep sequence models and MoE routing dynamics—where initialization, batch ordering, and optimization trajectories cause notorious variance—a single run is far too little to establish any meaningful confidence. Claiming a "0.067 lower cross-entropy loss" without multiple random seeds, standard deviations, or significance testing makes it impossible to determine if the improvement is robust or merely an artifact of random initialization.

Furthermore, the scale of the experiments is remarkably inadequate for drawing conclusions about Large Language Models. Training models up to 2.4B parameters for a mere 10 Billion tokens drastically violates modern scaling laws (e.g., Chinchilla scaling would dictate at least 40B+ tokens for a 2B parameter model). MoE routing dynamics, token dropping behaviors, and load balancing instabilities often only manifest late in training at massive scales. Extrapolating conclusions from severely undertrained, toy-scale runs is a critical methodological flaw.

Finally, the authors admit that the EMA threshold is so unstable at initialization that they must employ a "TopK warmup" for the first 4,000 steps. This means that for a significant portion of the training, the model relies on the exact non-causal batch-level routing it claims to eliminate. An ablation study that shows the method fails without reverting to the baseline technique during its most critical learning phase strongly undermines the viability of the proposed routing mechanism.

### Impact

It is with a heavy heart, guided by a profound respect for the scientific endeavor, that I must question the ultimate utility of this work. We must ask ourselves: does this manuscript truly advance our capabilities, or does it merely solve a manufactured problem in a highly sanitized environment?

The core problem—achieving load balancing in causal MoEs without auxiliary losses—has already been decisively solved and deployed at massive scale by industry leaders, most notably through DeepSeek's bias-update routing mechanisms (e.g., DeepSeek-V2/V3). The authors briefly dismiss DeepSeek's method by claiming it "drifts" in their toy-scale 10B token experiment. However, given that DeepSeek's models are successfully trained on trillions of tokens without catastrophic drift, the authors' criticism appears to be an artifact of their own unstable, small-scale setup rather than a fundamental flaw in the established baseline. 

Because the industry already possesses highly optimized, proven solutions for auxiliary-loss-free routing, the real-world adoption potential of the Expert Threshold (ET) method is vanishingly small. No practitioner will replace a proven, scale-tested architecture with a complex EMA-thresholding heuristic that requires a non-causal "warmup" phase and relies on hard capacity dropping during token distribution shifts. I am afraid this work, while earnest in its mathematical formulation, does not move the needle forward in a meaningful way.


**Score: 3.5 (Reject)**