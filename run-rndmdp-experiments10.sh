#!/bin/bash


for runseed in {1..1}
do
for alg in tdr utdr td totd utd utotd
do
time python pysrc/experiments/rndmdpexp.py 1000 $runseed results/rndmdp-experiments/state-10-ftype-binary/ $alg &

done

done


echo "Invoking matplotlib plot for the experiment ..."
python ./pysrc/plot/plotrndmdpexp10.py

