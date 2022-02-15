"""Compute level energies from molecular constants and combine into a
line list."""

from spectr.env import *

## level data
vlevel = viblevel.Level(species='32S16O')

## lower state
vlevel.add_manifold(name='X.3Σ+(v=0)', Tv=0, Bv=1, λv=1, γv=0.01)

## upper state
vlevel.add_manifold(name='B.3Π(v=0)', Tv=50000, Bv=1.1, Av=10) 

# ## vline
vline = viblevel.Line(vlevel)
vline.add_transition_moment('B.3Π(v=0)','X.3Σ+(v=0)',μv=1)
vline.construct()

## save output
vline.line['ν']
vline.line.save('t0.psv')

## plot
vlevel.plot(fig=1)
vline.plot(fig=2)
show()
