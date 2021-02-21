#!/bin/bash

#..source
source ../config.h
source ../software.h

#..RETRIEVE files
prev=../01-confine-bound/
cp ${prev}/5.gro ./0.gro
cp ${prev}/5.cpt ./0.cpt
cp ${prev}/index.ndx ./
cp ${prev}/complex.top ./
cp ../00-bound/cluster/store/file.x0 ./
cp ../00-bound/cluster/store/ref-bnd.pdb ./
cp ../00-bound/cluster/store/vba-bnd.dat ./vba.tmpl

#..make STORE
store=./store
if [ ! -d $store ]; then mkdir $store; fi

#..Run VBA
nn=1
for ll in 0.0001 0.001 0.01 0.1 0.2 0.5 1.0; do

    #..set K values
    awk -f ../awk/k2.awk -v TMPL=vba.tmpl -v LAMBDA=$ll\
    -v X0=file.x0 -v KK=SRC/file.kappa -v KRMS=SRC/file.krms -v OUT=plumed.dat

    #..run GROMACS
    prev=$(($nn - 1))
    $gmx grompp -f SRC/PROD.mdp -c ${prev}.gro -t ${prev}.cpt\
    -p complex.top -o ${nn}.tpr -maxwarn 2
    $gmx mdrun -deffnm ${nn} -plumed plumed.dat -v

    #..store
    mv VBA_rest ${ll}.vba
    if [ $ll = "1.0" ]; then cp plumed.dat ${store}/vba.dat; fi 

    #..iterate
    ((nn++))
done

#..Finish
rm \#*
rm *.dat
