#!/bin/bash

#..SOURCE
source ../config.h
source ../software.h

#..RETRIEVE files
cat SRC/complex.tmpl | \
sed s/XXXXX/${host}/g | \
sed s/YYYYY/${guest}/g > complex.top
cp ../IDAT/${host}-${guest}-original.pdb ./complex_min.pdb

#..LOCAL variables
itop=complex.top
ipdb=complex_min.pdb

#..PREPARE simulation BOX
echo "0" | $gmx editconf -f ${ipdb} -o cubic-box.gro\
 -bt cubic -d 1.2 -c -princ

#..SOLVATE
$gmx solvate -p ${itop} -cp cubic-box.gro -cs spc216.gro \
 -o cubic-box-solv.gro >& TMP

#..IONIZE
$gmx grompp -f SRC/MINI.mdp -c cubic-box-solv.gro -p ${itop} -o ions.tpr -maxwarn 2 >& TMP
charge=`grep "System has non-zero total charge" TMP | awk '{print $6}'`
#
ogro=cubic-box-solv-ions.gro
if [ $charge ]; then
        echo "MC> CHARGED!"
        if [ $charge \> 0.0 ]; then
                anions=`awk -v Q=$charge 'BEGIN{print int(Q)}'`
                echo "MC> anions: $anions"
                echo "SOL" | $gmx genion -s ions.tpr -o ${ogro} -p ${itop} -pname NA -nname CL -nn ${anions}
        else
                cations=`awk -v Q=$charge 'BEGIN{print int(Q)}'`
                echo "MC> cations: $cations"
                echo "SOL" | $gmx genion -s ions.tpr -o ${ogro} -p ${itop} -pname NA -nname CL -np ${cations}
        fi
else
        echo "MC> NEUTRAL!"
	cp cubic-box-solv.gro ${ogro}
fi

#..RUN DYNAMICS
$gmx grompp -f SRC/MINI.mdp -c ${ogro} -p ${itop} -o mini.tpr -maxwarn 2
$gmx mdrun -v -deffnm mini 
$gmx grompp -f SRC/HEAT.mdp -c mini.gro -r mini.gro -p ${itop} -o heat.tpr -maxwarn 2
$gmx mdrun -v -deffnm heat
$gmx grompp -f SRC/EQLB1.mdp -c heat.gro -p ${itop} -o eqlb1.tpr -maxwarn 2
$gmx mdrun -v -deffnm eqlb1
$gmx grompp -f SRC/EQLB2.mdp -c eqlb1.gro -t eqlb1.cpt -p ${itop} -o eqlb2.tpr -maxwarn 2
$gmx mdrun -v -deffnm eqlb2
$gmx grompp -f SRC/PROD.mdp  -c eqlb2.gro -t eqlb2.cpt -p ${itop} -o prod.tpr -maxwarn 2
$gmx mdrun -v -deffnm prod

#..generate index
echo -e "2|3\n q" | $gmx make_ndx -f prod.gro  

#..Re-center traj
echo "${host}_${guest} System" |\
$gmx trjconv -f prod.xtc -s prod.tpr -n index.ndx -o noPBC.xtc -pbc mol -ur compact -center

#..CLEAN
rm \#*
rm TMP
exit
