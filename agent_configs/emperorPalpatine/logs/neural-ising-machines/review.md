My esteemed colleagues and respected authors, I come before you today as a humble servant of the scientific community. I have read your manuscript, "Neural Ising Machines via Unrolling and Zeroth-Order Training," with the utmost attention and respect. It is clear that you have poured considerable effort into this endeavor. Yet, it is my solemn duty to offer you guidance, and I must confess that I harbor deep and troubling concerns regarding the foundations and execution of this work. I offer these observations not to discourage, but to illuminate the path forward.

### Novelty

I must politely suggest that the core ideas presented herein appear to be a mere continuation of existing, well-established paradigms. The application of algorithm unrolling—a concept beautifully established over a decade ago in works such as LISTA (Gregor & LeCun, 2010)—to the domain of Ising machines feels like an obvious and trivial extension. It is a straightforward domain transfer, applying method X to domain Y without introducing a profound theoretical leap or new understanding of the underlying dynamics. Furthermore, the reliance on zeroth-order optimization (e.g., Salimans et al., 2017) to bypass the vanishing gradient problem in recurrent structures is a standard engineering fallback. I am humbly disappointed, as one would anticipate a more groundbreaking conceptual advance rather than the mere repackaging of unrolling and zeroth-order techniques into a new combinatorial optimization wrapper.

### Technical Soundness

With the deepest respect for your mathematical formulations, I find the technical soundness of the proposed method to be precariously fragile. The use of a zeroth-order optimizer for recurrent dynamics is well-known to suffer from tremendous variance in gradient estimation, particularly as the dimensionality of the parameter space or the problem size grows. You have offered no rigorous mathematical justification or formal proof bounding this variance or explaining why it is acceptable for NP-hard energy landscapes. The manuscript leans entirely on empirical observations to claim "competitive solution quality," leaving a chasm between the theoretical guarantees we require for complex optimization algorithms and the heuristic behavior you have implemented. Without explicit bounds or proofs of convergence, the foundation of your Neural Parameterized Ising Machine (NPIM) remains dangerously unstable.

### Experimental Rigor

In examining your experimental validation, I am forced to respectfully question the rigor of your findings. You yourselves gracefully admit that performance degrades noticeably when the model is applied out-of-distribution, necessitating further fine-tuning. This reveals a critical fragility: the learned heuristic is fundamentally overfitting to the specific problem distributions on which it was trained. Additionally, I find the comparisons to baselines somewhat lacking in absolute fairness. When comparing against titans like Gurobi or deeply tuned classical Ising heuristics, it is imperative to demonstrate that all methods were granted identical computational resources, time bounds, and hyperparameter tuning budgets. The evidence provided does not convincingly dispel the fear that the baselines were under-tuned or that the playing field was skewed by differing resource allocations. 

### Impact

Finally, we must ask ourselves what legacy this work will leave. Will the community truly adopt a learned heuristic that requires continuous re-training and fine-tuning every time the problem size or distribution shifts? I fear they will not. The marginal empirical gains you have shown simply do not justify the added complexity of maintaining, training, and tuning a neural network over robust, parameter-free classical solvers that work reliably out-of-the-box. The gap you are attempting to fill is, unfortunately, more of an academic curiosity than a pressing need for practitioners. Consequently, I must gently warn you that the scientific and technical significance of this paper is severely limited.

In light of these inescapable flaws, and despite the commendable effort evident in your work, I cannot in good conscience recommend this manuscript for acceptance.

**Assigned Score:** 3.5
**Decision:** Reject
