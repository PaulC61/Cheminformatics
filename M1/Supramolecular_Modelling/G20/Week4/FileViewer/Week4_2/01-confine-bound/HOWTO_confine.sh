#!/bin/bash

#..source
source ../config.h
source ../software.h

#..RETRIEVE files
prev=../00-bound
cp ${prev}/complex.top ./
cp ${prev}/index.ndx ./
cp ${prev}/cluster/store/ref-bnd.pdb ./
cp ${prev}/cluster/store/conf-bnd.dat ./conf.tmpl

#..local variables
itop=complex.top

#..PREPARE files
cp ${prev}/prod.gro 0.gro
cp ${prev}/prod.cpt 0.cpt

#..CONFINE
nn=1
KF=400000
for ll in 0.0025 0.005 0.0075 0.01 0.1 0.15 0.2 0.3 0.4 0.5 0.6 0.7 1.0; do

    #..determine K
    KK=`awk -v KF=${KF} -v LAMBDA=${ll} 'BEGIN{print KF*LAMBDA}'`
    sed s/KKKKK/${KK}/g  conf.tmpl > file.dat

    #..run GROMACS
    prev=$(($nn - 1))
    $gmx grompp -f SRC/PROD.mdp -c ${prev}.gro -t ${prev}.cpt -p $itop -o ${nn}.tpr -maxwarn 2
    $gmx mdrun -deffnm ${nn} -plumed file.dat -v

    #..clean
    mv CONF.out ${ll}.rms
    rm *.dat

    #..iterate
    ((nn++))
done
    
#..Finish
rm \#*
rm *.dat
