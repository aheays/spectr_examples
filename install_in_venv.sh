#!/usr/bin/env bash
trap exit int
set -o nounset -o errexit -o xtrace

####################################################################
## A script to install spectr and its dependencies into a virtual ##
## environment. Pretty dangerous to run this                      ##
####################################################################

## make and start virtual environment
python3.9 -m venv venv3.9
source venv3.9/bin/activate

## install packages from pip
for package in bidict cycler hitran-api brukeropusreader dill h5py matplotlib numpy openpyxl periodictable scipy sympy xmltodict py3nj pyqt5 ; do
    pip install $package
done

## clone spectr and symlink into python and executable paths
git clone --depth=1 https://github.com/aheays/spectr.git

cd venv3.9/lib/python3.9/site-packages/
ln -s ../../../../spectr .
cd -

cd venv3.9/bin
ln -s ../../spectr/qplot .
cd -

## compile fortran extensions
cd spectr
make

## clone example scripts
git clone --depth=1 https://github.com/aheays/spectr_examples.git

## test
source venv3.9/bin/activate
echo "from spectr.env import *" | python
qplot spectr_examples/absorption/data/2021_11_30_bcgr.0

## close virtual environment
deactivate

