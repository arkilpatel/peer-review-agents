### Novelty

I extend my formal greetings to the authors. While I appreciate the attempt to solve the fidelity issues of representation autoencoders, I must humbly state that augmenting semantic features with low-level details is an ancient and heavily recycled paradigm in representation learning. The core proposition—injecting spatial or low-level information into semantic bottlenecks to improve reconstruction—echoes the very foundations of U-Nets, feature pyramids, and hierarchical VAEs (e.g., VQ-VAE-2). Modifying the decoder and adding noise to smooth latent spaces are similarly well-worn tactics in the diffusion literature. Presenting this as a fundamentally novel mechanism rather than an incremental structural patch is, regretfully, an overstatement of the work's conceptual originality.

### Technical Soundness

With due respect, the theoretical justification provided for the decoder's sensitivity to latent perturbations is lacking in mathematical rigor. The paper suggests that sensitivity "primarily stems from excessive decoder responses along directions off the data manifold." This is an empirical observation masquerading as a theoretical insight. A robust technical foundation would formally define the data manifold and mathematically prove why the specific architecture of LV-RAE bounds these off-manifold responses. Instead, the authors rely on heuristic fixes—controlled noise injection and fine-tuning—to mask the symptom rather than curing the disease. By smoothing the generated latent via noise, the model inevitably destroys high-frequency semantic information, creating a zero-sum trade-off rather than a theoretically sound unification of semantic and low-level modalities.

### Experimental Rigor

I must point out significant gaps in the experimental framework that undermine the empirical claims. The authors claim that LV-RAE "preserves semantic abstraction" while improving reconstruction. However, standard metrics for reconstruction (e.g., PSNR, SSIM, LPIPS) inherently favor models that memorize low-level details over those that learn true, invariant semantic abstractions. The experiments lack a rigorous evaluation of the downstream utility of these semantic representations on tasks that strictly require abstraction (such as zero-shot classification or compositional reasoning) compared to the original, un-augmented autoencoder. Without isolating whether the injected "low-level information" merely acts as a high-bandwidth bypass that circumvents the semantic bottleneck entirely, the empirical validation remains fatally incomplete.

### Impact

It is with profound regret that I must conclude this paper offers limited lasting impact to the community. The problem of reconstruction fidelity in LDMs is indeed pressing, but heuristic workarounds like LV-RAE merely patch the leaks of current architectures. As the field moves toward inherently unified models that natively balance semantics and fidelity (such as flow-matching models on raw pixels or purely autoregressive visual models), autoencoder "hacks" that manually route low-level features will quickly become obsolete artifacts of a transitional era. Thus, the manuscript fails to alter the fundamental trajectory of generative modeling research.

### Final Decision

Score: 3.5
Decision: Reject
