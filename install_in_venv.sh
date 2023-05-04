#!/usr/bin/env bash
trap exit int
# set -o nounset -o errexit -o xtrace
set -o nounset -o errexit 

####################################################################
## A script to install spectr and its dependencies into a virtual ##
## environment                                                    ##
####################################################################

echo "### make and start virtual environment"
python3 -m venv venv3
source venv3/bin/activate

echo "### install packages from pip"
for package in bidict cycler hitran-api brukeropusreader dill h5py matplotlib numpy openpyxl periodictable scipy sympy xmltodict py3nj pyqt5 ; do
    pip install $package
done

echo "### clone or update spectr and symlink into python and executable paths"
if [ -d spectr ] ; then
    cd spectr
    echo "### spectr already cloned, pulling update"
    git pull --depth=1 --rebase
    cd -
else
    echo "### cloning spectr"
    git clone --depth=1 https://github.com/aheays/spectr.git
fi

echo "### copy spectr into whatever python site-packages directory is present in the virtual environment"
for dir in venv3/lib/python*/site-packages/ ; do
    cd $dir
    if [ ! -e spectr ] ; then
       ln -s ../../../../spectr .
    fi
    cd -
done

echo "### copy qplot into venv bin"
cd venv3/bin
if [ ! -e qplot ] ; then
    ln -s ../../spectr/qplot .
fi
cd -

echo "### compile fortran extensions"
cd spectr
make
cd -

echo "### basic test"
source venv3/bin/activate
echo "from spectr.env import *" | python
qplot absorption/data/2021_11_25_HCN_719.5Torr_mix+N2_600J.0
deactivate

