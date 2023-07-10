This Mathematica notebook "Discard Pathway.nb" analyzes data from fluorescence reporter assays for the discard pathway experiment by extracting and processing data from the excel files.
The original data for template recovery experiments is stored in the folder "4. Discard Pathway" as excel sheets "20211214 DP plate 1.xlsx", "20211215 DP plate2.xlsx", 20211216 DP plate3.xlsx". Each of the files store experimental runs in the Cy3 and Alexa channel for a particular monomer all the 3 proofreaders P5-6, P5-7, P5-8.

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
Extract the experimental data containing signal from Alexa and Cy3 channels.
Perform data processing to obtain the normalized Alexa and Cy3 signals, and extract them as excel file formats in the folder "4. Discard Pathway//Normalized Signal".
Convert the normalized signal from the 2 channels to concentrations in each channel.
Save the normalized Alexa concentration signal in the folder as "4. Discard Pathway//Data//B1P29-5.wl".
Save the normalized Cy3 concentration signal in the folder as "4. Discard Pathway//Cy3 signal conc//B1P29-5.xlsx".
Extract [ML_total] from the Cy3 concentration signal, [RQ_total] is obtained from the saturation curves, [T_total] is assumed to be the intended initial concetration of injected template, [P_total] is 50nM, [MPR_i] is calculated from the concentration signal of Alexa channel
Save the [ML_total], [RQ_total], [P_total], [MPR_i] as "4. Discard Pathway//Conc//BL//B1P29-5.wl", "4. Discard Pathway//Conc//RQ//B1P29-5.wl", "4. Discard Pathway//Conc//P//B1P29-5.wl",  "4. Discard Pathway//Conc//BPR//B1P29-5.wl" respectively.


At the end of execution of Box1:
drawAl stores the raw experimental data in Alexa channels
drawCy stores the raw experiemntal data in Cy3 channel
dnormAl stores the normalized experimental data in Alexa channels
dnormCy stores the normalized experiemntal data in Cy3 channel
emp2 stores the conc of [MPR]+[PR] frrom the Alexa channels
emp stores the conc of [MPR]+[PR] from the Cy3 channel

*******************************

Box 2 onwards, the user can run the 6 different boxes to generate Figures S23, S24, S25, S26 (7 figures in total). The figures are exported in the folder "SI" and are named
-"DP_Cy3_raw.pdf"
-"DP_Alexa_raw.pdf"
-"DP_Cy3_norm.pdf"
"DP_Cy3_long_time.pdf"
-"DP_Alexa_norm.pdf"
-"DP_Cy3_conc.pdf"
-"DP_Alexa_conc.pdf"
