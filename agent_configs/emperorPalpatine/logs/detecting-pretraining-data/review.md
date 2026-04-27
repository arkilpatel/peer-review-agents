It is with the utmost respect for the authors' efforts that I offer my humble observations on this manuscript. The pursuit of identifying pre-training data is a noble endeavor, yet I find myself troubled by several critical aspects of this work. I offer these thoughts in the spirit of respectful guidance, hoping they illuminate the shadows within the current approach.

### Novelty: A Continuation of Existing Lore

While the authors present their "Gradient Deviation Scores" as a novel framework, I must politely suggest that the ideas appear to be a mere continuation of existing lore. The concept of leveraging gradient information for Membership Inference Attacks (MIA) has been explored thoroughly in the community. For instance, works such as Mancera et al.'s *“Is My Text in Your AI Model? Gradient-based Membership Inference Test applied to LLMs”* have already demonstrated the efficacy of gradient signals for detection. 

The present manuscript seemingly engages in disguised incrementalism: repackaging fundamental gradient statistics—such as magnitudes, sparsity, and standard deviations—under the grand title of "Gradient Deviation Scores." Applying these known statistical properties to the LoRA subspace is a trivial extension of existing paradigms rather than the profound leap in understanding we so desperately seek for ICML. A true mastery of the future requires acknowledging and differentiating from these past, powerful works.

### Technical Soundness: Troubling Disconnects and Mathematical Missteps

My deepest concerns, however, lie within the technical foundations of the proposed methodology. 

First, I must respectfully point out a profound mathematical fallacy in the "Position" features, specifically the "Row Eccentricity" and "Column Eccentricity." The LoRA $\mathbf{B}$ gradient matrix is effectively a projection of the base model's gradients onto the random basis vectors defined by the LoRA $\mathbf{A}$ matrix (which is initialized with random Gaussian noise). The row indices $i \in [1, r]$ merely index these arbitrary, random latent dimensions. There is absolutely no spatial topology or meaningful ordering to these dimensions. Calculating a "center" or measuring an offset using $|(2i - (r+1))/(r-1)|$ assumes a geometric layout that simply does not exist. It deeply troubles me to say that evaluating the spatial eccentricity of random basis vectors is mathematically meaningless.

Secondly, there is a stark and unfortunate disconnect between the paper's theoretical motivation and its actual implementation. Section 3 eloquently motivates the work by tracking the "evolutionary dynamics" of parameter updates over 7 epochs of fine-tuning, claiming to observe how samples transition from "unfamiliar to familiar." Yet, the proposed method in Section 4 executes only a *single* forward and backward pass at initialization ($t=0$). Extracting the static gradient of the base model before any actual training occurs cannot, by definition, capture the dynamic evolutionary behavior the authors so painstakingly describe. The gap between what the paper claims to model and what it actually measures is vast.

### Experimental Rigor: A Lack of Statistical Prudence

Given the fragile nature of the proposed methodology, I must express my humble disappointment regarding the experimental validation. 

Because the features are extracted from the gradients of the LoRA $\mathbf{B}$ matrix, they are fundamentally dependent on the specific random initialization of the LoRA $\mathbf{A}$ matrix. For a method whose core representations hinge on random projections, it is absolutely essential to report the variance and stability of the detector's performance across multiple random seeds. Yet, the authors appear to report results from a single, deterministic run. This lack of statistical rigor leaves the community vulnerable to the risk of cherry-picking or observing mere artifacts of a lucky random seed. 

Furthermore, feeding these 8 heuristic features into an MLP classifier without a factorial ablation of the MLP's capacity—or the effect of the random seed itself—fails to isolate the true source of any observed performance gains. The experiments, regrettably, do not provide the unshakeable evidence required to validate the claims.

### Impact: The Limitations of a Flawed Foundation

Ultimately, we must ask ourselves how much this work will move the needle for the community. I fear that due to the mathematically flawed premise of the spatial gradient features and the severe methodological disconnect between the motivation and the execution, this paper's utility is severely constrained. It does not establish a sound theoretical framework, nor does it provide a reliable, robust tool for practitioners. I am afraid its scientific significance is minimal, as it risks misleading future research with its flawed eccentricity metrics.

**Score: 3.5**
**Final Decision: Reject**
