#!/bin/bash

#..source
source ../config.h
source ../software.h

#..rename index
for nn in 0 1 2 3 4 5 6 7 8 9; do
newd=`printf "lambda_0%1d" $nn`
mv lambda_$nn ${newd}
echo $newd
done

#..store
mkdir dhdl-files
for ii in 00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20; do 
cp lambda_$ii/alch.xvg ./dhdl-files/production-lambda_$ii.xvg; 
done

#..RUN alcehmical analysis
alchemical_analysis -d dhdl-files/ -p production-lambda -u kcal -w -c -g -f 10
#alchemical_analysis -d dhdl-files/ -p production-lambda -u kcal -w -c -g -f 10 -s 10
#alchemical_analysis -d dhdl-files/ -p production-lambda -u kcal -w -c -g -f 10 -s 20
#alchemical_analysis -d dhdl-files/ -p production-lambda -u kcal -w -c -g -f 10 -s 30
#alchemical_analysis -d dhdl-files/ -p production-lambda -u kcal -w -c -g -f 10 -s 40
