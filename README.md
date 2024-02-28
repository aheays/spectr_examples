# `spectr_examples`

## Description

Some examples of using the `spectr` (<https://github.com/aheays/spectr>) library.

## Installation

To install these example scripts and data clone <https://github.com/aheays/spectr_examples>, with, e.g., , `git clone --depth=1 https://github.com/aheays/spectr_examples.git`.


## To run the example script

To run a script in an environment with `spectr` installed.

    cd subdirectory
    python script.py

Output from the scripts are in `subdirectory/output`.

To run all the scripts.

    ./run_all_examples.sh


## Description of examples

### Modelling absorption spectra

Example scripts showing how to quantify species in infrared absorption spectra.


#### `absorption/fit_one_line.py`

This function automatically fits the column density and pressure
broadening of HITRAN speces in IR absorption spectra.  This will
work sometimes but fail when the spectrum is more complex.
The frequency range is given by the preset `characteristic_infrared_bands`
values in <spectr/data/species_data.py>.  To fit other species (or
multiple) `'HCN'` with e.g., `'CO'` or `'H2O'`.


#### `absorption/fit_manually_1.py`

This is a lower-level script that fits a small part of one
spectrum.  The model results are output to
`output/fit_manually_1/model_of_experiment`.


#### `absorption/fit_manually_2.py`

A script that fits an entire spectrum including all identified species.


#### `absorption/fit_manually_3.py`

A script that fits the CO fundamental band including more instrumental
effects.


#### `absorption/fit_absorption_1.py`

This script uses a FitAbsorption object to more conveniently fit
multiple species in a spectrum.  


#### `absorption/fit_absorption_2.py`

A FitAbsorption script that fits multiple species in multiple spectra.


#### `absorption/fit_absorption_3.py`

A FitAbsorption script to that fits a cross section file (downloaded from HITRAN) to an experimental spectrum.  It also uses a measured background rather than a fitted spline curve.



### Modelling emission spectra


#### `emission/compute_emission_band.py`

Computes a list of diatomic level energies from molecular constants of electronic-vibrational bands, and then computes a linelist of electric-dipole transitions.


#### `emission/fit_emission_band_1.py`

Uses a linelist computed from molecular constants to fit the temperature of \ce{N2} emission in a laboratory spectrum. 


#### `emission/fit_emission_band_2.py`

Fit the temperature and molecular constants of multiple \ce{N2} emission bands in a laboratory spectrum. 


#### `emission/fit_emission_band_3.py`

Fit an effective J-dependent rotational temperature to some emission bands.



### Analysing ARGO output


#### `argo/analyse_argo_1.py`

Load a model and print whats in it.


#### `argo/analyse_argo_2.py`

Plot the dominant production and destruction reactions affecting particular species.


#### `argo/analyse_argo_3.py`

Compare two models.



### Computing effective-Hamiltonian diatomic level energies and linelists

1.  `viblevel/3Π_3Σ+_transition.py`

    Compute level energies from molecular constants and combine into a
    line list.

2.  `viblevel/run_comparison_with_pgopher.py`

    Compare various linear transitions with the output of pgopher.

