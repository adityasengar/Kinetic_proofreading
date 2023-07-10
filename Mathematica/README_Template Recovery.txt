This Mathematica notebook "Template Recovery.nb" analyzes data from fluorescence reporter assays for the template recovery experiment by extracting and processing data from the excel files.
The original data for template recovery experiments is stored in the folder "3. Template Recovery" as excel sheets "20211222 TR plate1.xlsx", "20220119 TR plate2.xlsx", 20220124 TR plate3.xlsx". Each of the files store experimental runs in the Cy3 and Alexa channel for a particular monomer all the 3 monomers M1, M2, M3.

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
Perform data processing to obtain the normalized Alexa and Cy3 signals, and extract them as excel file formats in the folder "3. Template Recovery//Normalized Signal".
Convert the normalized signal from the 2 channels to concentrations in each channel.
Save the normalized Alexa concentration signal in the folder as "3. Template recovery//Data//B1P29-5.wl".
Save the normalized Cy3 concentration signal in the folder as "3. Template Recovery//Cy3 signal conc//B1P29-5.xlsx".
Extract [MT_total] from the Cy3 concentration signal, [RQ_total] is obtained from the saturation curves.
Save the [MT_total], [RQ_total], [P_total] (assumed at 50nM) as "3. Template Recovery//Conc//BT//B1P29-5.wl", "3. Template Recovery//Conc//RQ//B1P29-5.wl", "3. Template Recovery//Conc//P//B1P29-5.wl" respectively.


At the end of execution of Box1:
dnew stores the raw experimental data in Alexa channels
dnewtem stores the raw experiemntal data in Cy3 channel
datanormA stores the normalized experimental data in Alexa channels
datanormC stores the normalized experiemntal data in Cy3 channel
emp2 stores the conc of [MPR]+[PR] frrom the Alexa channels
emp stores the conc of [MPR]+[PR] from the Cy3 channel

*******************************

Box 2 onwards, the user can run the 6 different boxes to generate Figures S20, S21, S22 (6 figures in total). The figures are exported in the folder "SI" and are named
-"TR_Cy3_raw.pdf"
-"TR_Alexa_raw.pdf"
-"TR_Cy3_norm.pdf"
-"TR_Alexa_norm.pdf"
-"TR_Cy3_conc.pdf"
-"TR_Alexa_conc.pdf"
