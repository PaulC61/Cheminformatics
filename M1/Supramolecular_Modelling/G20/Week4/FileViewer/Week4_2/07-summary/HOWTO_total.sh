#!/bin/bash

#..source
source ../config.h
source ../software.h

#..LOCAL variables
wkdir=`pwd`

#..RETRIEVE files
cd ../01-confine-bound
./ANAL_confine.sh > $wkdir/CONF_BND.dG

cd ../02-vba-bound
./ANAL_vba.sh > $wkdir/VBA_BND.dG

cd ../03-alchemical-bound
FILE=dhdl-files/results.txt
if [ -f $FILE ]; then 
cat $FILE > $wkdir/ALCH_BND.dG; 
else ./ANAL.sh > $wkdir/ALCH_BND.dG; 
fi

cd ../04-confine-unbound
./ANAL_confine.sh > $wkdir/CONF_UB.dG

cd ../05-alchemical-unbound
FILE=dhdl-files/results.txt
if [ -f $FILE ]; then                      
cat $FILE > $wkdir/ALCH_UB.dG;
else ./ANAL.sh > $wkdir/ALCH_UB.dG;
fi

cd ../06-work-unbound/
./HOWTO_confine-UB.sh > $wkdir/VBA_UB.dG

#..
cd $wkdir
FILE="dG"
if [ -f $FILE ]; then
rm $FILE
fi

#..restrain LIGAND in UNBOUND state
echo "CONF_UB"
cat CONF_UB.dG | tail -1 | awk '{print $1, "kcal/mol"}'
cat CONF_UB.dG | tail -1 | awk '{print $1, "kcal/mol"}' >> dG
echo ""

echo "VBA_UB"
cat VBA_UB.dG  | awk '{print  $2, "kcal/mol"}'
cat VBA_UB.dG  | awk '{print  $2, "kcal/mol"}' | tail -1 >> dG
echo ""

#..decouple LIGAND in UNBOUND state
echo "ALCH_UB"
grep "TOTAL:" ALCH_UB.dG | awk '{print $17, $18, $19, "kcal/mol"}'
grep "TOTAL:" ALCH_UB.dG | awk '{print $17, $18, $19, "kcal/mol"}' >> dG

#..recouple  LIGAND in BOUND state
echo "ALCH_BND"
grep "TOTAL:" ALCH_BND.dG | awk '{print -$17, $18, $19, "kcal/mol"}'
grep "TOTAL:" ALCH_BND.dG | awk '{print -$17, $18, $19, "kcal/mol"}' >> dG
echo ""

#..release LIGAND in BOUND state
echo "VBA_BND"
cat VBA_BND.dG  | awk '{print  -$1, "kcal/mol"}' 
cat VBA_BND.dG  | awk '{print  -$1, "kcal/mol"}' >> dG
echo ""

echo "CONF_BND"
cat CONF_BND.dG | tail -1 | awk '{print -$1, "kcal/mol"}'
cat CONF_BND.dG | tail -1 | awk '{print -$1, "kcal/mol"}' >> dG
echo ""

#..summary
awk -v ID=$guest '{sum+=$1}END{printf("DDM> %s %7.2f kcal/mol\n", ID, sum)}' dG
