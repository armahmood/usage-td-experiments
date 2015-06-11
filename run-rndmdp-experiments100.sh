#!/bin/bash


for runseed in {1..1}
do
for alg in td totd utd utotd tdr utdr
do
time python pysrc/experiments/rndmdpexp.py 1000 $runseed results/rndmdp-experiments/state-100-ftype-binary/ $alg &


done
done

echo "Invoking matplotlib plot for the experiment ..."
python ./pysrc/plot/plotrndmdpexp100.py
