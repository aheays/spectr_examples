#!/usr/bin/env python

## run files listed below to see if they generate an error


import subprocess,os,importlib

## non gui backend to matplotlib to prevent blocking
import matplotlib
matplotlib.use('pdf')


original_directory = os.getcwd()
for path in (

        'absorption/fit_absorption_1.py',
        'absorption/fit_absorption_2.py',
        'absorption/fit_absorption_3.py',
        'absorption/fit_manually_1.py',
        'absorption/fit_manually_2.py',
        'absorption/fit_manually_3.py',
        'absorption/fit_one_line.py',
        'argo/analyse_argo_1.py',
        'argo/analyse_argo_2.py',
        'argo/analyse_argo_3.py',
        'emission/compute_emission_band.py',
        'emission/fit_emission_band_1.py',
        'emission/fit_emission_band_2.py',
        'emission/fit_emission_band_3.py',
        'viblevel/3Π_3Σ+_transition.py',

):
    print(f'\n\n===== running {path!r} =====')
    directory,filename = os.path.split(path)
    os.chdir(original_directory)
    os.chdir(directory)
    exec(open(filename).read())

