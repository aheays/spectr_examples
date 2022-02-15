"""Load, print, and plot various things about an ARGO atmospheric
model output."""

from spectr.env import *
tools.warnings_off()

## create an AtmosphericChemistry object
model = atmosphere.AtmosphericChemistry(
    encoding='ascii',           # default is 'unicode' which I prefer
)

## load ARGO output
model.load_argo('data/early_earth/')

## print a summary of the model
print( model)

## plot a summary of the model
qfig(1)
model.plot()

## Compute total atmosphere column density
print( )
print(f"total column density (cm-2):",integrate(model['z'],model['nt']))

## list surface mixing ratios
print( )
print('surface mixing ratio:')
for i,(a,b) in enumerate(model.get_surface_mixing_ratio().items()):
    if i>10: 
        break
    print(f'    {a:10} = {b:10.3e}')

## plot specific species data
qfig(2)
## density (cm-3)
model.plot_vertical('z(km)',('n(NO)','n(NO2)','n(N2O)',),ax=subplot(0))
## mixing ratio (cm-3)
model.plot_vertical('z(km)',('x(NO)','x(NO2)','x(N2O)',),ax=subplot(1))
## cumulative column density beginning at the top (cm-2)
model.plot_vertical('z(km)',('N(NO)','N(NO2)','N(N2O)',),ax=subplot(2))

show()
