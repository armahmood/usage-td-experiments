#!/bin/bash


for runseed in {1..5}
do
for alg in td totd utd utotd
do
time python pysrc/experiments/rndmdpexp.py 1000 $runseed results/rndmdp-experiments/state-10-ftype-binary/ $alg &

done

done



