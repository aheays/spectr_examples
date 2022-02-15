## import the spectr environment
from spectr.env import *

## initialise VibLevel object that computes diatomic levels from molecular
## constants
vlevel = viblevel.Level(
    name='vlevel',                 # convenient label (valid python symbol)
    species='NH',             # ascii or unicode species name
    Eref=0.0,                 # reference energy relative to ground
                              # state equilibrium energy neglecting
                              # spin effects
    Zsource='self',           # source of partition function for
                              # computing line intensities, can be
                              # 'self', 'database', 'HITRAN', 'unity'
)


## Add electronic-vibrational levels from effective Hamiltonian
## parameters in agreement with the definition of pgopher. Parameters
## can be optimised.
vlevel.add_manifold(
    name       = 'X.3Σ-(v=0)',  # names can also be encoded with unicode subscripts/superscripts, e.g.,: X³Σ⁻(v=0)
    Tv         = 0.0,
    Bv         = 16.343275263,
    Dv         = 0.0017028445,
    Hv         = 1.238065e-07,
    Lv         = -1.4546e-11,
    Mv         = 6.9165e-16,
    γv         = -0.05485506,
    γDv        = 1.51582e-05,
    λv         = 0.91989675,
    λDv        = 3.436e-07,
)
vlevel.add_manifold(
    name       = 'X.3Σ-(v=1)',
    Tv         = P(3125.572486,False,1e-05,0.00032),
    Bv         = P(15.696418284,False,1e-07,2.2e-06),
    Dv         = P(0.00167936108,False,1e-09,3.5e-09),
    Hv         = 1.171315e-07,
    Lv         = -1.428646e-11,
    Mv         = 0.0,
    γv         = P(-0.05197386,False,1e-06,2.5e-05),
    γDv        = P(1.47892e-05,False,1e-09,6.1e-08),
    λv         = P(0.91947092,False,1e-06,0.00033),
    λDv        = 0.0,
)
vlevel.add_manifold(
    name       = 'X.3Σ-(v=2)',
    Tv         = P(6094.874867,False,1e-5),
    Bv         = P(15.050471062,False,1e-7),
    Dv         = P(0.0016612632,False,1e-9),
    Hv         = 1.10492e-07,
    Lv         = -1.66709e-11,
    Mv         = 0.0,
    γv         = P(-0.04908779,False,1e-6),
    γDv        = P(1.38427e-05,False,1e-9),
    λv         = P(0.91790688,False,1e-6),
    λDv        = 0.0,
)
vlevel.add_manifold(
    name       = 'X.3Σ-(v=3)',
    Tv         = P(8907.59525,False,1e-5),
    Bv         = P(14.40201424,False,1e-7),
    Dv         = P(0.0016506064,False,1e-9),
    Hv         = 1.02953e-07,
    Lv         = -2.1097e-11,
    Mv         = 0.0,
    γv         = P(-0.0461922,False,1e-6),
    γDv        = P(1.3319e-05,False,1e-9),
    λv         = P(0.915473,False,1e-6),
    λDv        = 0.0,
)

## make a VibLine object that combines level data and transition
## moments into a line spectrum. 
line = viblevel.Line(
    'line',                       # a convenient name
    vlevel,                          # Level object
)
## Add electric-dipole transition moments (atomic units) between two
## ascii or unicode encoded electronic-vibrational levels
line.add_transition_moment('X.3Σ-(v=1)','X.3Σ-(v=0)',μv=1)
line.add_transition_moment('X.3Σ-(v=2)','X.3Σ-(v=0)',μv=1)
line.add_transition_moment('X.3Σ-(v=3)','X.3Σ-(v=0)',μv=1)

## construct the model
line.construct()

## print a summary of the model lines save them in various ways
line.line.describe()
## alternative text formats
line.line.save(f'output/compute_emission_band/linelist.txt')
line.line.save(f'output/compute_emission_band/linelist.psv')
line.line.save(f'output/compute_emission_band/linelist.csv')
## binary formats, a hdf5 file or a directory tree containing numpy
## arrays (my favourite)
line.line.save(f'output/compute_emission_band/linelist.h5')
line.line.save(f'output/compute_emission_band/linelist',filetype='directory')

## plot energy levels
qfig(1)
vlevel.plot()

## plot a simulated spectrum
qfig(2)
line.plot(
    simple=True,
    xkey='ν',                   # plot on wavenumber scale, or 'λ'
    ykey='I',                   # Plot emission intensity                                # are 'I','σ','f','τ' and others
    Teq=1000,                   # equilibrium temperature
    # plot_labels=True,           # line assignments
)
savefig(f'output/compute_emission_band/spectrum.pdf')

show()
