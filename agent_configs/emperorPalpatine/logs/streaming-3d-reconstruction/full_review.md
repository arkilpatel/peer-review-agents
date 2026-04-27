I have carefully read the manuscript and evaluated its contributions. While the problem domain is undoubtedly important, I must respectfully outline several profound concerns regarding the novelty, theoretical soundness, empirical validation, and ultimate impact of this work.

### Novelty

While the authors present Self-expressive Sequence Regularization (SSR) as a novel mechanism for streaming 3D reconstruction, I must respectfully express my concerns regarding the true depth of this contribution. The concept of leveraging self-expressiveness to model temporal local subspaces is heavily derivative of established literature in Non-Rigid Structure from Motion (NRSfM). Specifically, the foundational idea of using a union-of-subspaces model and self-expressive properties has already been thoroughly explored by Zhu et al. (2014) and later integrated into deep learning frameworks by Deng et al. (2022). 

The proposed method merely appropriates these existing concepts and applies them as a test-time, post-hoc correction step within a sliding window for streaming reconstruction. Calculating an affinity matrix via dot-product similarity to perform a linear combination of past states is an incremental engineering adaptation rather than a fundamental theoretical leap. Furthermore, the paper draws heavily upon the baseline architecture of CUT3R, adding what amounts to a local temporal attention mechanism under the mathematical guise of Grassmannian manifolds. I am afraid this feels like a repackaging of established paradigms rather than the profound leap in understanding that our field so desperately requires.


### Technical Soundness

The manuscript attempts to frame the state trajectory within the elegant mathematical structure of a Grassmannian manifold $\mathcal{G}(n,r)$. However, I must gently point out a significant technical incongruity between the theoretical framing and the actual algorithmic implementation. In Section 3.3, the authors discuss the projection metric for Grassmannian manifolds, which rightly involves comparing subspaces using their projection matrices. Yet, when we examine the proposed SSR update in Algorithm 1, the affinity matrix $\mathbf{C}^{(t)}$ is computed using a simple non-normalized dot product followed by a softmax-like normalization, and the state correction is performed as a direct linear combination of the latent state vectors.

A linear combination of points (subspaces) on a Grassmannian manifold does not natively yield another valid point on that manifold under standard Euclidean addition, unless one is operating within the tangent space or employing specific Fréchet mean computations. The implementation reduces to a basic Euclidean space moving-average of latent vectors based on feature similarity. Consequently, the invocation of Grassmannian manifolds appears to be a superficial theoretical veneer that does not align with the empirical reality of the algorithm. This disconnect undermines the technical soundness of the work, as the formal claims do not match the practical execution.


### Experimental Rigor

I commend the authors for their efforts in evaluating the method across various datasets, but I must politely highlight a glaring vulnerability in the experimental validation. In Table 3, when evaluating on sparse views and short sequences (7-Scenes dataset), the proposed SSR method actively degrades performance, underperforming the CUT3R baseline (e.g., Accuracy of 0.132 vs. 0.126). The authors acknowledge this limitation, attributing it to the method incorrectly merging unrelated states due to faulty affinity computations when timestamps are lacking. 

However, in real-world streaming applications, encountering dropped frames, sparse viewpoints, or erratic camera movements is incredibly common. A sequence regularization method that fundamentally breaks down under these practical conditions is inherently brittle. Furthermore, the ablation study in Table 4 reveals that increasing the temporal window size (from $k=4$ to $k=64$) yields diminishing or even negative returns. This strongly implies that the method fails to genuinely capture and leverage long-range contextual information, instead relying merely on a very short, localized window (e.g., $k=4$ or $k=8$). This directly contradicts the core claim that SSR effectively suppresses long-horizon cumulative drift. 


### Impact

While the aspiration to mitigate geometric drift in streaming 3D reconstruction is noble, the practical impact of this specific approach seems exceedingly limited. Because the SSR mechanism requires maintaining a buffer of past states and computing pairwise similarities at inference time, it introduces a computational bottleneck that scales quadratically with the window size. The authors claim "minimal computational overhead," yet edge devices and real-time streaming systems operate under strict latency and memory constraints where such overheads are non-trivial.

More importantly, given the algorithm's demonstrated brittleness in handling sparse inputs—a frequent occurrence in real-world deployments—and its inability to effectively utilize longer temporal windows without performance degradation, its utility is severely constrained. Practitioners are unlikely to adopt a regularization scheme that risks catastrophically merging unrelated states during frame drops. Consequently, the broader scientific and practical impact of this work on the 3D vision community will likely be very marginal.


In light of these substantial flaws, including the derivative nature of the approach, the stark disconnect between the theoretical framing and the algorithmic reality, and the method's brittleness in practical sparse-view scenarios, I cannot recommend this manuscript for publication at such a prestigious venue. 

**Score: 3.5 (Reject)**
