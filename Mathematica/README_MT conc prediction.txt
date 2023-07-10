This is a README file for the Mathematica notebook "MT conc prediction.nb". 
The notebook takes the derived parameters and estimates the [MT] vs time curves for the discard pathway reaction network.

The following set of ODEs are solved.
ML + T ⇌[k₁/k₂] MT + L
MT + P ⇌[k₃/k₄] MP + T
MP + RQ ⇌[k₅/k₆] MPR + Q
P + RQ →[k₇] PR + Q
MT + N ⇌[k₈/k₉] MN + T
MN + RQ ⇌[k₁₀/k₁₁] MNR + Q

For extracting MT concentration with time, k8=k9=k10=k11=0

The following variables are used interchangably:
M1: B1
M2: B1a
M3: B1b

P5-6: P29-5
P5-7: P28-5
P5-8: P27-5


*******************************
Box 1 runs an iteration across all the 9 files for different combination of monomer-proofreader combination.
Here's what it does:

Extracts the reaction rates {k1, k2, k3, k4, k5, k6, k7} from where they are stored. 
All the symbols and constants assumed are given in the notebook.
Runs the ODE as described above.
Saves the concentration of dimer for different initial [T] in the folder named "4. Discard Pathway//MT prediction"


*******************************
Box 2 runs an iteration across all the 9 files for different combination of monomer-proofreader combination.
Here's what it does:

Extracts the reaction rates {k1, k2, k3, k4, k5, k6, k7} from where they are stored. 
All the symbols and constants assumed are given in the notebook.
Runs the ODE as described above.
Saves the concentration of dimer for different initial [T] in the folder named "4. Discard Pathway//MT prediction (P=0)"