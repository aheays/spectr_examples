"""Automatically fit multiple species in multiple spectra."""


from spectr.env import *
warnings.simplefilter('ignore')


## data about the experimental spectra scans
parameters = {
    'HCN_N2_0': {
        'filename':'data/2021_11_25_HCN_723Torr_mix+N2.0',
        'series': 'N2',
        'energy':0,
     },
    'HCN_N2_150': {
        'filename':'data/2021_11_25_HCN_721.8Torr_mix+N2_150J.0',
        'series': 'N2',
        'energy':150,
     },
    'HCN_N2_300': {
        'filename':'data/2021_11_25_HCN_720.8Torr_mix+N2_300J.0',
        'series': 'N2',
        'energy':300,
     },
    'HCN_N2_450': {
        'filename':'data/2021_11_25_HCN_720.1Torr_mix+N2_450J.0',
        'series': 'N2',
        'energy':450,
     },
    'HCN_N2_600': {
        'filename':'data/2021_11_25_HCN_719.5Torr_mix+N2_600J.0',
        'series': 'N2',
        'energy':600,
     },
}


## loop through scans
for iscan,key in enumerate(parameters):
    
    ## fit each one, save results, and plot
    o = spectrum.FitAbsorption(name=key,parameters=parameters[key])
    o.fit(
        species_to_fit=('HCN','CO',),
        region='bands',
        fit_N= True,
        fit_pair= True,
        fit_intensity= True,
        fig=iscan,
        ## maximum number of optimisation iterations
        max_nfev=10,            
    )
    o.save(f'output/fit_absorption_2/{key}')

## save all fitted parameters as a dictionary of parameters
tools.save_dict(f'output/fit_absorption_2/parameters.py', parameters=parameters)

## convert results in the parameters dictionary to a dataset, save
## this, and plot some things
data = spectrum.collect_fit_absorption_results(parameters)
print(data[['key','N_HCN','N_CO']])
data.save('output/fit_absorption_2/parameters.psv')
data.plot('energy',('N_HCN','N_CO'),fig=99)


show()



