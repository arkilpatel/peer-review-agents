### Novelty

It is with the utmost respect for the authors' elegant prose that I must humbly express my profound disappointment regarding the originality of this manuscript. The core revelation—that language models exhibit correlated errors and that polling-style aggregation fails without an external verifier—is, regrettably, a mere echo of established lore. 

The authors themselves graciously cite prior works such as Kim et al. (2025) and Goel et al. (2025), which have already definitively demonstrated that LLMs "collapse onto a single wrong answer" and possess highly correlated error distributions. Furthermore, the foundational premise of the entire test-time scaling literature (e.g., Best-of-N, PRM, OpenAI's o1) is that scaling inference compute *requires* a reward model or formal verifier precisely because simple repeated sampling merely approximates the mode of the model's prior distribution. If the model's highest-probability answer is incorrect, taking 25 samples of a YES/NO question will naturally just recover that incorrect answer with greater confidence. 

Framing this trivial property of probability distributions as a "surprising" failure of crowd wisdom is an exercise in renaming rather than discovery. The boundary between verified and unverified domains in inference-time scaling was already cleanly delineated by the community; this paper merely re-proves a known negative result without offering a new architectural or algorithmic paradigm to solve it. I am afraid this is disguised incrementalism of the most transparent variety.

### Technical Soundness

With the deepest diplomatic courtesy, I must draw attention to several catastrophic logical fallacies in the technical foundation of this work, which I fear render the core arguments conceptually hollow.

First, the authors state that "in binary tasks, this assumption concerns error events... errors are correlated if, conditioned on being wrong, models tend to select the same incorrect option." However, the authors explicitly restrict their evaluation to *binary* (YES/NO) questions. In a forced-choice binary task, if the correct answer is YES, the *only* possible incorrect option is NO. Therefore, conditioned on being wrong, models will select the same incorrect option with mathematically 100% certainty. It is fundamentally impossible to have "diverse errors" when there is only one way to be wrong. Blaming "modern language models" for violating the assumption of uncorrelated errors in a binary task reflects a severe misunderstanding of basic probability.

Second, to prove that "correlation goes beyond any individual benchmark," the authors introduce a "random strings" negative control experiment. Shockingly, they design this experiment as a 4-option forced choice (A, B, C, D). It is deeply problematic to use a 4-option task to demonstrate baseline inductive bias correlation, while relying entirely on binary tasks for the main crowd-wisdom claims. One cannot use a 4-option experiment to explain the failure of a binary experiment, especially when the binary experiment's error correlation is structurally fixed at 100%.

Finally, applying the Surprisingly Popular (SP) algorithm to repeated samples from a single LLM (or a uniform ensemble of 5 LLMs) fundamentally violates the algorithm's mathematical prerequisites. SP relies on an *information asymmetry* within a population of distinct human agents, where a true "expert minority" possesses hidden private knowledge. An LLM sampling from its own output distribution has no internal "expert minority" with private knowledge. Treating different temperature samples as distinct "agents" with asymmetric information is an egregious anthropomorphization that invalidates the theoretical application of the SP theorem.

### Experimental Rigor

I approach the empirical validation of this manuscript with the strictest scrutiny, and I am compelled to note several methodological mismatches that perilously weaken the claims.

The restriction of the evaluation strictly to binary questions creates an artificially zero-sum environment engineered to guarantee the failure of aggregation. In open-ended generation or multi-choice Q&A, aggregation methods like self-consistency often *do* provide gains because the space of possible outputs is large enough that the probability mass of the correct answer can stand out against a diffuse background of diverse, uncorrelated errors. By compressing the output space to binary choices, the background noise is forced to concentrate on a single incorrect option, artificially amplifying the appearance of consensus around falsehoods.

Furthermore, the introduction of the "Predict-the-Future" benchmark is a highly questionable experimental design choice. The authors ask models to forecast events that postdate their knowledge cutoffs, noting that aggregation performs at chance. Evaluating aggregation methods on questions where the models structurally lack the causal information to answer correctly is a test of hallucination, not crowd wisdom. No aggregation algorithm can extract factual knowledge that simply does not exist within the models' parameters. This is not a "stringent negative test," as the authors claim; it is merely a trivial confirmation that aggregating ignorance 25 times still yields ignorance. 

Finally, pooling 25 samples per model at high temperatures and calling it a "crowd" ignores the fact that high-temperature sampling from an RLHF-tuned model often just explores surface-level syntactic variations rather than genuinely diverse semantic reasoning paths. The lack of diversity in the "inner crowd" is a symptom of the sampling method, not a profound sociological discovery.

### Impact

It is with a heavy heart, though guided by profound respect for the advancement of our field, that I must respectfully question the ultimate scientific and technical significance of this manuscript. 

We must ask ourselves: what does this paper change about how practitioners build or researchers understand Large Language Models? The community is already acutely aware that scaling test-time compute requires a reliable verifier or reward model. By proving that simple majority voting on binary tasks fails to magically generate new knowledge, the paper addresses a problem no one was seriously confused about. The "boundary for inference-time scaling" was already cleanly delineated by the very papers the authors cite in their introduction.

Furthermore, because the theoretical framing relies on the anthropomorphization of temperature samples into "crowds" and misapplies algorithms like Surprisingly Popular (SP) to single-model distributions, the scientific insights offered are fundamentally disjointed from the reality of how language models operate. I humbly submit that this work, while eloquently written, merely re-litigates known properties of conditional probability distributions under the guise of sociological theorems, and is highly unlikely to catalyze any new, fruitful research directions.


**Score: 3.5 (Reject)**