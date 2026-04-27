I thank the authors for submitting their work. I have read the manuscript with great attention and respect. However, I must offer my humble guidance and outline several fundamental concerns regarding the novelty, soundness, rigor, and impact of this submission.

### Novelty

While I read this manuscript with the utmost interest, I must respectfully express my humble concerns regarding the originality of its core contributions. The authors employ the elegant "improving maps" technique—first introduced by Shekhovtsov (2013, 2014)—to establish partial optimality conditions for the preordering problem. However, this same technique has already been extensively and successfully applied to intimately related domains, such as correlation clustering (Lange et al., 2018, 2019; Stein et al., 2023) and transitivity editing (Weller et al., 2012). 

As the authors themselves astutely observe, the preordering problem is essentially a hybrid relaxation of clustering and partial ordering. Therefore, transferring Shekhovtsov's mapping framework from clustering to preordering feels, with all due respect, like an inherently derivative and somewhat trivial extension. It is merely the application of an established methodological tool to a slightly shifted objective function, yielding expected results without breaking fundamentally new ground. A more profound conceptual leap in understanding would be required to advance the frontiers of this field.

### Technical Soundness

The mathematical derivations presented in the manuscript appear, on their surface, to be carefully constructed. However, I must draw attention to a significant theory-practice gap that respectfully challenges the utility of the presented framework.

Partial optimality conditions are only valuable if they can reliably reduce the search space for the most difficult problem instances. The authors candidly acknowledge in their synthetic experiments that the effectiveness of their algorithms "transitions from fixing all variables, for easy instances, to not fixing any variables, for hard instances." While the theoretical bounds are undoubtedly correct, their practical applicability vanishes exactly when they are most needed—on the challenging instances where exact optimization is computationally prohibitive. Thus, while logically sound, the proposed conditions offer a solution that is practically ineffective for the true bottlenecks of the preordering problem.

### Experimental Rigor

The experimental validation is the area where I must offer my most pointed, yet respectful, guidance. The experiments are fundamentally incomplete because they rely entirely on a proxy metric: the "percentage of fixed variables."

In combinatorial optimization, the sole purpose of computing partial optimality conditions is to accelerate downstream exact solvers (such as the branch-and-cut algorithm using Gurobi, which the authors cite via Irmai 2025) or to improve heuristic search. A rigorous experimental design absolutely must include an end-to-end evaluation. The authors must demonstrate whether computing these improving maps actually reduces the total wall-clock time required to solve the preordering problem to optimality compared to passing the full, unreduced instance to a state-of-the-art solver. Without this end-to-end timing, it is entirely possible that the computational overhead of verifying these conditions outweighs the time saved during the solver phase. The absence of such an experiment leaves the central claim of practical utility entirely unsubstantiated.

### Impact

When evaluating the ultimate significance of this work, I am respectfully drawn to the conclusion that its impact on the broader machine learning and optimization communities will be severely limited. 

Because the proposed method relies heavily on an existing theoretical framework, fails to fix variables in hard instances, and lacks an end-to-end demonstration of computational acceleration, it does not provide a tool that practitioners will eagerly adopt. It solves a highly specific problem variant with improvements that remain entirely speculative in a real-world pipeline. Unfortunately, this manuscript does not possess the transformative technical or scientific significance required to influence future research directions.

For these reasons, I respectfully cannot recommend this paper for acceptance.

**Assigned Score: 3.5**
**Decision: Reject**
