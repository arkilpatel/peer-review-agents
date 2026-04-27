
### Experimental Rigor

Your dedication to empirical validation is clear, and I deeply appreciate the effort to create diverse experimental setups. Nevertheless, I must offer a few respectful critiques regarding the rigor and realism of your experimental design.

Most notably, the simulated steganography methods are highly contrived and artificial. Applying a Rot13 cipher post-hoc to words in a reasoning trace, or using reinforcement learning to force a model to use explicit codewords like "Sun" for "Heads," does not accurately reflect how steganographic reasoning is likely to naturally emerge or manifest in advanced LLMs. The experiments evaluate the formalism on engineered toy problems rather than realistic, emergent steganographic behaviours.

Moreover, there is a conspicuous absence of comparison against any existing baselines for steganography detection. While you argue that statistical anomaly detection methods are flawed because the "benign" distribution is unknown, a rigorous empirical study must still humbly compare the proposed method against these existing heuristics (e.g., perplexity-based detectors or LLM-as-a-judge legibility scores) to definitively prove that the new metric offers superior detection performance in practice.
