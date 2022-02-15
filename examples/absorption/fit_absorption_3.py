""""Fit a benzene from a reference cross section"""
from spectr.env import *

## Set the benzene cross section file path and a background scan
## filename.  This o[..] stuff is a shortcut for setting values in the
## o.parameters dictionary.
o = spectrum.FitAbsorption(filename='data/2021_11_30_benzene+N2_43.9Torr_360s.0')
o['species','C6H6','filename'] = 'data/C6H6_298.0_760.0_600.0-6500.0_09.xsc'
o['background','filename'] = 'data/2021_11_30_bcgr.0'

## Fit C6H6 and CO.  Because no cross section file is specified it
## will look for or download a linelist from HITRAN like normal.
o.verbose =  True               # do not print anything while optimising
o.fit(
    species_to_fit=(
        'C6H6',
        'CO',
    ),
    region='bands',
    fit_N= True,         
    fit_pair= True,             # only affects CO, C6H6 broadening is embedded in the spectrum
    fit_intensity= True,        # scale the background scan
    fig=1,                      
)
print(o)
show()



