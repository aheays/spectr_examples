from spectr.env import *

## define ground state molecular constants
X = spectr.viblevel.Level(
    name       = 'X',
    species    = 'NH',
    J          = range(0, 35),
    Eref       = 0.0,
    Zsource    = 'unity',
)
X.add_manifold(
    name       = 'X³Σ⁻(v=0)',
    Tv         = 0.0,
    Bv         = 16.343275263,
    Dv         = 0.0017028445,
    Hv         = 1.238065e-07,
    Lv         = -1.4546e-11,
    Mv         = 6.9165e-16,
    γv         = -0.05485506,
    γDv        = 1.51582e-05,
    λv         = 0.91989675,
    λDv        = 3.436e-07
)
X.add_manifold(
    name       = 'X³Σ⁻(v=1)',
    Tv         = P(3125.57345571,False,0.001,0.001),
    Bv         = P(15.6964229804,False,1e-06,1e-05),
    Dv         = P(0.00167935316895,False,1e-09,1.7e-08),
    Hv         = 1.171315e-07,
    Lv         = -1.428646e-11,
    Mv         = 0.0,
    γv         = P(-0.0587802524464,False,0.001,0.00036),
    γDv        = P(1.77970702957e-05,False,1e-07,7e-07),
    λv         = P(0.739405915415,False,1e-05,0.0037),
    λDv        = 0.0
)
X.add_manifold(
    name       = 'X³Σ⁻(v=2)',
    Tv         = P(6094.87232843,False,0.001,0.0018),
    Bv         = P(15.0504650848,False,1e-06,1.8e-05),
    Dv         = P(0.00166124004059,False,1e-09,3.7e-08),
    Hv         = 1.10492e-07,
    Lv         = -1.66709e-11,
    Mv         = 0.0,
    γv         = P(-0.0500051008894,False,0.001,0.00059),
    γDv        = P(1.29842153668e-05,False,1e-07,1.6e-06),
    λv         = P(0.560266814996,False,1e-05,0.0054),
    λDv        = 0.0
)
X.add_manifold(
    name       = 'X³Σ⁻(v=3)',
    Tv         = P(8907.60291518,False,0.001,0.003),
    Bv         = P(14.4019909752,False,1e-06,3.8e-05),
    Dv         = P(0.00165084597063,False,1e-09,9.8e-08),
    Hv         = 1.02953e-07,
    Lv         = -2.1097e-11,
    Mv         = 0.0,
    γv         = P(-0.0482380992366,False,0.001,0.0014),
    γDv        = P(1.93148528815e-05,False,1e-07,4.5e-06),
    λv         = P(0.805434652443,False,1e-05,0.0067),
    λDv        = 0.0
)
X.add_manifold(
    name       = 'X³Σ⁻(v=4)',
    Tv         = P(11562.3250129,False,0.001,0.0076),
    Bv         = P(13.7464358897,False,1e-06,0.00016),
    Dv         = P(0.00164837168095,False,1e-09,6.5e-07),
    Hv         = 7.2193e-08,
    Lv         = 0.0,
    Mv         = 0.0,
    γv         = P(-0.0440101663416,False,0.001,0.0027),
    γDv        = P(-4.48896728758e-05,False,1e-07,1.3e-05),
    λv         = P(1.12437935333,False,1e-05,0.011),
    λDv        = 0.0
)

## compute vibrational-rotational transition linelist from
## electronic-vibrational transition moments. These are fit relative
## to the 1-0 transition which is fixed to unity.
XX = spectr.viblevel.Line(name='XX',level=X)
XX.add_transition_moment(name_u='X³Σ⁻(v=1)',name_l='X³Σ⁻(v=0)',μv=1)
XX.add_transition_moment(name_u='X³Σ⁻(v=2)',name_l='X³Σ⁻(v=1)',μv=P(0.932750400972,False,0.0001,0.0023))
XX.add_transition_moment(name_u='X³Σ⁻(v=3)',name_l='X³Σ⁻(v=2)',μv=P(0.91472428209,False,0.0001,0.0028))
XX.add_transition_moment(name_u='X³Σ⁻(v=4)',name_l='X³Σ⁻(v=3)',μv=P(0.727783631061,False,0.0001,0.0036))

## set all lines to have a common upper-level rotational temperature
XX.line.set_value(key='Trot_u',value=P(1660.66990921,False,1,6.8))

## modify the rotational temperature for some upper levels individually
XX.line.set_value(encoded_qn='X³Σ⁻(v=1,N=11)–X',key='Trot_u',value=P(1751.69566534,False,1,8.2))
XX.line.set_value(encoded_qn='X³Σ⁻(v=1,N=12)–X',key='Trot_u',value=P(1936.77270446,False,1,8.4))
XX.line.set_value(encoded_qn='X³Σ⁻(v=1,N=13)–X',key='Trot_u',value=P(1809.14189832,False,1,52))
XX.line.set_value(encoded_qn='X³Σ⁻(v=1,N=14)–X',key='Trot_u',value=P(2413.72620163,False,1,10))
XX.line.set_value(encoded_qn='X³Σ⁻(v=1,N=15)–X',key='Trot_u',value=P(2658.27709284,False,1,10))
XX.line.set_value(encoded_qn='X³Σ⁻(v=1,N=16)–X',key='Trot_u',value=P(2659.95077444,False,1,9.7))
XX.line.set_value(encoded_qn='X³Σ⁻(v=1,N=17)–X',key='Trot_u',value=P(2949.08929445,False,1,10))
XX.line.set_value(encoded_qn='X³Σ⁻(v=1,N=18)–X',key='Trot_u',value=P(3196.44824116,False,1,12))
XX.line.set_value(encoded_qn='X³Σ⁻(v=1,N=19)–X',key='Trot_u',value=P(3289.48573857,False,1,27))
XX.line.set_value(encoded_qn='X³Σ⁻(v=1,N=20)–X',key='Trot_u',value=P(3339.53968243,False,1,29))
XX.line.set_value(encoded_qn='X³Σ⁻(v=1,N=21)–X',key='Trot_u',value=P(3445.72721431,False,1,14))
XX.line.set_value(encoded_qn='X³Σ⁻(v=1,N=22)–X',key='Trot_u',value=P(3540.23001408,False,1,13))
XX.line.set_value(encoded_qn='X³Σ⁻(v=1,N=23)–X',key='Trot_u',value=P(3426.1567854,False,1,13))
XX.line.set_value(encoded_qn='X³Σ⁻(v=1,N=24)–X',key='Trot_u',value=P(3470.94150144,False,1,14))
XX.line.set_value(encoded_qn='X³Σ⁻(v=1,N=25)–X',key='Trot_u',value=P(3068.24908266,False,1,22))
XX.line.set_value(encoded_qn='X³Σ⁻(v=1,N=26)–X',key='Trot_u',value=P(3920.57354475,False,1,97))
XX.line.set_value(encoded_qn='X³Σ⁻(v=1,N=27)–X',key='Trot_u',value=P(3399.6463008,False,1,21))
XX.line.set_value(encoded_qn='X³Σ⁻(v=1,N=28)–X',key='Trot_u',value=P(3001.52236633,False,1,37))
XX.line.set_value(encoded_qn='X³Σ⁻(v=2,N=11)–X',key='Trot_u',value=P(2005.96913802,False,1,14))
XX.line.set_value(encoded_qn='X³Σ⁻(v=2,N=12)–X',key='Trot_u',value=P(2232.95694588,False,1,14))
XX.line.set_value(encoded_qn='X³Σ⁻(v=2,N=13)–X',key='Trot_u',value=P(2470.41412179,False,1,15))
XX.line.set_value(encoded_qn='X³Σ⁻(v=2,N=14)–X',key='Trot_u',value=P(2780.66216334,False,1,16))
XX.line.set_value(encoded_qn='X³Σ⁻(v=2,N=15)–X',key='Trot_u',value=P(3088.12560994,False,1,18))
XX.line.set_value(encoded_qn='X³Σ⁻(v=2,N=16)–X',key='Trot_u',value=P(3299.42361527,False,1,18))
XX.line.set_value(encoded_qn='X³Σ⁻(v=2,N=17)–X',key='Trot_u',value=P(3602.50258887,False,1,19))
XX.line.set_value(encoded_qn='X³Σ⁻(v=2,N=18)–X',key='Trot_u',value=P(3655.48652961,False,1,20))
XX.line.set_value(encoded_qn='X³Σ⁻(v=2,N=19)–X',key='Trot_u',value=P(3475.02546068,False,1,18))
XX.line.set_value(encoded_qn='X³Σ⁻(v=2,N=20)–X',key='Trot_u',value=P(3433.9706487,False,1,20))
XX.line.set_value(encoded_qn='X³Σ⁻(v=2,N=21)–X',key='Trot_u',value=P(3196.53942724,False,1,19))
XX.line.set_value(encoded_qn='X³Σ⁻(v=2,N=22)–X',key='Trot_u',value=P(3063.67235241,False,1,23))
XX.line.set_value(encoded_qn='X³Σ⁻(v=2,N=23)–X',key='Trot_u',value=P(3026.48555274,False,1,25))
XX.line.set_value(encoded_qn='X³Σ⁻(v=2,N=24)–X',key='Trot_u',value=P(3003.08781838,False,1,29))
XX.line.set_value(encoded_qn='X³Σ⁻(v=2,N=25)–X',key='Trot_u',value=P(2703.44008793,False,1,45))
XX.line.set_value(encoded_qn='X³Σ⁻(v=2,N=26)–X',key='Trot_u',value=P(2323.25123395,False,1,98))
XX.line.set_value(encoded_qn='X³Σ⁻(v=2,N=27)–X',key='Trot_u',value=P(2480.48929541,False,1,1e+02))
XX.line.set_value(encoded_qn='X³Σ⁻(v=2,N=28)–X',key='Trot_u',value=P(2500.74208379,False,1,1.3e+02))

## Set the rotational temperature of X(v=3) levels to a
## rotation-dependent spline
XX.line.set_spline(
    xkey       = 'N_u',
    ykey       = 'Trot_u',
    knots      = [[10, P(1482.64500861,False,1,8.8)], [20, P(2196.57292085,False,1,9.4)], [30, P(1967.10456245,False,1,72)]],
    encoded_qn = 'X³Σ⁻(v=3)–X',
    N_u        = range(10, 29),
    order      = 1
)

## adjust P/R branch strengths of each vibrational transtion to
## account for the Herman-Wallis effect.
XX.line.set_herman_wallis(
    encoded_qn = 'X³Σ⁻(v=1)–X(v=0)',
    θ          = P(-0.00667009394366,False,0.0001,5.6e-05),
    γ          = 1
)
XX.line.set_herman_wallis(
    encoded_qn = 'X³Σ⁻(v=2)–X(v=1)',
    θ          = P(-0.00400057924271,False,0.0001,6.6e-05),
    γ          = 1
)
XX.line.set_herman_wallis(
    encoded_qn = 'X³Σ⁻(v=3)–X(v=2)',
    θ          = P(-0.00718183451355,False,0.0001,0.00011),
    γ          = 1
)

## load experimental spectrum
experiment = spectrum.Experiment()
experiment.set_spectrum_from_file(
    'data/NH_25022021_1_23 (best NH).txt.h5', # filename, loaded with dataset.load
    xspline='auto',             # convert experimental data to a regular grid
    xbeg= 2400, xend = 3500,    # range of experimental data to sue
)
## lower resolution is ok
experiment.convolve_with_gaussian(0.5) 

## begin model of specturm
model = spectrum.Model('model',experiment)
model.auto_add_spline()

## neglect the spectra range affected by an atomic line
model.set_residual_weighting(0,2466,2469)

## add the computed transitions lines
model.add_line(
    line       = XX.line,
    kind       = 'emission',
    ## overall intensity scaling
    Finstr     = P(0.00110216179932,False,5e-07,4.2e-06),
    ## Unity vibraitonal populations
    αvib_u     = 1,
    ## Gaussian lineshape matching experimental lineshape
    ΓD         = 0.5,
    ΓL         = 0,
)

## optimise model etc
model.optimise()

## print input lines modified by the optimisation
model.print_input(r'.*True.*')

## plot spectrum
model.plot(fig=1)

## save all results
model.save_to_directory('output/fit_emission_band_3')
 
## plot a graph of the fitted rotational temperatures
qfig(2)
XX.line.get_upper_level().plot(
    xkeys='N',
    ykeys='Trot',
    zkeys=('label','v'),
    title='Rotation-dependent temperature of NH in a discharge through N₂ + NH₃',
)
ylim(ymin=0)

show()
