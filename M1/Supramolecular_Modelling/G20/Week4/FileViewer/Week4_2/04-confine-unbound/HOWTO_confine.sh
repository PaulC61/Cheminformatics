#!/bin/bash

#..source
source ../config.h
source ../software.h

#..RETRIEVE files
PWD=`pwd`
srdir=$PWD/SRC
prev=../00-unbound
cp ${prev}/${guest}.top ./
cp ../00-bound/cluster/store/ref-unb.pdb ./ 
cp ../00-bound/cluster/store/conf-unb.dat ./conf.tmpl  

#..PREPARE files
itop=${guest}.top
cp ${prev}/prod.gro 0.gro
cp ${prev}/prod.cpt 0.cpt

#..make STORE
store=./store
if [ ! -d $store ]; then mkdir $store; fi

#..CONFINE
nn=1
KF=100000
for ll in 0.0025 0.005 0.0075 0.01 0.1 0.15 0.2 0.3 0.4 0.5 0.6 0.7 1.0; do

    #..determine K
    KK=`awk -v KF=${KF} -v LAMBDA=${ll} 'BEGIN{print KF*LAMBDA}'`
    sed s/KKKKK/${KK}/g  conf.tmpl > file.dat

    #..run GROMACS
    prev=$(($nn - 1))
    $gmx grompp -f SRC/PROD.mdp -c ${prev}.gro -t ${prev}.cpt -p $itop -o ${nn}.tpr -maxwarn 2
    $gmx mdrun -deffnm ${nn} -plumed file.dat -v

    #..store
    mv CONF.out ${ll}.rms
    if [ $ll = "1.0" ]; then cp file.dat ${store}/conf.dat; fi

    #..iterate
    ((nn++))
done
    
#..Finish
rm \#*
rm *.dat
rm conf.tmpl
