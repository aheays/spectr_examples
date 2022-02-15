"""Compare two ARGO models."""

from spectr.env import *
tools.warnings_off()

## load two models
model0 = atmosphere.AtmosphericChemistry()
model0.load_argo('data/early_earth/')
model0.reaction_network.calc_rates()
model1 = atmosphere.AtmosphericChemistry()
model1.load_argo('data/early_earth_reduced')
model1.reaction_network.calc_rates()

## compare density of abundant species
qfig(1)
model0.plot_density(ax=subplot(0))
title('model0');ylim(0,70)
model1.plot_density(ax=subplot(1))
title('model1');ylim(0,70)

## compare NxOy species
qfig(2)
model0.plot_vertical('z(km)',('n(NO)','n(NO₂)','n(N₂O)'),linestyle='-',ax=gca())
model1.plot_vertical('z(km)',('n(NO)','n(NO₂)','n(N₂O)'),linestyle=':',ax=gca())
ylim(0,70)

## compare N2O formation / destruction
qfig(3)
model0.plot_production_destruction('N₂O',normalise=True,ax=subplot(0,ncolumns=2))
title('model0')
model1.plot_production_destruction('N₂O',normalise=True,ax=subplot(1,ncolumns=2))
title('model1')

show()
