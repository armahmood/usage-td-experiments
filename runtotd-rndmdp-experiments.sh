#!/bin/bash

for alg in td tdr totd
do
for runseed in {1..10}
do
		python pysrc/experiments/rndmdpexp.py 1000 $runseed results/totd-rndmdp-experiments/small-tabular/ $alg &
done
done
echo Invoking matplotlib plot for the experiment ...
python ./pysrc/plot/plotrndmdpexp.py
