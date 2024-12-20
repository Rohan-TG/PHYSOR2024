import pandas as pd
import numpy as np
import periodictable
from matrix_functions import range_setter
### Script for inspecting missing values in data files provided

df = pd.read_csv('ENDFBVIII_MT16_XS_features.csv') # select data file

feature_names = ['Z', 'A', 'N', 'ME',
       'BEA', 'BEA_A', 'AM', 'Sn', 'S2n', 'Sp', 'S2p', 'Radius', 'Pairing',
       'Shell', 'Spin', 'Parity', 'Deform', 'Decay_Const', 'Z_even', 'A_even',
       'N_even', 'beta_deformation', 'gamma_deformation',
       'octopole_deformation', 'rms_radius', 'n_rms_radius', 'p_rms_radius',
       'n_gap_erg', 'p_gap_erg', 'n_chem_erg', 'p_chem_erg', 'Sn_compound',
       'S2n_compound', 'Sp_compound', 'S2p_compound', 'Radius_compound',
       'ME_compound', 'BEA_compound', 'BEA_A_compound', 'Sn_daughter',
       'S2n_daughter', 'Sp_daughter', 'S2p_daughter', 'Radius_daughter',
       'ME_daughter', 'BEA_daughter', 'BEA_A_daughter', 'Pairing_compound',
       'Shell_compound', 'Spin_compound', 'Parity_compound', 'Deform_compound',
       'Decay_compound', 'Pairing_daughter', 'Shell_daughter', 'Spin_daughter',
       'Parity_daughter', 'Deform_daughter', 'Decay_daughter', 'ERG', 'XS',
        'Asymmetry', 'Asymmetry_compound', 'Asymmetry_daughter']

# Note that BEA is binding energy per nucleon, BEA_A total binding energy.

# Run for full list of parameters with number of missing values

list_of_nuclides = range_setter(df, 0, 280)


target_nuclides = [[26,56], [40,90]]
# target_nuclides = list_of_nuclides

for nuclide in target_nuclides:
	tdf = df[(df['Z'] == nuclide[0]) & (df['A'] == nuclide[1])]
	for f_name in feature_names:
		if np.sum(pd.isna(tdf[f"{f_name}"])) > 1:
			print(f"{periodictable.elements[nuclide[0]]}-{nuclide[1]} missing {f_name}")

	print()
