"""Fit (nearly) all absorption in an IR spectrum."""

from spectr.env import *
model = spectrum.Model('model',experiment='data/2021_11_30_benzene+N2_43.9Torr_360s.0',)
model.interpolate(0.01)

## add a measured background intensity to the model with some slight
## rescaling
model.add_from_file('data/2021_11_30_bcgr.0',yscale=P(1.00627055101,False,1e-05,5e-05))

## Add benzene absorption according to an experimental cross section
## downloaded from HITRAN (https://hitran.org/xsc)
hitran_cross_section = hitran.load_cross_section('data/C6H6_298.0_760.0_600.0-6500.0_09.xsc')
model.add_spectrum(
    hitran_cross_section,
    kind='absorption',
    N = P(7.37415613567e+18*2, True,1e+15,7.7e+15),
)

## add absorption by various other species computed from HITRAN
## linelists.  Some parameters are common to all species
common = {
    'Teq':P(308.579132109,False,1,0.53),
    'min_S296K': 1e-21,
    'nfwhmL': 1000,
} 

model.add_hitran_line(
    'CO2',
    Nchemical_species = P(7.4641157658e+15,False,1e+12,5.9e+13),
    pair       = P(7545.31407688,False,1,3.9e+02,(100,50000)),
    **common
)

### model.add_hitran_line(
###     '¹²C¹⁶O₂',
###     # chemical_species='CO2',
###     Nchemical_species = P(7.4641157658e+15,False,1e+12,5.9e+13),
###     pair       = P(7545.31407688,False,1,3.9e+02,(100,50000)),
###     **common
### )

model.add_hitran_line(
    'CO',
    Nchemical_species = P(3.18641247407e+17,False,1e+12,3.8e+15),
    pair       = P(6852.11132824,False,1,1.2e+02,(100,50000)),
    **common
)

model.add_hitran_line(
    'H2O',
    Nchemical_species = P(2.59437473801e+16,False,1e+14,5.4e+14,(1e+12,1e+20)),
    pair       = P(11541.6298265,False,1,8.8e+02,(100,50000)),
    **common
)

model.add_hitran_line(
    'C2H2',
    Nchemical_species = P(1.09100175887e+18*0.7,False,1e+12,6.2e+15),
    pair       = P(9687.04918388,False,1,1.2e+02,(100,50000)),
    **common
)

model.add_hitran_line(
    'C4H2',
    Nchemical_species = P(4.71022479134e+17,False,1e+12,6.1e+15),
    pair       = P(36260.4587264,False,1,1.2e+03,(100,50000)),
    **common
)

model.add_hitran_line(
    'HCN',
    Nchemical_species = P(5.36423331066e+17/2*1,False,1e+12,2.9e+16),
    pair       = P(5000,False,1,1.7e+03,(100,50000)),
    **common
)

## I failed to identify a band betwee 3300 and 3360 so I remove this
## part of the spectrum from the fit
model.set_residual_weighting(0,xbeg=3300,xend=3360)

# convolve with a manually optimised function
model.convolve_with_instrument_function(
    sinc_fwhm=P(0.0666364979841,False,1e-05,1e-05,(0,inf)))

model.optimise()

## print the optimised valies of varied parameter
model.print_input(match_lines_regexp='.*False.*')

model.save_to_directory('output/fit_manually_2')
model.plot(fig=1)
# show()

