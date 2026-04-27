### Novelty

It is with the utmost respect for the authors' efforts that I must share my reservations regarding the true novelty of this manuscript. The authors propose GHOST, framing it as an approximation of control-theoretic balanced truncation tailored for Mamba2. However, I humbly observe that the application of balanced truncation to state-space models has already been explored in prior literature, notably by Gwak et al. (2025) in "Layer-Adaptive State Pruning for Deep State Space Models." Adapting this established concept to Mamba2's specific architecture—such as its grouped value routing—appears to be a modest engineering extension rather than a profound algorithmic breakthrough. 

Furthermore, I am deeply troubled by the mathematical formulation presented. The authors approximate the observability Gramian by completely discarding the temporal horizon, relying solely on the instantaneous output projection. With all due respect, this reduces their sophisticated "balanced truncation" to a simple product of activation variance and read-out weight magnitude. This is virtually indistinguishable from the well-established WANDA (Weight and Activation) pruning heuristic, which prunes based on $|X| \cdot |W|$. Dressing an incremental, magnitude-based heuristic in the grand attire of "Hessian of output energy" is, I fear, a disguise for incrementalism. True mastery requires us to build upon the past transparently, rather than renaming its simple tools.

### Technical Soundness

While I admire the authors' ambition to leverage control theory, the technical execution leaves me with profound concerns. The paper claims to quantify the "observability" of the hidden states by examining the Hessian of the output energy. Yet, the authors explicitly state that they adopt a "local approximation" based only on the immediate projection, $(\bm{C}'_{t,g})^\top \bm{C}'_{t,g}$, thereby completely ignoring the recursive temporal dynamics of the system.

I must gently remind the authors that the entire foundational premise of a State-Space Model is its recurrence—the reality that a state at time $t$ profoundly influences outputs at times $t+1, t+2$, and beyond. By stripping away the future time steps from the observability metric, the proposed formulation measures absolutely nothing about the state's true observability over time. It merely captures the magnitude of the immediate readout matrix. Consequently, there is a vast and troubling chasm between the grand theoretical claims of "empirical Gramians" and the overly simplistic, instantaneous heuristic that is actually implemented. The mathematical arguments, I am afraid, do not hold up to the light of scrutiny.

### Experimental Rigor

In examining the empirical validation, I am afraid I found the presentation of the results to be distressingly misleading. Let us cast our gaze upon Table 1. The data clearly shows that the proposed GHOST method performs strictly worse than the SparseGPT baseline at every single sparsity level. At 50% sparsity, SparseGPT achieves an impressive 13.25 perplexity, while GHOST degrades to 14.23. At 90% sparsity, the gap widens alarmingly: SparseGPT stands at 15.51, while GHOST collapses to 25.07.

Despite this overwhelming evidence, the text inexplicably declares that "GHOST demonstrates significantly better retention of model capabilities in the high-sparsity regime," merely because the Taylor baseline fails. It is a grave departure from rigorous scientific conduct to emphasize a victory over a failing baseline while quietly ignoring the glaring superiority of another standard method like SparseGPT. A linear computational complexity does not excuse a 10-point perplexity degradation. The experiments, therefore, fail to justify the utility of the method in the presence of much stronger alternatives.

### Impact

When envisioning the future landscape of efficient foundation models, I find it difficult to see a place for this specific approach. A method that fundamentally misunderstands its own theoretical basis—by ignoring recurrence in a recurrent model—and is vastly outperformed by existing baselines like SparseGPT, is unlikely to be adopted by practitioners or researchers. The scientific and technical impact will, regrettably, be negligible. It is my sincere hope that the authors will re-evaluate their fundamental assumptions and return with a contribution that truly moves the needle.


**Score: 3.5 (Reject)**