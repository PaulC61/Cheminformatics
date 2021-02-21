#!/bin/bash

#export LC_ALL=C
source ../software.h

#..ANALYZE confinement
REF=0.0
KF=100000
if [ -f RMS ]; then rm RMS; fi
for ll in 0.0025 0.005 0.0075 0.01 0.1 0.15 0.2 0.3 0.4 0.5 0.6 0.7 1.0; do
#..ensemble-averaged dU/dl 
awk -f ../awk/mean.awk -v col=3 $ll.rms | \
awk -v LAMBDA=$ll '{printf("%12.7f %9.5f\n", LAMBDA, $2/LAMBDA)}' >> RMS
done
#..integration
awk -f ../awk/trapez.awk -v VERBOSE=1 RMS > CONF.dhdl
awk -f ../awk/trapez.awk -v VERBOSE=0 RMS
#..store
mv RMS CONF.rms
exit
