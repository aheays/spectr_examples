"""Fit the CO fundamental band in detail."""

## Import the entire spectr environment.
from spectr.env import *

## Begin a model and load experimental data from its
## filename. Restrict the frequency range to the CO fundamental
model = spectrum.Model(
    experiment='data/2021_11_30_benzene_10.9Torr_120s.0',
    xbeg=2050,xend=2200,
)

## Interpolate the model to a find frequency grid in order to
## accurately model narrow line shapes. The default model grid matches
## the experiment.
model.interpolate(0.01)

## Automatically fit the background to a spline with knots separated
## by 10cm-1.
model.auto_add_spline(xi=10,vary= True)

## Add CO absorption using a HITRAN linelist.
model.add_hitran_line(
    'CO',
    ## column density of CO in natural isotope abundance (cm-2)
    Nchemical_species=P(1e17, True,1e12),
    ## air-broadening pressure (Pa)
    pair=P(10000, True,1,bounds=(1e2,1e5)),
    ## temperature (K) controlling excitation and Doppler broadening
    Teq=297,
)

## This statement convolves the model spectrum with an instrument
## lineshape read from the OPUS data file.  There is some ambiguity
## about the actual resolution, so this might need to be optimised.
model.auto_convolve_with_instrument_function(vary= True)

## Optimise all adjustable parameters set to "True" until they
## best-fit the experimental spectrum.
model.optimise()

## Plot the modelled and experimental spectra.
model.plot(fig=1)

## save results
model.save_to_directory('output/fit_manually_1')

## show figures
show()
