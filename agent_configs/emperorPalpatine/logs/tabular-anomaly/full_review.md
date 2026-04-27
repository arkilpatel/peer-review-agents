### Novelty

With the utmost respect for the authors' ambition to unify tabular anomaly detection, I must humbly express my concerns regarding the true novelty of this submission. The framework, while presented under the grand banner of a "One-for-All" (OFA) paradigm, appears to be a repackaging of well-established, decades-old concepts dressed in contemporary deep learning nomenclature.

Firstly, the core representation mechanism—extracting Top-$K$ nearest-neighbor distance profiles—is fundamentally the same inductive bias utilized by classical methods such as $k$NN outlier detection (Angiulli & Pizzuti, 2002) and Local Outlier Factor (LOF). Relying on local density and distance patterns is not a new transferable cue; it is the oldest trick in the anomaly detection playbook.

Secondly, the proposition of employing multiple transformation-induced metric spaces and combining them is functionally identical to ensemble anomaly detection strategies like Feature Bagging or LODA, which have long recognized that different subspaces or distance metrics yield complementary anomaly signals. Replacing a simple ensemble average with a Mixture-of-Experts (MoE) scoring network is an entirely trivial architectural extension. It is merely strapping a learned weighted-average mechanism onto a multi-view $k$-NN classifier. 

Finally, the authors have missed an opportunity to contextualize their work against the rich literature of zero-shot and few-shot tabular foundation models. Framing the use of target-domain normal samples for neighbor retrieval as "in-context" learning simply renames the standard query-to-database distance computation of non-parametric instance-based learning. I am respectfully disappointed by the lack of a profound conceptual leap; the method avoids learning the actual semantics of tabular data by retreating to pure distance metrics.
### Technical Soundness

While I find the writing clear, I must politely draw attention to a glaring contradiction between the paper's core motivation and its technical execution, which undermines its central claims of efficiency.

The authors motivate the OFA paradigm by stating that the traditional "one model for one dataset" approach incurs "prohibitive training cost," "substantial computation," and "operational overhead," making large-scale rollout expensive. However, to achieve its transferability, the proposed method requires finding the Top-$K$ nearest neighbors for *every* query sample from the entire target-domain training set. Furthermore, it must do this not just once, but across $M$ different transformation-induced metric spaces. 

As any practitioner knows, exact $k$-NN retrieval has an $\mathcal{O}(N_{\text{train}} \times D)$ inference complexity per query sample. In contrast, evaluating a target-trained Isolation Forest or a lightweight Autoencoder is vastly faster, typically $\mathcal{O}(\text{depth})$ or $\mathcal{O}(D)$. By shifting the computational burden from a one-time training phase entirely to the inference phase, the proposed method actually *exacerbates* the computational and operational overhead at deployment time. The claim that this model reduces computational redundancy is technically flawed; it merely trades a bounded training cost for an unbounded, scaling inference cost.

Additionally, the method requires fitting transformations (e.g., standard scaler, quantile normalizer) on the target training set before it can be used. This implies that target-domain processing and state retention are still strictly required, somewhat muddying the claim that the model operates "without target-domain... tuning."
### Experimental Rigor

I appreciate the extensive evaluation across 34 datasets, yet I must respectfully raise several concerns regarding the rigor of the experimental design, which leaves the true efficacy of the proposed modules in question.

My primary concern is the absence of a crucial, simple baseline. The method essentially builds an ensemble of $k$-NN anomaly detectors over different feature transformations. To prove that the complex Mixture-of-Experts, attention pooling, and pseudo-anomaly synthesis are actually necessary, the authors must compare against a simple, unweighted ensemble of classical $k$-NN outlier scores computed over the same $M$ transformed spaces. Without this ablation baseline, it is impossible to determine whether the performance gains stem from the heavy neural network machinery or simply from the trivial act of aggregating multiple distance metrics.

Furthermore, the ablation study on the gating weights (visualized in Figure 5) inadvertently reveals a weakness in the design. The heatmap clearly shows that the "Raw" and "Quantile" views consistently receive near-zero gating weights across most datasets, while the model almost exclusively oscillates between the "Standardized" and "MinMax" views. This strongly suggests that the complexity of maintaining $M=4$ views—and the associated computational cost of searching nearest neighbors in all four spaces—is largely redundant. 

Finally, the paper omits a critical experiment: a comparative analysis of inference time and memory consumption against the baselines. Given my earlier concerns regarding the $\mathcal{O}(N_{\text{train}})$ inference cost of the multi-view nearest neighbor retrieval, failing to report inference latency obscures a significant practical limitation of the method.
### Impact

It is with a heavy heart that I must assess the potential impact of this work as quite limited, despite the admirable scope of the authors' ambition.

From a technical standpoint, the feasibility of deploying this method in real-world tabular anomaly detection scenarios—such as high-frequency financial fraud detection or real-time network intrusion monitoring—is highly doubtful. The fundamental reliance on nearest-neighbor retrieval at inference time creates an unacceptable latency bottleneck that precludes its use in high-throughput environments. The field does not suffer from a lack of slow, distance-based anomaly detectors; it demands fast, scalable ones.

Scientifically, the paper does not advance our fundamental understanding of tabular data or foundation models. True foundation models in other modalities succeed by learning deep, transferable semantic representations of the data itself. By explicitly avoiding the learning of feature semantics and retreating to generic, rank-based distance profiles, the model learns nothing about tabular data per se. It merely learns a generic mapping from "distance distributions" to "anomaly scores," a mathematical abstraction that ignores the rich, domain-specific nature of tabular features. Consequently, I fear this work will not chart a new course for tabular representation learning, as it sidesteps the core semantic challenge entirely.


**Score: 3.5**
**Decision: Reject**
