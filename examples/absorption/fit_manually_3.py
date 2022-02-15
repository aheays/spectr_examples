"""Fit the CO fundamental band while modelling additional instrumental
effects.""" 

## import the spectr environment
from spectr.env import *

## load data into Experiment object, restricted to the wavelength
## region of the strongest HCN band, and plot
experiment = spectrum.Experiment(
    filename='data/blank 4.6 torr SO2,CO,CH4,N2,H2O,CO2.0',
    xbeg=2090, xend=2198,
)
experiment.scalex(scale=P(0.999999471308,False,1e-08,6.2e-09))

## begin a Model object
model = spectrum.Model('model',experiment=experiment)
model.interpolate(0.001)
model.add_spline(knots=[[2090.0077536581593, P(0.665697815435,False,6.4e-06,0.00028)], [2094.602932251791, P(0.664671437988,False,6.4e-06,0.00023)], [2101.6538948151338, P(0.662708297655,False,6.3e-06,0.00023)], [2111.311302941421, P(0.658621946475,False,6.3e-06,0.00023)], [2124.479126190057, P(0.652876717025,False,6.2e-06,0.00023)], [2141.4436215881847, P(0.646746225316,False,6.2e-06,0.00023)], [2146.9126374225725, P(0.644638030429,False,6.2e-06,0.00023)], [2158.7697048100736, P(0.639464351481,False,6.1e-06,0.00023)], [2175.1767523132366, P(0.633827167851,False,6.1e-06,0.00023)], [2184.1561832699717, P(0.630557448318,False,6e-06,0.00023)], [2195.9831183388264, P(0.62543111012,False,6e-06,0.00023)], [2199.990716718846, P(0.623350153711,False,6e-06,0.00037)]])

model.add_hitran_line(
    'CO',
    Nchemical_species = P(6.84911048153e+19,False,1e+12,3.2e+17),
    pair       = P(640.130343903,False,1,3.2,(1e+02,1e+05)),
    Teq        = P(273.896984978,False,1,0.19),
    ## how many Lorentzian full-width half-maximums to include when
    ## computing lineshapes. Defaults to infinity and making this
    ## smaller makes the computation faster.
    nfwhmL=10000,
)

## model.auto_convolve_with_instrument_function(vary=False)
model.convolve_with_instrument_function(
    blackman_harris_order = 3,
    blackman_harris_resolution = P(0.0386177915717,False,3e-07,4e-05,(0,inf))
)

## This scales the intensity by a sinusoid function.  This must be done after absorption has been added to the model.  To use the auto
## recorded in some experiments
# model.auto_scale_piecewise_sinusoid(xi=50,vary=True)
model.scale_piecewise_sinusoid(regions=[[2090.00776072448, 2143.9973428423573, P(0.029071492581,False,1.3e-07,5e-05), P(1.55867095328,False,1.6e-05,2.7e-05), P(3.36991734689,False,6.3e-05,0.0043)], [2143.9973428423573, 2197.9869249602343, P(0.0275092564449,False,1.2e-07,5.2e-05), P(1.55828695157,False,1.6e-05,1.4e-05), P(4.27586479915,False,6.3e-05,0.0031)]])

model.add_constant(constant=P(0.00741859492128,False,1e-05,0.00022))

## Optimise all adjustable parameters set to "True" to best-fit the
## experimental spectrum.
model.optimise()
model.print_input('.*True.*')
model.save_to_directory('output/fit_manually_3')

## Plot the modelled and experimental spectra and label all lines with
## absorption line strengths above a threshold
model.plot(
    fig=1,
    plot_labels= True,
    label_match={'min_S296K':1e-19,},
)
show()
