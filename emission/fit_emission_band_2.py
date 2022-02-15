"""Fit emission bands in appearing in a spectrum."""

from spectr.env import *

## make a model of many N2 emission transitions using reference
## molecular constants. Some of these were optimised to fit the
## spectrum.
vlevel = viblevel.Level(name='vlevel',species='¹⁴N₂',Eref=0.0)
for kwargs in (
        dict(name='B³Πg(v=5)', Tv=P(+1.778675278e+04,False, 1e-03,    nan), Bv=P(+1.536530510e+00,None , 1e-05,    nan), Dv=P(+6.054110000e-06,None , 1e-07,    nan), Hv=P(-2.864240000e-12,None , 1e-11,    nan), Av=P(+4.196410000e+01,None , 1e-03,    nan), ADv=P(-4.216350000e-04,None , 1e-05,    nan), λv=P(-2.110340000e-01,None , 1e-03,    nan), λDv=P(-7.176060000e-07,None , 1e-05,    nan), γv=P(-3.765210000e-03,None , 1e-03,    nan), ov=P(+1.141520000e+00,None , 1e-03,    nan), pv=P(+4.248960000e-03,None , 1e-03,    nan), qv=P(+7.460850000e-05,None , 1e-05,    nan),),
        dict(name='B³Πg(v=6)', Tv=P(+1.934700734e+04,False, 1e-03,    nan), Bv=P(+1.517715750e+00,None , 1e-05,    nan), Dv=P(+6.099210000e-06,None , 1e-07,    nan), Hv=P(-3.692640000e-12,None , 1e-11,    nan), Av=P(+4.189260000e+01,None , 1e-03,    nan), ADv=P(-4.216350000e-04,None , 1e-05,    nan), λv=P(-2.126710000e-01,None , 1e-03,    nan), λDv=P(-7.413250000e-07,None , 1e-05,    nan), γv=P(-3.800170000e-03,None , 1e-03,    nan), ov=P(+1.139080000e+00,None , 1e-03,    nan), pv=P(+4.226940000e-03,None , 1e-03,    nan), qv=P(+7.226220000e-05,None , 1e-05,    nan), ),
        dict(name='B³Πg(v=7)', Tv=P(+2.087804456e+04,False, 1e-03,    nan), Bv=P(+1.498763120e+00,None , 1e-05,    nan), Dv=P(+6.147670000e-06,None , 1e-07,    nan), Hv=P(-4.632100000e-12,None , 1e-11,    nan), Av=P(+4.181550000e+01,None , 1e-03,    nan), ADv=P(-4.216350000e-04,None , 1e-05,    nan), λv=P(-2.153920000e-01,None , 1e-03,    nan), λDv=P(-7.665540000e-07,None , 1e-05,    nan), γv=P(-3.766390000e-03,None , 1e-03,    nan), ov=P(+1.136580000e+00,None , 1e-03,    nan), pv=P(+4.204390000e-03,None , 1e-03,    nan), qv=P(+6.985930000e-05,None , 1e-05,    nan), ),
        dict(name='B³Πg(v=8)', Tv=P(+2.237976604e+04,False, 1e-03,    nan), Bv=P(+1.479672870e+00,None , 1e-05,    nan), Dv=P(+6.200040000e-06,None , 1e-07,    nan), Hv=P(-5.700030000e-12,None , 1e-11,    nan), Av=P(+4.172820000e+01,None , 1e-03,    nan), ADv=P(-4.216350000e-04,None , 1e-05,    nan), λv=P(-2.167990000e-01,None , 1e-03,    nan), λDv=P(-7.934770000e-07,None , 1e-05,    nan), γv=P(-3.909800000e-03,None , 1e-03,    nan), ov=P(+1.134020000e+00,None , 1e-03,    nan), pv=P(+4.181280000e-03,None , 1e-03,    nan), qv=P(+6.739640000e-05,None , 1e-05,    nan), ),
        dict(name='B³Πg(v=9)', Tv=P(+2.385205323e+04,False, 1e-03,    nan), Bv=P(+1.460436280e+00,None , 1e-05,    nan), Dv=P(+6.256900000e-06,None , 1e-07,    nan), Hv=P(-6.919220000e-12,None , 1e-11,    nan), Av=P(+4.162810000e+01,None , 1e-03,    nan), ADv=P(-4.216350000e-04,None , 1e-05,    nan), λv=P(-2.284470000e-01,None , 1e-03,    nan), λDv=P(-8.223070000e-07,None , 1e-05,    nan), γv=P(-4.266480000e-03,None , 1e-03,    nan), ov=P(+1.131390000e+00,None , 1e-03,    nan), pv=P(+4.157560000e-03,None , 1e-03,    nan), qv=P(+6.486950000e-05,None , 1e-05,    nan), ),
        dict(name='B³Πg(v=10)', Tv=P(+2.529478208e+04,False, 1e-03,    nan), Bv=P(+1.441005453e+00, None, 1e-05,    nan), Dv=P(+6.383165342e-06, None, 1e-07,    nan), Hv=P(-5.087147435e-11, None, 1e-11,    nan), Av=P(+4.152704828e+01, None, 1e-03,    nan), ADv=P(-5.028500686e-05, None, 1e-05,    nan), λv=P(-2.250780303e-01, None, 1e-03,    nan), λDv=P(+3.935710606e-05, None, 1e-05,    nan), γv=P(+8.854770713e-04, None, 1e-03,    nan), ov=P(+1.127102490e+00, None, 1e-03,    nan), pv=P(+4.033314697e-03, None, 1e-03,    nan), qv=P(+4.509206195e-05, None, 1e-05,    nan), ),
        dict(name='B³Πg(v=11)', Tv=P(+2.670777567e+04,False, 1e-03,    nan), Bv=P(+1.421353620e+00, None, 1e-05,    nan), Dv=P(+6.371179439e-06, None, 1e-07,    nan), Hv=P(-2.614566051e-11, None, 1e-11,    nan), Av=P(+4.142434578e+01, None, 1e-03,    nan), ADv=P(-4.694029661e-04, None, 1e-05,    nan), λv=P(-2.247473910e-01, None, 1e-03,    nan), λDv=P(-1.336042033e-06, None, 1e-05,    nan), γv=P(-4.303296602e-03, None, 1e-03,    nan), ov=P(+1.126050527e+00, None, 1e-03,    nan), pv=P(+4.153972874e-03, None, 1e-03,    nan), qv=P(+7.170744942e-05, None, 1e-05,    nan), ),
        dict(name='B³Πg(v=12)', Tv=P(+2.809084741e+04,False, 1e-03,    nan), Bv=P(+1.401585733e+00, None, 1e-05,    nan), Dv=P(+6.578712515e-06, None, 1e-07,    nan), Hv=P(+1.014022674e-10, None, 1e-11,    nan), Av=P(+4.128782544e+01, None, 1e-03,    nan), ADv=P(+2.901869790e-04, None, 1e-05,    nan), λv=P(-2.231579117e-01, None, 1e-03,    nan), λDv=P(-1.218427112e-04, None, 1e-05,    nan), γv=P(+5.884270333e-03, None, 1e-03,    nan), ov=P(+1.121524448e+00, None, 1e-03,    nan), pv=P(+4.261247857e-03, None, 1e-03,    nan), qv=P(+4.563939598e-05, None, 1e-05,    nan), ),
        dict(name='A³Σ⁺u(v=1)', Tv=P(+1.432907228e+03,None , 1e-03,    nan), Bv=P(+1.427461100e+00,None , 1e-05,    nan), Dv=P(+5.835380000e-06,None , 1e-07,    nan), Hv=P(-3.741380000e-12,None , 1e-11,    nan), λv=P(-1.321360000e+00,None , 1e-03,    nan), λDv=P(+3.133830000e-06,None , 1e-05,    nan), γv=P(-2.692640000e-03,None , 1e-03,    nan), ),
        dict(name='A³Σ⁺u(v=2)', Tv=P(+2.838142625e+03,None , 1e-03,    nan), Bv=P(+1.409051690e+00,None , 1e-05,    nan), Dv=P(+5.876890000e-06,None , 1e-07,    nan), Hv=P(-4.649380000e-12,None , 1e-11,    nan), λv=P(-1.314240000e+00,None , 1e-03,    nan), λDv=P(+3.244760000e-06,None , 1e-05,    nan), γv=P(-2.666680000e-03,None , 1e-03,    nan), ),
        dict(name='A³Σ⁺u(v=3)', Tv=P(+4.215637934e+03,None , 1e-03,    nan), Bv=P(+1.390529710e+00,None , 1e-05,    nan), Dv=P(+5.925480000e-06,None , 1e-07,    nan), Hv=P(-5.654760000e-12,None , 1e-11,    nan), λv=P(-1.306950000e+00,None , 1e-03,    nan), λDv=P(+3.362630000e-06,None , 1e-05,    nan), γv=P(-2.640070000e-03,None , 1e-03,    nan), ),
        dict(name='A³Σ⁺u(v=4)', Tv=P(+5.565297497e+03,None , 1e-03,    nan), Bv=P(+1.371876850e+00,None , 1e-05,    nan), Dv=P(+5.977560000e-06,None , 1e-07,    nan), Hv=P(-6.814150000e-12,None , 1e-11,    nan), λv=P(-1.299470000e+00,None , 1e-03,    nan), λDv=P(+3.488490000e-06,None , 1e-05,    nan), γv=P(-2.612760000e-03,None , 1e-03,    nan), ),
        dict(name='A³Σ⁺u(v=5)', Tv=P(+6.886992706e+03,None , 1e-03,    nan), Bv=P(+1.353074860e+00,None , 1e-05,    nan), Dv=P(+6.034170000e-06,None , 1e-07,    nan), Hv=P(-8.193960000e-12,None , 1e-11,    nan), λv=P(-1.291800000e+00,None , 1e-03,    nan), λDv=P(+3.623760000e-06,None , 1e-05,    nan), γv=P(-2.584710000e-03,None , 1e-03,    nan), ),
        dict(name='A³Σ⁺u(v=6)', Tv=P(+8.180556804e+03,None , 1e-03,    nan), Bv=P(+1.334101870e+00,None , 1e-05,    nan), Dv=P(+6.096720000e-06,None , 1e-07,    nan), Hv=P(-9.869190000e-12,None , 1e-11,    nan), λv=P(-1.283910000e+00,None , 1e-03,    nan), λDv=P(+3.770300000e-06,None , 1e-05,    nan), γv=P(-2.555860000e-03,None , 1e-03,    nan), ),
        dict(name='A³Σ⁺u(v=7)', Tv=P(+9.445778704e+03,None , 1e-03,    nan), Bv=P(+1.314932170e+00,None , 1e-05,    nan), Dv=P(+6.166930000e-06,None , 1e-07,    nan), Hv=P(-1.192320000e-11,None , 1e-11,    nan), λv=P(-1.275800000e+00,None , 1e-03,    nan), λDv=P(+3.930410000e-06,None , 1e-05,    nan), γv=P(-2.526140000e-03,None , 1e-03,    nan), ),
        dict(name='A³Σ⁺u(v=8)', Tv=P(+1.068239621e+04,None , 1e-03,    nan), Bv=P(+1.295534970e+00,None , 1e-05,    nan), Dv=P(+6.246830000e-06,None , 1e-07,    nan), Hv=P(-1.444900000e-11,None , 1e-11,    nan), λv=P(-1.267430000e+00,None , 1e-03,    nan), λDv=P(+4.106940000e-06,None , 1e-05,    nan), γv=P(-2.495470000e-03,None , 1e-03,    nan), ),
):
    vlevel.add_manifold(**kwargs)

vline = viblevel.Line('vline',vlevel)
vline.add_transition_moment(name_u='B³Πg(v=5)'  , name_l='A³Σ⁺u(v=1)' , μv=P(0.597898245576 ,False, 1e-05))
vline.add_transition_moment(name_u='B³Πg(v=6)'  , name_l='A³Σ⁺u(v=2)' , μv=1)
vline.add_transition_moment(name_u='B³Πg(v=7)'  , name_l='A³Σ⁺u(v=3)' , μv=P(1.08517554849  ,False, 1e-05))
vline.add_transition_moment(name_u='B³Πg(v=8)'  , name_l='A³Σ⁺u(v=4)' , μv=P(1.07019214     ,False, 1e-05))
vline.add_transition_moment(name_u='B³Πg(v=9)'  , name_l='A³Σ⁺u(v=5)' , μv=P(1.14921452256  ,False, 1e-05))
vline.add_transition_moment(name_u='B³Πg(v=10)' , name_l='A³Σ⁺u(v=6)' , μv=P(1.10146908421  ,False, 1e-05))
vline.add_transition_moment(name_u='B³Πg(v=11)' , name_l='A³Σ⁺u(v=7)' , μv=P(1.03850935806  ,False, 1e-05))
vline.add_transition_moment(name_u='B³Πg(v=12)' , name_l='A³Σ⁺u(v=8)' , μv=P(0.847435737083 ,False, 1e-05))

## load experimental spectrum, reduce its resolution for convenience
experiment = spectrum.Experiment()
experiment.set_spectrum_from_opus_file('data/N2_He_24022020_1_0.05 cm_50 sc_CaF2_PMT Vis 350V_(7+10) torr_200 A_full_16000-18000.0')
experiment.convolve_with_gaussian(1)

## model with spline background and emission lines
model = spectrum.Model('model',experiment)
model.add_spline(knots=[[15999.99900543663, P(0.839442836078,False,3.5e-06,0.0054)], [16197.456200535278, P(0.593401285323,False,6.1e-06,0.0023)], [16815.831991442414, P(0.43399669267,False,1e-05,0.0029)], [17296.141420691987, P(0.227746354763,False,8.4e-06,0.0029)], [17916.686739761353, P(0.12879900716,False,-9.3e-07,0.0032)], [18000.00264765816, P(0.145020022099,False,-2.8e-06,0.0058)]])
model.add_line(
    ## The output linelist of a VibLine object. It is a Dataset.
    line=vline.line,
    ## add emission lines
    kind='emission',
    ## Simulate pure Gaussian lines of 0.2 cm-1.FWHM. This is done
    ## by specirying the Lorentzian FWHM to be 0
    ΓG=1,
    ΓL=0,
    ## select the method for computing rotational partition function,
    ## in this case computed from the data in the vibline object
    Zsource='self',
    ## The instrumental efficiency. This is not well defined, and is
    ## degenerate with the fitted band strength.  Th value chosen here
    ## is arbitrary and referenced to the B(6)-A(2) transition
    Finstr     = P(9.79014691878e-12,False,1e-16,1.2e-14),
    # Finstr     = P(1.6800900131e-13, True,1e-16,2.1e-16),
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
    ## A nonthermal vibrational population (fixed to one for all
    ## v-levels in this case), and a rotational temperature.  If the
    ## vibrational band strengths, μv, above are fitted to the
    ## spectrum this will fit any vibrational distribution, but the
    ## vibrational excitation is now degenerate with the band
    ## strength.  Still assumes thermal rotational excitation, which
    ## might well be the case.
    αvib_u=1,
    Trot       = P(320.596574162,False,1,0.41),
)

## optimise adjustable parameters
model.optimise()

## print any regenerated input file lines containing optimised
## parameters
model.print_input('.*True.*')   

## plot the reults and label emission line assignments
model.plot(
    fig=1,
    plot_labels=True,
    label_zkeys=('label_u','v_u','label_l','v_l'), # do not divide branches into different spin-transitions
    label_key=None,                                # do not label rotational transition
    label_match={'not_Sij':0},                     # only label lines with nonzero intensity
)
show()


