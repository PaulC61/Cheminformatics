#!/bin/bash

#..source
source ../config.h
source ../software.h

#..LOCAL variables
PWD=`pwd`
srdir=$PWD/SRC
prev=../04-confine-unbound

#..RETRIEVE files 
TMPD=./tmp
if [ ! -d $TMPD ]; then mkdir $TMPD; fi
cp ${prev}/9.gro $TMPD/init.gro
cp ${prev}/9.cpt $TMPD/init.cpt
cp ${prev}/${guest}.top ./$TMPD/topol.top
cp ${prev}/ref-unb.pdb ./$TMPD
cp ${prev}/store/conf.dat ./$TMPD
ln -s ../charmm36-mar2019.ff ./

#..LOOP over lambda
for ll in 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20; do
#for ll in 0; do
wkdir=lambda_$ll
mkdir $wkdir
cp $TMPD/*   $wkdir/ 
echo $wkdir >> SUMM

#..RUN Gromacs
cd $wkdir/
cat $srdir/PROD.tmpl | \
sed s/YYYYY/$ll/g    | \
sed s/NNNNN/$guest/g > PROD.mdp
#
$gmx grompp -f PROD.mdp -c init.gro -t init.cpt -p topol.top -o alch.tpr -maxwarn 1
$gmx mdrun -deffnm alch -plumed conf.dat -v

#..store (checkpoint)
cp alch.cpt ../tmp/init.cpt
cp alch.gro ../tmp/init.gro

#..iterate
cd ../
done

#..clean
rm -rf $TMPD
rm \#* bck.*
exit
