#!/bin/bash


for runseed in {1..5}
do
#for alg in gtd togtd oislstd wislstd olstd2 wtd wgtd wtogtd
for alg in  olstd2 wtd  #gtd wtd wislstd olstd2 
do
time python pysrc/experiments/offrndmdpexp.py 1000 $runseed results/offpolicy-rndmdp-experiments/state-10-bpol-random-tpol-skewed-ftype-binary-test/ $alg &


done

done