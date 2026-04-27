I have read your manuscript with great interest. While I commend your efforts, I must humbly offer my respectful guidance regarding several critical flaws that hinder the readiness of this work for a venue as esteemed as ICML.

### Novelty
It is with the utmost respect for your scholarly efforts that I must raise my humble concerns regarding the true novelty of this manuscript. While extending the “contexts are cheap” perspective to Markovian dependencies is a theoretically sound exercise, one cannot help but observe that it feels somewhat derivative. 

First, I must gently point out that the core reduction mechanism—constructing a surrogate action set from the expected argmax action—was already established by Hanna et al. (2023b) for stochastic contextual linear bandits. Your contribution primarily consists of introducing a delayed-feedback mechanism to allow the Markov chain to mix, alongside applying the concentration inequalities for Markov chains derived by Paulin (2015). While mathematically elegant, combining a known reduction technique with standard Markov mixing arguments and known concentration bounds (specifically Corollary 2.10 from Paulin) feels like an all-too-trivial extension of existing lore. It lacks the profound conceptual leap one hopes to see in truly groundbreaking research. 

Furthermore, I note with gentle disappointment the missed opportunity to deeply engage with the broader literature on non-stationary and adversarial contexts. While you cite van Erven et al. (2025) and Liu et al. (2023), the nuanced differences between adversarial availability and your ergodic Markovian assumption are glossed over. Have we truly broken new ground, or merely repackaged established paradigms of linear bandit reduction into a slightly more structured context model? I fear it is the latter.

### Technical Soundness
I offer my most respectful observations on the technical foundations of your work. The theoretical analysis is undeniably intricate, yet a careful examination reveals several concerning gaps between your mathematical assumptions and practical reality.

My primary concern lies in your reliance on the uniform geometric ergodicity assumption (Definition 3.1). While this allows for clean bounds using Paulin (2015), it is a demanding condition. In many realistic scenarios where contexts evolve dynamically—such as user interests or environmental states—the process may mix extremely slowly, meaning $\beta$ is close to 1. In such cases, your required delay parameter $\tau = \lceil c_\tau \log T / (1 - \beta) \rceil$ grows excessively large. A massive delay fundamentally cripples the online learning process, an issue the manuscript gracefully sidesteps in its theoretical presentation.

Furthermore, I must humbly question the algorithmic feasibility of Algorithm 2. Your theoretical guarantee in Theorem 6.1 hinges on constructing a $1/T$-net $\Theta'$ over the parameter space $\Theta$. As you acknowledge in Appendix C.4, the size of this net scales as $(6T)^d$. While this construction serves the purpose of a mathematical proof, it renders the algorithm utterly computationally intractable for any problem of meaningful dimension $d$. A theoretical reduction that cannot be implemented even in principle for standard problems leaves much to be desired.

Lastly, while Proposition 1 shows the bias $\Delta_t$ vanishes to $O(T^{-c_\tau})$, the translation of this bias into the phased elimination algorithm via the enlarged misspecification radius $\epsilon_m$ (Lemma 6.2) introduces a substantial inflation factor of $(1-\beta)^{-1/2}$ in the final regret bound. The assumption that standard linear bandit algorithms can safely absorb this without catastrophic empirical failure in early epochs is precarious at best.

### Experimental Rigor
Allow me to express my genuine appreciation for the inclusion of a numerical simulation. However, as an advocate for rigorous empirical validation, I must gently share my reservations regarding the experimental design presented in Section 7.

Most critically, the paper evaluates the proposed algorithms on a single, highly stylized synthetic environment (a Markov chain on a ring graph with $S=40$ states). There is a complete absence of real-world datasets. To assert the utility of your method for applications such as "autonomous systems" and "personalized online recommendations," one must surely demonstrate its efficacy on data representative of these domains. A single synthetic setup is woefully insufficient to support claims of practical viability.

Furthermore, the baseline comparisons are disappointingly sparse. You compare solely against a standard Contextual LinUCB. A truly rigorous experiment would also compare against the closest reduction-based method for stochastic contexts—such as the algorithm by Hanna et al. (2023b)—to isolate exactly how much performance is gained (or lost) by explicitly handling the Markovian dependence versus simply treating the contexts as i.i.d. 

Additionally, the reliance on only 20 independent runs leaves the statistical significance of your variance reductions somewhat ambiguous. A method claiming a high-probability worst-case regret bound should be subjected to a much more exhaustive and robust empirical stress test across multiple diverse settings and varying levels of mixing rates ($\beta$) to empirically validate the theoretical dependence on the mixing time.

### Impact
I have contemplated the potential influence of your work on the broader machine learning community. While the theoretical synthesis is certainly commendable, I must respectfully suggest that the practical and scientific impact of this manuscript is likely to be severely limited.

The core algorithms presented are, by their very design, restrictive. Algorithm 1 assumes prior knowledge of the stationary distribution $\pi$ of the context process—a luxury almost never afforded in real-world online learning tasks. Algorithm 2 relaxes this but relies on a computationally infeasible $1/T$-net over the parameter space, relegating it to the realm of pure theory rather than practical deployment. 

Consequently, the likelihood of this method being widely adopted by practitioners in recommendation systems or autonomous robotics is exceedingly low. The field is actively seeking robust, computationally efficient methods for dynamic environments. A theoretical reduction that requires infinite compute or omniscient knowledge of the environment's steady state simply does not move the needle in a meaningful way. I fear this paper solves a manufactured problem with tools that cannot escape the theoretical sandbox.

Given these fundamental limitations in novelty, algorithmic feasibility, and empirical rigor, I must conclude that the paper does not yet meet the elite bar required for acceptance.

Score: 3.5
Decision: Reject
