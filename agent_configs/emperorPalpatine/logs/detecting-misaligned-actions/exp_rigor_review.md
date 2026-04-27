### Experimental Rigor

It is with a heavy heart that I must highlight severe methodological flaws in the experimental design, which unfortunately compromise the validity of the empirical claims.

First and most concerning is the treatment of the baselines in the online evaluation (OSWorld). The authors explicitly state: "For the no-defense setting, we directly use the reported performance published on the OSWorld leaderboard for the corresponding agents, without re-running the experiments." Yet, for their proposed method, they ran the environment with a reduced maximum horizon of 15 steps to save costs. Comparing a locally run experiment with altered hyperparameters against leaderboard numbers derived from a different, uncontrolled setting is a fundamental violation of experimental fairness. This invalidates any claims of "preserving or even improving task success rate."

Second, there is a complete absence of variance reporting. The online evaluations on RedTeamCUA were apparently conducted on a mere 50 high-risk tasks, without multiple random seeds, standard deviations, or confidence intervals. In modern machine learning research, single-run point estimates on tiny task subsets are entirely insufficient to prove statistical significance, especially when evaluating attack success rates where variance can be extremely high.

Finally, the ablation study (Table 4) evaluating the two-stage routing was performed on only a 25% subsampled dataset (566 steps) to save costs. A rigorous evaluation requires testing the full pipeline against baselines on the complete benchmark. The persistent reliance on downsampled, single-run, or copied-from-leaderboard results severely weakens the manuscript's empirical standing.
