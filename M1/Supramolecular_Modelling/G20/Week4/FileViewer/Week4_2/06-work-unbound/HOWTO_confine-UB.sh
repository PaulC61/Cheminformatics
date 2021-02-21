#!/bin/bash

#..source
source ../config.h
source ../software.h

#..LOCAL variables
PWD=`pwd`
awkd=../awk
prev=../02-vba-bound

#..RETRIEVE files 
cp ${prev}/SRC/file.kappa  ./KAPPA
ln -s ${prev}/1.0.vba      ./VBA-REST

#..COMPUTE REFs for r,theta,THETA
awk -f $awkd/mean.awk -v col=2 VBA-REST | awk '{print $2}' >> KAPPA
awk -f $awkd/mean.awk -v col=4 VBA-REST | awk '{print $2}' >> KAPPA
awk -f $awkd/mean.awk -v col=8 VBA-REST | awk '{print $2}' >> KAPPA

#..COMPUTE WORK
echo "sigma_L  ${sigma_L}"  >  SIGMA
echo "sigma_P  ${sigma_P}"  >> SIGMA
echo "sigma_PL ${sigma_PL}" >> SIGMA
#awk -f $awkd/work.awk -v IFILE=KAPPA -v IFILE2=SIGMA 
awk -f $awkd/work.awk -v IFILE=KAPPA -v IFILE2=SIGMA -v VERBOSE=1

#..CLEAN
rm KAPPA SIGMA 
rm VBA-REST
