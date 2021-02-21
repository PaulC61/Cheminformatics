#!/bin/bash

#..source
source ../config.h
source ../software.h

#..loop over lambda
for nn in 1 2 3 4 5 6 7; do

#..Re-center traj
echo "${host}_${guest} System" |\
$gmx trjconv -f $nn.xtc -s $nn.tpr -n index.ndx -o $nn-cnt.xtc -pbc mol -ur compact -center
done

#..Finish
exit
