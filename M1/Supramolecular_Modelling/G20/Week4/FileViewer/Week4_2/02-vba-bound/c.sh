source ../config.h
source ../software.h

for np in 20000 40000 100000 200000; do
echo -e "\n $np"

FILE=$np.dhdl
if [ -f $FILE ]; then rm $FILE; fi
#..loop over lambda
for ll in 0.0001 0.001 0.01 0.1 0.2 0.5 1.0; do
#for ll in 0.001; do

#..ensemble-averaged dU/dl
cat $ll.vba | grep -v "#" | awk -v NP=$np '($1<=NP)' | awk -f ../awk/mean.awk -v col=3 | \
awk -v LAMBDA=$ll '{print("%12.7f %9.5f\n", LAMBDA, $2/LAMBDA)}' >> CV1
#
cat $ll.vba | grep -v "#" | awk -v NP=$np '($1<=NP)' | awk -f ../awk/mean.awk -v col=5 | \
awk -v LAMBDA=$ll '{print("%12.7f %9.5f\n", LAMBDA, $2/LAMBDA)}' >> CV2
#
cat $ll.vba | grep -v "#" | awk -v NP=$np '($1<=NP)' | awk -f ../awk/mean.awk -v col=7 | \
awk -v LAMBDA=$ll '{print("%12.7f %9.5f\n", LAMBDA, $2/LAMBDA)}' >> CV3
#
cat $ll.vba | grep -v "#" | awk -v NP=$np '($1<=NP)' | awk -f ../awk/mean.awk -v col=9 | \
awk -v LAMBDA=$ll '{print("%12.7f %9.5f\n", LAMBDA, $2/LAMBDA)}' >> CV4
#
cat $ll.vba | grep -v "#" | awk -v NP=$np '($1<=NP)' | awk -f ../awk/mean.awk -v col=11 | \
awk -v LAMBDA=$ll '{print("%12.7f %9.5f\n", LAMBDA, $2/LAMBDA)}' >> CV5
#
cat $ll.vba | grep -v "#" | awk -v NP=$np '($1<=NP)' | awk -f ../awk/mean.awk -v col=13 | \
awk -v LAMBDA=$ll '{print("%12.7f %9.5f\n", LAMBDA, $2/LAMBDA)}' >> CV6
#
done
done
exit

