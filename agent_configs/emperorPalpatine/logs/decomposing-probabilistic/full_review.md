### Novelty

While I read this manuscript with the utmost respect for the authors' mathematical diligence, I must humbly submit that the core ideas appear to be a mere continuation of existing lore rather than a profound leap forward. 

The primary contribution—decomposing proper scoring rules into miscalibration, grouping loss, and irreducible uncertainty—is undeniably elegant, yet it heavily treads upon well-established paradigms. Specifically, the concept of "grouping loss" and its fundamental tension with calibration was already articulated with great clarity by Tasche (2021, "Calibrating sufficiently"). Furthermore, the explicit three-term decomposition of the expected loss into miscalibration, grouping loss, and irreducible feature-level uncertainty was already formalized for classification by Perez-Lebel et al. (2023, "Beyond calibration: estimating the grouping loss of modern neural networks"). 

The manuscript extends these prior works to arbitrary proper losses and nested information levels via a chain rule. However, with the greatest of respect, this extension feels like a somewhat trivial mathematical step. It is a long-established fact in statistical forecasting that strictly proper scoring rules behave analogously to Bregman divergences (e.g., Gneiting and Raftery, 2007). Consequently, applying the tower property of conditional expectation to yield an "information-level chain rule" is a direct and expected consequence of these known geometric properties. I am respectfully disappointed, as a more profound conceptual revelation was anticipated rather than a repackaging of known Bregman divergence properties under a new notational guise.
### Technical Soundness

The mathematical derivations presented in this work are executed with commendable precision, and I applaud the authors for their formal rigor. However, I must politely express my concerns regarding the depth and foundational implications of these theoretical claims.

The manuscript presents Theorem 2.1 and Theorem 2.2 as general decompositions. While technically sound, these theorems are essentially restatements of the fundamental properties of proper scoring rules—specifically, their equivalence to expected Bregman divergences and the ensuing generalized Pythagorean theorems. The "chain decomposition" is a straightforward application of the law of total expectation to these divergences. Consequently, there is a subtle gap between the paper's framing of these identities as novel theoretical insights and the reality that they are direct corollaries of classical decision theory (dating back to Savage, 1971). 

Furthermore, I must gently question the logical reasoning surrounding the interpretation of recalibration. The paper notes that recalibration cannot reduce grouping loss (information loss), which is mathematically true. Yet, the framing suggests this is a new diagnostic lens, whereas it is a well-understood tautology: a monotonic transformation of a score cannot magically recover features that were already discarded by the compression $\boldsymbol{X} \to S$. Presenting this fundamental axiom of information theory as an actionable, newly derived insight slightly overstates the theoretical contribution.
### Experimental Rigor

I turn now to the experimental validation, examining it with the careful scrutiny that such a foundational topic deserves. I must humbly express my profound concerns regarding the empirical rigor of this work.

Firstly, the real-world validation relies exclusively on a single dataset in the main text: the venerable, yet remarkably small, \textsc{GermanCredit} dataset (comprising a mere 1000 instances). Evaluating modern calibration paradigms on such a limited and outdated benchmark fails to represent the complexities of contemporary machine learning tasks. It is gently suggested that a much broader and more diverse suite of datasets is required to substantiate any empirical claims.

Secondly, the statistical rigor in reporting is unfortunately lacking. Table 1 presents single-point estimates for the Brier score and LogLoss without any standard deviations, confidence intervals, or indications of variance from multiple random seeds. Given that the reported Brier score improvements are minuscule (e.g., changes of 0.01 or exactly 0.00), it is mathematically impossible to determine whether these are true effects or merely statistical noise. A robust experimental design must report variance to be considered scientifically valid.

Most alarmingly, the recalibration procedure severely degrades the LogLoss of the "Average" model, skyrocketing from 0.52 to 0.75 (Table 1). The authors politely dismiss this as a "finite-sample phenomenon" where nonparametric monotone recalibration introduces distortions. However, from a rigorous experimental standpoint, this indicates a severe overfitting issue due to a poorly tuned baseline. If a proposed methodology (or diagnostic illustration) performs drastically worse than doing nothing, it is a significant experimental design flaw to leave it unaddressed rather than comparing against simpler, properly regularized baselines like Platt scaling.
### Impact

In considering the ultimate significance of this manuscript, I must offer my most respectful, yet candid, assessment. While the paper is beautifully written, its potential to shift the trajectory of the field appears exceedingly limited.

From a scientific perspective, the paper does not answer an open question or settle a debate. The community is already keenly aware that proper scoring rules encompass both calibration and refinement (resolution), and that post-hoc recalibration does not improve a model's discriminative power (grouping loss). Because the theoretical framework is a repackaging of Perez-Lebel et al. (2023) and Tasche (2021) generalized via standard Bregman divergence properties, it does not provide a fundamentally new understanding of the problem.

From a technical and practical perspective, the paper does not introduce a widely adoptable tool, a new calibration algorithm, or a definitive benchmark. Practitioners already understand that they must retain rich feature representations rather than compressing them prematurely if they wish to preserve information. I fear that three years from now, this paper may not fundamentally change how researchers design or evaluate probabilistic classifiers, as it merely restates known limitations of recalibration in a more generalized notation.


**Score: 3.5**
**Decision: Reject**
