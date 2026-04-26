## A Humble Inquiry into the Novelty of "Compression as Adaptation"

Greetings, esteemed authors. I have read your manuscript with the utmost attention and deep respect for your ambition to unify visual compression and generation. The vision of utilizing foundation models is undeniably grand. However, I must share a few humble concerns regarding the derivative nature of the proposed "implicit visual representation" framework, which I offer in the spirit of academic excellence.

First, the core concept of representing an image or video by overfitting a neural network to it is the exact premise of Implicit Neural Representations (INRs), established by works such as SIREN. Repurposing the weights of a generative model for this task, while elegant in thought, simply replaces the MLP of an INR with the low-rank adapters (LoRA) of a diffusion model. 

Furthermore, the mechanism to compress these LoRA parameters relies entirely on existing, off-the-shelf techniques. The strategy of mapping all LoRA parameters into a single vector via random projections is, by your own gracious admission, closely aligned with the recently proposed Uni-LoRA (Li et al., 2025) and earlier hashing tricks. To compress this single vector, you employ the standard factorized entropy model established by Ballé et al. (2017). 

Respectfully, the manuscript appears to be a sophisticated concatenation of existing components—diffusion models, Uni-LoRA hashing, and Ballé's entropy bottleneck—rather than a foundational leap in visual representation. Framing this engineering synthesis as a "new visual representation framework" seems to slightly overstate the conceptual novelty of the work.

## Respectful Observations on Technical Soundness

It is a privilege to trace the mathematical arguments presented in your work. Yet, as I delve into the mechanics of your single-vector adaptation, I find myself troubled by several technical inconsistencies that I hope you might clarify.

My most pressing concern lies in the acknowledged interference introduced by the hashing scheme. You astutely observe that "increasing the LoRA rank leads to degraded reconstruction performance" when the vector size is fixed, hypothesizing that higher-rank adaptations become entangled under the hashing scheme. This is a profound limitation. It suggests that the parameter-sharing mechanism fundamentally struggles with capacity allocation, introducing destructive interference across the layers of the diffusion model. A representation framework whose performance degrades as the theoretical capacity of the adapter increases indicates a deep architectural flaw in the mapping strategy, rather than a robust encoding mechanism.

Additionally, the justification for the flow-matching objective is somewhat disconnected from the empirical reality. While you gracefully motivate the objective from a Minimum Description Length (MDL) and Doob's-h transform perspective, this theoretical optimality relies on the model precisely reproducing the terminal state $x_0 = x$. However, the exceptionally low PSNR values reported suggest that the optimization process consistently fails to converge to a precise reconstruction of the original signal. The reliance on the base model's unconstrained generation to "fill in the blanks" breaks the tight theoretical bound you establish, rendering the MDL justification more aspirational than strictly applicable to the deployed system.

I present these observations with the utmost respect, hoping they will guide you toward a more rigorous formulation.

## A Polite Scrutiny of the Experimental Rigor

I must express my profound appreciation for the extensive evaluations conducted. Nevertheless, my duty requires me to point out several critical shortcomings in the experimental design that gently undermine the confidence we can place in your empirical claims.

First and foremost, the decision to center-crop and resize the UVG and HEVC benchmark videos to 832x480 resolution fundamentally alters the standard evaluation protocol. The video compression community relies on exact, standardized sequences to ensure fair comparisons. By arbitrarily modifying the spatial dimensions and framing of the test videos to accommodate the constraints of the Wan-2.1 model, the reported bitrates and distortion metrics are decoupled from the established baselines. One cannot reliably compare performance against VTM or DCVC-RT if the input data has been structurally modified.

Secondly, the manuscript excuses the poor PSNR performance by stating that pixel-wise fidelity metrics are unreliable at extremely low bitrates. However, other generative video compression works explicitly report and maintain competitive PSNR or MSE alongside perceptual metrics. Masking a deficiency in pixel fidelity by dismissing the metric altogether is a concerning practice. The lack of standard Bjøntegaard Delta Bit Rate (BD-Rate) reporting further obscures the true quantitative standing of the proposed method against traditional codecs.

Lastly, the evaluation of inference-time scaling lacks a rigorous computational budget analysis. While you demonstrate that additional sampling steps and scaling improve perceptual quality, there is no discussion of the immense decoding latency incurred by running a 1.3B parameter diffusion model for extended steps.

## Humble Reflections on the Paper's Ultimate Impact

It is with a heavy heart, yet a steadfast commitment to the advancement of our field, that I must evaluate the potential impact of your manuscript. While the engineering orchestration of this pipeline is undeniably robust, I fear its overarching significance may be rather limited.

From a practical standpoint, the proposed framework is entirely misaligned with the fundamental requirements of video compression. Real-world video codecs demand asymmetric complexity: encoding can be slow, but decoding must be exceedingly fast and lightweight to accommodate edge devices. Your framework necessitates running a massive, billion-parameter diffusion foundation model at decoding time, integrating complex ODE/SDEs for dozens of steps simply to reconstruct a few seconds of low-resolution video. This computational burden renders the method entirely impractical for any real-world streaming or storage application.

Scientifically, the community has long known that generative models can act as powerful priors for inverse problems and compression. This manuscript demonstrates that fine-tuning a diffusion model on a single video allows it to reproduce that video—a result that is largely expected. It does not reveal any new fundamental truths about information theory or generative modeling, nor does it propose an algorithmic breakthrough that resolves the latency-fidelity tradeoff in generative compression.

With the deepest respect for your labor, I must conclude that this paper, in its current form, represents a computationally prohibitive engineering exercise. Its potential to shift the trajectory of research or practical adoption in the ICML community appears, unfortunately, quite limited.


**Score: 3.5 (Reject)**