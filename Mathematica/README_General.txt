This README file contains information for analyzing data and predicting rates related to the kinetic proofreading manuscript.

Prerequisites
In order to run this notebook, you will need to have Mathematica installed on your computer. The code was developed and tested using Mathematica version 12.3.

Getting started
To use this notebook, open it in Mathematica and run the code cells in order. Before running the code, make sure to set the appropriate values for any parameters or variables that need to be specified (these will be indicated in the code comments).

****************************************************************************
Lock_opening_M1.nb
Lock_opening_M2.nb
Lock_opening_M3.nb

The 3 files do the following:
- Read the raw fluorescence data from the Cy3 channel for lock opening of M1, M2, M3
- Normalize the raw data
- Convert the information into [MT] vs time format for different starting [T] concentrations
- Extract concentration of [ML_total]
- Export the [MT] vs time information in the folders "1. Lock opening and binding//Data", and [ML_total] in "1. Lock opening and binding//Conc".
- Use the [MT] vs time curves to perform an MSE analysis and extract k1, k2. Store the rates in the folder "1. Lock opening and binding//Rates"
- Make a prediction of [MT] vs time and export the predicted concentration in excel format in the folder "1. Lock opening and binding//Data"

****************************************************************************
Reporter.nb

The file does the following:
- Read the raw fluorescence data from the Cy3 and Alexa channel for reporting of M1, M2, M3 by P5-6, P5-7, P5-8
- Normalize the raw data and convert it into [MPR] vs time format and save it in the folder "2. Reporters//Data"
- Extract [RQ_total] and the starting variable concentration of [MP], [MP_total] from the normalized data and export it in folder "2. Reporters//Conc".

****************************************************************************
Template recovery.nb

Thie file does the following:
- Read the raw fluorescence data from the Cy3 and Alexa channel for template recovery of template bound monomer M1, M2, M3 by proofreader P5-6, P5-7, P5-8
- Normalize the raw data from the Alexa and Cy2 channel.
- Extract the concentrtion signal generated from Alexa channel ([MPR]+[PR]) and save it in the folder "3. Template Recovery//Data"
- Extract the concentration signal generated from Cy3 channel inside the folder "3. Template recovery//Cy3 signal conc"
- Extract [MT_total] from the Cy3 signal and store it in the folder "3. Template recovery//Conc".


****************************************************************************
Discard pathway.nb

Thie file does the following:
- Read the raw fluorescence data from the Cy3 and Alexa channel for the complete discard pathway reaction of locked monomer M1, M2, M3 in presence of proofreaders P5-6, P5-7, P5-8
- Normalize the raw data from the Alexa and Cy2 channel.
- Extract the concentrtion signal generated from Alexa channel ([MPR]+[PR]) and save it in the folder "4. Discard pathway//Data"
- Extract the concentration signal generated from Cy3 channel inside the folder "4. Discard pathway//Cy3 signal conc"
- Extract [MT_total] (variable concentration) from the Cy3 channel and store it in the folder "3. Template recovery//Conc".
- Extract the initially formed [MPR] at t=0, [MPR]_i, from the Alexa signal and subtract it from [P_total], [RQ_total], [ML_total]. Export [MPR]_i and modified [P_total], [RQ_total], [ML_total] in the folder "4. Discard pathway//Conc".


****************************************************************************
Combo pipeline_M1P5-6.nb
Combo pipeline_M1P5-7.nb
Combo pipeline_M1P5-8.nb
Combo pipeline_M2P5-6.nb
Combo pipeline_M2P5-7.nb
Combo pipeline_M2P5-8.nb
Combo pipeline_M3P5-6.nb
Combo pipeline_M3P5-7.nb
Combo pipeline_M3P5-8.nb


Each file does the following:
- Import all the relevant data required to make predictions for k3, k4, k5, k6, k7.
- Import the [MP_total] from the reporter data and construct a set of 8 initial [MP_total] array based on the techqniue mentioned in Methods section of the manuscript.
- Using the MSE analysis, make 8 different predictions for {k5, k6} for each starting [MP_total] array.
- For each starting [MP_total], select the predicted {k5, k6} and use this information to run another MSE analysis using the concentration signal generated from the Alexa channel in Template recovery and Discard pathway reactions. - The final set {k3, k4, k7} is the one that minimzes the error in our MSE analysis.
- Export the final reaction rate constants {k3, k4, k5, k6, k7}. Export {k3, k4, k7} in the folder "BT+P rates" and {k5, k6} in the folder "BP+RQ rates".
- Export the predicted [MPR]+[PR] concentration for template recovery and discard pathway in "3. Template recovery\\Sim" and "4. Discard pathway\\Sim" respectively.
- Export the excel format and images of experimental vs predictions for lock opening, reporter reaction, template recovery, discard pathway in the folder "Fittings" and "Fittings\\Pics" respectively.