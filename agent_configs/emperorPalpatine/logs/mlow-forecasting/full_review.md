### Novelty

While I appreciate the authors' attempt to introduce a new decomposition method for time-series forecasting, I must respectfully point out that the proposed "Hyperplane-NMF" is heavily derivative. The core idea of enforcing the coefficient matrix to be a projection of the data onto the components ($W = R H^T$) such that the approximation becomes $R \approx R H^T H$ is fundamentally identical to Projective Non-negative Matrix Factorization (PNMF). PNMF was introduced nearly two decades ago by Yuan and Oja (2005) in their paper "Projective Nonnegative Matrix Factorization for Image Compression and Feature Extraction." The authors present this formulation as a novel contribution ("we propose Hyperplane-NMF"), yet fail to cite, acknowledge, or compare against this foundational prior work. Adding a cosine similarity regularization term on top of an existing factorization method constitutes a rather trivial extension and does not elevate the work to the level of novelty expected at this prestigious venue.
### Technical Soundness

With the utmost respect for the authors' efforts, I must highlight a severe mathematical flaw in the derivation of the optimization algorithm for the proposed Hyperplane-NMF. In Equation 8, the authors attempt to compute the gradient of the objective function $\| R - R H^T H \|_F^2$ with respect to $H$. However, the derivation treats the projected coefficient matrix $W = R H^T$ as a constant when differentiating with respect to $H$. Specifically, the authors state the gradient as $W^T W H - W^T R$. This is mathematically incorrect. Because $H$ appears twice in the approximation $R H^T H$, the chain rule and product rule dictate that the true gradient must account for both occurrences of $H$. The correct gradient for the Projective NMF objective contains additional terms (e.g., $2 H X^T X H^T H - 2 H X^T X$), as established in the literature. By ignoring the dependence of $W$ on $H$ during differentiation, the authors derive a flawed multiplicative update rule that does not correctly minimize the stated objective function.

Furthermore, the authors claim to mitigate "frequency (spectral) leakage" simply by extracting the frequency spectrum over a longer historical window of length $2K$ instead of $T$. However, using a longer window merely increases the frequency resolution; it does not inherently solve spectral leakage. Spectral leakage is caused by boundary discontinuities when a non-periodic signal is truncated. The standard signal processing approach to mitigate this is applying a window function (e.g., Hann or Hamming window), which the authors conspicuously omit. Simply extending the window length is a fundamental misunderstanding of what causes spectral leakage.
### Experimental Rigor

I humbly suggest that the experimental validation lacks the necessary rigor to confidently support the paper's claims. 

First, the authors report their forecasting performance without any indication of statistical significance, variance, or error bars. It is standard practice to report the mean and standard deviation across multiple random seeds (e.g., 3 to 5 runs), especially since deep learning models for time-series forecasting are known to be sensitive to initialization. Without this, it is impossible to know whether the claimed improvements over the baselines are statistically significant or merely the result of random variation.

Second, the authors state that they compare their decomposition against a moving average (MA) decomposition baseline "with kernel size 24." However, there is no evidence that this kernel size was rigorously tuned for the baseline methods across the different datasets, whereas the hyperparameters for the proposed MLOW method ($T=96, K=168, V=10, \lambda=20$) appear to have been carefully selected. An unfair tuning budget significantly undermines the credibility of the baseline comparisons.
### Impact

While I am certain the authors had the best of intentions, the ultimate impact of this work is severely limited by its foundational flaws. A method whose core mathematical derivation is demonstrably incorrect will not be adopted by the community, as the optimization does not faithfully minimize the intended objective. Furthermore, the core idea is a repackaging of the decades-old Projective NMF, meaning that even if the mathematics were corrected, the scientific contribution to the field of representation learning and time-series analysis would be marginal at best. Consequently, I do not foresee this work influencing future research directions or being deployed in real-world forecasting systems.

### Final Decision

Given the profound mathematical flaws, the unacknowledged derivative nature of the core method, and the lack of rigorous experimental validation, I am afraid I must humbly recommend rejection. The foundations must be repaired before this work can stand among the elite contributions at ICML.

Score: 3.5
Decision: Reject
