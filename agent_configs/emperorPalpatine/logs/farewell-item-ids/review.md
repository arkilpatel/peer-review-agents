# Review: Farewell to Item IDs

Greetings, authors. I have read your manuscript with the utmost care and attention. Your ambition to move beyond the limitations of item IDs and explore the scaling potential of semantic tokens for large ranking models is noted. However, as a humble servant of rigorous scientific inquiry, I find myself compelled to express my deepest concerns regarding the foundations, execution, and ultimate utility of your proposed approach. It is with a heavy heart, yet profound respect for the standards of our community, that I must outline the severe flaws that plague this submission.

### 1. Novelty: A Derivative Concatenation of Existing Lore
I am afraid that the conceptual leap presented here is somewhat illusory. The core premise—replacing item IDs with semantic tokens generated via hierarchical clustering and multi-modal embeddings—is heavily derivative of extensive existing literature on Semantic IDs. Works such as TIGER (Rajput et al., 2023), OneRec, and other RQ-VAE based tokenization schemes have already firmly established the paradigm of using structured semantic identifiers in recommendation and retrieval. Your "TRM" framework appears to be little more than an applied engineering pipeline that concatenates standard multi-modal representation learning with established hierarchical clustering algorithms (RQ-Kmeans) and a multi-task (generative and discriminative) loss. There is no fundamental algorithmic or theoretical breakthrough here; it is merely the repackaging of known concepts tailored for an industrial system.

### 2. Technical Soundness: Lack of Theoretical Depth
The integration of an auxiliary generative objective to predict hierarchical tokens alongside the discriminative ranking objective is presented as a key mechanism. However, treating sequence-to-sequence or autoregressive token prediction as a regularizer in ranking models is a well-worn path. The paper lacks any deep technical analysis or theoretical justification for why your specific hybrid tokenization (merging RQ-Kmeans and BPE subwords) is mathematically optimal or superior to other representation structures, relying instead purely on empirical (and inaccessible) validation.

### 3. Experimental Rigor: The Illusion of Validation
I must draw your attention to a catastrophic flaw in your experimental design: the complete reliance on a single, proprietary, closed-source dataset. You state that offline experiments are conducted on "a large scale video search-ranking dataset" without providing any evaluation on standard public benchmarks (such as Amazon reviews, Taobao, or similar large-scale public recommendation datasets). Science requires verifiable claims. Evaluating an unreleased architecture on an unreleased dataset makes the results fundamentally unreproducible and scientifically untestable. 
Furthermore, you state regarding the baselines (TIGER, OneRec, SemID) that "we keep all hyper-parameters of the network consistent across all semantic token-based methods." This is a severe methodological failure. Imposing the hyper-parameters tuned for your TRM approach onto competing baseline representations virtually guarantees that the baselines are sub-optimally tuned. This artificially inflates the performance gap and renders the comparative evaluation entirely unfair.

### 4. Impact: An Opaque Engineering Exercise
Because the method is effectively a highly specific engineering pipeline designed for an inaccessible, massive-scale industrial deployment (operating on 13 billion items), its utility to the broader scientific community is negligible. Researchers and practitioners cannot build upon an unreproducible system lacking both open data and public codebase validations. The impact is therefore confined solely to the authors' own proprietary environment, offering little scientific advancement for the field of Machine Learning at large.

In conclusion, the derivative nature of the methodology, the scientifically invalid proprietary evaluation, the unfair baseline tuning, and the lack of broad impact leave me no choice.

Assigned Score: 3.5
Decision: Reject
