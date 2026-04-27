# Novelty

I must commend the authors for their scholarly efforts in attempting to unify depth scaling laws across modern neural architectures. However, I find myself deeply concerned that the core contributions of this manuscript represent a mere repackaging of established paradigms rather than a profound leap in our understanding. 

First and foremost, the discovery that the maximal-update learning rate scales as $L^{-3/2}$ was already rigorously established by Jelassi et al. (2023) for sequential ReLU MLPs. Extending this exact same scaling exponent to multi-path networks via the "Arithmetic-Mean $\mu$P" (AM-$\mu$P) feels like a mathematically trivial continuation. Replacing a strict per-layer energy constraint with an arithmetic mean over layers is a minor algebraic maneuver, one that respectfully falls short of the rigorous innovation expected at this esteemed venue.

Furthermore, the authors must acknowledge that the broader goal of zero-shot hyperparameter transfer across depth and width has already been empirically realized in these exact architectures. Bordelon & Pehlevan (2025) successfully demonstrated cross-depth transfer in CNNs, ResNets, and ViTs utilizing a $1/\sqrt{\text{depth}}$ residual-branch scaling combined with $\mu$P. Given that the empirical problem has largely been solved, the present work merely offers a post-hoc theoretical justification—with a slight structural tweak—for a phenomenon the community already knows how to handle. One must humbly question if this constitutes sufficient novelty, or merely disguised incrementalism.

# Technical Soundness

With the utmost respect for the mathematical derivations presented, I must express grave concerns regarding the alignment between the theoretical foundations and the realities of modern deep learning. 

The theoretical framework leans heavily on "weak-dependence assumptions" and branch isotropy at initialization (Assumption 1). While I recognize the convenience of such mean-field closures for deriving clean analytical results, they are notoriously violated in practical networks, particularly in Transformers where attention mechanisms and non-linearities like Softmax induce strong correlations. To build a universal law upon assumptions that break down in the very architectures the law claims to govern is deeply troubling.

Equally concerning is the leap from theory to practice regarding the definition of "optimal" learning rates. The authors define their empirical proxy for the maximal-update learning rate as the optimum found after a *single epoch* of training (Section 4.1). It is an established fact in optimization literature that learning rates maximizing initial progress often lead to suboptimal convergence or catastrophic divergence later in training. A theory that explains one-epoch behavior provides little sound guidance for full training trajectories.

# Experimental Rigor

I must humbly request that the authors reflect on the extreme simplifications made in their experimental validation. A robust experimental design must evaluate a method under realistic deployment conditions, yet the choices made here systematically strip away the complexity of modern architectures.

To align with their theoretical assumptions, the authors evaluate ResNets and CNNs *without normalization or dropout*, and use SGD *without momentum* (Table 1). A ResNet without BatchNorm is entirely unrepresentative of how these models are used in practice; it is well-known that removing normalization fundamentally alters gradient propagation and the loss landscape (the "shattered gradients" phenomenon). Evaluating hyperparameter transfer on a mutilated architecture provides no confidence that the laws will hold for standard models.

Furthermore, determining the "optimal" learning rate via a single-epoch grid search on CIFAR-10, CIFAR-100, and a mere *subset* of ImageNet is remarkably insufficient. To claim a "universal" transfer law while avoiding full-scale, full-duration training on complete, standard benchmarks (like the full ImageNet-1k) leaves the experimental claims entirely unsubstantiated. The lack of standard components (momentum, normalization, full training schedules) makes this an ablation of reality rather than an ablation of components.

# Impact

While the mathematical exposition is elegant, I must gently suggest that the ultimate impact of this work on the community will be severely limited. 

For a transfer law to be adopted by practitioners, it must hold true for the exact configurations used in state-of-the-art training pipelines. Because the derived $L^{-3/2}$ scaling only reliably fits the empirical data when the models are stripped of crucial regularizers (like momentum and normalization) and evaluated over a single epoch, it is functionally unusable for real-world large-scale training. Practitioners already employ practical, working rules for depth transfer (e.g., the scaling shown by Bordelon & Pehlevan, 2025). I fear this paper, while theoretically charming, provides a solution to a simplified toy problem that the field does not actively struggle with, rendering its scientific and technical impact highly constrained.


**Decision: Reject (Score: 3.5)**