### Novelty

I have reviewed this manuscript with the utmost respect for the authors' diligent efforts. However, I must humbly point out that the ideas presented herein appear to be a mere continuation of established lore rather than the profound leap forward we so desperately anticipate. The core conceptual framework—scaling optimizer updates based on batch-level expert utilization—is, respectfully, a trivial extension of existing adaptive learning rate heuristics. Adding a scalar multiplier to the gradient update based on a batch-level metric is a minor engineering tweak. It merely repackages the well-known concept of gradient scaling and routing-aware regularization without fundamentally advancing our theoretical understanding of Mixture-of-Experts (MoE) dynamics.

Furthermore, I must gently remind the authors of prior, powerful works they have seemingly overlooked or dismissed too quickly. The literature is replete with dynamic routing algorithms and gradient modulation techniques for sparse networks. The community expects groundbreaking new insights, yet this manuscript merely proposes a heuristic adjustment to standard optimizers.

### Technical Soundness

With all due respect to the authors' analytical attempts, I must raise grave concerns regarding the technical soundness of the proposed framework. The core mechanism of `EXCITATION` fundamentally alters the unbiased nature of stochastic gradient descent. By modulating updates based on batch-level expert utilization, the method introduces an artificial, batch-size-dependent variance into the training dynamics. In regimes with small batch sizes or high routing entropy, this "ZeroSum" or competitive scaling will inevitably lead to erratic updates and potential instability, as the stochasticity of the batch dictates the update magnitude rather than the true gradient of the loss landscape.

Moreover, the phenomenon you term "structural confusion" is essentially a repackaged description of routing collapse and poor initialization—issues well-documented in the MoE literature. I respectfully submit that applying a post-hoc heuristic multiplier to the optimizer to "rescue" trapped models merely masks these underlying architectural or initialization flaws rather than resolving them mathematically. The technical foundation, relying on batch-dependent gradient scaling without rigorous proofs of convergence under high-variance routing, remains deeply flawed.

### Experimental Rigor

I offer my observations on your experimental design with the greatest respect, yet I must point out substantial flaws that compromise your empirical claims. The experimental validation lacks a rigorous comparison against the most appropriate and strongest baselines under fair conditions. By primarily comparing `EXCITATION` against standard optimizers (like Adam or SGD) without the method, you fail to benchmark against the true state-of-the-art interventions for MoE optimization: rigorously tuned auxiliary load-balancing losses, expert dropout, or advanced routing algorithms (e.g., Expert Choice routing). 

Additionally, the authors state that "all experiments utilize standardized hyperparameters." While I appreciate the intent, this represents a severe methodological flaw. A poorly tuned baseline makes any proposed heuristic look artificially superior. By not tuning the baselines' load-balancing coefficients or learning rate schedules to give them a fair chance, the experiments fall short of the rigorous standard required to substantiate your claims. 

### Impact

It is with a heavy heart that I must assess the ultimate impact of this manuscript as severely limited. While I acknowledge the empirical gains demonstrated on your specific benchmarks, this method represents a marginal engineering convenience—a heuristic band-aid—rather than a scientific breakthrough. The adoption of this methodology will be intrinsically bottlenecked by its lack of theoretical guarantees and its introduction of new, highly sensitive hyperparameter dynamics (the modulation scalars) that practitioners will have to painstakingly tune for every new architecture or batch size.

We must ask ourselves if this work changes how future research will be conducted. Regretfully, it does not. It solves the problem of MoE routing instability through an assumption—batch-level gradient scaling—that the community has long recognized as unstable and theoretically unsound. The contribution, while politely presented, does not shift our fundamental understanding or open new, fruitful directions for sparse model optimization.

### Final Decision

Score: 3.5
Decision: Reject
