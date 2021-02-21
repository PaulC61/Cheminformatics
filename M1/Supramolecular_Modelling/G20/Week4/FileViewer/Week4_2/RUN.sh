#! /bin/bash

#..01
#..modify SRC/plumed.tmpl
cd 01-confine-bound/
pwd
./HOWTO_confine.sh >& ./OUT

#..02
#..modify SRC/vba.tmpl
cd ../02-vba-bound/
pwd
./HOWTO_vba.sh >& ./OUT

#..03
cd ../03-alchemical-bound/
pwd
./HOWTO.sh >& OUT

#..04
#..modify SRC/plumed.tmpl
cd ../04-confine-unbound/
pwd
./HOWTO_confine.sh >& ./OUT

#..05
#..modify SRC/conf.dat
#..modify SRC/PROD.tmpl
cd ../05-alchemical-unbound/
pwd
./HOWTO.sh >& OUT

#..06
cd ../06-work-unbound/
pwd
./HOWTO_confine-UB.sh

#..07
cd ../07-summary/
pwd
./HOWTO_total.sh

