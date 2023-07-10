This is a README file to run the files "Lock_opening_M1.nb", "Lock_opening_M2.nb", and "Lock_opening_M3.nb" respectively.

The main difference in parameter is "type" variable which takes value 0 for M1, 1 for M2, 2 for M3.

The following variables are interchangable:
M1: B1
M2: B1a
M3: B1b

*******************************

The first box in each file performs the following tasks:

Extracts the raw experimental data and stores it in the variable "dnew".
Processes the data and stores the concentration of [MT] with time in the variable "dnewfl".
Extracts the total initial concentration of locked monomer [ML_total] and stores it in the variable "concBL".
Exports the initial concentration of [ML_total] as "1. Lock opening and binding//Conc//B1Linitial.wl".
Exports the concentration data of [MT] vs time extracted from experimental data and stores the raw experimental data as "1. Lock opening and binding//Data//B1lockopen_Raw.wl" and the processed concentration data as "1. Lock opening and binding//Data//B1lockopen.wl".

********************************

The second box defines the system of ODEs that can produce [MT] vs time for any given forward and backward rates (k1, k2).

********************************

The third box in each file performs the following tasks:

Extracts the reaction rate constants using the mean squared error (MSE) analysis described in the manuscript.
Defines the start and end limit of k1 and k2 while also defining the variable "T_interest".
Calculates the MSE for all times less than "T_interest" with a weight of 1.0 and a weight of 0.2 for all times greater than "T_interest".
Outputs the predicted values of k1 and k2.

*******************************

The forth box just produces a figure of the experiemntal data and the simulation prediction using the parameters obtained in the previous box.

*******************************

The fifth box exports the predicted curves for concentration of [MT] vs time as "1. Lock opening and binding//Data//Sim_B1.wl" and also exports the raw Cy3 signal in excel format as "Excel data//Lock opening//Cy3//B1lockopen_Raw.xlsx".

*******************************

The sixth box is unique to "Lock_opening_M3.nb". It generates Figures S15 and S16 in Supplementary material and outputs them as "SI//Lock opening M1 (Raw data).pdf" and "SI//Lock opening M1 (Processed).pdf", respectively.
