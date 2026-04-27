### Experimental Rigor

I must politely express my profound disappointment in the experimental design, which contains several critical flaws that bias the results. 

First, when comparing against baselines like ViewCrafter and Uni3C on "long trajectories", the authors state that these baselines are limited to single-window generation. To "solve" this, they uniformly subsample the long trajectories to 20 frames. This is a catastrophic violation of the baselines' intended use case! By subsampling a long video down to 20 frames, the temporal stride and baseline distance between consecutive frames become massive, pushing these models completely out of their training distribution. The standard, fair way to evaluate short-window models on long trajectories is to run them autoregressively (using sliding windows), not to artificially distort the frame rate.

Second, the baseline used in the ablation study (Table 4) is highly questionable. Because the official SEVA training code was unavailable, the authors "finetuned" SEVA using their own pipeline and augmented it with "Warped RGB" to serve as the baseline. Consequently, the improvements shown for "Warped DINO" and "Iterative DINO" are improvements over the authors' own makeshift baseline, not an established state-of-the-art model. The true gap between the proposed method and properly tuned, unmodified prior work remains opaque.
