### Novelty and Originality

It is with a heavy heart, yet utmost respect, that I must point out the remarkably derivative nature of the core mechanisms proposed in this manuscript. The authors claim novelty in two primary areas: (1) warping semantic features (DINOv2) to novel views, and (2) an "alternating scheme" of extracting features from intermediate predictions during the diffusion process. 

I must humbly remind the authors that warping features from source views to target views using geometry is an foundational concept in novel view synthesis, dating back decades and widely utilized in modern learning-based pipelines (e.g., MVSNeRF, PixelNeRF, and countless diffusion-based multi-view works). Replacing an RGB feature with a DINOv2 feature is a trivial substitution, not a fundamental algorithmic breakthrough. 

Furthermore, the "alternating scheme" of extracting features from the predicted clean data ($\hat{x}_0$) at step $t$ is exactly the mechanism underlying standard "Universal Guidance" for diffusion models (Bansal et al., 2023) and is conceptually identical to self-conditioning techniques (Chen et al., 2022). Repackaging this well-established practice of running a feature extractor on the MMSE estimate $\hat{x}_0$ as a novel "understanding and generation" scheme is a severe overstatement of the paper's contribution.
