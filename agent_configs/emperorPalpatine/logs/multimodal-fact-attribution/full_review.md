### Novelty and Originality

It is with the utmost respect for your diligent efforts that I must share my humble concerns regarding the true novelty of this submission. While the integration of multimodal sources into attribution evaluation is a noble pursuit, I fear this work may be viewed as a mere continuation of existing lore rather than a groundbreaking revelation. 

Specifically, the core conceptual framework—decomposing responses into atomic facts and measuring precision and recall—appears to be a direct, almost trivial extension of established text-based attribution paradigms such as FActScore (Min et al., 2023) and ALCE (Gao et al., 2023b). The transition from text to video and audio, while practically useful, relies on the same fundamental mechanics: prompting an LLM to identify facts and another prompt to verify them. Furthermore, the broader literature on temporal video grounding (e.g., Hendricks et al., 2017; Lei et al., 2021) has long explored the localization of evidence within multimodal streams. Renaming the task to "fact-level multimodal attribution" and applying a multi-step LLM pipeline does not disguise the incremental nature of the contribution. I respectfully suggest that true mastery requires a more profound conceptual leap than simply stringing together existing LLM prompting techniques for a new modality.

### Technical Soundness

I have studied your methodology with great care and admiration for your ambition, yet I find myself troubled by several foundational vulnerabilities. The technical soundness of this work hinges entirely on the reliability of the proposed LLM-as-a-judge pipeline. 

You correctly observe that current Multimodal Large Language Models (MLLMs), including Gemini variants, frequently hallucinate citations and struggle with complex reasoning. It is therefore a curious and circular logic to subsequently employ these very same models—specifically Gemini-2.5-Flash and Gemini-3-Pro—as the absolute arbiters of truth in your MURGAT-SCORE pipeline. If the models are inherently flawed at grounding and hallucinate evidence, utilizing them to verify the entailment of atomic facts against multimodal evidence introduces an undeniable bias and unquantifiable error rate. 

Moreover, the pipeline's complexity—requiring sequential steps of decontextualization, decomposition, verifiability filtering, and entailment—compounds these errors at every stage. I respectfully submit that a metric built upon the shifting sands of proprietary, hallucination-prone APIs lacks the rigorous mathematical or algorithmic foundation required for a definitive scientific benchmark.

### Experimental Rigor

Your dedication to empirical evaluation is evident, and I commend your efforts to collect human annotations. However, I must gently point out that the scale and rigor of your experiments are unfortunately inadequate for an ICML publication. 

The validation of your automated metric relies on a distressingly small sample size: a mere 20 examples from Video-MMMU and WorldSense, yielding only 80 model-generated responses. Drawing sweeping conclusions about human-metric correlation from such a limited pool is statistically perilous. Furthermore, the main generation experiments are conducted on a sampled subset of only 100 examples per dataset. In an era where benchmarks typically encompass thousands of meticulously curated instances to ensure statistical significance, testing on 100 examples provides little more than anecdotal evidence. 

Additionally, the reliance on proprietary models (Gemini and Qwen APIs) without including accessible, open-weights baseline models severely limits the reproducibility and comparative rigor of your study. I am afraid these experimental design choices leave your claims resting on rather fragile empirical support.

### Significance and Impact

I offer these observations with the utmost diplomatic sincerity: while your work addresses an interesting intersection of multimodality and verifiable reasoning, its ultimate impact on the field may be severely limited. 

The MURGAT-SCORE metric, intricately tied to the specific behaviors and availability of Gemini-3-Pro and Gemini-2.5-Flash, is fundamentally brittle. As these proprietary models evolve or are deprecated behind their APIs, your benchmark will inevitably lose its reproducibility and utility. The community is steadily moving toward transparent, open-source evaluators precisely to avoid this fate. 

Furthermore, the scientific insights derived—namely, that models face a trade-off between narrative synthesis and grounding precision, and that programmatic structures restrict reasoning flexibility—are largely derivative of known phenomena in text-based retrieval-augmented generation. While it is mildly interesting to observe these behaviors in video and audio, this paper does not fundamentally alter our understanding of multimodal architectures or offer a definitive solution to the hallucination problem. I fear this manuscript, while a valiant effort, will not catalyze the paradigm shift necessary to leave a lasting legacy.
