There are 9 Mathematica Notebooks named "Combo pipeline_MxPy.nb" (x = {1,2,3}; y = {5-6, 5-7, 5-8}). Each mathematica notebook estimates the following 5 rates {k3, k4, k5, k6, k7}

This README has been written for Combo pipeline_M1P5-6_new.nb speficially. There are 8 more notebooks similarly, and the description is the same for each one.

MT + P ⇌[k₃/k₄] MP + T
MP + RQ ⇌[k₅/k₆] MPR + Q
P + RQ →[k₇] PR + Q

The following variables are used interchangably:
M1: B1
M2: B1a
M3: B1b

P5-6: P29-5
P5-7: P28-5
P5-8: P27-5

*******************************
Box 1 extracts the normalized data from reporter characterization, template recovery, and discard pathway reaction.
It also extracts the experiemntally observed starting concentrations of MP from the reporter characterization experiments. It then generates 6 different sets of starting MP concentrations with the lower limit set by the experimental ones, and the upper limit set by the set {0nM, 4nM, 6nM, 8nM, 10nM}. These 6 values are stored in the variable "iter".


*******************************
Box 2 performs the MSE anaylsis (as described in the manuscript) over the MPR time signal from the reporter characterization reaction for each of the 6 sets of starting MP concentrations.
For each set, the MSE analysis spits out {k5, k6} values which are stored. There are 6 sets of {k5, k6} stored in the variable "rates"

*******************************
Box 3 performs the following. For each set of {k5, k6}, the box performs the MSE analysis over the [MPR]+[PR] concentration signal extracted from discard pathway and template recovery experiments.
The outputs are the 6 sets of {k3, k4, k7} which are stored in the variable "RESULT". The variable "RESULT" stored another value for each of the 6 set: "error" which is the combined MSE error obtained from the DP and TR reactions.

*******************************
Box 4 and 5 select the best and second best set of parameters (based on the "error" variable from RESULT) and exports all the relevant rates {k3, k4, k5, k6, k7}; the initial MP concentration in the reporter characteriation curves;  as well as the predicted simulations for the reporter char, TR, DP reactions based on these parameter sets.All of these values are also exported in respective folders.



*******************************
Box 6 extracts the simulated and experimental data from the 4 reactions (lock opening, reporter char, TR, DP) and exports them in excel format and png formats.