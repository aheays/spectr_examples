""""Automatically fit multiple species"""

## import spectr environment
from spectr.env import *

## make FitAbsorption object for this spectrum
o = spectrum.FitAbsorption(
    ## the experimental scan filename
    filename='data/2021_11_25_HCN_723Torr_mix+N2.0',
    ## set parameters to trade accuracy for speed
    min_S296K=1e-21,
    nfwhmL=1000,
)

## fit all species at the same time, which accounts for overlapping
## spectra
o.fit(
    species_to_fit=(
        'CO',
        'H2O',
        'CO2',
        'HCN',
    ),
    ## could be 'bands', 'lines', (1000,1200), or,
    ## ((1000,1200),(2000,2100),...)
    region='lines',
    ## Various options about what to optimise. Other options for
    ## fitting are given by the arguments of
    ## spectrum.FigAbsorption.make_model
    fit_N= True,           # whether to optimise column density
    fit_pair= True,        # whether to optimise "air" pressure
    fit_intensity= True,   # whether to optimise the spline background
    fit_FTS_H2O= True,     # whether to add and optimise more H2O
                           # absorption due to contamination in
                           # the spectrometer
    fit_instrument= True,  # whether to optimise the
                           # instrumental line shape
    fit_shift= True,       # whether to optimise a zero-level shift
    ## make a plot
    fig=1,                      
    plot_legend=True
)

## model the entire spectrum while fitting a global background. This
## uses the optimised column densities found above.
o.fit(
    fit_intensity=True, 
    intensity_spline_step=50,
)
fig = o.plot(fig=2)

## save all results
o.save('output/fit_absorption_1')
fig.savefig('output/fit_absorption_1/full_spectrum.pdf')

show()



