#!/bin/bash

#..source
source ../../software.h
source ../../config.h

#..local variables
coff=0.1

#..make STORE
store=./store
if [ ! -d $store ]; then mkdir $store; fi

#..BOUND state
#..CLUSTER trj based on RMSD
echo "${host}_${guest} ${host}_${guest}" | \
$gmx cluster -f ../noPBC.xtc -n ../index.ndx -s ../prod.tpr -dist -cutoff $coff -cl -method jarvis-patrick
#exit

#..EXTRACT most populated cluster
nRow=`grep -c ATOM ../complex_min.pdb | awk '{print $1}'`
grep -A $nRow "MODEL        7" clusters.pdb | tail -$nRow > most_populated.pdb
#exit

#..EXTRACT Reference structure for INT restraint
sed s/"0.00 "/"1.00 "/g most_populated.pdb | grep " ${guest} " > ref-bnd.pdb

#..PREPARE plumed for CONF/VBA
ipdb=ref-bnd.pdb
BEG=`head -1 $ipdb | awk '{print $2}'`
END=`tail -1 $ipdb | awk '{print $2}'`
cat SRC/conf.tmpl | sed s/XXX/$BEG/g | sed s/YYY/$END/g | sed s/RRRRR/$ipdb/g > conf-bnd.dat
#exit
cat SRC/vba.tmpl  | sed s/XXX/$BEG/g | sed s/YYY/$END/g | sed s/RRRRR/$ipdb/g | \
  sed s/P1/18/g  | sed s/P2/108/g   | sed s/P3/30/g   | \
  sed s/L1/131/g  | sed s/L2/129/g   | sed s/L3/137/g   > vba-bnd.dat
#exit

#..EXTRCT Ref values for POS/ORIE
cat SRC/refs.tmpl | sed s/XXX/$BEG/g | sed s/YYY/$END/g | sed s/RRRRR/$ipdb/g | \
  sed s/P1/18/g  | sed s/P2/108/g   | sed s/P3/30/g   | \
  sed s/L1/131/g  | sed s/L2/129/g   | sed s/L3/137/g   > refs.dat 
#..pdb
plumed driver --plumed refs.dat --mf_pdb most_populated.pdb
cat BOUND | awk 'substr($0,1,1)!="#"{for(ii=3;ii<=NF;ii++){print $ii}}' > file.x0
#..xtc
plumed driver --plumed refs.dat --mf_xtc ../noPBC.xtc  
#exit

#..UNBOUND state
#..CLUSTER trj based on RMSD
echo "${host}_${guest} ${guest}" | \
$gmx cluster -f ../noPBC.xtc -n ../index.ndx -s ../prod.tpr -dist -cutoff $coff -cl -method jarvis-patrick

#..EXTRACT most populated cluster
nRow=`grep -c ${guest} ../complex_min.pdb | awk '{print $1}'`
grep -A $nRow "MODEL        1" clusters.pdb | tail -$nRow | sed s/"0.00 "/"1.00 "/g > ref-unb.pdb 
#exit

#..PREPARE plumed for CONF
ipdb=ref-unb.pdb
BEG=`head -1 $ipdb | awk '{print $2}'`
END=`tail -1 $ipdb | awk '{print $2}'`
cat SRC/conf.tmpl | sed s/XXX/$BEG/g | sed s/YYY/$END/g | sed s/RRRRR/$ipdb/g > conf-unb.dat
#exit

#..STORE
cp file.x0 $store
mv refs.dat $store
cp vba-bnd.dat $store
mv conf-bnd.dat $store
mv conf-unb.dat $store
mv ref-bnd.pdb $store
mv ref-unb.pdb $store
mv most_populated.pdb $store
mv BOUND $store

#..clean
rm \#*
rm bck.*
rm rmsd*
rm cluster*

exit
