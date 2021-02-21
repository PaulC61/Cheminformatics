#!/bin/bash

#..SOURCE
source ../software.h
source ../config.h

#..00-bound
cp ../00-bound/cluster/store/ref-bnd.pdb ./
cp ../00-bound/cluster/store/refs.dat ./bound.dat
#
plumed driver --plumed bound.dat --mf_xtc ../00-bound/noPBC.xtc  
awk -f ~/Repository/awk/histo.awk -v col=2 -v MIN=0     -v MAX=0.03 -v NBIN=30  BOUND > rmsd-bnd.hh
awk -f ~/Repository/awk/histo.awk -v col=3 -v MIN=0.3   -v MAX=0.8  -v NBIN=50  BOUND > rr.hh
awk -f ~/Repository/awk/histo.awk -v col=4 -v MIN=0.0   -v MAX=2.0  -v NBIN=80  BOUND > tt.hh
awk -f ~/Repository/awk/histo.awk -v col=5 -v MIN=0.0   -v MAX=2.0  -v NBIN=80  BOUND > pp.hh
awk -f ~/Repository/awk/histo.awk -v col=6 -v MIN=0.0   -v MAX=3.14 -v NBIN=50  BOUND > TH.hh
awk -f ~/Repository/awk/histo.awk -v col=7 -v MIN=-3.14 -v MAX=3.14 -v NBIN=100 BOUND > PH.hh
awk -f ~/Repository/awk/histo.awk -v col=8 -v MIN=-3.14 -v MAX=3.14 -v NBIN=100 BOUND > PS.hh
#exit

#..00-unbound
cp ../00-bound/cluster/store/ref-bnd.pdb ./
#cp ../00-bound/cluster/store/refs.dat ./unbound.dat
#
plumed driver --plumed unbound.dat --mf_xtc ../00-unbound/noPBC.xtc
awk -f ~/Repository/awk/histo.awk -v col=2 -v MIN=0 -v MAX=0.03 -v NBIN=30 UNBND > rmsd-unb.hh
#exit

#..01-confine-bound
for ll in 0.0001 0.001 0.01 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0; do
awk -f ~/Repository/awk/histo.awk -v col=2 -v MIN=0 -v MAX=0.03 -v NBIN=30 ../01-confine-bound/$ll.rms > bnd-$ll.hh
done

#../02-vba-bound
for ll in 0.0001 0.001 0.01 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0; do
awk -f ~/Repository/awk/histo.awk -v col=2  -v MIN=0.3 -v MAX=0.8 -v NBIN=50 ../02-vba-bound/$ll.vba > rr-$ll.hh
awk -f ~/Repository/awk/histo.awk -v col=4  -v MIN=0.0 -v MAX=2.0  -v NBIN=80 ../02-vba-bound/$ll.vba > tt-$ll.hh
awk -f ~/Repository/awk/histo.awk -v col=6  -v MIN=0.0 -v MAX=2.0  -v NBIN=80 ../02-vba-bound/$ll.vba > pp-$ll.hh
awk -f ~/Repository/awk/histo.awk -v col=8  -v MIN=0.0 -v MAX=3.14 -v NBIN=50 ../02-vba-bound/$ll.vba > TH-$ll.hh
awk -f ~/Repository/awk/histo.awk -v col=10 -v MIN=-3.14 -v MAX=3.14 -v NBIN=100 ../02-vba-bound/$ll.vba > PH-$ll.hh
awk -f ~/Repository/awk/histo.awk -v col=12 -v MIN=-3.14 -v MAX=3.14 -v NBIN=100 ../02-vba-bound/$ll.vba > PS-$ll.hh
done
exit

#../04-confine-unbound/
for ll in 0.0001 0.001 0.01 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.0; do
awk -f ~/Repository/awk/histo.awk -v col=2 -v MIN=0 -v MAX=0.03 -v NBIN=30 ../04-confine-unbound/$ll.rms > unb-$ll.hh
done




exit
