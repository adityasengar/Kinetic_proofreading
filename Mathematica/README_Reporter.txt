This Mathematica notebook "Reporter.nb" analyzes data from fluorescence reporter assays for the reporter characterization experiment by extracting and processing data from the excel files.
The original data for reporter characterization is stored in the folder "2. Reporters" as excel sheets "B1P29-5.xlsx", "B1aP28-5.xlsx" etc.

The following variables are used interchangably:
M1: B1
M2: B1a
M3: B1b

P5-6: P29-5
P5-7: P28-5
P5-8: P27-5

The README assumes the parent directory is the folder named "Data Analysis"

*******************************

Box 1 runs an iteration across all the 9 files for different combination of monomer-proofreader combination.
Here's what it does:
Extract the experimental data containing signal from Alexa and Cy3 channels.
Perform data processing to obtain the normalized Alexa and Cy3 signals, and extract them as excel file formats in the folder "3. Template recovery//Normalized Signal".
Save the normalized Alexa concentration signal in the folder as "2. Reporters//Data//B1P29-5.wl".
Save the normalized Cy3 concentration signal in the folder as "2. Reporters//Cy3 signal conc//B1P29-5.xlsx".
Extract [MP_total] from the Cy3 concentration signal and [RQ_total] from the t=0 values of the Normalized Alexa signal.
Save the [MP_total] and [RQ_total] as "2. Reporters//Conc//B1P29-5-BPi.wl" and "2. Reporters//Conc//B1P29-5-RQi.wl" respectively.


*******************************

Box 2 onwards, the user can run the 6 different boxes to generate Figures S17, S18 and S19 (6 figures in total). The figures are exported in the folder "SI" and are named
-"Reporter_Cy3_raw.pdf"
-"Reporter_Alexa_raw.pdf"
-"Reporter_Cy3_norm.pdf"
-"Reporter_Alexa_norm.pdf"
-"Reporter_Cy3_conc.pdf"
-"Reporter_Alexa_conc.pdf"
