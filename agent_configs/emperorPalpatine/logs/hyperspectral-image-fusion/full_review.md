### Novelty

While the manuscript presents the framework with an air of grand innovation, a closer inspection reveals that the contributions are somewhat derivative. The spatial agnosticism is entirely built upon existing Implicit Neural Representation (INR) techniques, specifically mirroring the approach of LIIF (Learning Continuous Image Representation with Local Implicit Image Function, Chen et al., 2021). The authors themselves humbly acknowledge following the practice of LIIF, yet they package this as a core component of their "universal framework." Furthermore, the application of INR to hyperspectral image (HSI) fusion is not new, as evidenced by prior works like OTIAS and AFO that the authors cite. Thus, the spatial flexibility offers no conceptual leap.

More disappointingly, the so-called "Matryoshka Kernel" (MK) is presented as a novel architectural principle inspired by Matryoshka Representation Learning (MRL, Kusupati et al., 2022). However, MRL involves a deep, structured representation learning paradigm where multiple prefixes of a representation are explicitly trained to be informative. In contrast, the MK simply performs a literal, basic array slice operation on the input channel dimension of a convolutional filter (`[:, :C_in, :, :]`). Renaming a trivial channel truncation operation to "Matryoshka Kernel" does not magically transform it into a profound architectural innovation. I am respectfully disappointed to see such a basic programming operation masquerading as a fundamental contribution.
### Technical Soundness

With the utmost respect for the authors' efforts, the core mechanism intended to achieve "spectral-band agnosticism" is fundamentally flawed and physically unsound. 

The Matryoshka Kernel operates by simply selecting the first $C_{in}$ slices of the kernel weight tensor. However, the $n$-th channel in one dataset does not correspond to the same physical wavelength in another. As detailed in your dataset table, CAVE (31 bands) spans 400–700nm, PaviaC (102 bands) spans 430–860nm, and Washington DC (191 bands) spans 400–2500nm. Consequently, the shared weights in the early slices of the kernel are forced to process entirely different physical signals depending on which dataset is sampled in a given mini-batch. For instance, the first slice of the kernel processes 400nm light for CAVE but 430nm light for PaviaC. This guarantees that the network is not learning a universal, physically meaningful spectral representation, but rather suffering from catastrophic interference or simply using massive capacity to memorize disjoint mappings.

Furthermore, unlike true MRL where representations are explicitly optimized so that all nested prefixes are valid simultaneously, your loss formulation only updates the first $C_{in}$ slices for whatever dataset is currently sampled. There is no theoretical or empirical mechanism to enforce a cohesive nested structure across these disjoint physical bands. The method is technically broken at its foundation.
### Experimental Rigor

I must politely raise grave concerns regarding the fairness of the experimental validation. 

The manuscript states: "For each dataset... we trained a dedicated model independently for all SOTA methods... For our method, we trained only a single, unified model, with the training set composed of a mixture of training samples from the seven datasets." This is a deeply unfair comparison. The proposed method benefits from a massively larger, mixed training corpus (spanning seven diverse datasets), whereas the baselines are severely handicapped by being trained exclusively on individual, small-scale datasets. The observed performance gains could entirely stem from the massive increase in training data diversity rather than the proposed architectural changes. To make a scientifically valid claim, the baselines must be afforded the exact same mixed training data—perhaps by simply zero-padding all datasets to the maximum channel dimension (194 bands) and training a standard CNN.

Additionally, the paper lacks a crucial ablation study isolating the effect of the MK. Without comparing MK against the trivial baseline of zero-padding or channel-interpolation, it is impossible to verify if the "nested" slicing offers any actual empirical benefit over naive data formatting.
### Impact

While the ambition to construct a universal hyperspectral foundation model is commendable, the current approach's disregard for the physical realities of spectroradiometry severely limits its potential impact. Practitioners working with hyperspectral data rely on the precise physical meaning of narrow spectral bands. A model that scrambles wavelength alignments and treats spectral channels merely as numerical indices to be truncated will not be adopted by the remote sensing or medical imaging communities. Until the method evolves to align channels by their true physical wavelengths, its utility remains strictly confined to a mathematical curiosity with very limited real-world scientific significance.


**Score:** 3.5
**Decision:** Reject
