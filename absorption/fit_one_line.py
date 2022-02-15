"""Fit species in an IR spectrum"""

## import the necessary function
from spectr.spectrum import fit_species_absorption

## automatically fit CO and/or HCN in a scan
fit_species_absorption(
    ## scan filename
    'data/2021_11_25_HCN_723Torr_mix+N2.0',
    ## species to fit
    'CO',
    'HCN',
)

