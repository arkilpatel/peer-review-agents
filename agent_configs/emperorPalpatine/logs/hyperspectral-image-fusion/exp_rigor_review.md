### Experimental Rigor

I must politely raise grave concerns regarding the fairness of the experimental validation. 

The manuscript states: "For each dataset... we trained a dedicated model independently for all SOTA methods... For our method, we trained only a single, unified model, with the training set composed of a mixture of training samples from the seven datasets." This is a deeply unfair comparison. The proposed method benefits from a massively larger, mixed training corpus (spanning seven diverse datasets), whereas the baselines are severely handicapped by being trained exclusively on individual, small-scale datasets. The observed performance gains could entirely stem from the massive increase in training data diversity rather than the proposed architectural changes. To make a scientifically valid claim, the baselines must be afforded the exact same mixed training data—perhaps by simply zero-padding all datasets to the maximum channel dimension (194 bands) and training a standard CNN.

Additionally, the paper lacks a crucial ablation study isolating the effect of the MK. Without comparing MK against the trivial baseline of zero-padding or channel-interpolation, it is impossible to verify if the "nested" slicing offers any actual empirical benefit over naive data formatting.
