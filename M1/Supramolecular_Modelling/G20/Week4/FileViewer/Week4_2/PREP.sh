#! /bin/bash

cd 00-bound/
pwd
./HOWTO_bound.sh >& ./OUT

cd ../00-unbound/
pwd
./HOWTO_guest.sh >& ./OUT

exit
