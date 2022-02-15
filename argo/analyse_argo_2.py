"""Analyse chemistry output from ARGO model."""

from spectr.env import *
tools.warnings_off()

## create an AtmosphericChemistry object
model = atmosphere.AtmosphericChemistry()

## load argo model data
model.load_argo('data/early_earth/')

## compute rates at final timestep from data in ARGO output
model.reaction_network.calc_rates()

## plot abundances and summarise species
qfig(1)
model.plot_vertical('z(km)', ('n(NO)','n(NO₂)','n(N₂O)',))

for ispecies,species in enumerate((
        'NO',
        'NO₂',
        'N₂O',
        'O_¹D',
)):
    qfig(ispecies+2)
    model.plot_production_destruction(
        species, 
        ykey='z(km)',
        normalise= True,
        nsort=2,
    )
    print( )
    model.summarise_species(species)

show()
