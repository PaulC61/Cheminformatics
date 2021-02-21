#..local
srdir=./SRC

#..EVALUATE dH/dl
FILE="POS-ORIE.dhdl"
if [ -f $FILE ]; then rm $FILE; fi
#..loop over lambda
for ll in 0.0001 0.001 0.01 0.1 0.2 0.5 1.0; do

#..ensemble-averaged dU/dl 
cat $ll.vba | grep -v "#" | awk -f ../awk/mean.awk -v col=3 $ll.vba | \
awk -v LAMBDA=$ll '{printf("%12.7f %9.5f\n", LAMBDA, $2/LAMBDA)}' >> CV1
#
cat $ll.vba | grep -v "#" | awk -f ../awk/mean.awk -v col=5 $ll.vba | \
awk -v LAMBDA=$ll '{printf("%12.7f %9.5f\n", LAMBDA, $2/LAMBDA)}' >> CV2
#
cat $ll.vba | grep -v "#" | awk -f ../awk/mean.awk -v col=7 $ll.vba | \
awk -v LAMBDA=$ll '{printf("%12.7f %9.5f\n", LAMBDA, $2/LAMBDA)}' >> CV3
#
cat $ll.vba | grep -v "#" | awk -f ../awk/mean.awk -v col=9 $ll.vba | \
awk -v LAMBDA=$ll '{printf("%12.7f %9.5f\n", LAMBDA, $2/LAMBDA)}' >> CV4
#
cat $ll.vba | grep -v "#" | awk -f ../awk/mean.awk -v col=11 $ll.vba | \
awk -v LAMBDA=$ll '{printf("%12.7f %9.5f\n", LAMBDA, $2/LAMBDA)}' >> CV5
#
cat $ll.vba | grep -v "#" | awk -f ../awk/mean.awk -v col=13 $ll.vba | \
awk -v LAMBDA=$ll '{printf("%12.7f %9.5f\n", LAMBDA, $2/LAMBDA)}' >> CV6
#
done
paste CV* | awk '{printf("%12.7f %11.5f %11.5f %11.5f %11.5f %11.5f %11.5f\n", $1, $2, $4, $6, $8, $10, $12)}' > $FILE

#..INTEGRATE
awk -v VERBOSE=0 -f ../awk/multiCV_trapez.awk $FILE

#..Finish
rm CV*
exit
