### Experimental Rigor

I must raise significant concerns regarding the fairness of your empirical comparisons.

In the implementation details, it is revealed that in the default setting, the ViT encoder is initialized from a public MAE checkpoint. Yet, in Table 1, STELLAR is compared directly against MAE and TiTok. It is highly misleading to compare a model that starts from a pretrained MAE checkpoint—and is then further fine-tuned with joint-embedding clustering objectives (Sinkhorn-Knopp)—against MAE itself. Naturally, adding a DINO/SwAV-style objective on top of MAE features will yield richer semantics. This improvement comes from the additional self-supervised clustering phase, not necessarily the sparse factorization.

To make a scientifically valid claim about the superiority of STELLAR's sparse tokens over dense representations, the main benchmarking must compare models trained from scratch under identical computational budgets. Relegating the "from scratch" results to an ablation study while presenting the MAE-initialized results as the primary achievement fundamentally obscures the true source of the performance gains.
