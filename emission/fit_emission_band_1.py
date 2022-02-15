"""Fit emission bands in appearing in a spectrum."""
from spectr.env import *

## VibLevel objects is a model of one or more electronic vibrational
## levels of a linear molecule
vlevel = viblevel.VibLevel(
    name='vlevel',              # arbitrary, matches code symbol
    species='¹⁴N₂',             # diatomic molecule including isotopic information, e.g., ¹⁴N₂ or 14N2
    Eref=0,                   # reference energy level relative to electronic energy minimum
    J=range(0,31),
)
## add an electronic-vibrational manifolds representing the W³Δu(v=2)
## state
vlevel.add_manifold(
    ## a name, also decoded for quantum numbers
    name       = 'W(v=2)',
    ## quantum numbers
    label      = 'W',
    v          = 2,
    Λ          = 2,
    s          = 0,
    gu         = -1,
    ## molecular constants according to the Hamiltonian of pgopher or
    ## Brown (1979) [JOURNAL OF MOLECULAR SPECTROSCOPY 74,294-318]
    Tv         = 12557.807195,
    Bv         = 1.42768053,
    Dv         = 5.64249e-06,
    Hv         = -4.12869e-13,
    Av         = 5.72125,
    ADv        = 5.53435e-06,
    λv         = 0.675067,
    λDv        = 1.47446e-06,
    γv         = -0.00290735,
)
## add an electronic-vibrational manifolds representing the B³Πg(v=2)
## state
vlevel.add_manifold(
    name       = 'B(v=0)',
    label      = 'B',
    v          = 0,
    Λ          = 1,
    s          = 0,
    Tv         = 9550.007878,
    Bv         = 1.62876998,
    Dv         = 5.86261e-06,
    Av         = 42.2387,
    ADv        = -0.000421635,
    λv         = -0.202348,
    λDv        = -6.166e-07,
    γv         = -0.0036496,
    ov         = 1.15255,
    pv         = 0.00433925,
    qv         = 8.55895e-05,
    gu         = 1
)

## VibLine object combining two VibLevel (or the same one twice) to
## compute the transitions between them
vline = viblevel.VibLine(vlevel)
## add a transition moment between two named electronic-vibrational levels
vline.add_transition_moment(
    'W(v=2)',                   # taken from "upper" VibLevel
    'B(v=0)',                   # taken from "lower" VibLevel
    μv=1                        # electric-dipole
                                # electronic-vibrational transition
                                # moment (au)
)

## load an experimental spectrum from a data file
experiment = spectrum.Experiment()
x,y = tools.file_to_array_unpack('data/N_9713_3_03.txt.h5')
experiment.set_spectrum(x,y,xspline='auto', xbeg=2900,xend=3010)
## lower resolution for convenience
experiment.convolve_with_gaussian(0.2)

## model this experiment
model = spectrum.Model('model',experiment)

## fit background automatically
model.add_spline(knots=[[2900.0051, P(1785612.85396,False,16,3.6e+04)], [2904.055214149335, P(1517264.35757,False,13,1.6e+04)], [2916.5580665325606, P(1091390.48914,False,12,1.6e+04)], [2922.7382407159903, P(1289435.22211,False,14,1.4e+04)], [2936.2311210023863, P(1310055.61836,False,15,1.4e+04)], [2947.286432587794, P(1056580.86336,False,13,1.3e+04)], [2963.5768917217865, P(1601379.32637,False,21,1.3e+04)], [2977.062271796795, P(1209937.41923,False,19,1.4e+04)], [2980.789876856461, P(1380884.98961,False,18,1.3e+04)], [3000.507932594613, P(1602291.96507,False,26,1.5e+04)], [3005.1355630207977, P(1016261.82693,False,24,1.9e+04)], [3009.9957, P(1364510.12296,False,17,4.3e+04)]])

## add absorption based on the VibLine model band
model.add_line(
    use_cache = False,
    ## The output linelist of a VibLine object. It is a Dataset.
    line=vline.line,
    ## add emission lines
    kind='emission',
    ## For simulate pure Gaussian lines of 0.2 cm-1.FWHM. This is done
    ## by specirying the Lorentzian FWHM to be 0
    ΓG=0.2,                     
    ΓL=0,
    ## don't bother messinag around with partition functions in this
    ## non-absolute measurement
    Zsource='unity',
    ## The instrumental efficiency. 
    Finstr     = P(0.000134010176302,False,1e-09,1.3e-06),
    ## Here are several ways of controlling describing the excitation:
    ##
    ## An equilibrium temperature. This will probably fail because the
    ## rotational and vibrational excitation of lines in the spectra
    ## are unlikely to be in equilbrium.
    # Teq = P(2000,False,1)
    ## Separate vibrational and rotational temperatures. This might
    ## work if the vibrational excitation is not the result of a
    ## cascade if emission.
    # Tvib=P(2000,False,1),
    # Trot=P(300,False,1),
    ## A vibrational population fixed to one for all v-levels, and a
    ## rotational temperature.  If the vibrational band strengths, μv,
    ## above are fitted to the spectrum this will fit any vibrational
    ## distribution, but the vibrational excitation is now degenerate
    ## with the band strength.  Still assumes thermal rotational
    ## excitation, which might well be the case.  
    αvib_u=1,
    Trot       = P(379.848362085+200,False,1,3.7),
)

## optimise and "True" parameters
model.optimise()

## show updated parameters
model.print_input('.*True.*')
model.save_input('t0.py')

## plot results
model.plot(fig=1)
show()
